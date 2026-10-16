# /criterio-portfolio:portfolio-report html

El informe HTML de portafolio está generado: 26 páginas en `/home/claude/banco/ronda-6/bancos/espacio/reportes`. Cubre 13 proyectos, 11 de ellos con hallazgos, 78 señales en total.

**Términos y fichas.** Los términos ya estaban aceptados por José Francisco Ñáñez el 2026-10-16 (v1.1), así que no volví a registrarlos. Cargué las 13 fichas de `estado/records/`, generadas hoy; la carpeta `estado/fichas/` que menciona el comando no existe.

**Vistas por audiencia.**
- `index.html` es la vista por campo, con la cadena de evidencia completa, para quien va a actuar.
- `decisiones.html` es la vista por decisión, para el patrocinador.
- Para sacar el PDF, imprima el HTML.

**Qué cambió.** Nada: la única instantánea previa es la de hoy, así que este es el punto de partida y no hay delta.

**Verdes contradichos por la evidencia (4).**
- **PRY-203 Open Banking:** proyección de costo 23,6 % sobre lo aprobado y línea base movida 33 días sin autorización.
- **PRY-204 Débito contactless:** declara 48 % cuando el plan soporta 75–100 %, con 119 días de atraso sin autorización.
- **PRY-207 Onboarding PyME:** declara 30 % cuando el plan soporta 50–75 %, con compromisos vencidos y reprogramados.
- **PRY-208 Motor de decisión:** tiene un compromiso vencido hace 15 días.

**Otros hallazgos.**
- **Proveedores facturados sin entrega:** PRY-200 y PRY-206.
- **Hito vencido:** PRY-202 tiene "Integración con el core" vencido hace 4 días.
- **Hitos declarados cumplidos sin evidencia:** hay 20 en total.

**Secciones vacías.** Contradicciones entre fuentes, proyectos en silencio, dependencias entre proyectos y cambios de gobierno salieron sin nada.

**Vacíos.** Ninguno de los 13 proyectos tiene autoridad ni fase identificadas. Cuatro proyectos no tienen producto asociado: PRY-202, PRY-205, PRY-208 y PRY-210.

**Confirmación del mes.** Dejé las cinco preguntas cerradas en el informe sin responder, porque nadie las puede contestar en esta sesión.

La corrida quedó registrada como `2026-10-16-portfolio-report-1` en `estado/corridas/`; tardó 40 segundos y no releyó ningún documento. El texto completo del informe está en `estado/corridas/salida-portfolio-report.md`, con el pie de versión y el enlace a los términos.

Si hay comité próximo (el 2026-10-23), puedo preparar el material de comité o entrar al detalle de los proyectos con hallazgos.