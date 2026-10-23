# /criterio-portfolio:raid-log portafolio

## RAID — Portafolio de proyectos (13 proyectos) al 2026-10-23

Terminos: ya estaban vigentes (aceptados por José Francisco Ñáñez, v0.8.0), así que no hubo que registrarlos de nuevo.

**De qué documentos sale.**
- **RAID ya registrado:** las 13 fichas, tomadas de los informes de avance (cortes 2026-10-12 a 2026-10-22).
- **Leídos para esta corrida:** las 13 actas de constitución (sección «Dependencias declaradas»), las 12 minutas de comité, las notas de reunión de PRY-204 del 2026-10-22 y el informe de avance de PRY-204.
- **No releídos:** los otros 12 informes de avance. Sus ítems vienen de la ficha.

**Escala.** La configuración no define escala de probabilidad e impacto. Se usaría alta/media/baja, pero ningún ítem trae valoración y no se inventó ninguna.

**6 riesgos · 0 supuestos · 17 incidencias · 12 dependencias (35 ítems)**
35 sin doliente · 35 sin fecha · 35 sin dato de movimiento · 1 no registrado formalmente

Los ids (`199-R1`, `204-D2`…) son de este informe; las fichas no traen ids de RAID. R es riesgo, I es incidencia y D es dependencia.

### Reclasificados, y por qué
Doce ítems estaban como riesgo en los informes y pasan a dependencia, por la prueba rápida: si depende de alguien fuera del proyecto, es dependencia.
- **«El proveedor no ha confirmado la fecha de la última entrega»** (200, 201, 204, 206, 207, 210): la entrega es de un tercero y el propio texto dice que no está confirmada.
- **«Ventana de parada de planta definida por operaciones»** (202, 204, 207, 208, 209, 211): la ventana la fija Operaciones, no el proyecto.

Ninguna lleva código de proyecto, porque la contraparte es un proveedor u Operaciones, no otro proyecto del portafolio. Es criterio mío: si el gerente lo ve distinto, se devuelven a riesgo.

### Necesitan decisión ahora
Ningún ítem cumple de forma demostrable un criterio de escalamiento:
- No hay fecha de último movimiento, así que no se puede probar «más de dos períodos sin movimiento».
- No hay mitigaciones registradas, así que no hay una vencida.
- Ninguna dependencia apunta a otro proyecto.

Estos dos casos necesitan decisión por otras razones:

| Id | Tipo | Qué | Doliente | Desde | Por qué sube |
|---|---|---|---|---|---|
| 200-I1, 201-I2, 203-I1, 206-I1, 207-I3 | Incidencia | Hallazgo en la auditoría de seguridad | no consta | no consta | Hallazgo de seguridad abierto en cinco proyectos, sin doliente ni fecha. Cuatro de los cinco declaran verde. |
| 204-R1 | Riesgo | El proveedor podría no llegar con el equipo completo para la siguiente fase | `no_identificado` | 2026-10-22 | Dicho en reunión y nadie lo anotó. Hay que decidir si se formaliza y quién lo lleva. |

### Detectados en reuniones, no registrados
| Qué | Tipo | Dicho en | Fecha |
|---|---|---|---|
| «Se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase, nadie lo anotó como riesgo» | Riesgo (también tiene forma de dependencia del proveedor) | `PRY-204-monitoreo-de-taludes/2026-10-22-notas-reunion.txt` | 2026-10-22 |

Es el único. Las otras 11 minutas traen solo temas y compromisos.
- La nota no dice quién lo comentó.
- En esa misma reunión, «Óscar Ramírez: revisión con el proveedor, queda para el 2026-11-01». La nota no lo une a este riesgo, así que no afirmo que sea su mitigación.
- La nota tampoco nombra al proveedor. La ficha de PRY-204 lista dos: Geotecnia Aplicada S.A.S. y Montajes Industriales Ltda.

### Sin doliente o sin fecha
Los 35 ítems carecen de ambos y no se rellenó ninguno.

| Proyecto | Ítems |
|---|---:|
| PRY-199 | 2 |
| PRY-200 | 2 |
| PRY-201 | 4 |
| PRY-202 | 4 |
| PRY-203 | 2 |
| PRY-204 | 5 (204-R1 con doliente `no_identificado`) |
| PRY-205 | 1 |
| PRY-206 | 4 |
| PRY-207 | 5 |
| PRY-208 | 1 |
| PRY-209 | 1 |
| PRY-210 | 3 |
| PRY-211 | 1 |

### Dependencias en riesgo
Ningún proyecto declara dependencia de otro: las 13 actas dicen «Ninguna declarada». El cruce entre proyectos no tiene nada que cruzar. Eso no prueba que no existan dependencias, solo que nadie las declaró. Sí hay 12 dependencias de terceros:

| Id | Depende de | Confirmada | Qué pasó |
|---|---|---|---|
| 200-D1, 201-D1, 204-D1, 206-D1, 207-D1, 210-D1 | Proveedor (sin nombre en el informe) | No: «no ha confirmado la fecha de la última entrega» | Declarada, no acordada. |
| 202-D1, 204-D2, 207-D2, 208-D1, 209-D1, 211-D1 | Operaciones (ventana de parada de planta) | No consta | El informe no dice si Operaciones ya fijó la ventana. |

La frase del proveedor aparece palabra por palabra en seis informes. Con estos documentos no se sabe si es el mismo proveedor ni el mismo asunto.

### Incongruencias que afectan la lectura de las incidencias
- **Lluvias y montaje.** «Las lluvias detuvieron el montaje durante diez días» figura en 199, 201, 202, 204 y 207.
  - El cronograma ubica el montaje en 2027-09-03 (199), 2027-05-06 (204) y 2027-03-28 (207). El de 201 no tiene hito de montaje.
  - Un montaje que parece no haber empezado no pudo detenerse. O la incidencia está mal descrita o el cronograma no refleja lo que se hace. No lo corregí: hay que preguntarlo a cada gerente.
- **Verde con incidencias abiertas.** Hay 17 incidencias abiertas en 9 proyectos, pero 11 de los 13 declaran verde (207 rojo, 210 amarillo).
- **Frases idénticas entre proyectos.** Hallazgo de auditoría ×5, ensayo de disponibilidad ×4, rotación de ingeniero ×3. Puede ser coincidencia o texto copiado entre informes; los documentos no lo aclaran.

### Registro completo
El archivo `estado/corridas/salida-raid-log.md` trae las 35 filas con Id, Tipo, Qué, Prob., Impacto, Doliente, Fecha y Último movimiento. Prob., Impacto, Doliente, Fecha y Último movimiento dicen «no consta» en todos, tal como vienen las fichas. Por proyecto:

| Proyecto | Ítems |
|---|---|
| 199 | R1 concentración del conocimiento; I1 lluvias |
| 200 | D1 proveedor; I1 auditoría |
| 201 | D1 proveedor; I1 ensayo; I2 auditoría; I3 lluvias |
| 202 | D1 ventana; R1 licencia ambiental; I1 lluvias; I2 rotación |
| 203 | R1 licencia ambiental; I1 auditoría |
| 204 | D1 proveedor; D2 ventana; R1 proveedor con equipo completo (no registrado); I1 ensayo; I2 lluvias |
| 205 | R1 concentración del conocimiento |
| 206 | R1 bloqueo de la vía de acceso; D1 proveedor; I1 auditoría; I2 ensayo |
| 207 | D1 proveedor; D2 ventana; I1 rotación; I2 lluvias; I3 auditoría |
| 208 | D1 ventana |
| 209 | D1 ventana |
| 210 | D1 proveedor; I1 ensayo; I2 rotación |
| 211 | D1 ventana |

### Lo que este registro no sabe
- **Supuestos: cero.** Ningún documento los declara. Los candidatos habituales (persona clave, proveedor a tiempo, ventana de planta, licencia) aparecen hoy como riesgos o dependencias.
- **Movimiento:** las fichas no guardan cuándo se movió cada ítem y hay una sola corrida de estado, así que «dos períodos sin movimiento» no se puede evaluar. Se podrá desde la próxima corrida.
- **Mitigaciones:** ninguna registrada.
- Lo que se habló fuera de estos documentos no está aquí.

### Siguiente paso, si lo quieres
- Subir a comité los hallazgos de auditoría de seguridad sin doliente (200, 201, 203, 206, 207), con la decisión formulada: «¿quién es el doliente de cada uno y para qué fecha se cierra?».
- Proponer doliente para los 35 ítems. Es una propuesta, no una asignación: el gerente de cada proyecto es el candidato natural, pero lo decide cada comité.
- Pedir a cada gerente que formalice o descarte 204-R1.

---
Rigor: cada ítem cita el documento de donde sale y nada se rellenó; lo que falta figura como «no consta». La reclasificación de 12 ítems es criterio mío. Este borrador no sustituye la decisión del gerente ni del comité, y la verificación contra los documentos es tuya.

La corrida quedó registrada como `2026-10-23-raid-log-1` (148 segundos, 13 proyectos). El script contó los 80 hallazgos de la corrida anterior de health-check y no los de este informe. Tampoco midió documentos leídos. La nota de la corrida sí recoge lo que no sé.