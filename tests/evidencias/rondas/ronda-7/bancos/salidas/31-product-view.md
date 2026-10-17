# /criterio-portfolio:product-view APIs de datos

## Productos al 2026-10-17

Sale de `portafolio.py compute` de hoy sobre las fichas del estado. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| APIs de datos | 1 (PRY-203 Open Banking) | 0 | 2027-02-27 | COP 18.000.000.000 | COP 13.830.604.592 |

«APIs de datos» tiene un solo proyecto. La vista por producto no aporta nada ahí, así que no armé sección de grupo ni cruce de dependencias internas. Lo que sigue es la ficha de PRY-203 tal como la calcula el script.

- **Señales:** no hay ninguna abierta. Lleva 8 días sin movimiento y el umbral es 15.
- **Fecha:** 2027-02-27, sin replanificaciones y con 0 días de desviación.
- **Dinero:** las cuatro cifras vienen completas.
  - Comprometido: 76,8 % (el umbral es 90 %).
  - Ejecutado: COP 5.088.404.663, es decir 28,3 %.
  - Proyección: COP 18.145.395.715, 0,8 % sobre lo aprobado.
  - Disponible real: COP 4.169.395.408.
- **Declarado por el gerente:** amarillo y 30 % de avance, al 2026-10-09.

### Lo que no sé
- **Sustento documental débil:** de los 13 datos de la ficha, 0 salen de evidencia, 3 de declaración y 10 no están marcados. Que no haya alertas no significa que la evidencia lo confirme.
- **Sin cruce de avance contra plan:** el cálculo no lo entrega para este proyecto y no lo estimo.
- **Campos sin declarar:** quién aprueba el proyecto y en qué fase está. Ninguno de los 13 proyectos del portafolio tiene autoridad declarada.
- **Sin proveedores:** la ficha no trae ninguno, así que no hay nada que contrastar contra lo facturado.

### Proyectos sin producto declarado
Hay 4 de los 13 proyectos sin producto. Ninguno es parte de «APIs de datos», pero nadie puede responder por el conjunto al que sirven.

| Proyecto | Área dueña |
|---|---|
| PRY-202 Migración a la nube | no está en el cálculo |
| PRY-205 Prevención de lavado de activos | no está en el cálculo |
| PRY-208 Motor de decisión | no está en el cálculo |
| PRY-210 Portal de proveedores | no está en el cálculo |

El área dueña no sale de `compute`, así que no la escribí. Hay que leerla de la ficha de cada proyecto.

### Pie de rigor
- Cada cifra está copiada de la salida del cálculo de hoy. No leí documentos nuevos.
- Lo que hay que verificar: que el amarillo del 2026-10-09 siga vigente y quién es la autoridad de PRY-203.
- La corrida quedó registrada como `2026-10-17-product-view-1` (29 segundos, 13 proyectos). Su salida quedó en `estado/corridas/salida-product-view.md`.