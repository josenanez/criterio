# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Retail

**Miré:** 66 documentos en 13 proyectos (PRY-199 a PRY-211). Hay 36 en .md, 11 en .docx, 7 en .pdf, 7 en .xlsx, 3 en .csv, 1 en .json y 1 en .txt. El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio. Es la propuesta por defecto, porque hay 13 proyectos.
**Te aviso:** cada dos semanas, dos días antes del comité. Supuse el próximo comité el 2026-10-29, así que el informe aterriza el 2026-10-27. Si la fecha es otra, dímela y la cambio.
**En:** presentación, la opción por defecto.
**Términos:** José Francisco Ñáñez aceptó la versión 0.3.10 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.10-2026-10-15.md` y `.pdf`. El SHA-256 del .md empieza por `5a63e87d0ce9d540…`.

**Dónde queda todo:** la configuración en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes en `reportes/`.

### Probé con tres proyectos
Tomé los de documentación más reciente: PRY-209, PRY-204 y PRY-205. Sus fichas quedaron escritas y selladas en `estado/records/`. `compute` levantó 19 señales. Dos proyectos declaran verde y los documentos no lo sostienen.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-209 Migración del ERP | 16 (la ficha que publicó su gerente va aparte) | Declara amarillo y 75 %. Presupuesto aprobado de 6.800 M COP y proyección de 6.735 M. Saqué 26 compromisos de 6 minutas y de las notas del 15 de octubre. | Producto, facultad de decisión, fase, proveedores, cambios y evidencia de 3 de sus 4 hitos. |
| PRY-204 Cajas de autopago | 5 | Declara verde y 32 %. Presupuesto aprobado de 1.200 M COP y proyección de 1.342 M. | Facultad de decisión, fase, proveedores y quién responde por los riesgos. |
| PRY-205 Pago con QR | 7 | Declara verde y 40 %. Presupuesto aprobado de 18.000 M COP y proyección de 20.834 M. Tiene dos contratos, CT-431 y CT-592. | Facultad de decisión, fase y lo facturado en cada contrato. |

**PRY-204, verde sin sustento**
- Declara 32 % y el plan sostiene entre 50 y 75 %.
- «Ambiente de pruebas certificado» figura cerrado desde 2026-06-14 y no tiene acta de recibo (123 días).
- La proyección supera lo aprobado en 11,8 %.
- Camilo Beltrán tenía «Entregar el punto 15» para 2026-10-06 y sigue sin evidencia (9 días).

**PRY-205, verde sin sustento**
- La proyección supera lo aprobado en 15,7 %.
- «Licenciamiento de la plataforma» (CT-592, Tecnología para Tiendas) tenía fecha 2026-08-10 y sigue pendiente (66 días).
- Laura Vélez tenía «Entregar el punto 9» para 2026-10-07 y sigue abierto (8 días).

**PRY-209, amarillo con cuatro señales que el informe no menciona**
- «Ambiente de pruebas certificado» venció el 2026-10-05 (10 días).
- Hay 4 compromisos vencidos. Dos de ellos, «Entregar el punto 8» de Diana Molina y «Confirmar la fecha 15» de Laura Vélez, se dieron por entregados en reunión sin acta.
- Felipe Arango movió «Enviar el documento 1» 6 veces, de 2026-09-16 a 2026-11-29. Diana Molina movió «Cerrar la prueba 2» 5 veces.
- «Mandar el ajuste del presupuesto» no tiene fecha.
- Declara 75 % y el plan sostiene entre 25 y 50 %.
- La señal `pm_vs_pmo` sobre la fecha de cierre (2027-02-03 en mi ficha, 2027-03-06 en la del gerente) hay que mirarla con cuidado. Mi fecha salió del último hito del cronograma y la del gerente es el cierre del acta, así que son dos cosas distintas. Lo mismo pasó en PRY-204 y PRY-205, sin señal porque no tienen ficha del gerente.

Esto último no lo calculó `compute`, lo leí yo: en las notas del 15 de octubre se comentó que el proveedor podría no llegar con el equipo completo y nadie lo anotó como riesgo.

### El portafolio completo
Faltan 10 proyectos y 38 documentos. Caben en un solo lote, muy por debajo del tope de 400. La corrida de esta sesión quedó medida en 152 segundos de cómputo. El tiempo de lectura del resto es una estimación mía, algo más de lo que tomó esta prueba, y no lo medí.

### Lo que le falta a tu carpeta
Ninguno de estos puntos es bloqueante.
- Ninguna de las tres actas dice hasta qué monto o qué cambio de alcance puede decidir el gerente.
- Las tres actas traen alcance y exclusiones genéricos («Componente 1, 2, 3» y «Lo que otro proyecto cubre»).
- En PRY-205, patrocinadora y gerente son la misma persona, y el comité del 2026-10-10 la lista dos veces como asistente. El contrato CT-431 está firmado seis días antes del acta de constitución.
- En PRY-205 no hay facturas ni actas de recibo, así que no se ve qué se facturó contra qué.
- En PRY-204 el acta de recibo del diseño es del 2026-10-14, ocho meses después de la fecha en que el cronograma lo marcaba cerrado. El cierre del acta (2027-04-19) y el del último hito (2027-02-16) tampoco coinciden.
- Cinco proyectos tienen entre dos y tres documentos (PRY-200, 201, 206, 208 y 210). Sin actas de comité ni contratos no hay de dónde leer compromisos ni proveedores.
- Las notas del 2026-10-15 de PRY-209 están sueltas, fuera de `30-reuniones/`.

Hice cero preguntas, como pedía la sesión de prueba. Dejé la salida completa en `estado/corridas/salida-portfolio-setup.md` y la corrida registrada como `2026-10-15-portfolio-setup-1`. No medí los minutos hasta el primer resultado. Si quieres, corro el portafolio completo. También puedo publicar el estándar en una carpeta compartida para tu equipo.