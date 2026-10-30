# /criterio-legal:contract-scan 

Primera corrida: extraje las fichas de los 6 contratos (CTR-1901 a CTR-1906) y el motor encontró 5 señales. Los términos ya estaban aceptados por José Francisco Ñáñez el 2026-10-06. Este es el reporte, tal cual lo escribió el motor:

# Qué cambió en los contratos · Instituto Público de Fomento Andino · al 2026-10-06

**Entidad:** Instituto Público de Fomento Andino (899999101) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.0.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Garantía de cumplimiento de un contrato público menor que el mínimo de la ley (`public_guarantee_below_law`) | CTR-1901: la garantía es de 38.400.000,00 y la ley pide al menos el 10 % del valor del contrato, 48.000.000,00 | 9.600.000,00 | — | `contratos/CTR-1901-tecnologia-publica-s-a-s/20-garantias/poliza-cumplimiento.md` |
| 2 | Ídem | CTR-1906: la garantía es de 24.000.000,00 y la ley pide al menos 30.000.000,00 | 6.000.000,00 | — | `contratos/CTR-1906-mantenimiento-publico-s-a-s/20-garantias/poliza-cumplimiento.md` |
| 3 | Contrato público no publicado en el sistema nacional dentro del plazo (`public_contract_not_published`) | CTR-1902: no hay constancia de publicación en SECOP II, y la ley pedía hacerlo a más tardar el 2025-07-01 | — | 462 | `contratos/CTR-1902-suministros-del-estado-s-a-s/10-contrato/contrato.md` |
| 4 | Ídem | CTR-1904: se publicó el 2026-03-04, y la ley pide hacerlo a más tardar el 2026-02-27 (3 días hábiles desde la firma) | — | 5 | `contratos/CTR-1904-software-institucional-s-a-s/10-contrato/constancia-publicacion.md` |
| 5 | Ídem | CTR-1906: se publicó el 2025-10-06, y la ley pide hacerlo a más tardar el 2025-10-01 | — | 5 | `contratos/CTR-1906-mantenimiento-publico-s-a-s/10-contrato/constancia-publicacion.md` |

## El resultado

El motor no escribió texto en esta sección.

## Lo que no se pudo procesar

Todo lo que llegó se procesó. Las fichas quedaron sin `record_issues`.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

Las cinco citas de la tabla.

## Lo que quedó escrito

- **Fichas:** `estado-legal/899999101-instituto-publico-de-fomento-andino/contratos/CTR-190{1..6}.json`.
- **Salida de la corrida:** `estado-legal/899999101-instituto-publico-de-fomento-andino/corridas/salida-contract-scan.md`. Quedó registrada como `2026-10-06-contract-scan-1`, con 5 hallazgos.

## Dos cosas que conviene revisar

- **CTR-1902:** el contrato no trae constancia de publicación, así que dejé `public.published_on` en `null`. Si la constancia existe, falta en la carpeta.
- **CTR-1902, valor:** el registro de contratos dice 300.000.000 y el contrato más el otrosí OT-1 suman 240.000.000 + 60.000.000. Esta corrida no lo marcó como señal; lo cruza `/criterio-legal:contract-register`.

No hay opinión jurídica en lo anterior. Si las demoras o las garantías bajas son un problema para el contrato lo decide una persona.