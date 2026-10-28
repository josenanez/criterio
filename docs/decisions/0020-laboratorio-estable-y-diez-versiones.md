# 0020 · Laboratorio o estable lo dice la evidencia, y diez versiones por entero

**Fecha:** 2026-10-28 · **Estado:** aceptada el 2026-10-28 · **Modifica:** 0017 · **Reemplaza:** 0018

## Contexto

La decisión 0018 hacía de la 1.0 la versión estable de cada familia, y de todo lo anterior su
laboratorio. Eso juntaba en un solo número dos cosas distintas: **el orden** de las versiones y **la
calidad** de cada una. Una familia que agrega un país puede bajar su calidad sin dejar de avanzar en
su numeración, y una que no falla puede seguir en «laboratorio» solo porque su número todavía no
llega a 1.

Además, la PMO, la CFO, la CLO y la EA ya pasaron la 0.9: van en la 0.12.1.

**Y una sola ronda no basta para decir la calidad.** Musashi lo dice del combate: el mediocre pelea
con una sola katana y el estratega, con todas las herramientas que pueda. Medir con la ronda más
reciente, sola, deja a una familia en laboratorio porque esa ronda fue la de un país, aunque cada
entidad de su material haya pasado su corrida con los agentes. La calidad se dice con toda la
evidencia que hay:

- la corrida con los agentes de cada entidad del material;
- la prueba determinista del motor sobre todo el material, que corre con cada cambio;
- los controles;
- y el margen, que dice cuánto pesa la muestra.

## Decisión

### 1. La calidad es una etiqueta de cada versión, y la calcula el código

Una versión es **estable** cuando su evidencia cumple las tres condiciones. Si no las cumple, es de
**laboratorio**. La evidencia es cada entidad del material con su corrida más reciente con los
agentes, sea de la ronda que sea.

1. **El piso del margen del 95 % de la cobertura de las señales es de 95 % o más.** Se usa el piso
   del intervalo de Wilson, no el resultado puntual: un 100 % sobre 18 señales tiene un piso de
   82,4 %, y no es lo mismo que un 100 % sobre 300.
2. **El piso del margen del 95 % de los datos extraídos es de 95 % o más.**
3. **Ninguna entidad de control levanta una señal.** Una sola basta para que la versión sea de
   laboratorio, sea cual sea el margen.

Las condiciones se aplican así:

- **En la familia PMO** cada agente cuenta por separado, en su ronda más reciente, que corre todo su
  material: la precisión y la cobertura de Vera, los compromisos de Samuel, la cobertura de Alba y los
  proyectos de control sin alertas.
- **Una familia con una entidad que nunca corrió con los agentes es de laboratorio.**
- **La prueba del motor no es opcional.** Ninguna versión se libera con una puerta de
  `scripts/verificar.py` en rojo. Esa prueba corre el motor sobre todo el material con su clave, y
  sostiene el cálculo en cada versión, también en las que no traen una ronda nueva con los agentes.

`scripts/calidad.py` calcula la etiqueta desde `tests/evidencias/`. `scripts/registro.py` la anota
en cada liberación, con las rondas que la sostienen y sus pisos. Nadie la escribe a mano.

**El piso exige muestra.** Sin fallas, un 95 % pide al menos 73 casos; con una falla, 110. Una
familia que no falla y no llega es de laboratorio por tamaño, no por error. La salida barata es
sembrar más señales por entidad, no agregar entidades: el costo de una ronda crece con las entidades
y los comandos, no con las señales.

**Una versión que no alcanza el umbral sale como laboratorio**, con su análisis publicado. La
siguiente puede volver a ser estable. Ninguna familia se bloquea.

### 2. Diez versiones por entero

- **Cada número entero tiene diez versiones,** de x.0 a x.9, y después de la x.9 viene la x+1.0.
  Las correcciones —el tercer número, x.y.1— no cuentan entre las diez.
- **Las únicas excepciones son la 0.10, la 0.11 y la 0.12** de la PMO, la CFO, la CLO y la EA. El
  registro no se reescribe, y esas versiones se quedan como están. La próxima liberación de cada una
  de esas familias es su **1.0.0**, y desde ahí se cumple la regla.
- **La CSO empieza en la 0.1.0** y recorre su década completa.
- **Rostrum** está en la 0.12.1, como las cuatro familias. Su próxima liberación es la 1.0.0.

`scripts/registro.py liberar` falla con una versión que no siga la regla.

### 3. Lo que el número ya no dice

El número entero ya no anuncia la estabilidad, que dice la etiqueta, ni un cambio incompatible.

**Un cambio que rompe el esquema de la ficha** se declara en la entrada del registro y en las notas
de la versión, y la aceptación de los términos se pide de nuevo, como en cualquier versión nueva de
la familia.

## La calidad hoy

Calculada por `scripts/calidad.py` el 2026-10-28:

| Familia | Etiqueta | La evidencia | Los pisos |
|---|---|---|---|
| PMO | Estable | La ronda 11, sobre la versión 0.8.0 | Vera 99,0 % y 99,0 %, Samuel 97,6 %, Alba 98,1 %; controles limpios |
| CFO | Estable | La corrida más reciente de cada una de sus 15 entidades, rondas 4 a 6 | Señales 97,1 % (133), datos 96,9 % (122); controles limpios |
| CLO | Estable | La corrida más reciente de cada una de sus 15 entidades, rondas 2 a 5 | Señales 95,8 % (89), datos 99,6 % (2.012); controles limpios |
| EA | Laboratorio | La ronda 1 | Señales 78,4 % (14 señales: la muestra no alcanza), datos 95,3 % |
| CSO | Laboratorio | Sin ronda con los agentes | — |

La EA no falló ninguna señal. Es de laboratorio porque su material siembra 14: para un piso del 95 %
necesita 73.

## Consecuencias

- La 0018 queda reemplazada: la 1.0 ya no es «la versión estable», y el incremento reservado
  «La versión estable» sale de cada hoja de ruta.
- La próxima liberación de la PMO, la CFO, la CLO, la EA y Rostrum es su 1.0.0. La de la PMO,
  telecomunicaciones y logística, es la 1.0.0; la 0.14.0 que tenía planeada pasa a ser la 1.1.0.
- La hoja de ruta completa muestra la calidad de cada familia en lugar de su primera versión.
- El portal dice «laboratorio» o «estable» de cada familia con la etiqueta calculada, no con su
  número.
- El material de la EA y el de la CSO siembran señales suficientes para que su piso pueda llegar al
  95 %.
