---
description: Revisa o redacta el acta de constitución de un proyecto, señalando qué falta y qué consecuencia tiene que falte
argument-hint: "<código del proyecto> [revisar|redactar]"
---

# /project-charter — Acta de constitución

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el acta.
> Abre declarando si hay acta previa y de cuándo. Cierra con el pie de rigor.

## Invocación

```
/project-charter PRY-014 revisar
/project-charter PRY-020 redactar
```

## Modo revisar

Aplica **governance-artifacts** contra el acta que exista y reporta **qué falta y qué consecuencia tiene**. Un vacío sin consecuencia es una queja; con consecuencia es un hallazgo.

El campo que falta en nueve de cada diez actas es **la autoridad del gerente**: hasta qué monto y qué cambio de alcance puede decidir sin subir a comité. Su ausencia es la razón por la que todo termina en el comité, y así se reporta.

Los otros que hay que buscar explícitamente: objetivo de negocio en vez de descripción de la solución, exclusiones declaradas, patrocinador con nombre de persona, supuestos y restricciones, criterio de éxito medible y quién lo mide.

## Modo redactar

Solo con lo que sustenten los documentos y lo que el gerente confirme en la conversación. **Lo que no esté, se deja marcado como pendiente de definir, no se completa con lo razonable.** Un acta con campos inventados es peor que un acta incompleta: parece cerrada.

## Salida

```markdown
## Acta — [proyecto]
**Estado:** [existe, del (fecha) | no existe]

### Qué falta
| Campo | Estado | Consecuencia |

### Contenido
**Objetivo de negocio:** [medible, no la solución]
**Alcance:**
**Exclusiones:** [lo que el proyecto declara que NO hace]
**Patrocinador:** [persona] · **Gerente:** [persona]
**Autoridad del gerente:** hasta [monto] y [qué cambios] sin comité
**Comité al que reporta:** · **Cadencia:**
**Supuestos:** · **Restricciones:**
**Criterio de éxito:** [medible] · **Lo mide:** [quién]
**Hitos principales:**

[Cada campo con su fuente si viene de un documento, o marcado como pendiente.]
```

## Después

Si el acta quedó sin autoridad declarada, ofrece llevar esa definición al comité: es una decisión, no un trámite. Si de la revisión salieron supuestos, ofrece pasarlos al registro RAID.
