# /criterio-project:pm-setup documentos/proyectos/PRY-205-sistema-de-gestión-de-seguridad

## Listo — PRY-205 · Sistema de gestión de seguridad

**Lo que miré:** 5 documentos y 2 minutas. La última minuta es la del 2026-10-15. Pude leer todos los formatos. El cronograma (`10-plan/2025-08-11-cronograma-v1.xlsx`) existe, pero solo leí la última reunión, así que no lo leí y la ficha no trae hitos.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.8 el 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-project-0.3.8-2026-10-15.md` y `.pdf`. SHA-256: fd18d9cd0b3d5a0f…
**Configuración:** `config` la valida sin problemas.

**Respuestas por defecto (sin interfaz):**
- **Proyecto y gerente:** PRY-205 y Rubén Cárdenas, según el acta.
- **Reunión de seguimiento:** semanal, lunes. El comité del 12 de octubre fue lunes y la próxima la dejé para el 2026-10-19. Las notas del 15 dicen «próxima reunión en dos semanas», así que conviene confirmar la fecha.
- **Estado:** `estado/PRY-205-sistema-de-gestión-de-seguridad`.

### Lo que se prometió en tu última reunión (notas del 2026-10-15)
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Mauricio Pérez | Entregar el punto 4 | 2026-10-29 (antes 2026-10-12) | Abierto, reprogramado una vez. Cita: «no alcanzó, se compromete para el 29/10/2026» |
| Óscar Ramírez | Revisión con el proveedor | 2026-10-25 | Abierto. Cita: «queda para el 2026-10-25» |

Ninguno está vencido hoy. No hay acta de recibo que muestre que el punto 4 se entregó.

### Sin fecha
- **Laura Vélez** — mandar el ajuste del presupuesto. Cita: «la otra semana». No es una fecha, así que no puede estar vencido y por eso es el que se pierde. `compute` levantó una sola señal, `commitment_undated`, y es esta. Hay que preguntarle la fecha en la próxima reunión.

### Dicho en la reunión y no anotado
- «El proveedor podría no llegar con el equipo completo para la siguiente fase.» Lo dejé en la ficha como riesgo sin dueño, probabilidad ni impacto. El informe del 2026-10-11 (verde, 26%) lista otros dos riesgos y no este.

### Qué le falta a tu carpeta
- **Cronograma vigente:** solo hay la v1, de 2025-08-11, y está sin leer. Sin hitos no se puede contrastar el 26% declarado.
- **Minutas anteriores:** solo hay una en `30-reuniones/`, así que no puedo ver cuántas veces se reprogramó cada compromiso.
- **Actas de recibo:** no hay ninguna. Sin ellas un compromiso cumplido se ve igual que uno incumplido.
- **Acta de constitución:** no dice hasta dónde puede decidir el gerente sin subir a comité, ni la fase, y declara «Ninguna» como dependencia.
- **Notas del 15:** quedaron sueltas en la raíz del proyecto, fuera de `30-reuniones/`.

**Cuándo vuelvo:** el lunes 2026-10-19, según la reunión semanal. Puedo leer ahora las minutas anteriores y el cronograma para completar el historial de compromisos.

La corrida quedó registrada como `2026-10-15-pm-setup-1`. La salida completa está en `estado/PRY-205-sistema-de-gestión-de-seguridad/corridas/salida-pm-setup.md` y la ficha en `estado/PRY-205-sistema-de-gestión-de-seguridad/records/PRY-205.json`. No hice preguntas, por ser una sesión sin interfaz. Dos cosas se apartan del flujo:
- Escribí `config.json` a mano, porque el script no tiene un comando que lo genere.
- No incluí los hashes de los documentos en `documents_seen`.