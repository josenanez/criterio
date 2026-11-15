# /criterio-vulnerability:vuln-sla 

Términos vigentes (versión 1.5, aceptada). Tres vulnerabilidades siguen abiertas fuera de plazo y una excepción venció con la vulnerabilidad aún abierta; el detalle está en el reporte.

# Las vulnerabilidades contra su plazo · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 1.2.3 · **Comando:** `vuln-sla`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | bco-db-01 · CVE-2099-12003 · Escalamiento en el motor de base de datos: media, abierta desde el 2026-06-01 (136 días) y la política da 60 días | — | — | 76 | `50-escaneos/escaneo-2026-10-10.csv` fila 15 |
| 2 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | bco-web-01 · CVE-2099-12001 · Ejecución remota en el portal: critica, abierta desde el 2026-08-20 (56 días) y la política da 15 días | — | — | 41 | `50-escaneos/escaneo-2026-10-10.csv` fila 13 |
| 3 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | bco-ad-01 · CVE-2099-12006 · Delegación insegura en el directorio: critica, abierta desde el 2026-09-20 (25 días) y la política da 15 días | — | — | 10 | `50-escaneos/escaneo-2026-10-10.csv` fila 18 |
| 4 | Una excepción a la corrección pasó su vencimiento y la vulnerabilidad sigue abierta (`vuln_exception_expired`) | CVE-2099-12003 en bco-db-01: la excepción venció el 2026-09-30 y la vulnerabilidad sigue abierta en bco-db-01 | — | Gerente de tecnología | 15 | `60-remediacion/excepciones.csv` fila 3 · `50-escaneos/escaneo-2026-10-10.csv` fila 15 |

## El resultado

**Plazos de la política:** critica 15 días · alta 30 días · media 60 días · baja 120 días

| Activo | Vulnerabilidad | Severidad | Abierta desde | Días | Plazo | Excepción hasta |
|---|---|---|---|---|---|---|
| bco-ad-01 | CVE-2099-12006 · Delegación insegura en el directorio | critica | 2026-09-20 | 25 | 15 | — |
| bco-app-01 | TLS-DEBIL · Suites de cifrado débiles | baja | 2026-02-01 | 256 | 120 | 2026-12-31 |
| bco-backup-01 | CVE-2099-12004 · Servicio de respaldo expuesto | media | 2026-09-20 | 25 | 60 | — |
| bco-correo-01 | CVE-2099-12005 · Inyección en el servidor de correo | alta | 2026-09-20 | 25 | 30 | — |
| bco-db-01 | CVE-2099-12003 · Escalamiento en el motor de base de datos | media | 2026-06-01 | 136 | 60 | 2026-09-30 |
| bco-fw-borde-01 | CVE-2099-12002 · Omisión de autenticación en el cortafuegos | alta | 2026-09-20 | 25 | 30 | — |
| bco-web-01 | CVE-2099-11001 · Cabecera de seguridad ausente | baja | 2026-10-10 | 5 | 120 | — |
| bco-web-01 | CVE-2099-11003 · Desbordamiento en el servidor web | media | 2026-10-10 | 5 | 60 | — |
| bco-web-01 | CVE-2099-12001 · Ejecución remota en el portal | critica | 2026-08-20 | 56 | 15 | — |

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-escaneos/escaneo-2026-10-10.csv`
- `60-remediacion/excepciones.csv`
- Fuentes técnicas: F-05 (families/criterio-ciso/FUENTES.es.md)

La corrida quedó registrada como `2026-10-15-vuln-sla-1`. Los términos ya estaban vigentes, así que no registré ninguna aceptación nueva.