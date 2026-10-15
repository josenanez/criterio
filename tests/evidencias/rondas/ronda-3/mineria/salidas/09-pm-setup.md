# /criterio-project:pm-setup documentos/proyectos/PRY-203-despacho-automático-de-flota

## Listo — Despacho automático de flota (PRY-203)

La instalación quedó hecha. Leí la reunión de hoy y saqué tres compromisos. Ninguno está vencido a 2026-10-15.

**Lo que miré:** 18 documentos y 7 minutas o notas de reunión. La más reciente es la del 2026-10-15. Nada quedó ilegible, pero aún no abrí el cronograma (.xlsx) ni los dos PDF.

**Términos:** José Francisco Ñáñez aceptó la versión 0.3.9 el 2026-10-15. Tomé como sí explícito la aceptación escrita en tu invocación. El comprobante está en `.criterio/terminos/aceptacion-criterio-project-0.3.9-2026-10-15.md` y `.pdf`. El SHA-256 empieza por `0d907bfa1ce7cb70…`.

**Respuestas por defecto** (nadie respondió, no hice ninguna pregunta):
- **Proyecto y gerente:** Camilo Beltrán, gerente de PRY-203, según el acta de constitución.
- **Reunión de seguimiento:** el comité semanal de los jueves. Las notas de hoy dicen «próxima reunión en dos semanas», así que anoté el 2026-10-29.
- **Dónde guardo el estado:** `estado/PRY-203-despacho-automático-de-flota`.

### Lo que se prometió en tu última reunión (2026-10-15)

| Quién | Qué | Para cuándo | Cita |
|---|---|---|---|
| Óscar Ramírez | Enviar el documento 1 | 2026-11-24 | Reprogramado. El comité del 2026-10-08 lo tenía para 2026-11-10: «no alcanzó, se compromete para el 24/11/2026». |
| Óscar Ramírez | Revisión con el proveedor | 2026-10-25 | «queda para el 2026-10-25». |
| Laura Vélez | Mandar el ajuste del presupuesto | sin fecha | «la otra semana». |

### Sin fecha
El de Laura Vélez no tiene fecha, porque «la otra semana» no lo es. No puede estar vencido, y por eso es el que desaparece de los informes. El cálculo lo marcó como `commitment_undated`. Conviene pedirle una fecha en la próxima reunión.

### Otros hallazgos
- Se dijo que el proveedor podría no llegar con el equipo completo para la siguiente fase, y las notas aclaran que nadie lo anotó como riesgo. Lo dejé en la ficha sin dueño ni probabilidad, porque nadie los dijo.
- «Enviar el documento 1» se movió una vez entre las dos reuniones que leí. Eso no llega al umbral de alerta, que son 3 reprogramaciones.

### Qué le falta a tu carpeta
- **Actas de recibo:** el 2026-10-08, Javier Hoyos, Camilo Beltrán y Diana Molina dijeron haber entregado tres cosas y no se presentó acta. Sin acta, un compromiso cumplido se ve igual que uno incumplido.
- **Autoridad del gerente:** el acta de constitución no dice hasta qué monto ni qué cambio de alcance puede decidir sin comité.
- **Línea base:** el cálculo no encontró una.
- **Datos viejos:** patrocinador, gerente, presupuesto (9.500.000.000 COP) y cierre (2027-02-21) salen del acta de hace 13 meses, sin confirmación posterior.
- **Documentos sin leer:** las otras cinco minutas, el cronograma, el informe de avance del 2026-10-13 y las actas de recibo de seguimiento.

**La ficha** está en `estado/PRY-203-despacho-automático-de-flota/records/PRY-203.json`, sin sellar. Leí una reunión y el acta, no el proyecto entero.

**Cuándo vuelvo:** el jueves 2026-10-29.

**Para seguir:** puedo leer las minutas anteriores y armar el historial completo de compromisos. Ahí es donde aparece el que se reprogramó tres veces.

La salida quedó en `estado/PRY-203-despacho-automático-de-flota/corridas/salida-pm-setup.md` y la corrida está registrada como `2026-10-15-pm-setup-1`. El tiempo hasta el primer resultado no se midió, porque este comando no usa `corrida-inicio`.