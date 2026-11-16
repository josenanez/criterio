# /criterio-vulnerability:kev-check 

Los términos están vigentes (versión 1.5). La corrida es con fecha 2026-10-15. Una vulnerabilidad del catálogo KEV sigue abierta pasada su fecha de corrección.

# Lo explotado: el catálogo KEV · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 1.4.0 · **Comando:** `kev-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vulnerabilidad del catálogo KEV sigue abierta después de su fecha de corrección (`kev_past_due`) | bps-fw-borde-01 · CVE-2099-12002: está en el catálogo KEV desde el 2026-09-17 con corrección al 2026-10-01, y el escaneo del 2026-10-10 la sigue encontrando · uso conocido en ransomware | — | — | 14 | `50-escaneos/escaneo-2026-10-10.csv` fila 14 · `50-escaneos/known_exploited_vulnerabilities.csv` fila 3 |

## El resultado

**Catálogo KEV:** `50-escaneos/known_exploited_vulnerabilities.csv`, 3 entradas.

| Activo | Vulnerabilidad | Severidad | Abierta desde | Corrección del catálogo |
|---|---|---|---|---|
| bps-fw-borde-01 | CVE-2099-12002 | alta | 2026-09-20 | 2026-10-01 |
| bps-web-01 | CVE-2099-11003 | media | 2026-10-10 | 2026-10-29 |

La fecha de corrección es la que trae el catálogo de CISA (F-06). La directiva que la fija obliga a las agencias federales de los Estados Unidos, y el plazo de la organización es el de su política.

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

La corrida quedó registrada como `2026-10-15-kev-check-1`. La salida está en `estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-kev-check.md`.

No registré ninguna aceptación de términos con el nombre de José Francisco Ñáñez. Los términos ya figuraban vigentes (aceptada con la versión 1.4.0), así que el agente no pidió aceptarlos y no hizo falta.