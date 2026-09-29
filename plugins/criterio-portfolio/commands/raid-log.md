---
description: Levanta o actualiza el registro de riesgos, supuestos, incidencias y dependencias, incluidos los que se dijeron en reuniones y nadie registró
argument-hint: "<código del proyecto> o 'portafolio' para el consolidado"
---

# /raid-log — Registro RAID

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el registro.
> Abre declarando de qué documentos sale. Cierra con el pie de rigor.

## Antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/raid-log PRY-014
/raid-log portafolio
```

## Flujo

**1. Carga lo registrado.** El RAID que ya está en la ficha, con su historial de movimiento.

**2. Busca lo que nadie registró.** Aplica **raid-taxonomy** sobre minutas, transcripciones e informes de avance. Las reuniones están llenas de riesgos dichos al pasar que nunca llegaron al registro: *"si el proveedor no entrega en octubre estamos en problemas"*.

Cada uno entra citando la reunión y la fecha, marcado como **no registrado formalmente**, para que el gerente decida si lo formaliza. No inventes riesgos que nadie mencionó.

**3. Clasifica bien.** La prueba rápida: si ya pasó, es incidencia. Si depende de alguien fuera del proyecto, es dependencia. Si se está asumiendo sin verificar, es supuesto. Lo que queda es riesgo.

Un ítem mal clasificado en el registro existente se reclasifica y se dice por qué.

**4. Revisa lo abierto.** Ítems sin doliente, sin fecha, sin movimiento en dos períodos, o con mitigación vencida sin evidencia. Falta de doliente y de fecha se reporta como hallazgo; no se rellena.

**5. Cruza dependencias.** Cada dependencia lleva el código del proyecto del que depende. Si ese proyecto movió su fecha, la dependencia queda en riesgo y se dice.

## Salida

```markdown
## RAID — [proyecto o portafolio] al [fecha]
[N] riesgos · [N] supuestos · [N] incidencias · [N] dependencias
[N] sin doliente · [N] sin movimiento · [N] no registrados formalmente

### Necesitan decisión ahora
| Id | Tipo | Qué | Doliente | Desde | Por qué sube |

### Detectados en reuniones, no registrados
| Qué | Tipo | Dicho en | Fecha |

### Sin doliente o sin fecha
| Id | Tipo | Qué | Qué falta |

### Dependencias en riesgo
| Id | Depende de | Confirmada | Qué pasó |

### Registro completo
| Id | Tipo | Qué | Prob. | Impacto | Doliente | Fecha | Último movimiento |
```

## Después

Ofrece subir a comité los que cumplen el criterio de escalamiento, y proponer doliente para los que no tienen — proponer, no asignar.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/portafolio.py corrida --state <estado> --what raid-log \
    --salida <estado>/corridas/salida-raid-log.md \
    --caso <código del proyecto> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-raid-log.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
