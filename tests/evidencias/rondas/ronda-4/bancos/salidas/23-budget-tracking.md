# /criterio-portfolio:budget-tracking portafolio

El informe de presupuesto del portafolio (13 proyectos, todos en COP) está hecho y la corrida quedó registrada como `2026-10-15-budget-tracking-1`. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez, así que no hizo falta registrarlos de nuevo.

Las cifras de los 13 proyectos salen del informe de avance de cada uno. Es una declaración del gerente y no hay ningún soporte contable en la carpeta. Calculé todo con `portafolio.py compute` y no sumé nada a mano, así que el informe no trae totales del portafolio.

- **Ejecutado mayor que comprometido:** PRY-210 (59,5% contra 36,1%) y PRY-211 (39,2% contra 33,2%). Eso no cuadra, y su «disponible real» no es confiable hasta aclararlo.
- **Proyección sobre el aprobado:** seis proyectos, PRY-201, 203, 206, 207, 209 y 210, entre +0,3% y +4,2%. Ninguno llega al umbral de 10%.
- **Comprometido cerca del tope:** PRY-207 (89,2%) y PRY-208 (86,9%), sin cruzar el umbral de 90%. En PRY-207 el ejecutado es solo 32,3%, pero el disponible real es 735.237.184 de 6.800.000.000.
- **Proyección desactualizada:** la de PRY-204 y la de PRY-205 son anteriores a su solicitud de cambio, con costo adicional declarado de 166.000.000 y 156.000.000.
- **Cambios sin acta:** cinco cambios aprobados con costo (PRY-201, 202, 204, 205, 207) dicen «autorizada por el comité», pero no hay acta que lo respalde. Ninguno movió el presupuesto aprobado de la ficha.
- **Ejecución contra avance:** PRY-200 tiene el gasto por delante del avance (53,1% ejecutado, 34% de avance declarado). PRY-206 va al revés (31,3% ejecutado, 89% de avance declarado).
- **Sin dato:** no hay línea base de costo (presupuesto original y vigente) en ninguna ficha, solo de cronograma. La desviación del presupuesto contra la línea base es `not_found`.

Ofrecí preparar la solicitud de cambio de presupuesto para los seis proyectos con proyección sobre el aprobado, empezando por PRY-203. También ofrecí el detalle por proveedor para PRY-207 y PRY-208, cuyos proveedores aún no revisé.

El informe completo está en `estado/corridas/salida-budget-tracking.md`.