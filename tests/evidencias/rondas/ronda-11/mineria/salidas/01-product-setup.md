# /criterio-product:product-setup documentos/productos/PRD-309

## Listo — Inspección con drones (PRD-309)

**Lo que miré:** 4 documentos. Uno es de descubrimiento (las entrevistas del 2025-08-21). La definición es del 2026-03-17. Lo más reciente es el acta del comité del 2026-10-17. Pude leer todos; el .docx del comité lo leí extrayendo su texto.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.8.0 (términos 1.2, fecha 2026-10-22). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.8.0-2026-10-22.md` y `.pdf`. SHA-256 97ef3d7200b125fa…

**Configuración:** `.criterio/producto/PRD-309/config.json`. El estado está en `estado-producto/PRD-309`. Marqué la carpeta de documentos con `_CRITERIO_PRODUCTO.txt`, porque es la respuesta sugerida.

**Registro levantado:** la ficha del producto y 15 requerimientos del acta (13 aceptados, 2 propuestos).

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «Supervisores no tiene inspección con drones» | Una sola entrevista: «Lo necesito y hoy no lo tengo.» No dice que quien habla sea Supervisor | 2025-08-21 (14 meses) |
| Volumen mensual de 270.035 | Solo el propio caso de negocio. No hay ninguna serie medida | 2026-03-17 |
| Retorno esperado en 24 meses | Nada: no trae cifra, base ni cálculo | 2026-03-17 |
| «Propuesta principal» | Nada: la propuesta no tiene contenido | 2026-03-17 |

### Lo que no está dicho en ninguna parte
- **Quién decide qué se construye.** Ningún documento lo nombra. Sin ese dato no puede haber acta de constitución.
- **El criterio de éxito** y **en qué consiste la propuesta.**
- **De dónde sale el 270.035 mensual y cómo se llega al retorno.** Nadie está midiendo lo que el caso de negocio afirmó.
- **Qué proyecto construye algo.** De 13 requerimientos aceptados, 0 tienen proyecto (0,0 %).
- **Quién pidió REQ-4900 y REQ-4907.** Están aceptados sin evidencia de demanda.
- **Criterio de aceptación de REQ-4901, REQ-4903 y REQ-4913.** Están aceptados sin criterio.
- **Doliente de REQ-4912.** Figura como «sin asignar».
- **Qué dice cada requerimiento.** El acta solo les pone título «Requerimiento REQ-49xx».
- **Quién los pidió, en concreto.** El acta dice «Cliente entrevistado», y la única entrevista no nombra ninguno.

### Supuestos sobre los que está escrita
- **«La licencia ambiental lo permite»**, declarado el 2026-05-15 y sin verificar. Lleva 161 días así.
- Es el único supuesto que declara. No declara ninguno sobre volumen, retorno ni demanda.

### Lo que el cálculo marca en el registro
- **35 hallazgos** en total.
- **Evidencia vieja:** 13 requerimientos, con una entrevista de hace 14 meses.
- **Aceptados sin proyecto:** 13.
- **Aceptados sin criterio de aceptación:** 3.
- **Propuestos sin decidir:** 2. REQ-4904 lleva 183 días y REQ-4912 está desde 2026-03-29.
- **Sin doliente:** 1.
- **El acta:** dice solo «Se mantiene el plan», sin decisión por requerimiento ni quién decidió.

### Qué le falta a tu carpeta
- Las transcripciones completas de las entrevistas. Hoy hay una frase de un cliente, de hace 14 meses.
- La serie medida del volumen mensual, con su fuente.
- Las decisiones del comité: quién decide y qué decidió sobre cada requerimiento. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.
- Como sugerencia, falta la carpeta `20-metricas/`. No moví ni creé nada en tus documentos.

### Cómo se resolvieron las preguntas
No hubo preguntas a la persona. Tomé las respuestas sugeridas, como pediste.
- **Gerente:** Laura Vélez, de la definición.
- **Quién decide:** queda sin dato, porque ningún documento lo dice.
- **Carpeta de estado:** `estado-producto/PRD-309`.
- **Marca de la carpeta:** sí.

La corrida quedó registrada como `2026-10-23-product-setup-1`. La salida completa está en `estado-producto/PRD-309/corridas/salida-product-setup.md`.

**Siguiente:** `/product-discovery` sobre las entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.