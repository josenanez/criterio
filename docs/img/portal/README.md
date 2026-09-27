# Las capturas del portal

Estas imágenes **no las dibujó nadie**: son el portal corriendo sobre el corpus
sintético de [`tests/criterio-pmo/`](../../../tests/criterio-pmo/), con la fecha de
referencia fija en `2026-09-30`. «Banco del Ejemplo» y los seis proyectos `PRY-00x` son
material de prueba, no un cliente.

Se versionan para que la documentación se pueda leer sin correr nada, que es la misma
razón por la que se versionan las figuras de `docs/img/`.

## Cómo se reproducen

```
python3 tests/criterio-pmo/generar.py

mkdir -p /tmp/estado/records
cp tests/criterio-pmo/expected/fichas/*.json /tmp/estado/records/

python3 plugins/criterio-pmo/scripts/informe.py \
  --state /tmp/estado --salida /tmp/informe \
  --config <una configuración con organization.name> --today 2026-09-30

python3 plugins/criterio-pmo/scripts/servidor.py \
  --informe /tmp/informe --estado /tmp/estado --config <la misma>
```

Y después, la captura de cada página a **1240 px de ancho**, que es el que hace que las
tablas quepan sin comprimirse. Eso necesita un navegador, y por eso **no hay un script
aquí**: todo lo que este repositorio ejecuta corre con la librería estándar y sin
instalar nada, y un pipeline de capturas rompería esa propiedad por una comodidad.

| Archivo | Qué página es |
|---|---|
| `portada.png` | La portada que sirve el servidor, con las tres secciones |
| `informes-pmo.png` | `index.html` · cómo va el portafolio |
| `decisiones.png` | `decisiones.html` · lo que necesita una decisión del comité |
| `proyectos.png` | `proyectos.html` · el listado |
| `proyecto.png` | `PRY-002.html` · el informe de un proyecto |
| `productos.png` | `productos.html` · el listado |
| `producto.png` | `producto-cuenta-transaccional.html` · el informe de un producto |

## Cómo se sabe que envejecieron

Era un cabo suelto declarado: *«si cambia el diseño de las páginas, estas capturas
envejecen, y no hay nada que lo detecte solo»*. **Ya pasó**: siguieron diciendo que el
informe lo producía «Plomada» mucho después de que el agente se llamara Vera, y nadie lo
notó hasta que alguien miró la imagen.

Ahora [`captura.json`](captura.json) guarda la huella de `informe.py` y `servidor.py` del
momento en que se tomaron, y `tests/coherencia.py` compara. Cuando difieren lo dice:

```
Las capturas del portal
  nota  se tomaron con otra versión de informe.py · rehacerlas con docs/img/portal/README.md
```

**Es una nota y no una falla a propósito.** Volver a tomarlas necesita un navegador, y
hacer que la puerta verde dependa de un navegador rompería la propiedad que hace auditable
a este repositorio. Lo que se gana es que la podredumbre se vea, no que pare la corrida.
Después de rehacerlas, hay que actualizar `captura.json` con las huellas nuevas.
