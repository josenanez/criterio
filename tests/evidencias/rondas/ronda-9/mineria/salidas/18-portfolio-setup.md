# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

La instalación quedó lista y probé con tres proyectos. No hice ninguna pregunta: en todas tomé el valor sugerido, como pediste.

- **Miré:** 76 documentos en 13 carpetas. Formatos: .md 37, .docx 11, .pdf 11, .xlsx 9, .csv 6, .json 1, .txt 1. El más reciente es del 2026-10-17.
- **Eres:** PMO del portafolio, porque hay varios proyectos.
- **Te aviso:** dos días antes del comité. Los comités que vi son semanales, así que supuse el 2026-10-23 como primera fecha. Dime la fecha real y la cambio.
- **En:** presentación, el valor por defecto. La configuración lo guarda como `html`.
- **Términos:** aceptados por José Francisco Ñáñez el 2026-10-17, con tu mensaje de la prueba como sí explícito.
  - Corresponden a la versión 0.4.0 (términos 1.1).
  - El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.4.0-2026-10-17.md` y `.pdf`.
  - SHA-256: 96015115a67f6c94…
- **Dónde queda:** la configuración en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`. Ya existía `estado/PRY-211-…` del agente de proyecto; no la toqué.

### Probé con tres proyectos

Tomé los de documentación más reciente: PRY-200, PRY-210 y PRY-211. Cada ficha quedó escrita y sellada, y `compute` levantó 26 señales. Los 3 proyectos tienen alertas y 2 de los 3 reportan verde contra evidencia que no lo sostiene.

| Proyecto | Qué supe | Qué no está |
|---|---|---|
| **PRY-200** Mantenimiento predictivo de camiones (5 documentos) | Gustavo Neira es patrocinador y gerente a la vez. Presupuesto de 2.400 M COP, proyección de 2.647,9 M. Declara verde con 66 %. | Facultad del gerente y etapa |
| **PRY-210** Programa de relacionamiento comunitario (3 documentos) | Diana Molina es patrocinadora y Felipe Arango gerente. Presupuesto de 1.200 M COP, proyección de 1.214,3 M. Declara verde con 45 %. | Producto, facultad y etapa |
| **PRY-211** Control de polvo en vías (28 documentos) | Liliana Torres es gerente. Declara amarillo con 82 %. El fin vigente es 2026-11-28 tras CC-01 (+103 días). Su `ficha-pm.json` quedó aparte, en `pm_record`. | Producto, facultad y etapa |

### Hallazgos (todos los levantó `compute`)

- **PRY-200:**
  - Declara verde con 66 %, pero el cronograma solo sustenta entre 25 % y 50 % (1 hito cerrado de 4).
  - La proyección supera lo aprobado en 10,3 %.
- **PRY-210:**
  - Declara verde con un hito vencido: Ingeniería de detalle aprobada, desde el 2026-10-13.
  - Otro hito figura cerrado sin acta: Ingeniería básica aprobada, prevista para el 2026-08-07.
- **PRY-211:**
  - **Plazo:** +103 días, 23 % sobre la línea base original.
  - **Hitos:** 4 cerrados sin acta, el más antiguo desde hace 420 días.
  - **Compromisos:**
    - 5 vencidos y 2 sin fecha.
    - «Enviar el documento 1» se ha reprogramado 6 veces.
  - **Proveedor CT-110:** 2 entregables atrasados (386 y 263 días) y la calibración de sensores aceptada sin acta.
  - **Ficha del gerente vs. la mía:** difieren solo en el producto. Él pone «No aplica» y yo lo dejé vacío, porque el acta dice que no sirve a uno.

### El portafolio completo

Faltan 10 proyectos y 73 documentos, leídos uno tras otro en dos lotes. Mi estimación, sin medir, es del orden de media hora.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea nada.

- Ninguna acta dice hasta dónde puede decidir el gerente sin subir a comité.
- Hay hitos cerrados sin acta de recibo en PRY-210 y PRY-211.
- Ningún riesgo leído tiene responsable.
- En PRY-200 el comité lista dos veces el mismo asistente. Los compromisos son de Beatriz Cuéllar y Paula Céspedes, que no figuran como asistentes.

Lo que le mostré a la persona quedó entero en `estado/corridas/salida-portfolio-setup.md`, y la corrida quedó registrada con id `2026-10-17-portfolio-setup-1`. ¿Corro el portafolio completo? Publicar un estándar para gerentes de proyecto no aplica todavía, porque no hay carpeta compartida.