# /criterio-changes:change-check 

Cinco señales abiertas en los cambios de 2026-11: tres cambios normales sin aprobación en las actas, una emergencia sin revisión y un cambio revertido sin revisión. La decisión es del comité de cambios.

Los términos ya estaban vigentes (versión 1.6, aceptada en 0.1.0), así que no hubo que registrar la aceptación de nuevo.

# Cada cambio con su aprobación · Retail Control de Tecnología Sintético · periodo 2026-11

**Entidad:** Retail Control de Tecnología Sintético (RCT190101AB2) · **Fecha de corte:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | `change_without_approval` | CHG-100 · Actualización del certificado del portal: se implementó el 2026-10-05 sin una aprobación en las actas | — | `10-cambios/cambios_2026-10.xlsx` fila 2 |
| 2 | `change_without_approval` | CHG-103 · Ajuste del límite de sesiones: se implementó el 2026-10-08 sin una aprobación en las actas | — | fila 5 |
| 3 | `change_without_approval` | CHG-104 · Nueva versión del motor de pagos: se implementó el 2026-10-12 sin una aprobación en las actas | — | fila 6 |
| 4 | `emergency_change_without_review` | CHG-102 · Corrección de la conciliación de pagos: emergencia implementada el 2026-10-10; la política da 5 días para revisarla y no hay revisión en las actas | 41 | fila 4 |
| 5 | `failed_change_without_review` | CHG-104 · Nueva versión del motor de pagos: terminó «Revertido» el 2026-10-12 y no tiene revisión posterior | — | fila 6 |

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
La corrida quedó registrada como `2026-11-25-change-check-1`, con la salida en `corridas/salida-change-check.md`.