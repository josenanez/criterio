---
name: product-health
description: Las señales de un producto antes de que exista un proyecto, qué umbral gobierna cada una, en qué orden se leen y cuál no es hallazgo. Se carga al revisar el registro de requerimientos, la definición o el estado de un producto.
---

# El estado de un producto, antes de que haya plan

Un proyecto se juzga contra su plan. **Un producto en definición no tiene plan**, así que
se juzga contra otra cosa: la evidencia de que alguien pidió esto, el criterio con el que
se va a saber si quedó bien, y si lo que se decidió construir lo está construyendo
alguien.

Las once señales las calcula `producto.py`. **Este skill dice qué significan.** Ninguna
de las dos cosas se hace en el otro sitio: el código no opina y este documento no cuenta.

## Las once señales

| Señal | Qué es | Por qué importa |
|---|---|---|
| `requirement_without_owner` | No hay doliente, o el doliente es un área | Igual que un riesgo sin doliente: es decoración. *«Producto lo revisa»* no compromete a nadie |
| `requirement_without_acceptance` | Decidido y sin criterios de aceptación | Sin criterio, la discusión de si quedó bien se da al final, cuando ya está construido |
| `requirement_accepted_without_evidence` | Decidido y sin una sola cita de quien lo pidió | **La señal central.** Una definición que se sostiene sola |
| `requirement_undecided` | Propuesto, y nadie lo decide | Pasado el umbral no es un pendiente: es una decisión que no se está tomando |
| `requirement_untraced` | Aceptado y ningún proyecto lo ejecuta | Se decidió construirlo y no lo está construyendo nadie |
| `trace_not_confirmed` | El registro dice que lo ejecuta un proyecto, y la ficha de ese proyecto dice otra cosa | Alba no le cree a su propio registro. Lo confirma contra la ficha, que es de otro dueño |
| `decision_without_source` | Se decidió y no hay documento que lo diga | En seis meses nadie recuerda quién decidió, y la decisión se vuelve a discutir |
| `assumption_unverified` | Un supuesto que nadie verificó | Un supuesto que nadie verifica no es un supuesto: es un riesgo sin registrar |
| `evidence_stale` | La evidencia más nueva que lo sostiene ya envejeció | Una entrevista de hace dos años no sostiene una definición de hoy |
| `claim_vs_metric` | El negocio declara un número y la métrica mide otro | Con las dos fuentes y las dos fechas. Sin eso el hallazgo no sirve |
| `product_overlap` | Otro producto afirma tu misma métrica, comparte tu proyecto o dice servir a tu mismo segmento | La métrica compartida es el hallazgo más caro: **dos casos de negocio contando lo mismo producen una suma que no existe** |

## Los cuatro umbrales

| Umbral | Por defecto | Qué gobierna |
|---|---|---|
| `undecided_days` | 60 | `requirement_undecided` |
| `assumption_unverified_days` | 30 | `assumption_unverified` |
| `evidence_stale_months` | 12 | `evidence_stale` |
| `claim_gap_pct` | 20 | `claim_vs_metric` |

Los cuatro se cambian en la configuración de la organización, y el valor por defecto no
es una recomendación: es lo que se usa mientras nadie decida otra cosa. **Si una
organización mueve un umbral, la corrida siguiente lo usa y lo dice.**

## En qué orden se leen

No es el orden en que salen del cálculo. Es el orden en que sirven:

1. **`claim_vs_metric`.** El negocio y los datos no coinciden. Todo lo demás se define
   encima de un número que está en discusión.
1. **`product_overlap`, cuando es de métrica.** Si otro producto afirma tu misma cifra, la
   discusión del número deja de ser tuya y pasa a ser del portafolio de productos.
2. **`requirement_accepted_without_evidence`.** Lo que se va a construir y nadie pidió.
3. **`trace_not_confirmed`** y **`requirement_untraced`.** La brecha entre lo decidido y
   lo que se está construyendo.
4. **`assumption_unverified`** y **`evidence_stale`.** Lo que sostiene la definición y ya
   no la sostiene.
5. **`requirement_undecided`.** El registro que crece y nadie cierra.
6. **`requirement_without_owner`**, **`requirement_without_acceptance`**,
   **`decision_without_source`.** Vacíos de forma. Son los más fáciles de cerrar, y por
   eso van al final: cerrarlos primero da la sensación de avance sin haber movido nada.

## Lo que no es hallazgo

- **Un requerimiento propuesto sin evidencia todavía.** Nadie dijo que se hace. Exigirle
  evidencia a lo que aún no se decidió convierte el registro en un trámite.
- **Un requerimiento entregado sin traza.** Es historia, no hallazgo.
- **Una diferencia pequeña entre lo declarado y lo medido.** Por debajo del umbral es
  imprecisión; por encima es contradicción. **Reportar la imprecisión mata el informe.**
- **Un supuesto verificado, por incómodo que sea.** Ya hizo su trabajo.
- **Que el registro y la ficha del proyecto coincidan.** El caso normal no se reporta. Un
  agente que celebra las coincidencias es ruido.
- **Que dos productos sirvan al mismo segmento**, por sí solo. Una organización puede tener
  dos productos para el mismo cliente a propósito. Se reporta como pregunta, no como defecto.
- **Que no haya ningún otro producto publicado.** Entonces `product_overlap` no es una señal
  en cero: es una pregunta que no se puede responder, y se dice así.

## La comparación, un paso antes

En un proyecto se contrasta el **estado declarado** por el gerente contra la evidencia
documental. En un producto se contrasta la **definición** contra la evidencia de demanda.
Es la misma comparación, un paso aguas arriba, y tiene la misma restricción: **el agente
no declara.** Quién decide qué se construye es el gerente de producto, y si el agente
decidiera, la comparación compararía al sistema consigo mismo.

## De qué está hecha la peor cobertura de los tres

Conviene decirlo aquí y no en la conversación. La verdad de un portafolio vive en
documentos; la de un proyecto, en conversación que deja minuta; **la de un producto vive
en clientes, mercado y juicio, y de eso casi nada queda escrito antes de la decisión.**

Eso no hace inútil a este agente: hace que su aporte sea la cadena de evidencia y los
huecos señalados, no una conclusión. Cuando la cobertura no alcanza, la respuesta correcta
es *«no está dicho en ninguna parte»*, y es una respuesta válida y esperada.
