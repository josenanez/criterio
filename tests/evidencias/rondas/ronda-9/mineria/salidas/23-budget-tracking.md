# /criterio-portfolio:budget-tracking PRY-207

## Presupuesto — PRY-207 Gemelo digital de la planta, al 2026-10-17

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no los volví a registrar. Las cifras salen de la ficha `PRY-207.json` y de `portafolio.py compute`. Los documentos de origen son el acta de constitución (2025-08-17) y el informe de avance (2026-09-29).

**Moneda:** COP. Es la única que aparece.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 6.800.000.000 | 100 | Acta de constitución | 2025-08-17 |
| Comprometido | 5.445.601.460 | 80.1 | Informe de avance | 2026-09-29 |
| Ejecutado | 4.062.393.959 | 59.7 | Informe de avance | 2026-09-29 |
| Proyección al cierre | 7.922.563.459 | excede el aprobado en 16.5 | Informe de avance | 2026-09-29 |

**Disponible real** (aprobado menos comprometido): 1.354.398.540 COP.

La proyección es una declaración del informe de avance, no un dato medido. Tiene 18 días y no hay ningún cambio de presupuesto posterior que la deje vieja.

### Contra la línea base
- **Presupuesto:** el aprobado original y el vigente son el mismo, 6.800.000.000 COP. Hay 0 replanificaciones y 0 solicitudes de cambio.
- **Costo:** la proyección está 16.5 % por encima del aprobado, con un umbral de 10 %.

### Ejecución frente a avance
- **Cifras:** ejecutado 59.7 %, hitos cumplidos 3 de 4, avance declarado 20 %. El plan sostiene entre 75 y 100 %.
- **Lectura:** el gasto va muy por encima del avance que el propio proyecto declara. Los tres hitos «cumplidos» no tienen evidencia, así que estas cifras no se pueden reconciliar con los documentos.

### Alertas
- **Proyección sobre el aprobado:** 16.5 % de desviación en costo.
- **Brecha de avance:** 55 puntos entre el avance declarado y lo que sostiene el plan.
- **Hitos sin evidencia:** los tres hitos cumplidos son Ingeniería básica (vencía 2025-12-18), Ingeniería de detalle (2026-04-11) y Licencia y permisos (2026-08-03).
- **Estado «verde»:** el informe del 2026-09-29 lo declara, y hay cuatro señales abiertas que no recoge.
- **Compromiso vencido:** Andrés Lozano debía «Entregar el punto 14» el 2026-10-10, hace 7 días.
- **Comprometido:** está en 80.1 %, bajo el umbral de 90 %. No genera alerta, pero el disponible real es de 1.354.398.540 COP frente a una proyección que ya pasa el aprobado.

### Sin dato
- No están declaradas la autoridad que aprueba ni la fase del proyecto.
- Las cuatro cifras salen del acta y de un informe de avance, sin documento de evidencia aparte. No hay extracto contable ni facturas, así que no puedo confirmar el ejecutado y el comprometido.
- No hay contratos de proveedor registrados, así que no puedo abrir el comprometido por proveedor.
- Los campos de identidad y plan tienen 14 meses, con un umbral de 12, y piden confirmación.

### Siguiente paso
La proyección excede el aprobado. Puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. El detalle por proveedor queda pendiente hasta que haya contratos registrados.

La corrida quedó registrada como `2026-10-17-budget-tracking-1`, con este texto guardado en `estado/corridas/salida-budget-tracking.md`.

*Pie de rigor: es un borrador de trabajo, no una decisión ni asesoría. Cada cifra va con la cita de su documento y la verificación es de quien lee.*