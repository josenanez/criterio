# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-303 y registré la corrida. El caso tiene una sola cifra con fuente y le faltan los costos. Los términos ya estaban aceptados en la configuración (v1.0, 2026-10-14), así que no pregunté nada.

- **Cifras:**
  - El volumen mensual declarado es 198.346, del caso de negocio del 2025-12-09.
  - El medido es 179.966, del tablero con corte 2026-10-12.
  - La diferencia es del 9,3 %, por debajo del umbral configurado del 20 %. La dejé dentro del caso con sus dos fuentes y fechas.
- **Retorno:** "Retorno esperado en 24 meses" no trae valor ni base. Lo clasifiqué como supuesto.
- **Costos:** no hay costo de construir en ningún documento. Es el primer vacío, y sin él lo que hay es una propuesta.
- **Éxito:** no hay criterio de éxito ni fecha de corte.
- **Supuesto de la red:** está marcado "verificado" pero sin prueba citada.
- **Requerimientos:** el registro está vacío. El acta del comité del 2026-10-10 lista seis aceptados. Dos (REQ-1032 y REQ-2026) no tienen quién los pidió, y REQ-2026 tampoco tiene criterio de aceptación. Ninguno tiene proyecto que lo construya.
- **Otros productos:** no hay fichas publicadas, así que no pude hacer el cruce formal. Comparé a mano el volumen mensual de los demás casos de negocio y ninguno repite 198.346. Con eso no puedo saber si cuentan las mismas transacciones.

No calculé ni estimé ninguna cifra, ni recomendé aprobar o rechazar.

El script de registro devolvió `producto: "?"` y `requerimientos: 0`, porque `estado/producto.json` está vacío. El código PRD-303 sí quedó en el campo `caso`.

Archivos en `estado/`:
- corridas/salida-product-business-case.md
- corridas/2026-10-14-product-business-case-1.md