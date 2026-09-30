---
description: Estado de un proyecto contra su plan, separando lo que el gerente declara de lo que sustentan los documentos
argument-hint: "<código o nombre del proyecto>"
---

# /status-report — Estado de un proyecto

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el informe.
> Abre declarando de qué ficha sale y de cuándo. Cierra con el pie: versión, ficha aplicada con su fecha, campos inciertos y enlace a los términos.

## Antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/status-report PRY-014
/status-report originación digital
```

## Flujo

**1. Carga la ficha.** Si no existe, ofrece correr `/portfolio-scan` para ese proyecto. No improvises un estado leyendo documentos sueltos.

**2. Separa declaración de evidencia.** Aplica **project-record**. Lo que el gerente afirma va en una columna; lo que sustentan los documentos, en otra. **Nunca las fusiones.**

El script ya hizo la comparación: `declared.unaccounted_signals` trae las señales que el semáforo declarado no explica, y la alerta `declared_vs_evidence` aparece cuando el gerente reporta verde y hay evidencia que ese verde no cubre. **No la vuelvas a juzgar a ojo: cítala.** Si la declaración lleva más de un mes, `declaration_stale` lo dice y hay que decirlo también: un verde de hace seis semanas no es un verde.

**3. Mide.** Aplica **baseline-variance**: desviación contra la línea base original y contra la vigente, con el número de replanificaciones. Hitos con su fecha de línea base, su fecha vigente y si hay evidencia de cumplimiento.

**4. Revisa lo abierto.** Aplica **raid-taxonomy** y **commitment-tracking**: qué RAID sigue sin movimiento y qué compromisos vencieron sin evidencia.

**5. Lee el silencio.** Días desde el último documento y desde la última reunión. Un proyecto que reporta verde y lleva cinco semanas sin un documento es el caso que este informe existe para mostrar.

## Salida

```markdown
## [Proyecto] — estado al [fecha]

**Declara el gerente:** [estado] · [avance]% · al [fecha de la declaración]
**Sustento documental:** [sustentado | sin sustento | contradicho]
**Lo que el semáforo no explica:** [señales de `declared.unaccounted_signals`, o «nada»]
**Último documento:** [fecha] · **Última reunión:** [fecha]

### Contra el plan
| | Línea base original | Vigente | Desviación |
| Fecha de cierre | | | |
| Presupuesto | | | |

Replanificaciones: [N] — [fechas y motivos declarados]

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |

### Dónde no coincide
[Lo declarado frente a lo que dicen los documentos, con las dos fuentes y fechas. Si coincide todo, se dice en una línea.]

### Abierto
**Riesgos e incidencias sin movimiento:** [lista con días]
**Compromisos vencidos:** [quién, qué, desde cuándo]
**Dependencias sin confirmar:** [de qué proyecto]

### Sin dato
[Campos en `not_found` que importan para juzgar este proyecto.]
```

## Después

Si hay desviación por encima del umbral o riesgos que exceden la autoridad del gerente, ofrece preparar el punto de comité. Si el atraso viene de un cambio no formalizado, ofrece la solicitud de cambio.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/portafolio.py corrida --state <estado> --what status-report \
    --salida <estado>/corridas/salida-status-report.md \
    --caso <código del proyecto> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-status-report.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
