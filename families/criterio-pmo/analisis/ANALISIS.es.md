# Análisis estadístico de las pruebas · familia PMO

Generado por `scripts/analisis.py` desde `tests/evidencias/` · ronda más reciente: 12 (2026-10-28), versión probada 1.0.0 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La versión más reciente probada, 1.0.0, en la ronda 12: Vera con 100 % de precisión (margen del 95 %: 96,9–100 %) y 100 % de cobertura; Samuel con 100 % de compromisos correctos; Alba con 100 % de alertas encontradas; Rostrum con 100 % de comprobaciones.

Sumando las rondas 1–12, Vera acertó en el 99,2 % de las 2944 alertas que emitió y encontró el 99,7 % de las 2928 que había. Desde la ronda 6, las cuatro métricas se mantienen por encima del 99 %.

## Qué se probó y cómo

Cada ronda sortea hechos nuevos y escribe una clave que ningún agente ve. Los datos de prueba se construyeron para ser más exigentes que la documentación de una PMO promedio, y cada industria lleva un proyecto sano que no debe levantar ninguna alerta.

Precisión: de las alertas emitidas, cuántas eran correctas. Cobertura: de las que había, cuántas encontró. Margen del 95 %: intervalo de confianza de Wilson sobre los casos; para Vera en la última ronda, el que remuestrea proyectos.

|   |   |
|---|---|
| Periodo | 12 rondas, 2026-10-15 → 2026-10-28, versiones 0.3.6 → 1.0.0 |
| Industrias | Logística, Telecomunicaciones |
| Proyectos analizados | 624 |
| Documentos procesados | 6246: Markdown 3392, Word 1455, PDF 623, Excel 376, CSV 253, texto 60, JSON 48, xml 39 |
| Ejecuciones | 1784 |
| Lecturas de la clave | 0 |
| Proyectos de control | 48 |

## Resultados acumulados · rondas 1–12

Los acumulados de Samuel, Alba y Rostrum incluyen las primeras rondas, cuando esas capacidades se estaban construyendo; su valor actual es el de la versión más reciente.

| Agente · métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Vera · precisión | 2919 de 2944 | 99,2 % | 98,7–99,5 % |
| Vera · cobertura | 2919 de 2928 | 99,7 % | 99,4–99,9 % |
| Vera · proyectos de control sin alertas | 48 de 48 | 100 % | 92,5–100 % |
| Samuel · compromisos correctos | 1056 de 1092 | 96,7 % | 95,4–97,7 % |
| Alba · cobertura | 1413 de 1462 | 96,6 % | 95,5–97,5 % |
| Alba · precisión | 1413 de 1425 | 99,2 % | 98,5–99,6 % |
| Rostrum · comprobaciones (11 rondas) | 23 011 de 23 487 | 98 % | 97,7–98,2 % |
| Contratos cumplidos | 1766 de 1784 | 99 % | 98,4–99,4 % |

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
| 10 · 0.5.0 | 52 | 531 | 100 % | 100 % | 100 % | 100 % | 100 % | 4 |
| 11 · 0.8.0 | 78 | 823 | 100 % | 100 % | 100 % | 99,9 % | 99,6 % | 2 |
| 12 · 1.0.0 | 26 | 286 | 100 % | 100 % | 100 % | 100 % | 100 % | 0 |

## La versión más reciente probada · 1.0.0, ronda 12

Vera no emitió ninguna alerta falsa.

| Agente · métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Vera · precisión | 119 de 119 | 100 % | 96,9–100 % |
| Vera · cobertura | 119 de 119 | 100 % | 96,9–100 % |
| Samuel · compromisos correctos | 54 de 54 | 100 % | 93,3–100 % |
| Alba · cobertura | 61 de 61 | 100 % | 94–100 % |
| Alba · precisión | 61 de 61 | 100 % | 94–100 % |
| Rostrum · comprobaciones | 1072 de 1072 | 100 % | 99,6–100 % |
| Contratos cumplidos | 76 de 76 | 100 % | 95,1–100 % |

## Por industria · rondas 1–12

| Industria | Vera · precisión | Vera · cobertura | Samuel | Alba · cobertura | Alba · precisión | Rostrum |
|---|---|---|---|---|---|---|
| Banca | 98,7 % | 100 % | 90,2 % | 94,1 % | 98,5 % | 97,6 % |
| Cooperativas | 99,6 % | 100 % | 98,4 % | 98 % | 99,7 % | 97,9 % |
| Minería | 98,6 % | 98,6 % | 98,4 % | 97 % | 98,5 % | 98 % |
| Retail | 99,4 % | 100 % | 98,4 % | 96,5 % | 99,7 % | 97,6 % |
| Construcción | 100 % | 100 % | 100 % | 100 % | 100 % | 99,8 % |
| Oil & gas | 100 % | 100 % | 100 % | 100 % | 100 % | 100 % |
| Logística | 100 % | 100 % | 100 % | 100 % | 100 % | 100 % |
| Telecomunicaciones | 100 % | 100 % | 100 % | 100 % | 100 % | 100 % |

## Por tipo de alerta · Vera, rondas 1–12

Vera emitió alertas de 18 tipos; en 15 no tuvo una sola alerta falsa, y las 25 falsas se concentran en 3. «Gerente y PMO no dicen lo mismo» todavía no se sostiene: 18 falsas y ninguna correcta, la última en la ronda 9, ninguna en la ronda 12. Es la que hay que reforzar.

| Tipo de alerta | Correctas | Falsas | No detectadas | Precisión | Cobertura |
|---|---|---|---|---|---|
| Hito dado por cumplido sin evidencia | 986 | 0 | 0 | 100 % | 100 % |
| Compromiso vencido sin evidencia | 355 | 0 | 4 | 100 % | 98,9 % |
| Avance declarado que el plan no sostiene | 314 | 0 | 0 | 100 % | 100 % |
| Verde que la evidencia no sostiene | 270 | 0 | 0 | 100 % | 100 % |
| Entregable de proveedor vencido | 202 | 0 | 0 | 100 % | 100 % |
| Compromiso que nadie fechó | 168 | 0 | 1 | 100 % | 99,4 % |
| Desviación en tiempo | 116 | 0 | 1 | 100 % | 99,1 % |
| Compromiso prometido una y otra vez | 106 | 2 | 2 | 98,1 % | 98,1 % |
| Desviación en costo | 101 | 0 | 0 | 100 % | 100 % |
| Línea base movida más de lo autorizado | 67 | 0 | 1 | 100 % | 98,5 % |
| Entrega dada por aceptada sin evidencia | 53 | 5 | 0 | 91,4 % | 100 % |
| Hito vencido | 53 | 0 | 0 | 100 % | 100 % |
| Cambio aprobado sin línea base nueva | 35 | 0 | 0 | 100 % | 100 % |
| Facturado sin entregable aceptado | 34 | 0 | 0 | 100 % | 100 % |
| Proyecto sin actividad | 27 | 0 | 0 | 100 % | 100 % |
| Facturado por encima de lo aceptado | 26 | 0 | 0 | 100 % | 100 % |
| Presupuesto comprometido sin holgura | 6 | 0 | 0 | 100 % | 100 % |
| Gerente y PMO no dicen lo mismo | 0 | 18 | 0 | 0 % | — |

## Defectos

![Defectos](defectos-es.svg)

63 defectos registrados, cada uno con su origen, su corrección y la ronda que la verificó: 63 verificados y 0 por verificar. 18 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Código | 24 |
| Instrucciones del agente | 20 |
| Material de prueba | 10 |
| Clave de calificación | 4 |
| Arnés de pruebas | 4 |
| Comportamiento del modelo | 1 |

| Agente | Defectos |
|---|---|
| Vera | 29 |
| Samuel | 11 |
| Rostrum | 10 |
| Alba | 9 |
| Los tres | 4 |

## Tiempo, consumo y próximo paso

Las 12 rondas tomaron 37 horas de ejecución para 624 proyectos: 3,5 minutos por proyecto, con todos los comandos de los tres agentes y el servidor. Usaron 1391 millones de tokens; en promedio, 116 millones por ronda.

Las actas, los informes y las síntesis que redacta el modelo de lenguaje (LLM) se verifican por el contrato de cada comando y por la aritmética de sus cifras. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en cada agente y ninguna alerta en los proyectos de control (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias).
