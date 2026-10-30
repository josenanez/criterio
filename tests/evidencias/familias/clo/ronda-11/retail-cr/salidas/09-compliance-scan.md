# /criterio-compliance:compliance-scan 

Los términos vigentes (versión 1.3) ya estaban aceptados. Desde la corrida anterior no hay archivos nuevos, cambiados ni borrados (66 en el inventario). El informe de septiembre declara el periodo «con observaciones».

# Qué cambió en el cumplimiento · Almacenes de la Meseta · periodo 2026-09

**Entidad:** Almacenes de la Meseta (3101612904) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.1.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta (`report_case_overdue`) | Caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Obligación cumplida sin evidencia (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | Andrea Jiménez | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 3 | Política con la revisión vencida (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | Luis Diego Rojas | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 4 | Evidencia de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | Luis Diego Rojas | — | `00-referencia/matriz-obligaciones.csv` fila 11 |
| 5 | Obligación sin fuente (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | `00-referencia/matriz-obligaciones.csv` fila 12 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el del informe de cumplimiento más reciente
- ¿Dónde están las fichas de Fidel? → `estado-legal/3101612904-almacenes-de-la-meseta/contratos`
- ¿Dejo en la carpeta raíz el archivo `_CRITERIO_LEGAL.txt`? → Sí

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `40-canal/casos.csv`

Dos cosas que debo decir con franqueza:

- **Fecha de la corrida.** Pasé `--today 2026-10-06` en cada llamada del motor, pero las comandas `terminos` e `inventario` ya habían corrido con esa fecha y no pasé nada distinto en las demás. La fecha real del sistema es 2026-10-30.
- **Aceptación de términos.** No se registró ninguna aceptación nueva. El motor ya la daba como vigente, con la versión 1.1.0 aceptada, así que no usé el nombre de José Francisco Ñáñez.

La salida quedó en `estado-legal/3101612904-almacenes-de-la-meseta/corridas/salida-compliance-scan.md` y la corrida se registró como `2026-10-06-compliance-scan-1`, con 5 hallazgos.