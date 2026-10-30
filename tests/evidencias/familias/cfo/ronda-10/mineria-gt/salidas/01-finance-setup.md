# /criterio-finance:finance-setup finanzas/89090314-minera-del-motagua

## Listo — Minera del Motagua

**Lo que miré:** 66 archivos · periodos 2026-01 a 2026-09 y presupuesto-2026 · 0 fuera de la estructura.
**Términos:** aceptados para la versión 1.0.0 (términos 1.3) a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.

**Respuestas que tomé en lugar de preguntar:**
- **País y moneda:** Guatemala y GTQ, porque las facturas son FEL de la SAT en quetzales.
- **Cuentas que cruzan las facturas:** son las que sostienen facturas en los datos. Ventas 4135, compras 5135, 5145 y 5195, e IVA 2408.
- **Cuentas y bancos:** se concilian 1305 y 2205, y se esperan andino-8901 y pacifico-8902.
- **Aprueba el cierre:** Sofía León.
- **Marco contable:** ningún documento lo declara, así que quedó «por confirmar».
- **Marcador de carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

# Estado del cierre · Minera del Motagua · periodo 2026-09

**Estado declarado:** en curso (`2026-09/40-soportes/correo-estado-del-cierre.md`, 2026-10-05). **Avance con evidencia:** 53.85 %. **Avance declarado:** 53.85 %, ponderado por criticidad.

El checklist no está aprobado. El estado se calcula, pero una persona tiene que aprobarlo antes de darlo por bueno.

| Id | Tarea | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 | — |
| C-06 | Papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | en plazo | — |
| C-01 | Cerrar módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | cumplida con evidencia | `2026-09/40-soportes/C-01-soporte.md` |
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida con evidencia | `2026-09/40-soportes/C-02-soporte.md` |
| C-03 | Cruzar facturas emitidas con ventas | Lucía Mora | 2026-10-02 | cumplida con evidencia | `2026-09/40-soportes/C-03-soporte.pdf` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | cumplida con evidencia | `2026-09/40-soportes/C-04-soporte.pdf` |
| C-05 | Provisiones y causaciones | Jorge Vela | 2026-10-05 | cumplida con evidencia | `2026-09/40-soportes/C-05-soporte.pdf` |

**Ruta crítica del cierre:** C-07 → C-08 → C-09.

**Señales abiertas que calculó el motor (4):**
- Una factura emitida duplicada.
- Un registro contable sin factura electrónica.
- Un banco sin conciliar.
- Un requerimiento del auditor sin respuesta: R-09, con fecha límite 2026-10-09 y a cargo de Andrés Paz.

El reporte de close-status dice «nada abierto» porque solo mira el checklist. Cada señal se detalla en su comando: `/einvoice-check`, `/bank-reconcile` y `/audit-pack`.

**Qué falta para que esto sea mejor:**
- El marco contable.
- La aprobación del checklist.
- Los festivos.
- El extracto del banco andino-8901 en un formato que el motor lea. Hoy solo hay PDF.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

**Archivos:**
- Configuración: `.criterio/finanzas/89090314/config.json`
- Ficha del cierre: `estado-finanzas/89090314-minera-del-motagua/cierre/2026-09/ficha.json`
- Reporte: `estado-finanzas/89090314-minera-del-motagua/cierre/2026-09/reporte-close-status.md`
- Salida de esta corrida, registrada como `2026-10-06-finance-setup-1`: `estado-finanzas/89090314-minera-del-motagua/corridas/salida-finance-setup.md`

No medí los minutos hasta el primer resultado.