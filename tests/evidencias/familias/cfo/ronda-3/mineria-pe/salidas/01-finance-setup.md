# /criterio-finance:finance-setup finanzas/20730000015-minera-puna-alta

Ya terminé la instalación de Clara para Minera Puna Alta y el primer estado del cierre de 2026-09. Esta prueba no tuvo interfaz, así que tomé las respuestas sugeridas a partir de los documentos. Las dejé escritas en la ficha, en «Las preguntas que hizo».

**Lo que miré:** 63 archivos, periodos 2026-01 a 2026-09 y presupuesto-2026. No hay ninguno fuera de la estructura recomendada.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.9.0 (términos 1.2), con fecha 2026-10-06. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-0.9.0-2026-10-06.md` y `.pdf`.

**Estado del cierre:**
- **Declarado:** el correo de Sofía León del 2026-10-05 dice «en curso».
- **Avance:** 53.85 % con evidencia y 53.85 % declarado.
- **Con evidencia:** C-01 a C-05 están cumplidas con soporte.
- **Sin evidencia:**
  - C-06 (Elena Cruz) y C-07 (Lucía Mora) vencen el 2026-10-07 y siguen en plazo.
  - C-08 y C-09 (Sofía León) están bloqueadas por C-07 y C-08.
- **Ruta crítica:** C-07 → C-08 → C-09.
- **Checklist:** el checklist no está aprobado hasta que una persona lo apruebe.

**Señales abiertas:** el cálculo levantó 5 señales, una de cada tipo:
- una factura electrónica sin registro contable;
- un registro contable sin factura electrónica;
- un banco sin conciliar;
- un requerimiento de auditoría sin responder (R-09, que vence el 2026-10-09);
- una partida conciliatoria antigua.

El reporte de close-status dice «Nada abierto» porque esas señales las revisan otros comandos: einvoice-check, bank-reconcile, account-reconcile y audit-pack.

**Supuestos que conviene confirmar:**
- **Marco y moneda:** NIIF oficializadas por el Consejo Normativo de Contabilidad (F-15) y PEN, ambos tomados por defecto del país.
- **Cuentas:** ventas 41, compras 14/51/52/61 e IVA 2408 son las de defecto. El balance trae 4135, 1435, 51xx y 2408.
- **Festivos:** no se dieron, así que el calendario no tiene ninguno.
- **Auxiliares:** solo hay auxiliar de 1305 y 2205. Faltan los de las demás cuentas, por ejemplo 1435 Inventarios.

No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque la prueba no dio esa autorización.

Todo quedó en `estado-finanzas/20730000015-minera-puna-alta/`:
- `cierre/2026-09/reporte-close-status.md`
- `corridas/salida-finance-setup.md`

La corrida quedó registrada como `2026-10-06-finance-setup-1`, y la configuración está en `.criterio/finanzas/20730000015/config.json`.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.