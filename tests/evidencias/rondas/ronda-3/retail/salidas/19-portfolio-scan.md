# /criterio-portfolio:portfolio-scan 

Terminé el barrido: de 88 documentos leí 70, y ninguno quedó ilegible. Quedaron 13 fichas, 10 de ellas nuevas. El código marca 61 hallazgos en la corrida.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no tuve que registrar nada.

- **Proyectos:** escribí y sellé una ficha por cada uno de los 10 proyectos que se leyeron: PRY-199, 200, 201, 202, 205, 207, 208, 209, 210 y 211. PRY-203, 204 y 206 no cambiaron y no los abrí; las 18 piezas sin cambio son suyas.
- **PRY-201:** tiene 28 documentos. Su `ficha-pm.json` quedó guardada entera en `pm_record`, aparte de mi lectura, y el código emitió un `pm_vs_pmo`.
- **Movidos y pendientes:** no existe una carpeta `entrada/`, así que no moví nada y no hay nada pendiente de clasificar. Las notas del 2026-10-15 están en la raíz de la carpeta de PRY-201, no en `30-reuniones/`; las asigné a PRY-201 y no las moví.
- **Sin dato:** la autoridad del gerente y la fase no aparecen en ningún documento de los 10 proyectos. El producto falta en PRY-202, 209, 210 y 211, donde el acta dice "No aplica". PRY-211 no tiene cronograma ni actas de comité.

**Lo que más pesa en los 61 hallazgos:**
- **18 hitos cerrados sin acta que los pruebe.**
- **Facturas por encima de lo respaldado:**
  - PRY-201, contrato CT-978: la factura de 966.093.580 COP cubre dos entregables y solo uno tiene acta.
  - PRY-201, contrato CT-963: la factura de 921.509.752 COP supera lo que respaldan las actas.
  - PRY-205, contrato CT-377: hay una factura de 247.703.694 COP y ningún entregable del contrato está aceptado.
- **Compromisos vencidos sin evidencia (7):** cuatro en PRY-201, y uno cada uno en PRY-200, 205 y 210.
- **Reprogramaciones reunión tras reunión en PRY-201:** el documento 1 de Paula Céspedes lleva seis, hasta 2026-12-17.
- **Verde declarado frente a la evidencia:** PRY-208 y PRY-209 declaran verde y proyectan sobre el presupuesto aprobado. El cierre comprometido de PRY-208 era el 2026-02-28 y ya pasó.
- **Riesgo dicho y no registrado en PRY-201:** en las notas del 2026-10-15 se comentó que el proveedor podría no llegar con el equipo completo. Lo levanté en la ficha, sin probabilidad, impacto ni responsable.

**Para quien lo revise:**
- En mi texto de salida escribí que PRY-199 tiene un hallazgo de seguridad y una prueba de carga fallida pese a declarar verde. Es lo que dice su informe, pero el código no emitió ninguna señal para PRY-199.
- Los compromisos de PRY-205 (Sandra Gil) y PRY-210 (María Restrepo) tienen fecha anterior a la reunión que los registra. Los marqué como vencidos por eso.

Quedó registrada la corrida `2026-10-15-portfolio-scan-1` (227 segundos), con la instantánea y el texto completo de lo mostrado. Como hay más de un proyecto, puedo generar ahora el informe consolidado con `/portfolio-report`; no lo corrí.

Archivos en `/home/claude/banco/ronda-3/retail/espacio/estado/`:
- `corridas/salida-portfolio-scan.md`
- `records/` (una ficha por proyecto)

Criterio Portfolio 0.3.9 · términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.9