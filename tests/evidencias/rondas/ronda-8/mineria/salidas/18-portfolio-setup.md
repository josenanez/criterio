# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos mineros

La instalación quedó hecha y la probé con tres proyectos. Los tres declaran verde y en los tres hay señales que ese verde no explica.

**Miré:** 72 documentos en 13 proyectos (PRY-199 a PRY-211). Formatos: md 31, docx 14, pdf 11, xlsx 8, csv 6, json 1, txt 1. El más reciente es del 2026-10-17.
**Eres:** PMO del portafolio. Lo propuse porque hay varios proyectos.
**Te aviso:** dos días antes del comité. Supuse comité semanal, con el próximo el 2026-10-21, porque los documentos traen actas de «comité-semanal». Es un supuesto mío: corrígelo si no es así.
**En:** presentación.
**Dónde guardo lo que encuentro:** `estado/` (fichas) y `reportes/` (informes), junto a la carpeta de documentos.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.13 (términos 1.1), el 2026-10-17. Comprobante en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`. SHA-256 6d4b67767ea3a1ea…
**Preguntas hechas:** 0. Tomé la respuesta sugerida en cada punto.

### Probé con tres proyectos

Tomé los tres con la documentación más reciente: PRY-204, PRY-201 y PRY-206. Sus fichas quedaron selladas en `estado/records/`. Las 25 señales salen del cálculo (`compute`).

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-204 Monitoreo de taludes | 5 | Declara verde y 45% al 2026-10-17. Ejecutado: 45,2% de 800 M COP. | Autoridad del gerente, fase, actas de recibo de los 3 hitos, proveedor. |
| PRY-201 Ampliación de la relavera | 17 | Declara verde y 29% al 2026-10-09. Ejecutado: 33,2% de 4.200 M COP. Tomé 26 compromisos de 6 comités y de las notas del 10-17. Trae `ficha-pm.json` del gerente, que dejé aparte en `pm_record`. | Autoridad, fase, producto, proveedor y contrato, lo facturado, acta de la ingeniería básica. |
| PRY-206 Red privada LTE en mina | 4 | Declara verde y 68% al 2026-10-16. Ejecutado: 52,4% de 6.800 M COP. Proyección de costo 4,2% sobre lo aprobado. | Autoridad, fase, producto, actas de recibo de las 2 ingenierías, proveedor. |

**PRY-204 (7 señales)**
- Declara 45% con los tres hitos cerrados, que el plan sostiene como 100%. Son 55 puntos de diferencia.
- Los tres hitos figuran cerrados sin ningún acta que lo pruebe.
- El cierre corrió 40 días contra el acta (18,7%). La solicitud CC-01 (+40 días, +80 M COP) sigue pendiente de comité, así que ese movimiento no está autorizado.

**PRY-201 (15 señales)**
- El cierre corrió 96 días contra el acta (29,6%), con 0 días autorizados. CC-01 (+96 días, +192 M COP) está pendiente.
- La ingeniería básica figura cerrada desde hace 107 días sin acta.
- Hay 6 compromisos vencidos sin evidencia. El más viejo es «Actualizar la matriz 6», con 32 días.
- «Enviar el documento 1» se reprogramó 6 veces y «Cerrar la prueba 2», 5 veces.
- Dos compromisos no tienen fecha. En uno, María Restrepo dice haber entregado el anexo 11 y no hay acta.
- Los equipos del proveedor figuran entregados, sin acta de aceptación y sin proveedor nombrado.
- Del 2026-10-17: un riesgo dicho en la reunión que nadie registró. Es que el proveedor podría no llegar con el equipo completo a la siguiente fase.

**PRY-206 (3 señales)**
- Las dos ingenierías cerradas no tienen acta. Esa es la única señal que contradice su verde.
- No hay desviación de plazo contra el acta.

### El portafolio completo
Faltan 10 proyectos (PRY-199, 200, 202, 203, 205, 207, 208, 209, 210, 211) con 46 documentos, en un solo lote. Estimo 30 a 40 minutos con `workers: 1`. Es una estimación por lo que tardaron estos tres, no una medición.

### Lo que le falta a tu carpeta
Ninguno de estos puntos bloquea el análisis.
- **Actas de recibo:** PRY-204 y PRY-206 no tienen ninguna, y eso deja los hitos cerrados sin prueba. PRY-201 tiene cuatro, pero son de compromisos, no de hitos.
- **Autoridad del gerente:** no aparece en las tres actas, así que no se puede saber si un cambio excede lo que el gerente decide solo.
- **Alcance:** las actas dicen «Componente 1, 2 y 3», sin más detalle.
- **Producto:** PRY-201 y PRY-206 dicen «No aplica».
- **Reuniones:** PRY-204 no tiene carpeta de reuniones. Las notas del 10-17 de PRY-201 están sueltas en la raíz del proyecto.
- **Solo acta e informe:** PRY-205, PRY-208 y PRY-209 no tienen cronograma ni reuniones, así que ahí el análisis de plazos será corto.

### Registro
La salida está en `estado/corridas/salida-portfolio-setup.md`. Registré la corrida dos veces porque corregí un conteo (PRY-201 son 15 señales, no 14) y tuve que volver a registrarla. Las dos entradas están en `estado/corridas/`.

¿Corro los 10 proyectos que faltan? Si tienes equipo, también puedo publicar el estándar en una carpeta compartida para que tus gerentes usen los mismos criterios.