# /criterio-vulnerability:vuln-scan 

Corrida de prueba del 2026-10-15, sin preguntas. Los términos ya estaban vigentes, así que no registré ninguna aceptación. No había exportaciones nuevas, y el reporte procesa las que ya estaban.

# Qué cambió en las vulnerabilidades · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 0.1.0 · **Comando:** `vuln-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Abierta fuera del plazo de la política, sin excepción vigente (`vuln_past_sla`) | bco-db-01 · CVE-2099-12003 · Escalamiento en el motor de base de datos: media, abierta desde el 2026-06-01 (136 días) y la política da 60 días | — | 76 | `50-escaneos/escaneo-2026-10-10.csv` fila 15 |
| 2 | Abierta fuera del plazo de la política, sin excepción vigente (`vuln_past_sla`) | bco-web-01 · CVE-2099-12001 · Ejecución remota en el portal: critica, abierta desde el 2026-08-20 (56 días) y la política da 15 días | — | 41 | `50-escaneos/escaneo-2026-10-10.csv` fila 13 |
| 3 | KEV abierta después de su fecha de corrección (`kev_past_due`) | bco-fw-borde-01 · CVE-2099-12002: está en el catálogo KEV desde el 2026-09-17 con corrección al 2026-10-01, y el escaneo del 2026-10-10 la sigue encontrando · uso conocido en ransomware | — | 14 | `50-escaneos/escaneo-2026-10-10.csv` fila 14 · `50-escaneos/known_exploited_vulnerabilities.csv` fila 3 |
| 4 | Abierta fuera del plazo de la política, sin excepción vigente (`vuln_past_sla`) | bco-ad-01 · CVE-2099-12006 · Delegación insegura en el directorio: critica, abierta desde el 2026-09-20 (25 días) y la política da 15 días | — | 10 | `50-escaneos/escaneo-2026-10-10.csv` fila 18 |
| 5 | Figura cerrada y ningún escaneo posterior la da por corregida (`vuln_closed_without_rescan`) | TK-203 · bco-correo-01 · CVE-2099-12005: figura cerrada el 2026-09-25 y el escaneo del 2026-10-10 la sigue encontrando | — | 20 | `60-remediacion/seguimiento.xlsx` fila 4 · `50-escaneos/escaneo-2026-10-10.csv` |
| 6 | Excepción vencida con la vulnerabilidad aún abierta (`vuln_exception_expired`) | CVE-2099-12003 en bco-db-01: la excepción venció el 2026-09-30 y la vulnerabilidad sigue abierta en bco-db-01 | Gerente de tecnología | 15 | `60-remediacion/excepciones.csv` fila 3 · `50-escaneos/escaneo-2026-10-10.csv` fila 15 |
| 7 | Figura cerrada y ningún escaneo posterior la da por corregida (`vuln_closed_without_rescan`) | TK-202 · bco-backup-01 · CVE-2099-12004: figura cerrada el 2026-10-12 y ningún escaneo posterior incluye el activo | — | 3 | `60-remediacion/seguimiento.xlsx` fila 3 |
| 8 | Activo sin escaneo en la ventana configurada (`asset_not_scanned`) | bco-vpn-01: el último escaneo que lo incluye es del 2026-08-20; la ventana es de 30 días | Jefe de infraestructura | 56 | `00-referencia/inventario-activos.xlsx` fila 6 |
| 9 | Activo sin escaneo en la ventana configurada (`asset_not_scanned`) | bco-ws-finanzas-01: ningún escaneo lo incluye; la ventana es de 30 días | Jefe de infraestructura | — | `00-referencia/inventario-activos.xlsx` fila 10 |

## El resultado

| Escaneo | Fecha | Activos | Hallazgos |
|---|---|---|---|
| `escaneo-2026-08-20.csv` | 2026-08-20 | 8 | 4 |
| `escaneo-2026-09-20.csv` | 2026-09-20 | 8 | 7 |
| `escaneo-2026-10-10.csv` | 2026-10-10 | 8 | 9 |

**Abiertas en el último escaneo de cada activo:** 9 · **Catálogo KEV:** 3 entradas.

**Excluidos por omisión (no se abren):** `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

**Preguntas que hizo:** ninguna. **Fuentes:** `inventario-activos.xlsx`, `escaneo-2026-10-10.csv`, `known_exploited_vulnerabilities.csv`, `excepciones.csv`, `seguimiento.xlsx`, y F-05 y F-06 (families/criterio-ciso/FUENTES.es.md).

El reporte completo está en `estado-seguridad/901555123-banco-cordillera-sintetico/vulnerabilidades/2026-10/reporte-vuln-scan.md`. La salida de esta corrida quedó en `corridas/salida-vuln-scan.md` y la corrida se registró como `2026-10-15-vuln-scan-1`, con 9 hallazgos.

Aparte, el inventario marcó tres archivos de `80-revisiones/` que irían en `70-incidentes/`. Es solo un aviso.