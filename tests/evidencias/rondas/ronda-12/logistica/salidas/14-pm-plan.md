# /criterio-project:pm-plan 

# Plan — PRY-204 Cross docking en el puerto · borrador del 2026-10-28

**Términos:** ya estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no los registré de nuevo.

**Desde:** el acta del 2025-10-13. **Criterio de éxito:** «Cross docking en el puerto en producción y medido.» No dice medido contra qué ni quién lo mide.

El proyecto ya está en marcha: el informe del 2026-10-28 declara 53 % y verde, y existe el cronograma v1. Por eso este borrador reorganiza el trabajo sobre el acta. No es el plan original y no crea línea base nueva.

## Lo que le falta al acta
| Qué | Consecuencia de planificar sin eso |
|---|---|
| Alcance sin contenido: solo «Componente 1 / 2 / 3» | No hay entregables que descomponer. Esos nodos quedan sin definir. |
| «Fuera de alcance» dice «lo que otro proyecto cubre», sin decir cuál | No se puede trazar la frontera con ese otro proyecto. |
| Criterio de éxito sin métrica | No se sabe qué cuenta como «medido». El último hito del cronograma, pruebas con carga real, no equivale a «en producción y medido». |
| Autoridad no declarada en el acta | La configuración dice Comité de Inversiones, pero eso salió del setup, no del acta. No se sabe qué puede decidir la gerente sin subirlo. |
| Patrocinador y gerente son la misma persona (Liliana Torres) | No hay un patrocinador distinto a quien llevar excepciones; solo queda el Comité. |
| Dependencias: «ninguna declarada» | Las notas del 2026-10-28 mencionan un proveedor y el informe un «cliente ancla». Ninguno está en el acta. |
| Quién acepta cada entregable | No figura en ningún documento. |

## WBS
Ninguna duración tiene de dónde salir, así que todas van vacías. Nadie figura como aceptante de ningún nodo.

| # | Entregable | De dónde sale |
|---|---|---|
| 1 | Diseño de la operación aprobado | Supuesto (hito del cronograma v1, no del acta) |
| 2 | Permisos de operación obtenidos | Supuesto (cronograma v1) |
| 3 | Adecuación de la bodega terminada | Supuesto (cronograma v1) |
| 4 | Pruebas con carga real | Supuesto (cronograma v1) |
| 5–7 | Componentes 1, 2 y 3 | Sin definir (el acta solo los nombra) |
| 8 | Cross docking en producción | Del acta (criterio de éxito), sin detalle |
| 9 | Medición de resultados | Del acta («y medido»); qué se mide es sin definir |

## Orden
- **1 → 2 → 3 → 4:** así los encadena el cronograma v1.
- **4 → 8 → 9:** es mi lectura del criterio de éxito en orden. Ningún documento lo enlaza, así que es un supuesto.
- **Componentes 1–3:** no se pueden ordenar sin saber qué son.

## Supuestos
| Supuesto | Qué pasa si es falso |
|---|---|
| Los 4 hitos del cronograma son el esqueleto de entregables | Si los componentes 1–3 son otra cosa, la WBS omite trabajo que sí está en alcance. |
| «En producción» y «medido» son entregables propios, posteriores a las pruebas | Si el proyecto termina en las pruebas, el criterio de éxito pide más de lo que el plan construye. |
| Orden 4 → 8 → 9 | Si producción puede ir en paralelo con las pruebas, la ruta cambia. |
| El proveedor de las notas pertenece a este proyecto | Si es del «otro proyecto», ese riesgo no es de este plan. |
| La gerente puede aprobar este plan sin pasar por el Comité | El acta no lo dice. |

## Sin definir
- **Contenido de los componentes 1, 2 y 3:** lo define quien escribió el acta o el Comité.
- **Qué proyecto cubre lo excluido:** Comité o PMO.
- **Qué significa «medido»:** el área dueña (Seguridad y Salud en el Trabajo) y el patrocinador.
- **Quién acepta cada entregable:** el patrocinador, que hoy es la misma persona que la gerente.
- **Qué puede decidir la gerente sin subir:** el Comité.
- **Rol del proveedor y del cliente ancla:** la gerente con el Comité. No hay contrato en la carpeta.

## Proyectos análogos
Ninguno a la vista. La configuración no apunta a una carpeta de fichas de la PMO, así que no hay estimación por analogía y no la invento.

## Preguntas para el equipo
1. ¿Qué entregables son los componentes 1, 2 y 3, quién recibe cada uno y cuánto toma?
2. ¿Cuánto toma pasar de las pruebas a producción?
3. ¿Qué se mide, contra qué línea de base, y cuánto hay que observar para decir «medido»?
4. ¿Cuánto falta para cerrar las pruebas? El cronograma las marca al 50 %.
5. ¿Qué proyecto cubre lo que el acta deja fuera y dónde está el borde?
6. ¿El proveedor y el cliente ancla están dentro del alcance, con qué contrato y qué fecha?
7. ¿Quién acepta pruebas, producción y medición?
8. ¿Qué parte de la fase siguiente depende de que el proveedor llegue con el equipo completo?

## Para comprometer una fecha falta
- La disponibilidad real del equipo (no hay asignaciones en ningún documento).
- La fecha y el compromiso del proveedor para la fase siguiente.
- La ventana de la sala de producción y la fecha del cliente ancla.
- El contenido de los componentes y la definición de «medido». Sin eso no hay qué fechar.

## Después
Si el plan se aprueba, hay que registrarlo como línea base vigente sin borrar la original del 2025-10-13. También hay que pasar los supuestos al RAID con doliente. Hoy el RAID tiene dos riesgos y un incidente sin doliente, y ningún supuesto.

La corrida quedó registrada como `2026-10-28-pm-plan-1`, con la salida guardada en `estado/PRY-204-cross-docking-en-el-puerto/corridas/salida-pm-plan.md`.

El registro de la corrida muestra 13 señales abiertas (compromisos vencidos, reprogramados y sin fecha, y verde declarado frente a la evidencia). Son del estado del proyecto, no de este plan. No las analicé aquí.