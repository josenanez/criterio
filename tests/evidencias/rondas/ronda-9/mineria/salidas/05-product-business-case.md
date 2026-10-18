# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de PRD-300 (Monitoreo de flota), y el hallazgo principal es que no tiene costos en ningún documento. Sin ellos, lo que hay es una propuesta y no un caso que se pueda evaluar.

Los términos ya estaban aceptados por José Francisco Ñáñez el 2026-10-17, así que no registré nada nuevo. No había otros productos publicados en el espacio, por eso no hice el cruce de métricas con otro producto.

**Cifras:**
- **Volumen mensual:** el caso declara 236.725 (2025-12-15) y la bodega de datos mide 201.743 (corte 2026-10-15). La diferencia es de 14,8 %, bajo el umbral de 20 %, y la dejé dentro del caso. La serie tiene un solo punto y nadie define qué cuenta como «volumen», así que no se sabe si las dos cifras miden lo mismo.
- **Retorno:** el caso dice «retorno esperado en 24 meses» sin cifra ni base de cálculo. Lo clasifiqué como supuesto.

**Costos:** no hay ninguno con fuente. El costo de construir es el primer vacío.

**Otros vacíos:**
- No hay criterio de éxito.
- No dice qué pasa si no se hace.
- No lista alternativas consideradas.
- No fija fecha de corte para saber si funcionó.
- La sección «Propuesta principal» de la definición está vacía.

**Alcance:** los 11 requerimientos aceptados. Tres de ellos (REQ-4003, 4004, 4009) no tienen evidencia de que alguien los pidiera. REQ-4009 tampoco tiene criterio de aceptación. En ninguno de los 11 consta quién decidió, y ninguno tiene proyecto que lo construya.

**Supuesto del proveedor:** figura verificado el 2026-07-13, pero con el documento técnico del propio proveedor, que no está en la carpeta.

No produje cifras, no calculé rentabilidad y no recomendé aprobar ni rechazar.

La corrida quedó registrada como `2026-10-17-product-business-case-1`, con el texto completo en `estado-producto/PRD-300/corridas/salida-product-business-case.md`.

Como siguiente paso, los supuestos pueden pasar al seguimiento con assumption-tracking. Si el caso se aprueba, sigue `/criterio-product:product-charter`.