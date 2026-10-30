# /criterio-compliance:compliance-scan 

Terminé el escaneo y dejé la corrida registrada. No hay archivos nuevos ni cambiados desde la corrida anterior, y el motor marcó 5 señales para atender. Los términos vigentes ya estaban aceptados.

# Qué cambió en el cumplimiento · Almacenes del Altiplano · periodo 2026-09

**Entidad:** Almacenes del Altiplano (52934187) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.1.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolución sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |
| 3 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Lesly Rodas | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 4 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | — | Byron Estrada | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 5 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

(El motor no trajo contenido en esta sección.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dejo en la carpeta el archivo _CRITERIO_LEGAL.txt para reconocerla la próxima vez? → Sí (respuesta sugerida; sesión de prueba sin interfaz)
- ¿Los términos vigentes de esta versión los acepta José Francisco Ñáñez? → Sí, según la instrucción de la sesión de prueba

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`

La salida quedó en `corridas/salida-compliance-scan.md`, que es la copia del reporte del motor. En el chat solo añadí el aviso de que la sección «El resultado» vino vacía. La corrida quedó registrada como `2026-10-06-compliance-scan-1`.