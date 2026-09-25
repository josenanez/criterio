#!/usr/bin/env python3
"""Criterio PMO — el servidor.

    python3 servidor.py --informe <carpeta> --estado <estado> [--puerto 8787]
                        [--host 127.0.0.1] [--abierto] [--selftest]

Sirve el informe que `informe.py` ya produjo, y recibe peticiones para el agente.
Librería estándar, sin dependencias.

**El servidor no calcula nada y no escribe ninguna ficha.** Es una proyección: lo
que muestra ya estaba escrito en disco antes de que alguien abriera el navegador.
Esa es la razón de que exista como pieza aparte y no como un modo del agente. Un
servidor que calculara al vuelo tendría que leer documentos, y entonces dos
personas abriendo la misma página verían dos portafolios distintos.

Lo único que escribe es la cola de peticiones, en `<estado>/peticiones/`, que es
una carpeta suya. El agente la lee cuando despierta. Nadie del otro lado de la
pantalla puede tocar un dato del portafolio: **el camino de escritura hacia la
ficha no existe en este archivo.**

## Sobre el acceso

**Este servidor no autentica a nadie, y es deliberado.** Un servidor de cien
líneas sobre la librería estándar no va a autenticar mejor que el proxy que el
banco ya tiene, y prometer que sí es exactamente lo que este plugin no hace.

Por eso escucha solo en `127.0.0.1` salvo que se le pase `--abierto`, y cuando se
le pasa lo dice en voz alta. Publicarlo se hace como se publica cualquier cosa
adentro: detrás de lo que la organización ya usa para eso.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.parse
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import informe  # la paleta y la página son suyas; aquí no se vuelven a escribir

TOPE_PETICION = 16 * 1024          # una petición es un párrafo, no un adjunto

# Las rutas, declaradas y no solo implícitas en el `if` de abajo. Se declaran porque
# se parecen a comandos —`/decisiones` es una ruta, no un `/comando`— y el verificador
# del repositorio necesita poder distinguirlas sin que nadie le escriba una excepción.
RUTAS = {
    '/': 'la portada: las dos vistas, la frescura y el formulario de peticiones',
    '/decisiones': 'lo que necesita una decisión · para el comité',
    '/interna': 'el portafolio campo por campo · para quien va a actuar',
    '/p/<codigo>': 'la página de un proyecto',
    '/estado.json': 'de cuándo es el informe y cuántas peticiones hay abiertas',
    '/peticion': 'POST · deja una pregunta escrita para el agente',
}
ASUNTOS = {
    'revisar': 'Que revise un proyecto contra sus documentos',
    'explicar': 'Que explique de dónde salió un dato del informe',
    'corregir': 'Que algo del informe no coincide con lo que sé',
    'otra': 'Otra cosa',
}

EXTRA = f"""
.portada h1{{margin-bottom:.15em}}
.puertas{{display:flex;flex-wrap:wrap;gap:16px;margin:30px 0 0}}
.puerta{{flex:1 1 320px;border:1px solid {informe.FILETE};border-radius:10px;
  padding:22px 24px;background:{informe.PANEL_ALTO};display:block;
  border-bottom:1px solid {informe.FILETE};color:inherit}}
.puerta:hover{{border-color:{informe.ORO}}}
.puerta .q{{display:block;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;
  color:{informe.ORO};font-weight:600}}
.puerta .t{{display:block;font-size:1.2rem;color:{informe.TINTA};font-weight:500;
  margin:.35em 0 .3em;line-height:1.25}}
.puerta .d{{font-size:.93rem;color:{informe.APAGADO};margin:0}}
form.pide{{margin:14px 0 0;max-width:660px}}
form.pide .par{{display:flex;flex-wrap:wrap;gap:0 18px}}
form.pide .par > div{{flex:1 1 220px}}
label{{display:block;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;
  color:{informe.APAGADO};font-weight:600;margin:16px 0 5px}}
input,select,textarea{{width:100%;padding:10px 12px;border:1px solid {informe.FILETE};
  border-radius:6px;background:#fff;color:{informe.CUERPO};font:inherit;font-size:.95rem}}
input:focus,select:focus,textarea:focus{{outline:2px solid {informe.ORO};outline-offset:-1px}}
textarea{{min-height:110px;resize:vertical}}
button{{margin-top:20px;padding:11px 24px;border:1px solid {informe.ORO};border-radius:6px;
  background:{informe.ORO};color:{informe.CREMA};font:inherit;font-weight:600;cursor:pointer}}
button:hover{{background:{informe.TINTA};border-color:{informe.TINTA}}}
.aviso{{font-size:.88rem;color:{informe.APAGADO};margin:.6em 0 0;max-width:660px}}
@media print{{.puertas,form.pide{{display:none}}}}
"""


def e(x):
    return html.escape(str(x if x is not None else ''))


def pagina(titulo, cuerpo, hoy, nav=''):
    """La página del informe, con lo que solo el servidor necesita."""
    p = informe.pagina(titulo, cuerpo, hoy, nav)
    return p.replace('</style>', EXTRA + '</style>', 1)


# ---------------------------------------------------------------- la cola

def buzon(estado: Path) -> Path:
    return estado / 'peticiones'


def guardar_peticion(estado: Path, datos: dict) -> dict:
    """Escribe una petición y nada más. El agente la lee cuando despierta."""
    carpeta = buzon(estado)
    carpeta.mkdir(parents=True, exist_ok=True)
    ahora = dt.datetime.now(dt.timezone.utc)
    registro = {
        'id': ahora.strftime('%Y%m%d-%H%M%S-') + uuid.uuid4().hex[:6],
        'recibida': ahora.isoformat(timespec='seconds'),
        'asunto': datos.get('asunto') or 'otra',
        'proyecto': (datos.get('proyecto') or '').strip()[:40] or None,
        'de': (datos.get('de') or '').strip()[:80] or None,
        'texto': (datos.get('texto') or '').strip()[:4000],
        'respondida': None,
    }
    (carpeta / f"{registro['id']}.json").write_text(
        json.dumps(registro, ensure_ascii=False, indent=2), encoding='utf-8')
    return registro


def pendientes(estado: Path) -> list:
    salida = []
    for f in sorted(buzon(estado).glob('*.json')):
        try:
            r = json.loads(f.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            continue
        if not r.get('respondida'):
            salida.append(r)
    return salida


# ---------------------------------------------------------------- frescura

def frescura(informe_dir: Path, estado: Path) -> dict:
    """De cuándo es lo que se está mirando. Sin esto, nadie sabe si el informe
    es de hoy o de hace tres semanas, y un informe viejo sin fecha miente."""
    portada = informe_dir / 'index.html'
    generado = None
    if portada.exists():
        generado = dt.datetime.fromtimestamp(
            portada.stat().st_mtime, dt.timezone.utc).isoformat(timespec='seconds')
    cad = estado / 'cadencia.json'
    proximo = None
    if cad.exists():
        try:
            proximo = json.loads(cad.read_text(encoding='utf-8')).get('next_wake')
        except (json.JSONDecodeError, OSError):
            pass
    paginas = sorted(p.stem for p in informe_dir.glob('PRY-*.html'))
    return {'informe_generado': generado, 'proxima_corrida': proximo,
            'proyectos': paginas, 'peticiones_abiertas': len(pendientes(estado))}


def edad(iso, ahora=None):
    if not iso:
        return None
    ahora = ahora or dt.datetime.now(dt.timezone.utc)
    try:
        return (ahora - dt.datetime.fromisoformat(iso)).days
    except ValueError:
        return None


# ---------------------------------------------------------------- las páginas

def portada(fr: dict, hoy: str) -> str:
    dias = edad(fr.get('informe_generado'))
    if fr.get('informe_generado') is None:
        sello = ('<strong>Todavía no hay informe.</strong> Alguien tiene que correr '
                 '<code>/portfolio-report html</code> antes de que esto muestre algo.')
    elif dias and dias > 7:
        sello = (f"El informe que se sirve aquí se produjo hace "
                 f"<strong>{informe.plural(dias, 'día', 'días')}</strong>. "
                 f"No se recalcula al abrir esta página: lo que ves es de esa fecha.")
    else:
        sello = (f"El informe que se sirve aquí se produjo "
                 f"{'hoy' if not dias else 'hace ' + informe.plural(dias, 'día', 'días')}. "
                 f"No se recalcula al abrir esta página.")
    prox = fr.get('proxima_corrida')
    if prox:
        sello += f" La próxima corrida del agente es el <strong>{e(prox)}</strong>."

    abiertas = fr.get('peticiones_abiertas') or 0
    cola = ''
    if abiertas:
        cola = (f'<p class="aviso">Hay {informe.plural(abiertas, "petición sin responder", "peticiones sin responder")}. '
                f'El agente las toma en su próxima corrida.</p>')

    opciones = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in ASUNTOS.items())
    cuerpo = f"""<div class="portada">
<span class="ante">Portafolio de proyectos</span>
<h1>Qué dicen los documentos</h1>
<p class="pie-cab">{sello}</p>

<div class="puertas">
  <a class="puerta" href="/decisiones">
    <span class="q">Para el comité</span>
    <span class="t">Lo que necesita una decisión</span>
    <p class="d">Solo lo que excede la facultad de quien gerencia cada proyecto, como
    pregunta cerrada y con la consecuencia de no decidir. Si no hay nada que decidir,
    lo dice.</p>
  </a>
  <a class="puerta" href="/interna">
    <span class="q">Para quien va a actuar</span>
    <span class="t">El portafolio, campo por campo</span>
    <p class="d">Cada dato con la cita del documento del que salió y su fecha, para que
    se pueda abrir y verificar. Una página por proyecto.</p>
  </a>
</div>

<h2>Pedirle algo al agente</h2>
<p>Esto no le contesta ahora: <strong>deja la pregunta escrita</strong> y el agente la
toma en su próxima corrida. Sirve para lo que el informe no alcanza a responder —
por qué un dato dice lo que dice, o que algo no coincide con lo que tú sabes.</p>
{cola}
<form class="pide" method="post" action="/peticion">
  <label for="asunto">De qué se trata</label>
  <select id="asunto" name="asunto">{opciones}</select>
  <div class="par">
    <div><label for="proyecto">Proyecto, si aplica</label>
      <input id="proyecto" name="proyecto" placeholder="PRY-001" maxlength="40"></div>
    <div><label for="de">Quién pregunta</label>
      <input id="de" name="de" placeholder="Tu nombre" maxlength="80"></div>
  </div>
  <label for="texto">Qué necesitas</label>
  <textarea id="texto" name="texto" maxlength="4000"
    placeholder="Escríbelo como se lo dirías a la persona de la PMO."></textarea>
  <button type="submit">Dejar la petición</button>
</form>
<p class="aviso"><strong>Esta página no pide contraseña</strong>, así que quien pregunta
es quien dice ser y nada más. No escribas aquí nada que no pondrías en un correo
interno.</p>
</div>"""
    return pagina('Portafolio de proyectos', cuerpo, hoy)


def recibida(registro: dict, hoy: str) -> str:
    cuerpo = f"""<span class="ante">Petición recibida</span>
<h1>Queda anotada</h1>
<p class="pie-cab">{e(registro['id'])}</p>
<div class="bloque info">
<h3>Qué pasa ahora</h3>
<p>El agente la lee en su próxima corrida. <strong>No hay nadie del otro lado
respondiendo en este momento</strong>, y decirlo es más honesto que un «en breve
te contactamos».</p>
<p>Si es urgente, el camino sigue siendo el de siempre: la persona de la PMO.</p>
</div>
<div class="decision"><p class="p">{e(ASUNTOS.get(registro['asunto'], registro['asunto']))}</p>
<dl><dt>Proyecto</dt><dd>{e(registro['proyecto'] or '—')}</dd>
<dt>Quién pregunta</dt><dd>{e(registro['de'] or 'no lo dijo')}</dd>
<dt>Qué necesita</dt><dd>{e(registro['texto']) or '<em>en blanco</em>'}</dd></dl></div>"""
    return pagina('Petición recibida', cuerpo, hoy,
                  '<div class="nav"><a href="/">← Volver al portafolio</a></div>')


def error(codigo: int, que: str, hoy: str) -> str:
    cuerpo = f"""<span class="ante">{codigo}</span>
<h1>{e(que)}</h1>
<p class="pie-cab">Este servidor solo sirve el informe que ya se produjo. No busca
nada más ni ejecuta nada.</p>"""
    return pagina(f'{codigo}', cuerpo, hoy, '<div class="nav"><a href="/">← Portafolio</a></div>')


# ---------------------------------------------------------------- el servidor

SEGURO = re.compile(r'^[A-Za-z0-9._-]+$')


class Manejador(BaseHTTPRequestHandler):
    server_version = 'criterio-pmo'
    sys_version = ''
    informe_dir: Path = Path('.')
    estado: Path = Path('.')
    callado: bool = False

    # --- utilidades -----------------------------------------------------
    def log_message(self, formato, *args):   # una línea por visita, sin ruido
        if not self.callado:
            sys.stderr.write(f"{self.address_string()} · {formato % args}\n")

    def responder(self, codigo, cuerpo: bytes, tipo='text/html; charset=utf-8'):
        self.send_response(codigo)
        self.send_header('Content-Type', tipo)
        self.send_header('Content-Length', str(len(cuerpo)))
        # El informe lleva datos de proyectos. Que no se quede en caches intermedios.
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(cuerpo)

    def html(self, codigo, texto):
        self.responder(codigo, texto.encode('utf-8'))

    def hoy(self):
        return dt.date.today().isoformat()

    def archivo(self, nombre):
        """Sirve un archivo del informe, y solo del informe."""
        if not SEGURO.match(nombre):
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            return
        ruta = (self.informe_dir / nombre).resolve()
        raiz = self.informe_dir.resolve()
        if raiz not in ruta.parents or not ruta.is_file():
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            return
        self.responder(200, ruta.read_bytes())

    # --- rutas ----------------------------------------------------------
    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        ruta = urllib.parse.urlparse(self.path).path.rstrip('/') or '/'
        if ruta == '/':
            self.html(200, portada(frescura(self.informe_dir, self.estado), self.hoy()))
        elif ruta == '/decisiones':
            self.archivo('decisiones.html')
        elif ruta == '/interna':
            self.archivo('index.html')
        elif ruta.startswith('/p/'):
            self.archivo(ruta[3:] + '.html')
        elif ruta == '/estado.json':
            cuerpo = json.dumps(frescura(self.informe_dir, self.estado),
                                ensure_ascii=False, indent=2).encode('utf-8')
            self.responder(200, cuerpo, 'application/json; charset=utf-8')
        else:
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))

    def do_POST(self):
        ruta = urllib.parse.urlparse(self.path).path.rstrip('/') or '/'
        if ruta != '/peticion':
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            return
        try:
            largo = int(self.headers.get('Content-Length') or 0)
        except ValueError:
            largo = -1
        if largo < 0 or largo > TOPE_PETICION:
            self.html(413, error(413, 'Eso es demasiado largo para una petición',
                                 self.hoy()))
            return
        crudo = self.rfile.read(largo).decode('utf-8', 'replace')
        campos = {k: v[0] for k, v in urllib.parse.parse_qs(crudo).items()}
        registro = guardar_peticion(self.estado, campos)
        self.html(200, recibida(registro, self.hoy()))


def arrancar(informe_dir: Path, estado: Path, host: str, puerto: int) -> int:
    Manejador.informe_dir = informe_dir
    Manejador.estado = estado
    buzon(estado).mkdir(parents=True, exist_ok=True)
    fr = frescura(informe_dir, estado)

    if fr['informe_generado'] is None:
        print('Aviso: no hay informe en esa carpeta. La portada lo va a decir.\n'
              '       Corre primero:  /portfolio-report html\n')

    with ThreadingHTTPServer((host, puerto), Manejador) as srv:
        real = srv.server_address[1]
        print(f'Criterio PMO · sirviendo {informe_dir}')
        print(f'  Portafolio      http://{host}:{real}/')
        print(f'  Comité          http://{host}:{real}/decisiones')
        print(f'  Interna         http://{host}:{real}/interna')
        print(f'  Frescura        http://{host}:{real}/estado.json')
        if host not in ('127.0.0.1', 'localhost', '::1'):
            print()
            print('  ATENCIÓN: escuchando fuera de este equipo y SIN AUTENTICACIÓN.')
            print('  Cualquiera que alcance este puerto ve el portafolio completo.')
            print('  Publícalo únicamente detrás del control de acceso de tu organización.')
        print('\n  Ctrl-C para parar. No escribe ninguna ficha.\n')
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print('\nParado.')
    return 0


# ---------------------------------------------------------------- comprobarse

def selftest() -> int:
    """Lo que este servidor puede romper sin que nadie lo note.

    Dos cosas, y ninguna se ve mirando la pantalla: que sirva un archivo que no
    es del informe, y que la cola de peticiones toque algo que no es suyo.
    """
    import http.client
    import tempfile
    import threading

    fallas = []

    def ok(que, real, esperado):
        if real != esperado:
            fallas.append(f'{que}: {real!r} en vez de {esperado!r}')
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}')

    tmp = Path(tempfile.mkdtemp())
    inf, est = tmp / 'informe', tmp / 'estado'
    inf.mkdir(); (est / 'records').mkdir(parents=True)
    (inf / 'index.html').write_text('<h1>interna</h1>', encoding='utf-8')
    (inf / 'decisiones.html').write_text('<h1>decisiones</h1>', encoding='utf-8')
    (inf / 'PRY-001.html').write_text('<h1>uno</h1>', encoding='utf-8')
    (est / 'records' / 'PRY-001.json').write_text('{"identity":{}}', encoding='utf-8')
    (tmp / 'secreto.txt').write_text('no debe salir', encoding='utf-8')

    Manejador.informe_dir, Manejador.estado, Manejador.callado = inf, est, True
    srv = ThreadingHTTPServer(('127.0.0.1', 0), Manejador)
    hilo = threading.Thread(target=srv.serve_forever, daemon=True); hilo.start()
    puerto = srv.server_address[1]

    def pedir(ruta, metodo='GET', cuerpo=None):
        c = http.client.HTTPConnection('127.0.0.1', puerto, timeout=5)
        cab = {'Content-Type': 'application/x-www-form-urlencoded'} if cuerpo else {}
        c.request(metodo, ruta, cuerpo, cab)
        r = c.getresponse(); datos = r.read().decode('utf-8', 'replace'); c.close()
        return r.status, datos

    try:
        ok('la portada responde', pedir('/')[0], 200)
        ok('la portada nombra las dos vistas',
           all(x in pedir('/')[1] for x in ('/decisiones', '/interna')), True)
        ok('la vista de comité se sirve', pedir('/decisiones')[1].strip(), '<h1>decisiones</h1>')
        ok('la vista interna se sirve', pedir('/interna')[1].strip(), '<h1>interna</h1>')
        ok('la página de un proyecto se sirve', pedir('/p/PRY-001')[1].strip(), '<h1>uno</h1>')

        # Lo de arriba lo ve cualquiera. Esto no.
        ok('no se sale de la carpeta con ..', pedir('/p/../../secreto')[0], 404)
        ok('no se sale con una ruta absoluta', pedir('/p//etc/hostname')[0], 404)
        ok('no sirve un archivo que no es del informe', pedir('/p/secreto')[0], 404)
        ok('una ruta inventada es 404', pedir('/administrar')[0], 404)
        ok('no acepta POST en otra ruta', pedir('/interna', 'POST', 'x=1')[0], 404)

        est_json = json.loads(pedir('/estado.json')[1])
        ok('la frescura dice qué proyectos hay', est_json['proyectos'], ['PRY-001'])
        ok('la frescura dice de cuándo es el informe',
           est_json['informe_generado'] is not None, True)

        antes = (est / 'records' / 'PRY-001.json').read_text(encoding='utf-8')
        cod, cuerpo = pedir('/peticion', 'POST',
                            urllib.parse.urlencode({'asunto': 'explicar',
                                                    'proyecto': 'PRY-001',
                                                    'de': 'Quien sea',
                                                    'texto': '¿De dónde sale el verde?'}))
        ok('la petición se acepta', cod, 200)
        ok('la petición se confirma en pantalla', 'Queda anotada' in cuerpo, True)
        ok('la petición quedó en la cola', len(pendientes(est)), 1)
        ok('la ficha NO cambió', (est / 'records' / 'PRY-001.json').read_text(encoding='utf-8'), antes)
        ok('la cola vive en su propia carpeta', buzon(est).name, 'peticiones')

        grande = urllib.parse.urlencode({'texto': 'x' * (TOPE_PETICION + 100)})
        ok('una petición enorme se rechaza', pedir('/peticion', 'POST', grande)[0], 413)
        ok('y no entró en la cola', len(pendientes(est)), 1)

        # Que la tabla de rutas y el `if` digan lo mismo. Una ruta declarada y no
        # servida sale en el README como una promesa que devuelve 404.
        vivas = []
        for r in RUTAS:
            if r == '/peticion':
                continue
            prueba = '/p/PRY-001' if r.startswith('/p/') else r
            if pedir(prueba)[0] == 200:
                vivas.append(r)
        ok('todas las rutas declaradas responden', sorted(vivas),
           sorted(set(RUTAS) - {'/peticion'}))

        ok('el escape impide inyectar en la confirmación',
           '<script>' not in pedir('/peticion', 'POST',
                                   urllib.parse.urlencode({'de': '<script>x</script>'}))[1], True)
    finally:
        srv.shutdown(); srv.server_close()

    print()
    if fallas:
        print(f'{len(fallas)} falla(s)')
        return 1
    print('todo pasa')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description='Criterio PMO — el servidor del informe.')
    ap.add_argument('--informe', type=Path, help='carpeta que produjo informe.py')
    ap.add_argument('--estado', type=Path, help='carpeta de estado del agente')
    ap.add_argument('--puerto', type=int, default=8787)
    ap.add_argument('--host', default=None,
                    help='por defecto 127.0.0.1; con --abierto, 0.0.0.0')
    ap.add_argument('--abierto', action='store_true',
                    help='escuchar fuera de este equipo. SIN AUTENTICACIÓN: solo '
                         'detrás del control de acceso de tu organización')
    ap.add_argument('--selftest', action='store_true')
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.informe or not args.estado:
        ap.error('--informe y --estado son obligatorios (o usa --selftest)')
    if not args.estado.exists():
        ap.error(f'no existe la carpeta de estado: {args.estado}')

    host = args.host or ('0.0.0.0' if args.abierto else '127.0.0.1')
    try:
        return arrancar(args.informe, args.estado, host, args.puerto)
    except OSError as err:
        print(f'No se pudo levantar en {host}:{args.puerto} — {err}', file=sys.stderr)
        if getattr(err, 'errno', None) in (48, 98, 10048):
            print('Ese puerto ya está ocupado. Prueba con --puerto 8788.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
