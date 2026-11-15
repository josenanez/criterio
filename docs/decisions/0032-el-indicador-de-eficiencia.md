# 0032 · El indicador de eficiencia de cada agente, y las tres palancas que lo mueven

**Fecha:** 2026-11-15 · **Estado:** propuesta: el indicador, por publicar en la página de cada agente;
las palancas 1 y 2, aplicadas y medidas en la CFO; la 3, por construir · **Modifica:** el reloj de cada
agente (0028)

## Contexto

José Francisco Ñáñez pidió que cada agente sea más eficiente y más rápido, y que eso se publique como
un indicador en la página de cada agente. Las rondas ya guardan, por cada comando, los tokens que usó,
los que escribió, sus pasos, sus segundos, su costo y su modelo, tal como los informa Claude Code
(`claude -p`). Lo que más pesa es que **cada paso del agente relee todo el contexto**: un comando de
10 a 30 pasos relee entre 300 mil y 1,5 millones de tokens aunque escriba unos pocos miles.

## Decisión

### El indicador

Por agente, desde las corridas publicadas en `tests/evidencias/` —nunca escrito a mano—, lo que
`scripts/consumo_pruebas.py` deja en `plugins/criterio-server/scripts/consumo-pruebas.json`:

| Medida | Qué es |
|---|---|
| Una pasada | La suma de las medianas de los comandos del agente que corrieron en las rondas, en tokens |
| Costo de una pasada | La misma suma, en dólares, con el modelo con que corrió cada comando |
| Tiempo de una pasada | La misma suma, en segundos |
| Un día sin pendientes | Lo que cuesta su reloj cuando no toca nada |
| La evolución | Las mismas medidas ronda por ronda, para ver qué cambió de una versión a otra |

La página del agente muestra la pasada de hoy contra la de la primera ronda con la misma entidad, y
cada cifra lleva la ronda de la que sale. Rostrum la muestra en `/consumo`.

### Las tres palancas

1. **El reloj, por el camino corto.** `despertar` sin `--config` pregunta a todas las configuraciones
   del agente en una sola llamada, con sus términos y sus peticiones; con `--registrar`, si no toca
   nada, el motor deja la corrida registrada él mismo y el agente termina en una línea. Aplicada en
   los once relojes que usan el núcleo común; los tres de la PMO siguen por hacer.
2. **El modelo según el comando.** Los comandos que presentan lo que el motor ya calculó corren con
   un modelo más pequeño (`model: sonnet` en el comando). El setup, el barrido y el reloj siguen con el
   de la sesión, porque procesan documentos. Aplicada en la CFO.
3. **Setups de pocos pasos.** El motor arma en una llamada lo que hoy el agente recorre paso a paso:
   la raíz, el inventario, las cuentas y los términos, y después la configuración, el estado y la
   aceptación. Por construir.

## La primera medición

La ronda 15 de la CFO repite la entidad de Business Central de la ronda 14 con las palancas 1 y 2:

| | Ronda 14 | Ronda 15 | Cambio |
|---|---:|---:|---:|
| Señales y datos | 9 de 9 · 8 de 8 | 9 de 9 · 8 de 8 | Igual |
| Tokens de los 22 comandos | 10,75 M | 10,52 M | −2 % |
| Costo | US$9,00 | US$6,40 | −29 % |
| Los 13 reportes con el modelo más pequeño | — | — | Entre 28 % y 58 % menos costo y entre 9 % y 43 % menos tiempo, cada uno |
| Un día sin pendientes, por agente | 300 mil tokens, 7 pasos | 98 mil tokens, 2 pasos | −67 % en tokens |

Los setups no cambiaron —la palanca 3 no está construida— y variaron entre una corrida y otra:
el de Tomás pasó de 20 a 28 pasos.

## Lo que queda abierto

1. La palanca 3, empezando por los tres setups de la CFO, con su ronda.
2. Las palancas 1 y 2 en la PMO, la CLO, la CCO, la CISO y la EA, cada familia con su ronda.
3. El indicador en el portal: la página de cada agente, desde `consumo-pruebas.json`.
