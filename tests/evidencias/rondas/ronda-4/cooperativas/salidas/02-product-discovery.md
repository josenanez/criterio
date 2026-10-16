# /criterio-product:product-discovery 

## Descubrimiento — Tarjeta débito (PRD-303), al 2026-10-15

No salió ningún tema. El único material de entrevistas es una sola entrevista (2025-09-19, de Natalia Ospina a un cliente) con una sola cita, es decir, una voz. Leí las 5 piezas del producto.

**Términos:** ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-15, así que no pedí ni registré nada nuevo.

**Dicho una sola vez** (no se promueve ni se descarta):

| Qué | Quién | Cuándo |
|---|---|---|
| *«Lo necesito y hoy no lo tengo.»* | Cliente entrevistado, sin nombre ni segmento | 2025-09-19 |

- **Alcance de la cita:** no dice qué necesita, así que no sustenta por sí sola ninguna funcionalidad.
- **Antigüedad:** tiene 13 meses y el umbral de evidencia vieja es 12.
- **Contra el registro:** no la pude cruzar con ningún requerimiento, porque el acta del 2026-10-12 titula REQ-4300 a REQ-4315, REQ-2030 y REQ-2038 solo con su número. La entrevista no contradice nada.
- **Afirmaciones numéricas y fuentes públicas:** no hay.

**Lo que dejó ver el cálculo** (no es descubrimiento):
- 16 de los 18 requerimientos dicen «Cliente entrevistado» como quien los pidió, pero solo hay una cita. Eso lo decide la gerencia, pero la evidencia de descubrimiento no alcanza para sustentarlos.
- El caso de negocio declara `volumen_mensual` 248.461 y el tablero mide 202.628, una brecha de 18,4 %, por debajo del umbral de 20 %.
- El supuesto «El reglamento vigente lo permite» lleva 43 días sin verificar, con umbral de 30.

**No pude sellar la lectura.** `sellar` se negó porque la ficha `producto.json` no se escribió en esta corrida. La próxima corrida volverá a leer las 5 piezas.

La corrida quedó registrada como `2026-10-15-product-discovery-1`: 22 segundos, 18 requerimientos y 42 hallazgos. El texto completo está en `estado-producto/PRD-303/corridas/salida-product-discovery.md`.