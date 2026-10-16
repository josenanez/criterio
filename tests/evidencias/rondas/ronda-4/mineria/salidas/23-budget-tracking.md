# /criterio-portfolio:budget-tracking PRY-202

**PRY-202, planta de tratamiento de agua: la proyección al cierre pasa del presupuesto aprobado en 20,3 %, el doble del umbral de 10 %. Aun así el informe de avance del 2026-10-06 la declara en verde.**

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que volver a registrarlos.

El informe sale de dos documentos: el acta de constitución (2026-02-22) y el informe de avance (2026-10-06). Los cálculos son del script al 2026-10-15.

| Cifra (COP) | Monto | % del aprobado |
|---|---|---|
| Aprobado | 9.500.000.000 | 100 |
| Comprometido | 3.612.108.532 | 38,0 |
| Ejecutado | 1.634.387.317 | 17,2 |
| Proyección al cierre | 11.432.506.949 | 20,3 sobre el aprobado |
| Disponible real (aprobado menos comprometido) | 5.887.891.468 | |

- **Estado verde sin respaldo:** esa declaración no explica el sobrecosto. La ficha no tiene ninguna fuente de evidencia, solo dos declaraciones.
- **Comprometido:** va en 38,0 %, muy por debajo del umbral de 90 %, así que no hay alerta de agotamiento.
- **Línea base de presupuesto:** no hay replanificaciones ni solicitudes de cambio. El presupuesto original y el vigente son el mismo.
- **Ejecución frente a avance:** va 17,2 % ejecutado contra 25 % de avance declarado. Puede ser trabajo hecho y no facturado, pero ningún documento lo confirma.
- **Incidencia abierta:** el equipo perdió dos semanas por la rotación de un ingeniero clave. El informe no dice si eso entra en la proyección.

**Sin dato:**
- Hitos del plan: no hay ninguno registrado, así que no se pudo medir el avance por hitos.
- Proveedores y contratos.
- La causa del sobrecosto proyectado.
- Producto, autoridad y fase del proyecto.

Dejé escrita la salida completa y la corrida registrada como `2026-10-15-budget-tracking-1`. Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/change-control`, pero no la inicié.

Archivos en `/home/claude/banco/ronda-4/mineria/espacio/estado/corridas/`:
- `salida-budget-tracking.md`