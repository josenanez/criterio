# `/criterio-portfolio:portfolio-report` · día 1

Corrido el 2026-09-28 · ? s · 146 documentos leídos · 158 hallazgos

**Lo que dijo que no sabía:** nombró tres vacíos de información en vez de rellenarlos: escalamiento en 50, producto en 21, línea base en 4

---

## Portafolio — 28 de septiembre de 2026

50 proyectos · 43 con hallazgos · $303.100M COP aprobados

| Cifra | Valor | Contra la clave |
|---|---|---|
| Alertas totales | 158 | ✓ 158 |
| Verdes que la evidencia no sostiene | 30 de 33 | ✓ 30, sobre 33 verdes |
| Hitos cerrados sin evidencia | 128 en 43 proyectos | ✓ 128 |
| Semáforo declarado | 33 verde · 17 amarillo | ✓ |
| Sin línea base | 4 · PRY-200, 205, 224, 232 | ✓ los mismos |
| Comprometido | 135.381.389.421 | ✓ exacto |
| Proyección al cierre | 301.365.242.635 (−0,6%) | ✓ exacto |
| **Aprobado (tabla de detalle)** | **303.100.000.000.000** | **✗ mil veces la cifra real** |

Secciones del informe: qué cambió desde la corrida anterior · contradicciones abiertas ·
hitos vencidos sin evidencia · proyectos en silencio (ninguno) · dependencias en riesgo
(ninguna declarada) · sin sustento · inconsistencia cruzada · vacíos de información ·
estado general · para el comité.

Vacíos que reportó en vez de rellenar: autoridad de escalamiento ausente en los 50
proyectos, producto asociado ausente en 21, línea base ausente en 4.

Produjo 65 páginas HTML en `.pruebas/corp-demo/reportes/`: index, decisiones, proyectos,
productos, y una por proyecto.

### Los dos defectos que dejó ver

1. **La cifra transcrita.** El aprobado salió mil veces mayor en la tabla de detalle,
   mientras el resumen del mismo informe y la desviación calculada usaban la cifra correcta.
   El script tenía razón; el error fue volver a teclear un número ya calculado.
2. **Dos secciones que se desmienten.** Dijo «sin contradicciones entre documentos de un
   mismo proyecto» y tres párrafos después listó 8 incompatibilidades bajo una sección
   inventada, porque `contradiction` estaba definida como «el mismo campo dicho distinto» y
   esto son dos campos cuya combinación es imposible.
