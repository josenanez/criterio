# /criterio-security:security-setup seguridad/20512345678-clinica-del-pacifico-sintetica

Alexis quedó instalado sobre la Clínica del Pacífico (sintética) y la primera ficha del periodo 2026-10 está calculada.

## Lo que hay que atender
Estos dos controles salieron del reporte `control-evidence`:
1. **A.8.15, Registro de eventos.** Figura «Implementado» y no tiene ninguna evidencia de que operó. Responsable: Oficial de cumplimiento. Cita: `declaracion-aplicabilidad.xlsx`, fila 12.
2. **A.5.18, Derechos de acceso.** Su última evidencia es del 2026-06-30 y su periodicidad es de 92 días. Venció el 2026-09-30, hace 15 días. Responsable: Jefe de infraestructura.

## Lo que hice
- **Carpeta:** usé la del argumento. El inventario dio 60 archivos. Las tres revisiones de `80-revisiones/` están fuera de lugar (irían en `70-incidentes/`) y no moví nada.
- **Excluidos sin abrir:** `credenciales-vpn.txt` (credencial), `servidor-web.pem` (llave) y `respaldo-correo-2026-06-20.zip` (respaldo).
- **Marca de la carpeta:** no dejé `_CRITERIO_SEGURIDAD.txt`. Es la única pregunta que hice, y la respondí yo con la respuesta sugerida: la ruta vino en el argumento y marcarla crearía un archivo que nadie pidió.
- **Términos:** la versión 1.3 quedó aceptada por José Francisco Ñáñez el 2026-10-15. El comprobante en Markdown y PDF está en `.criterio/terminos/`.
- **Configuración:** `.criterio/seguridad/20512345678/config.json`. `columns` quedó vacío porque el motor reconoció las cabeceras de la declaración, los sistemas, los terceros y los riesgos tal como vienen.
- **Ficha del periodo 2026-10:** tiene 12 evidencias, 3 revisiones de accesos y 3 evaluaciones de terceros.
- **Borrador descartado:** `A.8.28_borrador-guia-codificacion.docx` es un borrador sin aprobar. Lo dejé en `reviewed`, no como evidencia.
- **Señales:** el cálculo dio 8 en total. Las de accesos, terceros y riesgos salen en sus reportes, que no corrí en esta instalación.

## Para revisar
- **A.8.24:** la declaración no trae responsable en esa fila. El motor ya contó una señal `soa_control_unassigned`, y creo que es esta.
- **Cómo leí el xlsx:** `openpyxl` falló con ese archivo, así que lo leí directo del XML de la hoja. Si hay otra hoja o columna que el motor lea distinto, conviene confirmarlo.
- **Convertir:** no pasé por `convertir` la carpeta `20-accesos` ni la `30-terceros` en la primera tanda, solo `10-controles`. Corrí las tres para tener el texto en caché.

## Archivos
Todos están bajo `estado-seguridad/20512345678-clinica-del-pacifico-sintetica/`:
- `seguridad/2026-10/reporte-control-evidence.md`
- `seguridad/2026-10/ficha.json`
- `corridas/salida-security-setup.md` (corrida registrada como `2026-10-15-security-setup-1`)