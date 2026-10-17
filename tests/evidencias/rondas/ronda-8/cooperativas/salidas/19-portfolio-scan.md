# /criterio-portfolio:portfolio-scan 

El barrido terminó y quedó registrado como `2026-10-17-portfolio-scan-1`.

**Qué se hizo**
- **Documentos:** se leyeron 57 de 76; los otros 19 no habían cambiado. Los 76 se pudieron convertir a texto, ninguno quedó ilegible.
- **Fichas:** se crearon 10 nuevas (PRY-199, 200, 201, 203, 204, 205, 206, 207, 208 y 210) y cada una se selló al terminar su proyecto. PRY-202, 209 y 211 ya tenían ficha y no se tocaron.
- **Términos:** ya estaban vigentes (v1.1) a nombre de José Francisco Ñáñez, con fecha 2026-10-17. No hubo que registrarlos de nuevo.
- **Ejecución:** un solo lote, en esta conversación y sin subagentes. Tardó 217 segundos.
- **`entrada/`:** no existe, así que no se movió nada. Las notas de reunión de PRY-200 se leyeron donde están, en la raíz de su carpeta.
- **Archivos escritos:**
  - Las fichas están en `estado/records/`.
  - La salida completa está en `estado/corridas/salida-portfolio-scan.md`.
  - La instantánea es `estado/snapshots/2026-10-17.json`.

**Lo que hay que mirar**
- **Hitos cerrados sin acta:** el código marcó 25 en todo el portafolio, entre ellos PRY-200, 205, 207 y 210. En PRY-200 el cronograma declara los cinco hitos cerrados, y el informe de ese mismo proyecto dice que se reprogramó la salida y reporta 48 % de avance.
- **PRY-208:**
  - La factura FV-1349 (2026-09-05) cobra los dos entregables del contrato. El acta de recibo de la bolsa de horas es del 2026-09-30, así que se facturó antes de recibir. Ese caso lo señalo yo; el código no lo marcó como señal de factura sin entrega.
  - El cronograma v2 mueve la salida 117 días. La solicitud de cambio CC-01 declara los mismos 117 días, pero ningún documento las enlaza. El código la marca como cambio sin línea base.
- **PRY-203:** no tiene cronograma. Su cierre en el acta, 2026-03-16, ya venció, y la solicitud CC-01 dice "autorizada por el comité" sin decir cuál.
- **PRY-205:** el ejecutado supera al comprometido y la proyección supera el presupuesto aprobado.
- **Compromisos de PRY-200:** son 25. Algunos se reprogramaron hasta seis veces y cinco se dieron por entregados sin acta. En la reunión del 2026-10-17 se dijo que el proveedor podría no llegar con el equipo completo, y nadie lo registró como riesgo.
- **Vacíos:** "autoridad" y "fase" no aparecen en ningún documento de los 10 proyectos. El producto falta en PRY-205, 208 y 210 porque sus actas dicen "No aplica".

La ficha `ficha-pm.json` de PRY-200 quedó entera en `pm_record`, sin fusionarla con la mía.

Como hay más de un proyecto, puedo preparar el informe consolidado con `/criterio-portfolio:portfolio-report`.

criterio-portfolio 0.3.13 · Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13