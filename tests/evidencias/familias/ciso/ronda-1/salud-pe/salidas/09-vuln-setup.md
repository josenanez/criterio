# /criterio-vulnerability:vuln-setup seguridad/20512345678-clinica-del-pacifico-sintetica

Guillermo quedó instalado sobre Clínica del Pacífico Sintética (20512345678, Perú) y la corrida de `vuln-setup` quedó registrada. El comando `convertir` dejó una copia en texto de `credenciales-vpn.txt`, un archivo que debía quedar excluido. No la abrí: está en `estado-seguridad/…/00-referencia/credenciales-vpn.txt.md` y conviene borrarla.

- **Preguntas:** las contesté con lo que traen los documentos, como pediste.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-15. El comprobante está en `.criterio/terminos/` en Markdown y PDF.
- **Plazos:** salen de la sección 4 de la política (versión 3): crítica 10, alta 30, media 90 y baja 180 días. Usé 10 para crítica, no los 15 de la plantilla.
- **Columnas del escáner:** el motor no reconoció las cabeceras de las tres exportaciones. Las mapeé yo desde las cabeceras: Equipo afectado es el activo, Identificador la vulnerabilidad y Criticidad del hallazgo la severidad. Con eso se leen las 17 filas de octubre.
- **Escaneo y publicación:** ventana de escaneo de 30 días, según la sección 5 de la política. No se publica en Rostrum.
- **No abierto:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`.
- **Marca de la raíz:** no la dejé (`_CRITERIO_SEGURIDAD.txt`), porque nadie la autorizó y escribe dentro de los documentos.
- **Archivos fuera de lugar:** `80-revisiones/` tiene tres revisiones que irían en `70-incidentes/`. No las moví.

El reporte `vuln-sla` de 2026-10 (fecha de la prueba 2026-10-15) da 9 vulnerabilidades abiertas y estas señales:
- **Pasadas de plazo, 3:** CVE-2099-12001 en cli-web-01 (crítica, 56 días contra 10), CVE-2099-12006 en cli-ad-01 (crítica, 25 días contra 10) y CVE-2099-12003 en cli-db-01 (media, 136 días contra 90).
- **Excepción vencida, 1:** la de CVE-2099-12003, que venció el 2026-09-30.
- **KEV pasado de fecha, 1.**
- **Cierres sin reescaneo, 2.**
- **Activos sin escanear, 2.**

El reporte completo está en `estado-seguridad/20512345678-clinica-del-pacifico-sintetica/vulnerabilidades/2026-10/reporte-vuln-sla.md`. Lo que te mostré en esta sesión quedó en `corridas/salida-vuln-setup.md`.