# /criterio-security:security-wake 

Lo que tocaba hoy, según el motor: `security-scan` (documentos nuevos o la revisión semanal). No hay peticiones abiertas.

Desde la corrida anterior no hay documentos nuevos, cambiados ni borrados, y la ficha no tiene documentos pendientes. El inventario marca como fuera de lugar los tres archivos de `80-revisiones/` (dice que irían en `70-incidentes/`). Esa carpeta es de Amparo, el agente de respuesta y recuperación, así que aquí no se movieron.

# Qué cambió en la seguridad · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.5.1 · **Comando:** `security-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un control aplicable de la declaración figura implementado y no tiene ninguna evidencia de que operó (`control_without_evidence`) | A.8.15 · Registro de eventos: figura «Implementado» y la ficha no tiene ninguna evidencia de que operó | — | Oficial de cumplimiento | — | `00-referencia/declaracion-aplicabilidad.xlsx` fila 12 |
| 2 | La revisión de accesos de un sistema pasó su fecha, o no hay ninguna (`access_review_overdue`) | Directorio activo: la última revisión de accesos es del 2026-06-30; tocaba el 2026-09-28 | — | Jefe de seguridad de la información | 17 | `00-referencia/sistemas.csv` fila 4 · `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1` |
| 3 | Una aceptación de riesgo pasó su fecha de revisión (`risk_acceptance_expired`) | R-03 · Respaldo fuera de sitio a más de 24 horas: aceptado por Comité de riesgos hasta el 2026-09-30, y no se volvió a revisar | — | Comité de riesgos | 15 | `40-riesgos/registro-riesgos.csv` fila 4 |
| 4 | La evaluación de seguridad de un tercero crítico pasó su fecha, o no hay ninguna (`third_party_assessment_overdue`) | Mesa de Ayuda Externa: la última evaluación es del 2025-09-30; tocaba el 2026-09-30 | — | — | 15 | `00-referencia/terceros.csv` fila 4 · `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1` |
| 5 | La revisión de accesos de un sistema pasó su fecha, o no hay ninguna (`access_review_overdue`) | Portal de clientes: ninguna revisión de accesos registrada; la tabla pide una cada 180 días | — | Jefe de seguridad de la información | — | `00-referencia/sistemas.csv` fila 5 |
| 6 | La evaluación de seguridad de un tercero crítico pasó su fecha, o no hay ninguna (`third_party_assessment_overdue`) | Centro de Datos Alterno: tercero crítico sin ninguna evaluación de seguridad registrada; el registro pide una cada 365 días | — | — | — | `00-referencia/terceros.csv` fila 6 |
| 7 | La evidencia más reciente de un control periódico es anterior a su periodicidad (`control_evidence_stale`) | A.5.18 · Derechos de acceso: la evidencia más reciente es del 2026-06-30 y su periodicidad es de 92 días; venció el 2026-09-30 | — | Jefe de infraestructura | 15 | `00-referencia/declaracion-aplicabilidad.xlsx` fila 5 · `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1` |
| 8 | Un control aplicable no tiene responsable (`soa_control_unassigned`) | A.8.24 · Uso de la criptografía: aplicable y sin responsable en la declaración | — | — | — | `00-referencia/declaracion-aplicabilidad.xlsx` fila 14 |

## El resultado

**En la ficha:** 12 evidencias de controles, 3 revisiones de acceso y 3 evaluaciones de terceros.

**Excluidos por omisión:** 3 archivos —credenciales, llaves o respaldos— que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

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

- `00-referencia/declaracion-aplicabilidad.xlsx`
- `00-referencia/sistemas.csv`
- `00-referencia/terceros.csv`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`
- `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1`
- `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1`
- `40-riesgos/registro-riesgos.csv`

---

Quedaron registradas las dos corridas, con su salida en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/`: `2026-10-15-security-scan-2` y `2026-10-15-security-wake-1`.