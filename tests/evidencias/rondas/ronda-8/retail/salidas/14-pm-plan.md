# /criterio-project:pm-plan 

# Plan — Tienda en línea (PRY-200) · borrador del 2026-10-17

**Desde:** el acta de constitución del 2025-09-02. **Criterio de éxito:** «Tienda en línea en producción y medido».

Los términos v1.1 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo.

**Contexto:** el cierre del acta (2026-09-07) ya pasó. El informe declara rojo y 69 %, y el cronograma v1 marca los cinco hitos como «cerrado» sin acta de recibo en la carpeta. Solo existe la línea base v1, así que este borrador funciona como replanificación. Cualquier fecha nueva pasa por control de cambios.

## Lo que le falta al acta
| Qué | Consecuencia |
|---|---|
| Alcance: «Componente 1, 2, 3» sin contenido | No se puede descomponer por entregable. El 69 % no tiene sobre qué medirse. |
| Fuera de alcance: «Lo que otro proyecto cubre» | No dice qué proyecto ni qué. No hay frontera frente al riesgo de regulación de datos. |
| Criterio de éxito sin umbral («medido») | No se puede aceptar ni rechazar. |
| Sin autoridad declarada | No se sabe qué decides al replanificar y qué subes al comité. |
| Dependencias: «Ninguna declarada» | Hay un proveedor sin fecha de entrega y un cambio regulatorio posible. |
| Sin quién acepta cada entregable | Hay patrocinador (Jorge Medina), pero no quien recibe. |

## WBS
Todas las duraciones están vacías: el acta no trae ninguna y no hay otra fuente citable.

| # | Entregable | Quién acepta | De dónde sale |
|---|---|---|---|
| 1–3 | Componentes 1, 2, 3 | sin definir | del acta (nombre); contenido sin definir |
| 4 | Tienda en producción | sin definir | del acta |
| 5 | Medición (qué y con qué meta) | sin definir | del acta; meta sin definir |
| 6 | Diseño de la experiencia aprobado | sin definir | supuesto (hito del cronograma v1) |
| 7 | Ambiente de pruebas certificado | sin definir | supuesto (cronograma v1) |
| 8 | Integración con el ERP | sin definir | supuesto (cronograma v1) |
| 9 | Prueba de carga superada contra el umbral pactado | sin definir | supuesto (informe: «se repite») |
| 10 | Piloto en tiendas | sin definir | supuesto (cronograma v1) |
| 11 | Despliegue en la cadena | sin definir | supuesto (cronograma v1) |
| 12 | Última entrega del proveedor | sin definir | supuesto (informe, sin fecha) |

## Orden
Sin fechas. Tomando el orden del cronograma v1 como supuesto: 6 → 7 → 8 → 10 → 11 → 4 → 5. El nodo 9 (carga) va entre 8 y 11 si el umbral es condición de salida, y eso no está dicho en ningún documento. El nodo 12 queda suelto. Los nodos 1–3 no se pueden ordenar.

## Supuestos
| Supuesto | Si resulta falso |
|---|---|
| Los hitos del cronograma son entregables aceptables | Caen los nodos 6–11. |
| El orden del cronograma v1 sigue vigente | Hay que rehacer el orden con el equipo. |
| El umbral de carga es previo al despliegue | Cambia la ruta crítica. |
| La entrega del proveedor es una sola | El nodo 12 se descompone. |
| Medir es medir en producción | El nodo 5 se adelanta. |

## Sin definir
| Qué | Quién define |
|---|---|
| Qué son los componentes 1–3 | Patrocinador con el gerente |
| Fuera de alcance concreto | Patrocinador y comité |
| Qué se mide y con qué meta | Patrocinador |
| Quién acepta cada entregable | Patrocinador |
| Autoridad del gerente | Comité de Transformación Digital |
| Umbral de la prueba de carga y dónde se pactó | Sin dueño visible |
| Proveedor y contrato | Sin dueño visible (no hay proveedor en la ficha ni contrato en la carpeta) |
| Fase actual | Sin dueño visible |

## Proyectos análogos
Ninguno a la vista. La configuración no apunta a una carpeta de fichas de la PMO, así que no hay referencia de duración.

## Preguntas para el equipo
1. ¿Qué son los componentes 1–3 y cuánto toma cada uno?
2. ¿Cuánto toma poner la tienda en producción?
3. ¿Qué se mide, con qué meta y por cuánto tiempo?
4. ¿El diseño sigue aprobado con los requisitos no funcionales? ¿Qué falta?
5. ¿Qué falta para certificar el ambiente de pruebas?
6. ¿Qué falta de la integración con el ERP?
7. ¿Cuánto toma repetir la prueba de carga y corregir lo que no alcanzó el umbral?
8. ¿El piloto se cerró con acta de recibo? ¿Dónde está?
9. ¿El despliegue ocurrió? Si ocurrió, ¿por qué el informe dice 69 %?
10. ¿Qué falta del proveedor y cuánto toma?

## Para comprometer una fecha falta
- La disponibilidad real del equipo.
- La fecha del proveedor, y si llega con el equipo completo para la siguiente fase. Eso se comentó hoy y nadie lo anotó como riesgo.
- La ventana de producción y de temporada.
- Una línea base vigente aprobada por el patrocinador y el comité.

## Después
Cuando el plan se apruebe, se registra como siguiente versión de la línea base, sin borrar la v1. Los supuestos pasan al RAID con doliente. Hoy el RAID ya tiene tres riesgos sin doliente.

---
Corrida registrada como `2026-10-17-pm-plan-1` (46 s, un proyecto). Este texto está guardado en `estado/PRY-200-tienda-en-línea/corridas/salida-pm-plan.md`, que es la evidencia de la corrida. El registro también contó 21 señales abiertas, entre ellas 9 compromisos vencidos y 5 hitos «cumplidos» sin evidencia. No las traté aquí.