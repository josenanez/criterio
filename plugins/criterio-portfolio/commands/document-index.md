---
description: Dice qué documentos cambiaron de verdad, qué hay que releer y qué citas dejaron de resolver
argument-hint: "[código del proyecto]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /document-index — Qué cambió en la carpeta

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla.
> Este comando no lee documentos: los cuenta y los compara. Es el paso que decide el costo de todo lo demás.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/document-index                          toda la carpeta
/document-index PRY-014                  solo lo que toca a un proyecto
```

## Flujo

**1. Corre el índice.** Aplica **document-intake**.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" index --state <estado> --docs <documentos>
```

**1b. Lo que hay que releer no se lee aquí.** Quien lo lee es el barrido, con el plan que arma `plan-lectura` a partir de este mismo índice: por lotes, con tope y en el orden configurado. Este comando dice el tamaño del trabajo; el barrido lo hace.

**2. Reporta lo que hay que releer, no lo que cambió.** Son cosas distintas y la
diferencia es el valor de este comando: un documento reguardado cambió de hash y no de
contenido, y releerlo es gastar por nada.

**3. Nombra las citas que dejaron de resolver.** Aplica **project-record**. Cada una con su
proyecto y su campo. Una cita rota es un dato que el informe sigue mostrando como
sustentado y ya no lo está.

**4. Ofrece el barrido solo de lo tocado.** Nunca el portafolio completo porque cambió un
archivo. La lista `projects_to_recompute` dice cuáles.

**5. Si hay renombrados, ofrece corregir las citas** de las fichas afectadas, una por una y
mostrando el cambio. No se reescribe una ficha en silencio.

## Salida

```markdown
## Carpeta al [fecha]

**Documentos:** [N] · **Sin cambio:** [N] · **Hay que releer:** [N]

### Cambió el contenido
| Documento | Proyectos |

### Solo se reguardó
[Cambiaron los bytes y no el texto. No se relee. N documentos.]

### Renombrado o movido
| Antes | Ahora | Proyectos |

### Ya no está
| Documento | Proyectos |

### Citas que dejaron de resolver
| Proyecto | Campo | Documento citado |

### Formatos que no se pudieron leer
[Cuáles y por qué. Nada se salta en silencio.]
```

## Después

Si `hay que releer` es cero y no hay citas rotas, dilo en una línea y **no produzcas nada
más**. Una corrida donde no pasó nada se contesta con una línea, no con un informe.

Si hay documentos por releer, ofrece `/portfolio-scan` limitado a los proyectos tocados.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what document-index \
    --salida <estado>/corridas/salida-document-index.md \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-document-index.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
