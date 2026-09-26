---
name: regulatory-sweep
description: El primer barrido de obligaciones normativas que toca la definición de un producto, citadas y sin opinar sobre cumplimiento. Se carga cuando una definición de producto roza datos personales, pagos, consumidor financiero o retención de información.
---

# El primer barrido normativo

**Lo que este skill hace: nombrar y citar.** Lo que no hace, y hay que decirlo antes de
cualquier otra cosa: **no dice si el producto cumple.** Eso es un juicio jurídico, la
responsabilidad es de la organización que despliega esto, y un agente que lo emita está
generando una confianza que no puede sostener.

La utilidad es de tiempo, no de criterio: un gerente de producto que llega a la revisión
jurídica con la lista de lo que su definición toca, citada, tiene una conversación de una
hora en vez de tres reuniones.

## Cómo se barre

1. **Parte la definición en lo que hace con la información y con el dinero.** Qué dato
   recoge, de quién, dónde lo guarda, a quién se lo muestra, cuánto lo conserva, qué cobra,
   a quién, y con qué medio de pago.
2. **Para cada uno, nombra la obligación aplicable, con la norma y el artículo.** Si no
   sabes cuál es, **dilo**: *«esto toca tratamiento de datos personales y no tengo la norma
   del país a la vista»* es una salida correcta. Inventar una cita de norma es la peor cosa
   que este agente puede hacer.
3. **Marca el país.** Es la parte que más se pierde en una definición escrita para «la
   región»: la obligación no es la misma, y una definición que asume que sí es una
   definición que va a cambiar tarde.
4. **Separa obligación de restricción de diseño.** *«Hay que conservar la trazabilidad de
   la transacción»* es una obligación; *«hay que guardarla siete años en almacenamiento
   inmutable»* ya es una decisión de arquitectura, y no sale de la norma sola.

## Lo que se mira siempre

Sin pretender exhaustividad — es un barrido, no un dictamen:

- **Datos personales.** Qué se recoge, con qué finalidad declarada, qué autorización hace
  falta, qué pasa con los datos sensibles, y qué obligaciones tiene quien encarga el
  tratamiento a un tercero.
- **Transferencia a otro país.** Si el dato sale del país, es su propio tema, y es el que
  más aparece cuando el producto corre en infraestructura de nube.
- **Medios de pago y sistemas de pago.** Quién puede mover dinero, con qué autorización, y
  qué reportes debe.
- **Protección al consumidor**, y cuando el producto es financiero, las obligaciones
  propias de quien atiende consumidor financiero: información previa, reclamos, cobros.
- **Retención y trazabilidad.** Cuánto tiempo se conserva qué, y quién puede pedirlo.
- **Accesibilidad**, cuando el producto atiende público.
- **Firma y prueba del consentimiento**, si el producto hace que alguien acepte algo.

## Cómo se escribe cada hallazgo

```markdown
| Qué toca la definición | País | Obligación | Norma citada | Estado |
| Recoge cédula y celular del comprador | CO | Autorización previa y finalidad declarada | [norma, artículo] | sin resolver |
| Guarda el dato en nube de otro país | CO | Transferencia internacional | [norma, artículo] | no tengo la norma a la vista |
```

**Cuatro estados, y solo cuatro**: `sin resolver`, `resuelto con cita` —hay un documento de
la organización que dice cómo se atiende, y se cita—, `no aplica con razón escrita`, y **`no
tengo la norma a la vista`**. Ese cuarto estado existe a propósito: es lo que impide que un
vacío de conocimiento del agente se vea como un vacío de la definición, o peor, como un
cumplimiento.

## Dónde termina esto

**En la revisión jurídica, siempre.** La salida de este barrido es el insumo de esa
revisión, no su sustituto, y el borrador lo dice en su propia primera línea.

Lo que queda sin resolver no se queda en un documento suelto: **entra al registro como
restricción del requerimiento** —aplica **requirement-record**— o como riesgo con doliente
—aplica **raid-taxonomy**—. Un hallazgo normativo que vive solo en un anexo es un hallazgo
que aparece cuando el producto ya está construido.
