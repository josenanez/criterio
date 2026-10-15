# /criterio-portfolio:status-report PRY-201

## PRY-201 · Core de depósitos — estado al 2026-10-15

Este informe sale de la ficha `estado/records/PRY-201.json` (actualizada el 2026-10-15) y del cálculo de `portafolio.py compute` con fecha de corte 2026-10-15. Los términos (v1.1) ya estaban aceptados por José Francisco Ñáñez el 2026-10-15, así que no los registré otra vez.

**Declara el gerente (Laura Vélez):** verde · 30 % · al 2026-09-21, con 24 días de antigüedad (informe de avance)
**Sustento documental:** sin sustento. De los documentos leídos, 0 son evidencia, 2 son declaración y 16 no están marcados.
**Lo que el semáforo no explica:** `silent` (24 días sin documentos) y `variance_cost`.
**Último documento:** 2026-09-21 · **Última reunión:** sin dato

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2026-10-12 | 2026-10-12 | 0 días |
| Presupuesto (COP) | 4.200.000.000 | 4.200.000.000 | Proyección de 4.767.564.975, es decir 13.5 % sobre lo aprobado (umbral 10 %) |

- **Dinero:** comprometido 2.283.317.036 (54.4 %), ejecutado 922.042.148 (22.0 %) y disponible real 1.916.682.964.
- **Replanificaciones:** 0.
- **Cierre planeado:** la fecha vigente, 2026-10-12, ya pasó. Ningún documento dice si el proyecto cerró, se movió o sigue abierto. El script no lo cuenta como atraso porque no hay replanificación registrada.

### Hitos
La ficha no tiene hitos. Por eso el 30 % declarado no se puede contrastar con el plan.

### Dónde no coincide
- **Declarado:** verde y 30 %.
- **Documentos:** el mismo informe proyecta un gasto 13.5 % mayor a lo aprobado. Además, desde ese informe no hay ningún documento en 24 días. Es la alerta `declared_vs_evidence`.
- **Riesgo sin dueño:** el informe menciona que el proveedor no ha confirmado la fecha de la última entrega. No tiene probabilidad, impacto, dueño ni fecha, y la ficha no tiene proveedores registrados.

### Abierto
- **Riesgos sin movimiento:** hay 1 (el del proveedor), pero sin fecha de movimiento no se pueden calcular los días.
- **Compromisos vencidos:** ninguno registrado. La ficha no tiene compromisos, lo que no significa que no existan.
- **Dependencias sin confirmar:** ninguna registrada.

### Sin dato
- Autoridad de aprobación.
- Fase.
- Hitos.
- Proveedores.
- Última reunión.
- El PDF del informe no tiene huella de texto, así que conviene verificar a mano la lectura de sus cifras.

### Siguiente paso
La proyección supera el umbral de costo, el verde no tiene sustento y el cierre planeado ya pasó. Puedo preparar el punto de comité para este proyecto. También puedo preparar una solicitud de cambio, aunque ningún documento dice que el sobrecosto venga de un cambio no formalizado.

---
*criterio-portfolio v0.3.9 · ficha PRY-201 con fecha 2026-10-15 · campos inciertos: autoridad, fase, hitos, proveedores y última reunión · [términos y nota legal](https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.9)*

La corrida quedó registrada como `2026-10-15-status-report-1`. La salida completa está en `estado/corridas/salida-status-report.md`.