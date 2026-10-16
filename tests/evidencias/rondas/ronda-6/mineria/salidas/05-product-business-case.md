# /criterio-product:product-business-case 

Armé el caso de negocio de Alerta de taludes (PRD-301) y registré la corrida; el costo de construir no está en ningún documento, así que es el primer vacío y sin él hay una propuesta, no un caso. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

- **Cifra con fuente:** el volumen mensual declarado es 169.380 (caso de negocio, 2026-06-01) y el medido es 106.047 (tablero, corte 2026-10-08). La declarada queda 37,4 % por encima (umbral 20 %). La serie medida tiene un solo punto, así que no se sabe si el volumen bajó o nunca llegó. El comité del 2026-10-12 decidió «Se mantiene el plan» sin tratar la diferencia.
- **Retorno:** el caso dice «retorno esperado en 24 meses» sin monto ni base. No lo traté como cifra.
- **Qué se construye:** la definición no dice qué se propone, solo trae «Propuesta principal». De los 13 requerimientos aceptados, 7 tienen cita de quien los pidió; los otros 6 quedan fuera de la tabla. Ninguno tiene proyecto.
- **Costo candidato sin confirmar:** el acta de PRY-204 «Monitoreo de taludes» dice «Producto asociado: alerta de taludes» y tiene 3.300.000.000 COP aprobados. El área dueña es Seguridad y Salud, no Mantenimiento, y la definición de PRD-301 dice «Ninguno declarado». El vínculo es solo por nombre. Lo dejé como candidato a confirmar con `/product-trace`.
- **Supuestos y vacíos:** el supuesto del proveedor lleva 54 días sin verificar (umbral 30). Tampoco hay criterio de éxito, ni alternativas, ni qué pasa si no se hace, ni quién decide (se tomó al comité que emite el acta, sin confirmar).
- **Otros productos:** ninguno de los demás productos publicados afirma la misma cifra ni menciona taludes, así que no veo doble conteo.

Las cifras son las que ya traían los documentos; no proyecté ingresos ni retorno ni recomendé aprobar o rechazar. Ofrezco pasar los supuestos a `assumption-tracking`. `/product-charter` aún no aplica porque faltan costo, propuesta y criterio de éxito.

La corrida quedó registrada (35 hallazgos, 36 segundos).

Archivos en `/home/claude/banco/ronda-6/mineria/espacio/estado-producto/PRD-301/corridas/`:
- `salida-product-business-case.md`
- `2026-10-16-product-business-case-1.md`