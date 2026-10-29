# /criterio-portfolio:steering-pack 

Parto de 13 fichas (`estado/records/PRY-199` a `PRY-211`), con corte de cálculo 2026-10-28. Términos v1.3 (familia 0.12.1) vigentes, aceptados por José Francisco Ñáñez el 2026-10-28; no hubo que volver a pedirlos. Cifras derivadas: salida de `portafolio.py compute`.

# Comité de proyectos — 2026-10-28 (para el comité semanal del 2026-11-04)
7 decisiones · 6 escalamientos sin decisión asociada · 10 de 13 proyectos con hallazgos (70 señales en total)

## Decisiones del comité anterior
| Decisión | Fecha | Qué pasó | Estado |
|---|---|---|---|
| Ninguna consta | — | No hay un paquete de comité anterior en `estado/corridas`. Las minutas de comité que leí (PRY-205 del 2026-10-21, PRY-209 del 2026-10-25, PRY-206 del 2026-10-26) tratan «Avance» y «Compromisos» y no registran decisiones; la de PRY-200 (2026-10-19) no trató ningún cambio. | Sin cierre posible: el ciclo anterior no dejó decisiones escritas. |

Dos solicitudes de cambio dicen «Autorizada por el comité» (PRY-205 y PRY-209) y ninguna minuta lo recoge; van como decisión 2.

## Decisiones de hoy

### [1] ¿Se designa por escrito quién aprueba cambios y con qué umbrales de tiempo y costo, para los 13 proyectos?
**Proyecto:** todo el portafolio · **Quién decide:** no determinable; es lo que este punto resuelve. Las actas nombran un «Comité de Cambios» y una patrocinadora, sin umbrales (`identity.authority` no se encontró en los 13). · **Si no se decide hoy:** los puntos 2 a 6 no se pueden verificar contra una facultad; cualquier aprobación queda sin sustento.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Una regla única para el portafolio (umbrales de días y de COP; por encima, comité) | Ninguno | Una sesión para fijarla | Ninguno |
| B. Cada acta se enmienda con su propia autoridad | Toca 13 actas | Semanas | Ninguno |
| C. Se mantiene el Comité de Cambios como único órgano | Ninguno | Ninguno | Todo cambio, de cualquier tamaño, pasa por comité |
**Recomendación:** A. Los cambios pendientes son de 76 a 110 días y de 152 a 220 millones de COP, así que cualquier umbral razonable los deja en comité; lo que falta es la regla escrita.

### [2] ¿Ratifica el comité el CC-01 de PRY-205 y el de PRY-209, que figuran autorizados sin acta que lo recoja?
**Proyecto:** PRY-205, PRY-209 · **Quién decide:** el Comité de Cambios, según su acta; no consta que tenga la facultad para estos montos. · **Si no se decide hoy:** las líneas base se movieron (104 y 82 días) con una autorización que ningún documento sustenta, y el script las cuenta como autorizadas por lo que dice la solicitud.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ratificar ahora, con acta | Ampliación de alcance (no se describe cuál) | PRY-205 +104 días; PRY-209 +82 días | PRY-205 +208.000.000 COP; PRY-209 +164.000.000 COP |
| B. No reconocer la autorización hasta que exista acta | Sin ampliación vigente | Las líneas base vuelven a las anteriores | Sin costo adicional reconocido |
**Recomendación:** A solo con el acta escrita y con la descripción del alcance. En ambos casos quien solicitó el cambio (Diana Molina en PRY-205, Liliana Torres en PRY-209) aparece como asistente del comité que lo habría autorizado; conviene que el acta diga quién votó.

### [3] ¿Se aprueba el CC-01 de PRY-206 (ampliación de alcance, +93 días, +186.000.000 COP)?
**Proyecto:** PRY-206 · **Quién decide:** Comité de Cambios (ver punto 1) · **Si no se decide hoy:** la línea base ya se movió 93 días sin autorización (17,4 % contra la original) y el proyecto sigue en rojo.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar como está | Ampliación sin describir | +93 días | +186.000.000 COP; aprobado 4.200.000.000, proyección 4.261.219.163 |
| B. Rechazar | Sin ampliación | Se revierte el movimiento de 93 días | Sin costo adicional |
| C. Devolver hasta que describa el alcance y el motivo | Sin cambio hoy | Los 93 días siguen sin autorizar hasta decidir | Sin cambio hoy |
**Recomendación:** C, con plazo al 2026-11-04. La solicitud (Javier Hoyos, 2026-10-19) no dice qué se amplía ni por qué, y no se puede aprobar un cambio que no se sabe qué es.

### [4] ¿Se aprueba el CC-01 de PRY-208 (ampliación de alcance, +76 días, +152.000.000 COP)?
**Proyecto:** PRY-208 · **Quién decide:** Comité de Cambios (ver punto 1) · **Si no se decide hoy:** nada se rompe todavía: la línea base no se ha movido (0 días) y la solicitud es de hoy.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar como está | Ampliación sin describir | +76 días | +152.000.000 COP; aprobado 3.300.000.000, proyección 3.320.169.600 |
| B. Rechazar | Sin ampliación | Sin cambio | Sin cambio |
| C. Devolver hasta que describa el alcance y el motivo | Sin cambio hoy | Sin cambio hoy | Sin cambio hoy |
**Recomendación:** C. Mismo vacío que en el punto 3 (solicitante Felipe Arango, sin alcance ni motivo). A diferencia de PRY-206, aquí esperar no cuesta nada.

### [5] ¿Se aprueba el CC-01 de PRY-210 (ampliación de alcance, +110 días, +220.000.000 COP)?
**Proyecto:** PRY-210 · **Quién decide:** Comité de Cambios (ver punto 1) · **Si no se decide hoy:** la línea base ya se movió 110 días sin autorización (25,6 %) y la proyección de costo ya supera lo aprobado en 19,7 % (3.951.444.314 contra 3.300.000.000).
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar como está | Ampliación sin describir | +110 días | +220.000.000 COP sobre una proyección que ya excede lo aprobado |
| B. Rechazar | Sin ampliación | Se revierte el movimiento de 110 días | Se mantiene el exceso proyectado de 19,7 % |
| C. Devolver con alcance, motivo y proyección de costo actualizada | Sin cambio hoy | Los 110 días siguen sin autorizar | Sin cambio hoy |
**Recomendación:** C. No consta si los 220 millones ya están dentro de la proyección de 3.951.444.314; sin ese dato, aprobar es apostar. Solicitante: Felipe Arango, 2026-10-27, sin alcance ni motivo.

### [6] ¿Se aprueba el CC-01 de PRY-211 (ampliación de alcance, +102 días, +204.000.000 COP)?
**Proyecto:** PRY-211 · **Quién decide:** Comité de Cambios (ver punto 1) · **Si no se decide hoy:** la línea base ya se movió 102 días sin autorización (53,1 % contra la original, la mayor del portafolio) y la solicitud lleva 11 días sin presentarse.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar como está | Ampliación sin describir | +102 días | +204.000.000 COP; aprobado 3.300.000.000, proyección 3.037.162.738 (−8,0 %) |
| B. Rechazar | Sin ampliación | Se revierte el movimiento de 102 días | Sin costo adicional |
| C. Devolver con alcance, motivo y plan de recuperación | Sin cambio hoy | Los 102 días siguen sin autorizar | Sin cambio hoy |
**Recomendación:** C. El proyecto declara amarillo y 49 % con los 5 hitos marcados cumplidos y 21 señales abiertas; antes de moverle la fecha 102 días hay que saber qué es verdad del plan. Solicitante: Jorge Medina, 2026-10-17.

### [7] ¿Se congelan los pagos a proveedores que han facturado por encima de lo aceptado?
**Proyecto:** PRY-209 y PRY-211 (Obras Civiles de Telecomunicaciones), PRY-206 (Redes y Radio Andinas Ltda.) · **Quién decide:** no determinable (ver punto 1); toca a los tres gerentes y a quien aprueba pagos. · **Si no se decide hoy:** siguen pagándose facturas sin entregable aceptado.
Casos:
- PRY-209, CT-604: facturado 1.164.831.714 COP con 0 de 3 entregables aceptados; suministro de antenas y radios vencido hace 135 días y bolsa de horas hace 52.
- PRY-206, CT-381: facturado 267.686.057 COP contra 187.360.587 aceptados, diferencia 80.325.470 COP.
- PRY-211, CT-707 (mismo proveedor que PRY-209): 2 entregables vencidos y sin aceptar (216 y 145 días). El monto facturado no consta en la ficha.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Congelar pagos nuevos hasta que haya acta de recibo | Ninguno | Puede retrasar al proveedor | Protege lo ya facturado sin recibir |
| B. Seguir pagando y exigir regularización en 15 días | Ninguno | Ninguno | El exceso facturado sigue creciendo |
| C. Dejarlo a cada gerente | Ninguno | Ninguno | Sin control común sobre un proveedor que sirve a dos proyectos |
**Recomendación:** A para CT-604 y CT-381. Con CT-604 hay 1.164.831.714 facturados sin un solo entregable aceptado. Para CT-707 primero hay que traer el monto facturado.

## Escalamientos sin decisión asociada
| Proyecto | Qué | Desde cuándo | Qué se necesita |
|---|---|---|---|
| PRY-201, PRY-202, PRY-207 | Declaran verde y los documentos no lo sostienen: 51 %, 52 % y 35 % declarado contra todos sus hitos marcados cumplidos, sin evidencia de recibo en la mayoría. | Informes del 2026-10-17, 2026-10-25 y 2026-10-20 | Evidencia de cada hito o corregir el estado declarado |
| PRY-200 | 59 % y amarillo con 5 de 5 hitos «cumplidos»; 4 sin evidencia (el más viejo, 465 días). Entregables de proveedores vencidos 398 y 346 días; CT-478 con bolsa de horas aceptada sin evidencia. Compromiso de Carlos Peña vencido 22 días. | Hitos vencidos desde 2025-07-20 | Evidencia de los hitos; fecha real de salida (hay una solicitud de +30 días en la corrida `change-control` de hoy que no está en la ficha, sin solicitante ni motivo) |
| PRY-201 | Infraestructura de Torres del Sur (CT-801): 3 entregables vencidos (324, 222 y 121 días), 0 aceptados. | 2025-12-08 | Estado real del contrato con el proveedor |
| PRY-211 | 6 compromisos vencidos y 7 reprogramados; uno de ellos 6 veces (Gustavo Neira, «Enviar el documento 1», original 2026-09-20, hoy 2026-12-26). | 2026-09-20 | Doliente que responda por la agenda del proyecto |
| PRY-209 | Variación de tiempo de 82 días (27,2 %) autorizada, con 87 % declarado y hito «Sitios construidos» cumplido sin evidencia (37 días). | 2026-09-21 | Acta de recibo del hito |
| PRY-204 | Rojo declarado, 38 %, hito «Diseño de red aprobado» sin evidencia (125 días) y compromiso de Jorge Medina vencido 8 días. | 2026-06-25 | Evidencia del hito; quién destraba el compromiso |

## Para conocimiento
- PRY-199: verde, 20 %, sin señales. PRY-203: amarillo, 59 %, sin señales. PRY-208: amarillo, 79 %, sin señales salvo el cambio del punto 4.
- PRY-205: rojo, 48 %; 104 días de variación (22,8 %) y un hito sin evidencia; ver punto 2.

## Anexo
**Señales por proyecto** (suma 70): PRY-211 21 · PRY-200 10 · PRY-201 9 · PRY-202 6 · PRY-210 6 · PRY-206 5 · PRY-209 5 · PRY-207 4 · PRY-204 2 · PRY-205 2 · PRY-199, PRY-203, PRY-208 0.

**Estado declarado** (con fecha del informe): PRY-199 verde 20 % (2026-10-26) · PRY-200 amarillo 59 % (2026-10-17) · PRY-201 verde 51 % (2026-10-17) · PRY-202 verde 52 % (2026-10-25) · PRY-203 amarillo 59 % (2026-10-18) · PRY-204 rojo 38 % (2026-10-26) · PRY-205 rojo 48 % (2026-10-23) · PRY-206 rojo 65 % (2026-10-25) · PRY-207 verde 35 % (2026-10-20) · PRY-208 amarillo 79 % (2026-10-21) · PRY-209 amarillo 87 % (2026-10-26) · PRY-210 rojo 50 % (2026-10-28) · PRY-211 amarillo 49 % (2026-10-28).

**Verdes contradichos:** 3 (PRY-201, PRY-202, PRY-207).

**Vacíos de información:**
- Autoridad de aprobación: no consta en ningún acta (13 de 13). Fase: falta en las 13 fichas. Producto: falta en PRY-202, 203, 205, 206, 207, 209 y 210.
- Las seis solicitudes de cambio dicen «Ampliación de alcance» sin describir qué se amplía y ninguna da motivo.
- PRY-206 y PRY-210 declaran 65 % y 50 % cuando el plan sustenta entre 20 % y 40 %: van adelantados, y con un solo hito cumplido; contradice su estado rojo y los cambios de fecha. No lo resuelvo.
- PRY-199, PRY-201 y PRY-211: el facturado del proveedor no consta.
- No leí el registro RAID ni las dependencias entre proyectos: la ficha de dependencias está vacía en los 13, así que «ningún proyecto afecta a otro» es ausencia de dato, no un hallazgo. No evalué «dos períodos sin movimiento» ni «mitigación vencida».
- No hay conflictos entre documentos registrados por el script en ninguna ficha.
- Las minutas que leí son las de PRY-205, PRY-206 y PRY-209; el resto de minutas lo reflejan solo mediante las señales del script.

---
criterio-portfolio · familia 0.12.1 · términos v1.3 aceptados el 2026-10-28 por José Francisco Ñáñez · aplicados los criterios de escalamiento y de decisión descritos en el comando (no cargué por separado los skills raid-taxonomy y governance-artifacts) · 13 fichas con corte 2026-10-28 · campos inciertos: autoridad, fase, producto, alcance de los cambios, facturado de PRY-199/201/211 · términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.12.1

---
**Después:** una vez sesione el comité, puedo registrar sus decisiones en las fichas. Ahí se cierra el ciclo y el material del próximo comité empieza a armarse solo.

La corrida quedó registrada como `2026-10-28-steering-pack-1` y tardó 113 segundos. El texto de arriba es lo que guardé en `estado/corridas/salida-steering-pack.md`.