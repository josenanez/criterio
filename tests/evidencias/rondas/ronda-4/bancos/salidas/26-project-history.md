# /criterio-portfolio:project-history PRY-201

## Historia · PRY-201 Core de depósitos · 2026-04-12 a 2026-10-13

**Leí:** 8 documentos, entre el 2026-04-12 y el 2026-10-13. Son todos los de la carpeta del proyecto. Los términos ya estaban vigentes (versión 0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.

**Trimestres sin un solo documento:** julio–septiembre de 2026. Entre el 2026-04-12 y el 2026-10-02 pasaron 173 días sin ningún documento.

### En una línea
El proyecto se aprobó el 2026-04-12 con cierre el 2027-04-06 según el cronograma v1. Después hay cinco meses y medio de silencio. En la primera quincena de octubre aparecen los dos recibos de hitos que el plan fechaba en junio y septiembre, la solicitud de cambio CC-01 (+20 días) y un cronograma v2 que mueve el cierre al 2027-04-26 sin decir por qué.

### Las cuatro cifras
| Replanificaciones | Atraso acumulado vs. original | Meses declarando sin sustento | Cambios de gobierno |
|---|---|---|---|
| 1 | 20 días (5.7 %) | No se puede calcular: hay una sola declaración | 0 |

### Hallazgos
- **La replanificación no tiene motivo ni aprobador.**
  - **Fecha y efecto:** es del 2026-10-13 y mueve la salida a producción del 2027-04-06 al 2027-04-26.
  - **Posible causa:** los 20 días coinciden con CC-01, pero ningún documento los enlaza.
  - **Aprobación:** CC-01 dice «Autorizada por el comité» sin nombre ni acta. La única acta de comité de la carpeta es del 2026-10-02, cuatro días antes de la solicitud, y no la menciona.
- **Los recibos llegan tarde frente al plan, pero el plan no registra atraso.**
  - **Diseño funcional aprobado:** línea base 2026-06-30, recibo 2026-10-02, 94 días después.
  - **Ambiente de pruebas certificado:** línea base 2026-09-08, recibo 2026-10-09, 31 días después.
  - **Cronogramas:** ambos muestran esos hitos como cerrados en su fecha original. Un recibo tardío no prueba que el hito se terminara tarde; eso hay que preguntárselo a Carlos Peña.
- **El cronograma v1 tiene una inconsistencia de archivo.** Está fechado el 2026-04-12 pero ya marca como cerrados dos hitos con fechas de junio y septiembre. No puede reflejar el estado real de abril.
- **«Línea base original» tiene dos lecturas.** El acta de constitución dice cierre 2027-05-11 y el cronograma v1 dice 2027-04-06, ambos del 2026-04-12. El atraso de 20 días usa el cronograma v1; contra el acta sería menor.
- **No hay punto de separación calculable.** El 48 % declarado el 2026-10-13 cae dentro de lo que el plan sostiene (entre 40 % y 60 %).
- **Gobierno y compromisos sin cambios.** No hay cambios de gobierno. Hay un compromiso abierto, de Ricardo Salas (punto 9, para el 2026-11-05), sin repeticiones. El documento no dice a qué se refiere «punto 9».

### Lo que no sé
- Qué pasó entre abril y octubre.
- Por qué se movió el cierre y quién lo aprobó.
- Si el presupuesto aprobado incluye los 40.000.000 COP de CC-01. El informe sigue mostrando 6.800.000.000 COP, y su proyección de 7.022.864.553 COP lo supera en 3.3 %.

No atribuyo intención a nadie: los documentos muestran silencio y trazabilidad incompleta, y quién tiene esa conversación es una persona. Si hay una decisión que sacar de esto, la historia puede ir al comité del 2026-10-22 o al cierre del proyecto.

La corrida quedó registrada como `2026-10-15-project-history-1`, con 53 segundos y el texto completo en `estado/corridas/salida-project-history.md`. La corrida no midió cuántos documentos leí (`documentos: null`); la cifra de 8 es la que conté yo. La verificación contra las fuentes es de quien use este borrador.