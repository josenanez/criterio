# /criterio-finance:finance-setup finanzas/88733016-9-comercial-control-del-paraguay-sintetica

## Listo — Comercial Control del Paraguay (sintética)

**Lo que miré:** 66 archivos · periodos 2026-01 a 2026-09 y presupuesto-2026 · 0 fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.2.0 (términos 1.3). El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-1.2.0-2026-10-06.md` y `.pdf`. Quedó además un primer comprobante con la fecha real del sistema, 2026-11-02, porque el primer intento no llevó `--today`.

**Respuestas que tomé de los documentos** (nadie contestó):
- **Cuentas de las facturas:** ventas 4135, IVA 2408, compras 5135, 5145 y 5195. Son las que sostienen facturas del periodo según el motor.
- **Conciliación y bancos:** se concilian 1305 y 2205, que tienen auxiliar en 2026-08 y 2026-09. Los bancos son andino-13901 y pacifico-13902.
- **Marco contable:** normas del Consejo de Contadores Públicos del Paraguay, basadas en las NIIF (F-42). No es un banco.
- **Aprobación:** Sofía León aprueba el cierre. No declaré festivos.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`.

# Estado del cierre · periodo 2026-09

**Estado declarado:** en curso (`2026-09/40-soportes/correo-estado-del-cierre.md`, 2026-10-05, Sofía León). **Avance con evidencia:** 53,85 %. **Avance declarado:** 53,85 %. Los dos son ponderados por criticidad.

No hay nada abierto en lo que procesa este comando.

El checklist no está aprobado. Una persona tiene que aprobarlo antes de darlo por bueno.

| Id | Tarea | Responsable | Vence | Estado |
|---|---|---|---|---|
| C-01 a C-05 | Cierre de módulos, bancos, facturas, cartera y provisiones | varios | 2026-10-01 a 2026-10-05 | cumplidas con evidencia |
| C-06 | Papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | en plazo |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 |

**Ruta crítica del cierre:** C-07 → C-08 → C-09.

**Qué falta para que sea mejor:** que una persona apruebe el checklist.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

**Registro:** el reporte completo del motor está en `estado-finanzas/88733016-9-comercial-control-del-paraguay-sintetica/cierre/2026-09/reporte-close-status.md`. Lo de arriba lo resumí a mano. La salida de esta corrida está en `corridas/salida-finance-setup.md` y quedó registrada como `2026-10-06-finance-setup-1`, con 0 hallazgos.