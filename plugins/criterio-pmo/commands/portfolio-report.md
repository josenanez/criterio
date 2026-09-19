---
description: Informe consolidado de portafolio a partir de las fichas — qué cambió, qué se contradice, qué está en silencio y qué no tiene sustento
argument-hint: "[ppt|pdf|html] o vacío para el formato configurado"
---

# /portfolio-report — Informe de portafolio

Consolida las fichas y responde lo que el gerente de PMO no puede saber leyendo proyecto por proyecto.

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el informe.
> Abre declarando qué fichas cargó y su fecha. Cierra con el pie: versión, fichas aplicadas con su fecha, campos inciertos y enlace a los términos.

## Invocación

```
/portfolio-report              formato configurado
/portfolio-report ppt          material para presentar
/portfolio-report html         para consultar y filtrar
```

## Flujo

**1. Carga y verifica frescura**

Lee todas las fichas de `estado/fichas/`. Si alguna tiene más de una semana sin barrido, dilo en el banner de apertura y ofrece correr `/portfolio-scan` antes. No produzcas un informe de portafolio sobre fichas viejas sin advertirlo.

**2. Diff contra la instantánea anterior**

```
python3 scripts/pmo.py diff --state <estado>
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
python3 scripts/pmo.py compute --state <estado> --config <pmo.config.json>
```

Devuelve los números y la lista de señales que cruzaron umbral. Aplica **portfolio-health** para leer qué significa cada una, y **baseline-variance** para las desviaciones. El script ya calculó; aquí se decide qué merece aparecer y en qué orden.

**No recalcules nada a mano.** Si un número del informe no sale del script, está inventado.

**5. Arma la confirmación del mes**

Si toca, aplica la confirmación periódica: **cinco campos**, los más viejos entre los que importan. Van al final, como preguntas cerradas.

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
