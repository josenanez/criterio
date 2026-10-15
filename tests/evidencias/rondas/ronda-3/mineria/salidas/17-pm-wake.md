# /criterio-project:pm-wake 

## PRY-203 Despacho automático de flota · 2026-10-15

Los términos ya estaban vigentes: José Francisco Ñáñez los aceptó hoy (v0.3.9), así que no los registré de nuevo.

**Revisé:** 19 documentos, todos nuevos porque era el primer barrido. Entre ellos hay 7 minutas: los 6 comités del 09-03 al 10-08 y las notas de hoy.

### Lo que se venció solo
La ficha solo tenía los 3 compromisos de las notas de hoy. Los comités traían 23 más sin leer, y ahora están registrados con su historial.

**Vencidos sin evidencia (4):**
- **Actualizar la matriz 6** (Elena Duarte) venció el 2026-10-11, sin acta de recibo. El comité del 10-08 la repitió con la misma fecha.
- **Revisar el anexo 3** (Elena Duarte) venció el 2026-09-30. El 09-17 se dijo «ya entregó», no hubo acta y salió de la lista.
- **Validar el ambiente 4** (Beatriz Cuéllar) venció el 2026-09-09. Pasó lo mismo que con el anexo 3.
- **Aprobar el diseño 13** (Andrés Lozano) venció el 2026-10-04. Se dijo «ya entregó» el 10-01, sin acta, y salió de la lista el 10-08.

**Reprogramados:**
- **Enviar el documento 1** (Óscar Ramírez): 6 veces. Hoy quedó para el 2026-11-24, 75 días después de la primera promesa.
- **Cerrar la prueba 2** (Paula Céspedes): 5 veces. Hoy está para el 2026-11-13.

**Sin fecha (4):**
- El ajuste del presupuesto de Laura Vélez («la otra semana»).
- Entregar el punto 16 (Elena Duarte).
- Validar el ambiente 20 (Óscar Ramírez).
- Confirmar la fecha 15 (Diana Molina). El 10-08 se dijo «ya entregó», sin acta.

**Para vigilar:**
- Validar el ambiente 12 (Mauricio Pérez) vence hoy y todavía no hay acta.
- Cerrar la prueba 18 (Ricardo Salas) vence el 10-16.
- Aprobar el diseño 5 y Cerrar la prueba 10 también salieron de la lista con «ya entregó» sin acta, pero su fecha (10-21 y 10-20) aún no llega.

**Cerrados con acta:** Confirmar la fecha 7, Revisar el anexo 11 y Actualizar la matriz 14.

Las notas de hoy no dicen nada de los compromisos abiertos de los comités anteriores. No los di por cumplidos ni por reprogramados.

### La reunión
La reunión de hoy ya tiene acta, de una corrida anterior de hoy, así que no ofrezco `/pm-minutes`. `/pm-agenda` también corrió hoy y no la vuelvo a proponer. El próximo comité es el 2026-10-29 («dos semanas», según las notas). La configuración dice que el comité es semanal. Si pasó a quincenal, la configuración está desactualizada; las notas no lo dicen. El informe toca el 2026-10-28.

### Tu ficha publicada
No está vieja: se publicó hoy. Pero desde este barrido hay 4 vencidos y 2 reprogramados más que la ficha publicada no lleva. Publicarla de nuevo con `/pm-publish` es decisión tuya, no lo hago solo.

### Aparte
- El informe del 2026-10-13 declara Rojo con 91 % de avance, pero tiene ejecutado el 20,6 % del presupuesto. La proyección al cierre es 3,5 % mayor que lo aprobado. No sé cuál de las dos cifras de avance es la correcta; el estado lo declaras tú.
- El riesgo de que el proveedor no llegue con el equipo completo sigue sin registrar.
- El 25 de octubre, fecha de la revisión con el proveedor, es domingo.

**Vuelvo el 2026-10-16.**

Para que corra sin nadie delante en Claude Code, programa en el cron del sistema `claude -p "/criterio-project:pm-wake"`. La sesión necesita poder correr los scripts sin aprobar cada paso, y la carpeta del proyecto tiene que estar montada cuando dispare el reloj. No probé esa línea de comando. Si la organización no quiere corridas desatendidas, también sirve a mano cada lunes en la mañana.

La salida quedó en `estado/…/corridas/salida-pm-wake.md` y la corrida en `2026-10-15-pm-wake-1`. Antes de modificar la ficha de estado dejé una copia (`records/PRY-203.json.bak-antes-barrido`).