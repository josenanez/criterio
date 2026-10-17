# /criterio-project:pm-minutes documentos/proyectos/PRY-201-ampliación-de-la-relavera/2026-10-17-notas-reunion.txt

# Acta — Ampliación de la relavera (PRY-201) · 2026-10-17
**Asistieron:** Andrés Lozano, Felipe Arango, Gustavo Neira, Javier Hoyos, Jorge Medina, Laura Vélez, Liliana Torres, María Restrepo, Mauricio Pérez, Paula Céspedes, Sandra Gil, Óscar Ramírez (12, los mismos del comité del 2026-10-10). **Fuente:** `2026-10-17-notas-reunion.txt`. **Ausentes con tema en agenda:** ninguno, porque las notas no traen agenda.

**Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrar nada nuevo. Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

## Compromisos
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Paula Céspedes | Enviar el documento 1 | 2026-11-26 | **Reprogramado 6 veces.** Original 2026-09-14; luego 09-22, 10-12, 10-21, 11-01, 11-12 y 11-26. Las notas dicen «no alcanzó» y «se compromete para el 26/11/2026». |
| Óscar Ramírez | Revisión con el proveedor | 2026-10-27 | Nuevo |

### Sin fecha
| Quién | Qué |
|---|---|
| Laura Vélez | Mandar el ajuste del presupuesto. «La otra semana» no es una fecha y no le calculé una. |

## Decisiones
Ninguna. Las notas no registran ninguna.

## Quedó sin decidir
| Qué | Por qué | Quién tiene la facultad |
|---|---|---|
| Si el riesgo del proveedor se registra y quién lo lleva | Las notas dicen «nadie lo anotó como riesgo» | No consta en los documentos |

## Intenciones sin doliente
Ninguna.

## Dicho al pasar y no registrado
| Qué | Quién lo dijo | Categoría | ¿Ya estaba en el RAID? |
|---|---|---|---|
| «El proveedor podría no llegar con el equipo completo para la siguiente fase» | No consta; las notas dicen «se comentó» | Riesgo | No. El informe del 2026-10-09 registra otro, «el proveedor no ha confirmado la fecha de la última entrega», que habla de la fecha y no del equipo completo. Queda en la ficha sin responsable. |

## Cerrado en esta reunión
Nada. No se presentó ningún documento.

## Lo que esta reunión contradice
| Campo | Dijo la reunión | Dice el expediente | Fuente |
|---|---|---|---|
| Próximo comité | «En dos semanas» (2026-10-31) | Semanal, próximo 2026-10-24 | Notas 2026-10-17 y `config.json` |

La cadencia es un dato de la configuración, no de la ficha. La dejé sin cambiar hasta que confirmes cuál rige.

## Sin resolver de la transcripción
- «Lo de enviar el documento 1 no alcanzó»: el plazo vigente era 2026-11-12, que aún no llega. No queda claro a qué plazo se refiere.
- «Revisión con el proveedor, queda para el 2026-10-27»: no dice si es una reunión o un entregable, ni si había una fecha previa.
- «Se comentó…»: sin autor, no se sabe quién advirtió el riesgo.
- Las notas no mencionan los otros 20 compromisos abiertos. No los di por cumplidos ni por reprogramados.

## Recálculo
`compute` no trae incidencias de la ficha (`record_issues`). Corregí un dato mío: la «Revisión con el proveedor» tenía `original_due_date: no_declarada` y ahora es 2026-10-27, porque tuvo fecha desde la primera vez.

Con la ficha completa hay 26 compromisos, de los cuales 22 están abiertos:
- **Vencidos sin acta (6):** matriz 6 (32 días), punto 8 (15), ambiente 20 (9), anexo 19 (6), punto 24 (4) y diseño 5 (2).
- **Sin fecha (2):** anexo 11 y el ajuste del presupuesto.
- **Reprogramados 5 veces o más (2):** documento 1 y prueba 2.

El informe del 2026-10-09 declara verde y el cálculo lo contradice.

Pendiente de revisar: «Cerrar la prueba 18» (Javier Hoyos) y «Entregar el punto 8» (Óscar Ramírez) también traen `original_due_date: no_declarada` con una fecha puesta después. Eso viene de minutas anteriores y no lo toqué.

## Después
Puedes correr `/pm-commitments` para el seguimiento completo. `/pm-publish` no hace falta, porque esta reunión no cambió ningún campo de la ficha. El acta sale aquí y la guardas tú; no la escribí en tu carpeta de reuniones.

La corrida quedó registrada como `2026-10-17-pm-minutes-1` (14 hallazgos, 33 segundos), con esta acta en `estado/PRY-201-ampliación-de-la-relavera/corridas/salida-pm-minutes.md`.