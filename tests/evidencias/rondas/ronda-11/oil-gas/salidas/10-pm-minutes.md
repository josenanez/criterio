# /criterio-project:pm-minutes documentos/proyectos/PRY-200-campaña-de-perforación-del-bloque-sur/2026-10-22-notas-reunion.txt

# Acta — Campaña de perforación del bloque sur (PRY-200) · 2026-10-22

**Términos:** ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-22), así que no registré nada nuevo.

**Asistieron (11):** Beatriz Cuéllar, Carlos Peña, Elena Duarte, Javier Hoyos, Jorge Medina, Laura Vélez, María Restrepo, Paula Céspedes, Ricardo Salas, Rubén Cárdenas y Óscar Ramírez.

**Fuente:** `2026-10-22-notas-reunion.txt`, 8 líneas. Las notas no traen agenda, así que no sé qué ausentes tenían tema. Cinco personas con compromisos abiertos no asistieron y nadie las mencionó: Felipe Arango, Camilo Beltrán, Liliana Torres, Mauricio Pérez y Natalia Ospina.

## Compromisos
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Ricardo Salas | Enviar el documento 1 | 2027-01-15 | **Reprogramado por 6.ª vez.** La promesa original era el 2026-09-30. Es la fecha más lejana hasta ahora, 107 días después de la original. |
| Óscar Ramírez | Revisión con el proveedor | 2026-11-01 | Nuevo. El 2026-11-01 es domingo. |

### Sin fecha
| Quién | Qué |
|---|---|
| Laura Vélez | Mandar el ajuste del presupuesto. Dijo «la otra semana», que no es una fecha, y no le puse una. |

Con este, la ficha tiene 3 compromisos sin fecha. Los otros dos son de Camilo Beltrán («punto 8», desde el 09-17) y de Rubén Cárdenas («punto 16», desde el 10-01).

## Decisiones
Ninguna. Las notas no registran una decisión con quién la tomó y qué se descartó.

## Quedó sin decidir
- **Documento 1 de Ricardo Salas:** nadie decidió qué hacer con un compromiso reprogramado 6 veces. La facultad no está dicha en las notas; podría ser el patrocinador, Paula Céspedes, que estuvo presente, o el comité.
- **Retraso del proveedor:** se comentó, pero nadie lo anotó como riesgo.

## Intenciones sin doliente
Ninguna.

## Dicho al pasar y no registrado
| Qué | Quién | Categoría | Ya estaba en el RAID |
|---|---|---|---|
| «el proveedor podría no llegar con el equipo completo para la siguiente fase» | Las notas no lo atribuyen | Riesgo, sin probabilidad, impacto, doliente ni fecha | **No.** El riesgo más cercano («el proveedor no ha confirmado la fecha de la última entrega», informe del 10-19) trata otra cosa. Entra a la ficha hoy con `owner: no_declarada`. |

## Cerrado en esta reunión
Nada. Ninguna frase de las notas se apoya en un documento.

## Lo que esta reunión contradice
| Campo | Dijo la reunión | Dice el expediente |
|---|---|---|
| Cadencia del comité | «próxima reunión en dos semanas» (alrededor del 2026-11-05) | La configuración dice comité semanal, y las seis reuniones previas (del 09-10 al 10-15) fueron semanales. |

La fecha de próximo comité coincide con la configuración (2026-11-05); lo que no coincide es la cadencia. Si el comité pasó a quincenal, la configuración está vieja. Ningún campo del acta de constitución cambia en esta reunión.

## Sin resolver de la transcripción
- «lo de “enviar el documento 1” no alcanzó»: no dice qué no alcanzó.
- «el proveedor podría no llegar…»: no dice qué proveedor, qué «siguiente fase» ni quién lo comentó.
- «queda para el 2026-11-01»: no queda claro si es la fecha de la revisión o la de entregar su resultado. Registré la fecha de la revisión.

## Cálculo
Corrí `compute` y no trajo `record_issues`. Salen 17 alertas:
- **Compromisos:** 8 vencidos, 3 sin fecha y 2 reprogramados 3 veces o más (documento 1: 6; prueba 2: 5).
- **Informe del 10-19:** declara verde, pero 4 señales lo contradicen.
- **Esta reunión:** no movió ningún vencido. Laura Vélez, Óscar Ramírez y Elena Duarte tenían vencidos y estaban presentes, y las notas no dicen nada sobre ellos.

**El acta la guardas tú:** no la escribí en `30-reuniones`. Quedó en esta conversación y en `estado/PRY-200-campaña-de-perforación-del-bloque-sur/corridas/salida-pm-minutes.md`. La corrida quedó registrada como `2026-10-23-pm-minutes-1`.

Siguientes pasos: `/pm-commitments` para el seguimiento completo, y `/pm-publish` si quieres que la PMO vea el riesgo nuevo en la ficha.