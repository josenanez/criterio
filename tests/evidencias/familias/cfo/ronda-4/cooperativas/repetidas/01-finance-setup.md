# /criterio-finance:finance-setup finanzas/1790012345001-cooperativa-sierra-alta

## Listo: Cooperativa Sierra Alta

**Lo que miré:** 59 archivos, periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno quedó fuera de la estructura.
**Términos:** quedaron aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06, para la versión 0.10.0. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y `.pdf`.

Nadie respondió preguntas en esta sesión, así que tomé las respuestas de los documentos. La configuración quedó en `.criterio/finanzas/1790012345001-cooperativa-sierra-alta/config.json`.

Quedan tres cosas por confirmar:
- **Marco contable:** ningún documento lo dice. Quedó como "por confirmar".
- **Checklist:** usé `00-referencia/checklist-cierre.csv` y quedó sin aprobar.
- **Festivos:** no hay ninguno declarado.

No marqué la carpeta con `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

### Estado del cierre de 2026-09
- **Declarado:** "en curso", según el correo de Sofía León del 2026-10-05.
- **Avance:** 46.15 % con evidencia y 46.15 % declarado. Coinciden.
- **Tareas con soporte:** C-01, C-02, C-03 y C-04.
- **Tarea vencida:** C-05, Registrar provisiones y causaciones (Jorge Vela). Venció el 2026-10-05 y no tiene evidencia.
- **Tareas bloqueadas:** C-07, C-08 y C-09. C-06 está en plazo.
- **Ruta crítica:** C-05 → C-07 → C-08 → C-09.

`compute` encontró 8 señales en total. El reporte de close-status muestra solo la tarea vencida. Las otras 7 son:
- 1 factura sin registro contable.
- 2 registros contables sin factura.
- 1 cuenta sin conciliar.
- 2 requerimientos del auditor sin respuesta.
- 1 conciliación vencida.

Para mejorar el siguiente cierre faltan el extracto de pacifico-2302 (solo hay auxiliar de libros), los responsables y la aprobación del checklist, y el marco contable.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

Los archivos quedaron en `estado-finanzas/1790012345001-cooperativa-sierra-alta/`:
- `cierre/2026-09/reporte-close-status.md`
- `corridas/salida-finance-setup.md`

La corrida quedó registrada como `2026-10-06-finance-setup-1`.