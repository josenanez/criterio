# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

La instalación quedó armada y probé el agente con tres de tus 13 proyectos. En esta prueba sin interfaz no hice ninguna pregunta: tomé los valores sugeridos y los digo aquí. Los términos los registré con el sí de José Francisco Ñáñez que venía en los argumentos.

- **Miré:** 78 documentos en 13 proyectos. Formatos: md, pdf, docx, csv, xlsx, txt y json. El más reciente es del 2026-10-16.
- **Eres:** PMO del portafolio, porque hay 13 proyectos.
- **Te aviso:** dos días antes del comité semanal. Supuse el próximo para el 2026-10-19, porque las actas se llaman «comité semanal».
- **En:** presentación.
- **Términos:** versión 1.1, aceptados el 2026-10-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.12-2026-10-16.md` y `.pdf`. El SHA-256 del .md empieza por 08da686bb7c9acf4…
- **Dónde queda todo:** la configuración en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes en `reportes/`, junto a tu carpeta de documentos.

### Probé con tres proyectos

Los elegí por tener la documentación más reciente: PRY-202, PRY-205 y PRY-208. `compute` levantó 22 señales, todas en PRY-202 y PRY-205.

**PRY-202, Planta de tratamiento de agua** (declara amarillo, 70 %)
- **Hitos sin acta.** Cuatro de sus cinco hitos figuran cerrados y no hay acta que lo pruebe. Solo «Montaje e instalación» la tiene, del 2026-10-03.
- **Avance contra plan.** El cronograma da los cinco hitos por cumplidos (100 %) y el informe dice 70 %. El cierre comprometido, 2026-07-02, ya pasó.
- **Proveedor CT-250.** Dos entregables están vencidos y pendientes: licenciamiento (318 días) y bolsa de horas (237 días). «Calibración de sensores» figura recibido en el contrato, sin acta. Hay una factura de 110.830.774 COP radicada el 2026-08-31, y el contrato exige acta de recibo para facturar.

**PRY-205, Sistema de gestión de seguridad** (declara verde, 58 %)
- **El verde no se sostiene.** Hay siete compromisos vencidos, de 2 a 18 días.
- **Reprogramaciones.** «Enviar el documento 1», de Elena Duarte, se movió seis veces, del 2026-09-30 al 2026-12-20. «Cerrar la prueba 2», de Laura Vélez, se movió cinco veces, del 2026-10-02 al 2026-12-13.
- **Hito sin acta.** «Ingeniería básica aprobada» está cerrado sin acta.
- **Sin fecha.** Tres compromisos no tienen fecha.
- **Riesgo no registrado.** En las notas del 16-oct se dijo que el proveedor podría no llegar con el equipo completo a la siguiente fase. Nadie lo anotó; lo dejé en la ficha con su fuente.
- **`ficha-pm.json`.** El gerente publicó la suya y la guardé aparte, sin mezclarla con la mía.

**PRY-208, Trazabilidad del mineral** (declara verde, 77 %)
- No levantó señales. Tiene una solicitud de cambio pendiente, CC-01 (+25 días, +50 M COP), y no tiene cronograma.

En los tres falta la facultad del gerente, es decir, hasta qué monto y qué cambio de alcance puede decidir sin subir a comité.

### El portafolio completo

Faltan 10 proyectos y 52 documentos, en un solo lote. Estimo unos 20 a 30 minutos de conversación; es una estimación mía, no una medición.

### Lo que le falta a tu carpeta

- Ningún acta de constitución trae la facultad del gerente.
- PRY-206, PRY-208 y PRY-211 no tienen cronograma, así que no se puede contrastar su avance con un plan.
- En PRY-205, dos personas dijeron haber entregado («diseño 5» y «matriz 14») sin acta que lo respalde. Los compromisos de las notas del 16-oct tampoco están en ningún acta de comité.

Ninguno de estos puntos bloquea el análisis.

La corrida quedó registrada como `2026-10-16-portfolio-setup-1`, con lo que te mostré en `estado/corridas/salida-portfolio-setup.md`. ¿Corro el portafolio completo?