# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-304 (Tarjeta de crédito digital) y registré la corrida. El documento deja dos cifras con fuente y diez vacíos, y el primer vacío es el costo de construir. Sin costo, lo que hay es una propuesta, no un caso evaluable.

Los términos ya estaban vigentes y aceptados (v1.1, 2026-10-18, José Francisco Ñáñez), así que no los registré de nuevo.

**Cifras con fuente**
- **Declarada:** el volumen mensual es 263.889 (caso de negocio, 2026-01-21).
- **Medida:** el volumen mensual es 272.644 (tablero de métricas, corte 2026-10-15).
- **Contraste:** la diferencia es +3,3 %, bajo el umbral de 20 %. La serie tiene un solo punto. Ni el caso ni el tablero definen qué mide `volumen_mensual`, así que la cercanía no confirma nada.

**Supuesto central:** «la demanda se sostiene sin campaña» figura como verificado, pero el documento del proveedor en que se apoya no está en la carpeta. El anexo solo dice «se confirmó». Lo dejé como supuesto, no como cifra declarada.

**Vacíos nombrados**
- **Costo y retorno:** no hay costo de construir, y el «retorno esperado en 24 meses» no trae cifra.
- **Éxito y decisión:** no hay criterio de éxito, así que el documento dice que sin él no se podrá cerrar el producto. Tampoco hay una persona que decida: solo aparece el comité.
- **Alcance:** no se declara el país ni qué mide `volumen_mensual`.
- **Alternativas:** no se dice qué se consideró ni qué pasa si no se hace.
- **Trazabilidad:** 0 de 17 requerimientos aceptados tienen proyecto, y 5 se aceptaron sin cita de quien los pidió.

No hay otros productos publicados, así que no hubo cruce de cifras. No ofrecí `/product-charter` porque faltan criterio de éxito, decisor y costo. Sí queda sugerido pasar el supuesto «sin campaña» a assumption-tracking.

La corrida quedó registrada con id `2026-10-18-product-business-case-1`.

Archivos en `estado-producto/PRD-304/corridas/`:
- `salida-product-business-case.md`