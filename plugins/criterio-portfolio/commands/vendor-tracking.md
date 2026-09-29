---
description: Contrasta los entregables contractuales de un proveedor contra el avance real y contra lo facturado
argument-hint: "<código del proyecto> [nombre del proveedor]"
---

# /vendor-tracking — Proveedores

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el informe.
> Abre declarando de qué documentos sale. Cierra con el pie de rigor.

## Antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/vendor-tracking PRY-014
/vendor-tracking PRY-014 Sistemas del Norte
```

## El principio

Tres cosas que casi nunca se miran juntas: **lo que el contrato comprometió**, **lo que se entregó** y **lo que se facturó**. Cada una vive en un área distinta y nadie las cruza.

El hallazgo típico no es el fraude. Es un entregable aceptado sin evidencia de aceptación, o un hito facturado contra un avance que ninguna acta sustenta.

## Flujo

**1. Carga los entregables contractuales** desde la ficha y desde los documentos de `00-gobierno`. Si el contrato no está en la carpeta, dilo: sin el contrato esto es una lista de supuestos.

**2. Busca la evidencia de cada entregable.** Acta de recibo, correo de aceptación, mención explícita en una minuta. Aplica **project-record**: sin evidencia, el estado es `unknown`, no `delivered`.

**3. Cruza contra lo facturado**, si hay documentos que lo declaren. Dónde no cuadra, se nombra, con las dos fuentes.

El cruce lo calcula el script, no el ojo: por cada proveedor de la ficha devuelve `late` (entregables con fecha pasada, sin evidencia y sin declarar entrega), `accepted_without_evidence` (declarados entregados o aceptados y sin un documento que lo pruebe), `accepted`, `deliverables` e `invoiced`. Y levanta `vendor_invoiced_without_delivery` cuando hay factura y ni un entregable aceptado. Tómalo de ahí y cita el documento de cada línea.

**4. Revisa vencimientos y compromisos.** Aplica **commitment-tracking** sobre las reuniones con el proveedor: lo que prometió en comité es un compromiso como cualquier otro.

**5. Mira el vencimiento del contrato.** Fecha de terminación, renovación automática y preaviso. Un contrato cuyo preaviso vence antes del cierre del proyecto es un hallazgo urgente, no administrativo.

## Salida

```markdown
## Proveedores — [proyecto] al [fecha]

### [Proveedor] — contrato [ref]
**Vigencia:** [inicio] a [fin] · **Preaviso de no renovación:** [plazo] · **Vence el:** [fecha]

| Entregable | Comprometido | Estado | Evidencia | Facturado |

### Dónde no cuadra
| Qué | Dice el contrato | Dice la evidencia | Fuentes |

### Sin evidencia de recibo
| Entregable | Marcado como | Desde |

### Compromisos del proveedor vencidos
| Qué | Prometido en | Para | Días |

### Sin dato
[Contratos que no están en la carpeta, montos no declarados.]
```

## Después

Si el preaviso de un contrato está por vencer, dilo aquí y no en el anexo. Si hay entregables facturados sin evidencia, ofrece llevarlo a comité.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/portafolio.py corrida --state <estado> --what vendor-tracking \
    --salida <estado>/corridas/salida-vendor-tracking.md \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-vendor-tracking.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
