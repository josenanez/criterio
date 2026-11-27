# /criterio-changes:change-check 

Cinco señales abiertas en los cambios del periodo: tres cambios normales sin aprobación en las actas, un cambio de emergencia sin revisión y un cambio revertido sin revisión. La decisión es del comité de cambios.

# Cada cambio con su aprobación · Banco Control de Tecnología Sintético · periodo 2026-11

**Entidad:** Banco Control de Tecnología Sintético (901333666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Cambio normal implementado sin aprobación, o antes de ella (`change_without_approval`) | CHG-100 · Actualización del certificado del portal: se implementó el 2026-10-05 sin una aprobación en las actas del comité de cambios | — | `10-cambios/cambios_2026-10.xlsx` fila 2 |
| 2 | Ídem (`change_without_approval`) | CHG-103 · Ajuste del límite de sesiones: se implementó el 2026-10-08 sin una aprobación en las actas | — | `10-cambios/cambios_2026-10.xlsx` fila 5 |
| 3 | Ídem (`change_without_approval`) | CHG-104 · Nueva versión del motor de pagos: se implementó el 2026-10-12 sin una aprobación en las actas | — | `10-cambios/cambios_2026-10.xlsx` fila 6 |
| 4 | Cambio de emergencia sin revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-102 · Corrección de la conciliación de pagos: implementado el 2026-10-10; la política da 5 días para su revisión y no tiene revisión en las actas | 41 | `10-cambios/cambios_2026-10.xlsx` fila 4 |
| 5 | Cambio fallido o revertido sin revisión posterior (`failed_change_without_review`) | CHG-104 · Nueva versión del motor de pagos: terminó como «Revertido» el 2026-10-12 y no tiene revisión posterior en las actas | — | `10-cambios/cambios_2026-10.xlsx` fila 6 |

## El resultado

**Días de la política para revisar un cambio de emergencia:** 5.

| Cambio | Tipo | Implementado | Resultado | Aprobado | Revisado |
|---|---|---|---|---|---|
| CHG-100 | Normal | 2026-10-05 | Exitoso | — | — |
| CHG-101 | Estándar | 2026-10-20 | Exitoso | — | — |
| CHG-102 | Emergencia | 2026-10-10 | Exitoso | — | — |
| CHG-103 | Normal | 2026-10-08 | Exitoso | — | — |
| CHG-104 | Normal | 2026-10-12 | Revertido | — | — |

| Despliegue | Fecha | Sistema | Cambio | En la exportación |
|---|---|---|---|---|
| D-100 | 2026-10-05 | Portal | CHG-100 | sí |
| D-101 | 2026-10-08 | Portal | CHG-103 | sí |

Si un cambio se aprueba lo decide el comité de cambios: aquí se dice cuál llegó a producción sin su aprobación o sin su revisión.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-cambios/cambios_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)

---
La corrida quedó registrada como `2026-11-25-change-check-1`. El reporte está en `estado-tecnologia/901333666-banco-control-de-tecnologia-sintetico/cambios/2026-11/reporte-change-check.md` y lo mostrado, en `corridas/salida-change-check.md`. Los términos ya estaban vigentes (versión 1.6), así que no hizo falta registrar la aceptación. El motor registró 0 hallazgos en la corrida, aunque el reporte trae 5 señales.