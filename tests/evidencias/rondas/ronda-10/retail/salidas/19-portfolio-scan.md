# /criterio-portfolio:portfolio-scan 

Barrido terminado: 10 fichas escritas y selladas (PRY-199 a PRY-208), con 68 de los 83 documentos leídos. Los otros 15 pertenecen a PRY-209, PRY-210 y PRY-211, que no cambiaron.

- **Términos:** ya estaban vigentes (v1.1, José Francisco Ñáñez, 2026-10-18), así que no registré una aceptación nueva.
- **Sin pérdidas:** no hubo archivos ilegibles. No existe carpeta `entrada/`, así que no moví nada. El `.txt` suelto de PRY-206 lo leí donde está.
- **Ficha del gerente de PRY-206:** la guardé aparte en `pm_record`, sin mezclarla con mi lectura de los documentos. El contraste entre las dos lo calcula el script.
- **Hallazgos:** el script cuenta 63 sobre los 13 proyectos. Los grupos más grandes son 21 hitos cerrados sin acta, 9 compromisos vencidos, 7 de avance contra plan y 6 entregables de proveedor tarde.
- **Facturas:**
  - PRY-201: se facturó más de lo aceptado.
  - PRY-206: se facturó un contrato (CT-980) sin ningún entregable entregado.
  - PRY-206: la solicitud de cambio CC-01 aparece sin línea base asociada. Está «autorizada por el comité», sin decir cuál ni quién firmó.
- **Compromisos de PRY-206:** hay 6 vencidos. «Enviar el documento 1» lleva seis reprogramaciones, de 2026-09-13 a 2026-12-03.
- **Despliegue sin fecha nueva:** seis informes dicen que se reprogramó el despliegue, pero ningún cronograma posterior a v1 recoge la fecha nueva.
- **Campos sin dato:** autoridad y fase en las diez fichas; producto en PRY-202, 203 y 206; lo facturado de CT-199.

El informe consolidado queda a un paso con `/criterio-portfolio:portfolio-report`.

Todo está en `/home/claude/banco/ronda-10/retail/espacio/estado/`:
- `corridas/salida-portfolio-scan.md`
- `records/`
- `snapshots/2026-10-18.json`

Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal