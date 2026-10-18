# /criterio-portfolio:status-report PRY-208

## PRY-208 · Motor de decisión — estado al 2026-10-17

Este informe sale de la ficha `estado/records/PRY-208.json`, actualizada el 2026-10-17. Los términos v1.1 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no hubo que registrarlos de nuevo.

**Declara el gerente (Carlos Peña):** verde · 47 % · al 2026-09-30. La declaración lleva 17 días, así que aún no está vencida (el umbral es 30).
**Sustento documental:** sin sustento. Las 13 fuentes de la ficha no tienen marca de evidencia. Los únicos documentos leídos son el acta de constitución (2026-01-16) y el propio informe de avance (2026-09-30), que es la declaración.
**Lo que el semáforo no explica:** `silent`, es decir 17 días sin documentos con el umbral en 15. Por eso aparece la alerta `declared_vs_evidence`: reporta verde y esa señal queda sin cubrir.
**Último documento:** 2026-09-30. **Última reunión:** sin dato, porque la ficha no tiene minutas ni transcripciones.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2027-03-15 | 2027-03-15 | 0 días |
| Presupuesto aprobado | COP 1.200.000.000 | COP 1.200.000.000 | proyección COP 1.129.393.870 (−5,9 %) |

- **Ejecutado:** COP 459.175.619 (38,3 %).
- **Comprometido:** COP 844.902.221 (70,4 %).
- **Disponible real:** COP 355.097.779.
- **Replanificaciones:** 0. Hay una sola versión de línea base (v1, 2026-01-16) y ninguna solicitud de cambio.

### Hitos
La ficha no tiene hitos cargados. No se puede contrastar el 47 % declarado contra el plan.

### Dónde no coincide
- **Declarado:** verde, 47 %, al 2026-09-30.
- **Documentos:** no hay nada posterior al 2026-09-30, ni nada que sustente el verde fuera del propio informe.
- **Dentro del informe:** se levantó un hallazgo de seguridad en la revisión de arquitectura (incidencia desde 2026-09-30, sin responsable) y el informe mantiene el verde. El script no lo marca como señal. Lo cito como dato; juzgar si cabe en un verde le toca al gerente y al comité.

### Abierto
- **Riesgo:** dependencia del calendario de liberaciones del core. No tiene fecha ni responsable, y su única fuente es el informe del 2026-09-30.
- **Incidencia:** hallazgo de seguridad desde 2026-09-30 (17 días), sin responsable.
- **Compromisos vencidos:** ninguno registrado. La ficha no tiene compromisos, y sin minutas eso no equivale a «ninguno».
- **Dependencias sin confirmar:** ninguna registrada. El riesgo del core apunta a una dependencia externa que no está en la ficha como dependencia.

### Sin dato
- Producto, autoridad y fase del proyecto.
- Hitos y sus fechas de línea base.
- Última reunión, compromisos y proveedores.

**Siguiente paso posible:** hay una señal de silencio sobre el umbral y una incidencia de seguridad sin responsable. Puedo preparar el punto de comité. No hay cambio de alcance sin formalizar, así que no corresponde una solicitud de cambio.

---
**Pie:** criterio-portfolio 0.4.0 · ficha PRY-208 del 2026-10-17 (declaración del 2026-09-30) · campos inciertos: producto, autoridad, fase, hitos · [Términos y nota legal](https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.4.0)

La corrida quedó registrada como `2026-10-17-status-report-1`. El texto completo está en `estado/corridas/salida-status-report.md` y la corrida midió 22 segundos.