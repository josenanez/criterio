# /criterio-portfolio:portfolio-scan 

El barrido terminó. Leí 49 de los 72 documentos y escribí y sellé las 10 fichas de proyectos nuevos. Los términos v1.0 ya estaban aceptados en la configuración (José Francisco Ñáñez, 2026-10-14). Como la sesión no tenía interfaz, no hubo preguntas que contestar.

- **Documentos:** de los 72, 23 no cambiaron y no se abrieron. Son los de PRY-205, PRY-208 y PRY-209. Ninguno fue ilegible. No hay carpeta `entrada/`, así que no se movió nada.
- **Fichas nuevas:** PRY-199, 200, 201, 202, 203, 204, 206, 207, 210 y 211.
- **Sin dato en las 10:** la autoridad del gerente y la fase no aparecen en ningún documento.

Lo que debe mirar la PMO:
- **Hitos cerrados sin acta:** 19 de 24 hitos declarados cerrados no tienen acta de recibo. El script cuenta 26 al sumar PRY-205, 208 y 209, que no releí.
- **Cierre vencido con cronograma cerrado:** PRY-202, 207 y 211 pasaron su fecha de cierre y su cronograma da todos los hitos por cerrados. Los gerentes declaran 43 %, 80 % y 59 % de avance.
- **PRY-211, factura sin respaldo:** la factura FV-1509 es por 2.179.464.246 COP, el valor de tres entregables del contrato CT-509. Solo hay una acta de recibo, la de la bolsa de horas.
- **Cambios con el cronograma ya movido:** en PRY-203 la solicitud CC-01 sigue pendiente de comité y el cronograma v2 ya movió la fecha. En PRY-210 la CC-01 dice "autorizada por el comité" sin decir cuál, y el acta del 13 de octubre no la menciona.
- **Compromisos vencidos:** uno en PRY-204 (Gustavo Neira, para el 2026-09-27) y uno en PRY-210 (Beatriz Cuéllar, para el 2026-10-03).
- **Ejecutado mayor que comprometido:** PRY-200 y PRY-203 reportan más ejecutado que comprometido.
- **PRY-208:** las rutas de la ficha del gerente no resuelven contra la raíz de documentación. No la toqué, porque tiene otro escritor.

La corrida quedó registrada con `snapshot` y `corrida` (id `2026-10-14-portfolio-scan-1`, 198 segundos, 60 hallazgos en el portafolio). El script también marcó como hallazgos que mi resumen no incluye: tres proyectos en silencio (PRY-200, 201 y 211), tres con lo declarado contra la evidencia (PRY-201, 204 y 210), y atraso en PRY-210.

Archivos en `estado/`:
- `corridas/salida-portfolio-scan.md`
- `records/`