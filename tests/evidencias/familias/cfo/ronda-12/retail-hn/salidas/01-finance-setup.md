# /criterio-finance:finance-setup finanzas/08010006129040-almacenes-del-valle-de-sula

## Listo — Almacenes del Valle de Sula

**Lo que miré:** 64 archivos · periodos 2026-01 a 2026-09 y presupuesto-2026 · 0 fuera de la estructura.
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-06 para la versión 1.1.0 (términos 1.3). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-1.1.0-2026-10-06.md` y `.pdf`.

Septiembre se declaró cerrado (correo de Sofía León, 2026-10-05). Pero el motor encontró 7 señales abiertas y el avance con evidencia es 53.85 %. Las 16 facturas de Honduras son PDF y no XML, así que las pasé a la ficha del cierre.

# Estado del cierre · Almacenes del Valle de Sula · periodo 2026-09

**Entidad:** Almacenes del Valle de Sula (08010006129040) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Aprueba:** Sofía León

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `declared_close_vs_evidence` | El cierre se reporta cerrado (2026-10-05) y hay 6 señales abiertas que ese estado no explica | `2026-09/40-soportes/correo-estado-del-cierre.md` |

## El resultado

**Estado declarado:** cerrado · **Avance con evidencia:** 53.85 % · **Avance declarado:** 53.85 %

| Id | Tarea | Responsable | Vence | Estado |
|---|---|---|---|---|
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 |
| C-06 | Papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | en plazo |
| C-01 a C-05 | Módulos, bancos, facturas, cartera, provisiones | varios | 2026-10-01 a 2026-10-05 | cumplidas con evidencia |

**Ruta crítica:** C-07 → C-08 → C-09

Todo lo que llegó se procesó.

## Decisiones que tomé (nadie respondió)

- Periodo 2026-09.
- Ventas en 4135; compras en 5135, 5145 y 5195; ISV en 2408. Salen de las facturas.
- Se concilian 1305 y 2205. Se esperan los bancos andino-11301 y pacifico-11302.
- Aprueba Sofía León. No se dieron festivos.
- No dejé la marca `_CRITERIO_FINANZAS.txt`, porque nadie dio un sí.

## Siguiente paso

Las 7 señales abiertas están en `resultados.json`. Por tipo son:
- factura sin registro
- registro sin factura
- factura fuera del rango autorizado
- banco sin conciliar
- partida antigua
- requerimiento del auditor sin responder
- el desajuste entre lo declarado y lo evidenciado

El detalle de cada una sale con `/close-scan`. El checklist lo tomé como aprobado, porque así viene en el archivo de la organización. Falta que una persona lo apruebe.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

La salida quedó en `estado-finanzas/08010006129040-almacenes-del-valle-de-sula/corridas/salida-finance-setup.md` y la corrida está registrada como `2026-10-06-finance-setup-1`.

Esa salida también incluye las dos líneas de introducción y el reporte tal como lo escribió el motor. El archivo guardado dice que el extracto de pacifico-11302 en PDF "si se quiere cruzar con el xlsx" está pendiente. No lo verifiqué, y ese pendiente no es un hallazgo del motor.