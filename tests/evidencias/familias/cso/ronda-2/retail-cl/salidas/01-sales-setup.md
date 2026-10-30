# /criterio-sales:sales-setup comercial/76543210-3-tiendas-del-maipo

Augusto quedó instalado sobre Tiendas del Maipo (76543210-3, Chile, CLP) y corrió el reporte del embudo de 2026-10. El reporte señala 9 oportunidades para atender y el motor marcó además 1 señal de pronóstico sin respaldo.

**Configuración**
- **CRM:** las tres exportaciones (2026-10-01, 2026-10-16 y 2026-11-03) se reconocieron como Zoho. Tienen 19 filas cada una y no les falta ninguna columna.
- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez, con comprobante en `.criterio/terminos/`.
- **Reglas:** 30 días sin actividad detienen una oportunidad y el cierre puede correrse 2 veces, tal como dice `politica-comercial.md`.
- **Pronóstico comprometido:** el acta del 2026-10-02 compromete 756.000.000. El mejor escenario, 806.400.000, no se compromete y no entró a la ficha.
- **Sin marca de raíz:** no dejé `_CRITERIO_COMERCIAL.txt` porque nadie podía autorizarlo.

**Qué encontró el reporte**
- **Cinco oportunidades en «Compromiso» sin orden de compra:** OPP-2303, OPP-2320, OPP-2321, OPP-2322 y OPP-2323.
- **Cuatro oportunidades detenidas:** OPP-2305, OPP-2324, OPP-2325 y OPP-2326 llevan 35 días sin actividad, desde el 2026-10-01.
- **Pronóstico sin respaldo:** esa señal no aparece en el reporte del embudo. El detalle sale con `/forecast-check`, que no corrí.

La ficha del periodo (`estado-comercial/76543210-3-tiendas-del-maipo/comercial/2026-10/ficha.json`) tiene 14 propuestas, 5 órdenes de compra y el pronóstico del acta. Dejé fuera los correos y teléfonos de contacto de los clientes.

La corrida quedó registrada como `2026-11-05-sales-setup-1`, con el reporte completo en `estado-comercial/76543210-3-tiendas-del-maipo/corridas/salida-sales-setup.md`.