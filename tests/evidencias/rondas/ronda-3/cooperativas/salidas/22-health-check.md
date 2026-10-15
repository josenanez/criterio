# /criterio-portfolio:health-check PRY-202

## Diagnóstico · PRY-202 Core cooperativo · 2026-10-15

**Leí:** 7 documentos del proyecto, del 2025-05-17 al 2026-10-15. Formatos: md (5), csv (1), xlsx (1).

**No pude leer:** los .pdf, .docx y .xlsx de las otras carpetas no entraron en la búsqueda de menciones de PRY-202, que solo cubrió md y csv. En lo que sí cubrí, ningún documento de otro proyecto habla de PRY-202. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

### Dictamen
**Sostenido:** 4 afirmaciones · **Sin sustento:** 7 · **Contradicho:** 3

La carpeta confirma quién patrocina y gestiona el proyecto, cuánto se aprobó y cuál fue el plan original. No permite afirmar el verde. El informe declara 76 % de avance, y el cronograma v2, fechado el mismo día, tiene los 4 hitos cerrados (100 %). Ningún dato de la ficha viene de un documento de evidencia.

### Gobierno
| | Qué dice el documento |
|---|---|
| Patrocinador | Ricardo Salas (acta 2025-05-17) |
| Gerente | Camilo Beltrán (acta 2025-05-17) |
| Autoridad declarada | **No está.** |
| Comité | Consejo de Administración (acta 2025-05-17). Salas y Beltrán asistieron el 2026-10-15. |

### Contra el plan
- La línea base original es de 2025-05-17. Sus fechas son el cierre 2026-04-14 (acta) y el piloto 2026-03-09 (cronograma v1).
- La v2 (2026-10-14) mueve solo el piloto, al 2026-07-06, y no trae motivo.
- La desviación es de 119 días, 41,6 %, contra la original, y de 0 contra la vigente.
- CC-01 (2026-10-02) pide +119 días y 238.000.000 COP por una ampliación de alcance. Dice «autorizada por el comité», sin nombre ni fecha ni acta.
- La nueva fecha del piloto ya había pasado tres meses antes de la solicitud.
- El alcance sigue igual y el presupuesto aprobado no incorpora la ampliación.
- El criterio de éxito («en producción y medido») no corresponde a ningún hito.

### Hitos vencidos sin evidencia
| Hito | Fecha | Días |
|---|---|---|
| Ambiente de pruebas certificado | 2025-10-17 | 363 |
| Integración con el core cooperativo | 2025-12-27 | 292 |
| Piloto con asociados | 2026-07-06 | 101 |

«Diseño funcional aprobado» sí tiene acta, pero el recibo es del 2026-10-06 y el cronograma lo da por cerrado el 2025-08-06. Además lo recibe el propio gerente.

### Dinero (COP)
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 2.400.000.000 | 1.390.493.898 | 876.426.100 | 2.493.540.214 | 1.009.506.102 |

Está comprometido el 57,9 % y ejecutado el 36,5 %. La proyección excede lo aprobado en 3,9 %. Las cuatro cifras salen solo del informe de avance. Los 238.000.000 de CC-01 no están sumados, y nada dice si la proyección los incluye.

### Lo que se dijo y nadie registró
No hay ningún registro RAID. Estas son las cosas que aparecen en documentos pero no en un registro:
- **Hallazgo de seguridad** en la revisión de arquitectura, sin responsable ni gravedad.
- **Cambio normativo del supervisor** como riesgo, sin probabilidad, impacto ni dueño.
- **Dependencia del proveedor del core**, que contradice el «Ninguna declarada» del acta.
- **Ajuste del reglamento** pedido por el Consejo antes del piloto, sin responsable ni fecha.
- **Compromiso de Óscar Ramírez** de entregar el «punto 35» para el 2026-10-27. Está abierto, no vencido, y ningún documento dice qué es el punto 35.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Avance 76 % | Informe 2026-10-14 | Cronograma v2: 4 de 4 hitos cerrados |
| Piloto cerrado el 2026-07-06 | Cronograma v2 | Informe: el Consejo pidió ajustar el reglamento «antes del piloto» |
| Diseño funcional cerrado el 2025-08-06 | Cronogramas v1 y v2 | Acta de recibo del 2026-10-06 |

### Sin sustento
- El estado «Verde». Las señales abiertas son desviación de 41,6 %, tres hitos sin evidencia y una brecha de 24 puntos de avance.
- Los hitos «Ambiente de pruebas» e «Integración».
- La aprobación de CC-01.
- Comprometido, ejecutado y proyección.
- Los dos riesgos del informe.
- El hallazgo de seguridad.

### Lo que esta carpeta no permite saber
- **Si el piloto ocurrió.** Sin acta ni informe, no se sabe si el avance real es 100 %, 76 % u otro.
- **Si el proyecto tenía autoridad para mover sus fechas.** Sin autoridad declarada no hay desviación aprobada.
- **Quién aprobó CC-01 y v2, y por qué se replanificó.**
- **Qué incluye la ampliación de alcance.**
- **Si el gasto es real.** No hay ejecución presupuestal ni contratos que respalden las cuatro cifras.
- **Qué tan grave es el hallazgo de seguridad.**

No recomiendo detener, continuar ni reestructurar; eso lo decide quien tiene la facultad. Puedo preparar el punto de comité con la lista de lo que falta, o llevar a Camilo Beltrán las tres contradicciones como preguntas, una por una.

*Pie de rigor: las cifras derivadas están copiadas del cálculo de la corrida, y todo lo demás sale de los 7 documentos citados. Es un borrador de trabajo y la verificación es de quien lo lee.*

La corrida quedó registrada como `2026-10-15-health-check-1`, con la salida completa en `estado/corridas/salida-health-check.md`. Tardó 81 segundos. El script no pudo medir el número de documentos, así que ese campo quedó vacío.