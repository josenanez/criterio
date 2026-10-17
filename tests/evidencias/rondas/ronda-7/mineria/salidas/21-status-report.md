# /criterio-portfolio:status-report PRY-201

La corrida quedó registrada como `2026-10-17-status-report-1`. Este es el informe, igual al que guardé en `estado/corridas/salida-status-report.md`.

Mi nota para la corrida: los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré otra vez.

## PRY-201 · Ampliación de la relavera: estado al 2026-10-17

Sale de la ficha `estado/records/PRY-201.json` (actualizada 2026-10-17) y del cálculo de `portafolio.py compute`.

**Declara el gerente (Sandra Gil):** verde · 28% · al 2026-10-07 (hace 10 días, no está vencida).
**Sustento documental:** contradicho. La alerta `declared_vs_evidence` está abierta.
**Lo que el semáforo no explica:**
- un hito dado por cumplido sin evidencia
- un hito vencido
- avance por debajo del plan
- un entregable de proveedor atrasado
- facturado sin entrega
- facturado por encima de lo aceptado

**Último documento:** 2026-10-10 (hace 7 días; el umbral de silencio es 15). **Última reunión:** 2026-10-05.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2027-01-26 | 2027-01-26 | 0 días |
| Presupuesto (COP) | 4.200.000.000 | proyección 4.077.850.670 | −2,9% |

Hay 0 replanificaciones y una sola línea base (v1, 2026-04-11). No hay solicitudes de cambio.

- **Dinero (COP):** comprometido 2.607.597.890 (62,1%), ejecutado 1.067.730.191 (25,4%), disponible real 1.592.402.110. Estas cifras vienen del informe del gerente del 2026-10-07; ningún otro documento las respalda.
- **Avance:** el 28% declarado está 12,0 puntos por debajo de lo que el plan sustenta (entre 40% y 60%, con 2 de 5 hitos cumplidos).

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |
|---|---|---|---|---|
| Ingeniería básica aprobada | 2026-06-16 | 2026-06-16 | cumplido | Acta de recibo del 2026-10-10 |
| Ingeniería de detalle aprobada | 2026-08-11 | 2026-08-11 | declarado cumplido | Ninguna (67 días desde la fecha) |
| Licencia y permisos obtenidos | 2026-10-06 | 2026-10-06 | pendiente | Ninguna; vencido hace 11 días |
| Montaje e instalación | 2026-12-01 | 2026-12-01 | pendiente | Ninguna |
| Pruebas en operación | 2027-01-26 | 2027-01-26 | pendiente | Ninguna |

### Dónde no coincide
- **Verde frente a licencia vencida.** El cronograma v1 fecha la licencia el 2026-10-06 y sigue pendiente, sin replanificación registrada. El verde del 2026-10-07 no explica ese vencimiento.
- **Ingeniería de detalle «cumplida» sin acta de recibo.** El cronograma la marca cumplida, pero la ficha no encuentra evidencia. La ingeniería básica sí tiene acta, y es del 2026-10-10, no de junio.
- **Geotecnia Aplicada, CT-393.** Facturó 337.474.541 el 2026-08-28 y tiene 0 de 3 entregables aceptados. «Licenciamiento del software» (vencía 2026-07-07) lleva 102 días de atraso. «Bolsa de horas de ingeniería» (vencía 2026-09-22) lleva 25.
- **Geotecnia Aplicada, CT-663.** Facturó 546.514.606 el 2026-09-06 frente a 402.930.357 aceptados, es decir, 143.584.249 sin aceptación. La bolsa de horas vence el 2026-11-12 y está pendiente.
- **Posible doble contratación (no calculada por el script).** CT-393 y CT-663 tienen entregables con el mismo nombre y el mismo proveedor. Los documentos no aclaran si es doble contratación.

### Abierto
- **Riesgos e incidencias sin movimiento:**
  - Riesgo: ventana de parada de planta definida por operaciones. Sin responsable, valoración ni fecha.
  - Riesgo: cambio en la licencia ambiental que puede mover el alcance. Sin responsable ni valoración. Se conecta con el hito de licencia vencido.
  - Incidencia: las lluvias detuvieron el montaje diez días (desde 2026-10-07). Sin responsable, y el montaje sigue en 2026-12-01 en el cronograma.
- **Compromisos vencidos:** ninguno. Hay uno abierto: Óscar Ramírez, «Entregar el punto 11», para el 2026-11-06, sin reprogramaciones.
- **Dependencias sin confirmar:** ninguna registrada.

### Sin dato
- Producto, autoridad de aprobación y fase del proyecto.
- Evidencia de cumplimiento de los hitos 2 a 5 y de 4 de los 5 entregables de proveedor.
- Valoración de los dos riesgos.
- Respaldo contable de las cifras de dinero.

### Siguiente paso
La alerta de verde contradicho, la licencia vencida y los 143.584.249 facturados sin aceptación justifican llevarlo al comité del 2026-10-23. Puedo preparar el punto de comité con `/steering-pack` y revisar los pagos al proveedor con `/vendor-tracking`.

---
Criterio Portfolio v0.3.13 · ficha aplicada: PRY-201, actualizada 2026-10-17 · campos inciertos: los de «Sin dato» · Términos v1.1 aceptados el 2026-10-17 por José Francisco Ñáñez: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13