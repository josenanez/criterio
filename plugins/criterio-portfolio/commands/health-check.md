---
description: Diagnostica un proyecto desde cero contra la evidencia, sin asumir nada de lo que diga su informe de avance
argument-hint: "<código o nombre del proyecto>"
---

# /health-check — Diagnóstico de un proyecto

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el diagnóstico.
> Abre declarando cuántos documentos leíste y de qué fechas. Cierra con el pie de rigor.

## Antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/health-check PRY-014
/health-check originación digital
```

## En qué se diferencia de `/status-report`

`/status-report` parte de la ficha y dice qué cambió. **Este parte de cero y dice qué es
verdad**, sin asumir nada del informe de avance, que lo escribe quien está siendo evaluado.

Se corre dos o tres veces al año por proyecto: cuando algo no cuadra, cuando llega un
gerente nuevo, o cuando el comité pide una segunda opinión.

## Flujo

Aplica **project-diagnosis** de principio a fin, en su orden, que no es negociable porque
cada paso decide si el siguiente tiene respuesta posible.

**1. Lee todo.** No solo la carpeta del proyecto: también lo que otras minutas digan de él.
Reporta de entrada cuántos documentos, qué formatos y cuáles no pudiste leer.

**2. Gobierno.** Aplica **governance-artifacts**. Acta, patrocinador con nombre, autoridad
del gerente, comité. Sin autoridad declarada no hay desviación aprobada: hay fechas que
alguien escribió.

**3. Contra qué se mide.** Aplica **baseline-variance**. Si no hay línea base, el
diagnóstico de desviación termina ahí y se dice.

**4. Las cuatro cifras.** Nunca ejecutado contra aprobado a secas.

**5. La evidencia de cada hito vencido.** Es donde se cae un proyecto en verde.

**6. El silencio, y de quién es.** Del proyecto entero o solo de quien reporta.

**7. Lo dicho y no registrado.** Aplica **raid-taxonomy** y **commitment-tracking** sobre
las minutas.

**8. Dictamina cada afirmación**: sostenida, sin sustento, o contradicha. Y reporta el
conteo de los tres.

## Salida

```markdown
## Diagnóstico · [Proyecto] · [fecha]

**Leí:** [N] documentos · [rango de fechas] · formatos: [lista]
**No pude leer:** [cuáles y por qué]

### Dictamen
**Sostenido:** [N] afirmaciones · **Sin sustento:** [N] · **Contradicho:** [N]

[Un párrafo. Qué se puede afirmar de este proyecto desde su carpeta, y qué no.]

### Gobierno
| | Qué dice el documento | Fuente |
| Patrocinador | | |
| Gerente | | |
| Autoridad declarada | | |
| Comité | | |

### Contra el plan
[Línea base original, vigente, replanificaciones con motivo. O: no hay línea base.]

### Hitos vencidos sin evidencia
| Hito | Fecha | Días | Qué documento se esperaría |

### Dinero
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |

### Lo que se dijo y nadie registró
[Riesgos, compromisos y dependencias que están en minutas y no en ningún registro.]

### Contradicho
| Afirmación | Documento A | Documento B |

### Sin sustento
[Lo que nada contradice y nada respalda. Es el bloque más largo casi siempre.]

### Lo que esta carpeta no permite saber
[Con la consecuencia concreta de cada ausencia.]
```

## Después

No recomiendes detener, continuar ni reestructurar: eso lo decide quien tiene la facultad.

Si el dictamen es que la carpeta no permite diagnosticar, **dilo como resultado y no como
disculpa**, y ofrece preparar el punto de comité con la lista de lo que falta.

Si aparecieron contradicciones, ofrece llevarlas al gerente como preguntas, una por una.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/portafolio.py corrida --state <estado> --what health-check \
    --salida <estado>/corridas/salida-health-check.md \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-health-check.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
