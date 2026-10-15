# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Retail (prueba)

Instalé el agente PMO y probé con tres proyectos. El cálculo dio 9 hallazgos y la corrida quedó registrada como `2026-10-15-portfolio-setup-1`. Nadie respondió preguntas: usé las respuestas sugeridas y los términos que indicaste.

**Qué miré:** 88 documentos en 13 proyectos. Los formatos son .md (50), .pdf (13), .docx (12), .xlsx (6), .csv (5), .json (1) y .txt (1). El más reciente es del 2026-10-15.

**Configuración:**
- **Eres:** PMO del portafolio, porque hay 13 proyectos.
- **Aviso:** dos días antes de un comité quincenal. El próximo lo supuse para el 2026-10-22; nadie lo confirmó.
- **Formato:** presentación.
- **Dónde queda:** configuración en `.criterio/portafolio/config.json`, estado en `estado/` e informes en `reportes/`.

**Términos:** aceptados por José Francisco Ñáñez para la versión 0.3.9 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.9-2026-10-15.md` y `.pdf`. El SHA-256 del .md empieza por f0f8a373c9bdced2.

### Probé con tres proyectos
Elegí PRY-203, PRY-204 y PRY-206, que tienen documentos del 14 y 15 de octubre. Dejé PRY-201 fuera porque ya lo lleva su propio agente de proyecto. Los tres declaran rojo, así que ninguno estaba en verde con evidencia en contra.

| Proyecto | Hallazgos |
|---|---|
| PRY-203 Reposición automática | Ninguno. Su acta e informe quedaron registrados como declaración. No tiene cronograma, así que no hay hitos que contrastar. |
| PRY-204 Cajas de autopago | 2. El hito «Diseño de la experiencia aprobado» figura cerrado sin acta de recibo. Mauricio Pérez se comprometió a «entregar el punto 21» sin fecha en el comité del 2026-10-02. |
| PRY-206 Precios dinámicos | 7, abajo. |

**PRY-206:**
- **Avance:** declara 37 % y el plan sustenta entre 60 % y 80 %, una diferencia de 23 puntos.
- **Hito vencido:** «Piloto en tiendas» venció el 2026-10-04.
- **Hitos cerrados sin acta:** «Diseño de la experiencia aprobado» e «Integración con el ERP».
- **Entregable aceptado sin acta (CT-557):** «Configuración del catálogo». Aun así está facturado: 2.436.027.969 COP, el valor de tres entregables.
- **Entregable tardío (CT-778):** «Configuración del catálogo» venció el 2026-10-09 y sigue pendiente.
- **Facturado sobre lo aceptado (CT-778):** se facturó 257.089.358 COP más que el valor de los entregables con acta.

### El portafolio completo
Quedan 10 proyectos y 73 documentos sin leer, en dos lotes uno tras otro, muy por debajo del tope de 400 por corrida. El cálculo de esta prueba tardó 67 segundos sin contar mi lectura, así que no tengo una estimación de tiempo fiable.

### Lo que le falta a tu carpeta
- PRY-203 y PRY-211 no tienen cronograma. El cierre comprometido de PRY-203 (2026-08-25) ya pasó.
- Las actas de los tres proyectos tienen alcance genérico («Componente 1, 2, 3») y no dicen hasta dónde puede decidir el gerente sin subir a comité.
- En los tres proyectos faltan actas de recibo de hitos cerrados. Ninguno declara dependencias con otros proyectos.

Ninguno bloquea el análisis. Puedo correr el portafolio completo cuando quieras. Si tu equipo de gerentes lo necesita, también puedo publicar el estándar en una carpeta compartida.

Lo que te mostré quedó en `estado/corridas/salida-portfolio-setup.md`. Esa copia ya incluye las correcciones, que hice después de registrar la corrida.