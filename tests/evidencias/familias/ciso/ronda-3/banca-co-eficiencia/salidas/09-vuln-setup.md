# /criterio-vulnerability:vuln-setup seguridad/901555123-banco-cordillera-sintetico

Soy Guillermo. Pongo cada vulnerabilidad del escáner al lado del plazo para corregirla; no corro escaneos ni apruebo excepciones.

**Carpeta:** `seguridad/901555123-banco-cordillera-sintetico` (venía en el argumento).

**Lo que no abro** (el motor los excluye por omisión):
- `00-referencia/credenciales-vpn.txt`: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: .zip es una llave, una credencial o un respaldo

**Sugerencia sobre la estructura (no moví nada):** según el motor, `80-revisiones/INC-BCO-101_revision.md`, `INC-BCO-102_revision.md` e `INC-BCO-103_revision.md` irían en `70-incidentes/`.

**Exportaciones del escáner** (`50-escaneos/`):
- Procesé tres: `escaneo-2026-08-20.csv` (12 filas), `escaneo-2026-09-20.csv` (15) y `escaneo-2026-10-10.csv` (17).
- En las tres reconocí estas columnas: activo `Host`, vulnerabilidad `CVE`, título `Name`, severidad `Risk`, CVSS `CVSS v4.0 Base Score` y primera detección `First Found`. La fecha va en el nombre del archivo y no falta ninguna columna.
- El motor no identifica al fabricante, así que las procesa por sus columnas y `scanner.product` queda vacío.
- `known_exploited_vulnerabilities.csv` es el catálogo KEV de CISA, no una exportación del escáner. Por eso `escaneo` no le encuentra una columna de activo. No registré ninguna en `scanner.columns`.

**Respuestas, tomadas de los documentos:**
- **Entidad:** Banco Cordillera Sintético, 901555123, CO. Las fijó el setup de Alexis.
- **Periodo:** 2026-10.
- **Plazos:** crítica 15, alta 30, media 60 y baja 120 días calendario desde la primera detección. Salen de `00-referencia/politica-gestion-vulnerabilidades.pdf`, sección 4 «Plazos de corrección».
- **Cada cuánto se escanea un activo:** 30 días. Sale de la sección 5 de la misma política: «al menos una vez al mes».
- **Catálogo KEV:** sí, está en `50-escaneos/` como lo descargó la organización.
- **Publicar en Rostrum:** no (`vulnerability.publish: false`).
- **Dónde guardo lo que encuentro:** `estado-seguridad/901555123-banco-cordillera-sintetico`.
- **Marca `_CRITERIO_SEGURIDAD.txt`:** no la dejé, porque sin un sí de la persona no se crea.
- **Términos:** «Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal». Los aceptó José Francisco Ñáñez el 2026-10-15. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-vulnerability-1.2.3-2026-10-15.md` y `.pdf`.

**Configuración:** `.criterio/vulnerabilidades/901555123/config.json`. El motor la validó sin problemas.

Al calcular el periodo, el motor también encontró señales que este reporte no muestra: una vulnerabilidad del catálogo KEV vencida, cierres sin un escaneo posterior que los pruebe y activos sin escanear. Las muestran `/criterio-vulnerability:kev-check` y `/criterio-vulnerability:scan-coverage`.

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

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque nadie dio un sí. Para correrlo a mano: `/criterio-vulnerability:vuln-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---
Dejé la corrida registrada como `2026-10-15-vuln-setup-1`, con la salida en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-vuln-setup.md`.