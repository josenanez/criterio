# 0009 · El alcance se amplía a la función legal (CLO)

**Fecha:** 2026-10-20 · **Estado:** aceptada · **Modifica:** 0006

## Contexto

La 0006 amplió el alcance a la función financiera y dejó `criterio-legal` declarado sin
contenido: «ampliarlo a la función legal es otra decisión». La familia CFO salió construida con
su motor probado contra material sintético, y su forma —el motor procesa las tablas, el agente
extrae lo escrito, cada dato con su cita— sirve igual para lo que la empresa firmó.

La función legal cumple las mismas cuatro condiciones: trabajo recurrente sobre documentos
(contratos, otrosíes, pólizas, matrices), una brecha entre lo declarado y lo escrito (el
contrato que el registro dice vigente y ya terminó), cifras y fechas que calcula el código
(vencimientos, preavisos, pagos contra valor) y una persona que decide.

## Decisión

**El alcance se amplía a una familia CLO con dos roles: contratos y cumplimiento**, en Colombia y
Ecuador. Fidel (`criterio-legal`) procesa lo firmado; Constanza (`criterio-compliance`), la
matriz de obligaciones de la organización contra su evidencia.

Las tres reglas de la 0006 siguen, con una más estricta:

1. **Ninguna regla normativa entra sin verificarse contra el texto publicado.**
2. **Lo que una obligación exige lo define la organización en su matriz**, con la cita de su
   fuente. La familia no trae obligaciones propias.
3. **Sin opinión jurídica en la primera versión**: ninguno interpreta una cláusula o una norma ni
   califica la validez de un contrato o de una firma; lo que es criterio jurídico queda como
   pregunta para la persona.

## Alternativas descartadas

**Revisión de cláusulas con criterio de derecho civil por país**, que era lo que declaraba
`criterio-legal`. Es opinión jurídica con el nombre del responsable, el riesgo que la 0005 retiró.

**Un solo agente para la función.** Contratos y cumplimiento tienen dueños, cadencias y documentos
distintos.

## Consecuencias

- El diseño vive en `families/criterio-clo/DISENO.es.md`, desde las mismas tres fuentes que la
  familia CFO, y lo escribe `scripts/familias.py`.
- El motor, `legal.py`, usa el núcleo común de la familia CFO (`nucleo.py`) y se prueba con
  `tests/criterio-clo/evaluar.py` contra una clave.
