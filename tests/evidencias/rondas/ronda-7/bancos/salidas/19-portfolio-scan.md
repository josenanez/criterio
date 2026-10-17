# /criterio-portfolio:portfolio-scan 

## Barrido — 2026-10-17

Los términos de esta versión (0.3.13) ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-17. No hizo falta registrarlos de nuevo.

**Documentos:** hay 81 en la carpeta. Leí 51, 30 no cambiaron y ninguno fue ilegible.
**Proyectos:** hay 13. Creé 10 fichas nuevas y no toqué PRY-205, PRY-209 ni PRY-211.

El plan fue un solo lote de 10 proyectos, uno tras otro y sin subagentes. Nada quedó diferido. Word, Excel y PDF se leyeron por su texto convertido, y las citas van a los originales.

### Nuevos
| Proyecto | Docs | Campos encontrados | Campos sin dato |
|---|---|---|---|
| PRY-199 Renovación de cajeros | 6 | 13 de 15 | autoridad, etapa, facturado a Consultora Andina (no hay facturas) |
| PRY-200 Originación digital | 6 | 13 de 15 | autoridad, etapa |
| PRY-201 Core de depósitos | 6 | 13 de 15 | autoridad, etapa |
| PRY-202 Migración a la nube | 4 | 12 de 15 | autoridad, etapa, producto (el acta dice «No aplica») |
| PRY-203 Open Banking | 2 | 13 de 15 | autoridad, etapa y todos los hitos (**no hay cronograma**) |
| PRY-204 Débito contactless | 4 | 13 de 15 | autoridad, etapa |
| PRY-206 Billetera y QR | 5 | 13 de 15 | autoridad, etapa |
| PRY-207 Onboarding PyME | 7 | 13 de 15 | autoridad, etapa |
| PRY-208 Motor de decisión | 7 | 12 de 15 | autoridad, etapa, producto («No aplica») |
| PRY-210 Portal de proveedores | 4 | 12 de 15 | autoridad, etapa, producto («No aplica») |

Ninguna de las 13 fichas declara la autoridad del gerente, es decir, cuánto puede decidir sin subir a comité.

### Actualizados
Ninguno. Los 30 documentos de PRY-205, PRY-209 y PRY-211 no cambiaron, así que no los releí.

### Lo que ya muestran las señales
El script calculó 67 alertas en 11 de las 13 fichas, y 8 proyectos declaran «verde» con señales en contra. Hay 6 en este lote (PRY-200, 201, 202, 204, 207 y 210). Los otros dos están fuera de este barrido. El detalle va en el informe consolidado.

- **PRY-201 (verde, 66 %):** el cronograma v2 del 2026-10-10 corrió el piloto +107 días, pero CC-01 sigue pendiente de comité. El plan se movió sin cambio autorizado. La proyección supera el presupuesto en 24,2 %. Hay tres hitos «cerrado» sin acta de recibo.
- **PRY-207 (verde, 58 %):** pasa lo mismo. El cronograma v2 del 2026-09-24 mueve el piloto +58 días y CC-01 está pendiente. La proyección supera el presupuesto en 18,4 %. Tiene un compromiso vencido.
- **PRY-208 (rojo):** CC-01 figura «autorizada por el comité», pero el documento no nombra al comité ni cita acta. El cronograma v2 es seis días anterior a la solicitud.
- **PRY-204 (verde, 43 %):** el cierre del acta (2026-08-23) ya pasó. Los tres hitos están «cerrado» sin acta de recibo. La proyección supera el presupuesto en 23,5 %.
- **PRY-202 (verde, 34 %):** el piloto del 2026-10-13 venció sin cerrarse. La salida a producción se reprogramó sin nueva fecha. Hay dos hitos cerrados sin acta. El informe menciona un proveedor y no hay contrato en la carpeta.
- **PRY-200 (verde, 44 %):** Andrés Lozano figura como patrocinador y como gerente, y aparece dos veces como asistente del comité. El hito «Ambiente de pruebas» está cerrado sin acta.
- **PRY-210 (verde, 78 %):** el plan solo sostiene entre 25 y 50 %, porque hay 1 hito cerrado de 4. Menciona un proveedor sin contrato.
- **PRY-203 (amarillo, 18 000 M COP):** no tiene cronograma, así que no se puede medir el atraso. También menciona un proveedor sin contrato.
- **PRY-206 (rojo):** solo tiene un compromiso sin fecha.
- **PRY-199:** es la única sin alertas. El contrato CT-199 tiene 3 entregables de 144 M, todos pendientes. El primero vence el 2026-11-16.

**Compromisos vencidos sin evidencia:**
- PRY-200: el punto 13 venció el 2026-10-14.
- PRY-207: el punto 36 venció el 2026-10-10. El acta es del día 11, así que se registró con una fecha ya pasada.

**Compromisos sin fecha:** PRY-206 (punto 14) y PRY-208 (punto 37).

### No pude leer
Nada. Los 81 documentos se convirtieron a texto.

### Citas que dejaron de resolver
`index` marca 14 campos de la ficha del gerente de PRY-205 (`pm_record`) como fuente ausente, pero no es un borrado. Los documentos existen. Esa ficha cita rutas relativas a la carpeta del proyecto, y la raíz de documentación pide la carpeta incluida. No toqué esa ficha, porque es declaración del gerente. Conviene unificar la convención de rutas.

### Movidos desde entrada/
Nada. No existe `entrada/` en la carpeta de documentos.

### Pendientes de clasificar
Nada. El archivo `PRY-205-…/2026-10-17-notas-reunion.txt` queda en la raíz del proyecto, fuera de las subcarpetas de la convención. No cambió, así que no lo leí.

### Qué asumí sin poder preguntar
- Los hitos «cerrado» quedaron como `met` y los «en curso» como `pending`. Solo puse evidencia donde un acta de recibo nombra ese hito.
- «Producto asociado: No aplica» quedó como campo vacío.
- Los cronogramas v2 de PRY-201, 207 y 208 no traen motivo, así que la línea base 2 dice «no declarado en el documento».
- «Por definir» no se convirtió en fecha: quedó `no_declarada`.

### Registro de la corrida
`corrida` midió 178 segundos y 67 hallazgos. Su campo `relectura` dice 81 sin cambio y 0 releídos, porque lo calculó después de sellar. Yo sí leí 51 documentos en esta corrida.

### Después
Puedo preparar el informe consolidado con `/criterio-portfolio:portfolio-report`. Ahí entrarían las contradicciones y los compromisos vencidos.

---
Criterio Portfolio 0.3.13 · fichas tocadas: 10 (PRY-199, 200, 201, 202, 203, 204, 206, 207, 208, 210) · campos en `not_found`: autoridad y etapa en las 10, producto en 202, 208 y 210, hitos en 203 · Son borradores de trabajo, no asesoría. La verificación es suya. Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13

El informe quedó en `estado/corridas/salida-portfolio-scan.md`. La versión de ese archivo es algo más larga que este resumen. Incluye en "Qué asumí" la nota sobre «esta semana», que aquí omití.