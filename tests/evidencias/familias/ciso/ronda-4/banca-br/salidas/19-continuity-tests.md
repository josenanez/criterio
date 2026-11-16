# /criterio-resilience:continuity-tests 

Hay tres pruebas vencidas o sin ninguna: una de recuperación y dos de restauración. Quién las ejecuta y cuándo es decisión de una persona.

Los términos (v1.5) figuraron como vigentes en el motor, con la aceptación 1.4.0 ya registrada. No hizo falta aceptarlos de nuevo, así que no registré la aceptación a nombre de José Francisco Ñáñez.

# Las pruebas de continuidad · Banco Paulista Sintético · periodo 2026-10

**Fecha de corte:** 2026-10-15 · **Agente:** Amparo, versión 1.4.0

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | `continuity_test_overdue` | Recuperación del centro de datos alterno: la última prueba es del 2026-02-20; tocaba el 2026-08-19 | Jefe de infraestructura | 57 | `00-referencia/calendario-continuidad.csv` fila 3 · `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf` |
| 2 | `restore_test_overdue` | Restauración del correo corporativo: la última prueba es del 2026-06-20; tocaba el 2026-09-18 | Jefe de infraestructura | 27 | `00-referencia/calendario-continuidad.csv` fila 5 · `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf` |
| 3 | `restore_test_overdue` | Restauración de la base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | Jefe de infraestructura | — | `00-referencia/calendario-continuidad.csv` fila 6 |

## El resultado

| Prueba | Tipo | Sistema | Cada | Última | Resultado | Tocaba |
|---|---|---|---|---|---|---|
| Plan de continuidad del negocio | continuidad | Toda la entidad | 365 días | 2026-03-15 | exitosa | 2027-03-15 |
| Recuperación del centro de datos alterno | recuperación | Centro de datos | 180 días | 2026-02-20 | exitosa | 2026-08-19 |
| Restauración del core bancário | restauración | Core bancário | 90 días | 2026-08-01 | con observaciones | 2026-10-30 |
| Restauración del correo corporativo | restauración | Correo corporativo | 90 días | 2026-06-20 | exitosa | 2026-09-18 |
| Restauración de la base de clientes | restauración | Base de clientes | 180 días | — | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido, por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido, .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido, .zip es una llave, una credencial o un respaldo.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/calendario-continuidad.csv`
- `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf`
- `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf`

La corrida quedó registrada como `2026-10-15-continuity-tests-1`, con la salida en `estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-continuity-tests.md`.

Tres cosas que no coinciden con lo que pediste:
- **Reporte:** el motor escribió el reporte, y lo que muestro arriba es el mismo contenido. Aquí quité la columna Monto, que venía vacía, y acorté los textos de las señales.
- **Archivo de salida:** el archivo guardado sí tiene el reporte completo, con la tabla original. Lleva además una línea mía al inicio, igual que la de este mensaje. El archivo no tiene todo lo que ves aquí.
- **`--today`:** lo pasé en `terminos`, `reporte` y `corrida`. `corrida` no confirmó que lo aceptara, porque su salida no muestra la fecha.