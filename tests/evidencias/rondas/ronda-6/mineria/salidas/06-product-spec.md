# /criterio-product:product-spec 

Escribí el borrador de especificación de PRD-301 (Alerta de taludes), pero no tiene secciones de comportamiento. Los 13 requerimientos aceptados no tienen escrito el problema que resuelven, y el registro no permite inventarlo. Quien debe cerrarlo es Mauricio Pérez, gerente de producto.

Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-16). No hubo preguntas que responder.

- **Alcance:** entran los 13 aceptados, solo por su identificador. REQ-4111 queda fuera porque está propuesto desde hace 167 días y nadie lo ha decidido.
- **Criterios de aceptación:**
  - 12 de los 13 dicen «se verifica en producción», que es un lugar y no un criterio medible.
  - REQ-4105 no tiene ninguno.
  - No propuse umbrales, porque ningún documento los da.
- **Supuestos:**
  - «El proveedor cumple el tiempo pactado» lleva 54 días sin verificar.
  - La evidencia de demanda es una entrevista de hace 12 meses que no nombra ningún requerimiento.
  - La cifra del caso de negocio (169.380) está 37,4 % por encima de la medida (106.047).
- **Vacíos:** son 12, cada uno con quien lo cierra. Incluyen:
  - los casos borde, que ningún documento menciona;
  - el criterio de éxito, que no existe;
  - los 5 requerimientos sin doliente;
  - que el acta no dice quién decidió cada aceptación;
  - el proveedor, que nadie ha acordado;
  - las obligaciones normativas, que quedan por confirmar.
- **Lo que no cubre:** los 13 aceptados entran solo nominalmente, y la tabla da el motivo de cada uno. Seis no tienen ninguna cita de quien los pidió.
- **Siguiente paso:** `/product-charter` todavía no aplica. Primero hay que escribir el problema y el criterio de los más antiguos (REQ-4109, 4103, 4106) y asignar dolientes. `/product-trace` sí aplica, porque ninguno de los 13 tiene proyecto.

La corrida quedó registrada como `2026-10-16-product-spec-1`: 58 s, 14 requerimientos, 35 hallazgos.

Archivos en `estado-producto/PRD-301/corridas/`:
- `salida-product-spec.md`