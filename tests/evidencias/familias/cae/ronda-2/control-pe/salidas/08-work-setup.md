# /criterio-audit-work:work-setup auditoria/20602888432-cooperativa-control-sintetica

Justo quedó configurado para la Cooperativa Control Sintética (RUC 20602888432) y el primer reporte de hallazgos del periodo 2026-11 no encontró nada que atender.

**Las respuestas, tomadas de los documentos y del setup del plan:**
- **Carpeta:** `auditoria/20602888432-cooperativa-control-sintetica`. Era la única candidata y ya estaba marcada, así que no la volví a marcar.
- **Entidad:** Perú, en soles, como en la configuración del plan.
- **Escala de prioridad:** Alta desde 15, Media desde 8 y Baja desde 1, según la metodología.
- **Aprobaciones:** el plan lo aprueba el Comité de auditoría; el programa, la jefa de auditoría.
- **Publicación en Rostrum:** no se publica.
- **Estado:** se guarda en `estado-auditoria/20602888432-cooperativa-control-sintetica`, el mismo que usa el plan.

**Términos:** quedó registrado que José Francisco Ñáñez aceptó la versión 1.6 el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-work-0.2.2-2026-11-24.md`, con su `.pdf`.

**La configuración** está en `.criterio/trabajos/20602888432/config.json`.

**La primera ficha:** procesé los 15 documentos de `20-trabajos/` y los 15 se pudieron convertir. Llevé a la ficha los dos trabajos con sus tres hallazgos:

| Trabajo | Hallazgo | Prioridad | La de la metodología | Le falta | Papeles |
|---|---|---|---|---|---|
| TR-01 | H-01 | Alta | alta | — | PT-03 |
| TR-01 | H-02 | Media | media | — | PT-02 |
| TR-02 | H-03 | Media | media | — | PT-02 |

En H-02 no hay causa: el papel explica que la gerencia no entregó a tiempo el registro de avalúos, y el motor lo acepta como razón. Los papeles que no traen hallazgos son PT-01 de los dos trabajos y PT-03 de TR-02. El reporte completo está en `estado-auditoria/20602888432-cooperativa-control-sintetica/trabajos/2026-11/reporte-finding-check.md`.

**Algo raro en el reporte del motor:** en «Fuentes» dice «Sin documentos citados», aunque la ficha cita el papel y el informe de cada hallazgo. Parece que el motor no está pasando esas citas al reporte; conviene revisarlo.

**Reloj:** no quedó tarea programada, porque solo se crea con un sí explícito y en esta prueba nadie lo dio. Se puede correr a mano con `/criterio-audit-work:work-wake`.

La corrida quedó registrada como `2026-11-24-work-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.