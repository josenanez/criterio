# /criterio-resilience:continuity-tests 

Tres pruebas están vencidas o sin hacer, con fecha de corte 2026-10-15. Los términos estaban vigentes (versión 1.6), así que no hizo falta registrar una aceptación nueva.

# Las pruebas de continuidad · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.5.1 · **Comando:** `continuity-tests`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Prueba de continuidad o recuperación vencida (`continuity_test_overdue`) | Recuperación del centro de datos alterno: la última prueba es del 2026-02-20; tocaba el 2026-08-19 | Jefe de infraestructura | 57 | `00-referencia/calendario-continuidad.xlsx` fila 3 · `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf` |
| 2 | Prueba de restauración vencida (`restore_test_overdue`) | Restauración del correo corporativo: la última prueba es del 2026-06-20; tocaba el 2026-09-18 | Jefe de infraestructura | 27 | `00-referencia/calendario-continuidad.xlsx` fila 5 · `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf` |
| 3 | Prueba de restauración sin ninguna registrada (`restore_test_overdue`) | Restauración de la base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | Jefe de infraestructura | — | `00-referencia/calendario-continuidad.xlsx` fila 6 |

## El resultado

| Prueba | Tipo | Sistema | Cada | Última | Resultado | Tocaba |
|---|---|---|---|---|---|---|
| Plan de continuidad del negocio | continuidad | Toda la entidad | 365 días | 2026-03-15 | exitosa | 2027-03-15 |
| Recuperación del centro de datos alterno | recuperación | Centro de datos | 180 días | 2026-02-20 | exitosa | 2026-08-19 |
| Restauración del core bancario | restauración | Core bancario | 90 días | 2026-08-01 | con observaciones | 2026-10-30 |
| Restauración del correo corporativo | restauración | Correo corporativo | 90 días | 2026-06-20 | exitosa | 2026-09-18 |
| Restauración de la base de clientes | restauración | Base de clientes | 180 días | — | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión (por su nombre es una credencial o una llave).
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión (.pem es una llave, una credencial o un respaldo).
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión (.zip es una llave, una credencial o un respaldo).

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/calendario-continuidad.xlsx`
- `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf`
- `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf`

---

La corrida quedó registrada como `2026-10-15-continuity-tests-1`. Lo mostrado está guardado en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-continuity-tests.md`.

No ejecuté ni agendé ninguna prueba. Decidir quién las hace y cuándo es de una persona.