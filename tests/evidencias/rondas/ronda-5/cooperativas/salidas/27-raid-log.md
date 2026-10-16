# /criterio-portfolio:raid-log portafolio

# RAID del portafolio al 2026-10-16

El registro RAID de los 13 proyectos (PRY-199 a PRY-211) quedó levantado, y ningún ítem tiene doliente, fecha de gestión, probabilidad ni impacto. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no hubo nada que registrar. No hice preguntas.

El registro actual traía 18 riesgos, 16 incidencias y ninguna dependencia ni supuesto. Tras aplicar la prueba rápida de clasificación, el resultado es:

| Tipo | Cantidad |
|---|---|
| Riesgos | 5 |
| Supuestos | 0 (ninguno dicho en los documentos leídos) |
| Incidencias | 16 |
| Dependencias | 13 |
| Riesgo dicho en reunión y no registrado | 1 (PRY-211) |

**Qué cambié de clasificación.** 13 de los 18 "riesgos" eran dependencias, porque dependen de alguien fuera del proyecto:
- "Dependencia del proveedor del core cooperativo" está en 6 proyectos: PRY-199, 200, 204, 205, 206 y 211.
- "Aprobación del reglamento por el Consejo de Administración" está en PRY-202, 208, 209 y 210.
- "El proveedor no ha confirmado la fecha de la última entrega" está en PRY-200, 201 y 208.

**Lo que propongo subir al comité del 2026-10-23.** Cada punto necesita una decisión formulada:
1. Quién coordina con el proveedor del core para los 6 proyectos.
2. Fecha del Consejo y responsable para el reglamento, que afecta a 4 proyectos. Otros 5 informes reportan como incidencia que el Consejo pidió ajustar el reglamento.
3. El riesgo no registrado de PRY-211. En las notas del 2026-10-16 se dijo que el proveedor podría no llegar con el equipo completo para la siguiente fase. PRY-211 está en Rojo, con 56 % de avance.

Las otras 10 actas y notas de reunión solo traen compromisos, sin riesgos dichos al pasar.

**Lo que no pude hacer:**
- **Cruce de dependencias entre proyectos:** las 13 actas de constitución dicen "Ninguna declarada" y ninguna dependencia trae código de proyecto. PRY-202 se llama "Core cooperativo", pero ningún documento dice que el proveedor del core de los otros seis dependa de él. Es una hipótesis para confirmar con los gerentes.
- **Movimiento histórico:** solo hay una fotografía por proyecto. El "último movimiento" de cada ítem es la fecha del informe donde aparece, no un movimiento verificado.
- **Minutas:** faltan en 7 proyectos (PRY-200, 201, 203, 204, 207, 208 y 210). De esos solo leí los informes de avance.
- **Textos idénticos:** el mismo texto de riesgo aparece en proyectos sin relación, como mobiliario y cobranza. Puede ser una plantilla copiada, y conviene preguntarlo antes de escalar.

La corrida quedó registrada como `2026-10-16-raid-log-1`, con una duración de 108 segundos. El registro completo, con las 35 filas, está en `/home/claude/banco/ronda-5/cooperativas/espacio/estado/corridas/salida-raid-log.md`.