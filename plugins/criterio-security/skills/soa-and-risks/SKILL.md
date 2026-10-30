---
name: soa-and-risks
description: "La declaración de aplicabilidad y el registro de riesgos: qué es un control aplicable e implementado, su responsable y su periodicidad, y qué es una aceptación de riesgo con su fecha de revisión. Úsalo al revisar la declaración de `00-referencia/` o el registro de `40-riesgos/`. Statement of applicability, risk register, risk acceptance."
---

# La declaración de aplicabilidad y el registro de riesgos

## La declaración de aplicabilidad

Es la tabla en que la organización dice qué controles aplica y por qué. Su vocabulario suele ser el del anexo A de la ISO/IEC 27001:2022 (F-03), pero **el motor no trae la norma**: toma cada control con el número y el nombre que le da la organización. `A.8.13`, `8.13` y `A 8.13 Respaldo de la información` son el mismo control.

- **Aplicable**: sí o no. Un control que no aplica no se revisa.
- **Estado**: el que dice la organización. El motor pide evidencia solo a los que figuran **implementados u operando**; uno en implementación no la pide todavía.
- **Responsable**: quien responde por el control. Un control aplicable sin responsable es una señal.
- **Periodicidad**: cada cuánto tiene que haber evidencia de que operó —mensual, trimestral, semestral, anual o un número de días—. Sin periodicidad, el motor pide alguna evidencia, no una reciente.

**Nadie declara cumplido un control aquí.** El motor dice cuál no tiene evidencia y cuál la tiene vencida; la conclusión es de una persona.

## El registro de riesgos

Cada riesgo con su decisión —mitigar, transferir, evitar, aceptar— y, cuando se acepta, quién lo aceptó y **hasta cuándo**. Una aceptación de riesgo sin fecha de revisión no se puede vigilar: el motor lo dice. Una aceptación que pasó su fecha es una señal: alguien tiene que volver a decidir.

**El agente nunca acepta, cierra ni cambia la decisión sobre un riesgo**, ni sugiere aceptarlo.
