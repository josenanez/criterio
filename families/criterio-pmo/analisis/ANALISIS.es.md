# Análisis estadístico de las pruebas · familia PMO

Generado por `scripts/analisis.py` desde `tests/evidencias/` · ronda más reciente: 10 (2026-10-18), versión probada 0.5.0 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La versión más reciente probada, 0.5.0, en la ronda 10: Vera con 100 % de precisión (margen del 95 %: 98,4–100 %) y 97,2 % de cobertura; Samuel con 100 % de compromisos correctos; Alba con 100 % de alertas encontradas; Rostrum con 100 % de comprobaciones.

Sumando las rondas 1–10, Vera acertó en el 99 % de las 2444 alertas que emitió y encontró el 99,6 % de las 2428 que había. Desde la ronda 6, las cuatro métricas se mantienen por encima del 99 %.

## Qué se probó y cómo

Cada ronda sortea hechos nuevos y escribe una clave que ningún agente ve. Los datos de prueba se construyeron para ser más exigentes que la documentación de una PMO promedio, y cada industria lleva un proyecto sano que no debe levantar ninguna alerta.

Precisión: de las alertas emitidas, cuántas eran correctas. Cobertura: de las que había, cuántas encontró. Margen del 95 %: intervalo de confianza de Wilson sobre los casos; para Vera en la última ronda, el que remuestrea proyectos.

|   |   |
|---|---|
| Periodo | 10 rondas, 2026-10-15 → 2026-10-18, versiones 0.3.6 → 0.5.0 |
| Industrias | Banca, Cooperativas, Minería, Retail |
| Proyectos analizados | 520 |
| Documentos procesados | 5137: Markdown 2777, Word 1217, PDF 506, Excel 326, CSV 231, JSON 40, texto 40 |
| Ejecuciones | 1480 |
| Lecturas de la clave | 0 |
| Proyectos de control | 40 |

## Resultados acumulados · rondas 1–10

Los acumulados de Samuel, Alba y Rostrum incluyen las primeras rondas, cuando esas capacidades se estaban construyendo; su valor actual es el de la versión más reciente.

| Agente · métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Vera · precisión | 2419 de 2444 | 99 % | 98,4–99,4 % |
| Vera · cobertura | 2419 de 2428 | 99,6 % | 99,2–99,9 % |
| Vera · proyectos de control sin alertas | 40 de 40 | 100 % | 91,2–100 % |
| Samuel · compromisos correctos | 840 de 876 | 95,9 % | 94,3–97,1 % |
| Alba · cobertura | 1148 de 1197 | 95,9 % | 94,6–96,9 % |
| Alba · precisión | 1148 de 1160 | 99 % | 98,2–99,5 % |
| Rostrum · comprobaciones (9 rondas) | 18 723 de 19 198 | 97,5 % | 97,2–97,8 % |
| Contratos cumplidos | 1463 de 1480 | 98,9 % | 98,1–99,3 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda · versión | Proyectos | Documentos | Vera · precisión | Samuel | Alba · cobertura | Rostrum | Contratos | Defectos |
|---|---|---|---|---|---|---|---|---|
| 1 · 0.3.6 | 52 | 457 | 97,9 % | 75 % | 0 % | No medido | 100 % | 13 |
| 2 · 0.3.8 | 52 | 490 | 97 % | 83,3 % | 88,4 % | 79,8 % | 95,9 % | 13 |
| 3 · 0.3.9 | 52 | 528 | 98,4 % | 76,9 % | 99,3 % | 99,2 % | 98 % | 6 |
| 4 · 0.3.10 | 52 | 506 | 98,7 % | 96,2 % | 92,5 % | 99,8 % | 97,3 % | 5 |
| 5 · 0.3.11 | 52 | 498 | 97,8 % | 98,1 % | 100 % | 100 % | 100 % | 3 |
| 6 · 0.3.12 | 52 | 534 | 100 % | 99,1 % | 100 % | 99,9 % | 98 % | 4 |
| 7 · 0.3.13 | 52 | 534 | 100 % | 100 % | 100 % | 100 % | 100 % | 1 |
| 8 · 0.3.13 | 52 | 527 | 99,6 % | 100 % | 100 % | 99,3 % | 99,3 % | 2 |
| 9 · 0.4.0 | 52 | 532 | 99,6 % | 100 % | 100 % | 100 % | 100 % | 2 |
| 10 · 0.5.0 | 52 | 531 | 100 % | 100 % | 100 % | 100 % | 100 % | 3 |

## La versión más reciente probada · 0.5.0, ronda 10

Vera no emitió ninguna alerta falsa. Vera no detectó 7 alertas, todas en Minería. Alba emitió 1 alerta que no estaba en la clave. Corregidos y por verificar en la próxima ronda: D058, D059, D060.

| Agente · métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Vera · precisión | 242 de 242 | 100 % | 98,4–100 % |
| Vera · cobertura | 242 de 249 | 97,2 % | 90,4–100 % |
| Samuel · compromisos correctos | 108 de 108 | 100 % | 96,5–100 % |
| Alba · cobertura | 131 de 131 | 100 % | 97,1–100 % |
| Alba · precisión | 131 de 132 | 99,2 % | 95,8–99,9 % |
| Rostrum · comprobaciones | 2175 de 2175 | 100 % | 99,8–100 % |
| Contratos cumplidos | 148 de 148 | 100 % | 97,4–100 % |

## Por industria · rondas 1–10

| Industria | Vera · precisión | Vera · cobertura | Samuel | Alba · cobertura | Alba · precisión | Rostrum |
|---|---|---|---|---|---|---|
| Banca | 98,6 % | 100 % | 89 % | 93,4 % | 98,4 % | 97,4 % |
| Cooperativas | 99,5 % | 100 % | 98,2 % | 97,7 % | 99,7 % | 97,6 % |
| Minería | 98,4 % | 98,4 % | 98,2 % | 96,7 % | 98,3 % | 97,8 % |
| Retail | 99,4 % | 100 % | 98,2 % | 95,9 % | 99,6 % | 97,3 % |

## Por tipo de alerta · Vera, rondas 1–10

Vera emitió alertas de 18 tipos; en 15 no tuvo una sola alerta falsa, y las 25 falsas se concentran en 3. «Gerente y PMO no dicen lo mismo» todavía no se sostiene: 18 falsas y ninguna correcta, la última en la ronda 9, ninguna en la ronda 10. Es la que hay que reforzar.

| Tipo de alerta | Correctas | Falsas | No detectadas | Precisión | Cobertura |
|---|---|---|---|---|---|
| Hito dado por cumplido sin evidencia | 819 | 0 | 0 | 100 % | 100 % |
| Compromiso vencido sin evidencia | 281 | 0 | 4 | 100 % | 98,6 % |
| Avance declarado que el plan no sostiene | 266 | 0 | 0 | 100 % | 100 % |
| Verde que la evidencia no sostiene | 228 | 0 | 0 | 100 % | 100 % |
| Entregable de proveedor vencido | 167 | 0 | 0 | 100 % | 100 % |
| Compromiso que nadie fechó | 137 | 0 | 1 | 100 % | 99,3 % |
| Desviación en tiempo | 93 | 0 | 1 | 100 % | 98,9 % |
| Desviación en costo | 89 | 0 | 0 | 100 % | 100 % |
| Compromiso prometido una y otra vez | 79 | 2 | 2 | 97,5 % | 97,5 % |
| Línea base movida más de lo autorizado | 55 | 0 | 1 | 100 % | 98,2 % |
| Hito vencido | 51 | 0 | 0 | 100 % | 100 % |
| Entrega dada por aceptada sin evidencia | 44 | 5 | 0 | 89,8 % | 100 % |
| Cambio aprobado sin línea base nueva | 31 | 0 | 0 | 100 % | 100 % |
| Facturado sin entregable aceptado | 30 | 0 | 0 | 100 % | 100 % |
| Proyecto sin actividad | 22 | 0 | 0 | 100 % | 100 % |
| Facturado por encima de lo aceptado | 22 | 0 | 0 | 100 % | 100 % |
| Presupuesto comprometido sin holgura | 5 | 0 | 0 | 100 % | 100 % |
| Gerente y PMO no dicen lo mismo | 0 | 18 | 0 | 0 % | — |

## Defectos

![Defectos](defectos-es.svg)

60 defectos registrados, cada uno con su origen, su corrección y la ronda que la verificó: 57 verificados y 3 por verificar. 17 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Código | 22 |
| Instrucciones del agente | 20 |
| Material de prueba | 10 |
| Clave de calificación | 4 |
| Arnés de pruebas | 3 |
| Comportamiento del modelo | 1 |

| Agente | Defectos |
|---|---|
| Vera | 27 |
| Samuel | 11 |
| Alba | 9 |
| Rostrum | 9 |
| Los tres | 4 |

## Consumo y lo que esta medición no cubre

Las 10 rondas usaron 1156 millones de tokens y 30 horas de ejecución de los agentes; en promedio, 116 millones de tokens por ronda.

La redacción del modelo de lenguaje (LLM) —actas, informes, síntesis— se verifica por el contrato de cada comando y por la aritmética de sus cifras, no con un calificador determinista. El material es de prueba: el siguiente paso es el primer uso sobre la documentación de una organización concreta, que decide la versión 1.0.

---

La evidencia completa de cada ronda: [`tests/evidencias/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias).
