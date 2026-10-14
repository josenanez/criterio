# /criterio-product:product-definition 

Terminé la definición de PRD-303 «Gemelo digital» y dejé la corrida registrada, pero el cálculo no sirvió. `producto.py compute` corrió con `estado/producto.json` vacío, así que no entregó `claim_vs_metric` y registró 0 hallazgos. Todo lo de abajo sale de leer los documentos a mano, y la diferencia del volumen la calculé yo.

Los términos ya estaban aceptados (versión 1.0, 2026-10-14, José Francisco Ñáñez). No hubo preguntas que contestar.

- **Afirmaciones:** la definición es de una línea, del 2025-12-09. Tiene 5 afirmaciones; la propuesta principal está en blanco.
- **Contradicciones:** ninguna de frente. Hay un cruce sin confirmar: el acta de PRY-207 dice «Producto asociado: gemelo digital», con área dueña Geología y 9.500.000.000 COP. La definición dice «Ninguno declarado» y habla del segmento Gerencia. Queda para `/product-trace`.
- **Cifras:** el caso de negocio declara volumen_mensual 198.346 y el tablero mide 179.966 al 2026-10-12. Son −9,3 %, bajo el umbral de 20 %, y ningún documento dice la unidad. El «retorno en 24 meses» no tiene serie.
- **Demanda:** hay una sola entrevista, de un cliente sin nombre (2026-08-31), y es evidencia débil. Cuatro requerimientos se le atribuyen, y tres de ellos tienen fecha anterior a esa entrevista.
- **Supuesto de la red:** figura como «verificado», pero sin documento ni responsable. Lleva 125 días declarado.
- **Lo que falta para cerrar:** el criterio de éxito, la propuesta, el tamaño del problema, para quién (solo dice «Gerencia») y quién decide. Sin criterio de éxito no se puede cerrar, así que no ofrezco `/product-charter`.
- **Normativo:** la definición no toca datos personales ni pagos, pero eso no equivale a cumplimiento. No tengo la norma a la vista y debe ir a revisión jurídica.

La salida completa está en `estado/corridas/salida-product-definition.md`. La corrida quedó como `2026-10-14-product-definition-1`.