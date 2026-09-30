---
description: Reconstruye qué pasó en un proyecto desde sus documentos, con la línea de tiempo y el momento en que la evidencia dejó de sostener lo reportado
argument-hint: "<código del proyecto> [desde AAAA-MM]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /project-history — Qué pasó aquí

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes la historia.
> Abre declarando cuántos documentos leíste y qué período cubren. Cierra con el pie de rigor.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/project-history PRY-014
/project-history PRY-014 desde 2025-06
```

## Flujo

**Antes de escribir una cifra, recalcula.**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" compute --state <estado> --config <config>
```

Toda cifra derivada —porcentaje, desviación, días, suma, conteo de señales— se copia de esa salida, con todos sus dígitos. Si el script no la da, no se escribe: se dice qué dato falta para poder calcularla.

Aplica **portfolio-history**.

**1. Ordena los documentos por fecha**, la del documento y no la de su contenido. Un acta
de marzo que habla de enero se ubica en marzo y se anota la referencia. **La distancia
entre cuándo pasó algo y cuándo quedó escrito suele ser el hallazgo.**

**2. Arma la línea de tiempo.** Fecha, documento, qué cambió. Sin interpretación: esa va
después y va aparte.

**3. Las replanificaciones.** Aplica **baseline-variance**. Cuántas, cuándo, motivo
declarado, documento que las aprobó, y el atraso acumulado contra la línea base original.
Una sin motivo documentado se nombra como tal.

**4. Los cambios de gobierno.** Patrocinador, gerente, comité. Aparecen en correos y
minutas, no en actas reexpedidas.

**5. Los compromisos que se repitieron.** Aplica **commitment-tracking**. Mismo doliente,
lo mismo, fecha nueva cada vez.

**6. El punto de separación.** Recorre la serie de estados declarados y marca desde cuándo
lo declarado dejó de tener sustento. Casi nunca es un salto: es un deslizamiento.

## Salida

```markdown
## Historia · [Proyecto] · [período]

**Leí:** [N] documentos entre [fecha] y [fecha]
**Trimestres sin un solo documento:** [cuáles, o ninguno]

### En una línea
[Qué pasó con este proyecto. Un párrafo, con las fechas que importan.]

### Las cuatro cifras
| Replanificaciones | Atraso acumulado vs. original | Meses declarando sin sustento | Cambios de gobierno |

### Línea de tiempo
| Fecha | Documento | Qué cambió |

### Replanificaciones
| Nº | Fecha | Fecha de cierre nueva | Motivo declarado | Documento que la aprobó |

### Gobierno
| Fecha | Qué cambió | Documento |

### Compromisos que se repitieron
| Doliente | Qué | Veces | Fechas prometidas |

### Desde cuándo lo declarado no se sostiene
[La fecha, el primer hito sin evidencia, y qué se siguió reportando después.]

### Lecciones ancladas a un hecho
[Cada una con hecho, fecha y efecto. Si no se puede anclar, no va.]
```

## Después

**No atribuyas intención.** Que el atraso quedara oculto no dice que alguien lo ocultara: la
historia sirve para tener esa conversación con datos en vez de con memorias, y quién la
tiene es una persona.

Ofrece llevar la historia al cierre del proyecto, o al comité si hay una decisión que sale
de ella.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what project-history \
    --salida <estado>/corridas/salida-project-history.md \
    --caso <código del proyecto> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-project-history.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
