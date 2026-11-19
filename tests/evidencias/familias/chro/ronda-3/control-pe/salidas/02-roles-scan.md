# /criterio-roles:roles-scan 

Esta entidad (Servicios Andinos Control Sintéticos, 20601234567) no tiene registrada la aceptación de los términos, y `/roles-scan` no produce nada sin ella. Por eso no corrí el inventario, no extraje perfiles y no dejé registrada ninguna corrida.

Esto es lo que dice el motor (términos v1.6):

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

La aceptación se registra con `/criterio-roles:roles-setup`, no con este comando, así que no la registré aquí aunque las instrucciones de la prueba lo pedían. Para seguir:
1. Corre `/criterio-roles:roles-setup` y registra ahí la aceptación a nombre de José Francisco Ñáñez, con fecha 2026-11-16.
2. Vuelve a correr `/criterio-roles:roles-scan`.