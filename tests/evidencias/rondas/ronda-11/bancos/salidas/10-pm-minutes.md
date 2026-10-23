# /criterio-project:pm-minutes documentos/proyectos/PRY-206-billetera-y-qr/2026-10-23-notas-reunion.txt

# Acta — Billetera y QR (PRY-206) · 2026-10-23

**Asistieron:** Andrés Lozano, Beatriz Cuéllar, Camilo Beltrán, Carlos Peña, Gustavo Neira, Javier Hoyos, Jorge Medina, Laura Vélez, Liliana Torres, María Restrepo, Paula Céspedes, Ricardo Salas, Rubén Cárdenas, Sandra Gil, Óscar Ramírez.

**Fuente:** `2026-10-23-notas-reunion.txt`, que son 5 líneas de notas, no una transcripción.

**Ausentes con tema en agenda:** no hay agenda escrita. La única persona con compromiso abierto que no estuvo es Diana Molina («Actualizar la matriz 6», sin fecha desde el 2026-09-18).

**Términos:** ya estaban vigentes para la versión 0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23. No hizo falta registrarlos otra vez.

## Compromisos
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Camilo Beltrán | Cerrar la prueba 2 | 2027-01-09 | **Reprogramado por 6.ª vez.** Original 2026-10-07; luego 10-25, 11-10, 11-24, 12-13, 12-26 y 2027-01-09. Cita: «no alcanzó, se compromete para el 09/01/2027». |
| Óscar Ramírez | Revisión con el proveedor | 2026-11-02 | Nuevo. Las notas no dicen de cuál proveedor se trata (hay dos: Integra Sistemas, CT-360, y Talento Digital, CT-127). |

### Sin fecha
| Quién | Qué |
|---|---|
| Laura Vélez | Mandar el ajuste del presupuesto. Cita: «la otra semana». Eso no es una fecha y no se le puso una. |

## Decisiones, sin decidir, intenciones sin doliente
Ninguna en las notas.

## Dicho al pasar y no registrado
| Qué | Quién lo dijo | Categoría | Ya estaba en el RAID |
|---|---|---|---|
| El proveedor podría no llegar con el equipo completo para la siguiente fase | No se sabe: «se comentó» no tiene autor | Riesgo | No estaba en ningún documento del proyecto. Lo más cercano es «el proveedor no ha confirmado la fecha de la última entrega» (informe del 2026-10-20), que es otra cosa. Queda en la ficha **sin dueño**. |

## Cerrado en esta reunión
Nada. Las notas no traen ningún documento que cierre un compromiso.

## Lo que esta reunión contradice
Nada contra el expediente.

Una observación sobre la cadencia: «próxima reunión en dos semanas» (2026-11-06) coincide con `committee_next`. Pero el comité está configurado como semanal y las seis minutas anteriores son de viernes consecutivos.

## Sin resolver de la transcripción
- **«09/01/2027»:** lo leí día/mes (9 de enero de 2027), como el resto de las fechas del proyecto. Leído mes/día sería el 1 de septiembre de 2027, después del cierre del proyecto (2027-01-25). Hay que confirmarlo con Camilo Beltrán.
- **«La otra semana»** (Laura Vélez): sin fecha.
- **«El proveedor»:** sin nombre, tanto en el compromiso de Óscar Ramírez como en el riesgo.
- **«Se comentó…»:** sin autor, así que no se puede atribuir.
- **Compromisos que vencían hoy:** las notas no dicen nada de Andrés Lozano («Revisar el anexo 19») ni de Ricardo Salas («Confirmar la fecha 23»), ambos con fecha 2026-10-23. Sin nota ni documento, siguen abiertos.

## Recálculo
`compute` no devolvió `record_issues`. La ficha ya tenía todas estas entradas desde `/pm-setup`, que leyó las mismas notas. El acta no la cambió.

- **4 compromisos vencidos.**
- **3 sin fecha:** Diana Molina, Beatriz Cuéllar y Laura Vélez.
- **3 movidos tres veces o más:** Ricardo Salas ×4, Camilo Beltrán ×6 y Beatriz Cuéllar ×5.
- **Estado declarado:** el informe del 2026-10-20 sigue en verde, contradicho por esas señales.

## Siguiente paso
`/pm-commitments` para ver el seguimiento completo. No hace falta `/pm-publish`, porque ningún campo de la ficha cambió.

El acta sale aquí en la conversación y la guardas tú. No escribí nada en tu carpeta de reuniones. El texto está también en `estado/PRY-206-billetera-y-qr/corridas/salida-pm-minutes.md`, y la corrida quedó registrada como `2026-10-23-pm-minutes-1`.