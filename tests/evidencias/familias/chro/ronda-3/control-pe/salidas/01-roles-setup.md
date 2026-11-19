# /criterio-roles:roles-setup talento/20601234567-servicios-andinos-control-sinteticos

Norma no quedó lista sobre esta entidad. Me detuve en la validación final porque falta un dato que ningún documento de la carpeta trae, y no lo invento.

**Carpeta:** la única candidata es `talento/20601234567-servicios-andinos-control-sinteticos`, que tiene las seis subcarpetas de la estructura. Respuesta tomada: sí.

**Lo que encontré**
- 43 archivos, entre ellos 2 perfiles de cargo:
  - SA-01, Analista de soporte, con ocupación O*NET 15-1232.00.
  - SA-02, Cajero, con ocupación O*NET 41-2011.00.
- El estándar es la descarga de O*NET en `00-referencia/onet-31-0-sintetico/`, y se procesa. La ocupación 15-1232.00 trae su título («Computer User Support Specialists (synthetic)»), 1 tarea y la zona 3. No trae destrezas, porque el umbral de importancia está vacío.
- No se pudo procesar `30-candidatos/VAC-41/CAN-506/diploma.jpg` porque el formato .jpg no está soportado. Ese archivo es de Cándido, no de Norma.

**Respuestas que tomé de los documentos**
- **Entidad:** Servicios Andinos Control Sintéticos, RUC 20601234567, Perú. Periodo 2026-11.
- **Estándar:** O*NET. Es una descarga sintética de prueba, no la descarga oficial.
- **Revisión de perfiles:** cada 12 meses, según la política de selección.
- **Lo que un perfil no puede pedir:** edad, sexo, estado civil y fotografía, según la política de selección.
- **Equivalencia de estudios con la CINE:** queda vacía, porque con O*NET esa comparación no se hace.
- **Dónde guardo lo que encuentro:** `estado-talento/20601234567-servicios-andinos-control-sinteticos`.
- **Marca de la carpeta:** sí, pero no se dejó.

**Términos (versión 1.6), tal cual:**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Por qué me detuve:** al validar, el motor devolvió este problema: «standard.importance_threshold: O*NET da la importancia de cada destreza de 1 a 5; desde qué valor es exigible lo fija la organización». La política de selección no fija ese valor. Mientras falte:
- la aceptación de José Francisco Ñáñez no quedó registrada y no hay comprobante;
- la carpeta no quedó marcada;
- no se armó la primera ficha ni corrió el reporte de los perfiles.

**Para seguir:** que la organización diga desde qué importancia, de 1 a 5, una destreza es exigible, y volver a correr `/criterio-roles:roles-setup`.

**Lo que quedó escrito:**
- La configuración, en `.criterio/perfiles/20601234567/config.json`, con el umbral vacío.
- Lo que te mostré, en `estado-talento/20601234567-servicios-andinos-control-sinteticos/corridas/salida-roles-setup.md`.
- La corrida, registrada como `2026-11-16-roles-setup-1`.

**Cuándo vuelvo:** sin reloj. No ofrecí la tarea diaria porque la instalación no terminó.