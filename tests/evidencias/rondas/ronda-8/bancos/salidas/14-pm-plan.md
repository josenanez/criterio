# /criterio-project:pm-plan 

El borrador del plan de PRY-202 (Migración a la nube) está hecho y la corrida quedó registrada como `2026-10-17-pm-plan-1`. El plan no tiene ninguna fecha comprometida ni duraciones inventadas, y el acta tiene huecos que impiden descomponer el alcance con fundamento.

Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-17, v0.3.13), así que no hubo que registrarlos de nuevo. El proyecto ya tiene línea base (cronograma v1) y una versión vigente (v2), y este borrador no las reemplaza ni crea una nueva.

## Lo que le falta al acta
- **Alcance:** solo dice «Componente 1/2/3». La WBS no tiene de dónde sacar entregables reales, así que los nodos salen de los hitos del cronograma v1 y de los contratos, y van marcados como supuesto.
- **Fuera de alcance:** dice «Lo que otro proyecto cubre», sin nombrar el proyecto ni la cosa. Con eso no se puede evaluar CC-01, la solicitud de ampliación de alcance (+76 días, +152.000.000 COP).
- **Criterio de éxito:** «en producción y medido», sin umbral ni quién lo certifica.
- **Objetivo del negocio:** genérico, sin beneficio ni indicador.
- **Autoridad del gerente:** no está declarada.
- **Dependencias:** dice «Ninguna declarada», pero hay dos contratos con Datacore Colombia (CT-243 y CT-267).
- **Patrocinador:** sí está (María Restrepo).

## Lo demás
- **WBS:** solo dos nodos salen del acta (el entregable raíz y la medición). Los hitos y los tres entregables de Datacore van como supuesto, y el aceptante queda «sin definir» salvo en los de Datacore, donde firma el gerente.
- **Duplicado posible:** CT-243 y CT-267 tienen entregables con el mismo nombre («Licenciamiento del motor», «Bolsa de horas de desarrollo»). Quedó en «Sin definir» para que el gerente lo aclare con el proveedor.
- **Orden:** secuencia de dependencias sin fechas, declarada como supuesto mío, no del acta.
- **Análogos:** ninguno. La configuración no apunta a una carpeta de fichas de la PMO, y los otros proyectos (PRY-199 a PRY-211) no tienen fichas que citar.
- **Preguntas para el equipo:** nueve, una por cada duración vacía.
- **Para comprometer una fecha falta:** disponibilidad real del equipo, fecha confirmada del proveedor, ventana de la sala de producción, la decisión del comité sobre CC-01 y la definición de «medido».

Dos limitaciones. El acta de recibo en PDF del ambiente de pruebas (`2026-10-04-acta-recibo-ambiente-de-pruebas-certificado.pdf`) no la abrí, así que el estado «cerrado» de ese hito sale del cronograma sin verificar. Los 17 hallazgos que reporta la corrida son señales de otros comandos ya registradas sobre el proyecto, no de este borrador.

Archivos en `estado/PRY-202-migración-a-la-nube/corridas/`:
- `salida-pm-plan.md`
- `2026-10-17-pm-plan-1.md`