# /criterio-project:pm-plan 

# Plan — PRY-206 Precios dinámicos · borrador del 2026-10-16

Este borrador no compromete ninguna fecha ni propone ninguna duración. Los términos ya estaban vigentes (v0.3.12, aceptados por José Francisco Ñáñez el 2026-10-16).

**Desde:** el acta del 2025-11-15. **Criterio de éxito:** «Precios dinámicos en producción y medido». Está declarado, pero sin métrica, sin umbral y sin fecha de medición.

**Dos avisos antes de leerlo:**
- Ya existe un plan: `10-plan/2025-11-15-cronograma-v1.csv`, con cinco hitos con fecha. No lo tomé como base. Para revisarlo serviría `/pm-plan revisar`.
- El cierre del acta (2026-08-31) ya pasó frente a hoy.

## Lo que le falta al acta
| Qué | Consecuencia de planificar sin eso |
|---|---|
| Alcance sin contenido («Componente 1, 2, 3») | No hay entregables que descomponer, y no los inventé. |
| Fuera de alcance vacío («Lo que otro proyecto cubre») | No se sabe dónde termina el proyecto ni qué le toca a otro. |
| Criterio de éxito sin métrica | El entregable «medido» no se puede aceptar. |
| Objetivo del negocio genérico | No dice qué resultado se busca ni dónde. |
| Autoridad del gerente no declarada | No se sabe qué decide quien planifica y qué se sube. |
| Dependencias: «Ninguna declarada» | El proyecto tiene un contrato con proveedor (CT-914) y una integración con el ERP. |
| Producto asociado: «No aplica» | No hay quién reciba u opere el resultado. |

Sí están el patrocinador (Beatriz Cuéllar), la gerente (Diana Molina), el comité, el presupuesto y las fechas de inicio y cierre.

## WBS
Son 13 nodos, ninguno con duración.
- **Nodos 1 a 5:** los tres componentes, «en producción» y «medido». El nombre es del acta, el contenido está sin definir y nadie los acepta todavía.
- **Nodos 6 a 8:** los tres entregables de CT-914. Son supuesto, porque el acta no los nombra. Los acepta la gerente con el acta de recibo, según el contrato.
- **Nodos 9 a 13:** los cinco hitos del cronograma v1. También son supuesto.

## Orden
Todo el orden es supuesto, porque el acta no declara dependencias.
- Producción requiere piloto y despliegue, y la medición requiere producción.
- El ambiente de pruebas va antes de la integración con el ERP y del piloto.
- El licenciamiento va antes de la configuración del catálogo.
- Los componentes 1 a 3 no se pueden ordenar.

## Supuestos
- Los tres entregables de CT-914 son del proyecto.
- Los cinco hitos del cronograma v1 siguen vigentes.
- El orden de dependencias es el que escribí.
- «Producción» significa la cadena completa.
- Los componentes 1 a 3 no coinciden con los de CT-914 ni con los hitos.

## Sin definir
- Qué son los componentes.
- Qué proyecto cubre lo «fuera de alcance».
- Qué se mide y cuándo.
- Quién acepta cada entregable de negocio.
- La autoridad de la gerente.
- Las dependencias externas.
- Quién opera el resultado.
- La «siguiente fase» que mencionan las notas de hoy, que no está en el acta.

## Proyectos análogos
Ninguno a la vista. La configuración no apunta a una carpeta de fichas de la PMO, y no lo invento.

## Preguntas para el equipo
Hay ocho, una por cada duración vacía. La lista completa está en el archivo de salida.

## Para comprometer una fecha falta
- La disponibilidad real del equipo. Las notas de hoy dicen que el proveedor podría no llegar con el equipo completo y nadie lo registró como riesgo.
- La fecha del proveedor para lo que sigue.
- La ventana de despliegue en producción y en tiendas.
- Una decisión sobre el cierre vencido. Eso es control de cambios, no este plan.

Si el plan se aprueba, puede registrarse como línea base original y pasar los supuestos al RAID con doliente. No lo hice, porque lo decide quien lo apruebe.

## Registro de la corrida
La salida completa quedó en `estado/PRY-206-precios-dinámicos/corridas/salida-pm-plan.md` y la corrida en `2026-10-16-pm-plan-1`. Tardó 55 segundos.

El registro anotó 19 señales abiertas del proyecto: 5 compromisos vencidos, 5 sin fecha y 3 reprogramados; 4 hitos cumplidos sin evidencia; y una diferencia entre lo declarado y la evidencia y una de avance contra plan. Este comando no las produjo ni las analizó.