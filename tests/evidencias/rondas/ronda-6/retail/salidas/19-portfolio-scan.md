# /criterio-portfolio:portfolio-scan 

## Barrido — 2026-10-16

Leí 69 de los 82 documentos y dejé fichas nuevas para 10 proyectos; las fichas de PRY-200, 202 y 210 no cambiaron. Los términos ya estaban vigentes (versión 0.3.12, aceptados por José Francisco Ñáñez el 2026-10-16), así que no hubo que registrarlos de nuevo.

- **Plan:** un lote de 10 proyectos, uno tras otro y sin subagentes. Los 13 documentos que no leí son los de PRY-200, 202 y 210, que no tuvieron cambios.
- **Lectura:** los 82 documentos se convirtieron a texto y ninguno resultó ilegible. Cada ficha cita el documento original.
- **Fichas nuevas:** PRY-199, 201, 203, 204, 205, 206, 207, 208, 209 y 211, todas selladas al terminar cada una.
- **`entrada/`:** no existe esa carpeta, así que no moví nada.
- **Sin dato:** `identity.authority` e `identity.phase` quedaron `not_found` en las 10 fichas. `identity.product` también en PRY-203, 206, 209 y 211, porque sus actas dicen «No aplica».

**Lo que conviene mirar**
- **Hitos cerrados sin acta:** el cronograma los declara cerrados y no hay acta de recibo. Los registré como cumplidos con la evidencia vacía. Son 30 hitos en todo el portafolio, la mayoría en PRY-203, 206, 209 y 211.
- **Facturas sin entrega que las respalde:**
  - En PRY-209 hay una factura de 275.224.201 COP radicada, pero el contrato declara sus dos entregables como pendiente y en curso, sin acta.
  - En PRY-205 el contrato declara recibido un entregable que no tiene acta, y la factura cubre dos.
- **Cambios sin autorizante identificado:**
  - En PRY-207 y PRY-209, CC-01 dice «autorizada por el comité», sin nombre ni fecha.
  - En PRY-207 el presupuesto aprobado del informe sigue en 800.000.000 COP, sin los 128.000.000 del cambio.
  - En PRY-209 el cambio mueve a 2026-07-07 una fecha que ya había pasado.
- **PRY-206:**
  - Declara verde con 21% de avance, pero su cronograma tiene los cinco hitos cerrados y fecha final 2026-08-31.
  - Un compromiso se reprogramó 5 veces y otro 4.
  - Cinco compromisos se dieron por entregados en reunión sin acta.
  - Las notas del 2026-10-16 recogen un riesgo que nadie registró (el proveedor podría no llegar con el equipo completo).
- **Compromisos con fecha pasada:** PRY-201, 204 y 207, y los vencidos de PRY-206.
- **Despliegue reprogramado sin cronograma nuevo:** PRY-203, 204 y 211 lo dicen en el informe, pero solo existe el cronograma v1 con la misma fecha.
- **PRY-208:** declara 94% de avance con 459.248.225 de 2.400.000.000 COP ejecutados.

Para PRY-206 incluí la ficha que publicó su gerente (`ficha-pm.json`) entera en `pm_record`, sin mezclarla con mi lectura. Dejé la carpeta `estado/PRY-206-precios-dinámicos/` como estaba: no encaja en la estructura y no la toqué. Registré todos los compromisos de reunión como `open`, incluso los de fecha pasada; el cálculo de vencimiento lo hace el script.

La corrida quedó registrada con 76 señales sobre los 13 proyectos. De ellas, 30 son hitos cerrados sin acta, 9 compromisos vencidos y 8 de avance contra plan. La salida completa está en `estado/corridas/salida-portfolio-scan.md`.

Como hay varios proyectos con contradicciones y compromisos vencidos, el siguiente paso es el informe consolidado con `/criterio-portfolio:portfolio-report`.

*Criterio Portfolio 0.3.12 · fichas tocadas: 10 · campos en `not_found`: los indicados arriba · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.12*