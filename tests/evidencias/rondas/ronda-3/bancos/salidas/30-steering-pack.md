# /criterio-portfolio:steering-pack 

Terminé el paquete del comité del 2026-10-21 y lo registré como corrida `2026-10-15-steering-pack-1`. A continuación va el contenido entero, igual que el archivo guardado en `estado/corridas/salida-steering-pack.md`.

---

**Cargué:** las 13 fichas de `estado/records/` (PRY-199 a PRY-211), generadas el 2026-10-15, más las salidas de las corridas de hoy y el paquete `pm-escalate` de PRY-207. Cifras de `portafolio.py compute` con corte 2026-10-15. Términos vigentes (v1.1, familia 0.3.9), aceptados por José Francisco Ñáñez el 2026-10-15; no hizo falta registrarlos de nuevo. Como nadie respondía, tomé la fecha sugerida: la de `committee_next` en la configuración.

# Comité de proyectos — 2026-10-21
6 decisiones · 6 escalamientos sin decisión asociada · 11 de 13 proyectos con hallazgos (68 señales abiertas; 7 proyectos declaran verde y las señales lo contradicen)

## Decisiones del comité anterior
| Decisión | Fecha | Qué pasó | Estado |
|---|---|---|---|
| Ninguna registrada | — | No hay corrida previa de `/steering-pack` ni una sola decisión escrita en las 21 minutas de comité (solo tablas de compromisos). | Sin dato |

Este comité decide sin saber qué se decidió antes. Lo que se decida hoy debe quedar escrito para que el ciclo pueda cerrarse.

## Decisiones de hoy

### [1] ¿Se fija como regla transitoria que todo cambio de fecha, costo o alcance suba al comité del proyecto hasta que cada acta declare los umbrales del gerente?
**Proyectos:** los 13 · **Quién decide:** no determinable con certeza. La regla transitoria, el comité de portafolio, si tiene facultad sobre los otros. Los umbrales de cada proyecto, su propio comité. Son cuatro: Transformación Digital (PRY-199, 201, 202, 205), Banca Empresas (200, 206), Riesgos (203, 204, 208, 210) y Arquitectura (207, 209, 211). Ningún documento dice que el comité de portafolio mande sobre ellos; si no lo hace, aclararlo es lo primero de esta sesión.
**Si no se decide hoy:** `authority` está vacío en las 13 fichas. Hay tres cambios en curso (PRY-200, 202 y 209) que ningún documento permite dirigir con certeza a quien aprueba.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Regla transitoria: todo sube al comité | Sin cambio | Cada cambio espera al siguiente comité (semanal según la configuración) | Sin cifra; carga de agenda |
| B. Pedir a cada patrocinador una adenda con umbrales | Sin cambio | Sin fecha en los documentos | Sin cifra |
| C. A hoy y B con fecha | Sin cambio | A de inmediato; B según la fecha | Sin cifra |

**Recomiendo:** C. Sin umbrales por escrito, "desviación aprobada" no existe: hay fechas que alguien escribió (PRY-209 es el caso).

### [2] PRY-209 Nómina electrónica — ¿Se aprueba hoy CC-01 (+32 días, +64.000.000 COP)?
**Quién decide:** Comité de Arquitectura (aprobó el presupuesto en el acta del 2025-12-02); depende del punto 1 · **Si no se decide hoy:** el cronograma v2 sigue publicado con la salida en 2026-07-22 y 32 días de movimiento sin autorizar.
Hechos: el informe del 2026-10-15 declara verde con 86 %, y esa salida ya venció hace 85 días; no hay acta de paso a producción. El informe atribuye el movimiento a una "ventana de cambio del área de operaciones" y CC-01 lo presenta como "ampliación de alcance". La minuta del 2026-10-14 no registra que CC-01 se tratara.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar | Ampliación sin describir (el acta lista "Componente 1, 2 y 3" sin detalle) | Salida 2026-07-22, ya vencida (+32 días, 16,8 %) | +64.000.000 COP; no se sabe si la proyección de 1.121.091.254 COP ya los incluye |
| B. Rechazar | Sin cambio | Vuelve a la línea base v1 (2026-06-20); 32 días quedan como desviación no autorizada | 0 COP adicionales |
| C. Devolver con requisitos | Sin cambio | Decide en el comité siguiente | Sin cifra |

**Recomiendo:** C. Antes de aprobar una fecha ya consumada hay que saber el motivo real y si el proyecto salió a producción (3 de 5 hitos sin acta). Requisitos: motivo único por escrito, acta de paso a producción o declaración de que no ocurrió, y si la proyección incluye los 64.000.000 COP.

### [3] PRY-202 Migración a la nube — ¿Se ratifica por escrito CC-01 (+66 días, +132.000.000 COP) y se exige una solicitud de cambio aparte por la proyección de 1.501.431.307 COP?
**Quién decide:** Comité de Transformación Digital (según la ficha). CC-01 dice "autorizada por el comité" sin nombrar cuál. · **Si no se decide hoy:** ningún documento declara un presupuesto vigente: el informe del 2026-10-14 sigue en 1.200.000.000 COP y la proyección lo supera en 25,1 %.
Hechos: fin original 2026-06-11, vigente 2026-08-16 (+66 días, 32,4 %); ambas fechas ya pasaron. Declara verde con 65 %; el plan sostiene 100 % y los 3 hitos no tienen acta. Compromiso de Diana Molina vencido hace 26 días.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ratificar CC-01 y exigir solicitud aparte | Ampliación reconocida | Línea base 2: 2026-08-16; la 1 se conserva | +132.000.000 COP reconocidos; el exceso restante no se puede calcular sin presupuesto vigente |
| B. Ratificar sin más | Ídem | Ídem | La proyección queda sin contraste |
| C. No ratificar | Vuelve al alcance original | Vuelve a 2026-06-11, ya vencida | 1.200.000.000 COP; la proyección sigue 25,1 % encima |

**Recomiendo:** A. Deja escrito quién aprobó y obliga a que el sobrecosto proyectado pase por control de cambios.

### [4] Redes del Norte Ltda. (PRY-204 y PRY-209) — ¿Se instruye a los dos gerentes a no autorizar más pagos sin acta de recibo por entregable y se revisan las facturas ya radicadas?
**Proyectos:** PRY-204 (CT-470, rojo, 18.000.000.000 COP aprobados) y PRY-209 (CT-154) · **Quién decide:** el comité de cada proyecto (Riesgos para PRY-204; Arquitectura para PRY-209). · **Si no se decide hoy:** los pagos siguen a criterio de cada gerente; no sé si FV-1470 o FV-1154 ya se pagaron.
El patrón se repite en los dos contratos: "Licenciamiento del motor" vencido (159 días en PRY-204, 255 en PRY-209), "Bolsa de horas de desarrollo" aceptada sin acta de recibo, y una factura por ese monto aceptado: FV-1470 por 1.822.428.850 COP y FV-1154 por 105.979.087 COP. En PRY-209 también está vencida la Parametrización del tarifario (151 días).

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Instruir y revisar facturas | Sin cambio | Puede frenar entregas del proveedor | 0 COP nuevos; quedan retenidos los pagos pendientes de las dos facturas |
| B. Dejarlo a cada gerente | Sin cambio | Sin efecto | Sin cifra; se mantiene la exposición |

**Recomiendo:** A. Es un mismo proveedor en dos contratos: merece una instrucción y no dos conversaciones.

### [5] Calendario de liberaciones del core — ¿El comité nombra un responsable de publicarlo y confirmarlo?
**Proyectos:** PRY-200, 203, 204, 206, 207 y 208 lo declaran como dependencia; PRY-199, 200 y 203 ya sacaron historias del sprint por esa causa · **Quién decide:** no identificado · **Si no se decide hoy:** seis proyectos siguen apoyados en una fecha que nadie confirmó (las 13 actas dicen "Ninguna declarada" en dependencias).
Hipótesis, no hallazgo: el core podría ser PRY-201, que lleva 24 días en silencio y cuyo cierre comprometido (2026-10-12) ya pasó.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Nombrar responsable y fecha de publicación | Sin cambio | La fija el comité | Sin cifra |
| B. Cada proyecto lo gestiona | Sin cambio | Sin efecto | Sin cifra |

**Recomiendo:** A. Afecta a seis proyectos y a ninguno le corresponde resolverla. Primero hay que decir qué es "el core".

### [6] Disponibilidad del equipo de seguridad — ¿Se le pide confirmar por escrito su capacidad para las revisiones finales de seis proyectos?
**Proyectos:** PRY-199, 200, 202, 206, 210 y 211 lo dan por disponible sin verificarlo; PRY-202, 203 y 205 ya tienen hallazgos de seguridad abiertos · **Quién decide:** no identificado · **Si no se decide hoy:** el supuesto sigue sin verificar y ningún ítem de RAID tiene doliente ni fecha (32 de 32).

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Pedir confirmación escrita con calendario | Sin cambio | Hasta la respuesta | Sin cifra |
| B. Seguir sin verificar | Sin cambio | Sin efecto hoy | Sin cifra |

**Recomiendo:** A. Es un supuesto compartido; si falla, falla en seis proyectos a la vez.

## Escalamientos sin decisión asociada
| Proyecto | Qué | Desde cuándo | Qué se necesita |
|---|---|---|---|
| PRY-200 | Solicitud de +30 días (2026-11-16 → 2026-12-16) sin solicitante, motivo ni costo; avance 23 % contra 80–100 % del plan; Parametrización del tarifario vencida hace 108 días | 2026-10-15; entregable desde 2026-06-29 | Solicitante, motivo y costo por escrito; cuál es la fecha base (acta 2026-12-28 o cronograma 2026-11-16). **Devuelta al gerente (Sandra Gil).** |
| PRY-201 | 24 días en silencio, cierre 2026-10-12 vencido, proyección 4.767.564.975 COP contra 4.200.000.000 (+13,5 %), declarado verde | 2026-09-21 | Informe actualizado y solicitud de cambio de costo. Gerente: Laura Vélez |
| PRY-203 | Cierre 2026-10-29 con 25 % declarado, sin cronograma ni hitos; ejecutado 3.636.734.860 COP mayor que comprometido 2.587.925.781 COP | 2026-10-10 | Cronograma con hitos o fecha nueva autorizada; explicar ejecutado > comprometido. Gerente: Sandra Gil |
| PRY-204 | Rojo; hito "Integración con el core" vencido hace 7 días; compromiso de Javier Hoyos vencido hace 18 días; riesgo regulatorio sin doliente | 2026-10-08 · 2026-09-27 | Doliente del riesgo y fecha nueva del hito |
| PRY-205 | Rojo; dos incidencias sin doliente; avance 57 % contra 80–100 % | 2026-10-13 | Doliente por incidencia. Gerente: María Restrepo |
| PRY-207 | "Cerrar la prueba 2" reprogramado 6 veces (2026-09-23 → 2026-12-07); fin 2027-08-10 en el cronograma y 2027-11-03 en el acta | 2026-09-23 | Causa del bloqueo dicha por quien la conoce; cuál fecha de fin rige. La patrocinadora (Beatriz Cuéllar) puede nombrar al desbloqueador |

## Para conocimiento
- **PRY-199** verde 20 %, sin señales; primer entregable de CT-199 vence 2026-11-14 y está pendiente.
- **PRY-206** verde 62 %; plan sostiene 75–100 %; 3 hitos sin acta.
- **PRY-208** verde 29 %; plan sostiene 100 %; 3 hitos sin acta; compromiso de Gustavo Neira sin fecha.
- **PRY-210** verde 51 %; plan sostiene 100 %; 3 hitos sin acta.
- **PRY-211** verde 31 %; plan sostiene 67–100 %; 2 hitos sin acta.
- **PRY-207** además: proyección 7.058.214.079 COP contra 6.800.000.000 (+3,8 %, bajo el umbral de 10 %); comprometido 89,4 %, a 0,6 puntos del umbral de 90 %.

## Anexo
Contiene la tabla de estado por proyecto, las contradicciones abiertas (PRY-207, 209, 200, 202; el comité semanal de la configuración contra el quincenal que asumió PRY-207) y los vacíos de información. Está completo en `estado/corridas/salida-steering-pack.md`; no lo repito aquí.

## Después
Cuando el comité sesione, dime qué se decidió en cada punto y lo registro en las fichas, con las líneas base nuevas sin borrar las anteriores. No escribí a nadie ni asigné dolientes: las propuestas son del agente, y la decisión es de quien tiene la facultad.

---
*Pie:* criterio-portfolio · familia 0.3.9 · términos v1.1 (https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.9). Fichas aplicadas: las 13, generadas el 2026-10-15. Campos inciertos: autoridad y fase (13 fichas), producto (4), presupuesto vigente de PRY-202, fecha de fin vigente de PRY-207, comité que rige y su cadencia, estado de pago de FV-1470 y FV-1154. Borrador de trabajo, no decisión ni asesoría; la verificación es de quien lo usa.

---

Tres cosas que conviene saber:
- **Resumen en pantalla:** para esta respuesta acorté el anexo y "Para conocimiento". El archivo guardado tiene el contenido completo, incluida la tabla de estado por proyecto.
- **PRY-203:** `compute` no le levanta ninguna señal, así que no cuenta entre los 11 con hallazgos. Lo puse en escalamientos por mi lectura de la ficha: cierre en 14 días con 25 % declarado y ejecutado mayor que comprometido. Es juicio mío, no una señal del script.
- **Corrida:** la registré con 156 segundos medidos por el script. El script no midió documentos leídos en esta corrida.