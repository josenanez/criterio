# /criterio-portfolio:portfolio-scan 

El barrido terminó: escribí y sellé 10 fichas nuevas, tomé la instantánea y registré la corrida (`2026-10-17-portfolio-scan-1`).

- **Términos:** estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que volver a registrarlos.
- **Alcance:** había 91 documentos, de los que leí 71; 20 no habían cambiado. Todos eran legibles.
- **Proyectos:** las 10 fichas son PRY-199, 200, 202, 203, 204, 205, 206, 207, 210 y 211. PRY-201, 208 y 209 no cambiaron y no las toqué.
- **Ejecución:** fue un solo lote, uno tras otro en esta conversación, sin subagentes. La corrida tardó 260 segundos.
- **Archivos movidos:** ninguno, porque no existe `entrada/`. Dejé `2026-10-17-notas-reunion.txt` de PRY-203 donde estaba, en la raíz de la carpeta del proyecto.
- **Campos sin dato:** la autoridad del gerente y la fase faltan en las 10 fichas. El producto falta en 5, porque el acta dice «No aplica».

El script calculó 90 señales sobre las 13 fichas. Estas son las que más pesan:
- **Hitos cerrados sin acta:** 28 en total, según el script. Mi cuenta a mano fue 22 porque no incluí PRY-201 ni PRY-208.
- **Facturas sin entrega recibida:** PRY-206 facturó 182.444.266 sin ningún entregable recibido. PRY-203 facturó más de lo que tiene recibido. En PRY-210 solo uno de los tres entregables facturados tiene acta.
- **PRY-202, 210 y 211:** el cronograma v2 ya mueve la fecha de cierre por un cambio (CC-01) que aún no se aprueba (en PRY-202 y 211) o que se aprobó después (en PRY-210).
- **PRY-211:** el patrocinador y el gerente son la misma persona, y declara 27 % de avance con los cinco hitos cerrados.
- **PRY-207:** está en rojo, con cierre comprometido para el 2026-04-17, sin cronograma ni contrato.
- **PRY-203:** concentra 26 de los 33 compromisos. Uno lleva 6 reprogramaciones. La ficha del gerente quedó aparte, en `pm_record`.

El texto completo de lo que le mostré está en `estado/corridas/salida-portfolio-scan.md`. Puedo producir el informe consolidado con `/portfolio-report`, que es donde se calculan desviaciones y semáforo y se contrasta la ficha del gerente de PRY-203 con esta lectura.