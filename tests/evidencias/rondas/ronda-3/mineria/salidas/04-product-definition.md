# /criterio-product:product-definition 

## Definición — Almacén de repuestos (PRD-306) · contrastada al 2026-10-15

La definición está sostenida de forma débil, contradicha en una cifra y sin criterio de éxito. Los términos ya estaban aceptados por José Francisco Ñáñez el 2026-10-15, así que no hubo que registrarlos de nuevo.

- **La evidencia contradice una cifra.** El caso de negocio (2026-05-06) declara un volumen mensual de 249.273 y el tablero (corte 2026-10-12) mide 153.324. El declarado queda 38,5 % por encima, con un umbral de 20 %. La serie tiene un solo punto y ningún documento define qué mide «volumen», así que nadie ha confirmado que ambos midan lo mismo.
- **Una cifra nadie la mide.** «Retorno esperado en 24 meses» no trae cifra ni cálculo.
- **El problema lo sostiene una sola entrevista, ya envejecida.** Es del 2025-10-14, de un cliente sin nombre: «Lo necesito y hoy no lo tengo». Es evidencia débil porque nadie pagó ni se comprometió, y ya cumple los 12 meses del umbral. Los 9 requerimientos con evidencia se apoyan en esa misma entrevista, así que son una sola fuente.
- **Hay un supuesto sin verificar.** «El proveedor cumple el tiempo pactado» lleva 205 días sin verificar (umbral 30). Ningún documento nombra al proveedor ni el plazo, y tal como está escrito es difícil de desmentir. Verificarlo exigiría nombrarlos y contrastar entregas reales contra el plazo.
- **Hay cosas que no están dichas en ninguna parte:**
  - el criterio de éxito;
  - la propuesta de valor: la sección solo dice «Propuesta principal»;
  - que sea el segmento Gerencia quien tiene el problema: la entrevista no menciona segmento;
  - qué mide «volumen» y cómo se calculó 249.273;
  - qué proyecto construye el producto: «Ninguno declarado»;
  - quién decide: «Comité de producto» es solo una propuesta por defecto.
- **No identifiqué obligaciones normativas.** La definición no roza datos personales ni pagos y la configuración no declara país. Eso no es un cumplimiento; no tengo la norma a la vista, y la revisión jurídica queda pendiente.
- **Para cerrar la definición faltan dos cosas.** El criterio de éxito y quién decide. El problema y el segmento sí están declarados.
- **Discrepancia entre el cálculo y la ficha.** `compute` devuelve `unknown` vacío, pero la ficha marca el criterio de éxito como `not_found`. Tomé la ficha, que coincide con el documento.
- **Siguiente paso.** El supuesto del proveedor puede convertirse en riesgo con doliente. `/product-charter` no corresponde todavía porque la definición no está cerrada.

La corrida quedó registrada como `2026-10-15-product-definition-1`, con 31 hallazgos y 30 segundos. Los hallazgos son del barrido de requerimientos, no de las afirmaciones de la definición. El resultado completo está en `estado-producto/PRD-306/corridas/salida-product-definition.md`.