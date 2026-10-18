# /criterio-portfolio:steering-pack 

Fichas cargadas: las 13 de `estado/records/PRY-199…PRY-211`, al corte 2026-10-17. Cifras derivadas: salida de `portafolio.py compute` de hoy. Además uso los resultados de hoy de change-control, raid-log, vendor-tracking y project-closure en `estado/corridas/`. No releí los documentos originales de cada carpeta: lo que sigue es tan firme como esas fichas. Términos vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17; ya estaban registrados, no hubo que volver a aceptarlos).

# Comité de proyectos — 2026-10-23
9 decisiones · 5 escalamientos · 11 proyectos con hallazgos (de 13)

Portafolio, copiado de `compute`: 13 proyectos, 90 señales abiertas, 9 proyectos que declaran verde con señales en contra, 13 sin autoridad de aprobación declarada.
La fecha 2026-10-23 es la que fija la configuración (`committee_next`).

## Decisiones del comité anterior
| Decisión | Fecha | Qué pasó | Estado |
|---|---|---|---|
| Sin dato | — | No hay en la carpeta un acta del comité del portafolio ni una corrida anterior de este material. Las actas de `30-reuniones/` son reuniones de cada proyecto, no del comité. | No se puede cerrar el ciclo anterior |

Dos cambios figuran aprobados por «el comité» sin nombre ni acta: PRY-208 CC-01 y PRY-210 CC-01. Van como decisión 5.

## Decisiones de hoy

### [1] ¿Quién aprueba cambios de fecha y presupuesto mientras las actas de constitución no lo digan?
**Proyecto:** los 13 · **Quién decide:** no consta; es el primer punto del comité · **Si no se decide hoy:** las decisiones 4 a 6 se votarían sin saber si este comité tiene la facultad.
La ficha de los 13 marca `identity.authority` como no encontrado. Las fichas nombran cinco comités distintos: Expansión, Comercial, Cadena de Abastecimiento, Transformación Digital y Arquitectura. En PRY-211 el patrocinador y el gerente son la misma persona (Camilo Beltrán), según la ficha.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Este comité aprueba los cambios de los 13 hasta que cada acta se corrija | Sin cambio | Decide el 2026-10-23 | Sin costo directo |
| B. Cada comité nombrado en la ficha decide lo suyo | Sin cambio | Sin dato: no hay fechas de sus sesiones | Sin costo directo |
| C. Se pospone | Sin cambio | Los puntos 4 a 6 esperan | Sin dato |

**Recomendación:** A, de forma temporal y con acta, y pedir a cada gerente la cláusula de autoridad antes del próximo comité. Es la única opción que no deja los puntos 4 a 6 sin decidir. Que este comité tenga la facultad lo verifica quien lo convoca; yo no puedo.

### [2] ¿Se nombra un solo responsable para el «hallazgo de seguridad en los medios de pago»?
**Proyecto:** PRY-199, PRY-200, PRY-201, PRY-211 · **Quién decide:** no consta (punto 1) · **Si no se decide hoy:** sigue abierto sin doliente en cuatro informes; el de PRY-199 ya declara verde con esta incidencia abierta.
Misma redacción en cuatro informes, abierta desde 2026-10-09 (200, 201, 211) y 2026-10-15 (199). No sé si es un solo hallazgo o cuatro: nadie lo dice.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Un responsable único, que confirme si es un hecho o cuatro | Sin cambio | Respuesta antes del comité siguiente | Sin dato |
| B. Un responsable por proyecto | Sin cambio | Sin dato | Sin dato |
| C. No asignar hoy | Sin cambio | Sigue abierta | Sin dato |

**Recomendación:** A. Si es un solo hallazgo en medios de pago, cuatro dolientes lo parten; si son cuatro, el responsable único lo dirá.

### [3] ¿Se fija doliente y fecha para la «prueba de carga de temporada que no alcanzó el umbral y se repite»?
**Proyecto:** PRY-199, PRY-204, PRY-208, PRY-209, PRY-211 · **Quién decide:** no consta (punto 1) · **Si no se decide hoy:** cinco proyectos con una prueba que se repite, sin dueño ni fecha, ante una temporada alta que no se mueve.
Abierta desde 2026-10-05 hasta 2026-10-17 según el informe de cada uno.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Un responsable único y fecha para la repetición | Sin cambio | Sin dato | Sin dato |
| B. Cada gerente asume la suya | Sin cambio | Sin dato | Sin dato |
| C. No asignar hoy | Sin cambio | Sin dato | Sin dato |

**Recomendación:** A. Cruza cinco proyectos y el resultado de uno condiciona a los demás. No tengo el umbral pactado ni los resultados, y no los invento.

### [4] ¿Se aprueban, se rechazan o se devuelven las cuatro solicitudes de cambio pendientes (PRY-201, 202, 209, 211)?
**Proyecto:** PRY-201, PRY-202, PRY-209, PRY-211 · **Quién decide:** no consta; la ficha nombra al Comité de Cadena de Abastecimiento (201, 202, 211) y al Comité Comercial (209) · **Si no se decide hoy:** las cuatro siguen con el cronograma ya movido sin cambio autorizado.
Las cuatro piden «ampliación de alcance». En las cuatro, `compute` marca la línea base vigente movida sin cambio autorizado. Solo en PRY-201 sé el orden: la v2 es del 2026-10-09 y la solicitud del 2026-10-17. En las otras tres no tengo la fecha del movimiento.
| Proyecto | Pide (ficha) | Días movidos sin autorizar | Desviación vs original | Fin vigente | Declara |
|---|---|---|---|---|---|
| PRY-201 CC-01 (2026-10-17) | +24 días · 48.000.000 COP | 24 | 24 días (5,3 %) | 2026-09-17 | verde, 34 % |
| PRY-202 CC-01 (2026-10-04) | +116 días · 232.000.000 COP | 116 | 116 días (41,7 %) | 2026-09-20 | verde, 82 % |
| PRY-209 CC-01 (2026-10-17) | +80 días · 160.000.000 COP | 80 | 80 días (17,4 %) | 2027-10-16 | amarillo, 41 % |
| PRY-211 CC-01 (2026-10-10) | +118 días · 236.000.000 COP | 118 | 118 días (35,3 %) | 2026-09-27 | verde, 27 % |

En PRY-201, 202 y 211 la fecha de fin vigente ya pasó. En PRY-201 no puedo decir si los +24 días de la solicitud son los de la v2 o 24 adicionales. En PRY-202 la proyección supera lo aprobado en 17,8 %.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar con línea base nueva y motivo escrito | Ampliación, aún sin describir (el acta de PRY-201 lista «Componente 1, 2 y 3» sin detalle) | Lo pedido arriba | Lo pedido arriba, sin el costo de mantener al equipo |
| B. Rechazar y volver a la línea base original | Sin ampliación | Atraso real contra la original, hoy no recuperado | Sin costo adicional; sin dato de lo ya comprometido |
| C. Devolver hasta que traigan motivo, alcance concreto y plan | Sin cambio | Sigue sin línea base válida | Sin dato |

**Recomendación:** C para las cuatro. La línea base ya se movió sin autorización y las fichas no registran motivo ni alcance concreto. Aprobar hoy sería ratificar un atraso ocurrido sin poder decir qué se amplía.

### [5] ¿Se ratifican por escrito los dos cambios ya «aprobados» sin decisor nombrado (PRY-208 y PRY-210)?
**Proyecto:** PRY-208, PRY-210 · **Quién decide:** no consta (punto 1) · **Si no se decide hoy:** quedan aprobados sin quién los aprobó, y el de PRY-210 sin línea base nueva.
| Proyecto | Pide / aprobó | Decidido por (ficha) | Lo que marca `compute` |
|---|---|---|---|
| PRY-208 CC-01 (2026-10-11) | +78 días · 156.000.000 COP | «el comité (sin nombre en el documento)» | Desviación vs original 78 días (23,2 %), con 78 días aprobados |
| PRY-210 CC-01 (2026-10-05) | +106 días · 212.000.000 COP | «el comité» | Cambio aprobado sin línea base nueva (106 días); desviación vs original 106 días (21,2 %) |

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ratificar en acta, con decisor y fecha, y registrar la línea base nueva de PRY-210 | Ampliación ya aprobada | Los días de arriba | Los montos de arriba |
| B. Reabrir y evaluar como los del punto 4 | Sin dato | Sin dato | Sin dato |

**Recomendación:** A, si quien las aprobó se identifica. Si nadie sabe qué comité fue, B. Hoy no puedo decir cuál es el caso.

### [6] ¿Se aprueba mover 30 días el despliegue de PRY-200 Tienda en línea?
**Proyecto:** PRY-200 · **Quién decide:** no consta; la ficha nombra al Comité Comercial (aprobó la línea base) y al patrocinador Carlos Peña · **Si no se decide hoy:** sigue con cierre 2026-11-23 y un informe que ya dice que el despliegue «se reprogramó».
Quién lo pide y por qué no consta en ningún documento. Leí la solicitud como el hito «Despliegue en la cadena»; es interpretación del análisis de cambio de hoy, no un dato. Hay un hallazgo de seguridad en medios de pago abierto sin responsable (punto 2).
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar | Sin impacto declarado | 2026-11-23 → 2026-12-23 (+30 días; 6,6 % del plan, bajo el umbral) | Sin cálculo: proyección actual 6.859.551.454 COP sobre 6.800.000.000 aprobados (+0,9 %), más un mes sin costear |
| B. Rechazar | Sin cambio | Cierre 2026-11-23 | La proyección actual |
| C. Devolver | Sin cambio | Sin dato | Sin dato |

**Recomendación:** C. Faltan solicitante, motivo, costo del mes adicional, las fechas del congelamiento de fin de año y la fecha vigente real del despliegue.

### [7] ¿Se retienen los pagos a proveedores sin acta de recibo?
**Proyecto:** PRY-200, PRY-203, PRY-206 · **Quién decide:** no consta (punto 1) · **Si no se decide hoy:** las facturas pueden pagarse sin recibo comprobable. No sé si alguna ya se pagó.
| Proyecto | Proveedor · contrato | Qué no cuadra |
|---|---|---|
| PRY-200 | Sistemas Comerciales del Norte · CT-497 | FV-1497 por 445.577.090 COP (2026-09-10) sin acta de recibo; dos entregables vencidos sin entrega (294 y 43 días); la bolsa de horas figura «aceptada» sin evidencia |
| PRY-203 | Sistemas Comerciales del Norte · CT-338 | Facturado 118.225.663 COP contra 95.848.542 aceptados: diferencia de 22.377.121 COP; tres entregables vencidos (359, 260 y 161 días) |
| PRY-206 | Retail Andino Consultores S.A.S. · CT-783 | Facturado 182.444.266 COP con 0 de 2 entregables aceptados |

Es el mismo proveedor en PRY-200 y PRY-203, con el mismo entregable de licenciamiento vencido en ambos.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Retener todo hasta tener acta de recibo firmada | Sin cambio | Puede tensar al proveedor; sin dato de cuánto | Queda retenido lo facturado arriba |
| B. Pagar solo lo aceptado con acta y retener la diferencia | Sin cambio | Sin dato | Retiene 22.377.121 COP en PRY-203; en los otros dos no hay base aceptada |
| C. Pagar | Sin cambio | Sin demora | Se paga sin recibo comprobable |

**Recomendación:** A para PRY-200 y PRY-206; B para PRY-203. Antes de pagar FV-1497, pedir el acta de recibo firmada por la gerente (Sandra Gil) o devolver la factura. El contrato CT-497 no trae vigencia ni preaviso, así que no puedo decir si hay una fecha que presione.

### [8] PRY-207 Marca propia de alimentos: ¿se exige una replanificación formal o se decide su destino?
**Proyecto:** PRY-207 · **Quién decide:** no consta; la ficha nombra al Comité de Arquitectura, al patrocinador Felipe Arango y al gerente Javier Hoyos · **Si no se decide hoy:** sigue en rojo, con un plan que terminaba antes del corte y sin solicitud de cambio.
Declara rojo, 66 % (informe 2026-10-15). La única línea base es la v1, con fin 2026-04-17, anterior al corte. La ficha no trae hitos ni solicitud de cambio, y por eso `compute` no levanta ninguna señal de plan: ausencia de dato, no buena salud. Aprobado 9.500.000.000 COP; ejecutado 1.531.882.450 (16,1 %); comprometido 4.249.815.175 (44,7 %); proyección 9.186.690.012. El 66 % declarado frente al 16,1 % ejecutado: no sé si son coherentes.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Pedir solicitud de cambio con fecha, alcance y costo | A definir | Fecha nueva a definir | Parte de la proyección actual |
| B. Decidir su destino (cierre por decisión, pausa o continuación) con la información que traiga el gerente | Sin dato | Sin dato | Sin dato; hay 4.249.815.175 COP comprometidos |
| C. Esperar | Sin cambio | Sigue vencido | Sin dato |

**Recomendación:** A, y que el gerente traiga al comité la lista de hitos que hoy no existe. Sin hitos no se puede decir qué falta, así que B sería decidir a ciegas.

### [9] PRY-203 Reposición automática: ¿se exige una solicitud de cambio con fecha y presupuesto nuevos?
**Proyecto:** PRY-203 · **Quién decide:** no consta; la ficha nombra al Comité de Expansión, al patrocinador Carlos Peña y a la gerente Laura Vélez · **Si no se decide hoy:** declara verde, 92 %, con el despliegue vencido y 19,4 % de sobrecosto proyectado, sin ningún cambio registrado.
Señales de `compute`: hito «Despliegue en la cadena» vencido hace 8 días (fin 2026-10-09); proyección 1.432.210.423 COP sobre 1.200.000.000 aprobados (+19,4 %); 8 compromisos vencidos, 3 sin fecha y 3 reprogramados (6, 5 y 3 veces; el de Natalia Ospina «Enviar el documento 1» pasó de 2026-09-28 a 2026-12-18). Cambios registrados: 0. Además: dos semanas perdidas por la rotación de un desarrollador clave y un riesgo no registrado, dicho el 2026-10-17, de que el proveedor no llegue con el equipo completo (no dice cuál).
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Exigir solicitud de cambio con fecha de despliegue y presupuesto | A definir | Fecha nueva a definir | La proyección de arriba, ya +19,4 % |
| B. Que el patrocinador reasigne dolientes y fechas de los compromisos, sin cambiar la línea base | Sin cambio | Sigue el 2026-10-09 vencido | Sin dato |
| C. Esperar al próximo informe | Sin cambio | Sin dato | Sin dato |

**Recomendación:** A. Con la fecha de fin ya pasada y el sobrecosto sobre el umbral de 10 %, la línea base vigente ya no describe el proyecto. B por sí sola ocultaría el atraso.

## Escalamientos sin decisión asociada
| Proyecto | Qué | Desde cuándo | Qué se necesita |
|---|---|---|---|
| PRY-205 | Fin planeado 2026-10-19. Declara verde, 43 % (2026-10-07), con un plan que soporta 67–100 %; hitos cumplidos sin evidencia; 10 días sin informe nuevo | 2026-10-07 | Que el gerente (Mauricio Pérez) confirme si cierra el 2026-10-19 o replanifica |
| PRY-208 | Declara rojo; dos entregables de Datos y Demanda S.A.S. (CT-741) vencidos, de 3 con 0 aceptados: licenciamiento (146 días) y bolsa de horas (53 días). El contrato no trae vigencia en la ficha | 2026-05-24 | Fecha comprometida por el proveedor o decisión contractual |
| PRY-206 | Declara 61 % cuando el plan soporta 20–40 % (1 de 5 hitos cumplido) | 2026-10-09 | Que el gerente explique de dónde sale el 61 % |
| PRY-200 y PRY-204 | Compromisos de Beatriz Cuéllar vencidos desde el 2026-10-08, 9 días: «punto 17» (PRY-200) y «punto 9» (PRY-204). Ningún acta dice qué son esos puntos | 2026-10-08 | Qué es cada punto y confirmar la entrega |
| PRY-203 | Riesgo dicho en la reunión del 2026-10-17 y no anotado: el proveedor podría no llegar con el equipo completo | 2026-10-17 | Identificar el proveedor y registrarlo con doliente |

## Para conocimiento
- **PRY-199** Iluminación LED: verde, 20 %, el plan soporta 20–40 %; `compute` no levanta señales. Sus dos incidencias abiertas van en los puntos 2 y 3. Retail Andino (CT-199): 3 entregables, 0 aceptados.
- **PRY-200** Tienda en línea: puntos 2, 6 y 7. Verde, 57 %, el plan soporta 80–100 %.
- **PRY-201** Programa de fidelización: puntos 2 y 4. Cuatro de cinco hitos cumplidos sin evidencia; compromiso de Natalia Ospina vencido hace 16 días.
- **PRY-202** Centro de distribución norte: punto 4. Verde, 82 %; sobrecosto proyectado 17,8 %; dos semanas perdidas por rotación de un desarrollador clave.
- **PRY-203** Reposición automática: punto 9, y punto 7 por el proveedor.
- **PRY-204** Cajas de autopago: punto 3. Verde, 57 % contra 67–100 % del plan; fin 2026-10-31.
- **PRY-205** Pago con QR: escalamiento arriba.
- **PRY-206** Precios dinámicos: punto 7 y escalamiento arriba.
- **PRY-207** Marca propia: punto 8.
- **PRY-208** Domicilios en dos horas: puntos 3 y 5 y escalamiento. Rojo, 54 %.
- **PRY-209** Migración del ERP: puntos 3 y 4. Amarillo; su informe tiene 12 días.
- **PRY-210** Etiquetas electrónicas: punto 5. Verde, 75 %, informe de hace 18 días; dos entregables de Integra Comercio (CT-451) aceptados sin evidencia, facturado 616.866.660 COP, igual a lo aceptado.
- **PRY-211** Pronóstico de demanda: puntos 2, 3 y 4. Verde, 27 % contra 100 % del plan; compromiso de Rubén Cárdenas vencido hace 3 días; bolsa de horas de Tecnología para Tiendas (CT-101) aceptada sin evidencia.

## Anexo

### Estado de cada proyecto (declarado, no verificado)
| Proyecto | Declara | Avance | Fin vigente | Desviación vs original | Proyección sobre aprobado |
|---|---|---|---|---|---|
| PRY-199 | verde | 20 % | 2027-12-16 | 0 días | 0,0 % |
| PRY-200 | verde | 57 % | 2026-11-23 | 0 días | 0,9 % |
| PRY-201 | verde | 34 % | 2026-09-17 | 24 días (5,3 %) | −0,5 % |
| PRY-202 | verde | 82 % | 2026-09-20 | 116 días (41,7 %) | 17,8 % |
| PRY-203 | verde | 92 % | 2026-10-09 | 0 días | 19,4 % |
| PRY-204 | verde | 57 % | 2026-10-31 | 0 días | −3,0 % |
| PRY-205 | verde | 43 % | 2026-10-19 | 0 días | −0,3 % |
| PRY-206 | verde | 61 % | 2027-11-13 | 0 días | 3,1 % |
| PRY-207 | rojo | 66 % | 2026-04-17 | 0 días (sin hitos) | −3,3 % |
| PRY-208 | rojo | 54 % | 2027-04-11 | 78 días (23,2 %) | −6,1 % |
| PRY-209 | amarillo | 41 % | 2027-10-16 | 80 días (17,4 %) | −0,5 % |
| PRY-210 | verde | 75 % | 2027-06-09 | 106 días (21,2 %) | 3,4 % |
| PRY-211 | verde | 27 % | 2026-09-27 | 118 días (35,3 %) | −6,6 % |

### Contradicciones abiertas
Nueve proyectos declaran verde con señales de `compute` que su informe no explica: PRY-200, 201, 202, 203, 204, 205, 206, 210 y 211. PRY-199 declara verde sin señales de `compute`, pero con dos incidencias abiertas en su propio informe.

### Vacíos de información
- Autoridad de aprobación (`identity.authority`): no encontrada en los 13.
- RAID: 19 riesgos y 13 incidencias, sin doliente, fecha, probabilidad ni impacto. No puedo decir cuáles llevan dos períodos sin movimiento: es desconocido, no cero.
- Dependencias entre proyectos: ninguna declarada. Eso no prueba que no existan; no leí las actas `.docx` de siete proyectos.
- Comité anterior: sin acta ni registro de decisiones.
- Campos de identidad, alcance y presupuesto aprobado con más de 12 meses de antigüedad en varias fichas (por ejemplo PRY-200, 201 y 202).
- Los hitos «cumplidos» sin evidencia de recibo son la causa más común de las contradicciones; no los listo uno por uno aquí, están en la salida de `compute`.

### Pie
Versión del plugin criterio-portfolio 0.4.0 · términos 1.1. Fichas aplicadas: PRY-199 a PRY-211, al corte 2026-10-17. Campos inciertos: autoridad de aprobación, solicitante y motivo de la solicitud de PRY-200, fechas de movimiento de la línea base en PRY-202, 209 y 211, hitos de PRY-207, y qué comité aprobó los cambios de PRY-208 y PRY-210. Borrador de trabajo, no decisión ni asesoría; la verificación es de quien lo use. Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

## Después
Cuando el comité sesione, puedo registrar sus decisiones en las fichas. Ahí se cierra el ciclo y el material del próximo comité empieza a construirse solo.

---
Corrida registrada como `2026-10-17-steering-pack-1`. El texto de arriba está en `estado/corridas/salida-steering-pack.md`.