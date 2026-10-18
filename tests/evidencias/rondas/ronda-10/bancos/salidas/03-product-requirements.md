# /criterio-product:product-requirements 

## Registro — Tarjeta de crédito digital (PRD-304) · al 2026-10-18

Hay 18 requerimientos y 17 están decididos. El 70.6% de los decididos tiene evidencia y ninguno tiene un proyecto que lo ejecute (0%). Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-18, así que no los registré de nuevo.

**Se va a construir y nadie lo pidió.** Son cinco aceptados sin una sola cita de quien lo pidió:

| REQ | Doliente |
|---|---|
| REQ-2038 | Gustavo Neira |
| REQ-4402 | Ricardo Salas |
| REQ-4409 | Diana Molina |
| REQ-4410 | Jorge Medina |
| REQ-4413 | Felipe Arango |

REQ-4410 lleva 212 días aceptado sin sustento.

**Decidido y nadie lo está construyendo.** Son los 17 aceptados; ninguno tiene proyecto. La tabla con las fechas de decisión está en el archivo de salida.

**Sin doliente.** REQ-4407 y REQ-4408 no tienen doliente. Los otros 16 tienen una persona. Ninguno tiene un área en lugar de una persona.

**Sin criterio de aceptación.** REQ-4400, REQ-4412 y REQ-4414.

**Decidido sin documento que lo respalde.** El script no calculó esta señal en esta corrida, así que no la afirmo ni la descarto.

**Lleva meses y nadie lo decide.** REQ-4401 está propuesto desde hace 65 días, y el umbral es 60. La facultad de decidir es del Comité de producto, que es la autoridad que figura en la configuración. El doliente es Carlos Peña y el gerente de producto es Liliana Torres. Lo que corresponde es decidirlo (aceptar o descartar con su documento), no cerrarlo por viejo.

**Evidencia vieja.** Son 13 requerimientos cuya evidencia más nueva es del 2025-10-03, a 12 meses del umbral:
- REQ-2030, 4400, 4401, 4403, 4404, 4405, 4406, 4407, 4408, 4411, 4412, 4414 y 4415.
- Es la misma cita en todos: una entrevista de cliente («Lo necesito y hoy no lo tengo.») que no nombra ningún requerimiento. Sostiene la necesidad general, no cada requerimiento.
- REQ-4401 está propuesto, así que ahí no es un vacío exigible.

**Por estado.** Hay 1 propuesto y 17 aceptados. No hay ninguno en construcción, entregado ni descartado.

**Aparte.**
- El volumen mensual declarado (263.889) difiere 3.3% del medido (272.644, tablero del 2026-10-15), bajo el umbral de 20%, así que no es hallazgo.
- El criterio de éxito del producto no está dicho en ninguna parte.

**Después.** Conviene correr `/product-trace` sobre los 17 decididos que nadie construye. REQ-2030 tiene criterio y evidencia, pero la evidencia ya cumple 12 meses; revísala antes de pasarlo a `/product-charter`.

La corrida quedó registrada como `2026-10-18-product-requirements-1`: 41 hallazgos en 19 segundos. El texto completo está en `estado-producto/PRD-304/corridas/salida-product-requirements.md`.