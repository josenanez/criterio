# /criterio-product:product-definition 

La definición de PRD-307 (Remesas familiares) está contrastada. El hallazgo principal es que el volumen mensual declarado queda 30 % por encima del medido, y que el producto no tiene criterio de éxito ni autoridad que decida en ningún documento.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo. La definición se parte en 6 afirmaciones.

- **Contradicciones:** la evidencia no dice nada en contra de la definición. Lo único que no coincide es una cifra.
- **Cifra del negocio contra datos:** `volumen_mensual` se declaró en 108.635 (caso de negocio, 2025-10-02) y el tablero del 2026-10-16 mide 76.086. La diferencia pasa el umbral de 20 %. La serie tiene un solo punto, y el caso de negocio no aclara si 108.635 era una meta o una línea de partida.
- **Lo que no está dicho en ninguna parte:**
  - El criterio de éxito: el caso de negocio solo dice «Retorno esperado en 24 meses», sin cifra.
  - Quién decide: «Comité de producto» es la respuesta sugerida de esta prueba, no un documento.
  - En qué consiste la propuesta, que dice solo «Propuesta principal».
  - Cuántos microcomercios tienen el problema y cuánto pagarían.
  - El país.
  - Qué proyecto lo construye: la definición dice «Ninguno» y los 9 requerimientos aceptados siguen sin proyecto.
- **Evidencia de demanda:** es una sola entrevista de un cliente (2025-10-10), con una frase: «Lo necesito y hoy no lo tengo.» Es 8 días posterior a la definición y tiene 12 meses, justo en el umbral de 12. Es lo que dijo alguien, no lo que alguien pagó.
- **Supuesto «la regulación vigente lo permite»:** figura confirmado. Dos cosas a revisar: aparece «declarado el 2026-08-31» dentro de un documento fechado el 2025-10-02, y el anexo lo confirma con «la medición del piloto» sin decir qué se midió ni qué norma se miró.
- **Normativo:** nombré 7 puntos que toca la definición:
  - Mover dinero y pagos.
  - Remesa entre países.
  - Datos personales.
  - Dato que sale del país si se opera en nube.
  - Prevención de lavado de activos.
  - Consumidor financiero.
  - Trazabilidad.
  
  Todos quedan en «no tengo la norma a la vista» porque ningún documento declara el país, y no cité ninguna norma. Esto no dice si el producto cumple; va a revisión jurídica.
- **Para cerrar la definición faltan:** el criterio de éxito (sin él no se puede cerrar), quién decide, y el tamaño y la evidencia del problema más allá de esa entrevista.

La corrida quedó registrada como `2026-10-17-product-definition-1`, con 36 hallazgos y 41 segundos. El texto completo está en `estado-producto/PRD-307/corridas/salida-product-definition.md`.

No ofrecí convertir supuestos en riesgo con doliente porque no hay supuestos sin verificar. Tampoco ofrecí `/product-charter`, porque la definición no está cerrada.