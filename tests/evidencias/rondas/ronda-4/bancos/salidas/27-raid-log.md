# /criterio-portfolio:raid-log portafolio

**Registro RAID del portafolio, 2026-10-15** (13 proyectos, PRY-199 a PRY-211)

Los 35 ítems que ya estaban registrados llegaron sin doliente, sin fecha, sin probabilidad y sin impacto. No los rellené. Salen de las listas de «riesgos abiertos» de los informes de avance. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.

- **Conteo:** 15 riesgos, 14 incidencias, 6 dependencias y 0 supuestos. Hay además 1 riesgo no registrado.
- **Reclasificados:** 6 de los 21 «riesgos» registrados son en realidad dependencias.
  - 5 corresponden a «El proveedor no ha confirmado la fecha de la última entrega» (PRY-200, 201, 202, 204 y 205).
  - 1 corresponde a «Dependencia del calendario de liberaciones del core» (PRY-208).
- **No registrado:** en las notas del 2026-10-15 de PRY-210 se dice que el proveedor podría no llegar con el equipo completo a la siguiente fase y que «nadie lo anotó como riesgo». Es el único que encontré. Las minutas de PRY-199 a PRY-209 solo traen compromisos.
- **Para el comité del 2026-10-22:** subiría ese riesgo y la dependencia del proveedor sin confirmar, con la pregunta «¿quién confirma y para cuándo?». Del resto no puedo decir que cumpla un criterio de escalamiento, porque no hay doliente, fecha ni movimiento con qué medirlo.
- **No pude cruzar dependencias entre proyectos:** ningún documento dice qué proyecto es «el core». PRY-201 se llama «Core de depósitos», pero eso es solo coincidencia de nombre. Las actas de PRY-201, 207 y 208 dicen «Ninguna declarada» en dependencias, y PRY-208 aun así dice depender del core.
- **Texto repetido:** las mismas ocho frases aparecen en los 13 proyectos. Puede ser una plantilla de informe, y cada gerente tendría que confirmar que su riesgo es real.
- **Compromisos que se corren en PRY-210:** «Enviar el documento 1» pasó del 2026-09-17 al 2026-12-08, y «Confirmar la fecha 7» del 2026-10-02 al 2026-11-27. No son RAID, pero si bloquean algo, ese riesgo no está registrado.
- **No propuse dolientes:** no hay base en los documentos para hacerlo.

No leí el contenido de los `.docx`, `.pdf` y `.xlsx` más allá de lo que ya traían las fichas. Tampoco sé si hubo riesgos dichos en reuniones que no quedaron en minuta.

La corrida quedó registrada como `2026-10-15-raid-log-1` (85 segundos, 13 proyectos, caso PRY-210). El script no pudo medir el número de documentos. La salida completa, con las tablas y el registro ítem por ítem, está en `estado/corridas/salida-raid-log.md`.