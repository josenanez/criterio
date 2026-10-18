# /criterio-project:pm-setup documentos/proyectos/PRY-200-originación-digital

## Listo — PRY-200 · Originación digital

La configuración está escrita y la verifiqué: `config` devuelve `ok` sin problemas. No hubo interlocutor, así que tomé la respuesta sugerida en cada pregunta.

**Lo que miré:** 15 documentos y 7 minutas, la última del 2026-10-17. Leí las 7 minutas, de la más vieja a la más nueva, más 5 actas de recibo, el informe de avance, el acta de constitución y el cronograma. Todos los formatos se pudieron leer.

**Respuestas sugeridas que tomé:**
- Gerente: Diana Molina, según el acta de constitución.
- Cadencia: comité semanal, los sábados, que es el día en que caen las minutas. Las notas del 17-oct dicen «próxima reunión en dos semanas», así que dejé el 2026-10-31 como próxima reunión. Si la cadencia real es semanal, hay que cambiarlo.
- Estado: `estado/PRY-200-originación-digital`.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.4.0, con fecha 2026-10-17. Mostré el texto corto y lo registré con ese nombre, según tu indicación. El comprobante está en `.criterio/terminos/aceptacion-criterio-project-0.4.0-2026-10-17.md` y `.pdf`. Los SHA-256 empiezan por `99704ec1070b8386` (md) y `0c3de2b80140ee41` (pdf).

### Lo que está abierto, y cuántas veces se ha movido
La ficha tiene 26 compromisos:
- 5 cumplidos con acta de recibo.
- 8 vencidos sin evidencia.
- 3 sin fecha.
- 10 vigentes con fecha.

| Quién | Qué | Para cuándo | Historial |
|---|---|---|---|
| Elena Duarte | Enviar el documento 1 | 2026-12-05 | Reprogramado 6 veces. Primera promesa 09-25; luego 10-09, 10-19, 11-03, 11-11, 11-21 y 12-05. |
| Ricardo Salas | Cerrar la prueba 2 | 2026-11-20 | Reprogramado 4 veces. Su primera fecha fue 09-20; luego 10-09, 10-25, 11-06 y 11-20. |

Las fechas de Elena Duarte salen de las minutas del 09-05 al 10-10 y de las notas del 10-17. Esas notas escriben «05/12/2026» y lo leí como día/mes.

**Vencidos sin evidencia a 2026-10-17:**

| Quién | Qué | Para | Días |
|---|---|---|---|
| Sandra Gil | Validar el ambiente 12 | 09-22 | 25 |
| Carlos Peña | Validar el ambiente 4 | 09-25 | 22 |
| Felipe Arango | Revisar el anexo 11 | 09-29 | 18 |
| María Restrepo | Aprobar el diseño 13 | 10-06 | 11 |
| Gustavo Neira | Cerrar la prueba 18 | 10-08 | 9 |
| Carlos Peña | Entregar el punto 8 | 10-10 | 7 |
| Gustavo Neira | Confirmar la fecha 7 | 10-14 | 3 |
| Carlos Peña | Confirmar la fecha 15 | 10-15 | 2 |

Gustavo Neira dijo el 09-26 que ya entregó «Confirmar la fecha 7». No hay acta, así que no lo cerré.

### Sin fecha
Estos no pueden estar vencidos, y por eso son los que desaparecen de los informes:
- Liliana Torres, «Actualizar la matriz 14». Dijo el 10-03 que ya la entregó; no hay acta.
- María Restrepo, «Entregar el punto 24».
- Laura Vélez, «Mandar el ajuste del presupuesto». Las notas dicen «la otra semana», y no calculé una fecha.

### Otras señales que levantó el cálculo
- **Verde contra la evidencia:** el informe del 10-17 declara verde y 36%. Ese mismo día hay 8 compromisos vencidos, 2 muy reprogramados, un hito vencido y una desviación de costo.
- **Hito vencido:** «Diseño funcional aprobado» era para el 2026-10-05, lleva 12 días de atraso y no hay acta.
- **Costo:** la proyección al cierre supera lo aprobado en 15,9 %.
- **Riesgo dicho y no registrado:** en las notas del 10-17 se comentó que el proveedor podría no llegar con el equipo completo. Nadie lo anotó como riesgo; quedó en la ficha marcado así.

### Qué le falta a tu carpeta
- Actas de recibo de lo que dicen haber entregado (Confirmar la fecha 7 y Actualizar la matriz 14). Sin ellas se ven igual que lo incumplido.
- Un cronograma vigente: solo hay la v1 del 2026-05-28.
- Minutas completas. Las actuales traen solo la tabla de compromisos, sin decisiones ni riesgos.
- Las facultades del gerente y la etapa del proyecto no aparecen en ningún documento.

La ficha no está sellada, porque leí reuniones y actas, no el proyecto entero. `compute` no devolvió `record_issues`. La corrida quedó registrada como `2026-10-17-pm-setup-1`, y la salida completa está en `estado/PRY-200-originación-digital/corridas/salida-pm-setup.md`. Hice cero preguntas y no medí los minutos hasta el primer resultado.