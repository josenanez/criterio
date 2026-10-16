# /criterio-product:product-setup documentos/productos/PRD-309

## Listo — Crédito de libre inversión (PRD-309)

**Lo que miré:** 5 documentos y los 5 se leyeron. Hay una ronda de entrevistas del 2025-09-06 con una sola cita y el acta del comité del 2026-10-09. También hay la definición y el caso de negocio, ambos del 2025-12-13, y un tablero de métricas del 2026-10-11.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.10 (términos 1.1) el 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.10-2026-10-15.md` y `.pdf`. SHA-256 del Markdown: fdf0177cc54e5055…

**Preguntas:** hice 4 y tomé la respuesta sugerida en todas, porque la sesión no tiene interfaz. El gerente es Mauricio Pérez, según el caso de negocio. Como quien decide puse "Comité de producto", y es una propuesta mía porque ningún documento lo dice. El estado quedó en `estado-producto/PRD-309`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Microcomercio no tiene crédito de libre inversión | Una entrevista: «Lo necesito y hoy no lo tengo». No dice de qué segmento es el cliente | 2025-09-06 |
| `volumen_mensual` = 117.145 | Solo el caso de negocio. El tablero mide 85.140, que es **27,3 % menos** | 2025-12-13 / 2026-10-11 |
| El canal actual soporta el volumen | Un supuesto marcado «verificado», sin documento de la verificación | 2026-05-11 |
| Retorno esperado en 24 meses | Nada: no hay cifra ni base | — |

### Lo que no está dicho en ninguna parte
- El criterio de éxito del producto.
- Quién decide qué se construye.
- De dónde sale el 117.145: la única fuente es el propio caso de negocio.
- Cuánto es el retorno esperado y con qué se calculó.
- La propuesta de valor: la definición dice solo «Propuesta principal».
- Qué dijo cada cliente por requerimiento: el acta pone «Cliente entrevistado», sin cita ni nombre.
- El problema de cada requerimiento: los 15 se llaman «Requerimiento REQ-xxxx».
- Qué proyecto construye algo: no hay ninguno declarado.
- Qué plan se mantiene: el acta decide «Se mantiene el plan» y no dice cuál.

### Supuestos sobre los que está escrita
Declara uno solo: «El canal actual soporta el volumen». Está marcado verificado, pero no hay documento que lo muestre. Además está fechado 2026-05-11 dentro de una definición del 2025-12-13.

### El registro de requerimientos (15, tal como los dice el acta)
- Hay 11 aceptados y 4 propuestos.
- **8 aceptados no tienen criterio de aceptación:** REQ-4900, 4904, 4905, 4906, 4907, 4910, 4911 y 2035.
- **4 aceptados no tienen evidencia de demanda:** REQ-4900, 4902, 4905 y 4907.
- **11 aceptados no tienen proyecto que los ejecute.** Ninguno está trazado.
- **3 no tienen doliente:** REQ-4900, 4905 y 4913.
- **4 propuestos llevan más de 60 días sin decidir:** REQ-4901 (137 días), 4903 (168), 4908 (143) y 4913 (155).
- El cálculo da 63,6 % de aceptados con evidencia (7 de 11), pero cuenta «Cliente entrevistado» tal como lo escribe el acta. Eso es una categoría y no una cita, así que es un máximo. La única entrevista es de hace más de 12 meses.
- REQ-2035 no sigue la numeración de los demás (4900 a 4913). Lo dejé señalado y no lo corregí.
- El acta no dice quién decidió cada aceptación, solo la fecha.

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas. Hay una sola cita y ninguna enlaza con un requerimiento.
- La serie de `volumen_mensual`. Hay un solo punto, así que se ve la brecha pero no la tendencia.
- Las decisiones del comité con su motivo. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.
- Nadie ha medido el retorno esperado.

**Lo que no se pudo hacer:** `sellar` falló con "no hay una corrida abierta". Este comando no abre ninguna, así que la lectura de los 5 documentos quedó sin sellar. No lo forcé.

### Después
Con más material de entrevistas, `/product-discovery` convierte los temas en requerimientos con la cita de quién lo pidió. Con lo que hay hoy solo daría un tema.

La salida completa quedó en `estado-producto/PRD-309/corridas/salida-product-setup.md`. La corrida quedó registrada como `2026-10-15-product-setup-1`, con 31 hallazgos.