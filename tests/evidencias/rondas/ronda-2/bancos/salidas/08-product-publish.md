# /criterio-product:product-publish 

No publiqué la ficha de PRD-303 (Cuenta PyME): la configuración no tiene una carpeta de productos publicados. `config.json` solo declara `documents` y `state`. Sin ese sitio común no hay dónde escribir, y acordarlo es una conversación de la organización. No lo inventé: no escribí ninguna ficha, solo el registro de la corrida.

**Términos:** estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hizo falta registrar una aceptación nueva.

**Lo que habría llevado la ficha, con corte al 2026-10-15:**
- **Requerimientos:** 5 (REQ-1030, REQ-1031, REQ-1032, REQ-1033 y REQ-2018), todos «aceptado» y ninguno con proyecto asignado.
- **Proyectos:** 0.
- **Métricas afirmadas:** 1. Es `volumen_mensual`, declarada en 276747.0 en `documentos/productos/PRD-303/00-definicion/2026-02-02-caso-de-negocio.md`, tabla «Cifras que sostienen el caso».
- **Segmento declarado:** Segmento Empresas.
- **Gerente:** Beatriz Cuéllar.

La ficha no habría incluido la cifra medida (246553.0 al 2026-10-09, 10.9 % por debajo de lo declarado), porque las series medidas no se publican.

**Para publicar:** defina la carpeta común de productos publicados (por ejemplo `productos/publicados/`), regístrela en la configuración y vuelva a correr `/product-publish`.

La corrida quedó registrada como `2026-10-15-product-publish-1`. Registró 16 hallazgos en la ficha, repartidos así:

| Señal | Hallazgos |
|---|---|
| `evidence_stale` | 5 |
| `decision_without_source` | 5 |
| `requirement_untraced` | 5 |
| `requirement_without_acceptance` | 1 |

El texto que le muestro aquí está en `estado-producto/PRD-303/corridas/salida-product-publish.md`.