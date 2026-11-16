# /criterio-security:security-scan 

La ficha del periodo ya tenía todo lo que hay en `10-controles/`, `20-accesos/` y `30-terceros/`, y lo que registra coincide con el texto de cada documento, así que no tuve que agregar nada. El borrador de la guía de codificación sigue anotado como algo que no prueba que el control operó. Conviene sacar de la carpeta la credencial, la llave y el respaldo que el motor deja sin abrir.

# Qué cambió en la seguridad · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.4.0 · **Comando:** `security-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un control aplicable de la declaración figura implementado y no tiene ninguna evidencia de que operó (`control_without_evidence`) | A.8.15 · Registro de eventos: figura «Implementado» y la ficha no tiene ninguna evidencia de que operó | — | Oficial de cumplimiento | — | `00-referencia/declaracion-aplicabilidad.csv` fila 12 |
| 2 | La revisión de accesos de un sistema pasó su fecha, o no hay ninguna (`access_review_overdue`) | Directorio activo: la última revisión de accesos es del 2026-06-30; tocaba el 2026-09-28 | — | Jefe de seguridad de la información | 17 | `00-referencia/sistemas.csv` fila 4 · `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1` |
| 3 | Una aceptación de riesgo pasó su fecha de revisión (`risk_acceptance_expired`) | R-03 · Respaldo fuera de sitio a más de 24 horas: aceptado por Comité de riesgos hasta el 2026-09-30, y no se volvió a revisar | — | Comité de riesgos | 15 | `40-riesgos/registro-riesgos.xlsx` fila 4 |
| 4 | La evaluación de seguridad de un tercero crítico pasó su fecha, o no hay ninguna (`third_party_assessment_overdue`) | Mesa de Ayuda Externa: la última evaluación es del 2025-09-30; tocaba el 2026-09-30 | — | — | 15 | `00-referencia/terceros.csv` fila 4 · `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1` |
| 5 | La revisión de accesos de un sistema pasó su fecha, o no hay ninguna (`access_review_overdue`) | Portal de clientes: ninguna revisión de accesos registrada; la tabla pide una cada 180 días | — | Jefe de seguridad de la información | — | `00-referencia/sistemas.csv` fila 5 |
| 6 | La evaluación de seguridad de un tercero crítico pasó su fecha, o no hay ninguna (`third_party_assessment_overdue`) | Centro de Datos Alterno: tercero crítico sin ninguna evaluación de seguridad registrada; el registro pide una cada 365 días | — | — | — | `00-referencia/terceros.csv` fila 6 |
| 7 | La evidencia más reciente de un control periódico es anterior a su periodicidad (`control_evidence_stale`) | A.5.18 · Derechos de acceso: la evidencia más reciente es del 2026-06-30 y su periodicidad es de 92 días; venció el 2026-09-30 | — | Jefe de infraestructura | 15 | `00-referencia/declaracion-aplicabilidad.csv` fila 5 · `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1` |
| 8 | Un control aplicable no tiene responsable (`soa_control_unassigned`) | A.8.24 · Uso de la criptografía: aplicable y sin responsable en la declaración | — | — | — | `00-referencia/declaracion-aplicabilidad.csv` fila 14 |

## El resultado

**En la ficha:** 12 evidencias de controles, 3 revisiones de acceso y 3 evaluaciones de terceros.

**Excluidos por omisión:** 3 archivos —credenciales, llaves o respaldos— que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

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

- `00-referencia/declaracion-aplicabilidad.csv`
- `00-referencia/sistemas.csv`
- `00-referencia/terceros.csv`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`
- `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1`
- `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1`
- `40-riesgos/registro-riesgos.xlsx`

---

Guardé esto tal cual en `estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-security-scan.md` y la corrida quedó registrada como `2026-10-15-security-scan-1`.