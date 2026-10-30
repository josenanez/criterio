# /criterio-finance:finance-setup finanzas/28903114000160-mineracao-serra-azul

## Listo — Mineração Serra Azul

**Lo que miré:** 66 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`. Ninguno quedó fuera de la estructura.

**Términos:** aceptados por José Francisco Ñáñez (2026-10-06) para la versión 0.12.1, con términos 1.3. El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-0.12.1-2026-10-06.md` y `.pdf`.

**Lo que tomé como respuesta, sin preguntar a nadie:**
- Entidad: Mineração Serra Azul, CNPJ 28903114000160, país BR, moneda BRL, marco CPC / IFRS.
- Cuentas de facturas: ventas 4135; compras 5135, 5145 y 5195; IVA 2408 (generado y descontable). Son las que sostienen facturas del periodo.
- Cuentas que se concilian: 1305 y 2205. Bancos: bandeirante-3101 y litoral-3102.
- Checklist: el de la organización, `00-referencia/checklist-fechamento.csv`. Lo tomé como aprobado, y eso no lo confirmó ninguna persona.
- Aprueba el cierre Sofia Leão. Festivo: 2026-10-12.
- No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos.

**Estado del cierre de 2026-09 (reporte del motor):** la responsable del cierre declaró «en curso» en el correo del 2026-10-05. El avance con evidencia es 53,85 % y coincide con el declarado. Hay cinco tareas cumplidas con soporte (C-01 a C-05). C-06 y C-07 están en plazo. C-08 y C-09 están bloqueadas. La ruta crítica es C-07 → C-08 → C-09.

**Señales que el reporte no muestra:** el reporte dice «nada abierto», pero `compute` levantó 4 señales. Son una factura electrónica duplicada, un registro contable sin factura electrónica, una partida bancaria sin conciliar y el requerimiento R-09 del auditor sin responder (vence el 2026-10-09). Las tratan `einvoice-check`, `bank-reconcile` y `audit-pack`, y no las revisé.

**Para mejorar:** faltan extractos y auxiliares de los meses anteriores a 2026-08 (solo hay mayor), y que una persona apruebe el checklist.

**Archivos:**
- La configuración está en `.criterio/finanzas/28903114000160/config.json`.
- El reporte completo está en `estado-finanzas/28903114000160-mineracao-serra-azul/cierre/2026-09/reporte-close-status.md`.
- La salida de esta corrida quedó registrada con el id `2026-10-06-finance-setup-1`.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.