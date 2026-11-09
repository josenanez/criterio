# Términos de uso

[English](TERMS.md) · Versión 1.5 · 2026-11-09

Al instalar, desplegar, probar o ejecutar Criterio, usted acepta estos términos. Si no los acepta, no lo instale.

---

## 1. No es asesoría; cada versión se prueba antes de publicarse

Criterio entrega **análisis contrastado contra la evidencia** para quien decide: cada dato con la cita del documento del que sale. No es asesoría, no sustituye el juicio de quien decide y no crea relación profesional alguna entre usted y el mantenedor o cualquier aportante.

Cada versión pasa una validación interna antes de publicarse: pruebas automáticas del código en cada cambio, y rondas en las que los agentes de cada familia ejecutan sus comandos sobre material de prueba sintético de varias industrias y países, con entidades de control en las que cualquier señal es una falla, sin datos de ninguna organización. Lo que produce cada agente se compara con una clave de respuestas, y los resultados —con su margen de confianza, los defectos encontrados y su corrección— se publican en la evidencia de pruebas de cada familia, en https://www.josenanez.com/es/agents, y en la nota legal.

## 2. La decisión, y su verificación, son de quien la firma

Antes de usar un análisis de Criterio para decidir, firmar, reportar, escalar o asesorar, usted lo verifica contra sus fuentes y responde por esa decisión. Las citas existen para que la verificación tome segundos; no la sustituyen.

## 3. Qué puede y qué no puede saber

Su insumo son los documentos a los que usted lo apunte. No sabe lo que se decidió fuera de ellos. Que no aparezca un hallazgo no es evidencia de que no haya nada mal.

## 4. Sus datos

Los documentos que usted procese son tratados por la plataforma de IA sobre la que ejecute esto, bajo los términos de esa plataforma, y no solo en su equipo. Confirme que sea admisible bajo sus políticas, sus contratos y la ley de protección de datos aplicable antes de procesar material confidencial o personal. Esa evaluación le corresponde a usted.

No envíe a este proyecto documentos de clientes, datos personales reales ni material confidencial. Los aportes que los contengan serán rechazados.

## 5. Garantía y responsabilidad

Se rigen por la licencia Apache 2.0, secciones 7 y 8.

## 6. Aportes

Los aportes se licencian bajo Apache 2.0 por el solo hecho de enviarlos. Al aportar usted declara que escribió el contenido o tiene derecho a enviarlo, y que no contiene material confidencial ni de clientes.

Los aportantes se acreditan por su nombre. El crédito registra quién escribió algo; no es una garantía.

## 7. Marcas

Apache 2.0 no concede derechos sobre marcas. "Criterio" y el nombre del mantenedor no pueden usarse para respaldar ni promover productos derivados sin autorización escrita. Las marcas de Anthropic son suyas; este proyecto no está afiliado a Anthropic ni cuenta con su respaldo o patrocinio.

## 8. Cómo se registra la aceptación

**Una aceptación, mientras estos términos no cambien.** Usted acepta estos términos una vez, al configurar Criterio. Esa aceptación sigue vigente cuando actualiza a versiones nuevas de cualquier familia, mientras el texto de estos términos sea el mismo: actualizar no le pide aceptar de nuevo. Le recomendamos usar siempre la última versión estable de cada familia, que es la que se prueba y se publica con su evidencia. Hasta que la aceptación quede registrada, el plugin responde preguntas pero no produce análisis ni informes. No la asume, no la infiere de que usted siga conversando y no la registra sin un sí explícito.

**Un comprobante que es suyo.** Al aceptar, el plugin deja en su equipo, en `.criterio/terminos/`, un comprobante en Markdown y otro en PDF con su nombre, la fecha, la versión de la familia, la versión de estos términos, su huella SHA-256 y la entrada del registro de versiones, seguidos del texto completo que aceptó. Los comprobantes anteriores se conservan: la sucesión de aceptaciones es la trazabilidad. El detalle técnico está en `docs/acceptance.md`, en el repositorio.

**Integridad.** Todo comprobante conserva su integridad y no puede modificarse. Su huella SHA-256 (SHA-2 de 256 bits) queda registrada en la configuración, en el registro de aceptaciones y en un archivo `.sha256` que lo acompaña; cualquier cambio, por mínimo que sea, produce otra huella y le quita validez como constancia. Lo mismo vale para estos términos: su huella se publica con cada versión.

**Nota legal y registro de versiones.** La nota legal de Criterio y el registro de versiones —qué cambió en cada una, en qué versión queda cada familia, qué términos la rigen y su huella— se publican en https://www.josenanez.com/es/agents/criterio-pmo/legal. Cada entrada del registro lleva la huella de la anterior, así que una entrada alterada o quitada se nota.

Todo informe que genere el plugin lleva el descargo y el estado de las fichas que usó, para que la advertencia viaje con el documento y no se quede en este repositorio.

## 9. Cambios a estos términos

Estos términos están versionados. Un cambio sube la versión y la fecha al inicio de este archivo y queda en el registro de versiones con su huella. Ningún cambio a estos términos rige para usted sin su aceptación expresa: cuando el texto cambia, el plugin se lo muestra y le pide aceptarlo antes de producir análisis o informes, y deja un comprobante nuevo. Si no lo acepta, puede seguir usando la versión que ya aceptó.

## En corto

Esto es lo que el plugin le muestra antes de pedirle que acepte:

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

---

Texto completo de la licencia: `LICENSE`, en la raíz del repositorio. Límites en lenguaje llano: `DISCLAIMER.es.md`. Nota legal y registro de versiones: https://www.josenanez.com/es/agents/criterio-pmo/legal
