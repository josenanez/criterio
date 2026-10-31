# /criterio-security:security-scan 

Los términos de la versión 1.3 ya estaban vigentes, aceptados a nombre de José Francisco Ñáñez el 2026-10-15, así que seguí. La ficha del periodo 2026-10 ya traía los 18 documentos con la fecha y la cita que dice cada uno. No tuve que agregar nada. El motor calculó 8 señales, y la corrida quedó registrada como `2026-10-15-security-scan-1`.

Tres archivos quedaron sin abrir por ser credenciales, llaves o respaldos: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`.

El inventario también marca tres revisiones en `80-revisiones/` como fuera de lugar. El motor dice que irían en `70-incidentes/`.

# Qué cambió en la seguridad · Energía Andina Sintética · periodo 2026-10

**Entidad:** Energía Andina Sintética (20587654321) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 0.2.0 · **Comando:** `security-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Control implementado sin evidencia (`control_without_evidence`) | A.8.15 · Registro de eventos: figura «Implementado» y la ficha no tiene ninguna evidencia de que operó | Oficial de cumplimiento | — | `00-referencia/declaracion-aplicabilidad.xlsx` fila 12 |
| 2 | Revisión de accesos vencida (`access_review_overdue`) | Directorio activo: la última revisión es del 2026-06-30; tocaba el 2026-09-28 | Jefe de seguridad de la información | 17 | `00-referencia/sistemas.csv` fila 4 · `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1` |
| 3 | Aceptación de riesgo vencida (`risk_acceptance_expired`) | R-03 · Respaldo fuera de sitio a más de 24 horas: aceptado por Comité de riesgos hasta el 2026-09-30, y no se volvió a revisar | Comité de riesgos | 15 | `40-riesgos/registro-riesgos.csv` fila 4 |
| 4 | Evaluación de tercero crítico vencida (`third_party_assessment_overdue`) | Mesa de Ayuda Externa: la última evaluación es del 2025-09-30; tocaba el 2026-09-30 | — | 15 | `00-referencia/terceros.csv` fila 4 · `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1` |
| 5 | Revisión de accesos sin hacer (`access_review_overdue`) | Portal de clientes: ninguna revisión registrada; la tabla pide una cada 180 días | Jefe de seguridad de la información | — | `00-referencia/sistemas.csv` fila 5 |
| 6 | Evaluación de tercero crítico sin hacer (`third_party_assessment_overdue`) | Centro de Datos Alterno: tercero crítico sin ninguna evaluación registrada; el registro pide una cada 365 días | — | — | `00-referencia/terceros.csv` fila 6 |
| 7 | Evidencia de control vencida (`control_evidence_stale`) | A.5.18 · Derechos de acceso: la evidencia más reciente es del 2026-06-30 y su periodicidad es de 92 días; venció el 2026-09-30 | Jefe de infraestructura | 15 | `00-referencia/declaracion-aplicabilidad.xlsx` fila 5 · `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1` |
| 8 | Control aplicable sin responsable (`soa_control_unassigned`) | A.8.24 · Uso de la criptografía: aplicable y sin responsable en la declaración | — | — | `00-referencia/declaracion-aplicabilidad.xlsx` fila 14 |

## El resultado

**En la ficha:** 12 evidencias de controles, 3 revisiones de acceso y 3 evaluaciones de terceros.

**Excluidos por omisión:** 3 archivos (credenciales, llaves o respaldos) que el motor no abre.

## Las preguntas que hizo

- ¿Dejo en la carpeta de la entidad la marca _CRITERIO_SEGURIDAD.txt? → No: la carpeta vino en el argumento y no hay quien autorice crear archivos en ella
- ¿Qué periodo abre la primera ficha? → 2026-10, el mes de la fecha de la prueba

## Fuentes

`declaracion-aplicabilidad.xlsx`, `sistemas.csv`, `terceros.csv`, `registro-riesgos.csv`, y los PDF de A.5.18, del Directorio activo y de Mesa de Ayuda Externa citados arriba.

El reporte completo está en `estado-seguridad/20587654321-energia-andina-sintetica/seguridad/2026-10/reporte-security-scan.md`. La salida que te mostré está en `corridas/salida-security-scan.md`, en esa misma carpeta de estado.