# 0017 · Una versión por familia

**Fecha:** 2026-10-28 · **Estado:** aceptada el 2026-10-28 · **Modifica:** el versionado de `GOVERNANCE.es.md`

## Contexto

Hasta la 0.12.0, Criterio tuvo un solo número de versión para el marketplace y los diez plugins:
cada liberación subía la versión de todos, aunque solo hubiera cambiado una familia. La CFO que
sumó México llevó a la PMO, que no cambió, de la 0.11.0 a la 0.12.0, y a quien usa la PMO le pidió
aceptar los términos de nuevo por una versión que no traía nada suyo.

Las familias son independientes: cada una tiene sus agentes, su material de prueba, sus rondas y
su hoja de ruta, y crece a su ritmo. El número tiene que decir lo mismo.

## Decisión

**Cada familia lleva su propio número**, el mismo en todos sus plugins, y sube solo cuando ella
cambia: la PMO (Vera, Samuel y Alba), la CFO (Clara, Tomás y Áurea), la CLO (Fidel y Constanza), la
EA (Ofelia) y Rostrum, que sirve a todas. Qué plugins forman cada familia lo dice su `familia.json`;
Rostrum es su propia familia.

**El marketplace lleva el número del catálogo**, que sube con cada entrada del registro. Una
liberación dice qué familias suben y a qué versión: `registro.py liberar 0.13.0 --familia pmo=0.13.0`.
Un cambio común a todas —los términos, por ejemplo— las sube a todas: `--todas`.

**El registro sigue siendo una sola cadena.** Cada entrada nueva anota la versión de cada familia,
la de cada plugin y cuáles se liberaron en ella. Las entradas anteriores no se reescriben: tienen una
sola versión para todo, y así se leen.

**La aceptación de los términos va con la versión de la familia.** Cada versión de una familia pide
aceptar de nuevo; una versión de otra familia, no. El comprobante cita la entrada del registro donde
su plugin llegó a esa versión.

**Las puertas lo hacen cumplir.** `registro.py verificar` falla si un plugin no está en la versión
que la última entrada le registra a su familia, si un plugin no pertenece a ninguna familia, o si los
términos cambiaron sin una versión nueva. La hoja de ruta de cada familia se contrasta con las
versiones de esa familia, no con las de las demás.

## Consecuencias

- Desde la 0.12.1 los números se separan: todas las familias salen en 0.12.1, porque la llevan los
  términos 1.3, y de ahí cada una sube con lo suyo.
- La etiqueta de GitHub sigue siendo una por entrada del registro, con el número del catálogo, y sus
  notas dicen qué familias trae y en qué versión.
- La versión 1.0 de una familia es de esa familia: no arrastra a las demás.
