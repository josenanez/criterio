# /criterio-vulnerability:vuln-scan 

Corrida terminada y registrada. Esto es lo que mostré:

Corrida sin interfaz: los términos ya estaban vigentes para esta versión, a nombre de José Francisco Ñáñez, y no hubo preguntas que responder. Las tres exportaciones del escáner están en `.json.gz`, formato que el inventario marca como no soportado, pero el cálculo las procesó y el reporte las cita.

# Qué cambió en las vulnerabilidades · Seguros del Sur Sintéticos · periodo 2026-10

**Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo 0.2.0

## Lo que hay que atender (7 señales)

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | `vuln_past_sla` | seg-db-01 · CVE-2099-12003: media, abierta desde 2026-06-01 (136 días); la política da 60 | 76 | escaneo 2026-10-10 fila 7 |
| 2 | `vuln_past_sla` | seg-web-01 · CVE-2099-12001: crítica, abierta desde 2026-08-20 (56 días); la política da 10 | 46 | escaneo 2026-10-10 fila 5 |
| 3 | `vuln_past_sla` | seg-ad-01 · CVE-2099-12006: crítica, abierta desde 2026-09-20 (25 días); la política da 10 | 15 | escaneo 2026-10-10 fila 10 |
| 4 | `kev_past_due` | seg-fw-borde-01 · CVE-2099-12002: en KEV desde 2026-09-17, corrección al 2026-10-01, sigue abierta; uso conocido en ransomware | 14 | escaneo fila 6 · KEV fila 3 |
| 5 | `vuln_closed_without_rescan` | TK-203 · seg-correo-01 · CVE-2099-12005: cerrada el 2026-09-25 y el escaneo del 2026-10-10 la sigue encontrando | 20 | `seguimiento.csv` fila 4 |
| 6 | `vuln_exception_expired` | CVE-2099-12003 en seg-db-01: la excepción venció el 2026-09-30 y sigue abierta (responsable: Gerente de tecnología) | 15 | `excepciones.xlsx` fila 3 |
| 7 | `vuln_closed_without_rescan` | TK-202 · seg-backup-01 · CVE-2099-12004: cerrada el 2026-10-12 y ningún escaneo posterior incluye el activo | 3 | `seguimiento.csv` fila 3 |

## El resultado

| Escaneo | Fecha | Activos | Hallazgos |
|---|---|---|---|
| `escaneo-2026-08-20.json.gz` | 2026-08-20 | 3 | 4 |
| `escaneo-2026-09-20.json.gz` | 2026-09-20 | 7 | 7 |
| `escaneo-2026-10-10.json.gz` | 2026-10-10 | 7 | 9 |

**Abiertas en el último escaneo de cada activo:** 9. **Catálogo KEV:** 3 entradas.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante.

## Lo que no se pudo procesar

- Excluidos por omisión, sin abrirse: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`.
- `50-escaneos/`: las exportaciones de Microsoft Defender listan vulnerabilidades, no los equipos escaneados. La cobertura del inventario no se calcula sin otra exportación que lo diga.

## Las preguntas que hizo

Ninguna en esta corrida.

**Dónde quedó:**
- La salida está en `estado-seguridad/965123456-seguros-del-sur-sinteticos/corridas/salida-vuln-scan.md`.
- La corrida quedó registrada como `2026-10-15-vuln-scan-1`, con 7 hallazgos.

**Dos cosas que no calculé yo:**
- El comando `inventario` clasificó los tres `.json.gz` como ilegibles (formato no soportado). Aun así, `compute` y `reporte` los leyeron y los citan como fuente. Conviene revisar por qué las dos herramientas no coinciden.
- Los tres informes de `80-revisiones/` aparecen como fuera de lugar (irían en `70-incidentes/`). Es un asunto de otro agente y no lo toqué.