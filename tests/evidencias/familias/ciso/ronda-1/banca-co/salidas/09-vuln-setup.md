# /criterio-vulnerability:vuln-setup seguridad/901555123-banco-cordillera-sintetico

Guillermo quedó instalado sobre Banco Cordillera Sintético (901555123), y el motor dio por válida la configuración. El reporte `vuln-sla` del periodo 2026-10 está generado y la corrida quedó registrada con 9 hallazgos.

**Qué dejé hecho**
- **Configuración:** `.criterio/vulnerabilidades/901555123/config.json`, con país CO, moneda COP y estado en `estado-seguridad/901555123-banco-cordillera-sintetico`. No se publica en Rostrum.
- **Plazos:** los tomé de la sección 4 de la política (versión 3): crítica 15 días, alta 30, media 60 y baja 120. Esos valores difieren del ejemplo, que traía media 90 y baja 180. El escaneo mensual sale de la sección 5.
- **Exportaciones del escáner:** las tres reconocen las mismas columnas y no les falta ninguna. No hubo preguntas a la persona; todo salió de los documentos.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez con fecha 2026-10-15. El comprobante está en `.criterio/terminos/` en Markdown y PDF.
- **Marca de raíz:** no dejé `_CRITERIO_SEGURIDAD.txt` en la carpeta, porque nadie lo autorizó.

**Excluidos y no abiertos**
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

**Lo que hay que atender**
- **Críticas vencidas:** CVE-2099-12001 en bco-web-01, abierta 56 días con plazo de 15, y CVE-2099-12006 en bco-ad-01, abierta 25 días con plazo de 15.
- **Media vencida:** CVE-2099-12003 en bco-db-01, abierta 136 días con plazo de 60. Su excepción venció el 2026-09-30.
- **Otras señales:** 1 vulnerabilidad del catálogo KEV pasada de fecha, 2 cierres sin reescaneo y 2 activos sin escanear. Esas cuatro señales no las detallé; salen del conteo del motor.

**Un problema con el motor:** `convertir --caso 00-referencia` generó una copia de texto de `credenciales-vpn.txt` (`credenciales-vpn.txt.md`, 41 caracteres) aunque el archivo está en la lista de excluidos. No la abrí ni la borré. Conviene borrarla y revisar por qué `convertir` no respeta esa lista.

**Fuera de lugar:** `80-revisiones/` tiene tres revisiones (INC-BCO-101 a 103) que el motor sugiere llevar a `70-incidentes/`. No moví nada.

La salida completa quedó en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-vuln-setup.md`, y el reporte está en `estado-seguridad/901555123-banco-cordillera-sintetico/vulnerabilidades/2026-10/reporte-vuln-sla.md`.