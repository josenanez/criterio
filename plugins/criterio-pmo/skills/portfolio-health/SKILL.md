---
name: portfolio-health
description: "Cómo se juzga la salud de un portafolio a partir de las fichas: semáforo con evidencia, proyectos en silencio, contradicciones entre documentos, antigüedad del dato y los umbrales que hacen hablar al agente. Úsalo al consolidar portafolio, preparar comité, evaluar si un proyecto está realmente en verde, o decidir qué merece alerta. Portfolio health, thresholds and staleness."
---

# Salud de portafolio

## El principio

Un semáforo que repite lo que el gerente declaró no sirve de nada. La PMO ya tiene eso: se llama el reporte semanal.

Lo que aporta valor es **contrastar la declaración contra la evidencia** y decir dónde no coinciden. Por eso el estado que produce este plugin nunca es una opinión: es una comparación entre lo declarado y lo que sustentan los documentos.

## Los tres estados, y qué los sustenta

| Estado | Qué significa aquí |
|---|---|
| **Sustentado** | Lo declarado coincide con lo que dicen los documentos, y hay documentos recientes |
| **Sin sustento** | Lo declarado no se contradice, pero ningún documento lo respalda. No es lo mismo que estar mal |
| **Contradicho** | Un documento dice algo distinto de lo declarado |

"Sin sustento" es el estado más común en una PMO real y el que más incomoda. Reportarlo tal cual es el trabajo.

**Y ya no se juzga a ojo.** El script compara el semáforo declarado contra las señales que él mismo calculó, y devuelve en `declared.unaccounted_signals` las que ese semáforo no explica. Cuando el declarado es verde y esa lista no está vacía, levanta `declared_vs_evidence`. El total del portafolio lo trae `totals.green_contradicted`: **cuántos de los proyectos que reportan verde tienen evidencia que su luz ignora.** Es la primera cifra que debe recibir un comité.

Dos precisiones que evitan un hallazgo mal armado. La lista deja fuera las contradicciones entre documentos: son un defecto de la ficha, no del proyecto, y mezclarlas debilita el hallazgo. Y para el amarillo y el rojo la lista se calcula igual pero no se levanta alerta: quien ya reportó problema no está escondiendo nada.

## Las diecinueve señales

Este skill es el **único sitio** donde vive qué significa cada señal y cuándo merece alarma.
No se repite en la página de la capacidad ni en las hojas de diseño: una lista copiada se
desactualiza en el documento que nadie mira.

Los **valores** por defecto no están aquí: están en `DEFAULT_THRESHOLDS` de `scripts/pmo.py`,
que es lo que el código lee, y se cambian en la configuración local **hablando, no editando
archivos**. Aquí va qué clave gobierna cada señal, para saber qué preguntar cuando alguien
quiere moverla.

### Estado contra el plan

| Señal | Habla cuando | Clave |
|---|---|---|
| `milestone_overdue` | La fecha del hito pasó y ningún documento prueba que se cumplió | — siempre |
| `variance_time` | La desviación en tiempo contra la línea base **original** supera el porcentaje | `variance_time_pct` |
| `variance_cost` | La proyección al cierre se pasa del aprobado por encima del porcentaje | `variance_cost_pct` |
| `budget_committed` | Lo comprometido se acerca a lo aprobado. Un proyecto al 40% ejecutado y 95% comprometido no tiene holgura | `committed_pct` |
| `rebaseline_unauthorized` | La línea base se movió más días de los que autorizaron los cambios aprobados. **Es un hueco documental, no una acusación** | `rebaseline_tolerance_days` |
| `change_without_baseline` | Un cambio aprobado movió fechas y no dejó línea base nueva posterior | — siempre |

### La declaración contra la evidencia

| Señal | Habla cuando | Clave |
|---|---|---|
| `declared_vs_evidence` | El estado declarado es **verde** y hay al menos una señal que ese verde no cubre. Para amarillo y rojo la lista se calcula igual y no se levanta alerta: quien ya reportó problema no está escondiendo nada | — siempre |
| `declaration_stale` | La declaración tiene demasiados días. Un verde de hace seis semanas no es un verde | `declaration_stale_days` |
| `pm_vs_pmo` | El gerente y la PMO leyeron los mismos documentos y no dijeron lo mismo. **Solo es hallazgo cuando los dos citan**: entonces uno vio un papel que el otro no vio, y la señal dice cuál y de qué fecha | — |

### El silencio y la calidad del registro

| Señal | Habla cuando | Clave |
|---|---|---|
| `silent` | Días sin un documento nuevo. Un proyecto sin documentación no está mal gestionado: está sin documentar | `silent_days` |
| `contradiction` | Dos documentos dicen cosas distintas del mismo campo. Se reporta **siempre**, con las dos fuentes y las dos fechas | — siempre |
| `governance_change` | El conflicto está en el patrocinador, el gerente o el comité. **No es un defecto de la ficha: es un evento.** Nadie reexpide el acta porque se fue el patrocinador, y un proyecto con tres en dieciocho meses explica más que cualquier análisis de causa raíz | — siempre |

Un campo cuya fuente tiene más meses que `stale_field_months` carga su antigüedad visible en
el informe y **no** levanta alerta: es viejo, no es falso.

### Compromisos

| Señal | Habla cuando | Clave |
|---|---|---|
| `commitment_overdue` | Pasó la fecha prometida y no hay evidencia de cumplimiento | — siempre |
| `commitment_undated` | Nadie le puso fecha. No puede estar vencido, y por eso mismo desaparecía del informe: **un compromiso que nadie fechó es un hallazgo, no un vacío** | — siempre |
| `commitment_rescheduled` | El mismo compromiso se prometió de nuevo demasiadas veces. No son varios vencidos: es uno con historial, y un bloqueo que nadie nombró | `reschedules_to_flag` |

### Proveedores

| Señal | Habla cuando | Clave |
|---|---|---|
| `vendor_deliverable_late` | Pasó la fecha, no hay evidencia y nadie declaró la entrega | — siempre |
| `vendor_accepted_without_evidence` | Está declarado entregado o aceptado y ningún documento lo prueba | — siempre |
| `vendor_invoiced_without_delivery` | Hay facturación declarada y **ni un** entregable aceptado | — siempre |
| `vendor_invoiced_over_accepted` | La facturación supera la suma de los montos de los entregables aceptados | — siempre |

**El silencio cuando no pasó nada es la característica, no la falla.** Un agente que reporta
todos los lunes haya o no noticia se ignora en un mes.


### Sobre `pm_vs_pmo`, que es la única que compara dos fichas

Las demás señales salen de una ficha contra los documentos. Esta sale de **dos fichas
sobre los mismos documentos**: la que publica el agente del proyecto y la que escribe el
del portafolio. Nunca se fusionan — séptima invariante — y **la diferencia entre las dos
es lo que produce valor.**

Se contrastan **ocho campos**, no todos: `identity.sponsor`, `identity.manager`,
`identity.committee`, `identity.product`, `plan.end_date`, `money.approved`,
`declared.status` y `declared.as_of`. Son los que los dos tienen por qué leer.

Y hay cuatro formas de diferir, de las que **solo dos son hallazgo**:

| Lo que se observa | Qué significa |
|---|---|
| **Los dos citan y no coinciden** | Leyeron documentos distintos. El que cita el más reciente vio algo que el otro no. Es el hallazgo de más valor, y apunta a un documento concreto |
| **El gerente lo tiene y la PMO no** | **No es hallazgo.** Diferencia de profundidad: un compromiso dicho en una reunión no está al alcance de un barrido de portafolio |
| **La PMO lo tiene y el gerente no** | Sí es hallazgo: la PMO leyó un documento del proyecto que el gerente no está viendo |
| **Coinciden** | El caso normal, y no se reporta. Un agente que celebra las coincidencias es ruido |

La segunda fila es la que hace que esto sirva. Sin ella, cada corrida reportaría cien
diferencias de alcance y nadie volvería a abrir el informe.

**Contrastar no es arbitrar.** La señal no dice quién tiene razón, dice quién cita lo más
nuevo — y la mitad de las veces el que la tiene es el gerente, porque estuvo en la
reunión donde cambió el patrocinador y el acta de constitución no se actualizó nunca.

## Las tres defensas contra el dato viejo

Un campo deja de ser cierto sin que ningún archivo cambie. Contra eso hay exactamente tres mecanismos, y los tres se usan.

**1. Antigüedad.** Todo dato se reporta con la fecha de su fuente. Nunca *"el patrocinador es X"*; siempre *"según el acta de 2025-03, el patrocinador es X, sin confirmación posterior"*.

**2. Contradicción cruzada.** La minuta de la semana pasada nombra a otra persona que el acta de constitución. Es el hallazgo de más valor que produce el agente. Se reporta siempre, con las dos fuentes y las dos fechas, y va con pregunta al gerente.

**3. Confirmación periódica.** Mensual. **Cinco campos por corrida**, elegidos por importancia y no por antigüedad: patrocinador, gerente asignado, presupuesto aprobado, fecha comprometida de cierre y alcance. Un campo secundario simplemente carga su antigüedad visible en el informe y no gasta una pregunta.

Si preguntas por cuarenta campos, no responde nadie. Si preguntas por cinco, los responden.

## Qué se reporta del portafolio, y en qué orden

1. **Lo que cambió desde la corrida anterior.** Es lo primero porque es lo único que el gerente no sabe ya.
2. **Los verdes que la evidencia no sostiene**, con las señales que cada uno no explica. Van aquí y no al final porque es la razón de ser del informe.
3. **Contradicciones abiertas.**
4. **Hitos vencidos sin evidencia.**
5. **Proyectos en silencio**, con cuántos días.
6. **Dependencias cruzadas rotas**: un plan declara que depende de otro proyecto, y ese otro se movió.
7. **Replanificaciones que ningún cambio aprobado autoriza**, con los días que sobran.
8. **Vacíos de información**: proyectos sin presupuesto declarado, sin doliente, sin fecha de cierre.
9. **Lo que sigue igual**, en una línea. No se reexplica lo que no se movió.

## Lo que este skill no hace

No calcula. La desviación, los días de silencio y las proyecciones salen del script sobre las fichas. Este skill define **qué significa** cada número y **cuándo merece alerta**, no cómo se obtiene.

No opina sobre si un proyecto debe continuar. Eso es decisión de comité, y el material para tomarla lo prepara `steering-pack`.

No convierte un vacío en un juicio. Un proyecto sin documentación no está mal gestionado: está sin documentar, y eso es lo que se reporta.
