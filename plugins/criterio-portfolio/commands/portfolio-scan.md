---
description: Lee la carpeta de documentación de proyectos y produce o actualiza una ficha por proyecto, con cita a la fuente de cada dato
argument-hint: "[ruta de la carpeta] o vacío para usar la configurada"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /portfolio-scan — Barrido de la documentación

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
Puerta de entrada del plugin. Convierte una carpeta desordenada de documentos en fichas consultables.

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes fichas ni informe.
> Abre declarando qué encontró y cierra con el pie: versión, fichas tocadas, campos en `not_found` y enlace a los términos.


## Lo primero, antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición, y la promesa que estas páginas publican se mide en minutos.

## Invocación

```
/portfolio-scan                          usa la ruta de pmo.config.yaml
/portfolio-scan ~/PMO/proyectos          barre esa carpeta
/portfolio-scan PRY-014                  vuelve a barrer un solo proyecto
```

## Flujo

Aplica también **baseline-variance** —cada versión del cronograma es una línea base y cada solicitud de cambio un registro en `changes`— y **vendor-control** para los entregables de cada contrato con su acta de recibo y lo facturado.

**1. Inventario y plan, en una sola llamada**

No listes la carpeta tú: ni `find`, ni `ls -R`, ni una lista en `/tmp`. El inventario y el plan salen del mismo script, en el paso 2, y **ese es el primer comando que corres después de `corrida-inicio`**. `inventory` trae cuántas carpetas de proyecto hay, cuántos archivos de cada formato y cuáles no se pueden leer y por qué.

Reporta de entrada, con esas cifras: cuántos documentos hay, cuántos proyectos se distinguen, qué formatos, y qué archivos no vas a poder leer y por qué. Nada se salta en silencio.

**2. Pide el plan de lectura; no lo redactes**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" plan-lectura --state <estado> --docs <carpeta de documentos> --config <config>
```

Devuelve qué leer y en qué orden: lo nuevo y lo cambiado por hash contra `meta.documents_seen`, agrupado por proyecto en lotes de `execution.batch_projects`, cortado en `execution.max_documents_per_run` en frontera de proyecto, y `mode` dice cuántos lotes pueden ir a la vez (`execution.workers`). **Se ejecuta el plan tal cual.** Lo que no está en `batches` no se lee; lo que está en `deferred` se dice y queda para la corrida siguiente. Un plan con `to_read: 0` es la corrida más barata y más frecuente: no se abre ningún documento, se recalcula y se informa.

Di cuántos documentos vas a leer de cuántos que hay, con las cifras del plan. En un barrido de mantenimiento suelen ser cinco de doscientos, y el gerente debe verlo.

**3. Agrupa por proyecto**

Un proyecto es una carpeta bajo `proyectos/`. Si la estructura no está, agrupa por lo que digan los documentos y **propón** la estructura; no la impongas.

Un proyecto mencionado solo dentro de las minutas de otro también cuenta: se levanta, aunque no tenga carpeta.

**4. Extrae por lotes**

Aplica el skill **project-record**. Procesa en lotes por proyecto, no todo de una vez: la cuota importa y un lote fallido no debe perder el trabajo de los demás.

**Los lotes van como dice `mode`, y cada ficha se escribe y se sella apenas termina su proyecto.** Con `workers: 1` —el valor por defecto y el de cualquier plan con ventana de cuota— los lotes van uno tras otro en esta misma conversación, y no se lanza ningún subagente en paralelo ni en segundo plano. Con `workers: N`, hasta N lotes a la vez, cada uno en un subagente con contexto propio, y nunca más: el arnés cuenta los subagentes de cada corrida y marca en rojo la que exceda lo configurado. En una corrida real, cinco subagentes con ~70 documentos cada uno agotaron la cuota con 12 fichas de 51 escritas, la corrida quedó abierta sin registrar y el rastro solo vio el turno principal; esa es la razón de que la decisión no sea tuya.

Al cerrar cada proyecto:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" sellar --state <estado> --docs <carpeta de documentos> --proyecto <código>
```

Deja en `meta.documents_seen` de la ficha los documentos del proyecto con sus hashes, calculados por el script. **Se sella una ficha que acabas de escribir, nunca las demás ni en bloque al inicio**: sellar es declarar que el proyecto se leyó en esta corrida, y el script rechaza la ficha que no se reescribió después de `corrida-inicio`. **Nunca escribas un hash a mano ni dejes el campo en `null`**: una ficha sin hashes hace que el plan siguiente relea el proyecto entero. Si la cuota se acaba a mitad, lo sellado queda sellado, se registra la corrida con lo que alcanzó (paso 6) y se dice cuántos proyectos faltan.

Orden dentro de cada proyecto: primero `00-gobierno`, luego `10-plan`, después `20-seguimiento` y `30-reuniones` de más reciente a más antiguo. Lo reciente manda sobre lo viejo.

De las minutas y transcripciones, aplica **commitment-tracking** y **raid-taxonomy**: recoge los compromisos y los riesgos que se dijeron y nadie registró.

**5. Clasifica lo que está en `entrada/`**

Todo archivo suelto se asigna a su proyecto y **se mueve**. Lo movido va en la `--nota` de la corrida (paso 6). Si no se puede identificar el proyecto sin ambigüedad, se deja donde está, se pregunta y se levanta alerta. No es una secretaría: si puede resolverlo, lo resuelve.

**6. Escribe y deja rastro**

Guarda cada ficha en `<estado>/records/<codigo>.json`. Escribe en `<estado>/corridas/salida-portfolio-scan.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

Después corre:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" snapshot --state <estado>
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what portfolio-scan \
    --salida <estado>/corridas/salida-portfolio-scan.md \
    --docs <carpeta de documentos> \
    --nota "qué se movió, qué se omitió, qué hay que mirar"
```

La instantánea es lo que permite el diff de la corrida siguiente. **`corrida` es lo que permite compartirla**: deja en `<estado>/corridas/` qué se corrió, sobre cuántos proyectos, cuántos hallazgos y de qué señal, y contra la corrida anterior cuántos más o menos — en JSON para la máquina y en markdown para quien no abre un JSON.

Los dos son comandos y no indicaciones, a propósito. Antes esto decía «registra en `registro.log` qué leyó, qué movió y qué omitió», y en una corrida sobre cincuenta proyectos el archivo quedó vacío: una instrucción en prosa se salta sin que nada falle.

## Salida

```markdown
## Barrido — [fecha]

**Documentos:** [N] en la carpeta · [N] leídos · [N] sin cambio desde la corrida anterior · [N] ilegibles
**Proyectos:** [N] con ficha · [N] nuevos · [N] sin carpeta propia

### Nuevos
| Proyecto | Documentos | Campos encontrados | Campos sin dato |

### Actualizados
| Proyecto | Qué cambió | Fuente |

### No pude leer
| Archivo | Por qué |

### Movidos desde entrada/
| Archivo | A qué proyecto | Por qué |

### Pendientes de clasificar
| Archivo | Por qué no pude decidir |
```

## Después

Ofrece el informe consolidado si hay más de un proyecto, o el estado de uno solo si el barrido fue de uno. Si aparecieron contradicciones o compromisos vencidos, dilo aquí y no lo dejes para el informe.
