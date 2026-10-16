# /criterio-product:product-setup documentos/productos/PRD-303

## Listo — Tarjeta débito (PRD-303)

**Lo que miré:** 6 documentos, todos .md y legibles. Hay una sola ronda de entrevistas (2025-09-19) con una sola cita, la definición y el caso de negocio (2025-12-27), un tablero de métricas (2026-09-29) y el acta del comité (2026-10-12).

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-15 para la versión 0.3.10 (términos 1.1). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.3.10-2026-10-15.md` y `.pdf`. Las huellas SHA-256 empiezan por `fdf0177cc54e5055…` (md) y `dcaa4cbfec5be44312…` (pdf).

**Configuración:** el estado queda en `estado-producto/PRD-303`, aparte de `estado/`, que es del portafolio. Quien decide es el Comité de producto. Tomé ese nombre del acta, porque ningún documento lo dice; confírmalo. La gerente es Natalia Ospina.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Los microempresarios no tienen tarjeta débito | Una entrevista: «Lo necesito y hoy no lo tengo.» No dice que quien habla sea microempresario | 2025-09-19 |
| Volumen mensual de 248.461 | Solo el caso de negocio. El tablero mide 202.628, un 18,4 % por debajo | 2025-12-27 / 2026-09-29 |
| Retorno esperado en 24 meses | Nada. No hay monto, tasa ni cálculo | 2025-12-27 |
| El reglamento vigente lo permite | Es un supuesto declarado y sin verificar hace 43 días | 2026-09-02 |

El 18,4 % queda bajo el umbral de 20 %, así que cuenta como imprecisión y no como contradicción.

### Lo que no está dicho en ninguna parte
- El criterio de éxito de la definición no existe.
- El retorno no tiene cifra ni origen.
- La definición dice «Propuesta principal» y nada más sobre por qué esa propuesta.
- El acta atribuye 16 de los 18 requerimientos a «Cliente entrevistado». Hay una sola cita en toda la carpeta y no dice a cuál corresponde.
- La única decisión escrita es «Se mantiene el plan». No dice quién decidió ni sobre qué.
- Ninguno de los 12 requerimientos aceptados tiene proyecto que lo ejecute.
- El problema, en palabras de quien lo tiene, no está en ninguno de los 18. Los títulos dicen solo «Requerimiento REQ-xxxx».

### Supuestos sobre los que está escrita
Hay uno: «El reglamento vigente lo permite». Si falla, tumba el producto entero.

### Qué le falta a tu carpeta
- **Transcripciones de las entrevistas:** deben decir quién habló y de qué requerimiento. Hoy toda la evidencia tiene 12 meses, y 17 de los 18 requerimientos tienen evidencia vencida.
- **Serie de la métrica principal:** hay un solo punto (2026-09-29), no una serie.
- **Decisiones del comité con su motivo:** sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.

### Lo que levanté del acta (18 requerimientos: 12 aceptados, 6 propuestos)
- **Sin proyecto que los ejecute:** 12.
- **Sin criterio de aceptación:** 2 (REQ-2030, REQ-4302).
- **Aceptado sin nadie que lo pidiera:** 1 (REQ-4301).
- **Sin doliente:** 3 (REQ-4305, REQ-4306, REQ-4314), los tres aceptados.
- **Propuestos sin decidir hace más de 60 días:** 6 (REQ-4303, 4309, 4310, 4311, 4312, 4313).
- **Numeración distinta:** REQ-2030 y REQ-2038 no siguen la serie 43xx; lo dejo anotado sin interpretarlo.

### Pendientes
- **`sellar` no corrió.** Pide una corrida abierta (`corrida-inicio`), y este comando indica no usarla. La lectura queda sin sellar.
- **Ninguna traza quedó confirmada.** No hay fichas de proyectos en `estado/records`.

La corrida quedó registrada como `2026-10-15-product-setup-1`, con la salida completa en `estado-producto/PRD-303/corridas/salida-product-setup.md`.

Siguiente paso: `/product-discovery` sobre las entrevistas.