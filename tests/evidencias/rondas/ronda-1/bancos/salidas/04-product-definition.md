# /criterio-product:product-definition 

Contrasté la definición de Microseguros (PRD-306, del 2026-01-08) contra la evidencia: no hay nada que la contradiga, pero casi nada la sostiene.

**La contrastación**
- **Contradicciones:** ninguna. No hay serie de métricas, así que `compute` no calculó ninguna diferencia.
- **Evidencia a favor:** una sola entrevista del 2025-08-22 («Lo necesito y hoy no lo tengo»). Tiene 418 días, más que el umbral de 12 meses, y es una opinión de una persona, no un pago.
- **Supuesto del canal:** «El canal actual soporta el volumen» está marcado «verificado» el 2026-08-25, pero no hay evidencia a la vista, así que lo traté como supuesto. Su fecha es posterior a la del documento, y el documento no lo dice.
- **Cifras que nadie mide:** el volumen mensual de 139.663 y el «retorno en 24 meses» no tienen serie ni cálculo detrás.
- **No está dicho en ninguna parte:** el cliente concreto y cuántos son, qué es el producto (la propuesta es «Propuesta principal», sin contenido), el criterio de éxito, el proyecto que lo construye y qué decidió el comité del 2026-10-09 más allá de «Se mantiene el plan».
- **Normativo:** toca seguros, datos personales y cobro de primas. La definición no declara el país, así que no cité normas; los tres quedan en «No tengo la norma a la vista».
- **Cierre:** la definición no se puede cerrar sin criterio de éxito. Por eso no corresponde `/product-charter`. Sugiero convertir el supuesto del canal y la cifra de volumen en riesgos con doliente.

**Registro de la corrida**
- Los términos TERMS.md v1.0, ya aceptados en la configuración, estaban vigentes.
- La corrida quedó registrada como `2026-10-14-product-definition-1` y reporta 0 hallazgos por señal. El producto aparece como "?" porque `estado/producto.json` está vacío: las corridas anteriores no lo llenaron y esta tampoco.
- Los hallazgos están en el texto de la salida, no en los contadores.
- Puse el aviso de que es un borrador no certificado.

Archivos, en `/home/claude/banco/ronda-1/bancos/espacio/estado/corridas/`:
- salida-product-definition.md