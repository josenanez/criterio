# 0032 · El indicador de eficiencia de cada agente, y las tres palancas que lo mueven

**Fecha:** 2026-11-15 · **Estado:** propuesta: el indicador, por publicar en la página de cada agente;
las palancas 1 y 2, aplicadas en las seis familias y medidas en la CFO, la CLO, la CCO, la CISO y la EA; la 3, aplicada en los once agentes del núcleo común desde la 2.9.0 y por medir en una ronda; en la PMO, por construir · **Modifica:** el reloj de cada
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
| Una pasada | Los comandos del agente en su corrida más reciente —la de más comandos—, sumados, en tokens |
| Costo de una pasada | La misma suma, en dólares, con el modelo con que corrió cada comando, y el modelo de la sesión, que es el del setup |
| Tiempo de una pasada | La misma suma, en segundos |
| Un día sin pendientes | Lo que costó su reloj en esa corrida si no le tocaba nada: el camino corto, en dos o tres pasos |
| El cambio | Contra la pasada anterior sobre la misma entidad y con el mismo modelo de sesión, en los comandos que corrieron en las dos |

La página de cada familia muestra, por agente, la pasada más reciente y su cambio cuando hay una
anterior comparable, y cada cifra lleva la ronda y el modelo de la sesión de los que sale. Rostrum
muestra lo de cada comando en `/consumo`.

### Las tres palancas

1. **El reloj, por el camino corto.** `despertar` sin `--config` pregunta a todas las configuraciones
   del agente en una sola llamada, con sus términos y sus peticiones; con `--registrar`, si no toca
   nada, el motor deja la corrida registrada él mismo y el agente termina en una línea. Aplicada en
   los catorce relojes: los once del núcleo común y los tres de la PMO (`due --config --registrar`).
   `tests/reloj_corto.py` la comprueba en cada verificación.
2. **El modelo según el comando.** Los comandos que presentan lo que el motor ya calculó corren con
   un modelo más pequeño (`model: sonnet` en el comando). El setup, el barrido y el reloj siguen con el
   de la sesión, porque procesan documentos. Aplicada en 55 comandos de las seis familias.
3. **Setups de pocos pasos.** El motor arma en una llamada lo que hoy el agente recorre paso a paso:
   la raíz, el inventario, las cuentas y los términos, y después la configuración, el estado y la
   aceptación. Aplicada desde la 2.9.0 en los once setups del núcleo común: `arranque` trae la
   carpeta de la entidad, su inventario, los términos y la configuración de ejemplo antes de la
   primera pregunta, y `dejar-listo` prepara el estado, valida la configuración, registra la
   aceptación y marca la carpeta en una llamada después de la última. `tests/setup_corto.py` la
   comprueba en cada verificación. En la PMO, por construir.

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

### Las demás familias

Una ronda por familia, con todos sus comandos, el 15 de noviembre:

| Familia | Ronda · entidad | Señales | Datos | El reloj sin pendientes |
|---|---|---|---|---|
| CLO | 15 · retail de Paraguay | 10 de 10, ninguna de más | 132 de 132 | Fidel y Constanza: de unos 300 mil a 97 mil tokens, de 20 a 9 segundos |
| CCO | 3 · manufactura de México | 20 de 20, ninguna de más | 5 de 5 | No se midió: a los dos les tocaba algo ese día |
| CISO | 3 · banca de Colombia | 25 de 25, ninguna de más | 8 de 8 | No se midió: a los tres les tocaba algo ese día |
| EA | 3 · banca | 50 de 50, ninguna de más | 51 de 51 | No se midió: a Ofelia le tocaba algo ese día |

**Lo que estas rondas enseñan para el indicador:** las rondas anteriores de la CLO, la CCO, la CISO
y la EA corrieron con Sonnet como modelo de toda la sesión; estas, con Opus. El costo del setup y del
barrido depende del modelo de la sesión, que elige quien usa Criterio, así que el indicador compara
siempre con el mismo modelo de sesión y dice cuál fue. Lo que la palanca 2 garantiza es que los
reportes cuestan lo de Sonnet aunque la sesión sea Opus. La PMO no tuvo ronda: su ronda completa
cuesta unos 29 millones de tokens por industria; sus relojes se probaron con el motor.

## Lo que queda abierto

1. La ronda que mida la palanca 3 en los setups del núcleo común, y la palanca 3 en los setups de la PMO.
2. La ronda de la PMO con las palancas 1 y 2.
3. El indicador en el portal: la página de cada agente, desde `consumo-pruebas.json`, con el modelo
   de la sesión de cada ronda.
