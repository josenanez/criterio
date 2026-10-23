# /criterio-product:product-setup documentos/productos/PRD-302

## Listo — Gas para generación (PRD-302)

La configuración, los términos aceptados, la ficha del producto y los 18 requerimientos del acta quedaron registrados y sellados. No hubo nadie que contestara, así que tomé la respuesta sugerida en cada pregunta:

- **Carpeta:** `documentos/productos/PRD-302`, la del argumento.
- **Gerente:** Diana Molina.
- **Quién decide:** «Comité de producto». Es solo una propuesta por defecto: ningún documento dice quién decide. El único asistente al comité fue Diana Molina.
- **Estado:** `estado-producto/PRD-302`.
- **Marca de carpeta:** no dejé `_CRITERIO_PRODUCTO.txt` en tus documentos, porque no hubo un sí claro.

**Lo que miré:** 5 documentos, y solo uno es de descubrimiento: una entrevista del 2026-05-20, en `.docx`. Todos se pudieron leer. La definición y el caso de negocio son del 2026-01-10, el tablero del 2026-10-16 y el acta del comité del 2026-10-21.

**Términos (versión 1.2, plugin 0.8.0):** quedaron aceptados a nombre de José Francisco Ñáñez. El texto corto completo está en `estado-producto/PRD-302/corridas/salida-product-setup.md`. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.8.0-2026-10-23.md` (y `.pdf`). El SHA-256 del `.md` empieza por `d1497e5f9c2847335b…`. El script registró la fecha 2026-10-23, la del reloj de la sesión, y no la 2026-10-22 del argumento.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Industria no tiene gas para generación» | Una sola frase de un cliente sin nombre: «Lo necesito y hoy no lo tengo». No dice que sea de Industria. Sostén débil | 2026-05-20 |
| `volumen_mensual` de 115.628 | El tablero mide 98.962, 14,4 % por debajo. Es imprecisión (el umbral es 20 %), pero es un solo punto, no una serie | caso 2026-01-10 · tablero 2026-10-16 |
| «La comunidad respalda el proyecto» | Solo un supuesto, sin verificar hace 124 días | 2026-06-21 |
| «Retorno esperado en 24 meses» | Nada: no hay inversión, ingreso ni método | — |

### Lo que no está dicho en ninguna parte
- **La propuesta:** dice «Propuesta principal», un marcador sin contenido.
- **El criterio de éxito:** no existe en ningún documento.
- **El segmento:** cuántos clientes de Industria hay, cuáles, y cuánto gas.
- **El retorno:** de dónde sale el de 24 meses.
- **El plan:** el comité «mantiene el plan», pero no hay ningún plan ni proyecto declarado.
- **Quién decide:** el comité tuvo un solo asistente.
- **Los requerimientos:** los 18 se llaman «Requerimiento REQ-xxxx». Ningún documento dice qué necesita cada uno.

### Los 18 requerimientos: 16 aceptados y 2 propuestos
- **Sin proyecto que los ejecute:** los 16 aceptados (0,0 % con traza).
- **Sin evidencia de demanda:** 7 aceptados (REQ-2038, 4203, 4204, 4205, 4207, 4209, 4215). Solo 9 de 18 (56,2 %) llevan evidencia, y esa es siempre la misma entrevista, que no nombra ninguno.
- **Sin criterio de aceptación:** 4 aceptados (REQ-2038, 4201, 4204, 4214). Los demás dicen «se verifica en producción», idéntico en todos y no verificable.
- **Sin doliente:** REQ-4204, aceptado desde 2026-03-30 sin doliente, evidencia ni criterio.
- **Sin decidir:** REQ-4202 (116 días) y REQ-4211 (75 días), sobre un umbral de 60.
- **Numeración:** REQ-2030 y REQ-2038 siguen otra serie (2xxx en vez de 4xxx); confirma que son de este producto.

### Supuestos sobre los que está escrita
Solo uno está declarado: «La comunidad respalda el proyecto», fechado cinco meses después de la definición. No hay ninguna premisa sobre permisos u obligaciones normativas.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- Más entrevistas, con el nombre del cliente y su volumen.
- La serie de `volumen_mensual`.
- Un criterio de éxito.
- Un acta que diga quién decide cada requerimiento.
- El plan que el comité dice mantener.

No moví ni creé nada en `documentos/`.

Siguiente paso: `/product-discovery` sobre la entrevista, para convertir los temas en requerimientos con la cita de quién los pidió.

Para sellar tuve que abrir la corrida con `corrida-inicio`, porque `sellar` no corre sin ella. Y las dos veces que `sellar` falló, fue por esa corrida y por reescribir la ficha después de abrirla.

La corrida quedó en `estado-producto/PRD-302/corridas/2026-10-23-product-setup-1.md`. El texto mostrado está en `salida-product-setup.md`, en esa misma carpeta. La corrida tardó 33 segundos y no hizo ninguna pregunta.