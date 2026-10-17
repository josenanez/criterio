# /criterio-portfolio:status-report PRY-203

Terminé el informe de PRY-203 y registré la corrida. Es el texto que guardé en `estado/corridas/salida-status-report.md`.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

## PRY-203 · Reposición automática, estado al 2026-10-17

Sale de la ficha `estado/records/PRY-203.json` (actualizada el 2026-10-17) y del cálculo de `portafolio.py compute`.

**Declara el gerente (Gustavo Neira):** Rojo, 26 %, al 2026-10-16.
**Sustento documental:** sustentado en lo esencial. El rojo coincide con el atraso que muestran los documentos. El 26 % no cuadra con el plan, y las cifras de dinero son solo declaración.
**Lo que el semáforo no explica:** `commitment_overdue`, `milestone_overdue` y `progress_vs_plan`.
**Último documento:** 2026-10-16 (1 día de silencio). **Última reunión:** 2026-10-14, Comité de Arquitectura.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2026-11-28 | 2026-11-28 | 0 días |
| Presupuesto aprobado | COP 3.300.000.000 | COP 3.300.000.000 | La proyección declarada (COP 3.114.019.216) queda 5,6 % por debajo de lo aprobado |

- **Replanificaciones:** 0 registradas.
- **Dinero, solo declarado:** comprometido COP 2.518.562.063 (76,3 %), ejecutado COP 1.891.245.411 (57,3 %), disponible real COP 781.437.937.

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |
|---|---|---|---|---|
| Diseño de la experiencia aprobado | 2026-06-15 | 2026-06-15 | cumplido | Acta de recibo del 2026-10-09 |
| Ambiente de pruebas certificado | 2026-08-09 | 2026-08-09 | cumplido | Acta de recibo del 2026-10-16 |
| Integración con el ERP | 2026-10-04 | 2026-10-04 | **vencido hace 13 días** | Ninguna |
| Piloto en tiendas | 2026-11-28 | 2026-11-28 | pendiente | Ninguna |

### Dónde no coincide
- **Avance contra plan:** el gerente declara 26 %. Con 2 de 4 hitos cumplidos, el plan sostiene entre 50 % y 75 %, una brecha de 24 puntos.
- **Reprogramación sin formalizar:** el informe del 2026-10-16 dice «se reprogramó el despliegue». No hay línea base nueva ni solicitud de cambio, y ninguna fecha de hito se movió.
- **Actas tardías:** las dos actas de recibo (2026-10-09 y 2026-10-16) son muy posteriores a las fechas base de sus hitos. Los documentos no dicen si el hito se cumplió a tiempo y el acta llegó tarde, o si se cumplió tarde.

### Abierto
- **Riesgo sin movimiento:** «El proveedor no ha confirmado la fecha de la última entrega». No tiene responsable, probabilidad, impacto ni fecha.
- **Compromiso vencido:** Andrés Lozano, «Entregar el punto 27», para el 2026-10-04 (13 días de atraso), sin evidencia de entrega. Se dijo en el comité del 2026-10-14, con la fecha ya pasada, y Andrés Lozano no figura entre los asistentes.
- **Dependencias:** ninguna registrada.

### Sin dato
- Producto: el acta dice «No aplica».
- Autoridad: sin ella no se puede juzgar si los riesgos exceden la del gerente.
- Fase.
- Proveedores: la ficha no tiene ninguno, aunque el informe habla de «la última entrega» de un proveedor.
- Los tres componentes del alcance no tienen nombre en el acta.

### Después
El hito del ERP vencido, el compromiso sin evidencia y la reprogramación sin línea base justifican un punto de comité. Si la reprogramación por el congelamiento de fin de año es real, corresponde una solicitud de cambio. Te dejo ambas opciones; no preparé ninguna.

**Pie:** criterio-portfolio 0.3.13 · ficha de PRY-203 del 2026-10-17, sobre 6 documentos · campos inciertos: producto, autoridad, fase · términos v1.1: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13

## Sobre el registro de la corrida

La corrida quedó registrada como `2026-10-17-status-report-1`, con 39 segundos medidos y `--caso PRY-203`.

Sus totales, sin embargo, cubren los 13 proyectos del portafolio (61 hallazgos). Solo las tres señales del bloque `por_caso` de PRY-203 corresponden a este informe. Esto viene de cómo `corrida` agrega, no de algo que yo haya hecho distinto.