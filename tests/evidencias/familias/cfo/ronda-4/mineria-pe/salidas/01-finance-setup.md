# /criterio-finance:finance-setup finanzas/20730000015-minera-puna-alta

## Listo — Minera Puna Alta

**Lo que miré:** 63 archivos · periodos 2026-01 a 2026-09 y `presupuesto-2026` · 0 fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó (versión 1.2, familia 0.10.0, 2026-10-06). Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y `.pdf`.

Avance con evidencia del cierre de 2026-09: 53.85 %, igual al declarado. El correo de Sofía León del 2026-10-05 lo declara «en curso».

- **Cumplidas con evidencia:** C-01, C-02, C-03, C-04 y C-05.
- **En plazo:** C-06 y C-07.
- **Bloqueadas:** C-08, por C-07, y C-09, por C-08.
- **Ruta crítica:** C-07 → C-08 → C-09.
- **Checklist:** es el de la organización, pero nadie lo ha aprobado. Eso lo tiene que hacer una persona.

**Señales abiertas.** El reporte de `close-status` dice «Nada abierto en lo que procesa este comando». Pero el cálculo del periodo encontró 5 señales, que muestran otros comandos:
- una factura electrónica sin registrar en la contabilidad;
- un registro contable sin factura electrónica;
- una cuenta bancaria sin conciliar;
- el requerimiento R-09 del auditor sin respuesta, con vencimiento el 2026-10-09 y a cargo de Andrés Paz;
- una partida conciliatoria antigua.

**Respuestas que tomé de los documentos** (nadie contestó):
- RUC 20730000015, país PE, moneda PEN, marco NIIF oficializadas por el CNC (F-15).
- Periodo 2026-09, el último con `10-contabilidad/`.
- Cuentas de facturas, según las facturas que las sostienen: ventas 4135; compras 5135, 5145 y 5195; IVA generado y descontable 2408.
- Cuentas que se concilian: 1305 y 2205, que tienen auxiliar en 2026-09.
- Bancos esperados: andino-7301 y pacifico-7302.
- Aprueba Sofía León, según el checklist.

**Qué falta para que sea mejor:**
- Alguien debe aprobar el checklist.
- No tengo los festivos del calendario; los dejé vacíos.
- No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta, porque nadie lo autorizó.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

El reporte completo quedó en `estado-finanzas/20730000015-minera-puna-alta/cierre/2026-09/reporte-close-status.md`. La configuración quedó en `.criterio/finanzas/20730000015/config.json` y la corrida quedó registrada como `2026-10-06-finance-setup-1`. En `corridas/salida-finance-setup.md` guardé un resumen, no el reporte entero.