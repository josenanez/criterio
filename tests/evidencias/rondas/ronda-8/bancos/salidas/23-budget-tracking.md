# /criterio-portfolio:budget-tracking PRY-203

La corrida de PRY-203 quedó registrada. Lo que sigue es el informe completo, igual que el archivo guardado.

**Documentos de los que sale:** la ficha PRY-203 (`estado/records/PRY-203.json`) y los documentos de los que se construyó:
- `20-seguimiento/2026-10-17-informe-avance.md`
- el cronograma v1 y el acta de constitución, ambos del 2025-11-01
- el acta de recibo del diseño funcional (2026-10-17)
- el comité del 2026-10-12

Las cifras salen de `portafolio.py compute` al 2026-10-17.

## Presupuesto — PRY-203 Open Banking al 2026-10-17
**Moneda:** COP. Es la única; no hay otra moneda ni conversión.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 6.800.000.000 | 100% | informe-avance.md, sección Presupuesto | 2026-10-17 |
| Comprometido | 6.145.585.663 | 90,4% | ídem | 2026-10-17 |
| Ejecutado | 1.436.705.266 | 21,1% | ídem | 2026-10-17 |
| Proyección al cierre | 8.099.349.061 | 119,1% (excede el aprobado en 19,1%) | ídem | 2026-10-17 |

**Disponible real** (aprobado menos comprometido): 654.414.337 COP.

Las cuatro cifras vienen de un solo documento, el informe de avance de la gerente (María Restrepo). Son declaración, no evidencia contable: ningún documento del proyecto es un extracto de ejecución ni un contrato. La proyección lleva la misma fecha que las demás y no hay un movimiento de presupuesto posterior, así que no está vieja.

### Contra la línea base
| | Original | Vigente | Desviación |
|---|---|---|---|
| Aprobado | 6.800.000.000 | 6.800.000.000 | 0 (no hay solicitudes de cambio registradas) |
| Proyección frente al aprobado | — | 8.099.349.061 | +19,1% (umbral 10%) |

Replanificaciones de presupuesto: 0. Solo hay un valor aprobado. No hay una línea base de presupuesto anterior con la que compararlo, y no la inventé.

### Ejecución frente a avance
- Ejecutado 21,1%.
- Hitos cumplidos 3 de 4 según lo declarado, pero solo 1 tiene evidencia de recibo.
- Avance declarado 39%. Con esos hitos el plan sostiene entre 75% y 100%, una brecha de 36,0 puntos.

**Lectura:** lo ejecutado es 21,1%, pero ya hay 90,4% comprometido. La holgura real es 9,6%, no 78,9%. Lo ejecutado va por debajo del avance de hitos, pero esos hitos no están sustentados. Dos hitos marcados como cumplidos no tienen acta ni evidencia. Por eso no puedo decir si hay trabajo hecho sin facturar o hitos que no se cumplieron.

### Alertas
- **Comprometido en 90,4%, sobre el umbral de 90%.** El disponible real es 654.414.337 COP y falta el piloto con usuarios internos, previsto para el 2026-10-29.
- **La proyección excede el aprobado en 19,1%**, sobre el umbral de 10%. La diferencia es 1.299.349.061 COP.
- **Hitos cumplidos sin evidencia:** "Ambiente de pruebas certificado" (vencía el 2026-05-06, hace 164 días) e "Integración con el core" (vencía el 2026-08-02, hace 76 días).
- **Compromiso vencido:** Paula Céspedes, "Entregar el punto 23", vencía el 2026-10-12 (5 días). Fuente: `30-reuniones/2026-10-12-comite-semanal.md`.
- **Estado declarado "verde" con cinco señales sin explicar:** comprometido, proyección, avance frente a plan, hitos sin evidencia y compromiso vencido.

### Sin dato
- Presupuesto original distinto del vigente: no está declarado en ningún documento.
- Desglose del comprometido por proveedor o contrato: no hay contratos de proveedor en la documentación del proyecto.
- Fase del proyecto y autoridad de aprobación: `not_found`.

### Después
Como la proyección excede el aprobado, puedo preparar la solicitud de cambio de presupuesto. Como el comprometido está sobre el tope, puedo armar el detalle por proveedor, pero necesitaría los contratos. Ninguna de las dos cosas está hecha.

---
**Pie de rigor:** borrador de trabajo, no decisión ni asesoría. Cada cifra sale del informe de avance del 2026-10-17 (declaración de la gerente, sin evidencia contable) y de los cálculos de `compute`. La verificación es suya.

**Términos:** ya estaban vigentes (v1.1, familia 0.3.13), aceptados por José Francisco Ñáñez el 2026-10-17. No hubo que registrarlos de nuevo.

**Corrida:** la registré como `2026-10-17-budget-tracking-1`, con salida guardada en `estado/corridas/salida-budget-tracking.md`. El registro cuenta 13 proyectos y 60 hallazgos porque `compute` recorre todo el portafolio. Los de PRY-203 son 7, los mismos de arriba. El número de documentos leídos quedó sin medir (`null`).