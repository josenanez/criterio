# /criterio-project:pm-setup documentos/proyectos/PRY-201-programa-de-fidelización

Soy Samuel. Terminé la instalación de PRY-201: la configuración quedó válida y la corrida registrada. Leí solo la reunión más reciente, así que la ficha no está sellada.

## Listo — PRY-201 · Programa de fidelización

**Lo que miré:** 27 documentos, 7 de ellos minutas, la última del 2026-10-15. No hay formatos que no pueda leer.

**Términos:** aceptados por José Francisco Ñáñez para la versión 0.3.9, con fecha 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-project-0.3.9-2026-10-15.md` y `.pdf`, con SHA-256 `0d907bfa1ce70…`.

Nadie contestó las preguntas, así que tomé las respuestas sugeridas:
- **Proyecto:** PRY-201, con Diana Molina como gerente, según el acta de constitución.
- **Reunión:** los jueves, semanal, que es el patrón de los nombres de las minutas. Las notas del 15 dicen «próxima reunión en dos semanas», pero dejé la próxima en el 2026-10-22. Dime si es el 29.
- **Estado:** `estado/PRY-201-programa-de-fidelización`.

### Lo que se prometió en tu última reunión (notas del 2026-10-15)
| Quién | Qué | Para cuándo | |
|---|---|---|---|
| Paula Céspedes | Enviar el documento 1 | 2026-12-17 | Reprogramado una vez. El 2026-10-08 se había prometido para el 2026-12-03. Cita: «lo de "enviar el documento 1" no alcanzó, se compromete para el 17/12/2026». |
| Óscar Ramírez | Revisión con el proveedor | 2026-10-25 | Vigente. Cita: «revisión con el proveedor, queda para el 2026-10-25». |
| Laura Vélez | Mandar el ajuste del presupuesto | sin fecha | Ver abajo. |

Ninguno está vencido sin evidencia.

### Sin fecha
Laura Vélez dijo «la otra semana», que no es una fecha, y no la calculé. Es la única señal que levantó `compute`. Un compromiso sin fecha no puede figurar como vencido, y por eso suele desaparecer de los informes.

### Algo que se dijo y nadie registró
Se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase, y las notas dicen que nadie lo anotó como riesgo. Lo dejé en la ficha como riesgo sin dueño, sin probabilidad y sin impacto. `compute` no levantó ninguna señal sobre esto.

### Para tu lectura
- La nueva fecha de Paula Céspedes (2026-12-17) es posterior al cierre del acta de constitución (2026-12-07). `compute` no levantó señal por eso.
- La fecha de Óscar Ramírez (2026-10-25) cae en domingo.
- El comité del 2026-10-08 trae otros compromisos abiertos que no cargué en la ficha. Tres tenían fecha anterior a hoy: Óscar Ramírez (aprobar el diseño 13, 2026-10-09), Javier Hoyos (cerrar la prueba 18, 2026-10-11) y Jorge Medina (actualizar la matriz 14, 2026-10-12). No sé si se cumplieron. Para saberlo hay que leer las actas de recibo contra cada uno.

### Qué le falta a tu carpeta
- **Estado declarado:** ningún documento leído trae el estado ni el avance que declaras. Eso lo declaras tú.
- **Facultad del gerente:** el acta no dice hasta qué monto o cambio de alcance decides sin subir a comité.
- **Línea base:** no hay cronograma con línea base en la ficha. El cronograma v1 está en `10-plan/` sin leer.
- **Datos viejos:** lo que sale del acta (patrocinador, gerente, presupuesto de 4.200.000.000 COP, cierre) tiene 17 meses sin confirmación posterior.
- **Presupuesto:** no leí contratos ni facturas, así que ejecutado, comprometido y proyección están vacíos.
- **Actas de recibo:** hay 13 en `20-seguimiento/` y no las leí. Sin ellas, un compromiso cumplido se ve igual que uno incumplido.
- **Etapa del proyecto:** ningún documento leído la declara.

**Cuándo vuelvo:** el jueves 2026-10-22, según la reunión semanal.

¿Leo las minutas anteriores (2026-09-03 al 2026-10-08) para armar el historial de compromisos? Ahí aparece el que se reprogramó más de una vez.

## Dónde quedó
- **Configuración:** `.criterio/proyecto/PRY-201/config.json`. La primera versión no traía la sección `report`, que el script exige. La añadí y ahora `config` devuelve `ok`.
- **Ficha:** `estado/PRY-201-programa-de-fidelización/records/PRY-201.json`.
- **Salida de esta corrida:** `estado/PRY-201-programa-de-fidelización/corridas/salida-pm-setup.md`. La corrida quedó registrada como `2026-10-15-pm-setup-1`.