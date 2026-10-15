# /criterio-portfolio:raid-log portafolio

Levanté el registro RAID del portafolio con 36 ítems, y ninguno tiene doliente. Sale de las 13 fichas, de las actas de comité en Markdown y de las notas de reunión de PRY-203. No releí los informes de avance en PDF ni los comités de producto. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no volví a pedirlos.

- **Conteo:** 8 riesgos, 12 dependencias, 16 incidencias y 0 supuestos.
- **Reclasificados:** 12 de los 20 riesgos de las fichas pasan a dependencia, porque dependen de alguien fuera del proyecto.
  - La aprobación del reglamento por el Consejo está en 7 proyectos.
  - La fecha de entrega que el proveedor no ha confirmado está en 3.
  - La dependencia del proveedor del core está en 2.
- **No registrado formalmente:** un solo riesgo salió de las reuniones. En las notas del 2026-10-15 de PRY-203 se comentó que el proveedor podría no llegar con el equipo completo a la siguiente fase, y nadie lo anotó.
- **Faltantes:** ninguno de los 36 ítems tiene doliente, y los riesgos no traen probabilidad ni impacto. Los riesgos y las dependencias tampoco tienen fecha de compromiso, y las incidencias no tienen fecha de resolución. Lo reporté como hallazgo y no lo rellené.
- **Sin movimiento:** PRY-201 (21 días) y PRY-202 (18 días) pasan el umbral de 15 días de la configuración.
- **Dependencias entre proyectos:** ninguna ficha declara una con código de proyecto, así que no hay cruce posible. Las dependencias del proveedor del core en PRY-205 y PRY-210 podrían apuntar a PRY-202, pero ningún documento lo dice. No lo infiero y propongo confirmarlo con la PMO.
- **Para decidir ahora:** el reglamento del Consejo (afecta a 7 proyectos), el hallazgo de seguridad (3 proyectos), la rotación del desarrollador clave (PRY-200 y PRY-205), la prueba de carga que se repite (PRY-199 y PRY-202) y el cambio normativo del supervisor (4 proyectos).
- **Pendiente:** las fichas no traen mitigaciones, así que no pude revisar si alguna venció. Puedo subir a comité los cinco puntos anteriores. Propongo dolientes cuando me digas quién lleva cada proyecto, porque ninguna ficha ni acta lo nombra.

La corrida quedó registrada como `2026-10-15-raid-log-1`, con el texto completo en `estado/corridas/salida-raid-log.md`. Tardó 83 segundos.

Versión del plugin 0.3.8 · fichas leídas: 13 · [Términos y nota legal](https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.8)