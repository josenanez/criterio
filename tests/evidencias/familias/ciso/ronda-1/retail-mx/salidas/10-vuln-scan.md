# /criterio-vulnerability:vuln-scan 

Términos vigentes (versión 1.3). No hay exportaciones nuevas desde la corrida anterior, así que el motor procesó las existentes con fecha 2026-10-15. Tres archivos (credenciales, llave, respaldo) quedaron sin abrir, por diseño.

# Qué cambió en las vulnerabilidades · Tiendas del Bajío Sintéticas · periodo 2026-10

**Entidad:** Tiendas del Bajío Sintéticas (TBA110315K21) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 0.1.0 · **Comando:** `vuln-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Abierta después del plazo de su severidad, sin excepción vigente (`vuln_past_sla`) | tda-db-01 · CVE-2099-12003 · Escalamiento en el motor de base de datos: media, abierta desde el 2026-06-01 (136 días) y la política da 90 días | — | 46 | `50-escaneos/escaneo-2026-10-10.xlsx` fila 15 |
| 2 | Abierta después del plazo (`vuln_past_sla`) | tda-web-01 · CVE-2099-12001 · Ejecución remota en el portal: crítica, abierta desde el 2026-08-20 (56 días) y la política da 15 días | — | 41 | `50-escaneos/escaneo-2026-10-10.xlsx` fila 13 |
| 3 | KEV abierta después de su fecha de corrección (`kev_past_due`) | tda-fw-borde-01 · CVE-2099-12002: en el catálogo KEV desde el 2026-09-17 con corrección al 2026-10-01; el escaneo del 2026-10-10 la sigue encontrando · uso conocido en ransomware | — | 14 | `50-escaneos/escaneo-2026-10-10.xlsx` fila 14 · `50-escaneos/known_exploited_vulnerabilities.csv` fila 3 |
| 4 | Abierta después del plazo (`vuln_past_sla`) | tda-ad-01 · CVE-2099-12006 · Delegación insegura en el directorio: crítica, abierta desde el 2026-09-20 (25 días) y la política da 15 días | — | 10 | `50-escaneos/escaneo-2026-10-10.xlsx` fila 18 |
| 5 | Cerrada sin escaneo que la dé por corregida (`vuln_closed_without_rescan`) | TK-203 · tda-correo-01 · CVE-2099-12005: figura cerrada el 2026-09-25 y el escaneo del 2026-10-10 la sigue encontrando | — | 20 | `60-remediacion/seguimiento.csv` fila 4 · `50-escaneos/escaneo-2026-10-10.xlsx` |
| 6 | Excepción vencida con la vulnerabilidad abierta (`vuln_exception_expired`) | CVE-2099-12003 en tda-db-01: la excepción venció el 2026-09-30 y sigue abierta | Gerente de tecnología | 15 | `60-remediacion/excepciones.xlsx` fila 3 · `50-escaneos/escaneo-2026-10-10.xlsx` fila 15 |
| 7 | Cerrada sin escaneo que la pruebe (`vuln_closed_without_rescan`) | TK-202 · tda-backup-01 · CVE-2099-12004: figura cerrada el 2026-10-12 y ningún escaneo posterior incluye el activo | — | 3 | `60-remediacion/seguimiento.csv` fila 3 |
| 8 | Activo sin escaneo en la ventana (`asset_not_scanned`) | tda-vpn-01: el último escaneo que lo incluye es del 2026-08-20; la ventana es de 30 días | Jefe de infraestructura | 56 | `00-referencia/inventario-activos.csv` fila 6 |
| 9 | Activo sin escaneo en la ventana (`asset_not_scanned`) | tda-ws-finanzas-01: ningún escaneo lo incluye; la ventana es de 30 días | Jefe de infraestructura | — | `00-referencia/inventario-activos.csv` fila 10 |

## El resultado

| Escaneo | Fecha | Activos | Hallazgos |
|---|---|---|---|
| `escaneo-2026-08-20.xlsx` | 2026-08-20 | 8 | 4 |
| `escaneo-2026-09-20.xlsx` | 2026-09-20 | 8 | 7 |
| `escaneo-2026-10-10.xlsx` | 2026-10-10 | 8 | 9 |

**Abiertas en el último escaneo de cada activo:** 9 · **Catálogo KEV:** 3 entradas.

**Excluidos por omisión (no se abren):** `credenciales-vpn.txt`, `servidor-web.pem`, `respaldo-correo-2026-06-20.zip`.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

**Preguntas que hizo:** ninguna en esta corrida. **Fuentes:** inventario de activos, escaneo del 2026-10-10, catálogo KEV, excepciones y seguimiento de remediación; fuentes técnicas F-05 y F-06.

La corrida quedó registrada como `2026-10-15-vuln-scan-1` (9 hallazgos). La salida completa está en `estado-seguridad/tba110315k21-tiendas-del-bajio-sinteticas/corridas/salida-vuln-scan.md`.

Aviso sobre la prueba: la sesión no tenía fecha propia en el entorno (el sistema marca 2026-10-30). Usé `--today 2026-10-15` como se pidió. El motor marcó los términos como vigentes, así que no hizo falta registrar la aceptación a nombre de José Francisco Ñáñez.