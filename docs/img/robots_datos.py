#!/usr/bin/env python3
"""El trazo de cada robot, como SVG animado y como datos, para quien lo dibuja fuera de Rostrum.

    python3 docs/img/robots_datos.py            escribe docs/img/robots/<robot>.svg y robots.json
    python3 docs/img/robots_datos.py --check    falla si no son lo que sale de robots.py

Sale de plugins/criterio-server/scripts/robots.py, el dueño de cada robot y de su gesto. El SVG se
mueve igual en un README, en el portal y en Rostrum; robots.json lo usa la impresora del portal, que
dibuja el robot con su propio marcado. Va aparte de graficos.py porque no necesita fuentes ni Pillow,
y así la verificación comprueba que el portal no publique un robot viejo.
"""
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'plugins', 'criterio-server', 'scripts'))
import robots as trazos  # noqa: E402

ORO = '#d5a84b'   # el de graficos.py y docs/design.md
CARPETA = os.path.join(AQUI, 'robots')


def archivos() -> dict[str, str]:
    nombres = (trazos.ORDEN + trazos.ORDEN_CFO + trazos.ORDEN_CLO + trazos.ORDEN_EA + trazos.ORDEN_CCO
               + trazos.ORDEN_CISO + trazos.ORDEN_CHRO + trazos.ORDEN_CAE + trazos.ORDEN_CDO)
    salida = {f'{n}.svg': trazos.svg(n, ORO, ORO, animado=True) + '\n' for n in nombres}
    salida['robots.json'] = json.dumps(trazos.datos(), ensure_ascii=False, indent=1) + '\n'
    return salida


def main() -> int:
    if '--check' in sys.argv:
        malos = [n for n, texto in archivos().items()
                 if not os.path.isfile(os.path.join(CARPETA, n))
                 or open(os.path.join(CARPETA, n), encoding='utf-8').read() != texto]
        if malos:
            print(f'docs/img/robots/ no es lo que sale de robots.py ({", ".join(malos)}): corre docs/img/robots_datos.py')
            return 1
        print('los robots de docs/img/robots/ salen de robots.py')
        return 0
    os.makedirs(CARPETA, exist_ok=True)
    for n, texto in archivos().items():
        with open(os.path.join(CARPETA, n), 'w', encoding='utf-8') as fh:
            fh.write(texto)
    print(f'docs/img/robots/ · {len(archivos())} archivos')
    return 0


if __name__ == '__main__':
    sys.exit(main())
