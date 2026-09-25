# Las hojas de los agentes

Documento de trabajo. Aquí queda escrito **qué hace cada agente, qué no hace, y qué sigue
siendo de las personas.** Es la base para discutir el diseño antes de codificar, y la
referencia contra la cual se ajustan la arquitectura y el esquema.

No es material de mercado. La versión pública de la capacidad vive en
[`capabilities/pmo.es.md`](../../capabilities/pmo.es.md). Estas hojas están en español
porque su uso es discutirlas; la pareja en inglés entra cuando el diseño se estabilice, no
antes, para no duplicar la rotación.

Una hoja por agente:

- [Agente PMO](pmo.md) — gobierno de portafolio
- [Agente Project Manager](project-manager.md) — un proyecto
- [Agente Product Manager](product-manager.md) — antes de que exista el proyecto

---

## La necesidad común: proyectos

Los tres agentes existen alrededor de un mismo objeto, y la elección carga todo el peso del
diseño: **un proyecto tiene plan, y sin plan no hay contra qué comparar.**

Toda la propuesta se sostiene en contrastar lo que alguien declara contra lo que sustentan
los documentos. Esa comparación necesita una referencia aprobada. En un proceso o en un área
no existe el *contra qué*; en un proyecto sí, y se llama línea base.

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

### Las cinco invariantes

1. **Los agentes no se hablan entre sí.** Se hablan por la ficha.
2. **El servidor no escribe.**
3. **La fuente puede cambiar; la ficha no.** Un adaptador nuevo llena los mismos campos.
4. **Declarado y evidenciado nunca se fusionan**, venga de archivo o de base de datos.
5. **El modelo extrae, el código calcula.**

---

## La frontera

El criterio que decide si algo es del agente o de la persona no es repetitivo contra
creativo. Es este:

> **El agente puede producir cualquier cosa que sea una afirmación sobre lo que está
> escrito. No puede producir nada que comprometa a una persona o a la institución.**

Sobre ese criterio, cada función de cada rol cae en una de tres clases:

| Clase | Qué es |
|---|---|
| **A** | Repetitivo. Se hace hoy, consume tiempo, y el agente lo hace igual o mejor |
| **B** | No repetitivo. Hoy **no se hace**, porque costaría días por proyecto. El agente lo vuelve barato |
| **C** | No lo hace el agente, por riesgo |

**El alcance declarado de Criterio es A y B.** La clase C no se construye, no se ofrece y no
se insinúa.

La distinción entre A y B importa para entender el valor: la A ahorra tiempo en trabajo que
ya se hace; la B produce cosas que hoy no existen en ninguna PMO —el forense de catorce
meses, la contradicción entre cuarenta carpetas, el supuesto que nadie verificó—. La A la
agradece el equipo; la B la compra un director.

### Los cuatro riesgos de la clase C

| Código | Riesgo |
|---|---|
| **AUT** | Autoridad. Compromete a la organización, y alguien tiene que responder |
| **INF** | Información. Se decide con lo que no está en ningún documento |
| **PER** | Personas. Es un juicio sobre alguien |
| **SEÑ** | Señal. Si lo hace el agente, se destruye la comparación que sostiene el sistema |

Los cuatro no son iguales en el tiempo. **INF puede encoger** si la organización deja más
rastro escrito. **AUT no se mueve nunca.** Y **SEÑ es una restricción del diseño**, no una
prudencia: tiene una sola fila en las tres hojas, y está en el Project Manager.

---

## Lo que sigue siendo de las personas

Los tres roles siguen existiendo completos. Esto extiende capacidad; no sustituye función.
Y el argumento no es de cortesía, es estructural:

> **El insumo de cada agente lo produce el trabajo no delegable de su persona.**

El agente PM necesita que alguien dirija la reunión, porque de ahí sale la minuta que lo
alimenta. El agente PMO necesita que alguien persiga lo que el informe pide, porque si nadie
actúa el informe siguiente dice lo mismo. El agente de producto necesita que alguien hable
con el cliente, porque no hay síntesis sin entrevista.

Quitar a la persona no deja al agente solo: lo deja sin comida. Cada hoja documenta qué se
rompe primero si se intenta.

---

## Estado

| Agente | Estado |
|---|---|
| PMO | Disponible. La clase A está cerrada; falta la mitad de la B |
| Project Manager | En construcción. El método existe, la superficie de comandos no |
| Product Manager | Sin construir. Requiere primero el registro de requerimiento |

---

## Decisiones abiertas

Las cuatro son de esquema, y las tres primeras se deciden **antes** de que el agente PM
empiece a llenar fichas. Una ficha llena con el esquema equivocado es la migración que no
queremos hacer.

| Campo | Qué habilita | Si no está |
|---|---|---|
| `source_kind` — declaración o evidencia | Conectar una base de datos o un PPM sin contaminar la comparación | El día que entre el PPM del banco, sus *verdes* entran como evidencia y la tesis muere |
| `producto` | La vista transversal del PMO sobre los proyectos que tienen producto | *"¿Cómo va el producto?"* no se responde desde cuarenta fichas de proyecto |
| `requerimiento` como registro | *"Qué requerimientos faltan"* como filtro instantáneo, y el traspaso Product → Project | Es siempre una corrida de modelo sobre documentos, cada vez |
| `autoridad` del gerente | Que el control de cambios sepa si algo excede la facultad sin releer el acta | Se vuelve a derivar de los documentos en cada corrida |

Sobre la base de datos hay una trampa que conviene dejar escrita: **lo que trae un PPM son
más declaraciones, no evidencia.** El campo *"estado: verde"* de la herramienta corporativa
es la afirmación del gerente con otra interfaz. La evidencia sigue viviendo en actas y
minutas.
