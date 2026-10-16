# /criterio-project:pm-minutes documentos/proyectos/PRY-209-migración-del-erp/2026-10-16-notas-reunion.txt

# Acta — Migración del ERP (PRY-209) · 2026-10-16

**Asistieron (12):** Andrés Lozano, Carlos Peña, Diana Molina, Elena Duarte, Felipe Arango, Javier Hoyos, Laura Vélez, Liliana Torres, Mauricio Pérez, Natalia Ospina, Paula Céspedes y Óscar Ramírez.
**Fuente:** `2026-10-16-notas-reunion.txt`, cinco líneas de notas sin transcripción.
**Ausentes con tema en agenda:** no se puede saber, porque las notas no traen agenda.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los pedí de nuevo. `/pm-setup` ya había leído estas notas y su contenido estaba en la ficha. Esta corrida lo cruzó y lo recalculó, y no cambió nada en `estado/`.

## Compromisos
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Natalia Ospina | Enviar el documento 1 | 2026-11-25 | **Reprogramado por 6.ª vez.** Fechas: 09-20 (original), 09-29, 10-08, 10-19, 11-03, 11-11 y 11-25. Son 66 días sobre la promesa original. Supera el umbral de 3 reprogramaciones. La nota dice: «lo de "enviar el documento 1" no alcanzó». |
| Óscar Ramírez | Revisión con el proveedor | 2026-10-26 | Es nuevo y esta es su primera fecha. Ver *Sin resolver*. |

### Sin fecha
| Quién | Qué |
|---|---|
| Laura Vélez | Mandar el ajuste del presupuesto. Dijo «la otra semana», que no es una fecha. Queda como `no_declarada` con ese texto. |

Hay otros dos compromisos sin fecha que esta reunión no tocó: Carlos Peña, «Validar el ambiente 12», y Javier Hoyos, «Validar el ambiente 20». En total son 3 sin fecha.

## Decisiones
Ninguna. Las notas no registran que alguien decidiera algo.

## Quedó sin decidir
Las notas no dicen qué quedó abierto. Solo se puede afirmar que el ajuste del presupuesto está pendiente y sin fecha, y que nadie decidió nada sobre el proveedor.

## Intenciones sin doliente
Ninguna.

## Dicho al pasar y no registrado
| Qué | Quién | Categoría | ¿Ya estaba en el RAID? |
|---|---|---|---|
| «El proveedor podría no llegar con el equipo completo para la siguiente fase». Las notas añaden que nadie lo anotó como riesgo. | No consta («se comentó») | Riesgo | No como tal. El informe del 10-12 tiene uno cercano pero distinto: «el proveedor no ha confirmado la fecha de la última entrega». La ficha ya tiene la entrada nueva con `owner: no_identificado`, y nadie la ha aceptado. |

## Cerrado en esta reunión
Nada. Las notas no traen ningún documento que cierre un compromiso.

## Lo que esta reunión contradice
| Campo | Dijo la reunión | Dice el expediente | Fuente y fecha |
|---|---|---|---|
| Frecuencia del comité | «Próxima reunión en dos semanas» (≈ 2026-10-30) | La configuración dice comité **semanal**. Las seis reuniones archivadas, del 09-04 al 10-09, fueron semanales. | Notas 10-16 y `config.json`. La fecha 10-30 sí coincide con `committee_next`. |
| Estado del proyecto | Natalia reprograma por 6.ª vez y hay 6 compromisos vencidos. | Informe de avance: **verde**, 71 %. El cálculo lo marca como `declared_vs_evidence`: tres señales que el informe no explica (vencidos, reprogramados, avance contra plan). | Notas 10-16 e informe 10-12 |

Sobre el patrocinador, el comité y la fecha de cierre, la reunión no dice nada distinto del acta de constitución.

## Sin resolver de la transcripción
- **Óscar, «revisión con el proveedor, queda para el 2026-10-26»:** no se entiende qué se revisa ni si él la hace o solo asiste. Lo registré a su nombre porque la línea empieza con él, y habría que confirmarlo con él.
- **Laura, «la otra semana»:** puede ser la semana del 10-19 o una posterior, y no elegí una. Tampoco dice de qué proyecto o rubro es el presupuesto.
- **«Se comentó que el proveedor podría…»:** no dice quién lo dijo, qué proveedor ni qué fase.
- **«Próxima reunión en dos semanas»:** no trae día ni hora.

## Cifras recalculadas (con `compute`)
- **Vencidos:** 6.
  - Beatriz Cuéllar, 22 días.
  - Javier Hoyos, 16 días.
  - Felipe Arango, 9 días.
  - Natalia Ospina, 7 días.
  - Carlos Peña, 1 día.
  - Elena Duarte, 1 día.
  - Ninguno se mencionó en las notas de hoy.
- **Reprogramados sobre el umbral:** Natalia Ospina (6 veces) y Mauricio Pérez (5 veces, «Cerrar la prueba 2», ahora al 11-28).
- **Sin fecha:** 3.
- **Presupuesto (declarado en el informe del 10-12, sin evidencia contable):** ejecutado 49,1 %, comprometido 30,7 %, proyección 4,4 % por debajo de lo aprobado.

## Siguiente paso
Corre `/pm-commitments` para ver el seguimiento completo. Corre `/pm-publish` si quieres que la PMO vea la ficha, sobre todo por el verde declarado frente a las señales. El acta está en esta conversación y la guardas tú. No escribí nada en tu carpeta de reuniones.

La corrida quedó registrada como `2026-10-16-pm-minutes-1`, con 13 hallazgos. La salida completa está en `estado/PRY-209-migración-del-erp/corridas/salida-pm-minutes.md`.