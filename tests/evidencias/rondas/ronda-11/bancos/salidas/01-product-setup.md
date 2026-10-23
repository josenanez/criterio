# /criterio-product:product-setup documentos/productos/PRD-302

## Listo: Crédito hipotecario digital (PRD-302)

Ejecuté `/product-setup` completo sobre `documentos/productos/PRD-302`. No hubo interfaz, así que tomé la respuesta sugerida en cada pregunta.

**Lo que miré:** 6 documentos. Uno es de descubrimiento: una ronda de entrevistas del 2025-10-15, con un solo cliente sin nombre. La definición es del 2026-05-08 y lo más reciente es el acta del comité del 2026-10-22. No hubo formatos que no pudiera leer.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.8.0 (términos 1.2), con fecha 2026-10-23. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-product-0.8.0-2026-10-23.md` y `.pdf`. El SHA-256 del Markdown empieza por d1497e5f9c28…

**Respuestas por defecto que tomé:**
- **Gerente:** Elena Duarte.
- **Quién decide:** «Comité de producto». Ningún documento lo dice, así que es una propuesta y no un dato.
- **Dónde guardo el estado:** `estado-producto/PRD-302`, no la carpeta `estado/` de otro agente.
- **Marca de la carpeta:** dejé `_CRITERIO_PRODUCTO.txt` en la carpeta del producto, único archivo que escribí dentro de los documentos.

### Lo que la definición afirma y qué lo sostiene

| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Alguien necesita esto y hoy no lo tiene | Una entrevista anónima | 2025-10-15, 12 meses (vencida) |
| El segmento paga por esto | El anexo dice «se confirmó» y remite a un documento técnico del proveedor que no está en la carpeta. El anexo no trae ningún dato. | 2026-09-04 |
| Volumen mensual de 289.875 | Solo el caso de negocio. Lo medido es 235.072, y la diferencia es 18.9 %. | Declarado 2026-05-08, medido 2026-10-13 |

El 18.9 % queda bajo el umbral de 20 %, así que el cálculo no lo marca como alerta. Lo dejé dicho de todos modos.

### Lo que no está dicho en ninguna parte
- **El segmento del entrevistado:** la entrevista no dice que sea del segmento Empresas.
- **El criterio de éxito y la propuesta:** la definición dice solo «Propuesta principal».
- **El retorno esperado:** el caso de negocio dice «Retorno esperado en 24 meses», sin cifra ni fuente.
- **El origen de 289.875:** la fuente citada es el propio caso de negocio.
- **Quién decide qué se construye:** el acta solo registra a Elena Duarte como asistente.
- **Qué proyecto construye algo:** la definición dice «Ninguno declarado».
- **Un doliente para REQ-4214:** aparece como «sin asignar».

### Los 16 requerimientos del acta
Son 13 aceptados y 3 propuestos. Las señales:
- **13 con evidencia vencida:** toda sale de la misma entrevista de octubre de 2025.
- **13 aceptados sin proyecto:** la traza es 0 de 13.
- **3 aceptados sin criterio de aceptación:** REQ-4203, 4204 y 4209.
- **2 aceptados sin evidencia de quién los pidió:** REQ-4202 y 4213.
- **3 propuestos sin decisión:** llevan entre 92 y 208 días.
- **1 sin doliente:** REQ-4214.

El acta tampoco dice qué se pide en cada requerimiento: los 16 se llaman «Requerimiento REQ-42xx».

### Qué falta en la carpeta
- Material de descubrimiento posterior a octubre de 2025, que identifique al entrevistado.
- El documento técnico del proveedor del 2026-09-04.
- La serie histórica de `volumen_mensual`: hoy hay un solo punto medido.
- Una fuente para las cifras del caso de negocio y para el retorno.
- La decisión del comité sobre cada requerimiento: «Se mantiene el plan» no dice cuál.

### Qué quedó registrado
- **Estado:** la ficha del producto, 16 requerimientos y la métrica quedaron en `estado-producto/PRD-302`. La lectura quedó sellada.
- **Configuración:** está en `.criterio/producto/PRD-302/config.json`. El comando `config` la verificó sin campos faltantes.
- **Corrida:** `2026-10-23-product-setup-1`, con la salida completa en `estado-producto/PRD-302/corridas/salida-product-setup.md`.

### Tropiezo de mi parte
Abrí la corrida después de escribir la ficha y por eso `sellar` la rechazó. Reescribí la ficha dentro de la corrida y sellé de nuevo, ya sin error.

### Siguiente paso
Puedes correr `/product-discovery` sobre la entrevista. Ahí se ve qué temas hay y a cuáles requerimientos les falta la cita de quien los pidió.