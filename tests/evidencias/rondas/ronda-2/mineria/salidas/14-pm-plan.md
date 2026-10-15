# /criterio-project:pm-plan 

# Plan — PRY-205 Sistema de gestión de seguridad · borrador del 2026-10-15
**Desde:** acta de constitución del 2025-08-11 (`00-gobierno/2025-08-11-acta-constitucion.docx`) · **Criterio de éxito:** «Sistema de gestión de seguridad en producción y medido.» (acta)

**Antes de leer:** el acta es de hace 14 meses y el proyecto ya está en marcha: el cronograma v1 tiene dos hitos cerrados y el informe del 2026-10-11 declara 26 % de avance. Este borrador sirve para ver qué sostiene el acta hoy. Si lo que sigue es replanificar, eso es un cambio de línea base y pasa por control de cambios, no por este comando.

*Términos: vigentes (v0.3.8, aceptados por José Francisco Ñáñez el 2026-10-15); no hizo falta registrarlos de nuevo.*

## Lo que le falta al acta
| Qué | Consecuencia de planificar sin eso |
|---|---|
| **Alcance vacío.** Dice «Componente 1, Componente 2, Componente 3» y fuera de alcance «Lo que otro proyecto cubre». Son marcadores de plantilla. | No hay entregables que descomponer. La WBS no puede salir del acta: sus tres ramas principales quedan **sin definir**. |
| **Criterio de éxito sin umbral.** «En producción y medido»: no dice qué se mide, con qué meta ni quién lo mide. | No se puede saber cuándo el último entregable está aceptado. «Medido» queda sin dueño ni fecha. |
| **Autoridad no declarada.** El acta nombra patrocinador y comité, pero no qué puede decidir el gerente. | No se sabe qué puedes resolver al planificar y qué hay que subir. Todo lo dudoso se sube por defecto. |
| **Quién acepta cada entregable.** El acta no lo dice. | Los nodos terminales no tienen aceptante declarado. |
| **Dependencias: «Ninguna declarada».** Pero el informe del 2026-10-11 menciona la ventana de parada de planta definida por operaciones, y las notas del 2026-10-15 hablan de un proveedor para «la siguiente fase». | El plan nace con dependencias externas que el acta niega. Ni el proveedor ni la parada tienen documento de respaldo en la carpeta. |
| **Objetivo genérico.** «Entregar sistema de gestión de seguridad para Geología.» | No distingue qué sistema, qué procesos ni qué sitios cubre. |

Sí está en el acta: patrocinador (María Restrepo), gerente (Rubén Cárdenas), comité (Comité de Operaciones), presupuesto aprobado (9.500.000.000 COP, 2025-08-11), inicio 2025-08-21 y cierre 2027-01-19.

## WBS
Cada nodo debería ser algo que alguien recibe y acepta. Con lo que hay, solo se puede escribir la estructura; el contenido no está.

| # | Entregable | Quién lo acepta | De dónde sale | Duración |
|---|---|---|---|---|
| 1 | Componente 1 (el acta no dice qué es) | Sin definir | **Sin definir** (el acta lo nombra, no lo describe) | vacía |
| 2 | Componente 2 (ídem) | Sin definir | **Sin definir** | vacía |
| 3 | Componente 3 (ídem) | Sin definir | **Sin definir** | vacía |
| 4 | Ingeniería básica aprobada | Sin definir | **Supuesto**: sale del cronograma v1 (línea base 2026-01-15, cerrado), no del acta; se asume que es un entregable del proyecto y no de un componente | vacía |
| 5 | Ingeniería de detalle aprobada | Sin definir | **Supuesto**: cronograma v1 (línea base 2026-06-11, cerrado) | vacía |
| 6 | Licencia y permisos obtenidos | Sin definir | **Supuesto**: cronograma v1 (línea base 2026-11-06, en curso). No hay documento de licencia ni de permisos en la carpeta | vacía |
| 7 | Sistema en producción | Sin definir | **Del acta**: criterio de éxito, primera mitad | vacía |
| 8 | Sistema medido (con qué indicador, no se sabe) | Sin definir | **Del acta**: criterio de éxito, segunda mitad. El indicador es **sin definir** | vacía |
| 9 | «El punto 4» | Sin definir | **Sin definir**: es el compromiso de Mauricio Pérez en el comité del 2026-10-12 (vencía ese día) y en las notas del 2026-10-15 se reprograma para el 2026-10-29. Ningún documento dice de qué lista es el punto 4 | vacía |

Las duraciones quedan vacías: lo único citable es el calendario del cronograma v1 y el inicio y cierre del acta, y eso son fechas, no duraciones por nodo. La relación de los hitos 4–6 con los componentes 1–3 no está en ningún documento.

## Orden
Lo que se puede ordenar sin inventar:
- 4 → 5 → 6, en ese orden, porque así está en el cronograma v1. El cronograma no declara dependencias; que cada una necesite a la anterior es un supuesto.
- 6 antes de 7: no se pone en producción sin licencia y permisos. **Supuesto.**
- 7 antes de 8: no se mide lo que no está en producción. Es lógica del criterio de éxito, no una cita.
- La parada de planta condiciona 7 (el informe la lista como riesgo y dice que se reprogramó). **Supuesto**: nada dice que 7 dependa de ella.
- El proveedor condiciona «la siguiente fase» (notas del 2026-10-15). **Qué fase es no está dicho**, así que no se puede ubicar en la WBS.
- Componentes 1–3: sin orden. No se sabe qué son ni si dependen entre sí.

Un dato del calendario vigente: entre el último hito del cronograma v1 (2026-11-06) y el cierre del acta (2027-01-19) hay 74 días. En ellos tendrían que caber los componentes que no aparecen en el cronograma, la puesta en producción y la medición. Sin saber qué contienen, no se puede decir si alcanza.

## Supuestos sobre los que está construido
| Supuesto | Qué pasa si resulta falso |
|---|---|
| Los tres hitos del cronograma v1 son entregables del proyecto y los acepta alguien identificable | Los nodos 4–6 no tienen aceptante y el avance cerrado no se puede sustentar. |
| La sucesión 4 → 5 → 6 es una dependencia real | Si no lo es, el camino hacia producción es más corto o más largo de lo que el cronograma sugiere. |
| La licencia y los permisos son condición para entrar a producción | Si no, el hito 6 no está en el camino crítico y su fecha pesa menos. |
| La ventana de parada de planta es la que gobierna la puesta en producción | Si el sistema entra sin parada, el riesgo del informe es otro. Si la parada es la ventana, la fecha de cierre depende de operaciones. |
| El proveedor mencionado en las notas es el mismo que entrega la siguiente fase | Si es otro, o no hay contrato, no hay entregable contractual que seguir. |
| «Medido» se refiere a un indicador que ya existe y se puede obtener | Si hay que construirlo, es un entregable más y no está en el plan. |

Cuando el plan se apruebe, estos pasan al RAID con doliente. El riesgo de las notas del 2026-10-15 («el proveedor podría no llegar con el equipo completo», sin registrar) también.

## Sin definir
| Qué | Quién lo define |
|---|---|
| Contenido de los Componentes 1, 2 y 3 | El patrocinador (María Restrepo) o quien escribió el acta; el documento no lo dice |
| Qué se mide, con qué meta y quién lo mide | Sin definir; el criterio de éxito lo declara el patrocinador |
| Quién acepta cada entregable | Sin definir |
| Qué puede decidir el gerente | Sin definir; no hay autoridad declarada |
| Qué es «el punto 4» | Mauricio Pérez, que se comprometió a entregarlo |
| Qué fase es «la siguiente fase» y qué proveedor la entrega | Sin definir; no hay proveedor ni contrato en la carpeta |
| Fecha de la parada de planta | Operaciones; el informe dice que la define esa área |
| El ajuste de presupuesto que Laura Vélez prometió «la otra semana» | Sin definir; no hay fecha ni cifra |

## Proyectos análogos
La configuración no apunta a una carpeta de fichas de la PMO, así que no hay análogos a la vista. Dejo esa respuesta en vez de inventar una referencia. Con las fichas conectadas se podría traer lo que les pasó a proyectos con entregables del mismo tipo, sin estimar con eso.

## Preguntas para el equipo
1. ¿Qué entrega el Componente 1? ¿Y quién lo acepta?
2. ¿Qué entrega el Componente 2? ¿Y quién lo acepta?
3. ¿Qué entrega el Componente 3? ¿Y quién lo acepta?
4. ¿Cuánto toma terminar los componentes que no están en el cronograma v1?
5. ¿Cuánto toma obtener la licencia y los permisos, y qué falta hoy para tenerlos?
6. ¿Cuánto toma pasar a producción una vez tenidas la licencia y la ventana?
7. ¿Cuánto toma medir, y qué indicador y qué meta cuentan como «medido»?
8. ¿Qué es el punto 4 y qué lo hace cerrado?
9. ¿Qué es «la siguiente fase», qué proveedor la entrega y qué equipo se esperaba?
10. ¿Quién acepta los hitos de ingeniería básica y de detalle? ¿Dónde está el acta de recibo?

## Para comprometer una fecha falta
- **Disponibilidad real del equipo.** En las notas del 2026-10-15 aparecen Elena Duarte, Mauricio Pérez, Laura Vélez y Óscar Ramírez, pero ningún documento dice qué rol cumple cada uno ni cuánto tiempo tiene para el proyecto.
- **Fecha del proveedor.** La revisión con el proveedor queda para el 2026-10-25 (Óscar Ramírez), pero no hay contrato ni cronograma del proveedor en la carpeta.
- **Ventana de la parada de planta.** Operaciones la define y el informe dice que se reprogramó; ninguna fecha está escrita.
- **Contenido de los componentes y significado de «medido».** Sin eso no hay nodos que fechar.

No comprometo ninguna fecha. Esa decisión es del gerente.

---
La corrida quedó registrada como `2026-10-15-pm-plan-1`. La nota que guardé dice «3 de 9 nodos sin definir»; son 4 (nodos 1, 2, 3 y 9). Esta salida es la correcta. Cuando apruebes el plan puedo registrarlo como línea base original y pasar los supuestos al RAID.