# /criterio-security:security-setup seguridad/20599887766-distribuidora-control-sintetica

Soy Alexis. Pongo cada control de la declaración de aplicabilidad al lado de la evidencia de que operó; no acepto riesgos ni declaro cumplido un control.

La instalación quedó lista para `seguridad/20599887766-distribuidora-control-sintetica`, y la corrida quedó registrada como `2026-10-15-security-setup-1`.

- **Archivos que no abrí:** son tres, y el motor los excluyó por ser credenciales, llaves o respaldos.
  - `00-referencia/credenciales-vpn.txt`
  - `10-controles/A.8.24_certificados/servidor-web.pem`
  - `90-continuidad/respaldo-correo-2026-06-20.zip`
- **Fuera de lugar:** `80-revisiones/INC-DCS-101_revision.md` iría en `70-incidentes/`. No lo moví.
- **Configuración y términos:** la configuración ya existía y `config` la validó sin problemas, así que no la reescribí. Los términos (versión 1.3) ya estaban aceptados y vigentes por José Francisco Ñáñez el 2026-10-15, así que no pedí otro sí.
- **La ficha de 2026-10:** conservé la que ya había, porque coincide con los documentos convertidos. Tiene 13 evidencias, 4 revisiones de accesos y 3 evaluaciones de terceros. El borrador `A.8.28_borrador-guia-codificacion.docx` quedó como revisado, no como evidencia, porque no está aprobado.
- **Un cambio a la ficha:** la pregunta sobre la marca `_CRITERIO_SEGURIDAD.txt` tenía la respuesta vacía y el motor la rechazaba. Ahora dice "No (nadie autorizó crear el archivo; no se dejó)", y no creé el archivo. Después de eso `compute` no devolvió problemas.
- **Registro de riesgos:** `40-riesgos/registro-riesgos.xlsx` no se deja abrir con mis herramientas, así que no pude reconocer sus columnas ni declarar `columns.risks`. Queda pendiente.

## Lo que muestra el reporte

El reporte está en `estado-seguridad/20599887766-distribuidora-control-sintetica/seguridad/2026-10/reporte-control-evidence.md`.

- **Pendiente de atender:** ningún control vence antes de la fecha de corte, así que no hay nada abierto.
- **Sin evidencia:** el control 8.28 (Codificación segura) está "En implementación" y no tiene ninguna evidencia de que operó. Este es el único.
- **Vencen pronto:** estos controles vencen en las próximas semanas, según el motor.
  - 8.16 el 2026-10-16.
  - 8.7, 8.8, 8.13 y 8.15 el 2026-10-31.
  - 5.18 el 2026-11-15.
- **Los demás:** vencen entre 2026-12-31 y 2027-05-21.

La tabla completa de los 14 controles está en `corridas/salida-security-setup.md`, dentro de la misma carpeta de estado.