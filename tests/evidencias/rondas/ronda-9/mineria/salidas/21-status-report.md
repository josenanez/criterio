# /criterio-portfolio:status-report PRY-203

# PRY-203 · Despacho automático de flota: estado al 2026-10-17

La corrida de `/status-report` para PRY-203 quedó hecha y registrada.

Salió de la ficha `estado/records/PRY-203.json` (actualizada el 2026-10-17) y del cálculo con fecha 2026-10-17. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo.

**Declara el gerente (Felipe Arango):** rojo · 26 % · al 2026-10-14, hace 3 días, por lo que la declaración no está vencida.

**Sustento documental:** parcial.
- Ningún documento contradice el rojo.
- El 26 % no cuadra con el plan, y 2 de los 3 hitos cumplidos no tienen evidencia.
- Ningún documento de la ficha está marcado como evidencia: hay 0 de evidencia, 2 de declaración y 16 sin marcar.

**Lo que el semáforo no explica:** hitos cumplidos sin evidencia, montaje vencido, avance contra plan y desviación de costo.

**Último documento y última reunión:** ambos el 2026-10-14, comité semanal.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2026-10-04 | 2026-10-04 | 0 días. La fecha ya pasó hace 13 días y el proyecto sigue sin cerrar. |
| Presupuesto | COP 6.800.000.000 | Proyección COP 8.088.982.862 | +19,0 % (umbral 10 %) |

- **Dinero:** comprometido COP 4.780.108.610 (70,3 %), ejecutado COP 3.630.058.206 (53,4 %), disponible real COP 2.019.891.390.
- **Replanificaciones:** 0. Los informes declaran dos semanas perdidas por rotación de un ingeniero y diez días de lluvia sobre el montaje. Ninguna replanificación ni solicitud de cambio las recogió.

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |
|---|---|---|---|---|
| Ingeniería básica aprobada | 2026-02-03 | 2026-02-03 | Cumplido (declarado) | Ninguna (256 días desde la fecha) |
| Ingeniería de detalle aprobada | 2026-04-25 | 2026-04-25 | Cumplido | Acta de recibo del 2026-10-12 |
| Licencia y permisos obtenidos | 2026-07-15 | 2026-07-15 | Cumplido (declarado) | Ninguna (94 días desde la fecha) |
| Montaje e instalación | 2026-10-04 | 2026-10-04 | Pendiente | Vencido hace 13 días |

### Dónde no coincide
- **Avance contra plan:** el gerente declara 26 % y, con 3 de 4 hitos cumplidos, el plan respalda entre 75 % y 100 %. La diferencia es de 49,0 puntos. O el avance está subdeclarado, o los hitos «cumplidos» no lo están. Los documentos no permiten decidir cuál, así que hay que preguntárselo al gerente.
- **Hitos sin evidencia:** «Ingeniería básica» y «Licencia y permisos» figuran como cumplidos en el cronograma v1, sin acta, aprobación ni permiso que lo sustente.
- **Costo:** la proyección está 19,0 % por encima de lo aprobado y no hay solicitud de cambio de presupuesto.

### Abierto
- **Riesgos e incidencias:** hay 2 riesgos y 2 incidencias, sin responsable identificado.
  - Riesgos: concentración del conocimiento en una persona, y fecha de la última entrega del proveedor sin confirmar.
  - Incidencias: la rotación del ingeniero y las lluvias.
  - El cálculo no da días sin movimiento para estas entradas, así que no escribo cifras.
- **Compromisos vencidos:** ninguno. Hay uno sin fecha: Óscar Ramírez, «Entregar el punto 8», dicho en el comité del 2026-10-14. Sin fecha no se puede dar seguimiento.
- **Dependencias:** ninguna registrada. Tampoco hay proveedores en la ficha, aunque el riesgo del proveedor sugiere que existe uno.

### Sin dato
- Autoridad de aprobación (`identity.authority`) y fase (`identity.phase`).
- Responsable de los 4 riesgos e incidencias.
- Fecha del compromiso de Óscar Ramírez.

### Siguiente paso
PRY-203 supera el umbral de costo (19,0 % contra 10 %) y su fecha de cierre ya venció. Puedo preparar el punto de comité del 2026-10-23 y, si se decide mover fechas o presupuesto, la solicitud de cambio que hoy no existe.

---
Criterio Portafolio v0.4.0 · ficha PRY-203 aplicada con fecha 2026-10-17 · campos inciertos: autoridad y fase · términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.4.0

**Registro de la corrida:** el texto completo está en `estado/corridas/salida-status-report.md`. La corrida quedó como `2026-10-17-status-report-1`, con `--caso PRY-203` y una duración medida de 30 s. El conteo de señales que devolvió el registro cubre los 13 proyectos del portafolio, no solo PRY-203. Los 6 hallazgos de PRY-203 coinciden con el informe.