# /criterio-finance:finance-setup finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica

## Listo — Distribuidora del Ybytyruzú (sintética)

**Lo que miré:** 65 archivos · periodos 2026-01 a 2026-09 y el presupuesto 2026 · 0 fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.2.0 (términos 1.3). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-1.2.0-2026-10-06.md` y `.pdf`.

**Lo principal:** Sofía León escribió el 2026-10-05 que «el cierre de septiembre está cerrado». El motor encontró 5 señales abiertas que ese estado no explica. Solo 5 de las 9 tareas del checklist tienen evidencia (avance con evidencia 53,85 %). C-06 a C-09 siguen sin cerrar, y C-07, C-08 y C-09 forman la ruta crítica.

# Estado del cierre · Distribuidora del Ybytyruzú (sintética) · periodo 2026-09

**Entidad:** Distribuidora del Ybytyruzú (sintética) (88612904-4) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.2.0 · **Aprueba:** Sofía León

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `declared_close_vs_evidence` | El cierre se reporta cerrado (2026-10-05) y hay 5 señales abiertas que ese estado no explica | `2026-09/40-soportes/correo-estado-del-cierre.md` |

## El resultado

**Estado declarado:** cerrado · **Avance con evidencia:** 53,85 % · **Avance declarado:** 53,85 % (ponderados por criticidad)

| Id | Tarea | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 | — |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | en plazo | — |
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | cumplida con evidencia | `2026-09/40-soportes/C-01-soporte.md` |
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida con evidencia | `2026-09/40-soportes/C-02-soporte.md` |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | cumplida con evidencia | `2026-09/40-soportes/C-03-soporte.pdf` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | cumplida con evidencia | `2026-09/40-soportes/C-04-soporte.md` |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | cumplida con evidencia | `2026-09/40-soportes/C-05-soporte.pdf` |

**Ruta crítica del cierre:** C-07 → C-08 → C-09

**Lo que no se pudo procesar:** nada. Todo lo que llegó se procesó.

**Qué falta para que esto sea mejor:** el reporte muestra una sola señal, pero el motor contó 6. Las otras cinco son un banco sin conciliar, un registro sin factura electrónica, una factura duplicada, una factura fuera de autorización y un requerimiento del auditor sin respuesta. Están en `resultados.json`. Se abren con `bank-reconcile`, `einvoice-check` y `audit-pack`.

## Qué decidí por mi cuenta

Nadie respondió preguntas en esta prueba, así que tomé estas respuestas de los documentos. Quedaron en la ficha como las 10 preguntas del reporte.

- **Entidad:** nombre y RUC salen de la carpeta; país Paraguay y moneda PYG salen de que las facturas son del SIFEN.
- **Marco contable:** normas nacionales del Consejo de Contadores Públicos del Paraguay, basadas en las NIIF (F-42). Elegí ese porque la entidad no es un banco.
- **Periodo:** 2026-09.
- **Cuentas de las facturas:** ventas 4135; compras 5135, 5145 y 5195; IVA 2408. Son las que sostienen facturas del periodo.
- **Cuentas que se concilian:** 1305 y 2205, que tienen auxiliar en agosto y septiembre.
- **Bancos esperados:** andino-13701 y pacifico-13702.
- **Checklist:** el de la organización, `00-referencia/checklist-cierre.csv`. Lo marqué como aprobado, que es una suposición mía: nadie lo confirmó.
- **Quién aprueba:** Sofía León, porque es la responsable de C-08 y C-09. No hay festivos declarados.
- **Estado:** `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica`.
- **Marca `_CRITERIO_FINANZAS.txt`:** no la dejé, para no escribir nada dentro de los documentos.

La configuración está en `.criterio/finanzas/88612904-4/config.json`. La salida de esta corrida está en `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-finance-setup.md`. La corrida quedó registrada como `2026-10-06-finance-setup-1`, con 6 hallazgos.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.