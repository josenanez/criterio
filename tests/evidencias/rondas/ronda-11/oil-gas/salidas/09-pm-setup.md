# /criterio-project:pm-setup documentos/proyectos/PRY-200-campaña-de-perforación-del-bloque-sur

## Listo: PRY-200, Campaña de perforación del bloque sur

Leí los 15 documentos, de la minuta más vieja a la más nueva. Son 6 minutas semanales (2026-09-10 a 2026-10-15), las notas del 2026-10-22, 5 actas de recibo, el acta de constitución, el cronograma y el informe de avance. Todos eran legibles.

**Preguntas:** las cuatro con la respuesta sugerida, porque la sesión no tenía interfaz.
- La reunión de seguimiento es los jueves. Las notas del 2026-10-22 dicen que la próxima es en dos semanas, así que quedó para el 2026-11-05.
- El estado queda en `estado/PRY-200-campaña-de-perforación-del-bloque-sur`.
- No dejé la marca `_CRITERIO_PROYECTO.txt`, porque nadie autorizó escribir dentro de los documentos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-22, versión 0.8.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-project-0.8.0-2026-10-22.md` y `.pdf`. El SHA-256 del texto empieza en `97ef3d7200b125fa`.

### Compromisos
Son 26 en total: 3 cumplidos con acta, 8 vencidos sin evidencia, 3 sin fecha y 12 vigentes.

- **Ricardo Salas, «Enviar el documento 1»:** se reprogramó 6 veces (09-30 → 10-21 → 11-09 → 11-29 → 12-18 → 2027-01-01 → 2027-01-15).
- **Ricardo Salas, «Cerrar la prueba 2»:** se reprogramó 5 veces (09-15 → 09-24 → 10-13 → 11-02 → 11-20 → 11-29).
- **Vencidos sin evidencia (8):**

| Compromiso | Responsable | Días vencido |
|---|---|---|
| Confirmar la fecha 7 | Beatriz Cuéllar | 28 |
| Actualizar la matriz 14 | Laura Vélez | 19 |
| Aprobar el diseño 13 | Ricardo Salas | 18 |
| Aprobar el diseño 5 | Felipe Arango | 9 |
| Enviar el documento 9 | María Restrepo | 2 |
| Validar el ambiente 20 | Laura Vélez | 2 |
| Aprobar el diseño 21 | Óscar Ramírez | 2 |
| Cerrar la prueba 18 | Elena Duarte | 1 |

- Quienes dijeron que ya entregaron sin que haya acta no cierran el compromiso: Arango (diseño 5), Cuéllar (fecha 7), Torres, Pérez y Beltrán.
- **Sin fecha (3):**
  - Camilo Beltrán, «Entregar el punto 8».
  - Rubén Cárdenas, «Entregar el punto 16».
  - Laura Vélez, «Mandar el ajuste del presupuesto», que dijo «la otra semana».

### Contra lo declarado
El informe del 2026-10-19 declara verde y 84 % de avance. El cálculo dejó 17 señales, y 4 tipos de ellas contradicen ese verde:
- «Licencia ambiental otorgada» y «Montaje de facilidades» están cerrados en el cronograma, pero no hay acta de recibo de ninguno.
- El cronograma tiene 4 de 4 hitos cerrados y el informe dice 84 %, una diferencia de 16 puntos.
- La fecha de cierre vigente era el 2026-10-06 y ya pasó.
- La proyección al cierre es 3.453.463.040 COP, 4,7 % sobre los 3.300.000.000 aprobados. Va comprometido el 31,1 % y ejecutado el 16,3 %.
- Hay un riesgo que nadie registró: las notas del 22 de octubre dicen que el proveedor podría no llegar con el equipo completo.

### Qué le falta a la carpeta
- Actas de recibo de los dos hitos sin acta y de lo que dicen haber entregado Arango, Cuéllar, Torres, Pérez y Beltrán.
- Un cronograma posterior al v1, que nunca se ha movido, ni con el cierre vencido.
- El acta de constitución no trae la autoridad del gerente ni la etapa del proyecto, y los tres componentes del alcance no tienen nombre. Esos campos quedaron sin dato.

**Cuándo vuelvo:** el jueves 2026-11-05. No sellé la ficha, tal como pide el comando.

**Archivos que escribí:**
- Configuración: `.criterio/proyecto/PRY-200/config.json`.
- Ficha: `estado/PRY-200-campaña-de-perforación-del-bloque-sur/records/PRY-200.json`.
- Salida de la corrida: `estado/PRY-200-campaña-de-perforación-del-bloque-sur/corridas/salida-pm-setup.md`.
- Registro de la corrida: `2026-10-23-pm-setup-1`.

**Tiempo:** no se midió, porque no se corrió `corrida-inicio`.