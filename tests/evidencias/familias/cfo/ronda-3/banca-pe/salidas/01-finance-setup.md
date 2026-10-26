# /criterio-finance:finance-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera

**Lo que miré:** 64 archivos, periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno quedó fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.9.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.9.0-2026-10-06.md` y `.pdf`.

El correo de Sofía León del 2026-10-05 dice que el cierre de septiembre está cerrado. El motor encuentra 5 señales abiertas que lo contradicen. El checklist es el de la organización y queda sin aprobar hasta que una persona lo apruebe.

No dejé la marca `_CRITERIO_FINANZAS.txt` en la carpeta de documentos porque nadie la autorizó. No escribí nada en los documentos.

### Estado del cierre 2026-09

- **Declarado:** cerrado, según el correo de Sofía León del 2026-10-05.
- **Avance con evidencia:** 42.31 %. El avance declarado es 53.85 %, ponderados por criticidad.
- **Ruta crítica:** C-02 → C-07 → C-08 → C-09.

Lo que hay que atender:

1. **C-02 (conciliar cada cuenta bancaria, Andrés Paz):** figura cumplida y no hay soporte `C-02` en `2026-09/40-soportes/`. Esto bloquea C-07, C-08 y C-09.
2. **Cierre declarado contra evidencia:** el correo dice cerrado y hay 4 señales abiertas que ese estado no explica.

Las otras señales abiertas que cuenta el motor son una factura duplicada, un banco sin conciliar y una diferencia de monto en una factura. El reporte solo detalla dos señales en "Lo que hay que atender".

Tareas con evidencia: C-01, C-03, C-04 y C-05. C-06 está en plazo.

### Qué falta

- El soporte firmado de C-02 en `2026-09/40-soportes/`.
- La aprobación del checklist por una persona.
- Los festivos del calendario. No los di, así que quedó vacío.

Contesté todas las preguntas con la respuesta sugerida desde los documentos, y quedan en la ficha. No medí los minutos hasta el primer resultado.

**Dónde quedó todo:**
- Configuración: `.criterio/finanzas/20710000019/config.json`
- Reporte del motor: `estado-finanzas/20710000019-banco-ribera/cierre/2026-09/reporte-close-status.md`
- Salida de esta corrida: `estado-finanzas/20710000019-banco-ribera/corridas/salida-finance-setup.md`, registrada como `2026-10-06-finance-setup-1`

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.