# Las hojas de los agentes

Documento de trabajo. Aquí queda escrito **qué hace cada agente, qué no hace, qué entra y qué
sale de cada función, y cómo interactúa con la persona responsable.** Es la base para discutir
el diseño antes de codificar, y la referencia contra la cual se ajustan la arquitectura y el
esquema.

No es material de mercado. La promesa pública vive en el [README del market](../../README.es.md)
y en el [README del plugin](../../plugins/criterio-pmo/README.md). Estas hojas están en español porque
su uso es discutirlas; la pareja en inglés entra cuando el diseño se estabilice, no antes, para
no duplicar la rotación.

Una hoja por agente:

- [**Vera** · agente PMO](pmo.md) — gobierno de portafolio
- [**Samuel** · agente Project Manager](project-manager.md) — un proyecto
- [**Alba** · agente Product Manager](product-manager.md) — antes de que exista el proyecto

La forma de todo lo que estos agentes entregan —informes, proyección, piezas gráficas— está en
[`docs/design.md`](../design.md): es el diseño del portal, y se mantiene igual aquí.

---

## La necesidad común: proyectos

Los tres agentes existen alrededor de un mismo objeto, y la elección carga todo el peso del
diseño: **un proyecto tiene plan, y sin plan no hay contra qué comparar.**

Toda la propuesta se sostiene en contrastar lo que alguien declara contra lo que sustentan los
documentos. Esa comparación necesita una referencia aprobada. En un proceso o en un área no
existe el *contra qué*; en un proyecto sí, y se llama línea base.

---

## Los tres agentes y el único contrato

Nada se habla con nada directamente. **La ficha de proyecto es el único contrato.**

```
   archivos ─┐
             ├──► extracción ──► FICHA ──► cálculo ──► proyección ──► servidor
   base de   ┘                    ▲ ▲ ▲
   datos                          │ │ └── PMO      escribe hallazgos, lee todas
                                  │ └──── PM       escribe la ficha, lee la suya
                                  └────── Product  la crea, con el acta
```

El Product Manager trabaja antes de que exista plan: no escribe en la ficha, **la crea**. Su
entrega cierra con el acta de constitución, que es el certificado de nacimiento de la ficha.

Y el orden temporal es lo que hace de los tres un sistema:

```
Product Manager  ──acta──►  Project Manager  ──ficha──►  PMO
   define                      ejecuta                    vigila el conjunto
```

### Las siete invariantes

1. **Los agentes no se hablan entre sí.** Se hablan por la ficha.
2. **Rostrum, el servidor, no escribe.**
3. **La fuente puede cambiar; la ficha no.** Un adaptador nuevo llena los mismos campos.
4. **Declarado y evidenciado nunca se fusionan**, venga de archivo o de base de datos.
5. **El modelo extrae, el código calcula.**
6. **Ningún agente escribe la declaración.** El estado declarado lo escribe una persona.
7. **Una ficha, un escritor.** Dos agentes que leen los mismos documentos escriben dos
   fichas, y no se fusionan nunca. La diferencia entre las dos es el hallazgo.

La sexta es la más fácil de romper por conveniencia y la que se lleva el sistema entero si se
rompe: si el agente declara, la comparación entre declaración y evidencia compara al sistema
consigo mismo, y todo esto se vuelve un generador de informes bonitos. No es una recomendación
de la documentación: es una restricción del camino de escritura, y falla si se intenta.

La séptima es la cuarta un nivel más arriba, y aparece en cuanto hay más de un agente sobre
el mismo proyecto. La forma cómoda de resolverlo —una ficha y un dueño— obliga a elegir mal
en las dos direcciones: si manda el gerente, la PMO no puede leer por su cuenta cuando duda;
si manda la PMO, entra en el camino crítico de setenta proyectos. Dos fichas quitan el
problema en vez de arbitrarlo, y **lo que era un conflicto de escritura se vuelve la señal.**
Ver [Samuel · las dos fichas](project-manager.md#las-dos-fichas).

---

## Las tres clases

Cada función de cada rol cae en una de tres. **El alcance construido de Criterio es A y B.**

### A — Lo que el agente hace, y hoy consume tiempo de alguien

Trabajo que la organización ya ejecuta todas las semanas: leer, consolidar, cruzar, reportar.
El agente no lo acelera, lo sustituye. Se reconoce por una prueba simple: **si nadie lo hace,
alguien lo nota.**

### B — Lo que el agente hace y hoy no se hace

Trabajo que la organización no ejecuta, no por descuido sino porque costaría días por
proyecto: el forense de catorce meses, la contradicción entre cuarenta carpetas, el supuesto
que nadie verificó. Se reconoce por la prueba inversa: **si nadie lo hace, nadie lo nota.**

La distinción importa para entender el valor. La A ahorra tiempo en trabajo que ya se hace y la
agradece el equipo. La B produce lo que hoy no existe en ninguna PMO, y la compra un director.

### C — Lo que el agente no hace

Un conjunto de acciones que el agente **no ejecuta**. Nada más.

Esta lista no evalúa riesgos ni exposición de nadie: describe el límite del agente. Quien
instala Criterio acepta los [términos](../../TERMS.es.md) —la verificación es suya, §2; se
entrega sin garantía ni responsabilidad, §5— y el [descargo](../../DISCLAIMER.es.md). La
responsabilidad de uso y de ejecución es de la organización que lo despliega, y si en su
contexto la clase C es más grande que esta lista, delimitarla y documentarla le corresponde a
ella, con el descargo adicional que su gobierno interno exija.

Cada fila de C lleva dos datos, y ninguno es un riesgo:

- **Requiere** — por qué está fuera del alcance del agente: *autoridad* (compromete a la
  organización), *información fuera de los documentos*, o *juicio sobre personas*.
- **Qué le entrega al agente** — porque casi toda función de C produce el insumo de una función
  de A o de B. Es la parte que hace de esto un ciclo y no dos mundos separados.

---

## Cómo se llaman

**La capacidad se llama PMO, CFO o CLO. El agente lleva nombre de persona.** Son dos cosas
distintas y conviene no mezclarlas: la capacidad es la función de la organización, y el
agente es quien la extiende.

Que lleven nombre de persona no es un adorno: **son capacidades extendidas de personas
reales**, y el producto entero se sostiene en que la persona sigue ahí. Un nombre propio
dice eso sin tener que explicarlo.

| Pieza | Nombre | De dónde viene | La frase |
|---|---|---|---|
| Agente PMO | **Vera** | latín *verus*, lo verdadero | *Vera dice lo que los documentos dicen, no lo que se reporta* |
| Agente Project Manager | **Samuel** | «el que escuchó» | *Samuel oyó lo que se dijo en la reunión, y lo recuerda el viernes* |
| Agente Product Manager | **Alba** | el amanecer, antes de que haya luz | *Alba trabaja antes de que el proyecto exista* |
| El servidor | **Rostrum** | una tribuna | *Sostiene lo que ya está escrito, donde otros puedan leerlo* |

**La regla, que es lo que hace que esto escale y no la lista:** el nombre de un agente es
un nombre de persona **cuyo significado apunta al oficio que su familia extiende**, y tiene
que poder terminar la frase «X hace esto, y no opina». Si no la termina, está mal elegido.

Samuel es el que mejor lo muestra: la función central de ese agente es **el compromiso
dicho y no cumplido**, y el nombre significa literalmente «el que escuchó».

Las familias que vengan eligen con la misma regla y con las referencias de su propio
gremio — **CFO** con Mateo, patrono de contadores y banqueros, o Luca por Pacioli; **CLO**
con Ivo, patrono de los abogados. Quien pertenece al gremio reconoce la referencia sin que
nadie se la explique, y quien no la reconoce solo ve un nombre, que también está bien.

**El servidor es el único que no lleva nombre de persona, y es a propósito.** Los agentes
lo llevan porque toman decisiones sobre lo que leen; el servidor no toma ninguna. Es
infraestructura, y conserva nombre de objeto: una tribuna no mide, no corrige y no opina —
sostiene lo que ya está escrito a la altura de quien lo va a leer. Si algún día calculara
algo, el nombre dejaría de ser cierto, y eso es exactamente lo que se quiere que se note.

**Los nombres no se traducen** —son propios— y **no son identificadores**: el plugin se
sigue llamando `criterio-pmo`, los comandos y los skills no cambian. El nombre le da
carácter a lo que la persona ve, no a lo que el código importa.

---

## Un dueño por cosa

No se duplica documentación. Una tabla copiada en tres documentos se desactualiza en el
primero que nadie mire, y eso ya pasó: la lista de señales de la página pública llegó a estar
cinco señales atrás y a prometer una que el código no emitía.

| Cosa | Dueño | Por qué ahí |
|---|---|---|
| Los valores de los umbrales | `DEFAULT_THRESHOLDS` en `scripts/pmo.py` | Es lo que el código lee. Cualquier otra copia es una opinión |
| Qué significa cada señal y cuándo merece alarma | el skill `portfolio-health` | Es lo que el modelo carga en tiempo de ejecución, y tiene que sostenerse solo |
| El inventario de comandos y skills | el README del plugin | El plugin se distribuye por el market y su README viaja con él |
| La promesa pública y las cifras de terceros | el README del market | Es la primera página que alguien abre, y la única que decide una instalación |
| El diseño de cada agente | estas hojas | Clases, flujo, lo que es de las personas, lo que falta |
| El resultado de las corridas | `tests/<plugin>/EVIDENCIA.md` | La evidencia vive con el material que la produjo |

Lo verifican dos cosas, y ninguna es un humano acordándose: `scripts/validate_plugins.py`
exige que el README del plugin liste cada comando, y `tests/coherencia.py` exige que cada
señal que el código calcula esté documentada en su skill y que cada comando aparezca en la
página pública. **Si algo se agrega y no se documenta en su dueño, falla.**

---

## Lo que sigue siendo de las personas

Los tres roles siguen existiendo completos. Esto extiende capacidad; no sustituye función. Y el
argumento no es de cortesía, es estructural:

> **El insumo de cada agente lo produce el trabajo no delegable de su persona.**

El agente PM necesita que alguien dirija la reunión, porque de ahí sale la minuta que lo
alimenta. El agente PMO necesita que alguien persiga lo que el informe pide, porque si nadie
actúa el informe siguiente dice lo mismo. El agente de producto necesita que alguien hable con
el cliente, porque no hay síntesis sin entrevista.

Quitar a la persona no deja al agente solo: lo deja sin comida. Cada hoja documenta qué se
rompe primero si se intenta, y en qué orden.

---

## Estado

**Los tres están construidos y se pueden instalar hoy**, y los tres tienen la misma deuda,
que conviene no esconder: **verificados sobre corpus sintético, no probados sobre la
documentación real de una organización.**

| Agente | Se instala | Qué falta |
|---|---|---|
| Vera · PMO | `criterio-pmo` · 17 comandos, 10 skills | La mitad de la clase B |
| Samuel · Project Manager | `criterio-pm` · 6 comandos, 8 skills | El primer borrador del plan y de la WBS |
| Alba · Product Manager | `criterio-product` · 7 comandos, 12 skills | El análisis de canibalización |
| Rostrum · el servidor | Dentro de `criterio-pmo` | — |

Y una deuda que es de los tres a la vez: **la extracción nunca se ha corrido.** Los tres
corpus siembran el estado desde sus respuestas de referencia, así que la cadena documento →
modelo → ficha no se ha ejercitado.

La corrida que sostiene estos estados, con lo que prueba y lo que no, está en las tres
páginas de evidencia bajo [`tests/`](../../tests/) y, dibujada, en
[`docs/pruebas.html`](../pruebas.html). La quinta decisión de la tabla siguiente salió de
ahí y no de una conversación.

---

## Decisiones de esquema, cerradas

Aquí vivían cinco, todas de esquema y todas por decidir **antes** de que un agente empezara a
llenar fichas: una ficha llena con el esquema equivocado es la migración que no queremos hacer.

**Las cinco se construyeron** —`source_kind`, `producto`, `autoridad`, el monto por entregable
y, la última, **`requerimiento` como registro**—, y por eso salen de la tabla en vez de quedarse
como historia. El registro de requerimiento es el contrato de datos de Alba, vive en
`criterio-product` con su propia aritmética, y es el que vuelve *«qué requerimientos faltan»* un
filtro en vez de una corrida de modelo sobre documentos cada vez. El esquema va en 0.2.

Lo que queda abierto de verdad está en cada hoja: **cómo bajan los estándares de la PMO a N
instalaciones** y **qué pasa cuando un gerente publica su ficha y no quiere** —las dos en la
hoja del Project Manager—, y **el análisis de canibalización**, que necesita las métricas de más
de un producto a la vista y hoy cada instalación mira el suyo.

Sobre la base de datos hay una trampa que conviene dejar escrita: **lo que trae un PPM son más
declaraciones, no evidencia.** El campo *"estado: verde"* de la herramienta corporativa es la
afirmación del gerente con otra interfaz. La evidencia sigue viviendo en actas y minutas.
