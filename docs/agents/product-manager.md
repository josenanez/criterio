# Agente Product Manager

Extiende al **gerente de producto**: la persona que define qué se va a construir, antes de que
exista un proyecto.

Marco general, clases y códigos de riesgo: [README](README.md).

| | |
|---|---|
| **Instancia** | Una por producto |
| **Alcance** | El producto a lo largo de su vida, no un proyecto |
| **Escribe** | Su propio registro previo. **Crea la ficha** con el acta de constitución |
| **Lee** | Su registro, y las fichas de los proyectos que ejecutan su producto |
| **Estado** | Sin construir |

---

## Por qué este agente no encaja todavía

La espina de la ficha es `plan` + `baseline` + `money`. En investigación y definición **ninguno
de los tres existe**, así que este agente no puede escribir en la ficha: trabaja antes.

Sus artefactos son otros — el problema, la evidencia de demanda, las hipótesis, la definición,
los requerimientos, el criterio de decisión — y necesita su propio registro previo.

**La costura con el agente Project Manager es el acta de constitución.** Es el momento en que
un problema definido se vuelve plan con doliente, autoridad y criterio de éxito. Ya está en el
plugin, en `governance-artifacts` y `/project-charter`: el traspaso no necesita inventar nada.

Y el orden temporal completo, que es lo que hace de los tres un sistema:

```
Product Manager  ──acta──►  Project Manager  ──ficha──►  PMO
   define                      ejecuta                    vigila el conjunto
```

El PMO no vigila proyectos sueltos: vigila **todos los proyectos que tienen producto**, y para
eso necesita la dimensión `producto` en la ficha, que hoy no existe.

---

## A · Lo que haría, y hoy consume tiempo de alguien

Ninguna está construida. Todas necesitan primero el registro de requerimiento.

| Función | Nota |
|---|---|
| Sintetizar entrevistas y retroalimentación en temas | Con la cita de quién lo dijo, nunca como conclusión propia |
| Inventario de requerimientos con estado, doliente y evidencia | Es el registro que el esquema no tiene |
| Trazabilidad requerimiento → decisión → entregable | Lo que permite responder *"qué falta"* como filtro y no como corrida de modelo |
| Detectar requerimientos sin criterio de aceptación o sin doliente | Igual que un riesgo sin doliente: decoración |
| Recopilar análisis competitivo de fuentes públicas | Recopila y cita; no concluye posicionamiento |
| Consolidar las métricas del producto | Si están en un sistema, es lectura |
| Borrador de la especificación a partir de lo decidido | Borrador |
| Producir el acta de constitución del traspaso | La costura con el agente PM |

## B · Lo que haría porque hoy no se hace

| Función | Nota |
|---|---|
| Contrastar la definición contra la evidencia de demanda que existe | *"¿Qué sustenta que esto se necesita?"* — la pregunta que casi nunca se hace |
| Detectar contradicción entre lo que dice el negocio y lo que dicen los datos | Mismo mecanismo que declarado contra evidenciado |
| Identificar los supuestos no verificados de la definición | El supuesto es el que más daño hace: falla y se vuelve incidencia sin pasar por riesgo |
| Primer barrido de obligaciones normativas que toca el producto | Con cita a la norma y **sin opinar sobre cumplimiento** |
| Estructurar el caso de negocio | La estructura y los vacíos; las cifras son del negocio |
| Análisis de canibalización con datos internos | Barato si los datos están; imposible a mano |

La primera fila es la que traslada la tesis entera de Criterio aguas arriba: en un proyecto se
contrasta el estado declarado contra la evidencia documental; en un producto se contrasta la
**definición** contra la evidencia de demanda. Es la misma comparación, un paso antes.

## C · Lo que no hace

| Función | Riesgo | Por qué |
|---|---|---|
| Decidir qué se construye y qué no | **AUT** | Asignación de capital |
| Hablar con el cliente | **INF** | La entrevista es el insumo, y es humana |
| Leer lo que el cliente no dice | **INF** | Es el corazón del descubrimiento |
| Definir precio y modelo de negocio | **AUT** | |
| Juzgar deseabilidad: si esto va a gustar | **INF** | |
| Go / no-go de lanzamiento | **AUT** | |
| Retirar un producto | **AUT** | |
| Asumir el riesgo regulatorio de una definición | **AUT** | Consecuencia legal |
| Priorizar el backlog cuando hay conflicto de intereses | **AUT** + **INF** | |

Este es el agente con **la peor cobertura de información de los tres**, y conviene decirlo en
voz alta. La verdad de un portafolio vive en documentos; la de un proyecto, en conversación
que deja minuta; la de un producto, en clientes, mercado y juicio — de lo cual casi nada queda
escrito antes de la decisión.

---

## Lo que sigue siendo del gerente de producto persona

**Habla con el cliente, lee lo que el cliente no dice, juzga si algo va a gustar, decide qué
se construye, pone el precio, y firma el go / no-go.** Nada de eso se toca.

Lo que cambia es que llega a esa decisión con la cadena de evidencia armada y los huecos
señalados: qué de la definición está sustentado y por qué documento, qué supuestos no se han
verificado, dónde el negocio y los datos dicen cosas distintas, y qué obligaciones normativas
toca lo que va a definir.

Si una organización quitara al gerente de producto y dejara solo al agente, se rompe antes que
en los otros dos casos: **no hay descubrimiento, y sin descubrimiento el agente no tiene nada
que sintetizar.** Un agente de producto sin gerente de producto sintetiza el vacío.

---

## Antes de construir nada

1. **El registro de requerimiento**, que es la dependencia bloqueante.
2. **El campo `producto` en la ficha**, para que el PMO pueda mirar por producto.
3. **Que la ficha tenga dos escritores y el contrato haya aguantado** — es decir, que el agente
   PM esté corriendo sobre documentación real.

El tercero no es una formalidad. Definir este agente antes diluye la única tesis que hoy es
medible, y el proyecto ya pagó una vez el costo de abrir dos líneas a la vez: está escrito en
[`docs/decisions/0005`](../decisions/0005-scope-pmo-only.md).
