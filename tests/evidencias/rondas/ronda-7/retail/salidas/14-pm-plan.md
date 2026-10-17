# /criterio-project:pm-plan 

# Plan — PRY-211 · Pronóstico de demanda · borrador del 2026-10-17

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo. El proyecto lleva meses en ejecución y ya existe un cronograma v1. Este borrador reconstruye la estructura desde el acta y los contratos. No crea línea base ni compromete ninguna fecha.

## Lo que le falta al acta
- **Alcance sin describir:** dice «Componente 1, 2 y 3». La WBS solo se sostiene en los contratos y en los hitos del cronograma.
- **Criterio de éxito sin medida:** «en producción y medido» no dice qué se mide ni con qué umbral. Nadie puede aceptar el cierre.
- **Autoridad del gerente no declarada.**
- **Exclusión vacía:** «lo que otro proyecto cubre», sin decir cuál.
- **Dependencias «Ninguna declarada».** Las notas de hoy mencionan que el proveedor podría no llegar con el equipo completo.
- **Presupuesto sin desglose:** quedan 2.250.416.534 COP de los 6.800.000.000 aprobados sin destino documentado. Los dos contratos suman 4.549.583.466 COP.
- **Producto asociado «No aplica»:** nadie queda a cargo del pronóstico una vez en producción.

Sí están el patrocinador (Jorge Medina), el gerente (Andrés Lozano), el comité, las fechas de inicio y cierre, y el presupuesto aprobado.

## WBS
Tiene 13 nodos, y todas las duraciones quedaron vacías.
- **Hitos 1–5 (cronograma v1):** diseño, ambiente de pruebas, integración con el ERP, piloto y despliegue. Quién los acepta está sin definir.
- **Entregables 6–11 (contratos CT-842 y CT-565):** los acepta Andrés Lozano, porque la condición de pago es acta de recibo firmada por el gerente.
- **Nodo 12:** los Componentes 1–3, sin definir.
- **Nodo 13:** «en producción y medido», sin definir.

## Orden
- Licenciamiento, luego catálogo, luego piloto, luego despliegue, luego «medido».
- Soporte del primer trimestre después del despliegue.
- Casi todo este orden es supuesto: ningún documento lo dice.
- Los Componentes 1–3 no se pueden ordenar.

## Supuestos y sin definir
- **Cinco supuestos declarados.** Entre ellos: que los hitos del cronograma v1 son todos los entregables, que los componentes del acta equivalen a ellos, y que los dos contratos no se solapan.
- **Ocho cosas sin definir,** cada una con quién la define.

## Proyectos análogos
No hay ninguno a la vista. La configuración no apunta a una carpeta de fichas de la PMO, así que no hay referencia ni estimación.

## Preguntas para el equipo
Hay nueve, una por cada duración vacía. Una de ellas: el informe del 2026-10-14 dice que se reprogramó el despliegue, pero el cronograma v1 sigue en 2026-11-30.

## Para comprometer una fecha falta
- La disponibilidad real del equipo.
- La fecha confirmada de cada proveedor.
- Las fechas de la ventana de congelamiento de fin de año.
- La decisión sobre qué son los tres componentes.

**Fuera de este plan:** CT-842 lleva facturados 1.197.938.594 COP con un solo entregable con acta de recibo. CT-565 lleva 723.840.453 COP facturados sin acta de recibo. Eso corresponde a `vendor-control`.

La corrida quedó registrada como `2026-10-17-pm-plan-1`. El texto completo está en `estado/PRY-211-pronóstico-de-demanda/corridas/salida-pm-plan.md`.