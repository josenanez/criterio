# /criterio-portfolio:project-closure PRY-204

## Cierre de PRY-204 (Débito contactless): no procede

**Fuentes:** ficha `estado/records/PRY-204.json`, acta del 2025-09-26, cronograma v1, informe de avance del 2026-10-12, comité del 2026-10-12 y la salida de `compute` del 2026-10-17. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no registré nada nuevo.

**Por qué no se puede cerrar**
- **Criterio de éxito:** el acta lo fija como "Débito contactless en producción y medido". Ningún documento muestra producción ni medición, y el último informe reporta 43 % de avance.
- **Hitos:** los tres figuran como cumplidos (diseño funcional, ambiente de pruebas, integración con el core), pero ninguno tiene evidencia. El avance reportado queda 57,0 puntos por debajo de lo que sustenta el plan.
- **Estado declarado:** el informe dice Verde, y los documentos no lo sostienen.
- **Fecha:** la fecha comprometida (2026-08-23) venció hace 55 días sin cierre. No hubo replanificaciones ni cambios, así que la desviación contra la línea base es 0 días. Es un plan vencido, no uno bien cumplido.
- **Presupuesto (COP):**
  - aprobado: 1.200.000.000
  - comprometido: 757.948.023 (63,2 %)
  - ejecutado: 468.384.958 (39,0 %)
  - proyección al cierre: 1.481.747.420, es decir 23,5 % sobre lo aprobado

  Estas cifras son declaración del informe; ninguna tiene evidencia contable.
- **RAID:** el riesgo "dependencia del calendario de liberaciones del core" sigue abierto y no tiene doliente, probabilidad, impacto ni fecha. Los compromisos de Andrés Lozano (punto 4, 2026-11-09) y Camilo Beltrán (punto 36, 2026-11-02) no dicen qué son esos puntos.
- **Lecciones:** ninguna entra. No hay hechos documentados con fecha y efecto que las sustenten.
- **Archivo:** no propuse mover la carpeta a `archivo/`. El proyecto no está cerrado y archivarlo lo sacaría del barrido diario con seis señales abiertas.

El archivo tiene además las tablas de entregables y de lecciones, y la lista completa de lo que no se pudo determinar. Para cerrar hace falta, en este orden:
1. Que Ricardo Salas diga si el proyecto terminó.
2. Evidencia de producción y medición.
3. Evidencia de los tres hitos.
4. Que Sandra Gil decida sobre la fecha vencida y el sobrecosto proyectado.
5. Un doliente con nombre para el riesgo del core.

**Rigor:** es un borrador de trabajo, no una decisión. Las cifras derivadas salen de `compute`; la verificación contra las citas queda en quien lo use.

**Registro de la corrida:** `2026-10-17-project-closure-1`, 38 segundos. Dejé lo mostrado en `estado/corridas/salida-project-closure.md`.

Se me escapó una errata al escribir el archivo (una fecha de línea base y un número de disponible real mal puestos) y la corregí antes de registrar la corrida.