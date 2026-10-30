# /criterio-vulnerability:vuln-scan 

Corrida de prueba sin interfaz: no hubo preguntas. El reporte tiene una contradicción: dice «Nada abierto en lo que procesa este comando» y, a la vez, cuenta abiertas en el último escaneo de cada activo. Conviene revisarlo con `/criterio-vulnerability:vuln-sla` y `/criterio-vulnerability:kev-check`.

# Qué cambió en las vulnerabilidades · Comercial Control Sintética · periodo 2026-10

**Entidad:** Comercial Control Sintética (ccm090101ab3) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 0.1.0 · **Comando:** `vuln-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Escaneo | Fecha | Activos | Hallazgos |
|---|---|---|---|
| `50-escaneos/escaneo-2026-08-20.xlsx` | 2026-08-20 | 8 | 2 |
| `50-escaneos/escaneo-2026-09-20.xlsx` | 2026-09-20 | 10 | 1 |
| `50-escaneos/escaneo-2026-10-10.xlsx` | 2026-10-10 | 9 | 3 |

**Abiertas en el último escaneo de cada activo:** 3 · **Catálogo KEV:** `50-escaneos/known_exploited_vulnerabilities.csv`, 2 entradas.

**Excluidos por omisión:** 3 archivos —credenciales, llaves o respaldos— que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-05, F-06 (families/criterio-ciso/FUENTES.es.md)

La salida quedó en `estado-seguridad/ccm090101ab3-comercial-control-sintetica/corridas/salida-vuln-scan.md`. El motor registró la corrida como `2026-10-15-vuln-scan-1`.