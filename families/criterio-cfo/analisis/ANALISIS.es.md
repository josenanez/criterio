# Análisis estadístico de las pruebas · familia CFO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cfo/` · ronda más reciente: 4 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 4, parcial, sobre 9 de las 12 entidades del material: 80 de 80 señales sembradas encontradas (margen del 95 %: 95,4–100 %) y 0 de más; 74 de 74 datos extraídos bien (100 %, margen del 95 %: 95–100 %); y 3 de 3 entidades de control sin ninguna señal.

Sumando las rondas 1–4, 178 de 178 señales encontradas, 0 de más y 171 de 172 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

Cada entidad corre todos los comandos de los dos agentes, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte: el agente nunca la ve. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 4; la más reciente, la 4, es parcial |
| Material | Banca · Colombia, Banca · Perú, Cooperativas · Ecuador, Minería · Ecuador, Minería · Perú, Retail · Colombia |
| Entidades de control | Control · Colombia, Control · Ecuador, Control · Perú |
| Corridas de una entidad | 21 |
| Señales sembradas | 178 |
| Datos calificados | 172 |

## Resultados acumulados · rondas 1–4

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 178 de 178 | 100 % | 97,8–100 % |
| Señales · precisión | 178 de 178 | 100 % | 97,8–100 % |
| Extracción · datos correctos | 171 de 172 | 99,4 % | 96,7–99,9 % |
| Control · sin ninguna señal | 7 de 7 | 100 % | 64,5–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 100 % | 100 % | 100 % | 1 de 1 | 17,3 M | 3 |
| 2 | 6 | 100 % | 100 % | 98 % | 2 de 2 | 53 M | 1 |
| 3 | 4 | 100 % | 100 % | 100 % | 1 de 1 | 17,2 M | 3 |
| 4 | 9 | 100 % | 100 % | 100 % | 3 de 3 | 38 M | 3 |

## La ronda más reciente · ronda 4

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 80 de 80 | 100 % | 95,4–100 % |
| Señales · precisión | 80 de 80 | 100 % | 95,4–100 % |
| Extracción · datos correctos | 74 de 74 | 100 % | 95–100 % |
| Control · sin ninguna señal | 3 de 3 | 100 % | 43,8–100 % |

## Por industria y país · ronda 4

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | aurea, Clara, Tomás | 16 de 16 | 0 | 8 de 8 | 4,7 M |
| Banca · Perú | aurea, Clara, Tomás | 12 de 12 | 0 | 8 de 8 | 4,2 M |
| Cooperativas · Ecuador | aurea, Clara, Tomás | 14 de 14 | 0 | 8 de 8 | 4,2 M |
| Minería · Ecuador | aurea, Clara, Tomás | 14 de 14 | 0 | 9 de 9 | 4,6 M |
| Minería · Perú | aurea, Clara, Tomás | 12 de 12 | 0 | 9 de 9 | 4,1 M |
| Retail · Colombia | aurea, Clara, Tomás | 12 de 12 | 0 | 8 de 8 | 4,3 M |
| Control · Colombia | aurea, Clara, Tomás | 0 de 0 | 0 | 8 de 8 | 3,9 M |
| Control · Ecuador | aurea, Clara, Tomás | 0 de 0 | 0 | 8 de 8 | 3,8 M |
| Control · Perú | aurea, Clara, Tomás | 0 de 0 | 0 | 8 de 8 | 4,3 M |

## Lo que falló, uno por uno · rondas 1–4

1 falla en 21 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 1 de esas fallas vino de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 2 | Minería · Ecuador | Dato calificado como mal | presupuesto · committee_commitments | CFO-4 | Arnés de pruebas |

## Defectos

![Defectos](defectos-es.svg)

10 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 10 verificados y 0 por verificar. 5 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 4 |
| Material de prueba | 3 |
| Arnés de pruebas | 2 |
| Código | 1 |

| Agente | Defectos |
|---|---|
| Tomás | 5 |
| Clara | 3 |
| aurea | 2 |
| Ninguno | 1 |

## Consumo y próximo paso

Las 4 rondas usaron 136,2 millones de tokens: 125,5 millones en las corridas calificadas y 10,7 en las que se repitieron después de corregir un defecto. En promedio, 6 millones por entidad.

El material es sintético. El próximo paso es el despliegue en una organización, con su propia documentación.

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cfo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cfo).
