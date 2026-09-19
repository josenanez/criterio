---
description: Cierra un proyecto contra el criterio de éxito pactado y deja lecciones aprendidas que se puedan sustentar
argument-hint: "<código del proyecto>"
---

# /project-closure — Cierre

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el acta de cierre.
> Abre declarando de qué ficha y qué documentos sale. Cierra con el pie de rigor.

## Invocación

```
/project-closure PRY-014
```

## El principio

Un proyecto no se cierra porque se acabó el presupuesto ni porque el equipo se fue. Se cierra cuando alguien declara que terminó, **contra el criterio de éxito que se pactó al inicio**.

Si el acta no declaró criterio de éxito, eso es lo primero que dice el cierre, y el proyecto se cierra por decisión, no por cumplimiento.

## Flujo

**1. Recupera lo comprometido.** Aplica **governance-artifacts**: alcance y criterio de éxito del acta, con su fuente.

**2. Contrasta entregado contra comprometido.** Qué se entregó, qué quedó fuera, y con acuerdo de quién. Un alcance recortado sin decisión registrada es un hallazgo del cierre.

**3. Cierra los números.** Aplica **baseline-variance**: desviación final contra la línea base **original** —no la vigente— y contra la vigente, con el conteo de replanificaciones. Presupuesto aprobado contra ejecutado.

**4. Cierra el RAID.** Qué riesgos se materializaron y cuáles no, qué incidencias quedaron sin resolver, y qué queda abierto y a cargo de quién después del cierre. Lo que queda abierto necesita doliente con nombre o no está cerrado.

**5. Lecciones que se puedan sustentar.** Una lección genérica —"mejorar la comunicación"— es un lugar común. Una lección útil nombra el hecho, la fecha y el efecto: *"el ambiente de pruebas se pidió en abril y estuvo en julio; los tres meses están en el atraso del hito 4"*.

Si un aprendizaje no se puede anclar a un hecho documentado, no entra.

## Salida

```markdown
## Cierre — [proyecto] — [fecha]

### Contra lo comprometido
**Criterio de éxito:** [del acta, con fuente | no fue declarado]
**Se cumplió:** [sí | parcialmente | no se puede determinar]

| Entregable comprometido | Estado | Evidencia |

### Fuera de alcance final
| Qué quedó fuera | Decidido por | Cuándo |

### Números finales
| | Original | Vigente | Final | Desviación vs original |
| Fecha | | | | |
| Presupuesto | | | | |
Replanificaciones: [N]

### RAID al cierre
**Materializados:** · **No materializados:** · **Abiertos, con doliente:**

### Lecciones
| Qué pasó | Cuándo | Efecto | Qué haríamos distinto |

### Sin dato
[Lo que no se pudo determinar de la documentación disponible.]
```

## Después

Ofrece mover la carpeta del proyecto a `archivo/` y dejar la ficha congelada con su última instantánea. Un proyecto cerrado sale del barrido diario pero no se borra: su historial es lo que alimenta las lecciones del siguiente.
