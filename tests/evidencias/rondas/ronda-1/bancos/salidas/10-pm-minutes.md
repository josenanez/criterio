# /criterio-project:pm-minutes documentos/proyectos/PRY-202-migración-a-la-nube/2026-10-13-notas-reunion.txt

# Acta — Migración a la nube (PRY-202) · 2026-10-13

Los términos ya estaban aceptados en la configuración: versión 1.0, José Francisco Ñáñez, 2026-10-14. Coincide con la versión de `TERMS.md`.

**Asistieron (según las notas):** Paula Céspedes, Rubén Cárdenas, Sandra Gil, Laura Vélez, Óscar Ramírez.
**Fuente:** `2026-10-13-notas-reunion.txt`, cruzada con `30-reuniones/2026-10-13-comite-semanal.docx`.
**Ausentes con tema en agenda:** no se puede saber, porque las notas no traen agenda.

## Compromisos
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Paula Céspedes | Entregar el punto 3 | 28/10/2026 según las notas · 2026-11-02 según el acta del comité | Fecha en conflicto. No se cuenta como reprogramado, con 0 reprogramaciones registradas. Las notas dicen que «no alcanzó», pero no hay ninguna promesa anterior en los documentos leídos. |
| Óscar Ramírez | Revisión con el proveedor | 2026-10-24 | El 24/10/2026 es sábado. Lo anoto y no lo corrijo. |

### Sin fecha
| Quién | Qué |
|---|---|
| Laura Vélez | Mandar el ajuste del presupuesto. Dijo «la otra semana», así que queda `due_date: no_declarada`. |

## Decisiones
Ninguna. Las notas no registran que alguien decidiera algo ni qué se descartó.

## Quedó sin decidir
Nada. Las notas no plantean ningún punto como decisión pendiente, y no invento uno.

## Intenciones sin doliente
Ninguna. Rubén Cárdenas asistió, pero no aparece con ninguna intervención.

## Dicho al pasar y no registrado
| Qué | Quién lo dijo | Categoría | Ya estaba en el RAID |
|---|---|---|---|
| «El proveedor podría no llegar con el equipo completo para la siguiente fase» | No atribuido: las notas dicen «se comentó» | Riesgo | **No.** El informe del 2026-10-09 lista otros dos riesgos: el equipo de seguridad y el calendario de liberaciones del core. |

Queda en la ficha con probabilidad, impacto y doliente sin declarar.

## Cerrado en esta reunión
Nada. Sin documento que cierre algo, la sección se omite.

## Lo que esta reunión contradice
| Campo | Dijo la reunión | Dice el expediente | Fuente y fecha de cada uno |
|---|---|---|---|
| Fecha de Paula Céspedes | 2026-10-28 | 2026-11-02 | Notas y acta del comité, ambas del 2026-10-13. Ninguna anula a la otra. |
| Asistentes | Paula, Rubén, Sandra, Laura, Óscar | Sandra Gil y Camilo Beltrán | Notas y acta del comité, ambas del 2026-10-13. Camilo (patrocinador) no figura en las notas. No es seguro que sean la misma sesión. |
| Próxima reunión | «en dos semanas» (≈ 2026-10-27) | Comité semanal, próximo 2026-10-20 | Notas, 2026-10-13 · configuración local, 2026-10-14 |
| Fecha de cierre | Todos los compromisos caen después del cierre | Cierre 2026-10-16 | Observación mía, no dicha en la reunión. Acta de constitución, 2026-02-19. No hay documento de replanificación. |

## Sin resolver de la transcripción
- «lo de "entregar el punto 3" no alcanzó, se compromete para el 28/10/2026»: no se sabe qué no alcanzó ni cuál era la fecha anterior.
- «Óscar Ramírez: revisión con el proveedor, queda para el 2026-10-24»: no queda claro si Óscar se compromete a hacerla o si solo se anota la fecha de una cita.
- «la otra semana» (Laura Vélez): es relativo al 13/10 y no fija fecha.
- Quién comentó lo del proveedor.

---
**Recálculo (`compute`):** salió 1 alerta, `commitment_undated` (Laura Vélez), con 0 vencidos y 0 reprogramados. El cálculo no detecta el conflicto de fecha de Paula, así que lo declaro aquí. La ficha `PRY-202.json` ya traía estos tres compromisos y el riesgo, por eso no la modifiqué.

La corrida quedó registrada como `2026-10-14-pm-minutes-1`, y la salida está en `estado/PRY-202-migración-a-la-nube/corridas/salida-pm-minutes.md`.

**Siguiente:** `/pm-commitments` para el seguimiento completo. `/pm-publish` no hace falta por ahora, porque ningún campo de la ficha cambió.