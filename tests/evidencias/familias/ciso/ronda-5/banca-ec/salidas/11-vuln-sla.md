# /criterio-vulnerability:vuln-sla 

Tres vulnerabilidades siguen abiertas fuera de plazo y no tienen una excepción vigente. Una cuarta alerta es una excepción que venció con su vulnerabilidad aún abierta. Las cifras y fechas son las que calculó el motor, con corte 2026-10-15.

Los términos estaban vigentes (versión 1.6, aceptada con la 1.5.1), así que no hizo falta registrar de nuevo la aceptación de José Francisco Ñáñez.

# Las vulnerabilidades contra su plazo · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 1.5.1 · **Comando:** `vuln-sla`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Abierta después del plazo, sin excepción vigente (`vuln_past_sla`) | bgs-db-01 · CVE-2099-12003 · Escalamiento en el motor de base de datos: media, abierta desde el 2026-06-01 (136 días) y la política da 60 días | — | 76 | `50-escaneos/escaneo-2026-10-10.csv` fila 16 |
| 2 | Abierta después del plazo, sin excepción vigente (`vuln_past_sla`) | bgs-web-01 · CVE-2099-12001 · Ejecución remota en el portal: crítica, abierta desde el 2026-08-20 (56 días) y la política da 15 días | — | 41 | `50-escaneos/escaneo-2026-10-10.csv` fila 14 |
| 3 | Abierta después del plazo, sin excepción vigente (`vuln_past_sla`) | bgs-ad-01 · CVE-2099-12006 · Delegación insegura en el directorio: crítica, abierta desde el 2026-09-20 (25 días) y la política da 15 días | — | 10 | `50-escaneos/escaneo-2026-10-10.csv` fila 19 |
| 4 | Una excepción pasó su vencimiento y la vulnerabilidad sigue abierta (`vuln_exception_expired`) | CVE-2099-12003 en bgs-db-01: la excepción venció el 2026-09-30 y la vulnerabilidad sigue abierta | Gerente de tecnología | 15 | `60-remediacion/excepciones.csv` fila 3 · `50-escaneos/escaneo-2026-10-10.csv` fila 16 |

## El resultado

**Plazos de la política:** crítica 15 días · alta 30 días · media 60 días · baja 120 días

| Activo | Vulnerabilidad | Severidad | Abierta desde | Días | Plazo | Excepción hasta |
|---|---|---|---|---|---|---|
| bgs-ad-01 | CVE-2099-12006 · Delegación insegura en el directorio | crítica | 2026-09-20 | 25 | 15 | — |
| bgs-app-01 | 40001 · Suites de cifrado débiles | baja | 2026-02-01 | 256 | 120 | 2026-12-31 |
| bgs-backup-01 | CVE-2099-12004 · Servicio de respaldo expuesto | media | 2026-09-20 | 25 | 60 | — |
| bgs-correo-01 | CVE-2099-12005 · Inyección en el servidor de correo | alta | 2026-09-20 | 25 | 30 | — |
| bgs-db-01 | CVE-2099-12003 · Escalamiento en el motor de base de datos | media | 2026-06-01 | 136 | 60 | 2026-09-30 |
| bgs-fw-borde-01 | CVE-2099-12002 · Omisión de autenticación en el cortafuegos | alta | 2026-09-20 | 25 | 30 | — |
| bgs-web-01 | CVE-2099-11001 · Cabecera de seguridad ausente | baja | 2026-10-10 | 5 | 120 | — |
| bgs-web-01 | CVE-2099-11003 · Desbordamiento en el servidor web | media | 2026-10-10 | 5 | 60 | — |
| bgs-web-01 | CVE-2099-12001 · Ejecución remota en el portal | crítica | 2026-08-20 | 56 | 15 | — |

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión (por su nombre es una credencial o una llave).
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión (.pem es una llave, una credencial o un respaldo).
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión (.zip es una llave, una credencial o un respaldo).

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-escaneos/escaneo-2026-10-10.csv`
- `60-remediacion/excepciones.csv`
- Fuentes técnicas: F-05 (families/criterio-ciso/FUENTES.es.md)

La corrida quedó registrada como `2026-10-15-vuln-sla-1`, con 9 hallazgos. El texto mostrado está guardado en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-vuln-sla.md`, y el reporte del motor en `vulnerabilidades/2026-10/reporte-vuln-sla.md` de esa misma carpeta.

El archivo `salida-vuln-sla.md` guarda el reporte del motor tal cual, con la frase introductoria en una línea al principio. Aquí mostré el reporte en un formato un poco más corto, sin la columna "Monto" y con "crítica" acentuada. Si hace falta que el archivo y lo mostrado coincidan palabra por palabra, hay que volver a escribir el archivo.