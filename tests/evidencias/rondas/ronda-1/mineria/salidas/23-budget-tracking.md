# /criterio-portfolio:budget-tracking PRY-207

Ya terminé el presupuesto de PRY-207. La corrida quedó registrada (`2026-10-14-budget-tracking-1`).

## Presupuesto — PRY-207 Gemelo digital de la planta al 2026-10-14
**Fuentes:** la ficha de PRY-207, que sale del informe de avance del 2026-10-13, el acta de constitución, el cronograma v1 y el comité del 2026-10-09. Las cifras derivadas están copiadas de `compute`. Los términos los acepta José Francisco Ñáñez (v1.0, 2026-10-14).

**Moneda:** COP. No hay otra moneda ni conversión.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 9.500.000.000 | — | Informe de avance (declaración) | 2026-10-13 |
| Comprometido | 6.116.727.959 | 64.4% | Informe de avance (declaración) | 2026-10-13 |
| Ejecutado | 2.397.804.823 | 25.2% | Informe de avance (declaración) | 2026-10-13 |
| Proyección al cierre | 11.790.477.110 | 24.1% por encima del aprobado | Informe de avance (declaración) | 2026-10-13 |

**Disponible real** (aprobado menos comprometido): 3.383.272.041 COP.

Las cuatro cifras salen de un solo documento, el informe del gerente. Ninguna tiene respaldo de evidencia, como contrato, factura o causación. La proyección es una declaración de la misma fecha del informe. No hay ningún movimiento de presupuesto registrado, así que no es más vieja que el último.

**Contra la línea base**
- Ningún documento fija el presupuesto original, así que no se puede calcular la desviación del aprobado contra el original. Tampoco se puede saber si 9.500.000.000 es el monto original o uno ya modificado.
- Replanificaciones de presupuesto: 0 registradas. La única línea base es la de cronograma del 2025-11-29.

**Ejecución frente a avance**
- Ejecutado 25.2%, hitos cumplidos 4 de 4 (declarados), avance declarado 65%.
- La ejecución está muy por debajo del avance. Puede ser trabajo hecho y no causado, o avance sobrestimado, y los documentos no permiten distinguirlo.
- Hay base para dudar del avance. Dos de los cuatro hitos "cumplidos" no tienen acta de recibo: Ingeniería de detalle (vencía el 2026-04-03) y Montaje e instalación (vencía el 2026-07-28).
- El plan terminaba el 2026-07-28 y el proyecto sigue en curso, sin replanificación registrada. El plan sostiene 100% y el gerente declara 65%, una brecha de 35 puntos.

**Alertas**
- **Proyección sobre el aprobado:** 24.1%, con umbral de 10%. Es la señal principal.
- **Comprometido:** 64.4%, bajo el umbral de 90%, sin alerta. Aun así, la proyección dice que el disponible real no alcanzará.
- **Ejecución desalineada del avance:** 25.2% ejecutado contra 65% declarado.
- **Informe en rojo:** el gerente declara el proyecto en rojo y no explica la proyección ni la brecha de avance.

**Sin dato**
- Presupuesto original y fecha de su aprobación.
- Evidencia contable del comprometido y el ejecutado. La ficha no registra proveedores.
- Fecha y autor de cualquier movimiento de presupuesto.
- Autoridad que aprueba y fase del proyecto.

**Siguiente paso:** la proyección excede el aprobado, así que puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. El detalle por proveedor no corresponde: el comprometido no está cerca del tope y la ficha no tiene proveedores.

**Pie de rigor:** todo esto es lo que declara un solo informe del gerente y no se contrastó con evidencia contable. No convertí moneda ni redondeé porcentajes por mi cuenta.

**Archivos:**
- `estado/portafolio/corridas/salida-budget-tracking.md` (el informe completo)
- `estado/portafolio/corridas/2026-10-14-budget-tracking.md` (el registro de la corrida)

**Un detalle del registro:** el script contó la corrida sobre los 13 proyectos del portafolio, con 39 hallazgos en total, aunque el caso es solo PRY-207. El `--caso` quedó como PRY-207, pero las estadísticas de la corrida son del portafolio completo.