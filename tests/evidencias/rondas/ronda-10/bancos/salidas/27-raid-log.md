# /criterio-portfolio:raid-log portafolio

El RAID del portafolio está hecho y la corrida quedó registrada (`2026-10-18-raid-log-1`, 95 s, 13 proyectos). La salida completa está en `/home/claude/banco/ronda-10/bancos/espacio/estado/corridas/salida-raid-log.md`.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré otra vez.

Salen 35 ítems de las 13 fichas, tomados de los informes de avance y las minutas. Los PDF y los cronogramas no los releí; uso solo lo que la ficha ya cita.

- **Doliente y fecha:** ningún ítem tiene doliente, fecha, probabilidad, impacto ni mitigación. Por eso no puntué nada; subo tres ítems por otras razones.
- **Reclasificación:** de los 19 riesgos de las fichas, 9 pasan a dependencia porque dependen de alguien fuera del proyecto. Son 4 del calendario de liberaciones del core (PRY-201, 205, 206 y 210), 2 del proveedor sin fecha (PRY-204 y 207) y 3 de la disponibilidad del equipo de seguridad. Los 3 de seguridad son propuesta mía: vuelven a riesgo si ese equipo está dentro del proyecto. Quedan 10 riesgos, 0 supuestos, 16 incidencias y 9 dependencias.
- **No registrado:** hay un solo riesgo dicho en reunión sin registrar. En PRY-201, el 2026-10-18, se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase. La revisión con el proveedor está fijada para el 2026-10-28.
- **Decisión ahora:**
  - formalizar ese riesgo de PRY-201;
  - nombrar de qué proyecto depende cada uno de los cuatro proyectos que dependen "del core";
  - llevar al comité la solicitud de cambio CC-01 de PRY-210 (+102 días, 204.000.000 COP), con el proyecto en rojo.
- **Incidencias dudosas:** dos "se ajustó el plan de pruebas" (PRY-201 y 205) describen un ajuste, no un problema. Y "se recibió la aprobación regulatoria" (PRY-204) ya está resuelta.

Lo que no pude saber:
- **Movimiento:** cada ítem tiene una sola observación y no hay historial. No pude medir sin movimiento ni mitigación vencida.
- **Cuál es "el core":** ningún documento lo ata a un código de proyecto. Por eso no crucé las dependencias contra fechas de otros proyectos.
- **Fichas incompletas:** en PRY-202 y PRY-210 la ficha no recoge todas las líneas del informe. Las otras no las comparé; conviene releer sus PDF.

Ofrezco subir a comité los tres ítems de decisión. Doliente no asigné a nadie; si quieres, propongo uno por ítem.