# 0022 · La familia comercial se llama CCO

**Fecha:** 2026-10-30 · **Estado:** aceptada el 2026-10-30 · **Modifica:** 0019

## Contexto

La decisión 0019 abrió la familia de Augusto y Valeria como «Criterio CSO · La función comercial»,
por Chief Sales Officer. La sigla se lee de varias formas:

- **Chief Security Officer.** Choca con la familia de seguridad de la información (decisión 0013),
  que es la siguiente en construirse.
- **Chief Strategy Officer** y **Chief Sustainability Officer.**

Se consideraron dos alternativas:

- **CRO**, Chief Revenue Officer. Describe el ciclo que procesa la familia, de la oportunidad a la
  comisión.
- **CCO**, Chief Commercial Officer. Es el título de la función comercial en las organizaciones de la
  región: la vicepresidencia o la gerencia comercial. También se lee como Chief Compliance Officer,
  pero el cumplimiento ya tiene su nombre y su agente en la familia CLO, Constanza.

## Decisión

La familia se llama **Criterio CCO · La función comercial**, por Chief Commercial Officer. Lo decidió
José Francisco Ñáñez.

- La sigla cambia en todo lo que se sigue escribiendo:
  - la carpeta de la familia: `families/criterio-cco`;
  - el material de prueba: `tests/criterio-cco`;
  - la evidencia de sus rondas: `tests/evidencias/familias/cco`;
  - la página del portal: `/agents/criterio-cco`. La dirección anterior lleva a la nueva.
- Los defectos de sus rondas se numeran CCO-1 en adelante. Los que eran CSO-1 a CSO-4 son CCO-1 a
  CCO-4.
- Los plugins no cambian: `criterio-sales` (Augusto) y `criterio-revenue` (Valeria). Tampoco cambian
  las carpetas de su configuración, `.criterio/comercial` y `.criterio/ingresos`.
- **El registro no se reescribe.** Las entradas de los catálogos 1.0.0 a 1.3.0 están selladas con su
  huella SHA-256 y dicen `cso`. `scripts/registro.py` las lee con la sigla de hoy
  (`RENOMBRADAS`): la CSO 0.1.0 y 0.2.0 es la CCO 0.1.0 y 0.2.0. Las notas de esos lanzamientos y las
  decisiones 0019 a 0021 quedan como se escribieron.
- La familia todavía no se ha lanzado. El cambio no toca a nadie que la haya anunciado.
