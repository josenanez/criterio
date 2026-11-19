# /criterio-roles:profile-build 

Los términos no tienen aceptación registrada en esta carpeta, así que este comando se detiene aquí.

`talento.py terminos --today 2026-11-16` respondió `vigente: false` porque no hay ninguna aceptación registrada. Corresponde a los términos 1.6 de criterio-roles 0.1.0. Este es su `en_corto`, tal cual:

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Hay que correr `/criterio-roles:roles-setup`**, que es el comando que registra la aceptación. Ahí queda registrada la de José Francisco Ñáñez con fecha 2026-11-16, como indica la prueba. `/profile-build` no produce nada sin esa aceptación. Por eso no registré la aceptación desde aquí aunque el motor tiene una acción `aceptar`.

Por la misma razón no hice nada más:
- no consulté ninguna ocupación,
- no escribí ningún borrador,
- no escribí la salida ni registré la corrida.

Para cuando se reanude: la configuración es `.criterio/perfiles/20601234567/config.json`, de Servicios Andinos Control Sintéticos (PE), con el estándar O*NET. El argumento de la prueba no trae ni el código ni el nombre de un cargo, así que también habrá que indicar qué ocupación armar.