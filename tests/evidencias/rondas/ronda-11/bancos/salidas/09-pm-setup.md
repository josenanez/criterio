# /criterio-project:pm-setup documentos/proyectos/PRY-206-billetera-y-qr

## Listo: PRY-206 · Billetera y QR

Nadie respondió preguntas, así que tomé la respuesta sugerida en cada una:
- **Proyecto y gerente:** PRY-206, a cargo de Gustavo Neira.
- **Reunión:** los viernes. La próxima la anoté para el 2026-11-06, porque las notas del 23 dicen «en dos semanas».
- **Estado:** `estado/PRY-206-billetera-y-qr`.
- **Marca `_CRITERIO_PROYECTO.txt`:** no la dejé, porque nadie autorizó escribir dentro de los documentos.

**Términos:** José Francisco Ñáñez los aceptó para esta prueba, versión 1.2 del texto (plugin 0.8.0), con fecha 2026-10-23. El resumen salió tal cual en `salida-pm-setup.md`, con el enlace a la nota legal. La configuración quedó en `.criterio/proyecto/PRY-206/config.json` y `config` la valida sin problemas. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-project-0.8.0-2026-10-23.md` y `.pdf`, con SHA-256 c83631fe2c4cd4b0… (md) y e1748c5331c09218… (pdf).

**Lo que miré:** 16 documentos, de los que 7 son reuniones (6 minutas del 2026-09-11 al 2026-10-16 y las notas del 2026-10-23). Leí todas en orden y no hubo formatos ilegibles. La ficha tiene 26 compromisos y no la sellé. `compute` no devolvió `record_issues`.

### Compromisos
- **Cumplidos con acta (2):** Entregar el punto 8 (María Restrepo) y Validar el ambiente 20 (Javier Hoyos).
- **Movidos varias veces:**

| Quién | Qué | Veces | Fecha vigente |
|---|---|---|---|
| Camilo Beltrán | Cerrar la prueba 2 | 6 | 2027-01-09 |
| Beatriz Cuéllar | Validar el ambiente 4 | 5 | 2026-11-30 |
| Ricardo Salas | Enviar el documento 1 | 4 | 2026-11-30 |

  - La fecha de Camilo viene escrita «09/01/2027» en las notas. La leí día/mes; confírmala. Queda a 16 días de la salida a producción (2027-01-25).
- **Vencidos sin acta (4):**
  - Aprobar el diseño 5 (Camilo Beltrán), vencido el 2026-10-06. «Dijo que ya entregó» el 10-09, pero no hay acta. El acta del 10-14 nombra «Diseño funcional aprobado», no este compromiso.
  - Cerrar la prueba 10 (Andrés Lozano), vencido el 2026-10-15.
  - Validar el ambiente 12 (Rubén Cárdenas), vencido el 2026-10-10.
  - Aprobar el diseño 13 (María Restrepo), vencido el 2026-10-09.
- **Sin fecha (3):**
  - Actualizar la matriz 6 (Diana Molina). Dijo que ya la entregó el 09-25; no hay acta.
  - Confirmar la fecha 15 (Beatriz Cuéllar), «por definir» tres reuniones seguidas.
  - Mandar el ajuste del presupuesto (Laura Vélez), «la otra semana».

### Contra el informe del 2026-10-20 (Verde, 84 %)
No toqué lo declarado; esto es lo que muestran los documentos:
- **Avance:** el cronograma sostiene entre 60 % y 80 %, con 3 de 5 hitos cerrados.
- **Hitos cerrados sin acta (2):** «Ambiente de pruebas certificado» e «Integración con el core».
- **Entregables atrasados de Talento Digital (CT-127):** «Licenciamiento del motor» (108 días) y «Bolsa de horas de desarrollo» (31 días).
- **Entregable de Integra (CT-360) sin acta:** «Licenciamiento del motor» figura recibido, sin acta.
- **Riesgo sin registrar:** en las notas del 23 se comentó que el proveedor podría no llegar con el equipo completo. Lo dejé en la ficha como riesgo sin dueño.

En total salieron 16 señales.

### Qué le falta a tu carpeta
- **Acta del licenciamiento de CT-360:** el contrato factura contra acta firmada y la factura FV-1360 ya está radicada.
- **Actas de los dos hitos cerrados sin acta.**
- **Cierre de los compromisos vencidos:** actas o correos para los 4 vencidos y los 2 que dicen «ya entregué».
- **Cronograma vigente:** el único es la v1 del 2026-04-12 y no tiene ninguna fecha movida.
- **Campos sin dato en el acta de constitución:** alcance genérico («Componente 1, 2, 3»), sin facultad del gerente ni etapa.
- **Notas fuera de lugar:** `2026-10-23-notas-reunion.txt` está suelto en la raíz; su sitio es `30-reuniones/`. No lo moví.

**Cuándo vuelvo:** el viernes 2026-11-06, y el día anterior dejo el informe.

La salida completa y el registro de la corrida están en `estado/PRY-206-billetera-y-qr/corridas/` (`salida-pm-setup.md` y la corrida `2026-10-23-pm-setup-1`). La ficha está en `estado/PRY-206-billetera-y-qr/records/PRY-206.json`.