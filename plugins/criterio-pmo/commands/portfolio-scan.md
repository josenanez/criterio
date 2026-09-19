---
description: Lee la carpeta de documentación de proyectos y produce o actualiza una ficha por proyecto, con cita a la fuente de cada dato
argument-hint: "[ruta de la carpeta] o vacío para usar la configurada"
---

# /portfolio-scan — Barrido de la documentación

Puerta de entrada del plugin. Convierte una carpeta desordenada de documentos en fichas consultables.

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes fichas ni informe.
> Abre declarando qué encontró y cierra con el pie: versión, fichas tocadas, campos en `not_found` y enlace a los términos.

## Invocación

```
/portfolio-scan                          usa la ruta de pmo.config.yaml
/portfolio-scan ~/PMO/proyectos          barre esa carpeta
/portfolio-scan PRY-014                  vuelve a barrer un solo proyecto
```

## Flujo

**1. Inventario antes de leer**

Lista la carpeta completa. Para cada archivo registra ruta, tamaño, fecha de modificación y fecha del nombre si la trae. **No abras nada todavía.**

Reporta de entrada: cuántos documentos hay, cuántos proyectos se distinguen, qué formatos, y qué archivos no vas a poder leer y por qué. Nada se salta en silencio.

**2. Descarta lo que no cambió**

Compara el hash de cada documento contra `meta.documents_seen` de la ficha existente. Los que coinciden no se vuelven a leer y sus campos se conservan.

Di cuántos documentos vas a leer de cuántos que hay. En un barrido de mantenimiento suelen ser cinco de doscientos, y el gerente debe verlo.

**3. Agrupa por proyecto**

Un proyecto es una carpeta bajo `proyectos/`. Si la estructura no está, agrupa por lo que digan los documentos y **propón** la estructura; no la impongas.

Un proyecto mencionado solo dentro de las minutas de otro también cuenta: se levanta, aunque no tenga carpeta.

**4. Extrae por lotes**

Aplica el skill **project-record**. Procesa en lotes por proyecto, no todo de una vez: la cuota importa y un lote fallido no debe perder el trabajo de los demás.

Orden dentro de cada proyecto: primero `00-gobierno`, luego `10-plan`, después `20-seguimiento` y `30-reuniones` de más reciente a más antiguo. Lo reciente manda sobre lo viejo.

De las minutas y transcripciones, aplica **commitment-tracking** y **raid-taxonomy**: recoge los compromisos y los riesgos que se dijeron y nadie registró.

**5. Clasifica lo que está en `entrada/`**

Todo archivo suelto se asigna a su proyecto, **se mueve y se registra** en `estado/registro.log`. Si no se puede identificar el proyecto sin ambigüedad, se deja donde está, se pregunta y se levanta alerta. No es una secretaría: si puede resolverlo, lo resuelve.

**6. Escribe y deja rastro**

Guarda cada ficha en `<estado>/records/<codigo>.json`. Después corre:

```
python3 scripts/pmo.py snapshot --state <estado>
```

La instantánea es lo que permite el diff de la corrida siguiente. Registra en `<estado>/registro.log` qué leyó, qué movió y qué omitió.

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
