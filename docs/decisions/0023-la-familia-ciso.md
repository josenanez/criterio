# 0023 · La familia CISO: seguridad de la información, con tres agentes sobre estándares internacionales

**Fecha:** 2026-10-30 · **Estado:** diseño, por aprobar los nombres · **Modifica:** 0013, que pasa de propuesta a diseño

## Contexto

La decisión 0013 propuso la familia de seguridad de la información con un agente. José Francisco
Ñáñez pidió diseñarla completa. A diferencia de la CFO o la CLO, el rol se define sobre estándares
internacionales, no sobre la ley de cada país, así que el diseño y la prueba no dependen de un
registro de países:

| Marco | Qué aporta | Estado de la fuente |
|---|---|---|
| NIST Cybersecurity Framework 2.0 (26 de febrero de 2024) | Las seis funciones: gobernar, identificar, proteger, detectar, responder y recuperar. Ordena la familia | Por verificar en la publicación de NIST |
| ISO/IEC 27001:2022 | El sistema de gestión, la declaración de aplicabilidad y los controles del anexo A, cada uno con su evidencia | Norma de pago: se citan el número y el nombre de cada control, nunca su texto |
| NIST SP 800-61 Rev. 3 (3 de abril de 2025) | La respuesta a incidentes como perfil comunitario del CSF 2.0 | Verificada en csrc.nist.gov |
| CISA, BOD 22-01 y su catálogo KEV | Lo explotado se corrige en dos semanas, o en seis meses si su CVE es anterior a 2021 | Verificada en cisa.gov |
| FIRST CVSS v4.0 y CIS Controls v8.1 | La severidad de una vulnerabilidad y las salvaguardas de referencia | Por verificar |

## Decisión

**Criterio CISO · La seguridad de la información.** Tres agentes, uno por cada trabajo recurrente
que hoy se hace a mano contra documentos:

| Agente (nombre por aprobar) | Plugin | Funciones del CSF | Lo que hace |
|---|---|---|---|
| **Alexis**, del griego «el que defiende» | `criterio-security` | Gobernar, identificar, proteger | Contrasta la declaración de aplicabilidad y cada control con su evidencia, las revisiones de acceso, las evaluaciones de terceros y las aceptaciones de riesgo |
| **Guillermo**, «protector decidido» | `criterio-vulnerability` | Identificar, proteger, detectar | Cruza cada vulnerabilidad de la exportación del escáner con su plazo según la severidad y con el catálogo KEV, y su cierre con el escaneo que lo prueba |
| **Amparo**, «protección» | `criterio-resilience` | Responder, recuperar | Cruza cada incidente con los plazos de la política de respuesta y con las notificaciones que pide la matriz de la organización, y las pruebas de continuidad y de restauración con su calendario |

### Las señales que calcula el código

| Agente | Señal | Cuándo |
|---|---|---|
| Alexis | `control_without_evidence` | Un control aplicable de la declaración figura operando y no tiene evidencia del periodo |
| Alexis | `control_evidence_stale` | La evidencia más reciente de un control periódico es anterior a su periodicidad |
| Alexis | `soa_control_unassigned` | Un control aplicable no tiene responsable |
| Alexis | `access_review_overdue` | La revisión de accesos de un sistema pasó su fecha |
| Alexis | `third_party_assessment_overdue` | La evaluación de seguridad de un tercero crítico pasó su fecha |
| Alexis | `risk_acceptance_expired` | Una aceptación de riesgo pasó su fecha de revisión |
| Guillermo | `vuln_past_sla` | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política |
| Guillermo | `kev_past_due` | Una vulnerabilidad del catálogo KEV sigue abierta después de su fecha de corrección |
| Guillermo | `vuln_closed_without_rescan` | Una vulnerabilidad figura cerrada y ningún escaneo posterior la da por corregida |
| Guillermo | `vuln_exception_expired` | Una excepción a la corrección pasó su vencimiento |
| Guillermo | `asset_not_scanned` | Un activo del inventario no aparece en ningún escaneo del periodo |
| Amparo | `incident_response_late` | Un incidente se contuvo después del plazo de su severidad en la política |
| Amparo | `incident_notification_late` | Una notificación de la matriz —al supervisor, a los titulares, al cliente— se hizo tarde o no se hizo |
| Amparo | `incident_without_review` | Un incidente cerrado no tiene su revisión posterior dentro del plazo |
| Amparo | `continuity_test_overdue` | La prueba del plan de continuidad o de recuperación pasó su fecha |
| Amparo | `restore_test_overdue` | La prueba de restauración de un respaldo crítico pasó su fecha |

**Los plazos los fija la organización**, en su política y en su matriz, como en la CLO: el código
calcula y la persona decide. Lo único que viene de una fuente externa es la fecha de corrección
del catálogo KEV, que el catálogo trae.

### Lo que nunca hace

- Correr un escaneo, conectarse a un sistema o a una consola.
- Aceptar un riesgo o declarar cumplido un control.
- Calificar la madurez de la organización o certificarla contra la ISO/IEC 27001.
- Publicar en Rostrum las vulnerabilidades abiertas sin que la configuración lo diga: un informe
  de vulnerabilidades es un mapa para un atacante.
- Leer credenciales, llaves o respaldos. La configuración los excluye por omisión, y el informe dice
  qué excluyó.

### Los comandos

Cada agente tiene su instalación (`*-setup`), su revisión completa (`*-scan`), un reporte por cada
grupo de señales y su despertador (`*-wake`):

- **Alexis:** `soa-status`, `control-evidence`, `access-reviews`, `third-parties`, `risk-register`.
- **Guillermo:** `vuln-sla`, `kev-check`, `scan-coverage`.
- **Amparo:** `incident-timeline`, `notifications`, `continuity-tests`.

### La prueba

- **Organizaciones sintéticas** de banca, retail, salud y tecnología, más dos controles. Cada una
  trae:
  - la declaración de aplicabilidad y su matriz de controles con la evidencia;
  - las revisiones de acceso, el registro de terceros y el de riesgos;
  - el inventario de activos, tres exportaciones de escáner y el catálogo KEV;
  - la política de respuesta y el registro de incidentes con sus notificaciones;
  - el calendario de continuidad.
- **El material siembra al menos 73 señales**, lo que pide un piso del 95 % sin fallas (decisión
  0020), y una clave que el agente no ve.
- **Las exportaciones de escáner:** la primera versión procesa un CSV o un Excel con el mapeo de
  columnas del setup. El formato de cada producto (Tenable, Qualys, Rapid7, Defender) entra después,
  cada uno desde su fuente verificada, como entraron Dynamics y Zoho en la CCO.
- **Versiones:** la 0.1.0, construida con su motor probado; la 0.2.0, con la ronda de los tres
  agentes.

## Lo que queda abierto

1. **Los nombres de los agentes.** Alexis, Guillermo y Amparo son una propuesta; los decide José.
2. **Las fuentes por verificar:** NIST CSF 2.0, FIRST CVSS v4.0 y CIS Controls v8.1, antes de que
   el motor cite cualquiera de ellas.
3. **La regulación de cada país** (por ejemplo, la circular de ciberseguridad del supervisor
   financiero de Colombia): entra a la matriz de notificaciones de la organización. El motor no la
   trae.
