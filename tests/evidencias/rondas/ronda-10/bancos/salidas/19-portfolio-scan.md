# /criterio-portfolio:portfolio-scan 

El barrido escribió y selló 10 fichas nuevas (PRY-199, 200, 201, 202, 204, 205, 206, 207, 208 y 211). Las otras 3 (PRY-203, 209 y 210) no cambiaron y no las abrí.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo.
- **Lectura:** de 77 documentos leí 60. Los 77 se convirtieron a texto y ninguno resultó ilegible. Los proyectos se leyeron uno tras otro, sin subagentes.
- **`entrada/`:** no existe en la documentación, así que no moví nada.
- **Notas de PRY-201:** `2026-10-18-notas-reunion.txt` está suelta en la raíz de la carpeta del proyecto. La leí donde está y propongo moverla a `30-reuniones/`.
- **Campos sin dato:** `authority` y `phase` en las 10 fichas, y `product` en PRY-202, 205 y 208 (sus actas dicen «No aplica»). PRY-204 no tiene cronograma.

Hallazgos que levantó el código:

- **Total:** 67 hallazgos.
- **Hitos:** 23 cerrados sin acta de recibo que los pruebe. Los registré como cumplidos con la evidencia vacía.
- **Compromisos:** 10 vencidos, 3 reprogramados y 2 sin fecha.
- **PRY-201:** 25 compromisos con su historial. Uno lleva 6 reprogramaciones.
- **Riesgo sin registrar:** las notas del 2026-10-18 dicen que el proveedor podría no llegar con el equipo completo y nadie lo anotó. Lo levanté en `raid.risks`.
- **PRY-202:** el contrato CT-812 y la factura FV-1812 (614.970.173 COP) dan dos señales: facturado por encima de lo aceptado y un entregable aceptado sin acta.
- **PRY-204, 207 y 211:** tienen solicitudes de cambio CC-01 autorizadas por el comité. En 204 no hay cronograma que las refleje, y en 207 y 211 las registré como línea base v2.

Un detalle de las cifras: el registro de la corrida cuenta 77 documentos como «sin cambio», porque lo calculó después de sellar las fichas. El número de lectura real es 60 de 77.

El informe consolidado puede salir con `/criterio-portfolio:portfolio-report`.

Archivos en `estado/`:
- `records/` (las 10 fichas nuevas)
- `corridas/salida-portfolio-scan.md`
- `snapshots/2026-10-18.json`
- `corridas.json` (la corrida registrada)