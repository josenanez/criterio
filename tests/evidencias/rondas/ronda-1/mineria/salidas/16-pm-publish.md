# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-208 en `/home/claude/banco/ronda-1/mineria/espacio/documentos/proyectos/PRY-208-trazabilidad-del-mineral/00-gobierno/ficha-pm.json`, con corte al 2026-10-14. No se la mostré a nadie ni avisé a la PMO. Vera la leerá en su próximo barrido.

**Lleva:** 11 campos con dato y 1 sin decir en ninguna parte. El que falta es `declared.status`: la minuta del 14 de octubre no declara estado y `declared.as_of` queda vacío.

**Lo más viejo que va ahí:** los 11 campos con dato (identidad, plan y dinero aprobado) vienen del acta de constitución del 2025-07-26. Tienen 15 meses, así que pasan de un año.

Además:
- **Plan vencido:** `plan.end_date` es 2026-07-21, ya pasada. La ficha no trae hitos ni línea base.
- **Lectura parcial:** solo se leyeron la minuta del 14 de octubre, la del 9 de octubre y el acta. El resto del proyecto no se ha leído.
- **Patrocinador y gerente:** el acta los da como la misma persona, Gustavo Neira. Si eso cambió desde 2025, la PMO lo verá como contradicción.
- **Alerta abierta:** un compromiso sin fecha de Laura Vélez («Mandar el ajuste del presupuesto», «la otra semana»).

Los términos ya estaban aceptados en la configuración (versión 1.0, igual a `TERMS.md`). La carpeta de gobierno ya existía, así que no creé nada. La salida quedó en `estado/PRY-208-trazabilidad-del-mineral/corridas/salida-pm-publish.md` y la corrida se registró como `2026-10-14-pm-publish-1`.