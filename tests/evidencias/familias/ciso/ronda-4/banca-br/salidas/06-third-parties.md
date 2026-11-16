# /criterio-security:third-parties 

Dos terceros críticos tienen la evaluación de seguridad vencida o sin ninguna: Mesa de Ayuda Externa y Centro de Datos Alterno. La decisión sobre cómo atenderlos es de quien responde por ellos.

# Los terceros críticos · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.4.0 · **Comando:** `third-parties`

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

- ¿La carpeta de la entidad es seguridad/12345678000195-banco-paulista-sintetico? → Sí (respuesta sugerida, sesión de prueba sin interfaz)
- ¿La entidad es Banco Paulista Sintético, CNPJ 12345678000195, Brasil? → Sí (respuesta sugerida a partir del nombre de la carpeta)
- ¿El periodo es 2026-10? → Sí (respuesta sugerida a partir de la fecha de la prueba)
- ¿Las columnas de la declaración de aplicabilidad, de la tabla de sistemas, del registro de terceros y del registro de riesgos son las que reconoce el motor? → Sí (el motor no reportó columnas faltantes; columns quedó vacío)
- ¿Guardo lo que encuentro en estado-seguridad/12345678000195-banco-paulista-sintetico? → Sí (respuesta sugerida)
- ¿Aceptas los términos 1.5? → Sí, José Francisco Ñáñez
- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la carpeta? → Sí (respuesta sugerida)

## Fuentes

- `00-referencia/terceros.csv`
- `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1`

La corrida quedó registrada como `2026-10-15-third-parties-1`.

Una nota: `terminos` dijo que los términos estaban vigentes (aceptada 1.4.0, términos 1.5), así que no corrí la aceptación aparte. El reporte registra la aceptación de los términos 1.5 a nombre de José Francisco Ñáñez.