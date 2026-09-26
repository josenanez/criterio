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

- [**Plomada** · agente PMO](pmo.md) — gobierno de portafolio
- [**Escuadra** · agente Project Manager](project-manager.md) — un proyecto
- [**Compás** · agente Product Manager](product-manager.md) — antes de que exista el proyecto

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
2. **Atril, el servidor, no escribe.**
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
Ver [Escuadra · las dos fichas](project-manager.md#las-dos-fichas).

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

**La capacidad se llama PMO, CFO o CLO. El agente lleva el nombre de un instrumento.** Son
dos cosas distintas y conviene no mezclarlas: la capacidad es la función de la organización,
y el agente es quien la extiende.

| Pieza | Nombre | Por qué ese |
|---|---|---|
| Agente PMO | **Plomada** | Cuelga quieta y dice si algo está derecho. No opina: muestra |
| Agente Project Manager | **Escuadra** | Verifica el ángulo de una pieza. Un proyecto, no el conjunto |
| Agente Product Manager | **Compás** | Mide antes de trazar. Trabaja antes de que exista el proyecto |
| El servidor | **Atril** | Donde se pone lo que se va a leer delante de otros. Sostiene, no traza |

Instrumentos de trazo y verificación, porque es exactamente lo que hacen y porque así los
tres son hermanos evidentes. Un nombre que no estire a los hermanos obliga a rebautizar a
todos en cuanto aparezca el segundo.

**Atril es el único que no es un instrumento de medida, y es a propósito.** Los tres
agentes tienen nombre porque toman decisiones sobre lo que leen; el servidor no toma
ninguna. Un atril no mide, no corrige y no opina: sostiene lo que ya está escrito a la
altura de quien lo va a leer. Si algún día el servidor calculara algo, el nombre dejaría
de ser cierto — y eso es exactamente lo que se quiere que se note.

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

| Agente | Estado |
|---|---|
| PMO | Disponible. La clase A está cerrada; falta la mitad de la B |
| Project Manager | En construcción. El método existe, la superficie de comandos no |
| Product Manager | Sin construir. Requiere primero el registro de requerimiento |

La corrida que sostiene estos estados, con lo que prueba y lo que no, está en
[`tests/criterio-pmo/EVIDENCIA.md`](../../tests/criterio-pmo/EVIDENCIA.md). La quinta decisión
de la tabla siguiente salió de ahí y no de una conversación.

---

## Decisiones abiertas

Las cuatro son de esquema, y las tres primeras se deciden **antes** de que el agente PM empiece
a llenar fichas. Una ficha llena con el esquema equivocado es la migración que no queremos
hacer.

| Campo | Qué habilita | Si no está |
|---|---|---|
| `requerimiento` como registro | *"Qué requerimientos faltan"* como filtro instantáneo, y el traspaso Product → Project | Es siempre una corrida de modelo sobre documentos, cada vez |

Las otras cuatro que estaban aquí —`source_kind`, `producto`, `autoridad` y el monto por
entregable— **ya se construyeron**, y por eso salen de la tabla en vez de quedarse como
historia. El esquema va en 0.2. La que queda es de la hoja del Product Manager, no de la PMO.

Sobre la base de datos hay una trampa que conviene dejar escrita: **lo que trae un PPM son más
declaraciones, no evidencia.** El campo *"estado: verde"* de la herramienta corporativa es la
afirmación del gerente con otra interfaz. La evidencia sigue viviendo en actas y minutas.
