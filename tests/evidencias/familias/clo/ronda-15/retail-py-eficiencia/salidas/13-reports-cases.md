# /criterio-compliance:reports-cases 

Los términos estaban vigentes (versión 1.5), así que seguí con el reporte. Hay un caso fuera de plazo: C-003, de conflicto de interés.

**C-003:** se recibió el 2026-08-28 y sigue sin respuesta. Lleva 39 días y el plazo configurado es de 15 (`40-canal/casos.csv`, fila 4).

| Caso | Tipo | Recibido | Respondido | Días |
|---|---|---|---|---|
| C-001 | trato al cliente | 2026-08-01 | 2026-08-10 | 9 |
| C-002 | proveedores | 2026-09-25 | abierto | 11 |
| C-003 | conflicto de interés | 2026-08-28 | abierto | 39 |

C-002 está abierto, pero lleva 11 días y sigue dentro del plazo. El reporte no incluye datos de quién denunció. Todo lo que llegó se procesó y el motor no hizo preguntas.

El reporte quedó en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/cumplimiento/2026-10/reporte-reports-cases.md`. Guardé lo mostrado en `corridas/salida-reports-cases.md`, en esa misma carpeta de estado. La corrida quedó registrada como `2026-10-06-reports-cases-1`, y el motor la cuenta con 5 hallazgos.

La configuración no tiene una clave de estado que se pueda leer directamente. Primero creé por error una carpeta vacía bajo `.criterio/cumplimiento/`, y la borré. La ruta correcta la tomé de `paths.state` en `config.json`.