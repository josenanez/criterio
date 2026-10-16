# /criterio-portfolio:portfolio-setup documentos/proyectos

**Listo: Vera quedó instalada sobre tus documentos en `documentos/proyectos` y probé con tres proyectos.** Nadie respondió preguntas, así que tomé las respuestas sugeridas y las dejé dichas.

**Lo que encontré**
- **Carpeta:** 89 documentos en 13 proyectos. Hay .md, .pdf, .docx, .xlsx, .csv, un .json y un .txt. El más reciente es del 2026-10-15.
- **Rol y cadencia:** PMO, porque hay 13 proyectos. Comité cada dos semanas, con el próximo el 2026-10-22. Esa fecha es un valor sugerido, no un dato tuyo.
- **Formato del informe:** página (HTML).
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez, versión 0.3.10, con comprobante en `.criterio/terminos/` (.md y .pdf). La verificación de la configuración salió `ok: true` sin problemas.
- **Dónde quedó cada cosa:**
  - Configuración: `.criterio/portafolio/config.json`.
  - Lo que Vera va encontrando: `estado/`.
  - Informes: `reportes/`.

**Los tres proyectos de prueba** fueron PRY-207, PRY-210 y PRY-211, los de documentación más reciente. Escribí y sellé una ficha por proyecto, y `compute` levantó 25 señales:
- **PRY-207, Onboarding PyME:**
  - Declara amarillo y 40 %.
  - Sus tres hitos figuran cerrados, y ninguno tiene acta de recibo.
- **PRY-210, Portal de proveedores:**
  - Declara verde y 34 %. Contra eso hay 5 compromisos vencidos, 4 reprogramados y 2 sin fecha.
  - La salida a producción se movió 41 días (del 2027-03-01 al 2027-04-11) con CC-01 todavía pendiente.
  - La fecha de cierre difiere entre la ficha del gerente (2027-04-24) y el cronograma v2 (2027-04-11).
  - Guardé la ficha del gerente aparte, sin fusionarla con la mía.
- **PRY-211, Cobranza digital:**
  - Declara verde y 34 %.
  - Sus cuatro hitos figuran cerrados, y dos de ellos no tienen acta de recibo.

El informe de PRY-210 no es el único documento que cuenta algo que nadie registró. Las notas del 2026-10-15 mencionan que el proveedor podría no llegar con el equipo completo, y nadie lo anotó como riesgo.

**Para el portafolio completo** faltan 10 proyectos y 49 documentos, en un solo lote de diez proyectos, uno tras otro. Mi estimado es unas tres veces lo que tomó esta prueba; la prueba tomó 104 segundos.

**Qué le falta a tu carpeta** (ninguno bloquea):
- PRY-203 solo tiene dos documentos, sin cronograma ni minutas.
- PRY-211 no tiene minutas de comité.
- Ninguna acta de constitución dice hasta qué monto decide el gerente sin subir a comité.

La salida completa quedó en `estado/corridas/salida-portfolio-setup.md`, y la corrida quedó registrada como `2026-10-15-portfolio-setup-1`. Si quieres, el siguiente paso es correr el portafolio completo.