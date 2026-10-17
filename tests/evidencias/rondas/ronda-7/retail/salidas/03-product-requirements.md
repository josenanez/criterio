# /criterio-product:product-requirements 

La corrida de `/product-requirements` quedó registrada como `2026-10-17-product-requirements-1`. El registro de la Tarjeta de la tienda (PRD-309) tiene muchos vacíos, y ninguno de los 9 requerimientos aceptados tiene un proyecto que lo construya.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo. Pasé `compute` sin `--fichas` porque no hay fichas de proyecto en el espacio.

## Registro — Tarjeta de la tienda (PRD-309) · al 2026-10-17
13 requerimientos · 9 decididos · 55.6% con evidencia · 0% con proyecto que lo ejecuta

**Se va a construir y nadie lo pidió**

| REQ | Estado | Doliente |
|---|---|---|
| REQ-2026 | aceptado | Sandra Gil |
| REQ-4903 | aceptado | María Restrepo |
| REQ-4904 | aceptado | Jorge Medina |
| REQ-4907 | aceptado | (sin doliente) |

**Decidido y nadie lo está construyendo**
- Son los 9 aceptados: REQ-2026, 4900, 4901, 4903, 4904, 4905, 4906, 4907 y 4911.
- El más antiguo es REQ-4903, decidido el 2026-04-14.

**Sin doliente**
- REQ-4907 (aceptado) y REQ-4910 (propuesto).
- Diana Molina, como gerente de producto, asigna el doliente.

**Sin criterio de aceptación**
- REQ-4907 y REQ-4911, ambos aceptados. REQ-4909 tampoco lo tiene, pero está propuesto y no se le exige.
- Lo cierra el doliente. REQ-4907 necesita doliente antes.

**Decidido sin documento que lo respalde:** ninguno. Los 9 decididos citan un documento en `30-decisiones`.

**Lleva meses y nadie lo decide**

| REQ | Propuesto hace | Quién decide |
|---|---|---|
| REQ-4909 | 172 días | Comité de producto |
| REQ-4910 | 153 días | Comité de producto |
| REQ-4908 | 80 días | Comité de producto |
| REQ-4902 | 75 días | Comité de producto |

Se propone llevarlos al comité para decidir, sin cerrarlos por viejos.

**Evidencia vieja**
- Nueve requerimientos se sostienen solo en la entrevista del 2025-08-24, de hace 13 meses: REQ-4900, 4901, 4902, 4905, 4906, 4908, 4909, 4910 y 4911.

**Por estado**

| propuesto | aceptado | en construcción | entregado | descartado |
|---|---|---|---|---|
| 4 | 9 | 0 | 0 | 0 |

**Alertas de la definición**
- El caso de negocio declara un volumen mensual de 272.424 y el tablero mide 208.658, un 23.4% menos.
- El supuesto «El proveedor cumple el tiempo pactado» lleva 70 días sin verificarse.

**Siguiente paso:** `/product-trace` para los 9 aceptados sin proyecto. No ofrezco `/product-charter`: ninguno tiene a la vez evidencia, criterio y doliente. REQ-4900, 4901, 4905 y 4906 tienen los tres, pero su evidencia es de hace 13 meses.

La salida completa está en `estado-producto/PRD-309/corridas/salida-product-requirements.md`.