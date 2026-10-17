# /criterio-portfolio:portfolio-scan 

Barrido terminado: escribí y sellé 10 fichas nuevas (PRY-199, 200, 201, 204, 205, 206, 207, 209, 210 y 211). Leí 43 de los 78 documentos. Los otros 35, de PRY-202, 203 y 208, no habían cambiado y no los abrí.

Los términos estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que volver a registrarlos. No quedó ningún archivo ilegible ni pendiente de clasificar. La carpeta `entrada/` no existe, así que no moví nada.

El script calculó 60 alertas en el portafolio. Lo más importante en los 10 proyectos leídos:
- **Hitos cerrados sin acta que lo pruebe:** PRY-200 (3), PRY-204 (2), PRY-205 (3), PRY-210 (4) y PRY-211 (2).
- **Verde contradicho por sus propios documentos:** PRY-200, PRY-209 y PRY-211.
- **PRY-210:** la factura FV-1100 cubre dos entregables y solo uno tiene acta. Otros dos entregables del contrato siguen sin recibirse.
- **PRY-206:** la solicitud de cambio CC-01 (+97 días) está aprobada, pero no hay línea base nueva que la refleje.
- **PRY-201:** hay un compromiso vencido, de Elena Duarte, que ya nació vencido.
- **Sin señal pese a estar vencidos:** PRY-199 no tiene alertas. PRY-207 y PRY-209 pasaron su fecha de cierre y no tienen cronograma, así que el cálculo no puede medirlas.
- **PRY-205:** el mismo nombre figura como patrocinador y como gerente.
- **Vacíos:** en las 13 fichas falta la autoridad del gerente, porque ninguna acta la dice.

Dos cosas para vigilar:
- **PRY-202:** el índice marca 18 citas de la ficha de su gerente (`pm_record`) como no resueltas. Las rutas no llevan el prefijo de la carpeta del proyecto, aunque los archivos existen. No toqué esa ficha.
- **Registro de la corrida:** `relectura` muestra 78 sin cambio y 0 releídos. Eso sale del orden en que se sella y no refleja las 43 lecturas reales. Los 43 sí quedaron registrados en el plan.

El resultado completo está en `estado/corridas/salida-portfolio-scan.md`. Si quieres el informe consolidado del portafolio, corre `/criterio-portfolio:portfolio-report`.