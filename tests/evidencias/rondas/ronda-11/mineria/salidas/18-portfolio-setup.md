# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo: portafolio de proyectos configurado

La instalación quedó hecha y probé con tres proyectos. Los tres reportan verde y los documentos lo contradicen. No pregunté nada a nadie, porque la sesión no tenía interfaz. En cada paso tomé la respuesta sugerida.

**Qué dejé configurado**
- **Configuración:** `.criterio/portafolio/config.json`, y `config` la verificó sin problemas.
- **Carpeta de documentos:** `documentos/proyectos`, la del argumento y la única candidata. Tiene 93 documentos en 13 proyectos, el más reciente del 2026-10-22. Dejé en ella el archivo `_CRITERIO_PORTAFOLIO.txt`.
- **Rol:** PMO del portafolio, porque hay 13 proyectos.
- **Comité y aviso:** semanal, con el próximo el 2026-10-29. Esa fecha es una propuesta mía, porque ningún documento la dice. El informe llega dos días antes.
- **Formato del informe:** página (HTML), que es el valor por defecto de la plantilla.
- **Ubicaciones:** estado en `estado` e informes en `reportes`.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez para la versión 0.8.0, con comprobante en `.criterio/terminos/` (Markdown y PDF). El comprobante lleva la fecha del sistema, 2026-10-23, y no el 2026-10-22 que indicaste.

**Primer resultado: PRY-202, PRY-209 y PRY-211**

El cálculo levantó 26 señales: 4 en PRY-202, 15 en PRY-209 y 7 en PRY-211. Las fichas están en `estado/records/`.
- **PRY-202 (planta de tratamiento de agua):** el hito «Ingeniería de detalle» venció ayer, el cronograma lleva +55 días y el compromiso del punto 37 no tiene fecha.
- **PRY-209 (electrificación de equipos):**
  - Se facturaron 69.149.721 COP al contrato CT-576 sin ningún entregable aceptado. En CT-611 se facturaron 48.285.164 contra 32.663.188 aceptados.
  - El cronograma se movió 211 días y solo 115 están autorizados. Los otros 96 coinciden con la solicitud CC-01, que sigue pendiente de comité.
  - La proyección de costo supera lo aprobado en 15,8 %.
- **PRY-211 (control de polvo en vías):**
  - Declara 58 % de avance con los 4 hitos cerrados.
  - Tres de esos hitos no tienen acta de recibo.
  - El cronograma se movió 43 días sin autorización.

**Pendiente**
- **Portafolio completo:** faltan 10 proyectos, unos 66 documentos, en un solo lote. Mi estimación, no medida, es de 30 a 45 minutos. Lo puedo correr cuando quieras.
- **Cronogramas `.xml`:** el script marca los 9 como ilegibles. Los de estos tres proyectos los leí directamente porque son texto plano, pero el índice de cambios no los cubre.
- **Registro de la corrida:** como corregí un error de conteo (PRY-209 tiene 15 señales y escribí 14), registré la corrida dos veces. La segunda, `2026-10-23-portfolio-setup-2`, es la vigente. Los 118 segundos medidos solo constan en la primera, `…-1`.
- **PMO con equipo:** si tienes gerentes de proyecto, puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios.

Todo lo que le mostré a la persona quedó en `estado/corridas/salida-portfolio-setup.md`.