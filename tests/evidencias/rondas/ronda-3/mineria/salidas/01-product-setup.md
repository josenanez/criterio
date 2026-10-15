# /criterio-product:product-setup documentos/productos/PRD-306

## Listo — Almacén de repuestos (PRD-306)

La configuración y el registro del producto están escritos, y el comprobante de términos está en `.criterio/terminos/`. El hallazgo principal es que el caso de negocio declara un volumen mensual 38.5 % por encima de lo que mide el tablero.

**Lo que miré:** 5 documentos y los 5 se leyeron (los .docx extrayendo su texto). Solo 1 es de descubrimiento: una entrevista del 2025-10-14. Hay también la definición y el caso de negocio (2026-05-06), el acta del comité (2026-10-10) y el tablero (2026-10-12).

**Términos:** aceptados para la versión 0.3.9 (términos 1.1) a nombre de José Francisco Ñáñez, fecha 2026-10-15, como dejaste dicho. El comprobante está en `.criterio/terminos/` en Markdown y PDF, con SHA-256 eff52306622e7cd2… (el .md). La verificación de la configuración salió bien.

**Respuestas que tomé por defecto, porque nadie respondía:**
- El estado vive en `estado-producto/PRD-306`.
- Quien decide es «Comité de producto». Es propuesta mía: ningún documento dice quién decide.
- Ciclo mensual y próximo comité el 2026-11-12, también supuesto mío.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por |
|---|---|
| «Gerencia no tiene almacén de repuestos» | Solo la definición. La única entrevista dice «Lo necesito y hoy no lo tengo», sin decir quién ni de qué segmento. |
| volumen_mensual = 249.273 | Nada. El tablero mide 153.324 al 2026-10-12, es decir, 38.5 % menos (umbral 20 %). |
| «Retorno esperado en 24 meses» | Nada: no hay cifra, cálculo ni supuestos. |
| «El proveedor cumple el tiempo pactado» | Es un supuesto, declarado el 2026-03-24 y sin verificar hace 205 días. |

### Lo que no está dicho en ninguna parte
- **Éxito del producto:** no hay criterio de éxito.
- **Volumen mensual:** ninguno de los dos documentos define qué cuenta. Además hay un solo punto medido, así que no hay tendencia.
- **Retorno:** no se sabe de dónde sale el de 24 meses.
- **Quién decide qué se construye:** el acta no lo dice. «Se mantiene el plan» no dice qué plan.
- **Quién pidió qué:** 11 de 14 requerimientos dicen «Cliente entrevistado», pero la entrevista no nombra ninguno. Los 14 títulos son «Requerimiento REQ-46xx», sin el problema escrito.
- **Proyectos:** ningún requerimiento tiene proyecto que lo ejecute.

### Requerimientos (14: 10 aceptados, 4 propuestos)
- **10 aceptados** no tienen proyecto.
- **4 aceptados** no tienen criterio de aceptación: REQ-4603, 4605, 4607 y 4611.
- **REQ-4609** está aceptado sin evidencia de demanda.
- **REQ-4601** no tiene doliente («sin asignar»).
- **11 requerimientos** se apoyan en la entrevista de hace 12 meses, que ya está en el umbral de antigüedad.
- **3 propuestos** llevan más de 60 días sin decidirse: REQ-4606 (195 días), REQ-4612 (192) y REQ-4613 (176).

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas. Hay una sola ronda, de hace un año.
- La serie de volumen_mensual con su fuente y su definición.
- Las decisiones del comité con quién decidió. Sin eso, un requerimiento descartado se ve igual que uno que nadie miró.

**Lo que se desvió del comando:**
- `sellar` no funcionó sin una corrida abierta, así que corrí `corrida-inicio` aunque el comando dice que aquí no va.
- Hice una pasada de más para corregir el formato de los registros.
- En el archivo de salida corregí un conteo (10 pasó a 11 «Cliente entrevistado»). La copia ya registrada en `corridas/2026-10-15-product-setup-1.md` puede conservar el 10.
- La nota de la corrida dice «minutos no medidos»; el script midió 35 segundos de cálculo.

**Siguiente paso:** `/product-discovery` sobre las entrevistas, para que los temas se conviertan en requerimientos con la cita de quién los pidió.