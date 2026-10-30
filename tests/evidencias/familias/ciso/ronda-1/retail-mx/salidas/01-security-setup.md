# /criterio-security:security-setup seguridad/tba110315k21-tiendas-del-bajio-sinteticas

Alexis quedó instalado sobre Tiendas del Bajío (sintéticas) y la primera ficha del periodo 2026-10 está calculada. La configuración, el reporte y la corrida registrada están en disco. Lo que sigue es lo que muestra el reporte.

## Instalación
- **Entidad:** Tiendas del Bajío (sintéticas), TBA110315K21, México, MXN. La carpeta venía en el argumento y el motor validó la configuración sin problemas.
- **Documentos:** hay 60, todos nuevos. Las cuatro tablas (declaración de aplicabilidad, sistemas, terceros, riesgos) se reconocieron sin mapeo de columnas.
- **Fuera de lugar:** `80-revisiones/INC-TDA-101`, `102` y `103_revision.md` irían en `70-incidentes/`. No moví nada.
- **Sin abrir:** `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`.
- **Términos 1.3:** los mostré tal cual y los acepté a nombre de José Francisco Ñáñez, 2026-10-15. El comprobante está en `.criterio/terminos/` en Markdown y PDF.
- **Marca de la raíz:** no dejé `_CRITERIO_SEGURIDAD.txt`, porque sin interfaz nadie la autorizó.
- **Ficha:** 12 evidencias de control, 3 revisiones de accesos y 3 evaluaciones de terceros, cada una con su fecha y su fuente. La guía de codificación segura (A.8.28) es un borrador sin aprobar, así que quedó como revisada y no como evidencia.

## Lo que hay que atender (reporte `control-evidence`)
| # | Control | Qué pasa |
|---|---|---|
| 1 | A.8.15 · Registro de eventos | Figura «Implementado» y la ficha no tiene ninguna evidencia de que operó. Responsable: Oficial de cumplimiento. |
| 2 | A.5.18 · Derechos de acceso | La última evidencia es del 2026-06-30, con periodicidad de 92 días, y venció el 2026-09-30 (15 días). Responsable: Jefe de infraestructura. |

Ningún control se declara cumplido aquí.

## Otras señales
Con la ficha, el motor levanta 8 señales en total. Las otras 6 las cubren otros comandos, que no corrí:
- 1 control aplicable sin responsable (A.8.24, que además tiene evidencia).
- 2 revisiones de accesos vencidas.
- 2 evaluaciones de terceros vencidas.
- 1 aceptación de riesgo vencida.

## Archivos
Todos en `estado-seguridad/tba110315k21-tiendas-del-bajio-sinteticas/`:
- `seguridad/2026-10/reporte-control-evidence.md`
- `seguridad/2026-10/ficha.json`
- `corridas/salida-security-setup.md`

La corrida quedó registrada con 8 hallazgos.