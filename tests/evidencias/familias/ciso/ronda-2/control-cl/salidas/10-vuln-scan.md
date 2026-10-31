# /criterio-vulnerability:vuln-scan 

Términos vigentes (versión 1.3); no hubo preguntas. El reporte tiene una contradicción que no resolví. El encabezado dice "Nada abierto en lo que procesa este comando", pero el resultado cuenta 3 abiertas en el último escaneo de cada activo. Las cifras son las del motor.

# Qué cambió en las vulnerabilidades · Aseguradora Control Sintética · periodo 2026-10

**Entidad:** Aseguradora Control Sintética (966778890) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 0.2.0 · **Comando:** `vuln-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Escaneo | Fecha | Activos | Hallazgos |
|---|---|---|---|
| `50-escaneos/escaneo-2026-08-20.json.gz` | 2026-08-20 | 1 | 2 |
| `50-escaneos/escaneo-2026-09-20.json.gz` | 2026-09-20 | 1 | 1 |
| `50-escaneos/escaneo-2026-10-10.json.gz` | 2026-10-10 | 2 | 3 |

**Abiertas en el último escaneo de cada activo:** 3 · **Catálogo KEV:** `50-escaneos/known_exploited_vulnerabilities.csv`, 2 entradas.

**Excluidos por omisión:** 3 archivos (credenciales, llaves o respaldos) que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión; por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión; .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión; .zip es una llave, una credencial o un respaldo.
- `50-escaneos/`: las exportaciones de Microsoft Defender listan vulnerabilidades, no los equipos escaneados. La cobertura del inventario no se calcula sin otra exportación que lo diga.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-05, F-06, F-09 (families/criterio-ciso/FUENTES.es.md)

La salida quedó en `estado-seguridad/966778890-aseguradora-control-sintetica/corridas/salida-vuln-scan.md`. La corrida quedó registrada como `2026-10-15-vuln-scan-1`.

No registré la aceptación de términos porque no hizo falta: ya estaban vigentes. Por eso José Francisco Ñáñez no aparece en ningún registro de esta corrida.