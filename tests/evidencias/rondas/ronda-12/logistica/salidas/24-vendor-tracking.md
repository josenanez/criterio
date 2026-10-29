# /criterio-portfolio:vendor-tracking PRY-207

No pude cruzar contrato, entrega y factura de PRY-207, porque la carpeta del proyecto no tiene ningún contrato de proveedor. Sin el contrato, una lista de entregables sería solo supuestos, así que no la armé.

**Qué hay sobre proveedores.** En el acta de constitución, el cronograma v1 y el informe de avance del 2026-10-06, solo una línea. Es un riesgo abierto del informe: "El proveedor no ha confirmado la fecha de la última entrega". No nombra al proveedor, el contrato ni el entregable. El script confirma que la ficha no tiene proveedores registrados.

**Una contradicción documentada.** El acta declara "ninguna dependencia", pero el informe reporta un riesgo por una entrega pendiente de un proveedor.

**El contexto que calculó el script.**
- **Estado declarado:** el informe lo reporta en verde, con avance de 24 %.
- **Señales que lo contradicen:**
  - Lleva 22 días sin documentos nuevos.
  - El plan sustenta 100 % frente al 24 % declarado, una brecha de 76,0 puntos.
  - Los 3 hitos aparecen como cumplidos sin evidencia. Son hitos del proyecto, no entregables de proveedor, y no puedo atribuirlos a ninguno.
- **Fecha de cierre:** la fecha comprometida era el 2026-08-21 y ya pasó.
- **Presupuesto (COP):**
  - Aprobado: 9.500.000.000.
  - Comprometido: 6.597.325.946 (69,4 %).
  - Ejecutado: 3.638.979.753 (38,3 %).
  - Proyección al cierre: 9.899.993.006 (4,2 % sobre lo aprobado).

**Lo que no sé.**
- Contrato, vigencia, renovación automática y preaviso. No puedo decir si algún preaviso está por vencer.
- Facturas y actas de recibo o aceptación.
- Compromisos del proveedor: no hay minutas con él.

**Qué sugiero.**
1. Pedir a Jorge Medina, el gerente, el contrato, sus anexos y el acta de recibo de lo ya entregado.
2. Pedirle también la fecha de la "última entrega" y la factura emitida contra ella.
3. Repetir `/vendor-tracking PRY-207` cuando el contrato esté en `00-gobierno`.

Esto es un borrador de trabajo: lo anterior sale solo de los tres documentos citados y del cálculo del script, y la verificación contra los originales es suya.

La corrida quedó registrada como `2026-10-28-vendor-tracking-1` y duró 30 segundos. El texto completo está en `estado/corridas/salida-vendor-tracking.md`.