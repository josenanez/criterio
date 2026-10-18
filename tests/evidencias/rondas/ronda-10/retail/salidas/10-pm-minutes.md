# /criterio-project:pm-minutes documentos/proyectos/PRY-206-precios-dinámicos/2026-10-18-notas-reunion.txt

# Acta — Precios dinámicos (PRY-206) · 2026-10-18

**Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-18), así que no hubo que registrar nada.

**Asistieron (14):** Andrés Lozano, Carlos Peña, Diana Molina, Gustavo Neira, Javier Hoyos, Jorge Medina, Laura Vélez, Liliana Torres, Mauricio Pérez, Paula Céspedes, Ricardo Salas, Rubén Cárdenas, Sandra Gil y Óscar Ramírez.
**Fuente:** `2026-10-18-notas-reunion.txt` (9 líneas).
**Ausentes con tema en agenda:** las notas no traen agenda, así que no se puede decir. Estuvieron en el comité del 10-11 y hoy no: María Restrepo, Beatriz Cuéllar (tiene un compromiso abierto sin fecha) y Camilo Beltrán.

## Compromisos
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Liliana Torres | Enviar el documento 1 | 2026-12-03 | **Reprogramado por 6.ª vez.** Original 09-13; luego 09-30, 10-09, 10-16, 11-02, 11-19 y ahora 12-03. Cita: «no alcanzó, se compromete para el 03/12/2026» (línea 4). |
| Óscar Ramírez | Revisión con el proveedor | 2026-10-28 | Nuevo. No dice de cuál proveedor; hay dos con contrato, CT-847 y CT-980 (línea 6). |

### Sin fecha
| Quién | Qué |
|---|---|
| Laura Vélez | Mandar el ajuste del presupuesto. Cita: «la otra semana» (línea 5). No se le calculó una fecha. |

Siguen abiertos sin fecha desde reuniones anteriores Paula Céspedes (*Validar el ambiente 20*) y Beatriz Cuéllar (*Confirmar la fecha 23*). En total son 3.

## Decisiones, sin decidir e intenciones sin doliente
No hay ninguna. Las notas no registran una decisión con quién la tomó ni qué se descartó, y tampoco hay frases del tipo «tecnología lo revisa».

## Dicho al pasar y no registrado
| Qué | Quién lo dijo | Categoría | Ya estaba en el RAID |
|---|---|---|---|
| «el proveedor podría no llegar con el equipo completo para la siguiente fase, nadie lo anotó como riesgo» (línea 7) | No consta (la nota dice «se comentó») | Riesgo | No. Ninguno de los tres riesgos de la ficha menciona al proveedor. Ya quedó en la ficha, sin probabilidad, impacto ni dueño. |

La nota no dice de cuál proveedor habla. Como contexto, sin concluir nada:
- CT-847 tiene 2 entregables vencidos sin recibo.
- CT-980 tiene 2 vencidos y 599.677.238 COP facturados sin ningún entregable aceptado.

## Cerrado en esta reunión
Nada.

## Lo que esta reunión contradice
| Campo | Dijo la reunión | Dice el expediente | Fuente |
|---|---|---|---|
| Cadencia del comité | «próxima reunión en dos semanas» (≈ 11-01) | `cycle.committee: weekly` | notas 10-18 · configuración |

La fecha coincide con `committee_next: 2026-11-01`, pero no con «weekly». Si el comité pasó a ser quincenal, hay que actualizar la configuración.

## Sin resolver de la transcripción
- «03/12/2026» lo leí como 3 de diciembre. Como el 12 de marzo ya habría pasado, es la lectura que cuadra. Conviene confirmarlo con Liliana Torres.
- «la otra semana» no es una fecha.
- «el proveedor» aparece sin nombre en dos líneas, y puede ser el mismo en las dos o no.
- La línea 7 no dice quién lo dijo.

---
**Recalculado:** `compute` no trae `record_issues`. La ficha ya traía lo de esta reunión, porque `pm-setup` había leído las mismas notas, y la revisé contra la fuente sin cambiarla.

Compromisos vencidos sin evidencia (6):
- Javier Hoyos, dos.
- Jorge Medina.
- Ricardo Salas.
- Liliana Torres, *matriz 14*.
- Sandra Gil.

Hay 3 compromisos sin fecha. Dos están reprogramados 3 veces o más: Torres 6 y Céspedes 5. La ficha suma 22 hallazgos.

**Registro de la corrida:** `estado/PRY-206-precios-dinámicos/corridas/2026-10-18-pm-minutes-1.md`, con la salida completa en `salida-pm-minutes.md` de la misma carpeta.

**Después:** `/pm-commitments` para el seguimiento completo. `/pm-publish` no hace falta por esta acta, porque ningún campo de la ficha oficial cambió. El acta sale aquí y la guardas tú; no escribí nada en `30-reuniones`.