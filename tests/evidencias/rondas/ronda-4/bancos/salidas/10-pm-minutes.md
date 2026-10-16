# /criterio-project:pm-minutes documentos/proyectos/PRY-210-portal-de-proveedores/2026-10-15-notas-reunion.txt

# Acta — Portal de proveedores (PRY-210) · 2026-10-15
**Asistieron:** Andrés Lozano, Camilo Beltrán, Carlos Peña, Javier Hoyos, Jorge Medina, Laura Vélez, Liliana Torres, Mauricio Pérez, Natalia Ospina, Ricardo Salas, Rubén Cárdenas, Sandra Gil, Óscar Ramírez · **Fuente:** `2026-10-15-notas-reunion.txt` · **Ausentes con tema en agenda:** las notas no traen agenda, no se puede decir. Con compromisos abiertos y sin asistir: Diana Molina, María Restrepo, Paula Céspedes.

Los términos ya estaban vigentes (versión 0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar.

## Compromisos
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Jorge Medina | Enviar el documento 1 (#1) | 2026-12-08 | **Reprogramado 6 veces.** Original 2026-09-17; antes 09-29, 10-09, 10-30, 11-10, 11-24. Es la 6.ª fecha nueva; las notas dicen «no alcanzó». Fecha leída día/mes/año («08/12/2026»). |
| Óscar Ramírez | Revisión con el proveedor (#26) | 2026-10-25 | Nuevo según el texto. Puede ser lo mismo que «Entregar el punto 16» (#16, para 2026-11-03); las notas no lo dicen y no lo fusioné. El 25 cae domingo. |

### Sin fecha
| Quién | Qué |
|---|---|
| Laura Vélez | Mandar el ajuste del presupuesto (#25). Dicho como «la otra semana»; nadie dijo día y no se convirtió en fecha. Va con `due_date: no_declarada`. |

Ya había otro sin fecha: María Restrepo, «Revisar el anexo 19» (#19), desde el 2026-10-01.

## Decisiones
Ninguna. Las notas no registran que alguien haya decidido algo.

## Quedó sin decidir
Las notas no dicen qué quedó en suspenso. La única fecha de reunión es «próxima reunión en dos semanas», sin día.

## Intenciones sin doliente
Ninguna en estas notas.

## Dicho al pasar y no registrado
| Qué | Quién lo dijo | Categoría | Ya estaba en el RAID |
|---|---|---|---|
| «El proveedor podría no llegar con el equipo completo para la siguiente fase»; las notas dicen que nadie lo anotó como riesgo | No consta: «se comentó» | Riesgo | **No.** Está en la ficha como `registered: false`, sin dueño, probabilidad ni impacto. El único riesgo registrado es otro (disponibilidad del equipo de seguridad). |

La ficha tampoco tiene ningún proveedor en `vendors`, así que este riesgo no tiene a qué contrato atarse.

## Cerrado en esta reunión
Nada. Ninguna frase de las notas trae un documento de cierre.

## Lo que esta reunión contradice
| Campo | Dijo la reunión | Dice el expediente | Fuente y fecha de cada uno |
|---|---|---|---|
| Cadencia del comité | «Próxima reunión en dos semanas» (≈ 2026-10-29) | `cycle.committee: weekly`; las seis minutas previas son semanales | Notas 2026-10-15; configuración y minutas 09-03 a 10-08 |

No cambió patrocinador, fecha de cierre ni comité. La fecha 2026-10-29 sí coincide con `committee_next`.

## Sin resolver de la transcripción
- «Revisión con el proveedor, queda para el 2026-10-25»: no queda claro si es compromiso nuevo o el #16 reformulado.
- «Se compromete para el 08/12/2026»: leído como 8 de diciembre; si fuera otro orden, cambia la fecha.
- «Se comentó que el proveedor podría no llegar…»: no consta quién lo dijo.
- Las notas no mencionan los compromisos vencidos (Paula Céspedes, Camilo Beltrán #10, Diana Molina, Andrés Lozano #22, Laura Vélez #23). Laura Vélez asistió y tiene #23 vencido desde el 2026-10-11 sin mención.

## Cifras recalculadas (`portafolio.py compute`)
- Vencidos sin evidencia: 5. Sin fecha: 2. Reprogramados al umbral (3 o más): 4 (#1 × 6, #2 × 5, #7 × 4, #3 × 3).
- El informe del 2026-10-13 declara «verde» y 34 %; 4 señales lo contradicen.

## Después
Usa `/pm-commitments` para el seguimiento completo. `/pm-publish` no hace falta por esta acta: ningún campo de la ficha cambió por lo que se dijo. El acta sale aquí y la guardas tú.

La corrida quedó registrada como `2026-10-15-pm-minutes-1`, con 15 hallazgos y 31 segundos medidos. El texto de arriba está en `estado/PRY-210-portal-de-proveedores/corridas/salida-pm-minutes.md`.