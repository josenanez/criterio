# /criterio-product:product-wake 

Corrida de `product-wake` registrada para PRD-302 (Gas para generación). Era la primera, así que no había un corte anterior con el cual comparar y el informe describe el estado de hoy. Ese estado queda como línea base.

- **Términos:** ya estaban vigentes, aceptados por José Francisco Ñáñez para la versión 0.8.0. No hizo falta registrar nada.
- **Qué tocaba:** solo la revisión (`review`). La próxima es el 2026-11-22.
- **Lo que necesita decisión:**
  - REQ-4202 lleva 116 días propuesto sin decidirse y REQ-4211 lleva 75. Los dos son de Rubén Cárdenas.
  - El supuesto «La comunidad respalda el proyecto» lleva 124 días sin verificarse y no tiene dueño registrado.
  - REQ-4204 está aceptado y no tiene doliente, criterio de aceptación ni evidencia.
- **Huecos en lo aceptado:** 4 aceptados sin criterio de aceptación y 7 sin evidencia de demanda.
- **Declarado contra medido:** `volumen_mensual` declara 115.628 y el tablero mide 98.962, una brecha de 14,4 %. Está por debajo del umbral de 20 %, así que no es hallazgo.
- **Trazas:** ninguna se da por confirmada. La configuración no apunta a una carpeta de fichas de proyecto, así que los 16 aceptados figuran sin proyecto. Eso puede ser cierto o puede ser solo que faltan las fichas.
- **No leí documentos:** no releí ninguno ni revisé la carpeta de descubrimiento, porque sin corte previo no hay contra qué comparar.

El archivo `salida-product-wake.md` y el corte (`snapshots/2026-10-23.json`) están guardados en `estado-producto/PRD-302/`. La corrida quedó con 31 hallazgos sobre 18 requerimientos y duró 20 segundos.