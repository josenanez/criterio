# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Minería

**Miré:** 73 documentos en 13 proyectos (PRY-199 a PRY-211). Formatos: .md 42, .pdf 10, .docx 9, .csv 5, .xlsx 5, .json 1, .txt 1. El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio.
**Te aviso:** cada semana, dos días antes del comité. Los comités son semanales y no hay fecha del próximo.
**En:** presentación.
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-15 para la versión 0.3.10. El comprobante queda en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.10-2026-10-15.md` y `.pdf`. SHA-256 del Markdown: 5a63e87d0ce9d540…
**Preguntas:** no hice ninguna. En esta sesión sin interfaz tomé los valores sugeridos (rol, cadencia, formato, dónde guardar).

### Probé con tres proyectos

Cinco proyectos empatan con documentos del 2026-10-15 (PRY-200, 201, 203, 204 y 209). Tomé PRY-201, PRY-203 y PRY-204.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-201 Ampliación de la relavera | 5 | Sandra Gil (gerente), María Restrepo (patrocinadora), 2.400 M COP, cierre 2026-12-21. Declara verde y 50%. | Producto («No aplica»), facultad del gerente, etapa |
| PRY-203 Despacho automático de flota | 5 | Gustavo Neira (gerente), Felipe Arango (patrocinador), 1.200 M COP, cierre 2027-05-21. Declara verde y 41%. | Facultad del gerente, etapa |
| PRY-204 Monitoreo de taludes | 2 | Javier Hoyos (gerente), Gustavo Neira (patrocinador), 800 M COP, cierre 2026-01-16. Declara amarillo y 98%. | Cronograma e hitos, facultad del gerente, etapa |

### Hallazgos (los que levantó `compute`)

- **PRY-201, verde contradicho.**
  - Dos hitos figuran cerrados sin acta de recibo: ingeniería básica (plan 2026-06-29) e ingeniería de detalle (plan 2026-08-07).
  - El 50% declarado queda 10 puntos por debajo de lo que sostiene el plan, que es entre 60% y 80%.
- **PRY-203, verde contradicho.**
  - La ingeniería básica figura cerrada (plan 2026-03-13) sin acta.
  - El comité del 2026-10-15 dejó un compromiso sin fecha: Óscar Ramírez, «Entregar el punto 34».
- **PRY-204, sobrecosto proyectado de 13,9%.** La proyección al cierre es 910,8 M COP contra 800 M aprobados.

En total son 3 proyectos con señales, 8 señales y 2 verdes contradichos. Además, ninguna de las tres actas trae la facultad del gerente. En PRY-203 y PRY-204 los datos de identidad y presupuesto salen de actas de hace 12 y 17 meses, sin confirmación posterior.

### El portafolio completo

Faltan 10 proyectos (PRY-199, 200, 202, 205 a 211) y 66 documentos, en un lote de 10 proyectos y otro de 1, uno tras otro. PRY-200 es el más grande, con 24 documentos. Calculo de 30 a 40 minutos; es una estimación, no una medición.

### Lo que le falta a tu carpeta

- Actas de recibo para los hitos que el cronograma da por cerrados (PRY-201 y PRY-203).
- Cronograma en PRY-202, PRY-204 y PRY-208. PRY-204 tiene el cierre comprometido en 2026-01-16 y declara 98%.
- Fecha para los compromisos que salen de comité como «por definir».
- Facultad del gerente en las actas.
- Un archivo suelto: `PRY-200.../2026-10-15-notas-reunion.txt` está fuera de las subcarpetas de seguimiento y reuniones.

Ninguno bloquea nada. La salida completa quedó en `estado/corridas/salida-portfolio-setup.md` y la corrida, registrada con el id `2026-10-15-portfolio-setup-1`. ¿Corro el portafolio completo?