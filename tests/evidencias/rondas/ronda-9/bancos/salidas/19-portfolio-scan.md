# /criterio-portfolio:portfolio-scan 

El barrido terminó: leí 44 de los 71 documentos, escribí y sellé 10 fichas nuevas, y los otros 27 no habían cambiado. Registré la corrida con `portafolio.py corrida` (id `2026-10-17-portfolio-scan-1`) y tomé la instantánea.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no hubo que registrarlos de nuevo. La configuración existía y no inventé nada.

- **Proyectos con ficha nueva:** PRY-199, 202 y 204 a 211. PRY-200, 201 y 203 no se tocaron. No hay archivos ilegibles ni carpeta `entrada/`.
- **Contradicciones entre documentos:** ninguna.
- **Hitos cerrados sin acta de recibo:** 202, 206, 207 y 210. En 210 son cuatro.
- **Compromisos vencidos:** 204, 205 y 210. En 210 el de Andrés Lozano lleva 22 días vencido.
- **Entregables de proveedor vencidos sin entregar:** 205 (uno) y 210 (dos).
- **Sin documentos recientes:** 208 lleva 17 días y 209 lleva 21.
- **Cierre comprometido ya pasado:** 207, 209 y 211.
- **Proyección sobre el presupuesto:** 202 en 27,6% y 207 en 22%.
- **Solicitud de cambio CC-01 de PRY-211:** pide +116 días y +232.000.000 COP, y sigue pendiente del comité.
- **Sin cronograma:** 208, 209 y 211, así que no hay hitos que medir.
- **PRY-199:** no tiene señales.
- **Facturación de PRY-210:** la factura FV-1882 cuadra con los dos entregables que sí tienen acta.
- **Campos sin dato:** la autoridad y la fase no están en ningún acta y quedan `not_found` en los 10 proyectos. El producto también queda vacío en 202, 205, 208 y 210, porque el acta dice «No aplica».
- **Fechas nuevas de salida:** los informes de 210 y 211 dicen «se reprogramó la salida» pero no dan la fecha nueva. Dejé la comprometida y no inventé otra.
- **Compromisos con fecha anterior a su minuta:** los de 204, 205 y 210 vencían antes de la minuta que los registra. Los guardé como vencidos, con la fecha tal como está escrita.
- **Estado de los entregables:** guardé «en curso» como pendiente en el entregable de proveedor y «recibido» como aceptado.
- **Scripts encadenados:** corrí los `sellar` de 205 a 207 y de 208 a 211 en un bucle por llamada, no uno por llamada como pide la plantilla.

La salida completa está en `estado/corridas/salida-portfolio-scan.md`. El siguiente paso natural es `/portfolio-report`, con estas contradicciones y compromisos vencidos ya a la vista.