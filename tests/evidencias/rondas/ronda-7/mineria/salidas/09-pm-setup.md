# /criterio-project:pm-setup documentos/proyectos/PRY-202-planta-de-tratamiento-de-agua

## Listo — PRY-202 · Planta de tratamiento de agua

**Lo que miré:** 19 documentos, todos legibles. Entre ellos están 6 minutas del comité semanal (2026-09-05 al 2026-10-10), las notas del 2026-10-17 y 5 actas de recibo. Leí las reuniones de la más vieja a la más nueva.
**Términos:** aceptados por José Francisco Ñáñez para la versión 0.3.13 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-project-0.3.13-2026-10-17.md` y `.pdf`. SHA-256: b8d0cca7fea66fcb…
**Las cuatro preguntas** (tomé la respuesta sugerida en cada una):
- Proyecto PRY-202, gerente Jorge Medina, patrocinadora Laura Vélez.
- Reunión semanal los sábados. Las notas del 17 dicen que la próxima es en dos semanas, o sea el 2026-10-31.
- El estado queda en `estado/PRY-202-planta-de-tratamiento-de-agua`.
- Términos aceptados con el nombre indicado.

### Compromisos

Hay 26 compromisos. De ellos, 5 están cumplidos con acta de recibo, 5 vencidos sin evidencia, 14 abiertos con fecha y 2 sin fecha.

**Movidos 3 veces o más** (el bloqueo que nadie ha nombrado):

| Quién | Qué | Original → vigente | Veces |
|---|---|---|---|
| Javier Hoyos | Enviar el documento 1 | 2026-09-08 → 2026-12-08 | 6 |
| Gustavo Neira | Cerrar la prueba 2 | 2026-09-12 → 2026-11-30 | 5 |
| Camilo Beltrán | Validar el ambiente 4 | 2026-09-23 → 2026-12-05 | 5 |

Las notas del 17 dicen «08/12/2026» para el documento 1. Lo leí como día/mes; confírmalo.

**Vencidos sin evidencia:**

| Quién | Qué | Venció | Días |
|---|---|---|---|
| Laura Vélez | Revisar el anexo 11 | 2026-09-23 | 24 |
| Andrés Lozano | Entregar el punto 8 | 2026-10-04 | 13 |
| Gustavo Neira | Actualizar la matriz 6 | 2026-10-11 | 6 |
| Rubén Cárdenas | Actualizar la matriz 14 | 2026-10-12 | 5 |
| Felipe Arango | Enviar el documento 9 | 2026-10-15 | 2 |

Tres de estos (anexo 11, punto 8 y matriz 6) desaparecieron de las listas después de que alguien dijo «ya lo entregué». Las minutas anotan que no se presentó acta, y decirlo en la reunión no los cierra.

**Sin fecha** (no pueden estar vencidos): Laura Vélez, «Aprobar el diseño 21» y «Mandar el ajuste del presupuesto» («la otra semana»).

La tabla completa de los 14 abiertos con fecha y los 5 cumplidos está en `estado/PRY-202-planta-de-tratamiento-de-agua/corridas/salida-pm-setup.md`.

### Contra lo que declara el informe

El informe dice verde y 89%, pero el cálculo no lo sostiene:
- **Avance:** el cronograma tiene 2 de 5 hitos cerrados, así que el plan sostiene entre 40% y 60%. Son 29 puntos menos de lo declarado.
- **Tiempo:** el cierre pasó de 2027-05-28 a 2027-09-20, 115 días (25.8%) por la solicitud de cambio CC-01.
- **Costo:** la proyección es 1.030.910.468 COP contra 800.000.000 aprobados, 28.9% más. Todas las cifras del informe son declaradas.
- **Hitos sin acta:** Ingeniería básica e Ingeniería de detalle figuran cerrados, sin acta que lo pruebe.
- **Proveedor (CT-812):**
  - El licenciamiento venció el 2026-06-15 y sigue pendiente, 124 días.
  - La bolsa de horas figura como recibida, sin acta de recibo.
- **Riesgo no registrado:** en las notas del 17 se comentó que el proveedor podría no llegar con el equipo completo, y nadie lo anotó como riesgo. Lo dejé en la ficha con esa cita.

### Qué le falta a tu carpeta
- No hay minutas anteriores al 2026-09-05.
- Faltan actas de recibo para el anexo 11, el punto 8 y la matriz 6, para los dos hitos «cerrados» y para la bolsa de horas.
- No hay registro de la autorización de CC-01. La solicitud dice «autorizada por el comité», pero la minuta del 10-10 no la menciona.
- Las notas del 17 son un `.txt` suelto fuera de `30-reuniones/`.
- El acta de constitución no declara dependencias, producto ni qué puede decidir el gerente sin subir a comité.
- Jorge Medina firmó las 5 actas de recibo, incluida la de su propio compromiso (confirmar la fecha 15).

La ficha quedó escrita en `estado/PRY-202-planta-de-tratamiento-de-agua/records/PRY-202.json` y sin sellar, como pide el comando. `compute` no devolvió `record_issues` y `config` salió válida. La corrida quedó registrada como `2026-10-17-pm-setup-1`.

**Cuándo vuelvo:** el sábado 2026-10-31, la próxima reunión.