---
description: Informe consolidado de portafolio a partir de las fichas — qué cambió, qué se contradice, qué está en silencio y qué no tiene sustento
argument-hint: "[ppt|pdf|html] o vacío para el formato configurado"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /portfolio-report — Informe de portafolio

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
Consolida las fichas y responde lo que el gerente de PMO no puede saber leyendo proyecto por proyecto.

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el informe.
> Abre declarando qué fichas cargó y su fecha. Cierra con el pie: versión, fichas aplicadas con su fecha, campos inciertos y enlace a los términos.


## Lo primero, antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición, y la promesa que estas páginas publican se mide en minutos.

## Invocación

```
/portfolio-report              formato configurado
/portfolio-report ppt          material para presentar
/portfolio-report html         las dos vistas, para consultar y para imprimir
```

## Si el formato es `html`

No lo escribas tú. El informe impreso lo arma un script, con el diseño del producto:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/informe.py" --state <estado> --salida <carpeta> --config <archivo>
```

Produce **dos vistas que no se diferencian por detalle sino por autoridad**, y una
página por proyecto:

- `index.html` — **por campo**, con la cadena de evidencia completa. Para quien va a
  actuar, que necesita poder abrir el documento del que salió cada dato.
- `decisiones.html` — **por decisión**, para el patrocinador. Solo lo que excede la
  facultad de quien gerencia, formulado como pregunta cerrada y con la consecuencia de
  no decidir.

La segunda no es la primera recortada: es otro objeto. A un patrocinador se le entrega
la interna filtrada y hace lo que hacen los patrocinadores — se clava en un detalle y
desvía el comité.

**El PDF sale de imprimir el HTML**, que está construido para eso (`@media print`, modo
claro, sin cortar tablas ni bloques a mitad de página). No hay un generador de PDF: una
librería de PDF rompería la propiedad de que todo esto corre sin instalar nada.

Después de correrlo, di dónde quedaron los archivos y cuál de las dos vistas va a cada
audiencia. **No pegues el HTML en la conversación.**

## Flujo

**1. Carga y verifica frescura**

Lee todas las fichas de `estado/fichas/`. Si alguna tiene más de una semana sin barrido, dilo en el banner de apertura y ofrece correr `/portfolio-scan` antes. No produzcas un informe de portafolio sobre fichas viejas sin advertirlo.

**2. Diff contra la instantánea anterior**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" diff --state <estado>
```

Es lo primero que se calcula y lo primero que se reporta. **Qué cambió** es lo único que el gerente no sabe ya.

Si no hay instantánea previa, dilo: este es el punto de partida, no hay delta.

**3. Cruza el portafolio**

Aquí está el valor que no existe proyecto por proyecto:

- **Dependencias rotas.** Un proyecto declara depender de otro, por código, y ese otro movió la fecha.
- **Contradicciones.** Campos en `ambiguous`, con las dos fuentes y las dos fechas.
- **Cambios de gobierno.** Una persona distinta en un rol respecto de la corrida anterior, o respecto del acta.
- **Recursos y patrocinadores repetidos** en proyectos que compiten por la misma fecha.

**4. Aplica el juicio**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" compute --state <estado> --config <pmo.config.json>
```

Devuelve los números y la lista de señales que cruzaron umbral. Aplica **portfolio-health** para leer qué significa cada una, y **baseline-variance** para las desviaciones. El script ya calculó; aquí se decide qué merece aparecer y en qué orden.

**No recalcules nada a mano.** Si un número del informe no sale del script, está inventado.

**5. Arma la confirmación del mes**

Si toca, aplica la confirmación periódica: **cinco campos**, los más viejos entre los que importan. Van al final, como preguntas cerradas.


## Deja la corrida registrada

Lo último, siempre, y con la ruta real del informe:

Antes de `corrida`, escribe en `<estado>/corridas/salida-portfolio-report.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what portfolio-report \
    --salida <estado>/corridas/salida-portfolio-report.md \
    --docs <carpeta de documentos> --informe <dónde quedó el informe> \
    --nota "qué hay que mirar de esta corrida"
```

Sin esto la corrida no se puede compartir ni comparar: el informe queda en una carpeta que hay que recordar, y la del mes que viene no tiene contra qué medirse. Con esto, `<estado>/corridas/<fecha>-portfolio-report-<n>.md` dice qué se corrió, qué encontró por señal, dónde está el informe, y cuántos hallazgos más o menos que la vez anterior.

## Salida

```markdown
# Portafolio — [fecha]
[N] proyectos · [N] con hallazgos · último barrido [fecha]

## Qué cambió desde [fecha anterior]
[Si no hay nada: "Sin cambios desde la corrida anterior." Y se acaba la sección.]

## Contradicciones abiertas
| Proyecto | Campo | Dice | Fuente | Dice también | Fuente |

## Hitos vencidos sin evidencia
| Proyecto | Hito | Fecha | Días | Última mención |

## Proyectos en silencio
| Proyecto | Días | Último documento |

## Dependencias en riesgo
| Proyecto | Depende de | Qué pasó |

## Sin sustento
| Proyecto | Declara | Qué lo respalda |

## Vacíos de información
| Proyecto | Qué falta |

## Estado general
| Proyecto | Declarado | Sustento | Desviación vs original | vs vigente | Replanificaciones |

## Necesito que confirmes
[Cinco preguntas cerradas, o ninguna si no toca este mes.]
```

**El orden no es negociable.** Lo que cambió va primero porque es lo único nuevo. El estado general va casi al final porque es lo que el gerente ya cree saber.

Si una sección no tiene contenido, se escribe que está vacía en una línea y se sigue. No se omite: que no haya contradicciones abiertas es información.

## Después

Ofrece el material de comité si hay uno próximo, o entrar al detalle de los proyectos con hallazgos.
