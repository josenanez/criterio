# /criterio-product:product-setup documentos/productos/PRD-306

## Listo — Microseguros (PRD-306)

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

**Lo que miré:** 5 documentos, y solo 1 es de descubrimiento: una entrevista del 2025-09-25. Están la definición y el caso de negocio del 2026-07-22. Lo más reciente es el tablero del 2026-10-07. Los 5 se pudieron leer.

**Términos:** aceptados (versión 1.1) por José Francisco Ñáñez el 2026-10-17. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf`. Su SHA-256 empieza por d85e8bd2335ac89a…

**Preguntas:** nadie respondió, así que tomé la respuesta sugerida en cada una.
- **Producto:** Microseguros, PRD-306, gerente Mauricio Pérez, tal como dice el caso de negocio.
- **Quién decide:** «Comité de producto». Es la propuesta por defecto y ningún documento la confirma: el acta del 2026-10-05 solo lista a Mauricio Pérez como asistente. Confírmala.
- **Dónde guardo:** `estado-producto/PRD-306`. No toqué `estado/`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento PyME no tiene microseguros.» | Una frase de un cliente entrevistado: «Lo necesito y hoy no lo tengo.» La entrevista no dice de qué segmento es | 2025-09-25 (12 meses) |
| volumen_mensual = 140.572 | El caso de negocio. La serie medida dice 99.900, así que el negocio declara 28,9 % por encima | Declarado 2026-07-22; medido 2026-10-07 |
| «La demanda declarada se sostiene sin campaña» | Es un supuesto, sin verificar | Declarado 2026-05-04 (166 días) |
| Retorno esperado en 24 meses | Nada: no hay cifra, fuente ni cálculo | — |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** Ningún documento lo escribe.
- **De dónde sale 140.572.** El caso de negocio se cita a sí mismo como fuente, sin estudio ni cálculo.
- **El tamaño del segmento PyME** ni cuántas PyME lo necesitan.
- **Qué propuesta se construye.** La definición dice «Propuesta principal» y nada más.
- **Qué requerimiento nace de la entrevista.** Los 14 requerimientos del acta dicen «Cliente entrevistado», pero la entrevista no nombra ninguno. Los 9 aceptados con evidencia cuelgan de esa misma frase.
- **Quién decidió cada aceptación.** La única decisión escrita es «Se mantiene el plan».
- **Qué proyecto ejecuta cada requerimiento.** La definición dice «Ninguno declarado» y el acta pone «—» en los 14.

### Supuestos sobre los que está escrita
Declara uno: «La demanda declarada se sostiene sin campaña». Lleva 166 días sin verificar y no hay archivo de verificación para PRD-306. Es el que más importa verificar, porque la demanda medida está 28,9 % por debajo de la declarada.

### Los 14 requerimientos del acta (2026-10-05)
Hay 11 aceptados y 3 propuestos. Ninguno de los 11 aceptados tiene proyecto (0,0 %). Con evidencia hay 9 de 11 (81,8 %), toda de la misma entrevista.
- **Aceptados sin proyecto (11):** REQ-4600, 4601, 4602, 4603, 4604, 4605, 4607, 4609, 4611, 4612 y 4613.
- **Aceptados sin criterio de aceptación (3):** REQ-4602, 4609 y 4611.
- **Aceptados sin evidencia (2):** REQ-4605 y 4613. El acta pone «—» en quién los pidió.
- **Aceptado sin doliente (1):** REQ-4612, «sin asignar».
- **Evidencia vencida (10):** la entrevista cumple hoy 12 meses, que es el umbral. Afecta a 9 aceptados y a REQ-4610.
- **Propuestos sin decidir (3):** REQ-4606 (181 días), REQ-4608 (169) y REQ-4610 (103). El umbral es 60.
- **Títulos y criterios:** los 14 se titulan «Requerimiento REQ-46xx», sin el problema que resuelven. «Se verifica en producción» no es un criterio verificable.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- Más descubrimiento y más reciente: hay una sola entrevista, de hace 12 meses y anterior a la definición.
- Las transcripciones, con a quién se entrevistó y qué pidió cada uno.
- La serie de volumen_mensual: hay un solo punto, así que no se ve tendencia.
- El sustento del 140.572.
- Las decisiones del comité con quién decide y por qué. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.

**Siguiente:** `/product-discovery` sobre la entrevista, para ver si de ahí sale algún requerimiento con la cita de quién lo pidió.

La configuración quedó en `.criterio/producto/PRD-306/config.json` y `config` la verificó sin faltantes. La corrida quedó registrada como `2026-10-17-product-setup-1`, con la salida completa en `estado-producto/PRD-306/corridas/salida-product-setup.md`.

El script de sellado me obligó a abrir una corrida con `corrida-inicio` y a reescribir las fichas dentro de ella. El comando dice que aquí no va `corrida-inicio`, y lo dejé anotado en la nota de la corrida.