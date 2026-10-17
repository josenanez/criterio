# /criterio-product:product-setup documentos/productos/PRD-306

## Listo: Recaudos (PRD-306)

**Qué miré:** 5 documentos. Uno es de descubrimiento: una ronda de entrevistas con una sola cita. También leí la definición del 2025-09-28. Lo más reciente es del 2026-10-15. Pude leer todos los formatos (4 `.md` y 1 `.docx`).

**Cómo respondí:** nadie contestó, así que tomé la respuesta sugerida en cada pregunta.
- **Producto y gerente:** Recaudos, con gerente Gustavo Neira, tal como dicen la definición y el caso de negocio.
- **Quién decide:** propuse «Comité de producto». Ningún documento lo dice.
- **Dónde queda el estado:** en `estado-producto/PRD-306`, no en la carpeta `estado/` del portafolio.

**Términos 1.1:** mostré el texto resumido tal cual y lo registré a nombre de José Francisco Ñáñez, con fecha 2026-10-17, como pediste en el argumento. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf`. El SHA-256 del `.md` empieza por `d85e8bd2335ac89a…`.

### Qué sostiene la definición
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «Asociados urbanos no tiene recaudos» | Débilmente: una entrevista a un «Cliente entrevistado» sin nombre («Lo necesito y hoy no lo tengo»). No dice recaudos ni segmento. | 2025-09-27, ya con 12 meses (el umbral) |
| `volumen_mensual` = 196.775 | Solo el caso de negocio. El tablero mide 175.099; la brecha es 11.0%, bajo el umbral de 20%, y es un solo punto, no una serie. | Declarado 2025-09-28; medido 2026-10-15 |
| Retorno esperado en 24 meses | Nada: no trae cifra ni base. | 2025-09-28 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** ningún documento dice cuándo habrá funcionado.
- **La propuesta:** dice «Propuesta principal», que es un marcador.
- **Cifra y base del retorno.**
- **Quién decide:** el acta del 2026-10-15 solo lista a Gustavo Neira y no dice quién aceptó cada requerimiento.
- **Qué proyecto lo construye:** la definición dice «Ninguno declarado» y el acta no trae proyecto en ninguna fila. El acta dice «Se mantiene el plan», pero no hay plan en la carpeta.
- **El problema de cada requerimiento:** el acta solo trae números y títulos genéricos.

### Supuesto declarado
«El reglamento vigente lo permite» lleva 154 días sin verificar. Está fechado el 2026-05-16, ocho meses después de la definición, así que alguien la editó sin cambiar la fecha.

### Los 17 requerimientos del acta
Son 16 aceptados y 1 propuesto (REQ-4614).
- **Sin proyecto:** 0 de 16 aceptados tienen proyecto que los ejecute (0.0%).
- **Con evidencia:** 11 de 16 (68.8%), y es la misma entrevista de 2025-09-27 en las 11. No nombra ninguno de esos requerimientos, y las 11 ya pasaron el umbral de antigüedad.
- **Sin evidencia:** 5 (REQ-2030, 4600, 4605, 4607, 4613).
- **Sin criterio de aceptación:** 7 (REQ-2030, 4606, 4607, 4608, 4609, 4610, 4612). En los otros 9 el criterio es «se verifica en producción», que no dice qué se mide.
- **Sin doliente:** 2 (REQ-4611 y REQ-4614).
- **Sin decidir:** REQ-4614 lleva 124 días propuesto.
- **REQ-2030:** está aceptado desde el 2026-09-23, tiene otra numeración y no tiene criterio, evidencia ni proyecto.

### Qué le falta a la carpeta
- Las transcripciones de las entrevistas.
- La serie de `volumen_mensual` con su fuente.
- Las decisiones del comité con quién decidió y por qué. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.
- El criterio de éxito y la propuesta, escritos.

### Lo que no pude hacer
- **No sellé la lectura.** `sellar` exige una corrida abierta con `corrida-inicio`, y este comando dice que aquí no va. Respeté la prohibición. La próxima corrida releerá los 5 documentos, que es barato. Hay que corregir una de las dos instrucciones.
- **No medí los minutos hasta el primer resultado**, por la misma razón (la corrida registró `segundos: null`).
- **No busqué qué proyecto podría estar ejecutando Recaudos en `documentos/proyectos/`.** Eso lo hace `/product-trace`.

La configuración pasó la verificación. La salida completa y la corrida `2026-10-17-product-setup-1` quedaron en `estado-producto/PRD-306/corridas/`.

**Siguiente paso:** `/product-discovery` sobre las entrevistas. Con una sola entrevista de hace 12 meses, lo más útil es conseguir entrevistas nuevas.