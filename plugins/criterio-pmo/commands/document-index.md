---
description: Dice qué documentos cambiaron de verdad, qué hay que releer y qué citas dejaron de resolver
argument-hint: "[código del proyecto]"
---

# /document-index — Qué cambió en la carpeta

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla.
> Este comando no lee documentos: los cuenta y los compara. Es el paso que decide el costo de todo lo demás.

## Invocación

```
/document-index                          toda la carpeta
/document-index PRY-014                  solo lo que toca a un proyecto
```

## Flujo

**1. Corre el índice.** Aplica **document-intake**.

```
python3 scripts/pmo.py index --state <estado> --docs <documentos>
```

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
