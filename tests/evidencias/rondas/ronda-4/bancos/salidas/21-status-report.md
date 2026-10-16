# /criterio-portfolio:status-report PRY-208

## PRY-208 · Motor de decisión — estado al 2026-10-15

Este informe sale de la ficha `estado/records/PRY-208.json`, actualizada el 2026-10-15. Las cifras las recalculó `compute` al 2026-10-15. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

**Declara el gerente (Sandra Gil):** amarillo, 74%, al 2026-09-25 (hace 20 días; el umbral de declaración vencida es 30).
**Sustento documental:** parcial.
- El 74% cae dentro de lo que el plan sustenta (60–80%, con 3 de 5 hitos cerrados).
- El amarillo no explica cuatro señales abiertas:
  - **Hito sin acta:** «Diseño funcional aprobado» figura cumplido (base 2026-04-28) y no tiene acta de recibo. Van 170 días.
  - **Piloto vencido:** «Piloto con usuarios internos» vencía el 2026-10-11 y sigue pendiente. Van 4 días.
  - **Entregables de proveedor vencidos:** tres entregables de Datacore Colombia (contrato CT-932) pasaron su fecha sin recibo.
  - **Factura sin entrega:** Datacore facturó 105.076.622 COP (FV-1932, 2026-09-27) y ningún entregable está aceptado.

**Último documento:** 2026-10-12 (hace 3 días). **Última reunión:** 2026-10-06 (comité semanal).

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2026-12-05 | 2026-12-05 | 0 días |
| Presupuesto aprobado | 1.200.000.000 COP | 1.200.000.000 COP | sin cambio |

- **Presupuesto:** comprometido 1.042.279.479 (86,9%), ejecutado 673.930.886 (56,2%), disponible real 157.720.521.
- **Proyección:** 1.162.609.510 (−3,1% frente al aprobado). La declaró el gerente en el informe del 2026-09-25; no se calculó desde los documentos.
- **Replanificaciones y cambios:** 0 replanificaciones y 0 solicitudes de cambio.

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |
|---|---|---|---|---|
| Diseño funcional aprobado | 2026-04-28 | 2026-04-28 | cumplido (declarado) | **ninguna** |
| Ambiente de pruebas certificado | 2026-06-22 | 2026-06-22 | cumplido | acta de recibo 2026-10-02 |
| Integración con el core | 2026-08-16 | 2026-08-16 | cumplido | acta de recibo 2026-10-12 |
| Piloto con usuarios internos | 2026-10-11 | 2026-10-11 | pendiente, vencido 4 días | — |
| Salida a producción | 2026-12-05 | 2026-12-05 | pendiente | — |

### Dónde no coincide
- **Contrato CT-932:**
  - Ningún entregable figura recibido y no hay actas de recibo de ellos. Las dos actas de la carpeta son de hitos del proyecto, no de entregables del contrato.
  - La factura FV-1932 está radicada en cuentas por pagar (`20-seguimiento/2026-09-27-factura-ct-932.pdf`).
- **Hito de diseño:** el cronograma v1 (2026-02-22) lo marca cumplido, sin acta que lo respalde.
- **Piloto:** el cronograma lo tiene pendiente con la fecha ya pasada. El informe del 2026-09-25 no lo menciona como en riesgo.
- **Dependencia del core:** el informe la cita como riesgo y el acta de constitución no la declara.

### Abierto
- **Riesgos e incidencias:**
  - Hay dos riesgos y una incidencia registrados en el informe del 2026-09-25: la dependencia del calendario de liberaciones del core, la disponibilidad del equipo de seguridad y dos historias fuera del alcance del sprint.
  - Ninguno tiene dueño, fecha ni última fecha de movimiento, así que no se pueden contar días sin movimiento.
- **Compromisos vencidos:** ninguno. Hay uno abierto: María Restrepo, «Entregar el punto 17», para el 2026-11-09.
- **Dependencias sin confirmar:** ninguna registrada como dependencia.
- **Entregable próximo:** «Mesa de ayuda del primer trimestre» de CT-932 vence el 2026-11-02 y está pendiente.

### Sin dato
- Producto: el acta dice «No aplica», así que queda vacío.
- Autoridad de aprobación y fase: no figuran en ningún documento.
- Probabilidad, impacto y dueño de los riesgos, y dueño y fecha de inicio de la incidencia.
- Acta de recibo del hito «Diseño funcional aprobado».
- Línea base de costo anterior con la que comparar: solo hay una cifra aprobada.

**Siguiente paso posible:** puedo preparar el punto de comité (el próximo es el 2026-10-22) con la factura sin entrega y el piloto vencido.

---
Criterio Portfolio v0.3.10 · ficha PRY-208 aplicada, con fecha 2026-10-15 · campos inciertos: producto, autoridad, fase y evidencia del diseño funcional · Términos v1.1 aceptados por José Francisco Ñáñez el 2026-10-15 · Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

La corrida quedó registrada como `2026-10-15-status-report-1` (29 segundos). La salida completa está en `estado/corridas/salida-status-report.md`.