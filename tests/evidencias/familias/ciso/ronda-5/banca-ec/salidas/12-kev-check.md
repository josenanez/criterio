# /criterio-vulnerability:kev-check 

Los términos ya estaban vigentes (versión 1.6, aceptada con la 1.5.1), así que no hizo falta registrar una aceptación nueva. El periodo es 2026-10, el que corresponde a la fecha de prueba 2026-10-15.

**Una vulnerabilidad del catálogo KEV sigue abierta pasada su fecha de corrección.** Es la de `bgs-fw-borde-01`, y tiene uso conocido en ransomware.

# Lo explotado: el catálogo KEV · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 1.5.1 · **Comando:** `kev-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vulnerabilidad del catálogo KEV sigue abierta después de su fecha de corrección (`kev_past_due`) | bgs-fw-borde-01 · CVE-2099-12002: está en el catálogo KEV desde el 2026-09-17 con corrección al 2026-10-01, y el escaneo del 2026-10-10 la sigue encontrando · uso conocido en ransomware | — | — | 14 | `50-escaneos/escaneo-2026-10-10.csv` fila 15 · `50-escaneos/known_exploited_vulnerabilities.csv` fila 3 |

## El resultado

**Catálogo KEV:** `50-escaneos/known_exploited_vulnerabilities.csv`, 3 entradas.

| Activo | Vulnerabilidad | Severidad | Abierta desde | Corrección del catálogo |
|---|---|---|---|---|
| bgs-fw-borde-01 | CVE-2099-12002 | alta | 2026-09-20 | 2026-10-01 |
| bgs-web-01 | CVE-2099-11003 | media | 2026-10-10 | 2026-10-29 |

La fecha de corrección es la que trae el catálogo de CISA (F-06); la directiva que la fija obliga a las agencias federales de los Estados Unidos, y el plazo de la organización es el de su política.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-escaneos/escaneo-2026-10-10.csv`
- `50-escaneos/known_exploited_vulnerabilities.csv`
- Fuentes técnicas: F-06 (families/criterio-ciso/FUENTES.es.md)

La salida quedó en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-kev-check.md`. La corrida está registrada como `2026-10-15-kev-check-1`, con 9 hallazgos.