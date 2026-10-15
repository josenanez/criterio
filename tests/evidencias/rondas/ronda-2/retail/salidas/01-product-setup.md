# /criterio-product:product-setup documentos/productos/PRD-303

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

## Listo — Pago con QR (PRD-303)

**Lo que miré:** 4 documentos. Uno es de descubrimiento: una ronda de entrevistas del 2025-09-29 con una sola cita. La definición y el caso de negocio son del 2025-10-19. Lo más reciente es el acta del comité del 2026-10-10. Pude leer todos los formatos (2 .docx, 2 .md).

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-15 para la versión 0.3.8 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.8-2026-10-15.md` y `.pdf`. SHA-256: d532cc0636d081a9…

**Las cuatro preguntas** (sin interfaz, tomé la sugerida en cada una):
- **Gerente y producto:** María Restrepo y Pago con QR, tal como los dice la definición.
- **Quién decide:** los documentos no lo dicen, así que queda sin dato.
- **Dónde guardo:** `estado-producto/PRD-303`, hermana de la documentación. No toqué `estado/`.
- **Términos:** aceptados, como arriba.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Clientes frecuentes no tienen pago con QR (el problema) | Una cita de un cliente sin nombre: «Lo necesito y hoy no lo tengo» (`10-descubrimiento/2025-09-29-entrevistas.md`). No dice que sea cliente frecuente ni que hable de QR. Sostenida, y débil | 2025-09-29 |
| La demanda se sostiene sin descuento | Solo un supuesto declarado, sin verificar desde hace 212 días (`00-definicion/2025-10-19-definicion-producto.docx`) | declarado 2026-03-17 |
| El volumen mensual será 243.100 | El propio caso de negocio, que se cita a sí mismo como fuente. No hay serie medida detrás | 2025-10-19 |
| Los cinco requerimientos fueron pedidos por «Cliente entrevistado» | El acta del comité nombra la categoría, no quién ni qué dijo (`30-decisiones/2026-10-10-comite-producto.docx`). La única entrevista de la carpeta es la de arriba y no se refiere a ninguno de los cinco | acta 2026-10-10 |

### Lo que no está dicho en ninguna parte
- **Quién decide qué se construye.** Ningún documento lo nombra. El acta del comité solo lista a María Restrepo como asistente. Sin ese dato no hay acta de constitución posible.
- **El criterio de éxito.** No existe. Sin él, el cierre no tiene contra qué juzgarse.
- **La propuesta.** La definición tiene el título «Propuesta principal» y debajo nada.
- **Por qué Clientes frecuentes.** Ningún documento dice cuántos son ni por qué ese segmento y no otro.
- **De qué es el 243.100.** El caso no dice si son transacciones, pesos o clientes, ni a qué plazo.
- **El retorno.** «Retorno esperado en 24 meses» no trae cifra ni base.
- **Qué plan se mantiene.** El acta decide «Se mantiene el plan», pero la definición dice «Proyectos que lo construyen: Ninguno declarado». No hay plan escrito.
- **La necesidad detrás de cada requerimiento.** Los cinco se llaman «Requerimiento REQ-xxxx» y ninguno dice qué problema resuelve.
- **Quién aceptó cada requerimiento.** El acta da el estado «aceptado» y desde cuándo, pero no quién lo decidió.

### Supuestos sobre los que está escrita
Hay uno declarado: *«La demanda se sostiene sin descuento»*, sin verificar, 212 días. Es el único que el documento reconoce. Los demás (que el segmento quiere QR, que el volumen se alcanza) no están declarados como supuestos y aparecen en la sección anterior.

### Los números del registro
- Hay 5 requerimientos y los 5 están aceptados. Los 5 tienen evidencia (100.0%), pero esa evidencia es solo la categoría «Cliente entrevistado».
- **Con proyecto que los ejecute: 0 de 5 (0.0%).** Son cinco señales de «aceptado sin proyecto» (REQ-1030, 1031, 1032, 2017, 2025).
- **Sin criterio de aceptación: 2** (REQ-2017 y REQ-2025). Los otros tres dicen «se verifica en producción», que no dice qué se verifica.
- En total hay 8 señales: 5 sin proyecto, 2 sin criterio y 1 supuesto sin verificar.
- **Métrica medida: ninguna.** El caso declara volumen_mensual 243.100 (2025-10-19) y no hay ninguna serie en la carpeta. Nadie está midiendo lo que el negocio afirmó, y por eso no se puede contrastar.

### Qué le falta a tu carpeta
Es un hallazgo, no un requisito:
- Las transcripciones de las entrevistas, con quién habló y de qué. Hoy hay una cita de una persona sin nombre.
- La serie de volumen mensual con su fuente, para contrastar el 243.100.
- La decisión del comité por requerimiento, con quién la tomó. Hoy un requerimiento descartado se vería igual que uno que nadie miró.
- Un nombre para quien decide, y un criterio de éxito.

### Notas de la instalación
- El comando pide no abrir `corrida-inicio`, pero `sellar` se niega sin una corrida abierta. La abrí y re-guardé (con `touch`) los archivos de la ficha para que el sellado los diera por escritos en esta corrida. El contenido no cambió. Quedó sellada la lectura de los 4 documentos.
- `authority` queda en blanco en la configuración, a propósito.
- La definición lleva fecha 2025-10-19, pero su supuesto está declarado el 2026-03-17. El documento se editó después de su fecha y no lo dice.

La corrida quedó registrada como `2026-10-15-product-setup-1`. Lo mostrado está en `estado-producto/PRD-303/corridas/salida-product-setup.md`, y la configuración verifica sin faltantes.

**Siguiente paso:** `/product-discovery` sobre las entrevistas. Ahí los temas se vuelven requerimientos con la cita de quién los pidió.