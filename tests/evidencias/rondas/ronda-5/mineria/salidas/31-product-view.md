# /criterio-portfolio:product-view monitoreo de flota

# Producto «monitoreo de flota» al 2026-10-16

**Fuentes:** las fichas de `estado/records` (13 proyectos) y el cálculo de `portafolio.py compute` al 2026-10-16. Los términos estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-16 (v1.1), así que no hubo que registrarlos de nuevo.

«Monitoreo de flota» tiene un solo proyecto, PRY-200 (Mantenimiento predictivo de camiones). La vista por producto no aporta nada con un solo proyecto, así que no armé sección de producto y dejo el estado de ese proyecto.

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| monitoreo de flota | 1 (PRY-200) | 18 señales | 2026-08-08 (ya vencida) | COP 1.200.000.000 | COP 390.173.338 |

Las cuatro cifras de dinero están completas. Ejecutado: 438.812.017. Proyección: 1.175.719.466.

## Lo que hay que ver en PRY-200

- **Avance frente al plan:** declara 54 %, pero los 4 hitos figuran cumplidos y el plan respalda 100 %. La brecha es de 46 puntos.
- **Hitos cumplidos sin evidencia (4):** Ingeniería básica (venció hace 385 días), Ingeniería de detalle (280), Licencia y permisos (174) y Montaje e instalación (69).
- **Compromisos vencidos sin evidencia (6):** Sandra Gil, Liliana Torres, Andrés Lozano, Jorge Medina, Diana Molina y Javier Hoyos, con entre 1 y 12 días de atraso.
- **Compromisos reprogramados (4):** Elena Duarte lo hizo 6 veces, Diana Molina 5, y Óscar Ramírez y Javier Hoyos 3 cada uno.
- **Compromisos sin fecha (2):** Gustavo Neira y Laura Vélez.
- **Fecha de fin del plan sin acuerdo:** el cronograma de la PMO dice 2026-08-08 y el acta del gerente dice 2026-09-30. Las dos son del 2025-06-03, así que ninguna es más nueva. Las dos fechas ya pasaron.
- **Dinero:** lo ejecutado supera lo comprometido, y la ficha no lo explica. Hay que preguntar si faltan compromisos por registrar o si se ejecutó sin comprometer.

**Dependencias internas:** ninguna declarada. Eso no prueba que no existan, solo que ningún documento las menciona.

## Proyectos sin producto declarado

Siete proyectos no entran en ninguna vista por producto. En su acta, el campo de producto dice «No aplica», es decir, lo declaran como ausente.

| Proyecto | Área dueña |
|---|---|
| PRY-201 Ampliación de la relavera | Logística |
| PRY-202 Planta de tratamiento de agua | Mina |
| PRY-205 Sistema de gestión de seguridad | Tecnología |
| PRY-206 Red privada LTE en mina | Tecnología |
| PRY-209 Electrificación de equipos | Mina |
| PRY-210 Programa de relacionamiento comunitario | Medio Ambiente |
| PRY-211 Control de polvo en vías | Seguridad y Salud |

Nadie puede responder por el conjunto al que sirven. Hay que decidir si de verdad no sirven a ningún producto o si el acta se llenó por salir del paso.

**Portafolio, según el cálculo:** 13 proyectos, 11 con alertas y 58 señales. Seis proyectos reportan verde y la evidencia los contradice. Ninguno tiene autoridad de aprobación declarada.

**Rigor:** esto es un borrador de trabajo y la verificación es suya. Solo leí las fichas y el cálculo, no los documentos fuente. Las citas de cada señal están en las fichas.

**Corrida registrada:** `2026-10-16-product-view-1`, con la salida guardada en `estado/corridas/salida-product-view.md`.