# /criterio-sales:sales-setup comercial/CCM101010AB3-comercial-control-de-mexico

Augusto quedó instalado sobre Comercial Control de México (CCM101010AB3) para el periodo 2026-10, y el primer `pipeline-check` no deja nada que atender. Las tres exportaciones se leyeron completas y sin columnas faltantes.

**Exportaciones del CRM.** Las tres (`oportunidades-2026-10-01`, `2026-10-16` y `2026-11-03`, de 7 filas cada una) son de HubSpot. Mi propuesta inicial de Salesforce era incorrecta y la cambié en la configuración.

**Preguntas.** Nadie podía responder, así que tomé la respuesta de los documentos y la dije en una línea:
- **Periodo:** 2026-10, porque el acta del comité, la meta y la liquidación son de octubre. El corte de la exportación es el 2026-11-03.
- **Umbrales:** 30 días sin actividad detienen una oportunidad, y el cierre puede correrse hasta 2 veces, según `politica-comercial.md`.
- **Etapas:** salen de `00-referencia/etapas.csv`.

**Términos.** Quedó registrada la versión 1.3 a nombre de José Francisco Ñáñez, con comprobante fechado 2026-11-05. La primera vez que corrí `aceptar` salió con la fecha real del sistema (2026-10-29), así que lo repetí con `--today 2026-11-05`. El comprobante del 2026-10-29 sigue en `.criterio/terminos/` y no lo borré. No se autorizó dejar el archivo `_CRITERIO_COMERCIAL.txt` en la carpeta, así que no lo puse.

**Ficha del periodo.** Registré 8 documentos de evidencia (5 propuestas y 3 órdenes de compra) y el pronóstico comprometido de $ 2,205,000 del acta del 2026-10-02. El mejor escenario del acta, $ 3,360,000, no entra porque no se compromete. No guardé correos ni teléfonos de contacto.

**Primer resultado (`pipeline-check`).** Tiene 6 oportunidades y nada abierto: ninguna detenida y ninguna con cierre corrido más de las 2 veces permitidas. OPP-1604 y OPP-1607 se han corrido una vez cada una, y OPP-1601 y OPP-1602 ya están ganadas. El reporte está en `estado-comercial/CCM101010AB3-comercial-control-de-mexico/comercial/2026-10/reporte-pipeline-check.md`.

**Reservas:**
- El reporte dice «Sin documentos citados» en Fuentes, aunque la ficha sí cita los originales.
- `compute` devolvió 0 señales.
- No leí el `pipeline-check` para confirmar que esas dos cosas sean correctas. Conviene revisarlas antes de apoyarse en el «nada abierto».

La corrida quedó registrada como `2026-11-05-sales-setup-1`, con 0 hallazgos, y la salida completa está en `corridas/salida-sales-setup.md`.