# /criterio-product:product-setup documentos/productos/PRD-305

## Listo — Locales comerciales (PRD-305)

**Lo que miré:** 4 documentos. Uno es de descubrimiento (las entrevistas del 2026-02-03). Los otros son la definición y el caso de negocio, ambos del 2025-09-25, y el acta del comité del 2026-10-16. No hay serie de métricas, y todos los formatos se pudieron leer.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.8.0 (términos 1.2) el 2026-10-22. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.8.0-2026-10-22.md` y `.pdf`.

**Configuración:** `.criterio/producto/PRD-305/config.json`. El estado queda en `estado-producto/PRD-305`. Quien decide es el Comité de producto. Ningún documento lo dice con esas palabras. Lo propuse porque el comité es quien revisa y acepta los requerimientos.

**Marca de la carpeta:** no dejé `_CRITERIO_PRODUCTO.txt`. Es lo único que se escribiría dentro de tus documentos y no hubo un sí.

### Lo que tu definición afirma, y qué lo sostiene

| Afirmación | Sostenida por |
|---|---|
| Entidades públicas no tiene locales comerciales | Nada. La definición lo dice sin citar entrevista ni dato. La única entrevista dice «Lo necesito y hoy no lo tengo», sin decir qué ni quién. |
| Propuesta principal | Solo el título. No dice qué se propone. |
| volumen_mensual = 214.841 | El propio caso de negocio, que se cita a sí mismo. No hay serie medida. |
| Retorno esperado en 24 meses | Sin cifra ni base. |
| La licencia se expide sin objeciones | Supuesto declarado el 2026-09-06, sin verificar. |

### Lo que no está dicho en ninguna parte

- **Criterio de éxito:** no hay ninguno, así que el producto no se podrá cerrar contra nada.
- **Quién decide:** ningún documento lo nombra. El acta de comité solo lista a Beatriz Cuéllar como asistente.
- **Medición de volumen_mensual:** nadie está midiendo lo que el negocio afirmó.
- **Proyecto que ejecute los requerimientos:** de 13 aceptados, ninguno tiene proyecto. La definición dice «Ninguno declarado».
- **Quién pidió qué:** la entrevista no nombra ningún requerimiento. Los requerimientos con «Cliente entrevistado» se apoyan en esa única cita genérica. Tienen evidencia 7 de los 13 aceptados (53,8 %).
- **Aceptados sin evidencia (6):** REQ-4501, 4504, 4507, 4508, 4509 y 4513.
- **Aceptados sin criterio de aceptación (3):** REQ-4501, 4506 y 4507.
- **Sin doliente:** REQ-4502.
- **Propuestos sin decidir:** REQ-4502 (148 días) y REQ-4511 (204 días). El acta solo dice «Se mantiene el plan».
- **Qué problema es cada requerimiento:** los 15 se llaman «Requerimiento REQ-xxxx» y ningún documento lo explica.

### Supuestos sobre los que está escrita

Hay uno: «La licencia se expide sin objeciones», sin verificar, 46 días desde que se declaró. Su fecha (2026-09-06) es posterior a la de la definición (2025-09-25). O alguien editó el documento sin cambiar la fecha, o la fecha está mal.

### Qué le falta a tu carpeta

Como hallazgo, no como requisito:
- Las transcripciones completas de las entrevistas. Hay una sola ronda y una sola persona entrevistada.
- La serie de volumen_mensual con su fuente, en una carpeta `20-metricas`.
- El criterio de éxito.
- Un documento que nombre quién decide.
- La verificación del supuesto de la licencia.

**Siguiente paso:** `/product-discovery` sobre las entrevistas, para ver qué dijo el cliente y a qué requerimiento corresponde.

Fue una sesión sin interfaz, así que tomé las respuestas sugeridas y no hice preguntas. No medí los minutos hasta el primer resultado. El script midió 22 segundos de cómputo. La salida completa y la corrida quedaron registradas en `estado-producto/PRD-305/corridas/`.