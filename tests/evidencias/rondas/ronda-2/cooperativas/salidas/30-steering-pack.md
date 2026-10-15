# /criterio-portfolio:steering-pack 

Material de comité listo y corrida registrada (`2026-10-15-steering-pack-1`, 184 s medidos por la corrida, 13 proyectos). Lo de abajo es el contenido de `estado/corridas/salida-steering-pack.md`.

Una cosa del proceso: en una llamada usé `cd` dentro de un bucle de lectura de minutas, contra la instrucción de no usarlo.

---

**Términos:** vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15). Comprobante: `.criterio/terminos/aceptacion-criterio-portfolio-0.3.8-2026-10-15.md` y `.pdf`. Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.8

**Fichas cargadas:** las 13 de `estado/records` (PRY-199 a PRY-211), con cifras recalculadas por `compute` al 2026-10-15. Hoy no hay ficha de producto ni ficha de comité previo.

# Comité de proyectos — 2026-10-22 (preparado el 2026-10-15)
6 decisiones · 6 escalamientos · 12 de 13 proyectos con hallazgos

**Aviso previo:** ninguno de los 13 proyectos tiene autoridad de aprobación documentada. Por eso el punto 1 va primero. Los puntos 2 a 6 quedan como propuestas hasta que se resuelva.

## Decisiones del comité anterior
| Decisión | Fecha | Qué pasó | Estado |
|---|---|---|---|
| Sin registro | — | No hay acta ni material de un comité de portafolio anterior en `documentos` ni en `estado`. Las solicitudes de cambio dicen "Autorizada por el comité" sin nombrar cuál ni citar acta. | **No se puede cerrar el ciclo.** Lo que se decidió antes no consta. |

## Decisiones de hoy

### [1] ¿Quién tiene la facultad de aprobar cambios de línea base, sobrecostos y pagos sin aceptación, y en qué cuerpo?
**Proyecto:** los 13 · **Quién decide:** no consta en ningún documento. Esa es la pregunta. · **Si no se decide hoy:** los puntos 2 a 6 no tienen destinatario válido y se devuelven. Los cambios y pagos siguen "autorizados" por un comité sin nombre.

Hoy los proyectos citan cuerpos distintos: Consejo de Administración (PRY-199, PRY-210), Comité de Riesgos (PRY-200, PRY-201, PRY-203, PRY-211), Comité de Crédito (PRY-206) y Comité de Educación (PRY-205).

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Este comité aprueba lo que exceda los umbrales (10 % de tiempo o costo) y lo que cruce proyectos | Sin cambio | Una instancia única decide | Sin costo directo |
| B. Cada proyecto conserva su comité, y cada acta nombra qué aprueba | Sin cambio | Más lento al cruzar proyectos | Sin costo directo |
| C. No definir | — | — | — |

**Recomendación:** A para lo que exceda los umbrales o cruce proyectos, y B para el resto. En ambos casos el cuerpo queda escrito en el acta y en la ficha. Sin eso, "autorizada por el comité" no se puede verificar.

### [2] ¿Se ratifican los cambios PRY-208 CC-01 y PRY-210 CC-02, aprobados sin nueva línea base, y se ordena registrarla?
**Proyecto:** PRY-208, PRY-210 · **Quién decide:** pendiente del punto 1. · **Si no se decide hoy:** los dos proyectos se miden contra una línea base que ya no es la que dicen haber aprobado.

El script marca ambos como `change_without_baseline`: PRY-208 CC-01 y PRY-210 CC-02. Los dos dicen "Autorizada por el comité" y no hay acta en la carpeta. Lo mismo ocurre con PRY-200 CC-01 y PRY-210 CC-01, que sí movieron la línea base.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ratificar y registrar nueva línea base | Ampliado (la solicitud solo dice "Ampliación de alcance", sin detalle) | PRY-208 +113 días; PRY-210 CC-02 +101 días | PRY-208 226.000.000 COP; PRY-210 CC-02 202.000.000 COP |
| B. Devolver hasta que conste el acta de autorización | Sin ampliar mientras tanto | Sin cambio | Sin cambio |
| C. Rechazar | Sin ampliar | Sin cambio | Sin cambio |

**Recomendación:** B, salvo que alguien en la sala confirme que este comité los autorizó. En ese caso, A con el acta. No hay evidencia de quién autorizó, y dos de los cuatro cambios siguen sin línea base nueva.

### [3] ¿Qué se hace con los tres proyectos cuya proyección supera lo aprobado en más de 10 %?
**Proyecto:** PRY-204, PRY-207, PRY-209 · **Quién decide:** pendiente del punto 1. · **Si no se decide hoy:** los proyectos siguen comprometiendo presupuesto contra una cifra que su propia proyección ya excede.

| Proyecto | Aprobado COP | Proyección COP | Desviación | Estado declarado |
|---|---|---|---|---|
| PRY-204 Tarjeta débito | 6.800.000.000 | 7.967.490.454 | 17,2 % | amarillo, 73 % |
| PRY-207 Microcrédito rural | 3.300.000.000 | 4.254.910.977 | 28,9 % | verde, 91 % |
| PRY-209 Convenios de libranza | 3.300.000.000 | 4.235.779.323 | 28,4 % | verde, 41 % |

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ampliar presupuesto hasta la proyección | Sin cambio | Sin cambio | Hasta las cifras de la tabla |
| B. Mantener lo aprobado y recortar alcance | Recorte que ningún documento dimensiona | No estimado | Tope en lo aprobado |
| C. Diferir con re-estimación sustentada por proyecto antes del comité siguiente | Sin cambio | Una semana de espera | Sin cambio |

**Recomendación:** C para los tres. El avance que sustenta la petición no tiene evidencia:
- **PRY-204:** 3 de 3 hitos declarados cumplidos sin acta de recibo.
- **PRY-207:** declara 91 % cuando el plan sostiene entre 50 y 75 %, tiene un hito vencido hace 5 días y está en verde.
- **PRY-209:** no hay cronograma en la carpeta, así que no se puede contrastar el avance.

Aprobar dinero adicional sobre eso es aprobar sobre la declaración del gerente.

### [4] ¿Se retienen los pagos de facturas radicadas sin acta de recibo?
**Proyecto:** PRY-201, PRY-202, PRY-206 · **Quién decide:** pendiente del punto 1. La condición de pago de CT-683 pide acta firmada por el gerente del proyecto. · **Si no se decide hoy:** las facturas siguen radicadas en cuentas por pagar y el pago queda a criterio de quien lo procese.

- **PRY-201, CT-683 (Soluciones Solidarias):** FV-1683 por 121.861.832 COP, radicada el 2026-09-06. Cero entregables aceptados. Los dos están vencidos: licenciamiento hace 245 días y bolsa de horas hace 157.
- **PRY-206, CT-319 (Integración Financiera del Sur):** facturado 73.545.581 COP contra 55.571.557 aceptados; diferencia 17.974.024 COP. En CT-319 y CT-583 el licenciamiento figura "aceptado" sin acta.
- **PRY-202, CT-665 (Sistemas Cooperativos):** FV-2665 por 96.527.977 COP. El licenciamiento figura "aceptado" sin acta. CT-527 sí tiene acta de recibo (2026-08-09).

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Pagar lo radicado | Sin cambio | Sin cambio | Se desembolsa lo facturado sin aceptación |
| B. Retener hasta acta de recibo | Sin cambio | El proveedor puede reclamar mora; los contratos leídos no fijan cláusula | Sin desembolso mientras tanto |
| C. Pagar y abrir reclamo | Sin cambio | Sin cambio | Se desembolsa y se recupera por reclamo |

**Recomendación:** B. La condición de pago del contrato que sí leí (CT-683) exige el acta. Para PRY-202 y PRY-206, pedir primero el acta que debería existir y retener solo la diferencia mientras no aparezca.

### [5] ¿Se adopta la regla de que un hito solo cuenta como cumplido con acta de recibo, y de que un estado verde no se acepta con señales abiertas?
**Proyecto:** portafolio · **Quién decide:** pendiente del punto 1. · **Si no se decide hoy:** los informes siguen mostrando avance que ningún documento sostiene.

El script cuenta 5 proyectos en verde contradichos por la evidencia: PRY-201, PRY-202, PRY-207, PRY-209, PRY-211. Hay hitos declarados cumplidos sin acta en PRY-200, PRY-201, PRY-202, PRY-203, PRY-204, PRY-207, PRY-210 y PRY-211. Los dos casos más claros:
- **PRY-201:** 5 de 5 hitos "cumplidos" sin acta y avance declarado 47 %.
- **PRY-200:** 5 de 5 hitos declarados cumplidos, avance 53 % y fin vigente 2026-10-18.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Regla vigente desde hoy; los hitos sin acta se reclasifican como "declarados" | Sin cambio | Los gerentes adjuntan actas o reabren hitos esta semana | Sin costo directo |
| B. Regla desde el próximo período | Sin cambio | Sin presión inmediata | El avance reportado seguirá inflado un período más |
| C. No adoptar | — | — | — |

**Recomendación:** A. Hay actas de recibo en la carpeta (por ejemplo PRY-199, PRY-206, PRY-207 y PRY-200 en algunos hitos), así que el mecanismo existe. Lo que falta es exigirlo.

### [6] ¿Cuál es la fecha fin vigente de PRY-203: 2026-09-03 o 2026-10-15?
**Proyecto:** PRY-203 Aportes sociales en línea · **Quién decide:** el Comité de Riesgos, que según el acta aprobó la línea base inicial (a confirmar con el punto 1). · **Si no se decide hoy:** el proyecto, declarado en rojo con 34 %, sigue con dos fechas fin y ninguna medición de atraso es defendible.

El acta de constitución (2025-09-22) dice 2026-10-15. El cronograma v1 (misma fecha de documento) dice 2026-09-03. Ningún documento es más reciente. El plan marca 4 de 4 hitos cumplidos sin acta y el piloto vencía el 2026-09-03.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Fin vigente 2026-10-15 (el acta) | Sin cambio | Vence hoy; con 34 % declarado no llega | Presupuesto aprobado 4.200.000.000 COP; proyección 3.996.935.557 COP |
| B. Fin vigente 2026-09-03 (el cronograma) | Sin cambio | Ya vencido | Igual |
| C. Aceptar A y abrir solicitud de cambio con fecha nueva sustentada | Sin cambio | El comité fija la fecha | A determinar con "el ajuste del presupuesto" que Laura Vélez quedó de enviar sin fecha |

**Recomendación:** C. El acta es el instrumento de aprobación y el cronograma es derivado, pero con 34 % de avance ninguna de las dos fechas es alcanzable. Hace falta una fecha nueva con sustento y no una disputa entre dos fechas viejas.

## Escalamientos sin decisión asociada
| Proyecto | Qué | Desde cuándo | Qué se necesita |
|---|---|---|---|
| PRY-202 Core cooperativo | Silencio de 18 días (umbral 15); hito "Ambiente de pruebas certificado" vencido hace 11 días; declara verde. PRY-205 lo nombra como dependencia ("proveedor del core cooperativo"). Los hitos "Integración con el core" de PRY-200, 201, 203, 204 y 207 dependen del mismo core, pero ninguna ficha declara la dependencia. | Silencio desde 2026-09-27 | Que el gerente responda con fecha. Que se declaren las dependencias entre fichas. |
| PRY-204, PRY-205, PRY-208 | Los tres listan como riesgo abierto la "Aprobación del reglamento por el Consejo de Administración". PRY-208 informa que el Consejo pidió ajustarlo antes del piloto. | Sin fecha en los documentos | Fecha de sesión del Consejo y responsable del ajuste. |
| PRY-200 | Proveedor Talento Solidario (CT-992): 3 entregables vencidos hace 287, 222 y 157 días, cero aceptados, cero facturado. El informe de avance no menciona al proveedor. | Desde 2026-01-01 | Contacto de escalamiento con el proveedor y fecha comprometida o decisión contractual. |
| PRY-203 | Se comentó en la reunión del 2026-10-15 que el proveedor podría no llegar con el equipo completo y nadie lo registró. El informe lista que el proveedor no ha confirmado la última entrega. Además, el ajuste de presupuesto de Laura Vélez ("la otra semana") no tiene fecha. | 2026-10-15 | Registrar el riesgo con dueño y fecha. Fecha para el ajuste. |
| PRY-210 | Rojo, 177 días contra la línea original (74,1 %), avance 35 % contra 67–100 % del plan. Compromiso de Rubén Cárdenas ("punto 12") vencido hace 8 días. | Compromiso vencido desde 2026-10-07 | Evidencia de entrega o nueva fecha. Ver punto 2 por CC-02. |
| Compromisos vencidos | Carlos Peña: PRY-201 "punto 12" (18 días), PRY-203 "punto 2" (4 días). María Restrepo: PRY-206 "punto 15" (18 días); en PRY-205 su "punto 2" no tiene fecha. | Desde 2026-09-27 y 2026-10-11 | Evidencia de entrega o nueva fecha. El "punto N" no dice qué se entrega y las minutas no lo describen. |

## Para conocimiento
- **PRY-199** Cambio de mobiliario: verde, 20 %, sin señales del script. Fin 2027-12-14.
- **PRY-200** Crédito de libranza digital: amarillo, 53 %, 118 días (49,8 %) contra la línea original por CC-01. Ver puntos 2 y 5.
- **PRY-201** Apertura de ahorro: verde declarado, contradicho por 5 señales. Ver puntos 4 y 5.
- **PRY-202** Core cooperativo: verde declarado, silencioso. Ver escalamientos.
- **PRY-203** Aportes sociales: rojo, 34 %. Ver punto 6.
- **PRY-204** Tarjeta débito: amarillo, 73 %, sobrecosto 17,2 %. Ver punto 3.
- **PRY-205** Prevención de lavado de activos: rojo, 27 %, consistente con el plan (0–25 %). El informe no pide ninguna decisión.
- **PRY-206** Pagos con QR: amarillo, 43 %. Ver punto 4.
- **PRY-207** Microcrédito rural: verde declarado, sobrecosto 28,9 %, hito vencido. Ver puntos 3 y 5.
- **PRY-208** Motor de crédito: amarillo, 58 %. Ver punto 2.
- **PRY-209** Convenios de libranza: verde declarado, sobrecosto 28,4 %, sin cronograma. Ver punto 3.
- **PRY-210** Corresponsales rurales: rojo, 35 %. Ver escalamientos y punto 2.
- **PRY-211** Cobranza digital: verde declarado, 65 %, 2 hitos sin acta. Ver punto 5.

## Anexo

**Estado por proyecto** (declarado → lo que sostienen los documentos): ver "Para conocimiento". Las cifras vienen de `compute` del 2026-10-15. Totales: 13 proyectos, 12 con alertas, 59 alertas, 5 verdes contradichos, 8 productos, 13 sin autoridad documentada.

**Contradicciones abiertas**
- **PRY-203:** fin del plan 2026-10-15 (acta) contra 2026-09-03 (cronograma), mismo día de documento, sin ganador. Ver punto 6.
- **PRY-210:** el script reporta 177 días movidos en la línea base y a la vez CC-02 (+101) "sin nueva línea base". El cronograma v3 es del 2026-10-06 y CC-02 es del 2026-10-12. No sé cuál de las dos lecturas es la correcta. Se pide verificar contra el cronograma.
- **PRY-205 y PRY-208:** ejecutado mayor que comprometido (PRY-205: 3.928.364.439 contra 2.805.154.469; PRY-208: 1.497.208.124 contra 1.006.828.323). Lo ejecutado debería estar dentro de lo comprometido. Es un dato del informe de avance o una definición distinta de "comprometido"; no se pudo resolver.

**Vacíos de información**
- **Autoridad:** ningún proyecto la tiene documentada (13 de 13). La fase tampoco consta.
- **Campos antiguos** (12 a 13 meses, fuente de septiembre y octubre de 2025) en PRY-200, PRY-203, PRY-204 y PRY-208.
- **Comité previo:** sin acta que cerrar. Ninguna solicitud de cambio cita acta.
- **PRY-209:** sin cronograma, así que no hay contraste de avance contra plan.
- **PRY-203:** ficha del gerente sin estado, avance ni presupuesto comprometido, ejecutado o proyección. Sí tiene informe de avance; la ficha no lo incorpora.
- **Pagos:** no consta si las facturas radicadas ya se pagaron. Solo dicen "radicada en cuentas por pagar".
- **Lectura:** en esta corrida leí los informes, minutas, solicitudes de cambio y facturas citados. Los cronogramas `.xlsx` y los `.docx` los tomé de las fichas ya construidas, no los releí.
- **Cifras derivadas:** las sumas por costo de cambios y las diferencias de sobrecosto no se calcularon porque el script no las entrega.

---
**Pie:** criterio-portfolio versión 0.3.8, términos 1.1 aceptados el 2026-10-15. Fichas aplicadas: 13 (PRY-199 a PRY-211), cálculo del 2026-10-15. Campos inciertos: autoridad (13/13), fecha fin de PRY-203, línea base de PRY-210 tras CC-02, ejecutado contra comprometido en PRY-205 y PRY-208, y estado de pago de las facturas. Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.8

---

**Después:** cuando el comité sesione, puedo registrar sus decisiones en las fichas. Así el material del próximo comité ya trae el ciclo cerrado.

Dos advertencias sobre la corrida registrada:
- **Documentos leídos:** `documentos` salió sin medir (`null`), porque el script no lo mide en este comando. La nota de la corrida sí dice qué no releí (los `.xlsx` y `.docx`).
- **Sin respuestas:** como era una sesión sin interfaz, no hubo preguntas que contestar; el único dato que pedía alguien era el nombre para los términos, y ya estaban vigentes.