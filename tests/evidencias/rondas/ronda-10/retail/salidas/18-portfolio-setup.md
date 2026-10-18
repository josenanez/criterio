# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Retail

**Miré:** 83 documentos en 13 proyectos (PRY-199 a PRY-211). Formatos: 42 .md, 15 .pdf, 10 .docx, 7 .csv, 7 .xlsx, 1 .json y 1 .txt. El más reciente es del 2026-10-18.
**Eres:** PMO del portafolio, porque hay 13 proyectos.
**Te aviso:** dos días antes del comité semanal. El próximo comité es el 2026-10-25 y el informe sale el 2026-10-23. La fecha del comité la supuse por el ritmo semanal de las actas, así que corrígela si no es esa.
**En:** presentación.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.5.0 (términos 1.1) el 2026-10-18. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.5.0-2026-10-18.md` y `.pdf`. SHA-256 del .md: 9c54c0c51760b1…

En esta sesión de prueba nadie respondió preguntas, así que tomé las respuestas sugeridas. Quedó así:
- Rol PMO.
- Comité semanal.
- Presentación.
- Estado en `estado/`.
- Informes en `reportes/`.

### Probé con tres proyectos

Elegí PRY-209, PRY-210 y PRY-211. Varios proyectos empatan en documentación del 2026-10-18 y me quedé con estos tres.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-209 Migración del ERP | 4 | Patrocinador Felipe Arango y gerente Elena Duarte. Presupuesto 3.300 M COP y cierre 2027-10-11. Reporta verde con 61 % (informe del 2026-09-28). | Producto, facultad del gerente, fase |
| PRY-210 Etiquetas electrónicas de precio | 6 | Patrocinador Javier Hoyos y gerente Óscar Ramírez. Presupuesto 4.200 M COP y cierre 2027-03-14. Reporta verde con 79 % (informe del 2026-10-15). Tiene 2 hitos cerrados con acta de recibo. | Producto, facultad del gerente, fase |
| PRY-211 Pronóstico de demanda | 5 | Patrocinadora Sandra Gil y gerente Gustavo Neira. Presupuesto 9.500 M COP y cierre 2027-03-13. Reporta amarillo con 77 % (informe del 2026-09-27). | Producto, facultad del gerente, fase |

### Hallazgos

Son las cinco señales que levantó `compute`.

- **PRY-209, verde que los documentos no sostienen:** declara 61 %, pero solo 1 de 4 hitos está cumplido. El plan sostiene entre 25 % y 50 %.
- **PRY-211, avance sobre el plan:** declara 77 %. Con 2 de 5 hitos cumplidos, el plan sostiene entre 40 % y 60 %.
- **PRY-211, hito cerrado sin acta:** "Diseño de la experiencia aprobado" figura cerrado desde el 2026-07-09, hace 101 días, y no hay acta de recibo que lo pruebe.
- **PRY-211, compromiso vencido:** María Restrepo debía "Entregar el punto 5" el 2026-10-16. Lleva 2 días vencido.
- **PRY-210, sin señales:** el informe menciona una prueba de carga que no alcanzó el umbral y la rotación de un desarrollador. Quedaron en la ficha como incidencias, pero `compute` no las levantó como señal, así que no las presento como hallazgo.

No hay desviación de fechas ni de costo en ninguno de los tres.

### El portafolio completo

Faltan 10 proyectos (PRY-199 a PRY-208, 68 documentos), en un solo lote, uno tras otro. Esta primera pasada de tres proyectos tomó 51 segundos según el registro de la corrida. Eso sirve de referencia, pero no calculé un tiempo para el barrido completo.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea el trabajo.
- Ninguna de las tres actas dice qué producto sirve el proyecto ni hasta dónde puede decidir el gerente sin subir a comité.
- Alcance, "fuera de alcance" y dependencias son texto genérico ("Componente 1", "Lo que otro proyecto cubre", "Ninguna declarada"). Así no se puede contrastar el alcance real.
- PRY-211 tiene un hito cerrado sin acta de recibo.
- Dos compromisos de comité nombran a alguien que no asistió: María Restrepo en PRY-211 y Jorge Medina en PRY-210.
- PRY-209 no tiene actas de comité.
- Los informes de avance de PRY-209 y PRY-211 tienen 20 días o más.
- Estos tres proyectos no traen contratos de proveedor.

La corrida quedó registrada como `2026-10-18-portfolio-setup-1`, y lo que te mostré está en `estado/corridas/salida-portfolio-setup.md`. Si quieres, sigo con los otros 10 proyectos. Como eres PMO y tienes equipo, también puedo publicar el estándar en una carpeta compartida para que tus gerentes usen los mismos criterios.