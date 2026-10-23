# /criterio-product:product-requirements 

## Registro — Inspección con drones (PRD-309) · al 2026-10-23

Hay 15 requerimientos y 13 están decididos. El 84.6% de los decididos tiene evidencia y el 0% tiene un proyecto que lo ejecute.

Los términos ya estaban vigentes (v1.2, aceptados el 2026-10-22 por José Francisco Ñáñez), así que no registré nada nuevo. No hay carpeta de fichas de proyecto, así que `compute` corrió sin `--fichas`. Que ningún requerimiento tenga proyecto significa que no hay ficha que lo confirme.

### Se va a construir y nadie lo pidió
| REQ | Estado | Doliente |
|---|---|---|
| REQ-4900 | aceptado (2026-08-15) | Beatriz Cuéllar |
| REQ-4907 | aceptado (2026-06-26) | Elena Duarte |

Ninguno tiene una sola cita de quien lo pidió.

### Decidido y nadie lo está construyendo
Son los 13 aceptados, ninguno con proyecto. REQ-4905 (aceptado el 2026-03-31) y REQ-4910 (el 2026-04-22) llevan más de seis meses así.

### Sin doliente
REQ-4912 está propuesto y ningún documento le nombra un doliente.

### Sin criterio de aceptación
REQ-4901, REQ-4903 y REQ-4913, todos aceptados. REQ-4904 (propuesto) tampoco lo tiene, pero no se le exige.

### Decidido sin documento que lo respalde
No lo calculé. `compute` no emite esa señal, así que no lo afirmo ni lo descarto. Se puede mirar uno por uno con `/product-requirements REQ-xxxx`.

### Lleva meses y nadie lo decide
| REQ | Propuesto hace | Quién tiene la facultad |
|---|---|---|
| REQ-4912 | 208 días | No está definido: `authority` es null en la configuración |
| REQ-4904 | 183 días | No está definido: `authority` es null en la configuración |

Propongo decidirlos, no cerrarlos por viejos. Primero hay que nombrar quién tiene la facultad. Laura Vélez es la gerente de producto y además es doliente de REQ-4904.

### Evidencia vieja
Los 13 requerimientos con evidencia se apoyan en una sola entrevista del 2025-08-21, de hace 14 meses: «Lo necesito y hoy no lo tengo.» Esa cita no nombra ninguno de los requerimientos. Es una fuente repetida, no 13 pedidos.

### Otros vacíos
El supuesto «La licencia ambiental lo permite» lleva 161 días sin verificar. En la definición también faltan el criterio de éxito y la autoridad.

### Por estado
| propuesto | aceptado | en construcción | entregado | descartado |
|---|---|---|---|---|
| 2 | 13 | 0 | 0 | 0 |

### Siguiente paso
Hay 13 decididos que nadie construye, así que corresponde `/product-trace`. `/product-charter` solo aplica a un aceptado con evidencia y criterio. Los que cumplen eso tienen evidencia vieja y de un único origen, así que habría que renovarla antes.

La corrida quedó registrada como `2026-10-23-product-requirements-1`: 35 hallazgos en 24 segundos. La salida completa está en `estado-producto/PRD-309/corridas/salida-product-requirements.md`.