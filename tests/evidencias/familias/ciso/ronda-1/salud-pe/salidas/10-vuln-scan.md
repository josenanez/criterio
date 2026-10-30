# /criterio-vulnerability:vuln-scan 

Los términos ya estaban vigentes (versión 1.3), así que no registré ninguna aceptación. No hay exportaciones nuevas desde la corrida anterior, por eso no corrí `escaneo`. El periodo es 2026-10 y la fecha de la prueba es 2026-10-15.

# Qué cambió en las vulnerabilidades · Clínica del Pacífico Sintética · periodo 2026-10

**Entidad:** Clínica del Pacífico Sintética (20512345678) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 0.1.0 · **Comando:** `vuln-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Abierta después del plazo de su severidad, sin excepción vigente (`vuln_past_sla`) | cli-db-01 · CVE-2099-12003 · Escalamiento en el motor de base de datos: media, abierta desde el 2026-06-01 (136 días) y la política da 90 días | — | 46 | `50-escaneos/escaneo-2026-10-10.csv` fila 15 |
| 2 | Ídem (`vuln_past_sla`) | cli-web-01 · CVE-2099-12001 · Ejecución remota en el portal: crítica, abierta desde el 2026-08-20 (56 días) y la política da 10 días | — | 46 | `50-escaneos/escaneo-2026-10-10.csv` fila 13 |
| 3 | Ídem (`vuln_past_sla`) | cli-ad-01 · CVE-2099-12006 · Delegación insegura en el directorio: crítica, abierta desde el 2026-09-20 (25 días) y la política da 10 días | — | 15 | `50-escaneos/escaneo-2026-10-10.csv` fila 18 |
| 4 | KEV abierta después de su fecha de corrección (`kev_past_due`) | cli-fw-borde-01 · CVE-2099-12002: en el catálogo KEV desde el 2026-09-17 con corrección al 2026-10-01, y el escaneo del 2026-10-10 la sigue encontrando · uso conocido en ransomware | — | 14 | `50-escaneos/escaneo-2026-10-10.csv` fila 14 · `50-escaneos/known_exploited_vulnerabilities.csv` fila 3 |
| 5 | Figura cerrada y ningún escaneo posterior la da por corregida (`vuln_closed_without_rescan`) | TK-203 · cli-correo-01 · CVE-2099-12005: cerrada el 2026-09-25 y el escaneo del 2026-10-10 la sigue encontrando | — | 20 | `60-remediacion/seguimiento.xlsx` fila 4 · `50-escaneos/escaneo-2026-10-10.csv` |
| 6 | Excepción vencida con la vulnerabilidad aún abierta (`vuln_exception_expired`) | CVE-2099-12003 en cli-db-01: la excepción venció el 2026-09-30 | Gerente de tecnología | 15 | `60-remediacion/excepciones.csv` fila 3 · `50-escaneos/escaneo-2026-10-10.csv` fila 15 |
| 7 | Figura cerrada sin escaneo posterior (`vuln_closed_without_rescan`) | TK-202 · cli-backup-01 · CVE-2099-12004: cerrada el 2026-10-12 y ningún escaneo posterior incluye el activo | — | 3 | `60-remediacion/seguimiento.xlsx` fila 3 |
| 8 | Activo sin escaneo en la ventana (`asset_not_scanned`) | cli-vpn-01: el último escaneo que lo incluye es del 2026-08-20; la ventana es de 30 días | Jefe de infraestructura | 56 | `00-referencia/inventario-activos.xlsx` fila 6 |
| 9 | Ídem (`asset_not_scanned`) | cli-ws-finanzas-01: ningún escaneo lo incluye; la ventana es de 30 días | Jefe de infraestructura | — | `00-referencia/inventario-activos.xlsx` fila 10 |

## El resultado

| Escaneo | Fecha | Activos | Hallazgos |
|---|---|---|---|
| `50-escaneos/escaneo-2026-08-20.csv` | 2026-08-20 | 8 | 4 |
| `50-escaneos/escaneo-2026-09-20.csv` | 2026-09-20 | 8 | 7 |
| `50-escaneos/escaneo-2026-10-10.csv` | 2026-10-10 | 8 | 9 |

**Abiertas en el último escaneo de cada activo:** 9 · **Catálogo KEV:** `50-escaneos/known_exploited_vulnerabilities.csv`, 3 entradas.

**Excluidos por omisión:** 3 archivos que el motor no abre (credenciales, llaves o respaldos): `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

Los mismos 3 archivos excluidos por omisión.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/inventario-activos.xlsx`
- `50-escaneos/escaneo-2026-10-10.csv`
- `50-escaneos/known_exploited_vulnerabilities.csv`
- `60-remediacion/excepciones.csv`
- `60-remediacion/seguimiento.xlsx`
- Fuentes técnicas: F-05, F-06 (families/criterio-ciso/FUENTES.es.md)

---

**Anotaciones del inventario.** Tres archivos de `80-revisiones/` (`INC-CLI-101_revision.md`, `INC-CLI-102_revision.md` e `INC-CLI-103_revision.md`) aparecen como "fuera de lugar": el motor dice que irían en `70-incidentes/`. Dos archivos más, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`, salen como ilegibles porque su formato no es compatible.

**Corrida registrada.** Guardé el reporte en `estado-seguridad/20512345678-clinica-del-pacifico-sintetica/corridas/salida-vuln-scan.md` y quedó registrada como `2026-10-15-vuln-scan-1`, con 9 hallazgos. Guardé ese archivo copiando el reporte del motor tal cual. No incluye las dos líneas de contexto del comienzo ni estas anotaciones del inventario.