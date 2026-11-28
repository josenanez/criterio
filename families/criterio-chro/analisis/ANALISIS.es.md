# Análisis estadístico de las pruebas · familia CHRO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/chro/` · ronda más reciente: 5 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 5, parcial, sobre 1 de las 6 entidades del material: 22 de 22 señales sembradas encontradas (margen del 95 %: 85,1–100 %) y 0 de más; 305 de 305 datos extraídos bien (100 %, margen del 95 %: 98,7–100 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–5, 155 de 156 señales encontradas, 6 de más y 2257 de 2316 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Norma y Cándido —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 5; la más reciente, la 5, es parcial |
| Material | Retail · Ecuador |
| Entidades de control |  |
| Corridas de una entidad | 11 |
| Señales sembradas | 156 |
| Datos calificados | 2316 |

## Resultados acumulados · rondas 1–5

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 155 de 156 | 99,4 % | 96,4–99,9 % |
| Señales · precisión | 155 de 161 | 96,3 % | 92,1–98,3 % |
| Extracción · datos correctos | 2257 de 2316 | 97,5 % | 96,7–98,1 % |
| Control · sin ninguna señal | 4 de 5 | 80 % | 37,5–96,4 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 96,7 % | 93,5 % | 0 % | 0 de 1 | 16,5 M | 5 |
| 2 | 2 | 100 % | 100 % | 100 % | 1 de 1 | 16,7 M | 2 |
| 3 | 4 | 100 % | 91,7 % | 95,3 % | 2 de 2 | 20,5 M | 2 |
| 4 | 2 | 100 % | 100 % | 100 % | 1 de 1 | 11,4 M | 0 |
| 5 | 1 | 100 % | 100 % | 100 % | 0 de 0 | 9 M | 0 |

## La ronda más reciente · ronda 5

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 22 de 22 | 100 % | 85,1–100 % |
| Señales · precisión | 22 de 22 | 100 % | 85,1–100 % |
| Extracción · datos correctos | 305 de 305 | 100 % | 98,7–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 5

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Retail · Ecuador | Cándido, Norma | 22 de 22 | 0 | 305 de 305 | 9 M |

## Lo que falló, uno por uno · rondas 1–5

66 fallas en 11 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 7 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Banca · Colombia | Señal no encontrada | ["profile_review_overdue", "revision:PC-01"] | CHRO-3 | Material de prueba |
| 1 | Banca · Colombia | Dato calificado como mal | perfiles · profiles | CHRO-1 | Clave de calificación |
| 1 | Banca · Colombia | Dato calificado como mal | seleccion · candidates | CHRO-2 | Clave de calificación |
| 1 | Control · Colombia | Señal de más | ["claim_without_support", "soporte:CAN-406:K1"] | CHRO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Señal de más | ["protected_data_received", "protegido:CAN-406:fotografia"] | CHRO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | perfiles · profiles | — | — |
| 1 | Control · Colombia | Dato calificado como mal | seleccion · candidates | CHRO-5 | Instrucciones del agente |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].title | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].occupation.standard | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].occupation.code | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].education.label | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].education.source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].experience_alternative | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].tasks[T1].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].tasks[T1].text | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R1].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R1].text | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R1].tasks | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R1].element | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R1].source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R1].type | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R2].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R2].text | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R2].tasks | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R2].element | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R2].essential | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R2].source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R2].type | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R3].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R3].text | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R3].tasks | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R3].element | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R3].source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].requirements[R3].type | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-01].next_review | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].title | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].occupation.standard | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].occupation.code | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].education.label | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].education.source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].experience_alternative | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].tasks[T1].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].tasks[T1].text | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R1].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R1].text | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R1].tasks | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R1].element | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R1].source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R1].type | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R2].id | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R2].text | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R2].tasks | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R2].element | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R2].essential | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R2].source | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].requirements[R2].type | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].not_applicable | — | — |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles[SA-02].next_review | — | — |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-01:2_a_1_d"] | CHRO-8 | Material de prueba |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-01:2_c_4_a"] | CHRO-8 | Material de prueba |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-02:2_a_1_d"] | CHRO-8 | Material de prueba |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-02:2_c_4_a"] | CHRO-8 | Material de prueba |

## Defectos

![Defectos](defectos-es.svg)

9 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 9 verificados y 0 por verificar. 6 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 3 |
| Clave de calificación | 2 |
| Material de prueba | 2 |
| Arnés de pruebas | 2 |

| Agente | Defectos |
|---|---|
| Cándido | 5 |
| Norma | 4 |

## Consumo y próximo paso

Las 5 rondas usaron 74 millones de tokens: 74 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 6,7 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/chro/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/chro).
