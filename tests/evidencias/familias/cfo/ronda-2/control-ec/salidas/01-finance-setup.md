# /criterio-finance:finance-setup finanzas/1790000001001-comercial-control

## Listo: Comercial Control

**Lo que miré:** 58 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`. Ninguno quedó fuera de la estructura.

**Términos:** aceptados a nombre de José Francisco Ñáñez para la versión 0.8.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.8.0-2026-10-06.md` y `.pdf`.

**Cómo quedó la configuración:** como nadie respondió, usé la respuesta sugerida a partir de los documentos. La configuración está en `.criterio/finanzas/1790000001001/config.json` y el estado en `estado-finanzas/1790000001001-comercial-control`.
- La entidad es Ecuador, USD, RUC 1790000001001.
- El periodo en cierre es 2026-09, y aprueba Sofía León.
- Las cuentas de ventas, compras e IVA salen del balance de comprobación.
- Las cuentas que se concilian son 1305 y 2205, y los bancos esperados son `andino-6701` y `pacifico-6702`.
- Usé el checklist de la organización (`00-referencia/checklist-cierre.csv`), sin aprobar.
- No encontré en los documentos el marco contable de Ecuador ni los festivos. El marco quedó como «NIIF (marco por confirmar)» y los festivos vacíos.
- No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie autorizó escribir en ella.

### Estado del cierre 2026-09

- **Declarado:** en curso (correo de Sofía León, 2026-10-05).
- **Avance:** 53.85 % tanto con evidencia como declarado, ponderado por criticidad.
- **Señales abiertas:** ninguna. Todo lo que llegó se procesó.
- **Checklist sin aprobar:** el estado se calculó igual, pero una persona tiene que aprobar el checklist antes de darlo por bueno.

| Tarea | Responsable | Vence | Estado |
|---|---|---|---|
| C-01 Cerrar ventas, compras e inventarios | Lucía Mora | 2026-10-01 | cumplida con evidencia |
| C-02 Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida con evidencia |
| C-03 Cruzar facturas emitidas con ventas | Lucía Mora | 2026-10-02 | cumplida con evidencia |
| C-04 Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | cumplida con evidencia |
| C-05 Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | cumplida con evidencia |
| C-06 Papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo |
| C-07 Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | en plazo |
| C-08 Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 |
| C-09 Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 |

**Ruta crítica:** C-07 → C-08 → C-09.

### Qué falta

- El marco contable de Ecuador y los festivos.
- Que una persona apruebe el checklist.
- Correr `bank-reconcile`, `ledger-check` y `einvoice-check`. Este primer estado solo se apoya en el checklist y en los soportes firmados, y por eso no hay señales abiertas.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

La salida quedó en `estado-finanzas/1790000001001-comercial-control/corridas/salida-finance-setup.md`. La corrida está registrada como `2026-10-06-finance-setup-1`.

No medí los minutos hasta el primer resultado; la nota de la corrida lo dice.