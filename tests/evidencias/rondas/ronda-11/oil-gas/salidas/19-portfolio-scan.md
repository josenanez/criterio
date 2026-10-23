# /criterio-portfolio:portfolio-scan 

El barrido terminó. Leí 41 de 66 documentos y dejé 10 fichas nuevas, selladas y registradas en la corrida `2026-10-23-portfolio-scan-1` (190 segundos medidos).

Los términos ya estaban vigentes (versión 1.2, aceptada por José Francisco Ñáñez), así que no hubo que aceptar nada.

- **Proyectos:** hay 13 con ficha. Las 10 nuevas son PRY-199, 201, 203, 205, 206, 207, 208, 209, 210 y 211. Los otros 3 (PRY-200, 202 y 204) no cambiaron en sus 25 documentos y no los toqué.
- **Lectura:** fue un solo lote de 10 proyectos, uno tras otro y sin subagentes. No existe la carpeta `entrada/`, así que no moví nada.
- **XML:** el inventario marcó 4 cronogramas XML como ilegibles, pero `texto.py` sí extrajo su texto. Leí los de PRY-206, 209 y 210. El de PRY-204 no estaba en el plan. Conviene confirmar algún hito contra el original.
- **Campos sin dato:** la autoridad del gerente y la fase quedan en `not_found` en las 10 fichas. También faltan el cronograma y los hitos en PRY-201, 203 y 207.

Lo que muestran los documentos (el cálculo de señales es del script; la lista completa está en la salida de la corrida):
- **Hitos sin acta:** hay 15 hitos declarados cerrados sin acta de recibo. PRY-210 tiene sus 4 hitos cerrados así.
- **Cierres vencidos:** PRY-201, 206 y 210 pasaron su fecha de cierre sin una línea base nueva.
- **Gasto mayor que lo comprometido:** PRY-206 y PRY-211 tienen más ejecutado que comprometido.
- **Compromisos vencidos:** dos, uno en PRY-208 (Ricardo Salas) y otro en PRY-209 (María Restrepo).
- **Hito vencido y abierto:** PRY-209 «Pozos perforados», con fecha 2026-10-13.
- **Proveedor:** en PRY-208, el «Alquiler del taladro» del contrato CT-751 sigue pendiente desde 2026-01-05. La factura FV-1751 coincide en valor con la «Bolsa de horas», que sí tiene acta.

Archivos en `estado/`:
- `corridas/salida-portfolio-scan.md`
- `records/PRY-199.json` y las otras 9 fichas nuevas

Como hay más de un proyecto, puedo generar el informe consolidado con `/portfolio-report`.