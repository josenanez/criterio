# Rostrum en un servidor de la organización

[English](rostrum-en-servidor.md)

Rostrum es el portal de todas las familias: publica lo que escriben los agentes para quien no abre
una carpeta. Para mirarlo un rato basta `/criterio-server:server-start` en el equipo de quien lo
usa. **Esta guía es para que quede corriendo**, con un enlace estable que el patrocinador abre
mañana. Va dirigida a quien administra el servidor y a quien aprueba su publicación.

## Lo que pide, y lo que no

| Pide | Por qué |
|---|---|
| Un equipo de la red interna con Python 3.9 o superior | Rostrum usa solo la librería estándar de Python: no instala paquetes |
| Que ese equipo vea la carpeta de trabajo de los agentes | Lee el mapa y el estado que dejan los agentes. Escribe en un solo sitio: la carpeta `peticiones/` del agente a quien alguien le deja una pregunta |
| Un puerto | 8787 por omisión |
| Publicarlo detrás del control de acceso que la organización ya usa | **Rostrum no autentica, y es a propósito.** Un servidor sobre la librería estándar no va a autenticar mejor que el proxy de la organización |

**No pide** base de datos, salida a internet, certificado propio, cuenta de servicio con permisos ni
acceso al modelo de lenguaje (LLM): no corre ningún agente, solo sirve lo que ya escribieron.

## 1 · El mapa

El mapa dice qué agentes publica y dónde está su estado. Lo escribe `/criterio-server:server-setup`
en `.criterio/rostrum/config.json`, dentro de la carpeta de trabajo, y sus rutas son **relativas a
esa carpeta**. Por eso el servidor puede montar la carpeta compartida en cualquier ruta: lo único que
cambia es la que se le pasa a `--mapa`.

## 2 · El código, en una ruta que no cambia

No se apunta al código del plugin instalado: su ruta cambia con cada versión. Se clona el
repositorio en el servidor, en la versión vigente:

```
git clone --branch v2.2.0 https://github.com/josenanez/criterio /opt/criterio
```

Para actualizar, cada vez que haya una versión nueva —se publica los viernes—:

```
cd /opt/criterio && git fetch --tags && git checkout v<versión> && sudo systemctl restart rostrum
```

## 3 · Que arranque solo

Rostrum escucha en `127.0.0.1` y queda detrás del proxy, que es quien recibe a la red. En los ejemplos,
la carpeta de trabajo está montada en `/srv/criterio/trabajo`.

**Linux, con systemd** — `/etc/systemd/system/rostrum.service`:

```ini
[Unit]
Description=Rostrum, el portal de Criterio
After=network-online.target remote-fs.target

[Service]
User=rostrum
ExecStart=/usr/bin/python3 /opt/criterio/plugins/criterio-server/scripts/servidor.py --mapa /srv/criterio/trabajo/.criterio/rostrum/config.json --puerto 8787
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl enable --now rostrum
```

El usuario `rostrum` necesita leer la carpeta de trabajo y escribir en las carpetas `peticiones/` del
estado de cada agente, y nada más.

**macOS, con launchd** — `~/Library/LaunchAgents/com.criterio.rostrum.plist`, con la misma línea de
`ExecStart` en `ProgramArguments`, `RunAtLoad` y `KeepAlive` en `true`; se carga con
`launchctl load ~/Library/LaunchAgents/com.criterio.rostrum.plist`.

**Windows** — una tarea del Programador de tareas que corra al iniciar el equipo:
`python.exe C:\criterio\plugins\criterio-server\scripts\servidor.py --mapa <mapa> --puerto 8787`.

`/criterio-server:server-start`, en una sesión en el servidor, arma la versión exacta de cualquiera
de las tres con las rutas reales.

## 4 · Detrás del control de acceso

Rostrum se publica como cualquier aplicación interna. Con nginx, la parte que importa:

```nginx
location / {
    proxy_pass http://127.0.0.1:8787;
    proxy_set_header Host $host;
    # aquí va la autenticación que ya usa la organización: SSO, LDAP o la que sea
}
```

Si el proxy está en otro equipo, Rostrum tiene que escuchar fuera del suyo: se agrega `--abierto`,
que lo advierte al arrancar, y el firewall deja llegar solo al proxy.

## 5 · Comprobar que está bien

```
curl -s http://127.0.0.1:8787/estado.json
```

Dice de cuándo es lo de cada agente y cuántas peticiones tiene abiertas. Si un agente aparece sin
estado, todavía no ha corrido: Rostrum no inventa nada.

## Qué enlace se le pasa a quién

| Enlace | Para quién |
|---|---|
| `/` | Todos: los agentes del mapa y el formulario para dejarles una pregunta |
| `/resumen/<familia>` | La presidencia y el comité: el resumen ejecutivo de una familia en una página que se imprime |
| `/vence` | La gerencia: lo pendiente con fecha, de todas las familias |
| `/familia/<sigla>` | Quien responde por esa función |
| `/caso/<código>` | Quien pregunta por un proyecto, un producto o un contrato |

## Lo que Rostrum no hace

No calcula ni recalcula, no escribe ninguna ficha, no autentica y no envía nada. Una pregunta que
alguien deja en el formulario espera a que su agente corra su reloj
([decisión 0028](decisions/0028-el-setup-ofrece-el-reloj.md)); el servidor no puede correr un agente,
y eso es deliberado.
