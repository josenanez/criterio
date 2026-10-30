# criterio-ciso · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada vez,
byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el generador al
sembrar cada defecto; el motor no la ve. Los nombres, las normas, las cifras y los CVE son sintéticos:
los CVE llevan el año 2099 para que ninguno se confunda con una vulnerabilidad real.

## Las entidades

| Carpeta del material | País | Industria | Exportación del escáner | Señales esperadas |
|---|---|---|---|---:|
| `banca-co` | Colombia | banca | CSV, cabeceras en inglés, con la severidad y el puntaje | 25 |
| `retail-mx` | México | retail | Excel, cabeceras en español | 25 |
| `salud-pe` | Perú | salud | CSV con cabeceras que no se reconocen: piden su mapeo en `scanner.columns` | 25 |
| `tecnologia-cl` | Chile | tecnología | CSV con el puntaje CVSS y sin la severidad: sale de la escala del CVSS v4.0 (F-05) | 25 |
| `control-co` | Colombia | — | CSV, cabeceras en inglés | 0 |
| `control-mx` | México | — | Excel, cabeceras en español | 0 |

Cada una trae su carpeta de seguridad al 15 de octubre de 2026, con el periodo de octubre: la política
de gestión de vulnerabilidades en PDF y la de respuesta a incidentes en Word, con sus plazos, distintos
en cada entidad; la declaración de aplicabilidad con quince controles; la tabla de sistemas, el
registro de terceros, el inventario de activos, la matriz de notificaciones y el calendario de
continuidad; la evidencia de cada control, las revisiones de acceso y las evaluaciones de terceros; el
registro de riesgos; tres exportaciones del escáner —el 20 de agosto, el 20 de septiembre y el 10 de
octubre— y el catálogo KEV con las doce columnas que publica CISA (F-06); el seguimiento de la
remediación y las excepciones; y los incidentes del trimestre, cada uno con su informe, la constancia
de cada notificación y su revisión, y el informe de cada prueba de continuidad.

**Lo que nunca se abre, en cada entidad:** una llave privada (`.pem`), un archivo de credenciales y un
respaldo comprimido (`.zip`). El motor los excluye, cada reporte los nombra, y `evaluar.py` comprueba
que se excluya exactamente eso y que ningún resultado guarde su contenido.

## Lo que se siembra, y la señal que tiene que levantar

Las cuatro entidades de industria siembran lo mismo, cada una con sus plazos y su formato de escáner.
La lista exacta está en su clave, `material/<entidad>/clave.json`, en `esperado`.

| Agente | Lo que se siembra | Señal |
|---|---|---|
| Alexis | El registro de eventos (A.8.15) figura implementado y no tiene ninguna evidencia | `control_without_evidence` |
| Alexis | Los derechos de acceso (A.5.18), trimestrales, con la última evidencia de junio | `control_evidence_stale` |
| Alexis | El uso de la criptografía (A.8.24), aplicable y sin responsable | `soa_control_unassigned` |
| Alexis | El directorio activo, revisado en junio con revisión cada 90 días; el portal de clientes, sin ninguna revisión | `access_review_overdue` ×2 |
| Alexis | La mesa de ayuda externa, evaluada hace más de un año; el centro de datos alterno, crítico y sin evaluar | `third_party_assessment_overdue` ×2 |
| Alexis | Un riesgo aceptado hasta el 30 de septiembre | `risk_acceptance_expired` |
| Guillermo | Una vulnerabilidad crítica en el servidor web desde agosto, y otra en el directorio desde septiembre, pasado el plazo de su severidad | `vuln_past_sla` ×2 |
| Guillermo | Una vulnerabilidad del catálogo KEV abierta en el cortafuegos, con su fecha de corrección el 1 de octubre | `kev_past_due` |
| Guillermo | Una excepción que venció el 30 de septiembre sobre una vulnerabilidad que sigue abierta y fuera de plazo | `vuln_exception_expired`, `vuln_past_sla` |
| Guillermo | Un cierre del 12 de octubre sin escaneo posterior, y uno del 25 de septiembre que el escaneo de octubre sigue encontrando | `vuln_closed_without_rescan` ×2 |
| Guillermo | La VPN, escaneada por última vez en agosto, y una estación de finanzas que nunca se escaneó | `asset_not_scanned` ×2 |
| Amparo | Un incidente alto contenido seis horas después de su plazo, y otro alto que sigue sin contener | `incident_response_late` ×2 |
| Amparo | Un incidente crítico con datos personales notificado al supervisor a las 30 horas, con un plazo de 24; uno con clientes afectados que no se les notificó | `incident_notification_late` ×2 |
| Amparo | Un incidente bajo cerrado en agosto sin revisión posterior | `incident_without_review` |
| Amparo | La recuperación del centro alterno, probada en febrero con frecuencia semestral | `continuity_test_overdue` |
| Amparo | La restauración del correo, probada en junio con frecuencia trimestral; la de la base de clientes, nunca | `restore_test_overdue` ×2 |

Son 25 señales por entidad y 100 en el material, más de las 73 que pide un piso del 95 % sin fallas
(decisión 0020). Cada una de las dieciséis señales de la familia se siembra en las cuatro entidades.

## Lo que se parece a un defecto y no lo es

Está en todas las entidades, y las de control no traen nada más:

- un control que no aplica (A.7.4) y uno en implementación (A.8.28), los dos sin evidencia, y en la
  carpeta de controles un borrador sin aprobar que el agente deja en lo revisado;
- una evidencia mensual del 15 de septiembre, que vence mañana;
- un tercero no crítico sin evaluar, y una aceptación de riesgo que vence hoy;
- una vulnerabilidad baja fuera de plazo con su excepción vigente hasta diciembre;
- una vulnerabilidad del catálogo KEV cuya fecha de corrección todavía no llega;
- una vulnerabilidad cerrada en septiembre que el escaneo siguiente ya no encuentra;
- un activo fuera de alcance sin escanear, y uno escaneado que no está en el inventario;
- una notificación al supervisor hecha justo a las 24 horas;
- una prueba de restauración con observaciones, que cuenta como hecha.

## Lo que el material no prueba

- **La extracción del agente.** `evaluar.py` le da al motor la ficha correcta. Que Alexis lea la
  evidencia, que Amparo lea la línea de tiempo del informe y la hora de cada constancia, y que
  Guillermo y Amparo tomen los plazos de cada política, lo prueba la ronda con los agentes, sobre el
  mismo material.
- **El mapeo del escáner de `salud-pe`.** La clave trae el mapeo que tendría que dejar el setup; que el
  agente lo pregunte y lo registre bien, también lo prueba la ronda.
- **Los formatos propios de un escáner** —Tenable, Qualys, Rapid7, Microsoft Defender—: entran en su
  incremento, cada uno desde su fuente.
- **La documentación de una organización real.** Nada de esto se ha corrido todavía sobre ella.
