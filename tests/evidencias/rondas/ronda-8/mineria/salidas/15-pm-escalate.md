# /criterio-project:pm-escalate 

Armé el paquete de escalamiento de PRY-201 y dejé la corrida registrada. Al ser una sesión sin interfaz, no hubo tema indicado y tomé lo que el informe de la semana ya marcaba como escalable.

Los términos (v1.1) ya estaban vigentes a nombre de José Francisco Ñáñez, 2026-10-17, así que no los volví a pedir.

**Puntos del paquete**
1. **Autoridad no declarada.** El acta del 2026-03-06 no dice qué decide el gerente ni quién aprueba cambios. Va primero. Todo lo demás supone que decide el Comité de Operaciones, y eso es inferencia mía, no un dato del acta.
2. **CC-01** (+96 días, +192.000.000 COP).
   - La solicitud sigue "pendiente de presentación al comité". Aun así, el cronograma v2 ya pone el cierre en 2027-05-10, sobre la base del 2027-02-03.
   - La solicitud no describe qué componentes agrega, ni motivo, ni desglose del costo.
   - Opciones: aprobar, rechazar o devolver con plazo. Recomiendo aprobar solo si traen el detalle del alcance y dicen si la proyección ya incluye los 192 millones; si no, devolver con fecha.
3. **Dos compromisos reprogramados más de tres veces.** Paula Céspedes (6) y María Restrepo (5). La pregunta es si se mantienen como fechas firmes o se reasignan.

**Lo que el paquete no sabe**
- **Fecha de consecuencia.** Los documentos no traen fecha en que la falta de decisión cueste algo. No la inventé; la tiene que poner Mauricio Pérez, porque sin ella el punto se aplaza.
- **Cálculo de impacto.** `impact` aplicó los 96 días sobre un cierre que ya los incluye y dio 2027-08-14, lo que cuenta el cambio dos veces. No usé esa cifra; la correcta es 2027-05-10.
- **Otros proyectos.** No encontró ninguno alcanzado, pero el estado solo contiene PRY-201, así que no puedo afirmar que no haya.
- **Próximo comité.** La configuración dice 2026-10-24 y las notas dicen "en dos semanas" (2026-10-31). Hay que confirmar a cuál se lleva.

Archivos en `/home/claude/banco/ronda-8/mineria/espacio/estado/PRY-201-ampliación-de-la-relavera/corridas/`:
- `salida-pm-escalate.md`
- `2026-10-17-pm-escalate-1.md` (la corrida: 66 s, 1 proyecto, 14 señales abiertas)

Llevar el paquete al comité es de Mauricio Pérez. Este comando no escala ni decide solo.