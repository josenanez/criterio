# /criterio-portfolio:project-charter PRY-204 revisar

Revisé el acta de PRY-204 (Cajas de autopago). Existe, es del 2026-03-15 y le faltan casi todos los campos que importan. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo.

**Qué falta y qué consecuencia tiene**
- **Autoridad del gerente:** no está.
  - Nadie sabe hasta qué monto ni qué cambio de alcance puede decidir Liliana Torres sin comité.
  - CC-01 muestra el efecto: ampliación de alcance, +35 días y +70.000.000 COP (0,39 % de los 18.000 M). Quedó "autorizada por el comité", sin nombre ni fecha de sesión, y no se puede saber si hacía falta comité.
- **Objetivo de negocio:** dice "Entregar cajas de autopago para Comercial". Describe la solución, no un resultado medible.
- **Alcance:** son tres "Componente 1/2/3" sin describir, así que no se puede verificar qué amplió CC-01.
- **Exclusiones:** dice "Lo que otro proyecto cubre", sin nombrar el proyecto.
- **Criterio de éxito:** "en producción y medido", sin métrica ni meta. Tampoco dice quién lo mide.
- **Hitos, supuestos, restricciones y cadencia del comité:** no están. El acta declara cero dependencias aunque el proyecto toca medios de pago.
- **Patrocinador y gerente:** vienen con nombre de persona (Natalia Ospina y Liliana Torres). Esto está bien.

**Lo que se ve en el resto de la carpeta**
- El cierre original (2026-10-04) ya pasó. El informe declara 41 % de avance y estado amarillo.
- Ningún documento registra una línea base nueva ni la fecha de despliegue reprogramada.
- La proyección de costo no dice si incluye los 70 M de CC-01.

**Lo que no sé:** si el .docx trae algo que el texto convertido no recogió, qué comité autorizó CC-01 y si existe una línea base posterior. Los campos sin fuente quedaron marcados como pendientes de definir, sin completarlos.

**Siguientes pasos que te ofrezco**
- Llevar la definición de autoridad del gerente al Comité Comercial como decisión. El comité de portafolio está agendado para el 2026-10-22.
- Pasar los supuestos que salieron al registro RAID con `/raid-log`.

La corrida quedó registrada como `2026-10-17-project-charter-1`. Lo que te mostré está en `estado/corridas/salida-project-charter.md`.