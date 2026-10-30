# /criterio-finance:finance-setup finanzas/155791002-2-2017-almacenes-del-canal

Terminé la instalación de Clara para Almacenes del Canal y registré la corrida. El cierre de 2026-09 está declarado como cerrado, pero el motor encontró 5 señales abiertas.

## Listo — Almacenes del Canal

**Lo que miré:** 65 archivos, periodos 2026-01 a 2026-09 y presupuesto-2026. Ninguno está fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.

**Respuestas que tomé yo, sin que nadie las confirmara:**
- **Entidad:** Almacenes del Canal, RUC 155791002-2-2017, Panamá, USD. Lo saqué de las facturas (DGI) y de los extractos.
- **Marco contable:** NIIF. Ningún documento lo confirma, así que solo quedó registrado.
- **Cuentas que cruzan las facturas:**
  - Ventas: 4135.
  - Compras: 5135, 5145 y 5195.
  - IVA generado y descontable: 2408.
- **Cuentas que se concilian contra auxiliar:** 1305 y 2205. Ambas tienen auxiliar en 2026-08 y 2026-09.
- **Bancos esperados:** andino-7901 y pacifico-7902.
- **Checklist:** el de la organización, `00-referencia/checklist-cierre.xlsx`, sin aprobar.
- **Quién aprueba el cierre:** no lo encontré en los documentos y dejé "Contralor" por defecto.
- **Festivos:** ninguno.
- **Archivo `_CRITERIO_FINANZAS.txt`:** no lo dejé en la carpeta, porque nadie lo autorizó.

**Estado del cierre:**
- **Declarado:** el correo de Sofía León del 2026-10-05 dice que el cierre de septiembre está cerrado.
- **Avance:** 53.85 % con evidencia, igual al declarado.
- **Tareas:**
  - C-01 a C-05 están cumplidas con soporte.
  - C-06 y C-07 siguen en plazo.
  - C-08 y C-09 están bloqueadas.
  - La ruta crítica es C-07 → C-08 → C-09.
- **Señales abiertas:** la declaración de cierre sin evidencia, una factura electrónica duplicada, un banco sin conciliar, un registro sin factura electrónica y un requerimiento de auditoría sin responder. El reporte solo muestra la primera en su tabla; no pude ver el detalle de las otras cuatro.

**Dónde quedó cada cosa:**
- **Configuración:** `.criterio/finanzas/155791002-2-2017/config.json`. Es válida y no tuvo problemas.
- **Ficha del cierre:** `estado-finanzas/155791002-2-2017-almacenes-del-canal/cierre/2026-09/ficha.json`.
- **Reporte:** `estado-finanzas/155791002-2-2017-almacenes-del-canal/cierre/2026-09/reporte-close-status.md`.
- **Salida de la corrida:** `estado-finanzas/155791002-2-2017-almacenes-del-canal/corridas/salida-finance-setup.md`.
- **Corrida registrada:** `2026-10-06-finance-setup-1`.

**Qué falta para mejorar el resultado:**
- Un aprobador del cierre y un marco contable confirmados por escrito.
- Aprobación del checklist por una persona.
- El auxiliar de otras cuentas, si también se concilian.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.