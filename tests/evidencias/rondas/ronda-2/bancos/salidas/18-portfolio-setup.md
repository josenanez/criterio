# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

**Miré:** 75 documentos en 13 proyectos. Formatos: .md (36), .xlsx (11), .docx (10), .pdf (10), .csv (6), .json (1), .txt (1). El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio.
**Te aviso:** dos días antes del comité. Los comités son semanales y supuse que el próximo es el 2026-10-22; ese dato no está en tus documentos.
**En:** presentación.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.8 (términos 1.1), con fecha 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.8-2026-10-15.md` y en el `.pdf` del mismo nombre. SHA-256: 906ca52cb3296d17…

Como no hubo interfaz, en cada pregunta tomé la respuesta sugerida. Eso incluye dejar el estado en `estado/` y los informes en `reportes/`.

### Probé con tres proyectos

Los de documentación más reciente: PRY-204, PRY-206 y PRY-202.

| Proyecto | Docs | Qué supe | Qué no está |
|---|---|---|---|
| PRY-204 Débito contactless | 4 | Declara **rojo**, 58 %. Aprobado 800 M COP, proyección 1.020,7 M. | Autoridad del gerente, fase. |
| PRY-206 Billetera y QR | 14 | Declara **rojo**, 31 %. Aprobado 6.800 M, proyección 7.686 M. Tiene dos contratos de proveedor y su `ficha-pm.json`. | Autoridad, fase. La ficha del gerente no trae estado ni avance. |
| PRY-202 Migración a la nube | 6 | Declara **verde**, 82 %. Aprobado 18.000 M, proyección 17.240 M. CC-01 sumó 42 días y 84 M. | Producto ("No aplica"), autoridad, fase. |

### Hallazgos

`compute` levantó 19 señales:

- **PRY-202, verde contradicho.** Sus dos hitos cerrados no tienen acta de recibo. Su atraso contra la línea base original es de 42 días, por CC-01.
- **PRY-204.**
  - Dos hitos cerrados sin acta.
  - La proyección supera el aprobado en 27,6 %.
  - Un compromiso de Jorge Medina no tiene fecha.
- **PRY-206, 12 señales.**
  - Declara 31 % de avance y su cronograma tiene 5 de 5 hitos cerrados; tres de ellos sin acta.
  - La proyección supera el aprobado en 13 %.
  - Redes del Norte facturó 1.317,8 M contra 920,1 M aceptados, una diferencia de 397,8 M.
  - Dos entregables de CT-725 figuran como recibidos sin acta.
  - Dos entregables van atrasados: el tarifario de CT-279 (103 días) y la bolsa de horas de CT-725 (232 días).
  - El fin del proyecto es el 2026-09-25 según el cronograma y el 2026-11-11 según el acta.

También anoté un riesgo dicho en reunión que nadie registró: el proveedor podría no llegar con el equipo completo. Es lectura mía de las notas del 2026-10-15, no una señal de `compute`.

### El portafolio completo

Faltan 10 proyectos y 51 documentos. Estimo unos 30 a 40 minutos, un proyecto tras otro. La corrida de hoy tardó 95 segundos y no medí el tiempo hasta el primer resultado.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea nada.
- Ningún proyecto declara la autoridad del gerente (3 de 3), ni la fase.
- 7 de los 9 hitos cerrados que leí no tienen acta de recibo.
- Los compromisos de comité llegan con "por definir" o "la otra semana".
- Las actas de constitución traen alcance genérico y "Ninguna declarada" en dependencias.
- PRY-205 no tiene cronograma ni reuniones, y PRY-211 no tiene cronograma.

La corrida quedó registrada como `2026-10-15-portfolio-setup-1`, con la salida completa en `estado/corridas/salida-portfolio-setup.md`. ¿Corro el portafolio completo?