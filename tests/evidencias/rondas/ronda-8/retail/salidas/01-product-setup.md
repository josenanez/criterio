# /criterio-product:product-setup documentos/productos/PRD-309

## Listo — Tarjeta de la tienda (PRD-309)

**Lo que miré:** 5 documentos. Uno es de descubrimiento: una entrevista del 2025-10-11. Hay una definición escrita del 2025-11-12, con su caso de negocio. Lo más reciente es el acta del comité del 2026-10-16. Pude leer los 5.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.1 (familia 0.3.13) el 2026-10-17. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf`. Las huellas SHA-256 empiezan con d85e8bd2335ac89a… (`.md`) y ffdddcc09fd7c905… (`.pdf`).
**Preguntas hechas:** 0. Nadie respondía, así que tomé la respuesta sugerida en cada una:
- **Gerente y producto:** Elena Duarte, «Tarjeta de la tienda», PRD-309 (sale del caso de negocio).
- **Quién decide qué se construye:** «Comité de producto» (sale del acta). El acta lista un solo asistente, Elena Duarte, y no dice quién decidió.
- **Dónde guardo lo que encuentre:** `estado-producto/PRD-309`. No toqué `estado/`, que es de otro agente.
- **Términos:** sí, con el nombre y la fecha que dio la sesión de prueba.

**Registro levantado:** `producto.json` y los 15 requerimientos que nombra el acta, en `estado-producto/PRD-309/requirements/`. 11 están aceptados y 4 propuestos. Solo copié lo que dice el acta.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Clientes frecuentes no tiene tarjeta de la tienda» | Nada que la nombre. La única entrevista dice «Lo necesito y hoy no lo tengo» y no menciona ni la tarjeta ni el segmento. | Entrevista del 2025-10-11 (12 meses) |
| «La regulación de datos lo permite» | Un supuesto declarado el 2026-03-28, con verificación del 2026-08-21 («se confirmó»). Se apoya en un concepto jurídico que **no está en la carpeta**. | 2026-08-21 |
| Volumen mensual de 106.991 | El propio caso de negocio, que se cita a sí mismo como fuente. No hay serie medida. | 2025-11-12 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** Ni la definición ni el caso de negocio dicen cómo se sabe que la tarjeta funcionó.
- **La propuesta.** La sección dice solo «Propuesta principal». No dice qué se ofrece, ni a quién, ni con qué condiciones.
- **Qué es un «cliente frecuente»**, ni cuántos hay. El segmento no tiene definición ni tamaño.
- **Qué cuenta 106.991.** «volumen_mensual» no trae unidad: puede ser transacciones, tarjetas o pesos. Tampoco hay serie medida con qué contrastarlo.
- **El retorno esperado.** Dice «Retorno esperado en 24 meses» y no trae cifra ni fuente.
- **Qué pidió cada requerimiento.** El acta solo trae el identificador («Requerimiento REQ-4900», etc.).
- **Quién decidió cada aceptación.** El acta da el estado y la fecha, pero no quién.
- **Qué proyecto construye algo.** La definición dice «Ninguno declarado» y la columna «Proyecto que lo ejecuta» del acta está vacía en los 15.

### Supuestos sobre los que está escrita
Declara uno: «La regulación de datos lo permite». Figura verificado, pero la verificación es una nota corta que remite a un concepto jurídico del 2026-08-21. Ese concepto no está en la carpeta, así que lo único citable es que alguien dice haberlo confirmado.

La definición lleva fecha 2025-11-12 y menciona hechos del 2026-03-28 y del 2026-08-21. Se editó después de su fecha, así que esa fecha no es la de su contenido.

Hay dos supuestos que el documento no declara: que los clientes frecuentes quieren la tarjeta, y que el volumen de 106.991 se alcanza.

### Lo que el registro ya muestra
| Señal | Cuántos | Cuáles |
|---|---|---|
| Evidencia envejecida (12 meses; la más nueva es la entrevista del 2025-10-11) | 11 | todos los que tienen evidencia |
| Aceptado sin proyecto que lo ejecute | 11 de 11 aceptados (0,0 % con traza) | todos los aceptados |
| Aceptado sin criterio de aceptación | 4 | REQ-2028, REQ-4901, REQ-4911, REQ-4913 |
| Aceptado sin evidencia de demanda | 2 | REQ-4903, REQ-4911 |
| Propuesto sin decidir | 4 | REQ-4909 (152 días), REQ-4900 (105), REQ-4904 (77), REQ-4908 (70) |
| Sin doliente | 2 | REQ-4909, REQ-4913 («sin asignar») |

- **Evidencia:** el acta dice que 9 aceptados y 2 propuestos los pidió un «cliente entrevistado». Los 11 apuntan a la misma entrevista: una persona sin nombre, que no nombra ninguno de ellos. La cité como la más cercana, con su fecha, y lo anoté en cada registro. 9 de los 11 aceptados tienen alguna evidencia (81,8 %), y siempre es la misma cita.
- **Cifras:** no hay ninguna serie medida del volumen. Nadie está midiendo lo que el caso de negocio afirmó, y eso es un hallazgo.
- **REQ-2028** no sigue la numeración de los demás (4900–4913) y se aceptó el 2026-09-22. Lo registré tal cual y no sé de dónde sale.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito. Esto funciona con lo que hay.
- **Las transcripciones de las entrevistas.** Hay una entrevista de una sola cita, y de ella cuelgan 11 requerimientos.
- **La serie del volumen mensual**, con su fuente y su fecha.
- **El concepto jurídico del 2026-08-21** que sostiene la verificación del supuesto.
- **Las decisiones del comité con quién decidió.** Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró. El acta no registra ninguno descartado.
- **El plan al que se refiere «Se mantiene el plan».** No está en la carpeta.

### Lo que sigue
Corre `/product-discovery` sobre el material de entrevistas. Ahí los temas se vuelven requerimientos con la cita de quién lo pidió.

---
**Dos cosas del arnés:**
- `sellar` se negó a correr sin una corrida abierta, y también exigió que `producto.json` se escribiera dentro de ella. Por eso usé `corrida-inicio`, aunque el comando dice que aquí no va, y reescribí la ficha. El tiempo registrado (37 s) cuenta desde ese punto, no desde el inicio de la conversación.
- La corrida quedó como `2026-10-17-product-setup-1`. La verificación de la configuración (`config`) devolvió `ok` sin campos faltantes.