# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de Tarjeta débito (PRD-303) y registré la corrida. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.

**Lo que dice el caso**
- **Qué se construye:** el registro tiene 12 requerimientos aceptados y 6 propuestos, todos del acta del 2026-10-12. Ninguno tiene proyecto que lo ejecute. La propuesta de la definición dice solo "Propuesta principal".
- **Volumen mensual:** el caso declara 248.461 (2025-12-27) y el tablero mide 202.628 (2026-09-29). La brecha es del 18,4 %, por debajo del umbral de 20 %. La dejé dentro del caso con las dos cifras y las dos fechas, porque es la primera pregunta de un comité.
- **Retorno:** dice "en 24 meses", sin monto ni tasa. No lo completé con ninguna cifra.
- **Supuesto normativo:** "El reglamento vigente lo permite" sigue sin verificar, 43 días después de declarado.

**Lo que falta**
- Los costos están vacíos. Ningún documento trae el costo de construir ni el del equipo, y ese es el primer vacío.
- No hay criterio de éxito ni fecha de corte. La definición no los trae, así que el producto no se podría cerrar meses después.
- La demanda tiene una sola entrevista genérica, que ningún requerimiento cita de forma concreta.
- REQ-4305, 4306 y 4314 no tienen doliente. REQ-4302 y 2030 no tienen criterio de aceptación. REQ-4301 no tiene quién lo pidió.
- No hay productos publicados con los que cruzar métricas, así que no hice ese cruce.
- La definición está fechada el 2025-12-27, pero registra un supuesto "declarado el 2026-09-02". Lo anoté como algo a confirmar.

La corrida quedó como `2026-10-15-product-business-case-1`, con 42 hallazgos entre 18 requerimientos y 31 segundos de duración. El texto completo está en `estado-producto/PRD-303/corridas/salida-product-business-case.md`.

El siguiente paso que propone el comando es pasar los supuestos a seguimiento con assumption-tracking. `/product-charter` no tiene base todavía, porque el caso no está aprobado.