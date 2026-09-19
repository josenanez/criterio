# criterio-pmo

**Oficina de proyectos.** Lee la documentación que tu PMO ya tiene y dice qué cambió, qué se contradice y qué lleva semanas en silencio.

No existe un plugin de PMO aguas arriba. Lo más cercano es `product-management`, y es gestión de producto: asume un equipo, un producto, un backlog. Una PMO corre un portafolio.

> Esto produce borradores de trabajo, no decisiones. Ver [TERMS.es.md](../../TERMS.es.md) y [ACCEPTANCE.md](ACCEPTANCE.md).

---

## El problema que resuelve

El problema de una PMO no es que le falten plantillas. Es que **nadie ha leído junta la documentación que ya existe**: cuarenta proyectos, actas, cronogramas, minutas, correos y hojas de cálculo que nadie ha cruzado.

De ahí salen los hallazgos que ninguna herramienta da hoy: el hito que venció sin evidencia, el proyecto que reporta verde y lleva cinco semanas sin un documento, la minuta que nombra a un patrocinador distinto del acta, la dependencia que un plan declara y el otro ignora.

## Cómo funciona

La espina es la **ficha de proyecto**: un contrato de datos que todos los comandos leen y escriben, con cita al documento fuente y a su fecha en cada campo. Ningún comando lee documentos crudos por su cuenta.

Eso permite tres cosas: consolidar cuarenta proyectos sin volver a leerlos, **calcular en vez de opinar**, y comparar una corrida contra la anterior para decir qué cambió.

Dos principios que no se negocian:

**El modelo extrae; el script calcula.** Leer una fecha es lectura. Restar días, proyectar desviación y sumar ejecutado contra comprometido es aritmética, y la aritmética va en [`scripts/pmo.py`](scripts/pmo.py), sin dependencias y con su propia verificación:

```
python3 scripts/pmo.py selftest
```

**Todo dato lleva su cita o declara que no está.** "No está dicho en ninguna parte" es un hallazgo válido y esperado. Sin trazabilidad no se defiende ante un comité.

## Comandos

| Comando | Qué hace |
|---|---|
| `/portfolio-scan` | Lee la carpeta de documentación y produce o actualiza una ficha por proyecto. Puerta de entrada |
| `/portfolio-report` | Informe consolidado: qué cambió, qué se contradice, qué está en silencio, qué no tiene sustento |
| `/status-report` | Estado de un proyecto, separando lo que el gerente declara de lo que sustentan los documentos |
| `/steering-pack` | Material de comité como paquete de decisiones, no como informe de avance |
| `/raid-log` | Riesgos, supuestos, incidencias y dependencias, incluidos los que se dijeron en reuniones y nadie registró |
| `/change-control` | Evalúa un cambio en alcance, tiempo y costo, y crea línea base nueva sin borrar la anterior |
| `/vendor-tracking` | Entregables contractuales contra avance real y contra facturación |
| `/budget-tracking` | Aprobado, comprometido, ejecutado y proyección, con desviación contra las dos líneas base |
| `/project-charter` | Revisa o redacta el acta, señalando qué falta y qué consecuencia tiene |
| `/project-closure` | Cierra contra el criterio de éxito pactado, con lecciones que se puedan sustentar |

## Skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten.

| Skill | Qué encapsula |
|---|---|
| `project-record` | La ficha: esquema, reglas de extracción, citación, estados de campo, qué hacer cuando dos documentos se contradicen |
| `portfolio-health` | Semáforo con evidencia, umbrales por defecto, y las tres defensas contra el dato que dejó de ser cierto |
| `baseline-variance` | Línea base de solo agregar, desviación contra la original y contra la vigente, las cuatro cifras de presupuesto |
| `raid-taxonomy` | Las cuatro categorías y cómo distinguirlas, valoración, criterio de escalamiento |
| `commitment-tracking` | Compromisos dichos en reuniones: extracción, estados, qué cuenta como evidencia |
| `governance-artifacts` | Acta, comité, control de cambios y cierre: qué contiene cada uno y quién decide qué |

## Sin contenido regulatorio

La gestión de portafolio es método, no normativa: funciona igual en Bogotá que en Santiago. Si una obligación regulatoria toca un proyecto, este plugin la registra como restricción o como riesgo, y no opina sobre ella.

## Fuera de alcance, y por qué

**Capacidad y asignación de recursos**, y **materialización de beneficios**. No por poco importantes: porque los datos no están en la carpeta. Capacidad exige horas reales y beneficios exige medición posterior que casi ninguna organización tiene.

Un skill que promete lo que el insumo no permite quema la credibilidad del plugin entero.

## Criterios de aceptación

En [ACCEPTANCE.md](ACCEPTANCE.md). Nada se publica hasta que pasen sobre el set de prueba sintético.
