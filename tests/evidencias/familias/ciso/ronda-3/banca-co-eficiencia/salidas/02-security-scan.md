# /criterio-security:security-scan 

La ficha del periodo ya traía todos los documentos de `10-controles/`, `20-accesos/` y `30-terceros/`. Comparé cada uno con su texto y coinciden, así que no hubo que añadir nada. El borrador de A.8.28 sigue anotado como revisado y no se usa como evidencia.
Hay tres archivos que no se abrieron: una credencial, una llave y un respaldo. Conviene sacarlos de la carpeta de evidencia.

# Qué cambió en la seguridad · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.2.3 · **Comando:** `security-scan`

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

- ¿Cuál es la entidad, su identificación fiscal y su país? → Banco Cordillera Sintético, NIT 901555123, Colombia (sugerida por el nombre de la carpeta; sesión de prueba sin interfaz)
- ¿Qué periodo se revisa? → 2026-10 (sugerida por la fecha de la prueba)
- ¿Las columnas reconocidas de la declaración de aplicabilidad, la tabla de sistemas, el registro de terceros y el de riesgos son las correctas? → Sí (sugerida: todas se llaman como el motor las espera; no hace falta mapear columns)
- ¿Dónde se guarda lo que se encuentra? → estado-seguridad/901555123-banco-cordillera-sintetico (sugerida)
- ¿Se acepta la versión vigente de los términos? → Sí, José Francisco Ñáñez
- ¿Se deja la marca _CRITERIO_SEGURIDAD.txt en la carpeta raíz? → Sí (sugerida); el motor falló al escribirla y no quedó
- ¿Se crea una tarea programada para que Alexis revise lo que toca cada día? → Sin respuesta explícita en la sesión de prueba: no se crea, sin reloj

## Fuentes

- `00-referencia/declaracion-aplicabilidad.xlsx`
- `00-referencia/sistemas.csv`
- `00-referencia/terceros.csv`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`
- `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1`
- `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1`
- `40-riesgos/registro-riesgos.csv`