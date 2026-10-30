# /criterio-finance:finance-setup finanzas/3101612904-almacenes-de-la-meseta

## Listo — Almacenes de la Meseta

**Lo que miré:** 65 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`, ninguno fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3). Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.

El correo de Sofía León del 2026-10-05 dice que septiembre está cerrado. Los documentos no lo sostienen. Hay 5 señales abiertas que ese estado no explica. Un banco no está conciliado, hay una factura duplicada, un registro contable sin factura electrónica, un requerimiento del auditor sin responder y una partida conciliatoria antigua. El reporte solo detalla la señal del cierre declarado contra la evidencia. Esas cinco quedan en `resultados.json`, no en el reporte.

El avance con evidencia es 53,85 %, igual al declarado. C-01 a C-05 tienen soporte. C-06 y C-07 están en plazo y sin evidencia. C-08 y C-09 están bloqueadas, y la ruta crítica es C-07 → C-08 → C-09.

El checklist (`00-referencia/checklist-cierre.xlsx`) no tiene aprobación registrada, así que una persona tiene que aprobarlo antes de darlo por bueno. El reporte completo está en `estado-finanzas/3101612904-almacenes-de-la-meseta/cierre/2026-09/reporte-close-status.md`.

**Respuestas que tomé por defecto, sin nadie que contestara:**
- **Periodo:** 2026-09, el último con contabilidad y balance de comprobación.
- **Cuentas de facturas:** ventas 4135, IVA 2408, compras 5135, 5145 y 5195. Son las que el motor encontró en las facturas del periodo.
- **Cuentas a conciliar:** 1305 y 2205, que tienen auxiliar en agosto y septiembre.
- **Bancos esperados:** andino-10301 y pacifico-10302.
- **Marco contable:** NIIF, país CR y moneda CRC. Lo inferí de las facturas costarricenses; ningún documento lo declara.
- **Aprobador y festivos:** aprobador «Contralor» por defecto y sin festivos, porque ningún documento los dice.
- **Marca de carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, para no escribir dentro de los documentos.

El motor no dio ninguna cifra de más. El avance de 53,85 % es la que trae el reporte.

**Para mejorar el resultado:** falta la aprobación del checklist y el nombre real de quien aprueba el cierre. La evidencia de C-06 y C-07 también está pendiente. Hay que revisar el requerimiento R-03, que llegó en Word, por si trae solicitudes fuera de la tabla del auditor. No lo procesé.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

La salida completa quedó en `estado-finanzas/3101612904-almacenes-de-la-meseta/corridas/salida-finance-setup.md`. La corrida quedó registrada como `2026-10-06-finance-setup-1`, con 6 hallazgos.