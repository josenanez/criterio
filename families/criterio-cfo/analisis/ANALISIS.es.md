# Análisis estadístico de las pruebas · familia CFO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cfo/` · ronda completa más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 2, sobre las 6 entidades del material: 45 de 45 señales sembradas encontradas (margen del 95 %: 92,1–100 %) y 0 de más; 48 de 49 datos extraídos bien (98 %, margen del 95 %: 89,3–99,7 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 58 de 58 señales encontradas, 0 de más y 64 de 65 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

Cada entidad corre todos los comandos de los dos agentes, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte: el agente nunca la ve. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la completa más reciente es la 2 |
| Material | Banca · Colombia, Cooperativas · Ecuador, Minería · Ecuador, Retail · Colombia |
| Entidades de control | Control · Colombia, Control · Ecuador |
| Corridas de una entidad | 8 |
| Señales sembradas | 58 |
| Datos calificados | 65 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 58 de 58 | 100 % | 93,7–100 % |
| Señales · precisión | 58 de 58 | 100 % | 93,7–100 % |
| Extracción · datos correctos | 64 de 65 | 98,5 % | 91,7–99,8 % |
| Control · sin ninguna señal | 3 de 3 | 100 % | 43,8–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 100 % | 100 % | 100 % | 1 de 1 | 17,3 M | 3 |
| 2 | 6 | 100 % | 100 % | 98 % | 2 de 2 | 53 M | 1 |

## La ronda completa más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 45 de 45 | 100 % | 92,1–100 % |
| Señales · precisión | 45 de 45 | 100 % | 92,1–100 % |
| Extracción · datos correctos | 48 de 49 | 98 % | 89,3–99,7 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Clara, Tomás | 13 de 13 | 0 | 8 de 8 | 8,4 M |
| Cooperativas · Ecuador | Clara, Tomás | 11 de 11 | 0 | 8 de 8 | 9,2 M |
| Minería · Ecuador | Clara, Tomás | 11 de 11 | 0 | 8 de 9 | 9,7 M |
| Retail · Colombia | Clara, Tomás | 10 de 10 | 0 | 8 de 8 | 8,8 M |
| Control · Colombia | Clara, Tomás | 0 de 0 | 0 | 8 de 8 | 8,4 M |
| Control · Ecuador | Clara, Tomás | 0 de 0 | 0 | 8 de 8 | 8,5 M |

## Lo que falló, uno por uno · rondas 1–2

1 falla en 8 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 1 de esas fallas vino de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 2 | Minería · Ecuador | Dato calificado como mal | presupuesto · committee_commitments | CFO-4 | Arnés de pruebas |

## Defectos

![Defectos](defectos-es.svg)

4 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 4 verificados y 0 por verificar. 2 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Arnés de pruebas | 2 |
| Instrucciones del agente | 1 |
| Código | 1 |

| Agente | Defectos |
|---|---|
| Tomás | 3 |
| Ninguno | 1 |
| Clara | 1 |

## Consumo y próximo paso

Las 2 rondas usaron 71,1 millones de tokens: 70,3 millones en las corridas calificadas y 0,8 en las que se repitieron después de corregir un defecto. En promedio, 8,8 millones por entidad.

El material es sintético. El próximo paso es el despliegue en una organización, con su propia documentación.

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cfo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cfo).
