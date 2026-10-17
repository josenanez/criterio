# /criterio-product:product-setup documentos/productos/PRD-304

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

Al ser una sesión sin interfaz, tomé la respuesta sugerida en cada pregunta.

**Qué encontré en `documentos/productos/PRD-304`:** 5 documentos y ninguno que no pueda leer.
- **Descubrimiento:** una sola ronda de entrevistas (2025-10-15), con una cita.
- **Definición:** caso de negocio y definición escrita, ambos del 2025-09-15.
- **Gobierno:** un anexo de verificación de un supuesto (2026-09-26) y el acta del comité de producto (2026-09-16, .docx).
- **Lo más reciente:** el anexo, del 2026-09-26.

**Preguntas:**
1. **Quién eres y qué producto es:** Andrés Lozano, gerente de PRD-304 «Trazabilidad».
2. **Quién decide qué se construye:** «Comité de producto». Ningún documento lo dice; el acta solo lista a Andrés Lozano como asistente.
3. **Dónde guardo lo que encuentre:** `estado-producto/PRD-304`. No toco la carpeta `estado/` que ya existe.
4. **Términos (versión 1.1):**
> Criterio produce borradores de trabajo, no decisiones ni asesoría. Procesa los documentos que usted le indique y dice lo que muestran; no sabe lo que se habló fuera de ellos. Puede equivocarse, y por eso cada dato viene con la cita del documento de donde salió: la verificación es suya. Sus documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo. Cada versión se certifica antes de publicarse; garantía y responsabilidad: licencia Apache 2.0. Cada versión se acepta de nuevo y deja un comprobante en Markdown y PDF con su huella SHA-256. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

La aceptación quedó registrada a nombre de José Francisco Ñáñez, con la instrucción de esta prueba (2026-10-17).

## Listo — Trazabilidad (PRD-304)

**Lo que miré:** 5 documentos · 1 de descubrimiento · la definición del 2025-09-15
**Términos:** aceptados para la versión 0.3.13 (términos 1.1) · comprobante en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf` · SHA-256 d85e8bd2335ac89a…

**Registro levantado:** `producto.json` y 16 requerimientos del acta (11 aceptados, 5 propuestos). Solo lo escrito; lo que ningún documento dice quedó en `not_found`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Operadores no tiene trazabilidad» | Una sola cita: «Lo necesito y hoy no lo tengo», de un cliente sin nombre. No dice que sea Operador ni nombra trazabilidad. Sostenida, pero débil | 2025-10-15 (12 meses) |
| Volumen mensual 240.425 | Solo el caso de negocio, que se cita a sí mismo como fuente. No hay serie medida | 2025-09-15 |
| «Retorno esperado en 24 meses» | Nada: sin cifra, sin base y sin fuente | 2025-09-15 |
| «Operaciones adopta la herramienta» (supuesto) | Un anexo que dice «se confirmó» con la medición del piloto del 2026-09-26. Esa medición no está en la carpeta | 2026-09-26 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** Sin él el producto no se puede cerrar contra nada.
- **La propuesta.** La definición dice solo «Propuesta principal», un texto de relleno.
- **Cualquier medición del volumen mensual (240.425).** Nadie está midiendo lo que el negocio afirmó.
- **Qué respalda el retorno a 24 meses.**
- **La medición del piloto** que, según el anexo, confirmó el supuesto.
- **Quién decide qué se construye.** El acta solo dice «Se mantiene el plan».
- **El proyecto que ejecuta cada requerimiento.** La definición dice «Ninguno declarado» y el acta no pone proyecto en ninguna fila.

### Lo que sale del registro (cifras del cálculo, hoy 2026-10-17)
- **11 de 11** aceptados siguen sin proyecto que los ejecute (0 % con traza).
- **14 de 16** requerimientos tienen evidencia con 12 meses de antigüedad (umbral: 12). La única entrevista es del 2025-10-15, justo en el umbral.
- **9 de 11** aceptados tienen evidencia de demanda (81,8 %). **2 no tienen ninguna** (REQ-4401 y REQ-4414).
- **5 aceptados sin criterio de aceptación** (REQ-4400, 4402, 4404, 4410, 4414). En los demás el criterio es «se verifica en producción», que dice dónde se mira, no qué se mide.
- **3 requerimientos sin doliente** (REQ-4400, 4405, 4414).
- **5 propuestos sin decidir** hace más de 60 días (REQ-4405, 4407, 4408, 4411, 4415).
- Las 14 filas del acta con «Cliente entrevistado» como quien lo pidió se apoyan en **la misma cita anónima**. La entrevista no nombra ninguno de esos requerimientos.

### Supuestos sobre los que está escrita
Uno declarado: «Operaciones adopta la herramienta» (declarado el 2026-07-24).
- La definición está fechada 2025-09-15 pero contiene un supuesto declarado diez meses después, así que el documento se editó sin cambiar su fecha.
- El supuesto habla de «Operaciones» y el segmento del problema es «Operadores». El documento no dice si son lo mismo.

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas: hay una ronda con una cita.
- La serie de la métrica principal (volumen mensual) con su fuente.
- La medición del piloto del 2026-09-26.
- Las decisiones del comité con quién decidió. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.

### Después
Si quieres, `/product-discovery` sobre el material de entrevistas: ahí los temas se vuelven requerimientos con la cita de quién lo pidió.

**Notas de la corrida**
- **Corrida abierta:** el comando dice que aquí no va `corrida-inicio`, pero `sellar` se niega a sellar sin una corrida abierta. La abrí, reescribí la ficha y sellé. Por eso el tiempo medido es de 25 segundos y no el de la conversación.
- **Corrida registrada dos veces:** la primera salida decía «15 filas» donde son 14. Corregí el texto y volví a registrar, así que hay dos entradas: `2026-10-17-product-setup-1` y `-2`. La segunda es la buena.
- **Dónde quedó todo:**
  - Configuración: `.criterio/producto/PRD-304/config.json`. La verificación da `ok: true`.
  - Estado: `estado-producto/PRD-304/`.
  - Salida completa: `estado-producto/PRD-304/corridas/salida-product-setup.md`.