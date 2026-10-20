# 0006 · El alcance se amplía a la función financiera (CFO)

**Fecha:** 2026-10-20 · **Estado:** aceptada · **Modifica:** 0005

## Contexto

La 0005 dejó el alcance en gestión de proyectos y declaró `criterio-finance` y `criterio-legal`
sin contenido, «hasta que el alcance se amplíe deliberadamente». La familia PMO salió en la
0.5.0 con diez rondas de prueba y su método quedó probado: el modelo de lenguaje (LLM) extrae,
el código calcula, cada dato cita su documento y la decisión sigue siendo de una persona.

La función financiera cumple las cuatro condiciones con que se elige una capacidad: trabajo
recurrente sobre documentos (balances, extractos, facturas, presupuestos), una brecha entre lo
declarado y lo escrito (el cierre que se reporta contra el que sostienen los soportes), cifras
que calcula el código (conciliaciones, cuadres, desviaciones) y una persona que firma.

## Decisión

**El alcance se amplía a una familia CFO con dos roles: el contralor y FP&A.** Se diseña para
NIIF adoptadas localmente, en Colombia y Ecuador, con la factura electrónica de la DIAN y del SRI.

El riesgo que la 0005 nombró sigue siendo el mismo, y por eso la ampliación lleva tres reglas:

1. **Ninguna regla normativa entra sin verificarse contra el texto publicado.** Una tarifa, un
   plazo o un tratamiento contable que no se pueda citar a su fuente oficial no se escribe.
2. **Los formatos sí se leen desde la fuente técnica oficial**: el anexo técnico de la DIAN y la
   ficha técnica del SRI. Son estructura, no opinión, y se pueden verificar campo por campo.
3. **El agente no opina sobre tratamientos ni sobre impuestos en la primera versión.** Contrasta
   documentos y calcula; lo que es criterio contable o fiscal queda como pregunta para la persona.

`criterio-legal` sigue declarado sin contenido. Ampliarlo a la función legal es otra decisión.

## Alternativas descartadas

**Arrancar por la jurisdicción, con paquetes de reglas por país.** Es exactamente lo que la 0005
retiró: reglas sin verificar publicadas con el nombre del responsable.

**Un solo agente para toda la función.** El cierre y el presupuesto tienen dueños, cadencias y
documentos distintos; mezclarlos repite el error que la familia PMO evitó con un agente por rol.

## Consecuencias

- El diseño vive en `families/criterio-cfo/DISENO.es.md` y se construye por incrementos, como la
  familia PMO: primero comandos y skills con sus contratos; después material de prueba con clave;
  después rondas. Nada se declara probado sin ronda.
- La familia es `criterio-cfo`. `criterio-finance` pasa a ser el plugin de Clara, la contralora, y
  `criterio-budget` el de Tomás, FP&A.
- La página de capacidades cambia el estado de CFO de «declarada» a «en construcción» solo cuando
  exista el primer comando que cumpla su contrato.
