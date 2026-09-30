---
name: document-intake
description: "La disciplina de la carpeta: qué documento hay que volver a leer y cuál no, cómo se detecta un renombrado o un borrado, y qué hacer con una cita que dejó de resolver. Úsalo al barrer un portafolio, antes de releer cualquier documento, al configurar la cadencia, o cuando una corrida esté saliendo caro. Document intake, hashing, re-read discipline."
---
<!-- COPIA · la fuente es plugins/criterio-portfolio/skills/document-intake/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Entrada de documentos

## Por qué esto es lo primero

El único paso caro de todo el sistema es leer un documento. Todo lo demás —restar
días, sumar comprometido, comparar declaración contra evidencia— es aritmética y
cuesta lo mismo con cuarenta proyectos que con cuatro.

Entonces la pregunta que decide el costo de una corrida no es *"¿qué leo?"* sino
**"¿qué NO tengo que volver a leer?"**. Y la respuesta no se estima: se calcula.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" index --state <estado> --docs <carpeta>
```

## Las dos etapas del hash

**Etapa uno, el hash de los bytes.** Si es el mismo de la corrida anterior, el
documento no se toca y sus campos se conservan tal cual.

**Etapa dos, el hash del texto normalizado.** Si los bytes cambiaron, se extrae el
texto y se compara. **Un documento que alguien abrió y guardó sin escribir nada cambia el
primero y no el segundo**, porque en un `.docx` o un `.xlsx` el guardado mueve metadatos del
ZIP, el orden de las partes y la cadena de cálculo. En un banco eso pasa todos los días, y
cada falso positivo ahí cuesta una relectura completa.

Con una precisión que conviene no exagerar: si una fórmula volátil recalculó a un valor
distinto, **el texto sí cambió** y hay que releer — el número es otro. La etapa dos no
ahorra relecturas de contenido nuevo; ahorra las de contenido idéntico.

El índice los separa: `changed` es lo que hay que releer, `resaved_only` es lo que
cambió de bytes y no de contenido. Solo el primero entra en `to_read`.

## Qué se puede leer, y con qué

La conversión vive en `scripts/texto.py` y produce Markdown en un caché. **El Markdown es
un caché, no la fuente:** la cita de una ficha apunta siempre al documento original, porque
es lo que una persona abre para verificar.

| Formato | Cómo se lee | Dependencia |
|---|---|---|
| `.md` `.txt` `.csv` `.tsv` `.json` `.yaml` | Directo | ninguna |
| `.docx` `.xlsx` `.pptx` | Son ZIP con XML adentro: `zipfile` y `xml.etree` | **ninguna** |
| `.eml` | El parser de correo de la librería estándar | ninguna |
| `.html` `.xml` | Se quitan las etiquetas | ninguna |
| `.pdf` con capa de texto | `pdftotext`, de poppler | el binario |
| `.pdf` escaneado | **No se lee.** Necesita OCR | — |
| `.msg` `.doc` `.xls` `.mpp` | **No se leen.** Se dice cómo guardarlos para que sí | — |

Que los formatos de Office se lean sin instalar nada no es un detalle: es lo que permite
que la mitad de la carpeta de una PMO real entre sin un proyecto de integración.

**Lo que no se puede leer se declara, con la razón y con la salida.** Un escaneo sin capa de
texto no produce un campo vacío: produce un hallazgo que dice que ese documento nadie lo
leyó, y por lo tanto que el dato que contenía no está. Fingir que un documento ilegible no
existe es la peor forma del salto silencioso.

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
