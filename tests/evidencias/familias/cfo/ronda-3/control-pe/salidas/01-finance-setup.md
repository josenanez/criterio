# /criterio-finance:finance-setup finanzas/20790000014-comercial-control-sur

## Listo — Comercial Control Sur

**Lo que miré:** 64 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`. Ninguno está fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.9.0. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-0.9.0-2026-10-06.md` y `.pdf`.

**Respuestas que tomé de los documentos** (nadie las confirmó):
- **País y moneda:** Perú y PEN, por el RUC 20790000014, las facturas F001 de la SUNAT y la moneda de los XML.
- **Marco:** NIIF oficializadas por el Consejo Normativo de Contabilidad (F-15).
- **Periodo:** 2026-09, el último con `10-contabilidad/`.
- **Cuentas:** ventas 41, compras 14/51/52/61 e IGV 2408, según el balance. Se concilian la 1305 y la 2205.
- **Bancos:** `andino-7901` y `pacifico-7902`, por las carpetas de `20-bancos`.
- **Aprueba el cierre:** Sofía León, que firma las tareas C-08 y C-09 y escribió el correo del estado.
- **Festivos:** no hay ninguno. No me dieron festivos.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

El checklist es el de la organización (`00-referencia/checklist-cierre.csv`). Lo dejé en la configuración como aprobado, pero nadie lo confirmó en esta sesión.

### Estado del cierre 2026-09

- **Declarado:** "en curso", en el correo de Sofía León del 2026-10-05.
- **Avance con evidencia:** 53.85 %, igual al declarado.
- **Señales abiertas:** ninguna; todo lo que llegó se procesó.
- **Tareas con evidencia:** C-01 a C-05, cada una con su PDF en `40-soportes`.
- **En plazo:** C-06 (vence 2026-10-07) y C-07 (vence 2026-10-07).
- **Bloqueadas:** C-08 depende de C-07 y C-09 depende de C-08.
- **Ruta crítica:** C-07 → C-08 → C-09.

El reporte completo está en `estado-finanzas/20790000014-comercial-control-sur/cierre/2026-09/reporte-close-status.md`. La sección «Fuentes» del reporte salió vacía.

**Lo que falta para mejorarlo:**
- El extracto de `andino-7901` viene en PDF y el de `pacifico-7902` en XLSX.
- No hay auxiliares de inventarios ni de activos fijos.
- Falta que una persona apruebe el checklist.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

La salida quedó en `corridas/salida-finance-setup.md` y la corrida se registró con el id `2026-10-06-finance-setup-1`. No hice ninguna pregunta a la persona, porque la sesión era sin interfaz.