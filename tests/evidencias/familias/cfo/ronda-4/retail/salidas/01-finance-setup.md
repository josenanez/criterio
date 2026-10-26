# /criterio-finance:finance-setup finanzas/900765432-almacenes-caribe

## Listo — Almacenes Caribe

**Lo que miré:** 65 archivos · periodos 2026-01 a 2026-09 y `presupuesto-2026` · 0 fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.10.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06-2.md` y `.pdf`.

**Resultado:** el cierre de 2026-09 se declaró «cerrado» el 2026-10-05, en un correo de Sofía León. El motor encontró 7 señales abiertas que ese estado no explica:
- Libro mayor contra balance de comprobación: 2.
- Facturas electrónicas duplicadas: 2.
- Partida bancaria sin conciliar: 1.
- Factura electrónica con diferencia de monto: 1.
- Conciliación vencida: 1.

**Checklist:**
- Avance con evidencia: 53,85 %, igual que el declarado.
- C-01 a C-05 están cumplidas y tienen soporte.
- C-06 y C-07 siguen en plazo, sin evidencia.
- C-08 y C-09 están bloqueadas.
- Ruta crítica: C-07 → C-08 → C-09.
- El checklist no está aprobado: una persona tiene que aprobarlo antes de darlo por bueno.

**Dos cosas que no pude resolver sin una persona:**
- **Marco contable:** puse «grupo 1» por defecto. Ningún documento lo dice, así que hay que confirmarlo.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie autorizó escribir en los documentos.

**Qué falta para mejorar el resultado:**
- El auxiliar de la cuenta 2205 (proveedores) de septiembre: lo hubo en agosto y este mes no está.
- Que alguien apruebe el checklist y confirme el marco.
- Soportes de C-03 y C-04 con algo más que la línea de firma.

**Archivos que quedaron:**
- La configuración está en `.criterio/finanzas/900765432-almacenes-caribe/config.json`.
- El reporte del motor está en `estado-finanzas/900765432-almacenes-caribe/cierre/2026-09/reporte-close-status.md`.
- La salida completa de esta corrida está en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-finance-setup.md`.
- La corrida quedó registrada como `2026-10-06-finance-setup-2`.

No medí los minutos hasta el primer resultado, así que no puedo confirmar si se cumplió el cuarto de hora. Clara vuelve a diario durante la ventana del cierre y una vez por semana fuera de ella.