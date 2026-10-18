# /criterio-portfolio:raid-log portafolio

# RAID — portafolio (13 proyectos, PRY-199 a PRY-211) al 2026-10-17

Salió de las 13 fichas, los informes de avance, las actas, las minutas de comité y las notas de PRY-200 del 2026-10-17. Los términos de esta versión ya estaban aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo.

**Conteo en los informes:** 21 riesgos, 14 incidencias, 0 supuestos y 0 dependencias.

- **Sin doliente ni fecha:** los 35 ítems no tienen doliente. Los 21 riesgos tampoco traen fecha, probabilidad ni impacto. No rellené nada.
- **No registrado formalmente:** 1 riesgo, en PRY-200. Las notas del 2026-10-17 dicen que "el proveedor podría no llegar con el equipo completo para la siguiente fase" y que nadie lo anotó. No encontré otros riesgos dichos al pasar en las minutas.
- **Sin movimiento en dos períodos:** no pude medirlo, porque las fichas guardan una sola fecha por ítem y ningún historial.
- **Texto repetido:** el mismo texto aparece en varios proyectos (8 con el calendario del core, 6 con la prueba de carga, 6 con concentración del conocimiento, 5 con el equipo de seguridad). Puede ser un problema común o plantilla copiada; los documentos no lo aclaran.

**Reclasificaciones, mías y sin confirmar:**
- **Pasan de riesgo a dependencia:**
  - "Calendario de liberaciones del core" en 8 proyectos.
  - "Equipo de seguridad" en 5 proyectos.
  - "El proveedor no ha confirmado la fecha" en PRY-202.
- **Sin códigos de proyecto:** ninguna dependencia lleva el código del proyecto del que depende. Las actas de los 13 dicen "Ninguna declarada".
- **Sin cruce de fechas:** por eso no pude cruzar si algún proyecto movió su fecha. Tampoco sé si "el core" es PRY-201; no lo afirmé.

**Necesitan decisión ahora (7):**
- El calendario del core, que afecta a 8 proyectos.
- La prueba de carga repetida en 6 proyectos.
- El equipo de seguridad (5 proyectos) y el hallazgo de seguridad de PRY-208.
- La salida reprogramada sin fecha nueva en PRY-210 y en PRY-211.
- La rotación en PRY-209.
- El proveedor sin confirmar en PRY-202.

**Datos viejos:** los informes de PRY-203, PRY-208 y PRY-209 superan el umbral de 15 días de silencio, así que su RAID puede estar desactualizado.

**Siguiente paso:** puedo subir a comité los 7 ítems con la decisión formulada. También puedo proponer un doliente para los 35 ítems sin él; propondría, no asignaría.

**Archivos:**
- La salida completa, con las tablas de decisión, dependencias y el registro de los 36 ítems, está en `estado/corridas/salida-raid-log.md`.
- La corrida quedó registrada como `2026-10-17-raid-log-1`.

**Qué no pude ver:** quién es "el core" y quién es el "equipo de seguridad"; probabilidad, impacto, doliente y fecha de los ítems; cuánto lleva cada uno sin movimiento; y lo que se habló fuera de los documentos. Cada ítem remite al informe de su proyecto, y la verificación contra los originales es suya.