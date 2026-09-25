---
name: document-intake
description: "La disciplina de la carpeta: qué documento hay que volver a leer y cuál no, cómo se detecta un renombrado o un borrado, y qué hacer con una cita que dejó de resolver. Úsalo al barrer un portafolio, antes de releer cualquier documento, al configurar la cadencia, o cuando una corrida esté saliendo caro. Document intake, hashing, re-read discipline."
---

# Entrada de documentos

## Por qué esto es lo primero

El único paso caro de todo el sistema es leer un documento. Todo lo demás —restar
días, sumar comprometido, comparar declaración contra evidencia— es aritmética y
cuesta lo mismo con cuarenta proyectos que con cuatro.

Entonces la pregunta que decide el costo de una corrida no es *"¿qué leo?"* sino
**"¿qué NO tengo que volver a leer?"**. Y la respuesta no se estima: se calcula.

```
python3 scripts/pmo.py index --state <estado> --docs <carpeta>
```

## Las dos etapas del hash

**Etapa uno, el hash de los bytes.** Si es el mismo de la corrida anterior, el
documento no se toca y sus campos se conservan tal cual.

**Etapa dos, el hash del texto normalizado.** Si los bytes cambiaron, se extrae el
texto y se compara. **Un Word reguardado, un Excel que recalcula al abrirlo y un PDF
reimpreso cambian el primero y no el segundo.** Eso no es un caso raro: en un banco
pasa todos los días, y cada falso positivo ahí cuesta una relectura completa.

El índice los separa: `changed` es lo que hay que releer, `resaved_only` es lo que
cambió de bytes y no de contenido. Solo el primero entra en `to_read`.

Cuando el formato no se puede leer sin instalar nada, no hay etapa dos. **Eso se
declara**, no se finge: el documento entra a releer por si acaso, y la salida dice por
qué.

## Los cuatro estados de un documento

| Estado | Qué significa | Qué se hace |
|---|---|---|
| **nuevo** | No está en `documents_seen` de ninguna ficha | Se lee |
| **cambiado** | Cambió el texto | Se relee, y se recalcula su proyecto |
| **reguardado** | Cambiaron los bytes y no el texto | Se actualiza el hash y nada más |
| **renombrado** | Desapareció una ruta y apareció otra con el mismo contenido | Se corrigen las citas |
| **borrado** | Desapareció y ningún archivo nuevo tiene su contenido | Se reporta |

El renombrado se detecta por contenido, no por parecido de nombre. Dos archivos con el
mismo hash son el mismo documento aunque se llamen distinto.

## La cita que dejó de resolver

Esto no es una optimización, es integridad. **Toda cita de toda ficha tiene que apuntar
a un archivo que existe.** Cuando alguien renombra o mueve un documento, cada campo que
lo citaba queda apuntando al vacío, y el informe sigue mostrando el dato como si
estuviera sustentado.

El índice devuelve `source_missing` con el proyecto y el campo exacto. **Una cita que no
resuelve es un hallazgo y se reporta como tal**, con la misma seriedad que una
contradicción: en un método cuyo valor entero es la trazabilidad, una cita rota es una
afirmación sin respaldo.

## Un documento toca varios proyectos

Una minuta de comité o un Excel de portafolio afecta a doce fichas. El índice devuelve,
por cada documento, los proyectos que lo citan, y la lista
`projects_to_recompute` con los que hay que recalcular. **No se recalcula el portafolio
completo porque cambió un archivo.**

## Formatos

Se reporta de entrada cuántos documentos hay, qué formatos, y **cuáles no se van a poder
leer y por qué.** Nada se salta en silencio. Un `.msg` que nadie puede abrir es un
hallazgo de la carpeta, no un detalle técnico.

## La cadencia sale de aquí

`daily_sweep` no es un reloj que dispara una relectura: es este índice. Listar, comparar,
extraer solo lo que cambió de verdad, recalcular solo los proyectos tocados. **El costo
escala con la rotación de documentos, no con el tamaño del portafolio**, y por eso setenta
proyectos con semanas quietas cuestan casi nada.

## Lo que este skill no hace

No decide qué dice un documento. Decide si hay que abrirlo.

No borra ni mueve nada. Reporta lo que encontró; reorganizar una carpeta es del dueño de
la carpeta.
