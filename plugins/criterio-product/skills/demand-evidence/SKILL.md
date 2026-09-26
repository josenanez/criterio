---
name: demand-evidence
description: Qué cuenta como evidencia de que alguien pidió algo, qué no cuenta aunque lo parezca, cómo envejece y cómo se contrasta una definición contra ella. Se carga al sustentar o cuestionar la definición de un producto.
---

# La evidencia de demanda

Esta es la tesis de Criterio, un paso aguas arriba. En un proyecto se contrasta el **estado
declarado** contra la evidencia documental. En un producto se contrasta la **definición**
contra la evidencia de demanda. **La misma comparación, antes de que haya plan.**

Y tiene la misma falla característica: nadie miente. La definición se escribió hace ocho
meses con la evidencia que había, la evidencia envejeció, y el documento sigue igual.

## Qué cuenta

Ordenado por lo que aguanta una pregunta incómoda en un comité:

| Evidencia | Qué tan fuerte | Por qué |
|---|---|---|
| **Alguien ya pagó por esto** | La más fuerte | Una orden, un contrato, un piloto pagado. Es demanda demostrada, no declarada |
| **Uso medido de algo parecido que ya existe** | Fuerte | Una serie, con su fuente y su fecha. Aplica **product-metrics** |
| **El cliente lo pidió, por escrito, con su nombre** | Fuerte | Ticket, correo, acta de reunión con el cliente |
| **El cliente lo dijo en una entrevista** | Media | Con la cita y el conteo. Aplica **discovery-synthesis** |
| **Una obligación normativa lo exige** | Fuerte, y distinta | No es demanda: es restricción. Aplica **regulatory-sweep** |
| **Un competidor lo tiene** | Débil sola | Dice que alguien apostó, no que tu cliente lo quiera |
| **Una encuesta de intención** | Débil | *«Lo usaría»* y *«lo pagué»* se parecen en el papel y en nada más |

## Qué no cuenta, aunque lo parezca

- **El juicio del equipo.** *«Esto claramente hace falta»* puede ser cierto y no es
  evidencia. Se registra como supuesto, y aplica **assumption-tracking**.
- **La cifra que alguien dijo de memoria.** *«Perdemos como el 30%»* es una cita de quien
  lo dijo. Se busca la serie, o se declara que no existe.
- **Que lo pida un directivo.** Es una decisión, y las decisiones se registran como
  decisiones, con quién y con su documento. **Es una razón perfectamente válida para
  construir algo, y no es evidencia de demanda.** Confundir las dos es lo que hace que seis
  meses después nadie sepa por qué se hizo.
- **Un informe de mercado sobre otra geografía.** Se cita como lo que es, y se dice de qué
  mercado habla.
- **Un tema de descubrimiento sin ninguna cita.** Ver **discovery-synthesis**.

## Cómo envejece

La evidencia de demanda tiene fecha, y **la más nueva es la que decide si el conjunto está
vigente**: una entrevista de hace tres años no envejece a la de ayer. Pasado
`evidence_stale_months` el cálculo emite `evidence_stale` con los meses y la cita de lo más
reciente.

Lo que envejece más rápido, y conviene tenerlo escrito:

- **La intención declarada.** Lo que alguien dijo que usaría el año pasado.
- **La comparación con un competidor.** El competidor cambió.
- **El uso medido de un canal que cambió de forma.** La serie sigue, y ya no mide lo mismo.

Lo que no envejece igual: **que alguien haya pagado.** Sigue siendo cierto que pagó.

## Cómo se contrasta la definición

Es el trabajo concreto, y se hace afirmación por afirmación:

1. **Parte la definición en afirmaciones.** Cada frase que dice algo sobre el mundo —quién
   tiene el problema, qué tan grande es, qué haría el cliente— es una afirmación aparte.
2. **Para cada una, busca qué la sostiene.** Con la cita y la fecha.
3. **Clasifícala en tres, y solo tres:**
   - **Sostenida** — hay evidencia, y se dice cuál.
   - **Sostenida por un supuesto** — no hay evidencia; hay una creencia declarada. Va a
     **assumption-tracking**.
   - **No está dicha en ninguna parte** — nadie la afirmó ni la negó. **Es la categoría más
     útil y la que ninguna revisión encuentra**, porque leyendo un documento bien escrito
     todo parece sustentado.
4. **Lo que la evidencia contradice va aparte**, con las dos fuentes y las dos fechas. No
   se fusiona con lo que no está dicho: es otra cosa y se resuelve de otra manera.

## Lo que este skill no decide

**Si la demanda alcanza.** Que ocho comercios de ochenta lo pidan es un dato; si eso
justifica construirlo depende del costo, de la estrategia y de la política de la
organización, y eso es del gerente de producto. Aquí se arma la cadena y se señalan los
huecos.

Y **si va a gustar.** Eso no está en ningún documento, es la parte del oficio que necesita
estar frente al cliente, y ningún agente la va a tener.
