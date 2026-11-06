# 0029 · La demostración: Criterio funcionando antes de abrir un documento propio

**Fecha:** 2026-11-06 · **Estado:** aceptada el 2026-11-06 · **Modifica:** lo que trae Rostrum; ningún agente cambia

## Contexto

Quien dirige una función decide si le abre sus documentos a un agente después de verlo trabajar, no
antes. Hasta ahora la única forma de verlo era instalarlo y correr su setup sobre documentos propios:
quince minutos por agente y una decisión de confianza tomada a ciegas.

José Francisco Ñáñez pidió el 6 de noviembre de 2026 un modo de demostración que deje todo listo en
unos cinco minutos.

## Decisión

1. **`/criterio-server:server-demo`.** Va en Rostrum porque Rostrum lo instala cualquier familia y
   es donde se ve todo junto. Descomprime una organización de prueba en `./criterio-demo`, pide los
   términos de Rostrum y lo levanta sobre ella, con un recorrido en cuatro enlaces.
2. **Una entidad por familia, del material de prueba, sin su clave**: el portafolio de la PMO, el
   Banco Andino en finanzas y legal, Almacenes del Valle en comercial, el Banco Cordillera en
   seguridad y una presidencia en dirección.
3. **Nada se escribe a mano.** `scripts/demo.py` escribe en el estado lo que el agente extraería, con
   la misma función con la que se prueba cada motor (`sembrar`), toma las configuraciones de la
   clave y corre el motor de cada agente, el de su propio plugin. El resultado es un zip
   determinista en `plugins/criterio-server/demo/`.
4. **Una puerta lo compara byte a byte** (`scripts/demo.py --check`): un cambio en un motor o en el
   material que mueva la demostración rompe la verificación hasta que se regenere. La liberación de
   cada versión la regenera, porque los reportes llevan la versión de cada motor.
5. **No procesa ningún documento de la persona** y no escribe fuera de la carpeta de la
   demostración. La oficina de Ofelia está en la demostración pero no en el portal, como en
   cualquier organización (ADR 0012).

## Consecuencias

- Una persona ve en cinco minutos lo que cada familia levanta, sin decidir antes si confía.
- Las fechas del material son las de su ronda, entre septiembre y noviembre de 2026: con el tiempo,
  más filas aparecen como «ya pasó». Se dice en el recorrido.
- Lo que la demostración muestra es lo que el motor calcula con la extracción correcta. Cómo extrae
  el agente lo prueban las rondas, no la demostración.
