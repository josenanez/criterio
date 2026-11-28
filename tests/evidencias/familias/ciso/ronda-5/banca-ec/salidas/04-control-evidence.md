# /criterio-security:control-evidence 

Términos vigentes. Este es el cruce de cada control aplicable contra su evidencia: hay dos controles que atender, uno sin ninguna evidencia y otro con la evidencia vencida.

# Los controles contra su evidencia · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Agente:** Alexis, versión 1.5.1 · **Comando:** `control-evidence`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Control aplicable implementado sin ninguna evidencia de que operó (`control_without_evidence`) | A.8.15 · Registro de eventos: figura «Implementado» y la ficha no tiene ninguna evidencia | Oficial de cumplimiento | — | `00-referencia/declaracion-aplicabilidad.xlsx` fila 12 |
| 2 | Evidencia más reciente anterior a su periodicidad (`control_evidence_stale`) | A.5.18 · Derechos de acceso: la evidencia más reciente es del 2026-06-30, su periodicidad es de 92 días y venció el 2026-09-30 | Jefe de infraestructura | 15 | `00-referencia/declaracion-aplicabilidad.xlsx` fila 5 · `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1` |

## El resultado

| Control | Estado | Evidencias | La más reciente | Vence |
|---|---|---|---|---|
| 5.1 · Políticas de seguridad de la información | Implementado | 1 | 2026-02-20 | 2027-02-21 |
| 5.9 · Inventario de información y otros activos | Implementado | 1 | 2026-07-31 | 2027-01-30 |
| 5.15 · Control de acceso | Implementado | 1 | 2026-09-30 | 2026-12-31 |
| 5.18 · Derechos de acceso | Implementado | 1 | 2026-06-30 | 2026-09-30 |
| 5.19 · Seguridad en las relaciones con proveedores | Implementado | 1 | 2026-03-15 | 2027-03-16 |
| 5.24 · Preparación para la gestión de incidentes | Implementado | 1 | 2026-01-30 | 2027-01-31 |
| 5.30 · Preparación de las TIC para la continuidad | Implementado | 1 | 2026-04-10 | 2027-04-11 |
| 8.7 · Protección contra el malware | Implementado | 1 | 2026-09-30 | 2026-10-31 |
| 8.8 · Gestión de las vulnerabilidades técnicas | Implementado | 1 | 2026-09-30 | 2026-10-31 |
| 8.13 · Copias de seguridad de la información | Implementado | 1 | 2026-09-30 | 2026-10-31 |
| 8.15 · Registro de eventos | Implementado | 0 | — | — |
| 8.16 · Actividades de seguimiento | Implementado | 1 | 2026-09-15 | 2026-10-16 |
| 8.24 · Uso de la criptografía | Implementado | 1 | 2026-05-20 | 2027-05-21 |
| 8.28 · Codificación segura | En implementación | 0 | — | — |

Ningún control se declara cumplido aquí: se dice cuál no tiene evidencia de que operó.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión (credencial o llave por su nombre)
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión (.pem es una llave, una credencial o un respaldo)
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión (.zip es una llave, una credencial o un respaldo)

## Las preguntas que hizo

Las ocho se tomaron con la respuesta sugerida. La tarea diaria de security-wake quedó sin programar, porque nadie dio un sí explícito. La aceptación de los términos 1.6 quedó a nombre de José Francisco Ñáñez, 2026-10-15.

## Fuentes

- `00-referencia/declaracion-aplicabilidad.xlsx`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`

La corrida quedó registrada como `2026-10-15-control-evidence-1`, con 8 hallazgos. Lo que te mostré está en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-control-evidence.md`.

Dos cosas que no coinciden con lo que pedía la prueba:
- **Fecha del sistema:** la del sistema es 2026-11-28, pero todas las llamadas al motor llevaron `--today 2026-10-15`, como indicaste.
- **Reporte en disco:** el motor imprimió el reporte en pantalla. No comprobé que además lo guardara en `reporte-control-evidence.md`.