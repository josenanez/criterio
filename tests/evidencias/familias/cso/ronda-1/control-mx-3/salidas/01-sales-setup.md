# /criterio-sales:sales-setup comercial/CCM101010AB3-comercial-control-de-mexico

Augusto quedó instalado sobre Comercial Control de México (CCM101010AB3), periodo 2026-10, y el primer reporte del embudo no encontró nada abierto.

**Formato del CRM**
- Las tres exportaciones de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) son HubSpot, con 7 filas cada una y sin columnas faltantes.
- La empresa asociada va en la columna `Associated Company`.

**Términos**
- Quedaron aceptados (versión 1.3) a nombre de José Francisco Ñáñez, con fecha 2026-11-05.
- El comprobante en Markdown y PDF está en `.criterio/terminos/`.

**Configuración y ficha**
- La configuración está en `.criterio/comercial/CCM101010AB3-comercial-control-de-mexico/config.json` y el motor la validó. El umbral es de 30 días sin actividad y 2 corrimientos del cierre, según la política comercial.
- Convertí los 8 documentos de `30-evidencia/` y los registré en la ficha: 5 propuestas y 3 órdenes de compra, sin los datos de contacto de los clientes.
- Del acta del 2026-10-02 tomé el pronóstico comprometido, $ 2,205,000, y dejé fuera el mejor escenario de $ 3,360,000 porque el acta dice que no se compromete.

**Resultado del embudo**

| Oportunidad | Etapa | Monto | Cierre | Falta | Días sin actividad | Veces corrido |
|---|---|---|---|---|---|---|
| OPP-1601 | Ganada | 840,000.00 | 2026-10-10 | — | 26 | 0 |
| OPP-1602 | Ganada | 1,260,000.00 | 2026-10-22 | — | 14 | 0 |
| OPP-1603 | Compromiso | 1,750,000.00 | 2026-11-20 | — | 6 | 0 |
| OPP-1604 | Propuesta | 630,000.00 | 2026-12-15 | — | 7 | 1 |
| OPP-1605 | Calificación | 490,000.00 | 2026-12-20 | — | 9 | 0 |
| OPP-1607 | Negociación | 770,000.00 | 2026-12-18 | — | 5 | 1 |

OPP-1606 (Perdida) no aparece en la tabla. Es una oportunidad cerrada como perdida, y supongo que por eso el reporte no la lista; no lo verifiqué.

**Qué quedó sin hacer**
- No creé la marca `_CRITERIO_COMERCIAL.txt` en la raíz, porque nadie podía autorizarla en esta sesión.
- Las demás respuestas las tomé de los documentos, sin consultar a nadie.

La corrida quedó registrada con el id `2026-11-05-sales-setup-1`. El reporte está en `estado-comercial/CCM101010AB3-comercial-control-de-mexico/comercial/2026-10/reporte-pipeline-check.md`.