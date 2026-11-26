---
name: technology-intake
description: "Qué documentos procesa la familia CTO, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae el agente a la ficha. Úsalo al recorrer la carpeta de tecnología de una entidad, al recibir un catálogo de servicios, una exportación de cambios, un registro de despliegues, un acta del comité de cambios o de arquitectura, una exportación de incidentes o de problemas, un inventario, unas licencias, un contrato o unas facturas de un proveedor, o la factura de la nube, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Technology office document intake, folder structure."
---
<!-- COPIA · la fuente es plugins/criterio-changes/skills/technology-intake/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Los documentos del área de tecnología

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** El catálogo de servicios, la exportación de cambios, el registro de despliegues, los incidentes, los problemas, la disponibilidad, el inventario de activos, las licencias, el cumplimiento y las facturas de los proveedores, y la factura y el presupuesto de la nube llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `tecnologia.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** Cada aprobación de un cambio y cada revisión posterior que quedó en un acta del comité de cambios —Fausto, con **change-record**—; cada excepción aprobada sobre un activo sin soporte que quedó en un acta del comité de arquitectura y cada nivel de servicio de un contrato con su crédito —Domingo, con **vendor-record**—. Se convierte con `tecnologia.py convertir` y se registra con su cita. El código no lo inventa ni lo infiere.

## Lo que nunca se procesa

**Ningún agente se conecta a una herramienta de gestión del servicio, a la nube, a una herramienta de inventario ni a un servidor, y ninguno procesa la seguridad** (decisión 0037). Procesan exportaciones. Las vulnerabilidades, los controles y los incidentes de seguridad son de la familia CISO: si llegan a esta carpeta, se dice que llegaron y que son de otra familia.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes, en español, en portugués y en inglés:

| Tabla | Archivo, por lo que lleva su nombre | Columnas que necesita | Opcionales | En `columns` |
|---|---|---|---|---|
| El catálogo de servicios | `00-politica/catalogo_de_servicios` | `servicio` | `nombre`, `disponibilidad_acordada`, `dueno` | `catalogo` |
| La exportación de cambios | `10-cambios/cambios` | `cambio` | `tipo`, `fecha_de_implementacion`, `resultado`, `servicio`, `descripcion` | `cambios` |
| El registro de despliegues | `10-cambios/despliegues` | `despliegue` | `fecha`, `ambiente`, `cambio`, `sistema` | `despliegues` |
| Los incidentes | `20-servicio/incidentes` | `incidente` | `prioridad`, `incidente_mayor`, `servicio`, `fecha_de_solucion` | `incidentes` |
| Los problemas | `20-servicio/problemas` | `problema` | `incidente`, `causa`, `fecha_de_registro` | `problemas` |
| La disponibilidad del periodo | `20-servicio/disponibilidad` | `servicio`, `disponibilidad` | `periodo` | `disponibilidad` |
| El inventario de activos | `30-activos/inventario` | `activo` | `nombre`, `dueno`, `ambiente`, `fin_de_soporte` | `inventario` |
| Las licencias | `30-activos/licencias` | `software`, `licencias_compradas` | `licencias_en_uso` | `licencias` |
| El cumplimiento de los proveedores | `40-proveedores/cumplimiento` | `proveedor`, `valor` | `metrica`, `periodo` | `cumplimiento` |
| Las facturas de los proveedores | `40-proveedores/facturas` | `factura`, `proveedor` | `periodo`, `valor`, `credito` | `facturas` |
| La factura de la nube | `50-nube/factura_de_la_nube` | `cuenta`, `costo` | `periodo`, `servicio` | `nube` |
| El presupuesto de la nube | `50-nube/presupuesto_de_la_nube` | `cuenta`, `presupuesto` | `periodo` | `presupuesto_nube` |

Cuando una tabla llama una columna de otra forma, el motor dice cuál falta. **No adivines**: pregúntale a la persona cómo se llama y regístralo en `columns` de la configuración, por tabla.

## La estructura recomendada

<!-- cto:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). La política tiene un solo lugar, `00-politica/`, y los dos agentes la usan: Fausto procesa cada cambio contra su aprobación y cada servicio contra su nivel, y Domingo cada activo, cada licencia, cada proveedor y la nube.

Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, la política de cambios y de niveles de servicio con el catálogo de servicios; los cambios, los despliegues y las actas del comité de cambios; los incidentes, los problemas y la disponibilidad; el inventario de activos y las licencias; los contratos, el cumplimiento y las facturas de los proveedores, y la factura y el presupuesto de la nube.

```
tecnologia/
└── <entidad>/
    ├── 00-politica/
    ├── 10-cambios/
    ├── 20-servicio/
    ├── 30-activos/
    ├── 40-proveedores/
    └── 50-nube/
estado-tecnologia/
```

**`<entidad>/`** · Lo que el área de tecnología lleva de la entidad

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-politica/` | La política de cambios y de niveles de servicio, con sus plazos y umbrales, y el catálogo de servicios con el nivel acordado de cada uno | Fausto, Domingo |
| `10-cambios/` | La exportación de cambios de la herramienta de gestión del servicio, el registro de despliegues en producción y las actas del comité de cambios | Fausto |
| `20-servicio/` | Las exportaciones de incidentes y de problemas, y la disponibilidad de cada servicio en el periodo | Fausto |
| `30-activos/` | El inventario de activos con su dueño, su ambiente y su fin de soporte; las licencias compradas y su uso, y las actas del comité de arquitectura con sus excepciones | Domingo |
| `40-proveedores/` | Los contratos de nivel de servicio de cada proveedor, el cumplimiento que reporta y sus facturas | Domingo |
| `50-nube/` | La factura de la nube por cuenta y el presupuesto de cada cuenta | Domingo |

**`estado-tecnologia/`** · Lo que escriben Fausto y Domingo: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cto:intake -->
