# /criterio-vulnerability:vuln-setup seguridad/12345678000195-banco-paulista-sintetico

Guillermo está configurado para Banco Paulista Sintético (CNPJ 12345678000195). La configuración pasó la validación, los términos quedaron aceptados y se generó el primer reporte del periodo 2026-10.

**Carpeta:** solo había una carpeta posible, `seguridad/12345678000195-banco-paulista-sintetico`. Ya tenía la marca `_CRITERIO_SEGURIDAD.txt` y las carpetas 00 a 90, así que no la volví a marcar.

**Archivos que no abrí** (credenciales, llaves y respaldos):
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

**Sugerencia de orden, sin mover nada:** el motor dice que los tres `INC-BPS-10x_revision.md` de `80-revisiones/` irían en `70-incidentes/`.

**Exportaciones del escáner:** las tres (de agosto, septiembre y octubre) traen todas las columnas que el motor necesita, así que no hubo que preguntar por ninguna. El motor no reconoce de qué marca es el escáner; las procesa por los nombres de sus columnas.

**Respuestas, tomadas de los documentos porque nadie podía contestar:**
- **Entidad:** Banco Paulista Sintético, CNPJ 12345678000195, Brasil. Son los mismos datos que ya tenía la configuración de Alexis.
- **Periodo:** 2026-10.
- **Plazos de corrección:** crítica 15, alta 30, media 60 y baja 120 días calendario. Salen de la sección 4 de `politica-gestion-vulnerabilidades.pdf`. Media y baja son más cortos que los valores por omisión, que eran 90 y 180.
- **Cada cuánto se escanea un activo:** 30 días, porque la sección 5 de la política dice «al menos una vez al mes».
- **Catálogo KEV:** está en `50-escaneos/`. El motor lo pasó por la revisión de columnas y pidió una columna de activo. No la registré: es el catálogo de CISA, no una exportación del escáner, y no trae esa columna.
- **Publicar en Rostrum:** no.
- **Dónde se guarda lo que encuentro:** `estado-seguridad/12345678000195-banco-paulista-sintetico`.
- **Términos 1.5:** aceptados por José Francisco Ñáñez el 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-vulnerability-1.4.0-2026-10-15.md` y en `.pdf`.
- **Tarea programada diaria:** no la creé, porque necesita un sí explícito y en esta sesión no había quién lo diera. A mano se corre con `/criterio-vulnerability:vuln-wake`.

**Primer reporte (2026-10):** el motor encontró 9 alertas en total. El reporte de plazos muestra 4 de ellas:
- **3 vulnerabilidades fuera de plazo:**
  - CVE-2099-12003 en bps-db-01, 76 días pasada del plazo.
  - CVE-2099-12001 en bps-web-01, 41 días pasada.
  - CVE-2099-12006 en bps-ad-01, 10 días pasada.
- **1 excepción vencida:** la de CVE-2099-12003 en bps-db-01 venció el 2026-09-30 y la vulnerabilidad sigue abierta. Responsable: el gerente de tecnología.

Las otras 5 corresponden a otros comandos:
- **1 vulnerabilidad del catálogo KEV vencida:** `/criterio-vulnerability:kev-check`.
- **2 cierres que ningún escaneo posterior comprueba** y **2 activos sin escanear:** `/criterio-vulnerability:scan-coverage`.

El reporte completo está en `estado-seguridad/12345678000195-banco-paulista-sintetico/vulnerabilidades/2026-10/reporte-vuln-sla.md`. La corrida quedó registrada como `2026-10-15-vuln-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.