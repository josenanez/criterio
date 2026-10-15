# Términos de uso

[English](TERMS.md) · Versión 1.1 · 2026-10-15

Al instalar, desplegar, probar o ejecutar Criterio, usted acepta estos términos. Si no los acepta, no lo instale.

---

## 1. No es asesoría; cada versión se certifica antes de publicarse

Criterio produce **borradores de trabajo**. No es asesoría y no crea relación profesional alguna entre usted y el mantenedor o cualquier aportante.

Cada versión pasa una certificación interna antes de publicarse: pruebas automáticas del código en cada cambio, y rondas en las que los tres agentes ejecutan todos sus comandos sobre datos de prueba sintéticos, construidos a partir de proyectos reales de entidades financieras, retail y minería, sin datos de ninguna organización. Lo que produce cada agente se compara con una clave de respuestas, y los resultados —con su margen de confianza, los defectos encontrados y su corrección— se publican en la evidencia de pruebas y en la nota legal: https://www.josenanez.com/es/agents/criterio-pmo.

## 2. La verificación es suya

Usted es responsable de verificar toda salida antes de usarla para decidir, firmar, reportar, escalar o asesorar. Las citas existen para que la verificación sea posible; no la sustituyen.

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

**Una aceptación por versión.** Cada versión de la familia de agentes pide aceptar estos términos, también cuando su texto no cambió: instalar Criterio o actualizarlo a una versión nueva exige una aceptación nueva. Hasta que la aceptación de la versión instalada quede registrada, el plugin responde preguntas pero no produce análisis ni informes. No la asume, no la infiere de que usted siga conversando y no la registra sin un sí explícito.

**Un comprobante que es suyo.** Al aceptar, el plugin deja en su equipo, en `.criterio/terminos/`, un comprobante en Markdown y otro en PDF con su nombre, la fecha, la versión de la familia, la versión de estos términos, su huella SHA-256 y la entrada del registro de versiones, seguidos del texto completo que aceptó. Los comprobantes anteriores se conservan: la sucesión de aceptaciones es la trazabilidad. El detalle técnico está en `docs/acceptance.md`, en el repositorio.

**Integridad.** Todo comprobante conserva su integridad y no puede modificarse. Su huella SHA-256 (SHA-2 de 256 bits) queda registrada en la configuración, en el registro de aceptaciones y en un archivo `.sha256` que lo acompaña; cualquier cambio, por mínimo que sea, produce otra huella y le quita validez como constancia. Lo mismo vale para estos términos: su huella se publica con cada versión.

**Nota legal y registro de versiones.** La nota legal de la familia de agentes y el registro de versiones —qué cambió en cada una, qué términos la rigen y su huella— se publican en https://www.josenanez.com/es/agents/criterio-pmo/legal. Cada entrada del registro lleva la huella de la anterior, así que una entrada alterada o quitada se nota.

Todo informe que genere el plugin lleva el descargo y el estado de las fichas que usó, para que la advertencia viaje con el documento y no se quede en este repositorio.

## 9. Cambios a estos términos

Estos términos están versionados. Un cambio sube la versión y la fecha al inicio de este archivo y queda en el registro de versiones con su huella. Como cada versión de la familia se acepta de nuevo, un cambio en los términos llega a quien usa Criterio en la siguiente actualización.

## En corto

Esto es lo que el plugin le muestra antes de pedirle que acepte:

> Criterio produce borradores de trabajo, no decisiones ni asesoría. Procesa los documentos que usted le indique y dice lo que muestran; no sabe lo que se habló fuera de ellos. Puede equivocarse, y por eso cada dato viene con la cita del documento de donde salió: la verificación es suya. Sus documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo. Cada versión se certifica antes de publicarse; garantía y responsabilidad: licencia Apache 2.0. Cada versión se acepta de nuevo y deja un comprobante en Markdown y PDF con su huella SHA-256. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

---

Texto completo de la licencia: `LICENSE`, en la raíz del repositorio. Límites en lenguaje llano: `DISCLAIMER.es.md`. Nota legal y registro de versiones: https://www.josenanez.com/es/agents/criterio-pmo/legal
