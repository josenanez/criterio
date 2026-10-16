# /criterio-portfolio:project-charter PRY-201 revisar

Revisé el acta de PRY-201 (Core de depósitos). Existe, es del 2026-05-07 y está incompleta en los campos que más pesan.

Los términos ya estaban vigentes (versión 0.3.12, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Qué falta y qué consecuencia tiene**
- **Autoridad del gerente:** no existe.
  - La proyección al cierre es 4.299.777.057 COP contra 4.200.000.000 aprobados, unos 99,8 millones más (≈2,4 %).
  - Sin una autoridad declarada, nadie puede decir si Camilo Beltrán decide ese exceso o si le toca al Comité de Transformación Digital.
- **Objetivo de negocio:** solo describe el entregable («Entregar core de depósitos…»). No tiene resultado ni cifra, así que no hay cómo juzgar si el proyecto sigue valiendo lo aprobado.
- **Alcance:** dice «Componente 1, 2, 3», sin detalle. No se puede distinguir un cambio de alcance de una aclaración.
- **Exclusiones:** dice «Lo que otro proyecto cubre», sin nombrar el proyecto. Así no excluye nada.
- **Criterio de éxito:** «en producción y medido» no dice qué se mide, con qué umbral ni quién lo mide.
- **Supuestos, restricciones y cadencia de reporte:** no existen.
- **Dependencias:** el acta dice «Ninguna declarada», pero el informe del 2026-10-14 reporta como riesgo abierto la dependencia del calendario de liberaciones del core. El cronograma además tiene el hito «Integración con el core» (2027-04-12).
- **Patrocinador y gerente:** tienen nombre (Elena Duarte y Camilo Beltrán). Sin hallazgo.

En el contenido del acta dejé como «pendiente de definir» todo lo que ningún documento sustenta. No completé nada con lo razonable.

**Lo que no cubre esta revisión:** no evalué si el «Verde» del informe se sostiene (prueba de carga fallida, dos semanas perdidas, hallazgo de seguridad). Tampoco sé nada de lo hablado fuera de los documentos.

**Siguientes pasos que ofrezco**
- Llevar la definición de la autoridad del gerente al comité del 2026-10-23, junto con el exceso proyectado.
- Pasar al registro RAID la dependencia no declarada y la falta de supuestos, con `/raid-log`.

Registré la corrida con `portafolio.py corrida` (`2026-10-16-project-charter-1`, 27 segundos). Los archivos están en `estado/corridas/`:
- `salida-project-charter.md`
- `2026-10-16-project-charter-1.md`

El script de la corrida devolvió cifras de los 13 proyectos del portafolio y no de este caso: 78 hallazgos en total, con la lista de PRY-201 vacía. Esas cifras no son hallazgos de esta revisión. Los hallazgos de PRY-201 están solo en el texto de la salida.

Esto es un borrador de trabajo, no una decisión ni asesoría. Cada dato cita el documento de donde sale (acta de constitución, informe de avance del 2026-10-14 y la ficha de PRY-201 para los hitos del cronograma), y la verificación queda en manos de quien lo use.