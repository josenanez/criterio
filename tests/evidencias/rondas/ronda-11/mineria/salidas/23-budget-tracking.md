# /criterio-portfolio:budget-tracking PRY-201

PRY-201 tiene el presupuesto casi agotado en compromisos y el estado declarado en verde. Los términos ya estaban vigentes, así que no los volví a registrar. Las cifras salen del informe de avance del 2026-10-21 y las recalculé con `portafolio.py compute` al 2026-10-23.

| | COP | % del aprobado |
|---|---|---|
| Aprobado | 18.000.000.000 | 100 % |
| Comprometido | 16.735.307.598 | 93,0 % |
| Ejecutado | 6.108.769.631 | 33,9 % |
| Proyección al cierre | 18.209.304.767 | 1,2 % por encima del aprobado |

El disponible real (aprobado menos comprometido) es 1.264.692.402 COP.

- **Compromisos:** el comprometido pasa el umbral de 90 %. Con 33,9 % ejecutado, no hay holgura: casi todo está comprometido y falta que se cause.
- **Estado verde:** el informe declara verde con tres señales abiertas que no menciona. Son el comprometido sobre el umbral, un hito cumplido sin evidencia y 61 días de atraso contra la línea base original (14,1 %).
- **Avance:** el 67 % declarado solo lo respalda el extremo alto del plan, que sustenta entre 33 % y 67 %. Los hitos cumplidos son 1 de 3.
- **Solicitud de cambio CC-01:** pide 122.000.000 COP adicionales y dice "autorizada por el comité", sin nombre ni acta que la cite.
- **Sin dato:**
  - No hay presupuesto original y vigente por separado, así que no calculé desviación de costo.
  - Ningún documento dice si los 122.000.000 de CC-01 están dentro de los 18.000.000.000.
  - No hay detalle del comprometido por proveedor.
  - No hay evidencia del hito cumplido.

Puedo preparar la solicitud de cambio de presupuesto, porque la proyección excede el aprobado. El detalle por proveedor requiere que se aporten los contratos.

La corrida quedó registrada como `2026-10-23-budget-tracking-1`, con el informe completo en `estado/corridas/salida-budget-tracking.md`.