# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de minería

**Miré:** 74 documentos en 13 proyectos (PRY-199 a PRY-211). Formatos: md 30, docx 14, pdf 14, csv 7, xlsx 7, json 1, txt 1. El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio, porque hay 13 proyectos.
**Te aviso:** dos días antes de cada comité, con comité semanal. No hay fecha del próximo, porque no la dieron.
**En:** presentación.
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-15, para la versión 0.3.8 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.8-2026-10-15.md` y `.pdf`. SHA-256: 906ca52cb3296d17…

La configuración quedó en `.criterio/portafolio/config.json` y pasó la verificación. Lo que voy encontrando va en `estado/` y los informes irán en `reportes/`. Ya existía `estado/PRY-205-…/` con trabajo del gerente de ese proyecto, y no lo toqué.

### Probé con tres proyectos
Tomé PRY-201, PRY-204 y PRY-205, los tres con documentos del 2026-10-15.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-201 Ampliación de la relavera | 5 | Declara verde y 41 %. Proyección de 839,6 M COP, un 5,0 % sobre los 800 M aprobados. 1 de 4 hitos cumplido, con acta de recibo. | Producto, facultad del gerente, fase |
| PRY-204 Monitoreo de taludes | 4 | Declara verde y 30 %. Proyección de 2.505,7 M COP, un 4,4 % sobre los 2.400 M aprobados. 2 de 3 hitos declarados cerrados. Producto: «alerta de taludes». | Facultad del gerente, fase |
| PRY-205 Sistema de gestión de seguridad | 6 | Declara verde y 26 %. Proyección de 9.244,1 M COP, dentro de los 9.500 M aprobados. Tiene una ficha publicada por su gerente, que guardé aparte sin mezclarla con la mía. | Producto, facultad del gerente, fase |

### Hallazgos
El cálculo levantó 13 señales, y los tres proyectos declaran verde pese a tener señales.

- **Hitos cerrados sin acta (PRY-204 y PRY-205):**
  - PRY-204: Ingeniería básica (2026-02-09) e Ingeniería de detalle (2026-07-11).
  - PRY-205: Ingeniería básica (2026-01-15) e Ingeniería de detalle (2026-06-11).
  - Ningún documento prueba el cierre de esos cuatro hitos.
- **Avance declarado muy por debajo del plan (PRY-204 y PRY-205):**
  - PRY-204 declara 30 % y su cronograma sostiene entre 67 % y 100 %.
  - PRY-205 declara 26 % contra la misma banda.
  - Esas cifras no pueden ser ciertas a la vez.
- **Compromisos vencidos:**
  - PRY-201: Liliana Torres, «punto 15», para el 2026-10-03, con 12 días de atraso.
  - PRY-204: Óscar Ramírez, «punto 40», para el 2026-10-14, con 1 día.
- **Compromiso sin fecha (PRY-205):** Laura Vélez, «ajuste del presupuesto», «la otra semana».
- **Diferencia con la ficha del gerente (PRY-205):** la fecha de cierre es 2027-01-19 en el acta y 2026-11-06 en el cronograma. No decido quién tiene razón, y esa fecha del cronograma es la de su último hito, que puede no ser el cierre del proyecto.
- **Riesgo sin registrar (PRY-205):** en la reunión del 2026-10-15 se comentó que el proveedor podría no llegar con el equipo completo y nadie lo anotó. Lo dejé en la ficha sin dueño.
- **Datos sin confirmar:** en PRY-204 y PRY-205 el patrocinador, el presupuesto y el alcance salen de actas de hace 14 meses sin confirmación posterior.

### El portafolio completo
Faltan 10 proyectos (PRY-199, 200, 202, 203 y 206 a 211), en dos lotes uno tras otro. Estimo entre 25 y 35 minutos. Es una estimación, no una medición.

### Lo que le falta a tu carpeta
- Actas de recibo de los hitos que los cronogramas dan por cerrados.
- La facultad del gerente: no aparece en ningún proyecto de los tres.
- Una confirmación posterior a las actas de 2025.
- Orden en PRY-205, que tiene `ficha-pm.json` y unas notas de reunión fuera de las carpetas habituales.
- PRY-206, que solo tiene acta de constitución e informe, sin cronograma ni reuniones.
- Una fecha del próximo comité, para dejar armado el aviso de dos días antes.

Ninguno bloquea nada.

La corrida quedó registrada como `2026-10-15-portfolio-setup-1`. Hice 0 preguntas, porque nadie podía responder y tomé las respuestas sugeridas. Tardé unos 5 minutos hasta el primer resultado, medido a ojo. Lo que te mostré está entero en `estado/corridas/salida-portfolio-setup.md`.

Si quieres, corro el portafolio completo ahora.