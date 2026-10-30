# /criterio-resilience:resilience-setup seguridad/20512345678-clinica-del-pacifico-sintetica

Amparo quedó instalada sobre la Clínica del Pacífico (sintética), y la primera ficha del periodo 2026-10 y la corrida quedaron guardadas. Hay un problema del motor que conviene corregir: `convertir` copió al caché el archivo de credenciales, sin abrirlo yo. Lo borré.

**Lo que no abrí:** `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`. Conviene sacarlos de la carpeta de evidencia.

**El problema con `convertir`:** ignora la lista de excluidos y deja en `estado-seguridad/.../cache/` una copia de los archivos de texto que debería saltarse. Eso pasó con `credenciales-vpn.txt`. No abrí esa copia y la borré. Mientras el motor no se corrija, otra corrida de `convertir` la volvería a crear.

**Qué quedó instalado:**
- **Plazos de la política (v2, secciones 5 y 7):** contención de 4 h (crítica), 12 h (alta), 48 h (media) y 120 h (baja), y revisión posterior en 20 días.
- **Matriz de notificaciones y calendario de continuidad:** el motor reconoció sus columnas sin necesidad de mapearlas.
- **Preguntas:** nadie las respondió, así que tomé la respuesta sugerida a partir de los documentos y quedó anotada en la ficha.
- **Términos 1.3:** José Francisco Ñáñez los aceptó el 2026-10-15, y el comprobante está en `.criterio/terminos/` en Markdown y PDF. El texto corto está en `corridas/salida-resilience-setup.md`.
- **Configuración:** `.criterio/resiliencia/20512345678/config.json`, validada sin problemas.
- **Marca `_CRITERIO_SEGURIDAD.txt`:** no la creé, porque nadie la autorizó.

**Primera ficha:** 6 incidentes, 3 revisiones y 4 pruebas, con 8 señales que el motor calculó con fecha de corte 2026-10-15:

| Señal | Casos | Qué muestra el reporte |
|---|---|---|
| Contención fuera de plazo o pendiente | 2 | INC-CLI-102 se contuvo en 18 h y la política da 12. INC-CLI-106 (alta, detectado el 2026-09-28) sigue sin contención registrada. |
| Cerrado sin revisión posterior en plazo | 1 | INC-CLI-105, cerrado el 2026-08-25, lleva 31 días sin revisión y la política da 20. |
| Notificación tarde o sin hacer | 2 | Solo el conteo. Los detalles salen con `notifications`, que no corrí. |
| Prueba de continuidad vencida | 1 | Solo el conteo. Los detalles salen con `continuity-tests`, que no corrí. |
| Prueba de restauración vencida | 2 | Solo el conteo. Los detalles salen con `continuity-tests`, que no corrí. |

El calendario incluye la restauración de la base de clientes, y en `90-continuidad/` no hay informe de esa prueba. En INC-CLI-104 y 106 dejé el cierre vacío porque el informe dice "abierto".

Las tres revisiones de `80-revisiones/` las procesé donde están, aunque el inventario sugiere moverlas a `70-incidentes/`. No moví ni renombré nada.

El reporte completo está en `estado-seguridad/20512345678-clinica-del-pacifico-sintetica/resiliencia/2026-10/reporte-incident-timeline.md`, con la ficha en `ficha.json` de la misma carpeta. Lo que te mostré quedó en `estado-seguridad/20512345678-clinica-del-pacifico-sintetica/corridas/salida-resilience-setup.md`.