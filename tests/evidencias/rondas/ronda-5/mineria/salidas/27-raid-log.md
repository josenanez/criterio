# /criterio-portfolio:raid-log portafolio

Levanté el RAID del portafolio sobre las 13 fichas (PRY-199 a PRY-211). El resultado: 40 ítems y ninguno tiene doliente, fecha, probabilidad, impacto ni fecha de último movimiento.

**Qué incluye**
- **Conteo:** hay 23 riesgos y 17 incidencias. No hay supuestos ni dependencias: ninguna ficha trae dependencias, y las actas de PRY-199, 201, 210 y 211 dicen «Ninguna declarada».
- **Sin doliente ni fecha:** los 40 ítems salen solo de las listas de «Riesgos abiertos» y de hallazgos de los informes de avance. Lo reporté como hallazgo y no rellené nada.
- **Escalamiento:** no pude aplicar tres de los cinco criterios (dos períodos sin movimiento, doliente externo sin respuesta, mitigación vencida), porque no hay fechas con qué medirlos. Eso no significa que no haya problemas.
- **Riesgo no registrado:** hay uno solo. En las notas del 2026-10-16 de PRY-200 se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase, y nadie lo anotó como riesgo. Probablemente sea el mismo problema que el riesgo ya registrado en ese proyecto (el proveedor no ha confirmado la fecha de la última entrega). Los demás comités son tablas de compromisos y no contienen riesgos dichos al pasar. No inventé ninguno.
- **Reclasificar como dependencia:** 13 ítems hoy están como riesgo.
  - 7 son «el proveedor no ha confirmado la fecha de la última entrega» (PRY-200, 201, 203, 206, 207, 209 y 210).
  - 6 son «ventana de parada de planta definida por operaciones» (PRY-199, 202, 203, 205, 208 y 210).
  - En ambos casos se depende de alguien fuera del proyecto. La contraparte es el proveedor o operaciones, no un proyecto del portafolio, así que no puse código PRY.
- **Parada de planta reprogramada:** en PRY-202 y PRY-210 el riesgo de la ventana sigue abierto y el mismo informe ya reporta que se reprogramó la parada. Es una inferencia mía: el riesgo parece haberse cumplido, y cada gerente debe confirmarlo.
- **Frases repetidas:** los 40 ítems usan solo 12 frases distintas, repetidas casi textuales entre proyectos (por ejemplo, las lluvias que detuvieron el montaje aparecen en PRY-200, 208 y 211). Puede ser lenguaje de plantilla, así que conviene verificarlo con los gerentes antes del comité.

**Pendiente de su decisión:** si quiere que suba a comité los dos puntos de «necesitan decisión» (formalizar el riesgo no registrado de PRY-200 y revisar la parada de planta en PRY-202 y PRY-210). También puedo proponer un doliente por ítem; propongo, no asigno.

**Términos y corrida:** los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no registré una aceptación nueva. La corrida quedó registrada como `2026-10-16-raid-log-1`.

Archivos en `/home/claude/banco/ronda-5/mineria/espacio/estado/corridas`:
- `salida-raid-log.md`
- `2026-10-16-raid-log-1.md`