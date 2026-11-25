---
name: marketing-intake
description: "Qué documentos procesa la familia CMO, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae el agente a la ficha. Úsalo al recorrer la carpeta de mercadeo de una entidad, al recibir una pieza, un soporte, las bases de una promoción, un registro de bases de contactos, un plan de mercadeo, unas facturas de pauta o una exportación de una plataforma, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Marketing office document intake, folder structure."
---
<!-- COPIA · la fuente es plugins/criterio-claims/skills/marketing-intake/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Los documentos del área de mercadeo

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** El registro de piezas, el registro de bases de contactos, el plan de mercadeo, las facturas de pauta y la exportación de resultados de la plataforma llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `mercadeo.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** Cada afirmación de una pieza con su soporte y cada promoción con su vigencia y sus condiciones —Lucía, con **claim-record**—; cada resultado del informe de mercadeo con su campaña, su indicador, su valor y su corte —Próspero, con **result-record**—. Se convierte con `mercadeo.py convertir` y se registra con su cita. El código no lo inventa ni lo infiere.

## Lo que nunca se procesa

**Ningún agente se conecta a una plataforma de pauta ni de analítica, y ninguno procesa los datos de una persona** (decisión 0036). Procesan exportaciones; de una base de contactos, solo su registro: cuántos registros tiene, con qué autorización y desde cuándo. Si llega una extracción con los datos de las personas, no se abre: se dice que llegó y que no se procesa.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes, en español, en portugués y en inglés:

| Tabla | Archivo, por lo que lleva su nombre | Columnas que necesita | Opcionales | En `columns` |
|---|---|---|---|---|
| El registro de piezas | `10-piezas/registro_de_piezas` | `pieza` | `nombre`, `canal`, `fecha_de_publicacion`, `fecha_de_aprobacion`, `aprobado_por`, `pagada_a_influenciador`, `identificada_como_publicidad`, `influenciador` | `piezas` |
| El registro de bases de contactos | `40-bases/registro_de_bases_de_contactos` | `base` | `registros`, `autorizacion_para_mercadeo`, `fecha_de_autorizacion`, `finalidad` | `bases` |
| El plan de mercadeo | `50-campanas/plan_de_mercadeo` | `campana` | `nombre`, `presupuesto`, `inicio`, `fin`, `meta`, `indicador`, `base_de_contactos` | `plan` |
| Las facturas de pauta | `50-campanas/facturas` | `factura`, `valor` | `campana`, `orden_de_compra`, `proveedor`, `fecha`, `pauta_hasta` | `facturas` |
| La exportación de la plataforma | `50-campanas/resultados_plataforma` | `campana`, `indicador`, `valor` | `corte` | `plataforma` |

Cuando una tabla llama una columna de otra forma, el motor dice cuál falta. **No adivines**: pregúntale a la persona cómo se llama y regístralo en `columns` de la configuración, por tabla.

## La estructura recomendada

<!-- cmo:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). La política tiene un solo lugar, `00-politica/`, y los dos agentes la usan: Lucía procesa cada pieza contra su soporte y su aprobación, y Próspero cada campaña contra su presupuesto y su resultado.

Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, la política de publicidad; las piezas aprobadas con su registro; los soportes de las afirmaciones; las bases de cada promoción; el registro de bases de contactos, y el plan de mercadeo con las facturas de pauta, la exportación de la plataforma y el informe de resultados.

```
mercadeo/
└── <entidad>/
    ├── 00-politica/
    ├── 10-piezas/
    ├── 20-soportes/
    ├── 30-promociones/
    ├── 40-bases/
    └── 50-campanas/
estado-mercadeo/
```

**`<entidad>/`** · Lo que el área de mercadeo lleva de la entidad

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-politica/` | La política de publicidad y de aprobación de piezas, con sus tolerancias | Lucía, Próspero |
| `10-piezas/` | Cada pieza aprobada con su texto y el registro de piezas: su canal, su fecha de publicación, su aprobación y si es pagada a un influenciador | Lucía |
| `20-soportes/` | Los soportes de cada afirmación: estudios, mediciones, certificados y comparativos | Lucía |
| `30-promociones/` | Las bases de cada promoción, con su vigencia y sus condiciones de modo y lugar | Lucía |
| `40-bases/` | El registro de bases de contactos: cada base con sus registros, su autorización para mercadeo y su fecha. Nunca los datos de una persona | Lucía |
| `50-campanas/` | El plan de mercadeo con el presupuesto, la meta y la base de cada campaña; las facturas de pauta; la exportación de la plataforma y el informe de resultados | Próspero, Lucía |

**`estado-mercadeo/`** · Lo que escriben Lucía y Próspero: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cmo:intake -->
