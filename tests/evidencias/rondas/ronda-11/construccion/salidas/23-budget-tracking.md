# /criterio-portfolio:budget-tracking PRY-203

## Presupuesto — PRY-203 Planta de tratamiento de agua, al 2026-10-22

Salió de la ficha PRY-203 y del recálculo `compute` de hoy. Los términos (v1.2) ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-22, así que no los registré de nuevo.

**Moneda:** COP, la única en la ficha. No convertí nada.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 3.300.000.000 | 100% | Acta de constitución | 2025-07-24 |
| Comprometido | 2.066.126.764 | 62.6% | Informe de avance | 2026-10-17 |
| Ejecutado | 1.510.877.959 | 45.8% | Informe de avance | 2026-10-17 |
| Proyección al cierre | 4.214.486.517 | 27.7% por encima del aprobado | Informe de avance | 2026-10-17 |

**Disponible real** (aprobado menos comprometido): 1.233.873.236 COP.

La proyección es una declaración del informe de avance, no un dato duro. Es posterior a los dos cambios aprobados, así que no está desactualizada frente al último movimiento de presupuesto.

### Contra la línea base
- **Presupuesto:** el original es 3.300.000.000 COP. El vigente no está declarado en ningún documento. El comité aprobó CC-01 (+202.000.000 COP) y CC-02 (+92.000.000 COP). `compute` no da un presupuesto vigente, así que no lo sumé a mano.
- **Plazo:** 147 días (63.6%) contra la línea base original y 0 contra la vigente.
- **Replanificaciones:** 1, de cronograma. La ficha no registra una línea base de costo nueva.

### Ejecución frente a avance
El ejecutado es 45.8%, el avance declarado es 93% y los hitos cumplidos son 4 de 4 (declarados). El avance está muy por encima de lo ejecutado. Hay dos lecturas posibles: hay trabajo hecho y no causado que aparecerá de golpe, o el avance está sobredeclarado. Los documentos no permiten decidir cuál. Dos hitos figuran como cumplidos sin acta de recibo ni otra evidencia (Cimentación terminada y Estructura terminada), lo que da más peso a la segunda lectura.

### Alertas
- **Proyección sobre el aprobado:** 4.214.486.517 contra 3.300.000.000 COP, 27.7% por encima (umbral 10%).
- **Plazo:** 147 días (63.6%) de desviación contra la línea base original.
- **Ejecución desalineada del avance:** 45.8% ejecutado contra 93% declarado.
- **Hitos cumplidos sin evidencia:** Cimentación terminada (vencía el 2026-01-23) y Estructura terminada (vencía el 2026-08-16).
- **Compromisos vencidos:** Elena Duarte, "Entregar el punto 28" (5 días), y Javier Hoyos, "Entregar el punto 19" (7 días).
- **Informe de avance:** declara estado rojo y no da cuenta de ninguna de estas señales.
- **Comprometido:** 62.6%, bajo el umbral de 90%. No hay alerta por ese concepto.

### Sin dato
- El presupuesto vigente, es decir el original más CC-01 y CC-02.
- Si el comprometido, el ejecutado y la proyección ya incluyen esos cambios.
- El detalle por proveedor: la ficha no tiene proveedores.
- El aprobado y los campos de identidad y plan tienen fuente de 2025-07-24, con 15 meses de antigüedad (umbral 12).

### Siguiente paso posible
Como la proyección excede el aprobado, puedo preparar la solicitud de cambio de presupuesto.

*Borrador de trabajo, no decisión ni asesoría. Cada dato lleva su cita y la verificación es de quien lo usa.*

La corrida quedó registrada como `2026-10-22-budget-tracking-1`, con el informe en `estado/corridas/salida-budget-tracking.md`. Tardó 36 segundos. No se midió el número de documentos leídos. El conteo de señales que muestra el registro cubre los 13 proyectos, no solo PRY-203.