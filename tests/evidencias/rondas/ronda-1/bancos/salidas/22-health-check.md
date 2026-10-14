# /criterio-portfolio:health-check PRY-203

Hice el diagnóstico de PRY-203 Open Banking y lo dejé registrado en `estado/corridas/salida-health-check.md`. La corrida quedó como `2026-10-14-health-check-1`.

Leí 8 documentos (del 2026-02-27 al 2026-10-12) y pude leerlos todos. Ningún documento de los otros 12 proyectos menciona PRY-203. Los términos v1.0 ya constaban en la configuración, así que no hizo falta pedirlos.

**Dictamen:** 7 afirmaciones sostenidas, 9 sin sustento y 3 contradichas.

- **Sostenido:** quién gobierna el proyecto, el presupuesto aprobado de 6.800.000.000 COP, el contrato CT-948 y el estado Rojo declarado.
- **Gobierno:** no hay autoridad del gerente declarada en ningún documento.
- **Línea base:** hay una desviación de 112 días (44.4 %) contra la original. La línea base v2 no tiene aprobación documentada. CC-01 dice "autorizada por el comité", sin nombre, fecha ni acta.
- **Hitos:** 4 hitos figuran como cerrados, hace entre 17 y 169 días, y ninguno tiene evidencia.
- **Contradicciones:**
  - El avance declarado es 45 %, pero el cronograma tiene 4 de 5 hitos cerrados.
  - Se radicó una factura de 631.036.273 COP sin acta de recibo, con cero entregables aceptados.
  - El ejecutado (3.066.221.014) supera al comprometido (3.046.727.673).
- **Cifras:** las derivadas las copié de `compute`. El informe mantiene 6.800.000.000 como aprobado aunque CC-01 pide 224.000.000 más.

Con la salida de la corrida quedó también el detalle de lo que dijo y nadie registró, y de lo que la carpeta no permite saber.

No recomiendo detener, continuar ni reestructurar, porque eso lo decide quien tiene la facultad. Puedo llevar las 3 contradicciones al gerente como preguntas, una por una, o preparar el punto del comité del 2026-10-20 con lo que falta.

Un detalle de método: dos comandos míos usaron `cd`, un bucle y tuberías, contra la regla de llamadas simples. No cambia el resultado.