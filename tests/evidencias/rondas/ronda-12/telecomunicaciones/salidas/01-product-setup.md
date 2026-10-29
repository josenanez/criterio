# /criterio-product:product-setup documentos/productos/PRD-306

## Listo: Televisión IP (PRD-306)

**Lo que miré:** 5 documentos. Uno es de descubrimiento: una ronda de entrevistas del 2025-09-25. La definición es del 2026-03-07 y lo más reciente es el acta de comité del 2026-10-25. Pude leer todos los formatos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-28 para la versión 0.12.1 (términos 1.3). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.12.1-2026-10-28.md` y `.pdf`, con SHA-256 0436c0ebf441ef53…

**Respuestas sugeridas que tomé, porque nadie contestaba:**
- **Carpeta:** `documentos/productos/PRD-306`, la del argumento.
- **Quién eres:** Gustavo Neira, gerente del producto, según la definición.
- **Quién decide:** sin dato. Ningún documento lo dice, así que lo dejé vacío y no lo inventé.
- **Estado:** `estado-producto/PRD-306`, aparte de `estado/`, que es la carpeta de otro agente.
- **Marca de carpeta:** sí. Dejé `_CRITERIO_PRODUCTO.txt` en `documentos/productos/PRD-306`; es lo único que escribí dentro de los documentos.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Grandes empresas no tiene televisión ip» | Una sola entrevista, de un cliente sin nombre: «Lo necesito y hoy no lo tengo». No dice de qué segmento es. Evidencia media, con 13 meses de antigüedad. | 2025-09-25 |
| «El proveedor cumple el tiempo pactado» (supuesto) | El anexo de verificación dice «se confirmó» y se declara a sí mismo como evidencia. No trae el documento técnico del proveedor ni dice cuál es el tiempo pactado. | declarado 2026-08-11, verificado 2026-09-19 |

### Lo que no está dicho en ninguna parte
- **Para quién es.** La entrevista es la única demanda escrita y no nombra al cliente ni su segmento, así que no hay nada que diga que lo pidió Grandes empresas.
- **El criterio de éxito.** La definición no lo tiene. El caso de negocio solo dice «Retorno esperado en 24 meses», sin cifra ni forma de medirlo.
- **La propuesta.** Dice «Propuesta principal» y nada más.
- **El volumen mensual de 100.016.** No dice de qué es el volumen ni de dónde sale la cifra. No hay ninguna serie medida, porque no existe `20-metricas/`: nadie está midiendo lo que el negocio afirmó.
- **Quién decide qué se construye.** El acta solo lista a Gustavo Neira como asistente y su decisión es «Se mantiene el plan». Ningún documento dice cuál plan.
- **Qué pidió cada requerimiento.** Los 12 se llaman «Requerimiento REQ-46xx», sin enunciado.
- **Proyectos que los construyan.** La definición dice «Ninguno declarado» y el acta no nombra proyecto para ninguno.

### Lo que el registro ya muestra
- **Sin proyecto:** de 11 requerimientos aceptados, ninguno tiene proyecto que lo ejecute (0,0 %).
- **Una sola entrevista:** 8 aceptados (72,7 %) tienen evidencia, y es siempre la misma entrevista de 13 meses. Esa entrevista trata «Necesidad principal» y no nombra ninguno de los 8.
- **Sin evidencia:** REQ-4600, REQ-4602 y REQ-4609 no tienen quién los pidió.
- **Sin criterio de aceptación:** REQ-4603 y REQ-4608.
- **Sin decidir:** REQ-4605 sigue propuesto y sin doliente, desde el 2026-04-07 (204 días).

### Supuestos sobre los que está escrita
Declara uno: «El proveedor cumple el tiempo pactado». La definición está fechada 2026-03-07 pero contiene un supuesto declarado en agosto, así que se editó después de su fecha sin decir cuándo. No declara ningún supuesto sobre el tamaño del segmento.

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas, con quién habló y de qué empresa.
- La serie de la métrica principal, con su fuente.
- Un criterio de éxito escrito y quién autoriza qué se construye.
- El documento técnico del proveedor que cita el anexo.

**Siguiente paso:** `/product-discovery` sobre las entrevistas, para que los temas queden con la cita de quién los pidió.

La salida quedó en `estado-producto/PRD-306/corridas/salida-product-setup.md`. La corrida quedó registrada como `2026-10-28-product-setup-1`: 31 segundos y 26 señales sobre los 12 requerimientos.

Para sellar la lectura tuve que abrir una corrida con `corrida-inicio`, aunque el comando dice que aquí no va. Sin eso `sellar` se negaba a sellar, y además reescribí `producto.json` dentro de esa corrida.