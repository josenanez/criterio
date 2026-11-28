# /criterio-vulnerability:vuln-setup seguridad/1790987654001-banco-del-guayas-sintetico

Guillermo quedó instalado para Banco del Guayas Sintético (RUC 1790987654001) y la primera ficha de 2026-10 marca cuatro vulnerabilidades o excepciones que ya pasaron su plazo.

Las preguntas se resolvieron con la respuesta sugerida:
- **Plazos:** crítica 15, alta 30, media 60 y baja 120 días. Salen de la sección 4 de `politica-gestion-vulnerabilidades.pdf`.
- **Ventana de escaneo:** 30 días, porque la sección 5 pide escanear al menos una vez al mes.
- **Escáner:** Tenable. Reconoció todas las columnas de las tres exportaciones y no registré ninguna columna adicional.
- **Rostrum:** no se publica.
- **Entidad y estado:** los tomé del setup de Alexis.

**Qué no abrí:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`.

**Archivos:**
- La configuración quedó en `.criterio/vulnerabilidades/1790987654001/config.json`.
- Los términos los aceptó José Francisco Ñáñez, con fecha 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-vulnerability-1.5.1-2026-10-15.md` y `.pdf`.
- La corrida quedó registrada como `2026-10-15-vuln-setup-1`.

**Para tener en cuenta:**
- El catálogo KEV trae solo 3 filas. Si no es el catálogo completo, conviene descargarlo de nuevo de CISA.
- El cálculo también encontró señales del catálogo KEV y de la cobertura de escaneo que este reporte no muestra. Se ven con `/criterio-vulnerability:kev-check` y `/criterio-vulnerability:scan-coverage`.

---

# Las vulnerabilidades contra su plazo · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 1.5.1 · **Comando:** `vuln-sla`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | bgs-db-01 · CVE-2099-12003 · Escalamiento en el motor de base de datos: media, abierta desde el 2026-06-01 (136 días) y la política da 60 días | — | — | 76 | `50-escaneos/escaneo-2026-10-10.csv` fila 16 |
| 2 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | bgs-web-01 · CVE-2099-12001 · Ejecución remota en el portal: critica, abierta desde el 2026-08-20 (56 días) y la política da 15 días | — | — | 41 | `50-escaneos/escaneo-2026-10-10.csv` fila 14 |
| 3 | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente (`vuln_past_sla`) | bgs-ad-01 · CVE-2099-12006 · Delegación insegura en el directorio: critica, abierta desde el 2026-09-20 (25 días) y la política da 15 días | — | — | 10 | `50-escaneos/escaneo-2026-10-10.csv` fila 19 |
| 4 | Una excepción a la corrección pasó su vencimiento y la vulnerabilidad sigue abierta (`vuln_exception_expired`) | CVE-2099-12003 en bgs-db-01: la excepción venció el 2026-09-30 y la vulnerabilidad sigue abierta en bgs-db-01 | — | Gerente de tecnología | 15 | `60-remediacion/excepciones.csv` fila 3 · `50-escaneos/escaneo-2026-10-10.csv` fila 16 |

## El resultado

**Plazos de la política:** critica 15 días · alta 30 días · media 60 días · baja 120 días

| Activo | Vulnerabilidad | Severidad | Abierta desde | Días | Plazo | Excepción hasta |
|---|---|---|---|---|---|---|
| bgs-ad-01 | CVE-2099-12006 · Delegación insegura en el directorio | critica | 2026-09-20 | 25 | 15 | — |
| bgs-app-01 | 40001 · Suites de cifrado débiles | baja | 2026-02-01 | 256 | 120 | 2026-12-31 |
| bgs-backup-01 | CVE-2099-12004 · Servicio de respaldo expuesto | media | 2026-09-20 | 25 | 60 | — |
| bgs-correo-01 | CVE-2099-12005 · Inyección en el servidor de correo | alta | 2026-09-20 | 25 | 30 | — |
| bgs-db-01 | CVE-2099-12003 · Escalamiento en el motor de base de datos | media | 2026-06-01 | 136 | 60 | 2026-09-30 |
| bgs-fw-borde-01 | CVE-2099-12002 · Omisión de autenticación en el cortafuegos | alta | 2026-09-20 | 25 | 30 | — |
| bgs-web-01 | CVE-2099-11001 · Cabecera de seguridad ausente | baja | 2026-10-10 | 5 | 120 | — |
| bgs-web-01 | CVE-2099-11003 · Desbordamiento en el servidor web | media | 2026-10-10 | 5 | 60 | — |
| bgs-web-01 | CVE-2099-12001 · Ejecución remota en el portal | critica | 2026-08-20 | 56 | 15 | — |

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

---

**Cuándo vuelvo:** sin reloj. La tarea programada pide un sí explícito y esta prueba no lo dio; además, este equipo no tiene `crontab`. Para correrlo a mano: `/criterio-vulnerability:vuln-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.