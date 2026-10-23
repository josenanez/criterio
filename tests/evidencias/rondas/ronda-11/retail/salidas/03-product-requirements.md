# /criterio-product:product-requirements 

Terminé la corrida de `/product-requirements` para PRD-301, Puntos de fidelización, al 2026-10-23. Tiene 17 requerimientos, de los que 12 están decididos y 5 siguen propuestos. Encontró 40 hallazgos.

Los términos v1.2 ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-23), así que no registré nada nuevo.

**Los vacíos, en el orden de lectura del comando:**
- **Aceptados sin que nadie los pidiera:** REQ-2030 y REQ-4115 no tienen ninguna cita de quien los pidió.
- **Aceptados que nadie construye:** los 12 aceptados no tienen proyecto que los ejecute. La carpeta `estado/records` no existe, así que el 0% con proyecto sale de ahí y del acta del comité.
- **Sin doliente:** REQ-4103 y REQ-4105 aparecen «sin asignar».
- **Sin criterio de aceptación:** REQ-4101, 4103, 4106, 4109 y 4110, todos ya aceptados.
- **Decididos sin quién decidió:** los 12 aceptados no registran decisor. Esto lo comprobé yo contra los archivos de cada requerimiento, no con el cálculo. El acta del 2026-10-20 solo dice «Se mantiene el plan».
- **Sin decidir hace más de 60 días:** REQ-4104 (186 días), REQ-4108 (117), REQ-4105 (113) y REQ-4113 (75). Quien tiene la facultad de decidirlos es el Comité de producto.
- **Evidencia vieja:** 14 requerimientos se apoyan solo en la entrevista del 2025-08-29, de hace 13 meses, que no nombra ninguno de ellos.

**Fuera del registro, tres datos más:**
- El supuesto «Las tiendas soportan el volumen» lleva 119 días sin verificar.
- La definición del producto no tiene criterio de éxito.
- El volumen mensual declarado (297.074) y el medido (310.136) difieren 4,4%, por debajo del umbral de 20%.

**Siguiente paso posible:** `/product-trace` para los 12 decididos que nadie construye.

**Archivos:**
- Lo que te mostré quedó en `estado-producto/PRD-301/corridas/salida-product-requirements.md`.
- La corrida quedó registrada como `2026-10-23-product-requirements-1`.