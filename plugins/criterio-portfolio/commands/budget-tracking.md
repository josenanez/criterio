---
description: Presupuesto aprobado, comprometido, ejecutado y proyección, con la desviación contra la línea base original y la vigente
argument-hint: "<código del proyecto> o 'portafolio' para el consolidado"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /budget-tracking — Presupuesto

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el informe.
> Abre declarando de qué documentos sale y de cuándo. Cierra con el pie de rigor.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/budget-tracking PRY-014
/budget-tracking portafolio
```

## Flujo

**Antes de escribir una cifra, recalcula.**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" compute --state <estado> --config <config>
```

Toda cifra derivada —porcentaje, desviación, días, suma, conteo de señales— se copia de esa salida, con todos sus dígitos. Si el script no la da, no se escribe: se dice qué dato falta para poder calcularla.

**1. Las cuatro cifras, ninguna asumida.** Aplica **baseline-variance**: aprobado, comprometido, ejecutado, proyección. Cada una con su fuente y su fecha. Si una no está declarada en ningún documento, va `not_found` y el informe lo dice.

**2. El error que hay que nombrar.** Reportar ejecutado contra aprobado ignorando el comprometido. Un proyecto con 40% ejecutado y 95% comprometido **no tiene holgura**: tiene el presupuesto agotado y todavía no se ha causado.

**3. Trata la proyección como lo que es.** Una declaración, no un dato duro. Lleva fuente y fecha como cualquier otro campo, y si es más vieja que el último movimiento de presupuesto, se dice.

**4. No mezcles monedas.** Si hay contratos en otra moneda, se reporta por separado. Si hay que convertir, se declara la tasa y su fecha. Nunca se convierte en silencio.

**5. Cruza contra el avance.** Presupuesto ejecutado muy por encima del avance de hitos es la señal que este informe existe para dar. Y al revés: ejecución muy por debajo a mitad de proyecto suele ser trabajo hecho y no facturado, que aparecerá de golpe.

## Salida

```markdown
## Presupuesto — [proyecto o portafolio] al [fecha]
**Moneda:** [código] [si hay más de una, se listan por separado]

| | Monto | % del aprobado | Fuente | Fecha |
| Aprobado | | | | |
| Comprometido | | | | |
| Ejecutado | | | | |
| Proyección al cierre | | | | |

**Disponible real** (aprobado menos comprometido): [monto]

### Contra la línea base
| | Original | Vigente | Desviación |
Replanificaciones de presupuesto: [N]

### Ejecución frente a avance
Ejecutado [X]% · Hitos cumplidos [Y] de [Z] · [lectura en una línea]

### Alertas
[Comprometido por encima del umbral, proyección que excede el aprobado, ejecución desalineada del avance.]

### Sin dato
[Cifras no declaradas en ningún documento.]
```

## Después

Si la proyección excede el aprobado, ofrece preparar la solicitud de cambio. Si el comprometido está cerca del tope, ofrece el detalle por proveedor.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what budget-tracking \
    --salida <estado>/corridas/salida-budget-tracking.md \
    --caso <código del proyecto> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-budget-tracking.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
