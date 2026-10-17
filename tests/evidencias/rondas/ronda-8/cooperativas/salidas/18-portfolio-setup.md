# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa

**Miré:** 76 documentos en 13 proyectos. Los formatos son .md (36), .pdf (14), .docx (11), .xlsx (8), .csv (5), .json (1) y .txt (1). El más reciente es del 2026-10-17.
**Eres:** PMO del portafolio, porque hay varios proyectos.
**Te aviso:** dos días antes del comité semanal. Nadie dio fecha, así que supuse que el primero es el 2026-10-24. Los documentos muestran comités semanales.
**En:** presentación, que es el valor sugerido.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-17 para la versión 0.3.13 (términos 1.1).
- El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`.
- El SHA-256 del Markdown empieza por 6d4b67767ea3a1ea….

No hubo preguntas: en esta sesión sin interfaz tomé el valor sugerido para cada una. La verificación de la configuración pasó sin problemas.

### Probé con tres proyectos

Elegí PRY-202, PRY-209 y PRY-211, que tienen documentos del 15 al 17 de octubre. PRY-200 empata en fecha y quedó fuera.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-202 Core cooperativo | 4 | Gerente Natalia Ospina. Cierre pactado 2026-05-16. Declara verde y 65 %. | Producto, autoridad, fase y actas de recibo |
| PRY-209 Convenios de libranza | 7 | Gerente Felipe Arango. Cierre 2027-04-10. Declara amarillo y 27 %. | Producto, autoridad, fase y actas de los hitos cerrados |
| PRY-211 Cobranza digital | 8 | Gerente Camilo Beltrán. Cierre pactado 2026-10-14. Declara rojo y 77 %. | Autoridad, fase y actas de recibo de los entregables del proveedor |

### Qué levantó el cálculo

`compute` levantó 19 señales en los tres proyectos.

- **PRY-202 declara verde y los documentos no lo sostienen.**
  - Sus cuatro hitos figuran cerrados y ninguno tiene acta de recibo.
  - Declara 65 %, pero el cronograma da por cumplido el 100 %.
  - Hay dos compromisos vencidos, uno de 24 días y otro de 2.
  - Sus datos de gobierno vienen del acta de 2025-08-20, sin confirmación posterior.
- **PRY-209:**
  - Dos hitos cerrados no tienen acta.
  - Declara 27 %, y el cronograma sostiene entre 40 y 60 %.
  - Un compromiso lleva 7 días vencido.
- **PRY-211: el rojo es honesto y lo grave está en el proveedor.**
  - Datos para Cooperativas facturó 376.332.909 COP el 2026-08-29, y ningún entregable del contrato CT-650 tiene acta de recibo.
  - Esos dos entregables van con 160 y 69 días de atraso.
  - La salida a producción, pactada para el 2026-10-14, no se cumplió.
  - Dos hitos cerrados no tienen acta y hay un compromiso vencido.

### El portafolio completo

Faltan 10 proyectos (PRY-199, 200, 201, 203 a 208 y 210) y 57 documentos. Con lo que vi, tomaría unos 30 a 40 minutos, en dos lotes. Es una estimación mía, no una medición.

### Lo que le falta a tu carpeta

- Los hitos cerrados casi nunca traen su acta de recibo. Es la brecha que más se repite.
- Ninguna de las tres actas de constitución declara la autoridad del gerente ni la fase.
- PRY-200 publicó una `ficha-pm.json`. Vera la leerá aparte y la contrastará contra su propia lectura.
- Hay un archivo de notas suelto, `PRY-200/2026-10-17-notas-reunion.txt`, fuera de las carpetas numeradas.

Nada de esto bloquea el análisis.

La salida completa quedó en `estado/corridas/salida-portfolio-setup.md`, y la corrida se registró como `2026-10-17-portfolio-setup-1`. La lectura de las tres fichas y el cálculo tomaron 87 segundos.

¿Corro el portafolio completo? Si tienes equipo, también puedo publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios.