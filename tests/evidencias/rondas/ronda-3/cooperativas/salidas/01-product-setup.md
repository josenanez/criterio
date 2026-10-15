# /criterio-product:product-setup documentos/productos/PRD-303

## Listo — Tarjeta débito (PRD-303)

**Lo que miré:** 5 documentos. Uno es de descubrimiento: una sola ronda de entrevistas, del 2025-09-12. La definición es del 2026-04-05, en el caso de negocio y en un `.docx` que leí como texto. Lo más reciente es el tablero de métricas del 2026-10-06.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.9 (términos 1.1), el 2026-10-15. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.3.9-2026-10-15.md` y `.pdf`. El SHA-256 de los términos empieza por `d31e6b3611041618…`.

**Preguntas:** nadie respondió, así que tomé la propuesta en cada una:
- **Producto:** Tarjeta débito (PRD-303), gerente Sandra Gil, según el caso de negocio.
- **Quién decide:** "Comité de producto". Es una propuesta mía, porque ningún documento lo dice. El acta solo lista como asistente a Sandra Gil.
- **Dónde se guarda:** `estado-producto/PRD-303`. No usé `estado/`, que es de otro agente.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Los Pensionados no tienen tarjeta débito | Una sola cita: «Lo necesito y hoy no lo tengo.». No dice quién habla, ni que sea pensionado, ni de qué producto | 2025-09-12 (13 meses) |
| `volumen_mensual` = 250.670 | El tablero mide 256.871, a 2,5 % de diferencia. Está bajo el umbral de 20 %: es imprecisión, no contradicción | Declarado 2026-04-05, medido 2026-10-06 |
| "Retorno esperado en 24 meses" | Nada: no hay cifra ni fuente | 2026-04-05 |
| El proveedor cumple el tiempo pactado | Un supuesto declarado y sin verificar desde hace 158 días | Declarado 2026-05-10 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** La definición no lo trae. El caso de negocio solo dice "retorno esperado en 24 meses", sin cifra.
- **Qué necesita cada requerimiento.** Los 16 se llaman "Requerimiento REQ-43xx" y ningún documento dice qué problema resuelve ninguno.
- **Quién pidió cada requerimiento.** Hay una sola cita. Doce requerimientos dicen "Cliente entrevistado", pero esa cita no nombra ninguno de ellos.
- **Qué proyecto ejecuta lo aceptado.** Hay 11 requerimientos aceptados y ninguno tiene proyecto. La definición dice "Ninguno declarado".
- **Cuál es "el plan" que el comité mantuvo el 2026-10-05.** No hay plan en la carpeta.
- **Quién aceptó los 11 requerimientos.** El acta no nombra a quien decidió.
- **Cuántos Pensionados son, y cuál es el tiempo pactado con el proveedor.** No aparecen el tamaño del segmento, el plazo ni el contrato.

### Lo que dice el registro
- Hay 16 requerimientos: 11 aceptados y 5 propuestos.
- 4 aceptados no tienen evidencia de quién los pidió: REQ-4300, 4307, 4309 y 4314.
- 11 aceptados no tienen proyecto que los ejecute.
- 4 requerimientos no tienen doliente (REQ-4303, 4309, 4313, 4314). REQ-4309 y 4314 tampoco tienen evidencia ni proyecto.
- 2 aceptados no tienen criterio de aceptación (REQ-4303 y 4305). Los demás dicen "se verifica en producción", que no se puede verificar.
- 12 requerimientos se apoyan en la misma entrevista, que tiene 13 meses.
- 5 propuestos llevan entre 82 y 175 días sin decisión. El más viejo es REQ-4306.
- De los 11 decididos, el 63,6 % tiene evidencia y el 0,0 % tiene proyecto.

### Supuestos sobre los que está escrita
La definición declara uno: "El proveedor cumple el tiempo pactado", sin verificar. No declara ninguno sobre adopción, regulación ni emisión de la tarjeta, y eso también es un hallazgo.

### Qué le falta a tu carpeta
- **Las transcripciones de las entrevistas.** Hay una sola cita, de una sola ronda, de hace 13 meses.
- **La serie de la métrica principal.** Hay un solo punto, así que no se ve tendencia.
- **Las decisiones del comité con quién decidió y por qué.** Esta acta no registra ningún requerimiento descartado. Sin esas decisiones, uno descartado se ve igual que uno que nadie miró.

### Nota sobre la corrida
`sellar` exigió una corrida abierta y que las fichas se escribieran dentro de ella, aunque el comando dice que aquí no va `corrida-inicio`. Abrí la corrida y reescribí las fichas, así que los 31 segundos medidos son de esta conversación completa. El registro de la corrida quedó en `estado-producto/PRD-303/corridas/2026-10-15-product-setup-1.md`. No se generó el HTML que el comando menciona. Corregí en la salida un error mío de tipeo en la huella.

**Después:** corre `/product-discovery` sobre las entrevistas, para que los temas se vuelvan requerimientos con la cita de quién los pidió.