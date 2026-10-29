# /criterio-product:product-setup documentos/productos/PRD-303

## Listo — Logística de frío (PRD-303)

**Lo que miré:** 5 documentos, de los cuales 1 es de descubrimiento: una ronda de entrevistas del 2025-10-13 con una sola cita. También leí la definición del 2026-05-27 y el acta del comité del 2026-10-15, que es un .docx. Todo se pudo leer.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.3 el 2026-10-28. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.12.1-2026-10-28.md` y `.pdf`, con SHA-256 `0436c0ebf441ef53`…
**Configuración:** `.criterio/producto/PRD-303/config.json`. El estado queda en `estado-producto/PRD-303`; no toqué `estado/`, que es de otro agente. La verificación de la configuración salió bien.
**Registro:** levanté la ficha del producto y 15 requerimientos, 13 aceptados y 2 propuestos, tal como los dice el acta. La salida completa quedó en `estado-producto/PRD-303/corridas/salida-product-setup.md`, y la corrida quedó registrada como `2026-10-28-product-setup-1`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Farmacéuticas no tiene logística de frío» | Una cita de un «cliente entrevistado» sin nombre: «Lo necesito y hoy no lo tengo.» No dice que sea farmacéutica ni que hable de frío. | 2025-10-13 |
| «Propuesta principal» | Nada: es texto de relleno. | — |
| volumen_mensual = 70.118 | Solo el propio caso de negocio, sin serie medida. | 2026-05-27 |
| «Retorno esperado en 24 meses» | Nada: no hay cifra ni cálculo. | 2026-05-27 |
| «El precio del combustible se sostiene» (supuesto) | El supuesto declarado y un anexo que dice «se confirmó». | 2026-09-06 |

### Lo que no está dicho en ninguna parte
- **Segmento:** que las farmacéuticas, como segmento, no tengan logística de frío.
- **Propuesta:** cuál es. El documento solo dice «Propuesta principal».
- **Éxito:** no hay criterio de éxito.
- **Volumen:** de dónde sale 70.118 al mes y qué mide.
- **Retorno:** cómo se llega al de 24 meses.
- **Autoridad:** quién decide qué se construye. El acta solo registra a Ricardo Salas como asistente y no dice quién decidió. En la configuración puse «Comité de producto» como propuesta, no como dato de un documento.
- **Requerimientos:** el problema de cada uno. Los 15 se llaman «Requerimiento REQ-xxxx» y ninguno dice qué se necesita.
- **Plan:** cuál «se mantiene», según el acta. No hay plan en la carpeta.
- **Cifras recalculadas:**
  - 15 requerimientos, 10 con evidencia (76,9 %) y 0 con proyecto que los ejecute (0,0 %).
  - 3 aceptados sin evidencia: REQ-2028, REQ-4301 y REQ-4312.
  - 6 aceptados sin criterio de aceptación.
  - 13 aceptados sin proyecto.
  - 11 con evidencia vencida.
  - 2 propuestos sin decidir: REQ-4308 con 61 días y REQ-4309 con 95.
- **Serie medida:** no hay ninguna a la vista. Nadie está midiendo lo que el caso de negocio afirmó, así que no se puede calcular ninguna desviación.

### Supuestos sobre los que está escrita
- **Único supuesto declarado:** «El precio del combustible se sostiene», declarado el 2026-08-30, tres meses después de la definición.
- **Verificación:** figura como verificado con la medición del piloto del 2026-09-06. Pero el anexo que dice ser esa evidencia solo trae «se confirmó» y no la medición. Lo registré como verificado según el documento, con esa reserva.
- **Lo que no declara:** ningún supuesto sobre que el cliente pagaría, el volumen o el retorno.

### Qué le falta a tu carpeta
- **Transcripciones de las entrevistas:** hoy hay una ronda con una cita, y diez requerimientos se apoyan en ella. Tiene 12 meses, así que toda la evidencia de demanda está vencida.
- **Serie del volumen mensual:** falta la serie, con su fuente.
- **Decisiones del comité:** faltan con quién decidió. Sin eso, un requerimiento aceptado se ve igual que uno que nadie revisó.
- **REQ-2028:** sigue otra numeración que los demás (REQ-43xx) y se aceptó el 2026-10-07. Conviene confirmar que es de este producto.
- **Proyectos:** ninguno declarado para los 13 aceptados.
- **Marca de la carpeta:** no dejé `_CRITERIO_PRODUCTO.txt` porque nadie lo pidió y es lo único que un agente escribiría dentro de tus documentos.

### Notas de la corrida
- **Preguntas:** las 4 se resolvieron con la respuesta sugerida, y las dije en una línea cada una. El tiempo hasta el primer resultado no se midió.
- **Orden de comandos:** `sellar` exigía una corrida abierta, así que corrí `corrida-inicio` antes. El texto del comando decía que aquí no va.

### Después
Te sugiero `/product-discovery` sobre las entrevistas: ahí los temas se vuelven requerimientos con la cita de quién los pidió.