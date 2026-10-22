# /criterio-budget:budget-setup finanzas/900123456-banco-andino

Terminé la instalación de Tomás para Banco Andino y la corrida quedó registrada como `2026-10-06-budget-setup-2`. El texto completo está en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-setup.md`.

- **Configuración:** ya existía una de una instalación anterior y la reutilicé. Corregí una ruta: `pmo_records` apuntaba a `estado/records`, que no existe, y ahora apunta a `estado-pmo/records`, donde está `PRY-310.json`. La configuración pasó la validación.
- **Lo que vi:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.
- **Versión aprobada:** el acta 01 (2026-01-20) aprueba la versión 1. El acta 05 (2026-06-28) aprueba un traslado, y la versión 2 es del 2026-06-30. Ningún acta aprueba la versión 2 como tal, pero el motor la usa como vigente.
- **Términos:** registré la aceptación de José Francisco Ñáñez para la versión 0.7.0. El comprobante es `.criterio/terminos/aceptacion-criterio-budget-0.7.0-2026-10-06-2.md`, con su PDF. Esa versión ya estaba aceptada desde antes, así que quedó un segundo comprobante con sufijo `-2`.
- **Archivos fuera de lugar:** hay dos archivos de estado de una corrida anterior dentro de la carpeta de documentos (`presupuesto-2026/estado-finanzas/...`). No los moví ni los borré.
- **Marca de la raíz:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

Con corte a 2026-09, las señales del reporte son estas:

| Señal | Detalle |
|---|---|
| Servicios públicos (Administración) | Ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte, +15,0 %. |
| Administración se reporta dentro del presupuesto | Los números no lo sostienen en esa misma línea. |
| PRY-310 | La ficha dice 64.800.000,00 y el área tiene asignado 72.000.000,00. |

El resto de las líneas está entre −3 % y 0 % frente a lo aprobado al corte. El reporte también quedó en `estado-finanzas/900123456-banco-andino/presupuesto/2026/`.