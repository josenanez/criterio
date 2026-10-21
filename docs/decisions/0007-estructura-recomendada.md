# 0007 · La familia PMO recomienda una estructura de carpetas

**Fecha:** 2026-10-20 · **Estado:** aceptada · **Modificada por:** [0011](0011-la-carpeta-raiz-se-busca-y-se-marca.md), que permite marcar la carpeta raíz con permiso

## Contexto

Los agentes de la familia PMO procesan la carpeta como esté, y las pruebas lo comprueban con
cuatro disposiciones: la de referencia, plana, revuelta y sin carpeta por caso. La estructura de
referencia existía solo para el material de prueba, y `tests/sintetico/corpus.py` dejó escrito
que convertirla en recomendación sería una decisión de producto.

Quien adopta la familia pregunta dónde va cada documento. La familia CFO nace con una estructura
de carpetas por periodo, y conviene que las dos familias respondan esa pregunta de la misma forma.

## Decisión

**La estructura de referencia pasa a ser la estructura recomendada, y sigue sin ser un
requisito.** Una sola fuente, `families/criterio-pmo/carpetas.json`, la define; la usa el material
de prueba y `scripts/carpetas.py` la escribe en los README de la familia y en el skill
`document-intake` de los tres plugins. Una puerta comprueba que las cinco copias digan lo mismo.

Los comandos de setup la muestran como sugerencia cuando la carpeta no está ordenada. Nunca
mueven, renombran ni crean nada dentro de los documentos de la organización.

## Alternativas descartadas

**Hacerla obligatoria.** Rompe la promesa que las pruebas sostienen —funciona con lo que haya— y
deja fuera a quien ya tiene sus documentos organizados de otra forma.

**Que el setup cree las carpetas.** Escribe en los documentos de la organización, y el contrato de
los comandos de setup solo les permite escribir su configuración y su estado.

## Consecuencias

Es un cambio de comportamiento de los tres setups: entra en la siguiente versión menor, la 0.7.0,
y la ronda de esa versión lo prueba.
