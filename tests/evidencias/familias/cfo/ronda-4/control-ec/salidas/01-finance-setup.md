# /criterio-finance:finance-setup finanzas/1790000001001-comercial-control

## Listo — Comercial Control

**Lo que miré:** 64 archivos, periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno está fuera de la estructura.

**Términos:** aceptados por José Francisco Ñáñez para la versión 0.10.0 (términos 1.2). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y `.pdf`.

**Cómo quedó la configuración:**
- La entidad es Comercial Control, RUC 1790000001001, Ecuador, USD. El marco registrado es «NIIF Ecuador». Escribí el nombre desde el de la carpeta y la moneda desde el país; los documentos no los traen.
- Ventas va en 4135. Compras va en 5135, 5145 y 5195. El IVA generado y el descontable van en 2408. Todas salen de las facturas del periodo.
- Se concilian 1305 y 2205, que tienen auxiliar en 2026-09. Los bancos esperados son andino-6701 y pacifico-6702.
- Sofía León aprueba el cierre. No hay festivos cargados.
- La configuración quedó en `.criterio/finanzas/1790000001001/config.json`. El motor la validó sin problemas.

## Estado del cierre 2026-09 (copiado del reporte del motor)

- **Declarado:** «en curso», según el correo de Sofía León del 2026-10-05.
- **Avance con evidencia:** 53.85 %. El avance declarado es el mismo, 53.85 %.
- **Señales abiertas:** ninguna en lo que procesa este comando.
- **Ruta crítica:** C-07 → C-08 → C-09.
- **Cumplidas con soporte:** C-01 a C-05, cada una con su archivo en `2026-09/40-soportes/`.
- **Pendientes:**
  - C-06 (impuestos, Elena Cruz) y C-07 (balance de comprobación, Lucía Mora) están en plazo, con vencimiento el 2026-10-07.
  - C-08 y C-09 (Sofía León) están bloqueadas por la tarea anterior de la cadena.
- **Checklist:** no está aprobado. El estado se calcula igual, pero una persona tiene que aprobarlo antes de darlo por bueno.

El reporte completo quedó en `estado-finanzas/1790000001001-comercial-control/cierre/2026-09/reporte-close-status.md`. Lo que te mostré arriba también está en `corridas/salida-finance-setup.md`, y la corrida quedó registrada.

**Qué falta para mejorarlo:** aprobar el checklist y pasar los festivos de Ecuador. No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie lo autorizó, y no escribí nada dentro de los documentos. No medí los minutos hasta el primer resultado.

**Preguntas:** no hubo interfaz, así que tomé la respuesta sugerida a partir de los documentos en las 11 preguntas. Quedaron registradas en la ficha del cierre y en el reporte.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.