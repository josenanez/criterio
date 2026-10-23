# /criterio-product:product-business-case 

El borrador del caso de negocio de PRD-301 (Puntos de fidelización) está hecho, pero todavía no es un caso evaluable. No hay ningún costo en los documentos y el retorno esperado no tiene cifra. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré otra vez.

- **Qué se construye:** 12 de los 17 requerimientos están aceptados y entran al caso; los otros 5 están propuestos y quedan fuera. Ninguno tiene proyecto que lo ejecute.
- **Demanda:** la única evidencia es una entrevista del 2025-08-29 («Lo necesito y hoy no lo tengo»). No nombra ningún requerimiento ni dice que el cliente sea del segmento Jóvenes.
- **Dos cifras con fuente:** el volumen mensual declarado es 297.074 (caso de negocio, 2025-12-18). El medido es 310.136 (tablero, corte 2026-10-11). La diferencia es de 4,4 %, por debajo del umbral de 20 %, y va dentro del caso igualmente. La serie medida tiene un solo punto.
- **Un supuesto sin verificar:** «Las tiendas soportan el volumen», declarado el 2026-06-26 y sin verificar desde hace 119 días (el umbral es 30).
- **Vacíos principales:** no están los costos, el valor del retorno («en 24 meses» no es una cifra), qué mide el «volumen mensual», las alternativas, el criterio de éxito con su fecha de corte ni el proyecto que construye el producto.
- **Cruce con otros productos:** no se hizo, porque no hay fichas publicadas (la carpeta `estado/records` no existe).

No calculé retorno ni recomendé aprobar o rechazar.

La corrida quedó registrada como `2026-10-23-product-business-case-1`: 37 segundos, 17 requerimientos y 40 hallazgos.

El documento está en `estado-producto/PRD-301/corridas/salida-product-business-case.md`. Puedo pasar los 3 supuestos a seguimiento con assumption-tracking; si el caso se aprueba, el siguiente paso es `/criterio-product:product-charter`.