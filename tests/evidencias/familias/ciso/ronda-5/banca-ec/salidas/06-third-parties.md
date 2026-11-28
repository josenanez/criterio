# /criterio-security:third-parties 

Dos terceros críticos tienen la evaluación de seguridad vencida o sin ninguna: Mesa de Ayuda Externa y Centro de Datos Alterno.

# Los terceros críticos · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.5.1 · **Comando:** `third-parties`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La evaluación de seguridad de un tercero crítico pasó su fecha, o no hay ninguna (`third_party_assessment_overdue`) | Mesa de Ayuda Externa: la última evaluación es del 2025-09-30; tocaba el 2026-09-30 | — | — | 15 | `00-referencia/terceros.csv` fila 4 · `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1` |
| 2 | La evaluación de seguridad de un tercero crítico pasó su fecha, o no hay ninguna (`third_party_assessment_overdue`) | Centro de Datos Alterno: tercero crítico sin ninguna evaluación de seguridad registrada; el registro pide una cada 365 días | — | — | — | `00-referencia/terceros.csv` fila 6 |

## El resultado

| Tercero | Servicio | Crítico | Cada | Última evaluación | Resultado | Tocaba |
|---|---|---|---|---|---|---|
| Nube Andina Servicios | infraestructura en la nube | sí | 365 días | 2026-02-10 | sin hallazgos | 2027-02-10 |
| Pasarela de Pagos Sintética | procesamiento de pagos | sí | 365 días | 2025-11-20 | con observaciones | 2026-11-20 |
| Mesa de Ayuda Externa | soporte a usuarios | sí | 365 días | 2025-09-30 | sin hallazgos | 2026-09-30 |
| Papelería del Centro | insumos de oficina | no | 365 días | — | — | — |
| Centro de Datos Alterno | sitio de recuperación | sí | 365 días | — | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

- ¿Es esta la carpeta de la entidad: seguridad/1790987654001-banco-del-guayas-sintetico? → Sí (respuesta sugerida; prueba sin interfaz)
- ¿La entidad es Banco del Guayas Sintético, RUC 1790987654001, Ecuador, en USD? → Sí (respuesta sugerida a partir del nombre de la carpeta; prueba sin interfaz)
- ¿El periodo es 2026-10? → Sí (respuesta sugerida a partir de la fecha de la prueba)
- ¿Las tablas de 00-referencia/ y 40-riesgos/ se toman con las columnas que el motor reconoce, sin mapeo? → Sí (respuesta sugerida: sistemas.csv, terceros.csv y registro-riesgos.csv traen los nombres esperados)
- ¿Guardo lo que encuentro en estado-seguridad/1790987654001-banco-del-guayas-sintetico? → Sí (respuesta sugerida)
- ¿Aceptas los términos 1.6? → Sí, José Francisco Ñáñez, 2026-10-15
- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la carpeta? → Sí (respuesta sugerida)
- ¿Programo la tarea diaria de security-wake? → No (sin interfaz, nadie dio un sí explícito)

## Fuentes

- `00-referencia/terceros.csv`
- `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1`

---
Corrida registrada: `2026-10-15-third-parties-1`.