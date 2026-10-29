# /criterio-portfolio:portfolio-scan 

Barrido terminado: leí 39 de los 74 documentos y dejé fichas nuevas para 10 de los 13 proyectos. Los términos ya estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no hubo que registrarlos de nuevo.

**Qué hice**
- **Alcance:** PRY-200, PRY-204 y PRY-206 no tenían documentos nuevos y conservan su ficha anterior. Fue un solo lote de 10 proyectos, uno tras otro y sin subagentes. Cada ficha se escribió y se selló al terminar su proyecto.
- **Fichas nuevas:** PRY-199, 201, 202, 203, 205, 207, 208, 209, 210 y 211.
- **Registro de la corrida:** la instantánea y la corrida quedaron guardadas. La salida completa está en `estado/corridas/salida-portfolio-scan.md`.
- **Tiempo:** el script midió 171 segundos.
- **Sin ilegibles:** el inventario marcó 5 cronogramas `.xml` como no legibles, pero `texto.py` los convirtió todos. Solo leí el de PRY-207. Los otros cuatro son de proyectos sin cambio y no los releí.
- **Nada movido:** no existe `entrada/`.
- **Pendiente de clasificar:** hay un `2026-10-28-notas-reunion.txt` suelto en la raíz de PRY-204. Es de ese proyecto, pero no entró en este plan y no lo moví.

**Qué hay que mirar**
- **Hitos cerrados sin acta:** el cronograma los declara cerrados, pero no hay acta que lo pruebe.
  - PRY-201: 2 de 3.
  - PRY-202: 4 de 4.
  - PRY-205: 2 de 5.
  - PRY-207: 3 de 3.
  - PRY-208: 2 de 4.
- **PRY-207:** declara verde con 24 % de avance, pero sus 3 hitos están cerrados y su cierre comprometido (2026-08-21) ya pasó.
- **PRY-202:** su cierre (2026-09-11) venció y sigue en 80 % y amarillo. Lo ejecutado supera a lo comprometido.
- **PRY-210 y PRY-211:** sus cierres (2026-10-15 y 2026-09-21) ya pasaron y siguen con avance parcial.
- **PRY-203:** aprobó un cambio de +40 días y +80 M COP, pero no hay cronograma que lo refleje.
- **PRY-199:** declara 1.080 M COP comprometidos, pero el único contrato (CT-199) suma 432 M. Es de estanterías y vehículos, no de pintura de portería. Conviene confirmarlo con el gerente.
- **Compromisos vencidos sin evidencia:** Liliana Torres en PRY-202 y Felipe Arango en PRY-205.
- **Campos vacíos:** «autoridad» y «fase» quedan sin dato en las 10 fichas.

Entre las 13 fichas, el script contó 49 hallazgos. Esa cifra incluye los de PRY-200, PRY-204 y PRY-206, que no releí.

Cierre: plugin v0.12.1, 10 fichas tocadas, y los términos están en https://www.josenanez.com/es/agents/criterio-pmo/legal.

Como hay más de un proyecto, puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`.