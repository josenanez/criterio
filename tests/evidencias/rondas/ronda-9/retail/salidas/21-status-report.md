# /criterio-portfolio:status-report PRY-203

Terminé la corrida de `/status-report PRY-203` y estaba cerrando el registro. Este es el informe, igual al que guardé en `estado/corridas/salida-status-report.md`.

Sale de la ficha PRY-203, actualizada el 2026-10-17, y las cifras las recalculé con `compute` al 2026-10-17. Los términos ya estaban vigentes (José Francisco Ñáñez, 2026-10-17, versión 0.4.0), así que no los registré de nuevo.

## PRY-203 · Reposición automática — estado al 2026-10-17

**Declara el gerente (Laura Vélez):** verde · 92 % · al 2026-10-15 (hace 2 días, vigente). Fuente: `20-seguimiento/2026-10-15-informe-avance.pdf`.
**Sustento documental:** **contradicho**. El script marca `declared_vs_evidence`: el verde no explica 7 señales abiertas. Ninguna fuente de la ficha está marcada como evidencia (0 de evidencia, 2 de declaración, 161 sin marcar).
**Lo que el semáforo no explica:**
- compromisos vencidos y compromisos reprogramados;
- hitos «cumplidos» sin evidencia y un hito vencido;
- desviación de costo;
- entregables de proveedor atrasados y proveedor facturado por encima de lo aceptado.

**Último documento:** 2026-10-17 (notas de reunión). **Última reunión de comité:** 2026-10-10. Días en silencio: 0.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2026-10-09 | 2026-10-09 | 0 días en el papel, pero la fecha ya pasó y el despliegue sigue pendiente |
| Presupuesto (COP) | 1.200.000.000 | 1.200.000.000 | Proyección 1.432.210.423, es decir **+19,4 %** (umbral 10 %) |

Replanificaciones: 0. No hay línea base posterior a la v1 (acta del 2025-07-06) ni solicitudes de cambio. El plan no se movió aunque la fecha de cierre ya venció.

Dinero (COP):
- Comprometido: 742.486.754 (61,9 %).
- Ejecutado: 251.538.678 (21,0 %).
- Disponible real: 457.513.246.

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |
|---|---|---|---|---|
| Diseño de la experiencia aprobado | 2025-10-14 | 2025-10-14 | cumplido (declarado) | **sin evidencia** (368 días) |
| Ambiente de pruebas certificado | 2026-01-12 | 2026-01-12 | cumplido (declarado) | **sin evidencia** (278 días) |
| Integración con el ERP | 2026-04-12 | 2026-04-12 | cumplido (declarado) | **sin evidencia** (188 días) |
| Piloto en tiendas | 2026-07-11 | 2026-07-11 | cumplido (declarado) | **sin evidencia** (98 días) |
| Despliegue en la cadena | 2026-10-09 | 2026-10-09 | pendiente | **vencido hace 8 días** |

El 92 % declarado cabe en lo que sostiene el plan (80–100 %, 4 de 5 hitos). Pero ese rango depende de cuatro hitos que nadie sustenta.

### Dónde no coincide
- **Verde frente al hito de cierre:** el informe del 2026-10-15 dice verde. El cronograma v1 pone el despliegue el 2026-10-09 y sigue pendiente, con 8 días de atraso.
- **Verde frente al costo:** el mismo informe proyecta 1.432.210.423 sobre 1.200.000.000 aprobados (+19,4 %).
- **Proveedor Sistemas Comerciales del Norte (CT-338):**
  - Facturó 118.225.663 y se aceptaron 95.848.542, o sea **22.377.121 por encima de lo aceptado** (4 de 4 montos declarados).
  - Tiene tres entregables pendientes y vencidos: Licenciamiento de la plataforma (2025-10-23, 359 días), Bolsa de horas de desarrollo (2026-01-30, 260 días) y Configuración del catálogo (2026-05-09, 161 días).
  - «Soporte del primer trimestre» figura aceptado sin evidencia de recibo.
- **Incidencia del propio informe:** el equipo perdió dos semanas por la rotación de un desarrollador clave (desde 2026-10-15). No tiene responsable ni replanificación registrada.

### Abierto
**Riesgos e incidencias sin movimiento:**
- «Concentración del conocimiento en una sola persona» (informe del 2026-10-15): sin responsable, probabilidad, impacto ni fecha de último movimiento, así que no puedo calcular los días.
- «El proveedor podría no llegar con el equipo completo para la siguiente fase» (dicho en reunión, notas del 2026-10-17, nadie lo registró): mismos campos vacíos.
- Incidencia de rotación del desarrollador: abierta desde 2026-10-15 (2 días), sin responsable.

**Compromisos vencidos (8):**
| Quién | Qué | Vencía | Días |
|---|---|---|---|
| Carlos Peña | Validar el ambiente 4 | 2026-09-25 | 22 |
| Liliana Torres | Confirmar la fecha 15 | 2026-09-29 | 18 |
| Laura Vélez | Cerrar la prueba 10 | 2026-10-03 | 14 |
| Ricardo Salas | Enviar el documento 17 | 2026-10-06 | 11 |
| Natalia Ospina | Revisar el anexo 3 | 2026-10-10 | 7 |
| María Restrepo | Aprobar el diseño 13 | 2026-10-11 | 6 |
| Camilo Beltrán | Actualizar la matriz 14 | 2026-10-11 | 6 |
| Elena Duarte | Entregar el punto 16 | 2026-10-15 | 2 |

**Reprogramados varias veces:**
- Natalia Ospina, «Enviar el documento 1»: 6 veces; original 2026-09-28, hoy 2026-12-18.
- Laura Vélez, «Cerrar la prueba 2»: 5 veces; original 2026-09-18, hoy 2026-11-24.
- Jorge Medina, «Revisar el anexo 11»: 3 veces; original 2026-10-01, hoy 2026-11-20.

**Sin fecha:**
- Jorge Medina, «Confirmar la fecha 7».
- Gustavo Neira, «Validar el ambiente 12».
- Laura Vélez, «Mandar el ajuste del presupuesto» (notas del 2026-10-17).

**Dependencias sin confirmar:** ninguna registrada en la ficha.

### Sin dato
- Evidencia de cumplimiento de los 5 hitos y de los 4 entregables del proveedor.
- Producto, autoridad y fase del proyecto.
- Probabilidad, impacto, responsable y último movimiento de los riesgos.
- Identidad, plan y presupuesto aprobado vienen del acta y el cronograma del 2025-07-06, con 15 meses (umbral 12). Hay que confirmarlos con quien los gobierna.

### Siguiente paso
Hay desviación de costo por encima del umbral (19,4 % frente a 10 %) y un cierre vencido sin replanificar. Puedo preparar el punto de comité (el próximo es el 2026-10-23) y, si el atraso viene de un cambio no formalizado, la solicitud de cambio.

---
Criterio Portfolio 0.4.0 · ficha aplicada: PRY-203, actualizada el 2026-10-17 · campos inciertos: los de «Sin dato» · Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.4.0

La corrida quedó registrada como `2026-10-17-status-report-1`, caso PRY-203, con 34 segundos medidos. El registro cuenta 13 proyectos y 90 hallazgos porque suma todo el portafolio, no solo PRY-203. El número de documentos leídos quedó sin medir.