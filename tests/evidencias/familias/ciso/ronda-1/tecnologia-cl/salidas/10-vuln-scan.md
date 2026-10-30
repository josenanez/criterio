# /criterio-vulnerability:vuln-scan 

Los términos estaban vigentes (versión 1.3), así que no hubo que registrar una aceptación nueva. No había exportaciones nuevas en `50-escaneos/`, y el inventario no trae archivos nuevos, cambiados ni borrados. Aquí está el reporte del motor, tal cual:

# Qué cambió en las vulnerabilidades · Nube Austral Software Sintética · periodo 2026-10

**Entidad:** Nube Austral Software Sintética (76543210k) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 0.1.0 · **Comando:** `vuln-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | nub-db-01 · CVE-2099-12003 · Escalamiento en el motor de base de datos: media, abierta desde el 2026-06-01 (136 días) y la política da 60 días | — | — | 76 | `50-escaneos/escaneo-2026-10-10.csv` fila 15 |
| 2 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | nub-web-01 · CVE-2099-12001 · Ejecución remota en el portal: critica, abierta desde el 2026-08-20 (56 días) y la política da 7 días | — | — | 49 | `50-escaneos/escaneo-2026-10-10.csv` fila 13 |
| 3 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | nub-ad-01 · CVE-2099-12006 · Delegación insegura en el directorio: critica, abierta desde el 2026-09-20 (25 días) y la política da 7 días | — | — | 18 | `50-escaneos/escaneo-2026-10-10.csv` fila 18 |
| 4 | Una vulnerabilidad del catálogo KEV sigue abierta después de su fecha de corrección (`kev_past_due`) | nub-fw-borde-01 · CVE-2099-12002: está en el catálogo KEV desde el 2026-09-17 con corrección al 2026-10-01, y el escaneo del 2026-10-10 la sigue encontrando · uso conocido en ransomware | — | — | 14 | `50-escaneos/escaneo-2026-10-10.csv` fila 14 · `50-escaneos/known_exploited_vulnerabilities.csv` fila 3 |
| 5 | Una vulnerabilidad figura cerrada y ningún escaneo posterior la da por corregida (`vuln_closed_without_rescan`) | TK-203 · nub-correo-01 · CVE-2099-12005: figura cerrada el 2026-09-25 y el escaneo del 2026-10-10 la sigue encontrando | — | — | 20 | `60-remediacion/seguimiento.csv` fila 4 · `50-escaneos/escaneo-2026-10-10.csv` |
| 6 | Una excepción a la corrección pasó su vencimiento y la vulnerabilidad sigue abierta (`vuln_exception_expired`) | CVE-2099-12003 en nub-db-01: la excepción venció el 2026-09-30 y la vulnerabilidad sigue abierta en nub-db-01 | — | Gerente de tecnología | 15 | `60-remediacion/excepciones.xlsx` fila 3 · `50-escaneos/escaneo-2026-10-10.csv` fila 15 |
| 7 | Una vulnerabilidad figura cerrada y ningún escaneo posterior la da por corregida (`vuln_closed_without_rescan`) | TK-202 · nub-backup-01 · CVE-2099-12004: figura cerrada el 2026-10-12 y ningún escaneo posterior incluye el activo | — | — | 3 | `60-remediacion/seguimiento.csv` fila 3 |
| 8 | Un activo del inventario no aparece en ningún escaneo de la ventana configurada (`asset_not_scanned`) | nub-vpn-01: el último escaneo que lo incluye es del 2026-08-20; la ventana es de 30 días | — | Jefe de infraestructura | 56 | `00-referencia/inventario-activos.csv` fila 6 |
| 9 | Un activo del inventario no aparece en ningún escaneo de la ventana configurada (`asset_not_scanned`) | nub-ws-finanzas-01: ningún escaneo lo incluye; la ventana es de 30 días | — | Jefe de infraestructura | — | `00-referencia/inventario-activos.csv` fila 10 |

## El resultado

| Escaneo | Fecha | Activos | Hallazgos |
|---|---|---|---|
| `50-escaneos/escaneo-2026-08-20.csv` | 2026-08-20 | 8 | 4 |
| `50-escaneos/escaneo-2026-09-20.csv` | 2026-09-20 | 8 | 7 |
| `50-escaneos/escaneo-2026-10-10.csv` | 2026-10-10 | 8 | 9 |

**Abiertas en el último escaneo de cada activo:** 9 · **Catálogo KEV:** `50-escaneos/known_exploited_vulnerabilities.csv`, 3 entradas.

**Excluidos por omisión:** 3 archivos —credenciales, llaves o respaldos— que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/inventario-activos.csv`
- `50-escaneos/escaneo-2026-10-10.csv`
- `50-escaneos/known_exploited_vulnerabilities.csv`
- `60-remediacion/excepciones.xlsx`
- `60-remediacion/seguimiento.csv`
- Fuentes técnicas: F-05, F-06 (families/criterio-ciso/FUENTES.es.md)

La corrida quedó registrada como `2026-10-15-vuln-scan-1`, con 9 hallazgos. El reporte está en `estado-seguridad/76543210k-nube-austral-software-sintetica/vulnerabilidades/2026-10/reporte-vuln-scan.md`. Lo que te mostré quedó guardado en `estado-seguridad/76543210k-nube-austral-software-sintetica/corridas/salida-vuln-scan.md`.

El inventario también marca tres revisiones (`INC-NUB-101` a `103`) en `80-revisiones/` que irían en `70-incidentes/`. No afectan este reporte.