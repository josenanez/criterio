# /criterio-sales:sales-setup comercial/0990234566001-sistemas-integrados-del-guayas

Dejé a Augusto instalado sobre Sistemas Integrados del Guayas (0990234566001) y la primera revisión del embudo de octubre ya está hecha. Nadie contestó preguntas, así que tomé cada respuesta de los documentos.

- **Exportaciones del CRM:** las tres de `10-crm/` se reconocen como Zoho, con 19 filas cada una y sin columnas faltantes. Las fechas van día/mes/año.
- **Configuración:** quedó en `.criterio/comercial/0990234566001/config.json`, con Ecuador, USD y periodo 2026-10. Los umbrales salen de la política comercial: 30 días sin actividad detienen una oportunidad y el cierre puede correrse 1 vez.
- **Términos:** quedaron registrados a nombre de José Francisco Ñáñez (versión 1.3, 2026-11-05). El comprobante está en `.criterio/terminos/aceptacion-criterio-sales-0.2.0-2026-11-05.md` y en PDF. Los términos se los mostré tal cual en el registro de la corrida.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie podía autorizarla.
- **Ficha de 2026-10:** tiene 15 documentos de evidencia (11 propuestas y 4 órdenes de compra), sin datos de contacto de clientes. También tiene el pronóstico comprometido del acta del 2 de octubre.
- **Reporte `pipeline-check`:** el motor dejó 11 señales, que aparecen en el reporte con su monto y su cita:
  - OPP-1820, OPP-1821 y OPP-1822 están en «Compromiso» sin orden de compra.
  - OPP-1804, OPP-1826, OPP-1827 y OPP-1828 corrieron su fecha de cierre 2 veces, una más de lo permitido.
  - OPP-1805, OPP-1823, OPP-1824 y OPP-1825 llevan 35 días sin actividad.
- **Corrida:** quedó registrada como `2026-11-05-sales-setup-1`, con 12 hallazgos en total. El reporte trae 11 señales; la que falta es la de la meta contra lo cerrado, que se ve con `target-check`.

Un tropiezo mío: un `cd` hizo que `init` creara por error una carpeta de estado vacía dentro de la carpeta de documentos. La borré sin archivos adentro y la repetí en la ruta correcta.

El reporte está en `estado-comercial/0990234566001-sistemas-integrados-del-guayas/comercial/2026-10/reporte-pipeline-check.md`. Lo que le mostré a la persona, entero, está en `estado-comercial/0990234566001-sistemas-integrados-del-guayas/corridas/salida-sales-setup.md`.