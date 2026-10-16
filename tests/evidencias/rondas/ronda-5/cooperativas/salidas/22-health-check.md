# /criterio-portfolio:health-check PRY-204

## Diagnóstico · PRY-204 Tarjeta débito para asociados · 2026-10-16

**Leí:** 6 documentos, de 2025-10-24 a 2026-10-15. Son 2 md, 2 pdf, 1 xlsx y 1 csv. Busqué también en los textos de los otros 12 proyectos y ninguno menciona PRY-204. No quedó nada sin leer, pero el xlsx lo leí por su conversión a texto, no abriendo el original.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no hubo que registrarlos de nuevo.

### Dictamen
**Sostenido:** 4 · **Sin sustento:** 6 · **Contradicho:** 5 (15 afirmaciones en total).

- **Sostenidas:**
  - Presupuesto aprobado de 18.000.000.000 COP.
  - Patrocinador, gerente y comité nombrados en el acta.
  - Piloto con acta de recibo del 2026-10-15.
  - Los +115 días de CC-01, que coinciden con el cronograma v2.
- **Sin sustento:**
  - Tres hitos «cerrados» sin acta de recibo: diseño funcional, ambiente de pruebas e integración con el core.
  - Comprometido y ejecutado, porque no hay contratos ni facturas.
  - La proyección al cierre.
  - La frase «autorizada por el comité» de CC-01.
- **Contradichas:**
  - Estado «verde».
  - Avance de 83 %.
  - Fecha vigente del piloto.
  - «Dependencias: ninguna».
  - Cierre comprometido el 2026-10-18.

La carpeta no permite diagnosticar el proyecto como verde. Lo que sí permite decir es que su estado declarado no está sustentado.

### Gobierno
| | Qué dice el documento |
|---|---|
| Patrocinador | Ricardo Salas |
| Gerente | Diana Molina |
| Autoridad declarada | **No declarada** |
| Comité | Comité de Riesgos, sin ninguna minuta en la carpeta |

El alcance del acta son «Componente 1, 2, 3». Por eso «ampliación de alcance» en CC-01 no tiene contra qué medirse. Sin autoridad declarada no hay desviación aprobada.

### Contra el plan
- **Línea base original:** el piloto estaba para el 2026-09-09 y el cierre para el 2026-10-18.
- **Cronograma v2 (2026-10-12):** el piloto pasa al 2027-01-02, sin motivo ni nueva fecha de cierre.
- **Desviación:** 115 días contra la línea base original (37.1 %).
- **CC-01** (2026-10-13): +115 días y +230.000.000 COP, «autorizada por el comité», sin fecha ni acta. El cronograma v2 es un día anterior a la solicitud que lo justifica.
- **Piloto:** el cronograma v2 lo marca «cerrado» con fecha vigente futura (2027-01-02), pero el acta de recibo es del 2026-10-15.

### Hitos vencidos sin evidencia
| Hito | Fecha | Días | Documento esperado |
|---|---|---|---|
| Diseño funcional aprobado | 2026-01-19 | 270 | Acta de recibo del diseño |
| Ambiente de pruebas certificado | 2026-04-07 | 192 | Certificado o acta de recibo |
| Integración con el core | 2026-06-23 | 115 | Acta de recibo o pruebas de integración |

El acta de recibo del piloto la firma solo la gerente. No trae resultados del piloto ni aceptación del patrocinador.

### Dinero (COP)
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 18.000.000.000 | 12.906.403.597 (71.7 %) | 4.779.778.113 (26.6 %) | 20.519.654.277 (14.0 % sobre lo aprobado) | 5.093.596.403 |

Las cifras vienen del informe del gerente y ningún documento las respalda. Ningún documento muestra el presupuesto aprobado modificado por los 230.000.000 de CC-01, y no hay cifra calculada que lo reconcilie con la proyección.

### Lo que se dijo y nadie registró
No hay minutas del proyecto, así que no hay compromisos que extraer. Hay un riesgo sin probabilidad, impacto, responsable ni fecha: la dependencia del proveedor del core. El acta, en cambio, dice «Dependencias: ninguna».

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Verde | Informe del 2026-10-12 | El mismo informe (+14.0 % de proyección) y el cronograma v2 (+115 días) |
| Avance 83 % | Informe | Cronograma con 4 de 4 hitos cerrados (brecha de 17.0 puntos) |
| Piloto vigente 2027-01-02 y «cerrado» | Cronograma v2 | Acta de recibo del 2026-10-15 |
| Dependencias: ninguna | Acta | Riesgo abierto en el informe e hito de integración con el core |
| Cierre 2026-10-18 | Acta | Cronograma v2 con un hito en 2027-01-02 |

El informe no menciona ni el movimiento del piloto ni CC-01.

### Lo que esta carpeta no permite saber
- Si diseño, pruebas e integración se entregaron: sin actas, no se puede medir el avance real.
- Qué se amplió en el alcance, y si 115 días y 230.000.000 COP son razonables.
- Quién autorizó el desvío, y si el cronograma v2 es una línea base aprobada.
- En qué se gastó el dinero.
- Por qué se movió el piloto, y cuál es la fecha real de cierre.
- Si el piloto funcionó.

No recomiendo detener, continuar ni reestructurar; eso lo decide quien tiene la facultad. Puedo preparar el punto de comité con la lista de lo que falta, o llevarle a Diana Molina las cinco contradicciones como preguntas, una por una.

**Corrida registrada:** `2026-10-16-health-check-1`, caso PRY-204, 69 s. La salida completa quedó en `estado/corridas/salida-health-check.md`.

**Pie de rigor:** las cifras derivadas salen de `portafolio.py compute`. Las demás son transcripción de los documentos citados. Criterio produce borradores de trabajo y la verificación es suya.