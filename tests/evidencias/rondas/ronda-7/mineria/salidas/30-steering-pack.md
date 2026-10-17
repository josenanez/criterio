# /criterio-portfolio:steering-pack 

El paquete de comité está listo y la corrida quedó registrada como `2026-10-17-steering-pack-1`. Lo que sigue es el material completo, igual que el archivo `/home/claude/banco/ronda-7/mineria/espacio/estado/corridas/salida-steering-pack.md`.

> Fichas cargadas: 13 (PRY-199 a PRY-211), `estado/records/`, con corte 2026-10-17. Cifras copiadas de `portafolio.py compute` de esta corrida. Términos vigentes (v0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17).
> No cargué los skills raid-taxonomy ni governance-artifacts: apliqué los criterios tal como los resume el comando.

# Comité de proyectos — 2026-10-23 (próximo comité según la configuración)
5 decisiones · 3 escalamientos sin decisión asociada · 12 de 13 proyectos con hallazgos (86 alertas en total)

Una advertencia de fondo: **ninguna ficha tiene autoridad de aprobación** (13 de 13). Cada «quién decide» de abajo es lo que se infiere de los documentos, no lo que establece un acta. Por eso el punto 1 va primero.

## Decisiones del comité anterior
No hay corrida previa de steering-pack ni acta de comité de portafolio en el estado. No puedo decir qué se decidió antes, y por eso tampoco qué se hizo con ello. Si existen actas fuera de `estado/`, no las busqué.

## Decisiones de hoy

### [1] ¿Quién tiene la facultad de aprobar cambios de alcance, tiempo y costo en cada proyecto?
**Proyecto:** los 13 · **Quién decide:** este comité (o quien lo convoca; no consta) · **Si no se decide hoy:** los puntos 2 y 3 no se pueden cerrar con validez, y siguen apareciendo cambios «aprobados por el comité» sin acta.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Nombrar una autoridad por proyecto y registrarla en el acta de cada uno | Sin cambio | Una ronda de firmas; plazo no calculado | Sin costo directo |
| B. Fijar una autoridad única para todo el portafolio con umbrales | Sin cambio | Más rápido; concentra decisiones | Sin costo directo |
| C. No decidir | — | Los cambios siguen sin respaldo | — |

**Recomendación:** A. Los proyectos nombran comités distintos (Ambiental, de Operaciones, de Seguridad), y una autoridad única sería una decisión de diseño que ningún documento respalda.

### [2] PRY-205 · CC-01: ¿se aprueba la ampliación de alcance (+75 días, 150.000.000 COP)?
**Proyecto:** PRY-205 Sistema de gestión de seguridad · **Quién decide:** no determinable (autoridad vacía). El comité que figura es el Comité de Seguridad y el sponsor es Ricardo Salas, según un acta del 2026-10-13. · **Si no se decide hoy:** la línea base ya se movió 75 días sin autorización (`rebaseline_unauthorized`) y la solicitud sigue pendiente.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar | Se amplía | Fin 2027-04-07 (la fecha ya está movida) | +150.000.000 COP; la proyección ya está 3.4% sobre lo aprobado, sin contar esta solicitud (no verifiqué si la incluye) |
| B. Rechazar y devolver la línea base | No se amplía | Se revierte el movimiento de 75 días; la fecha original no consta en lo que leí | Sin costo adicional |
| C. Aprobar con condiciones (acreditar primero lo que el informe declara) | Se amplía tras la acreditación | Más de 75 días, sin calcular | +150.000.000 COP |

**Recomendación:** C. El informe del 2026-10-05 declara verde con 23% de avance, y el plan respalda entre 75% y 100%. Esa distancia no se puede asumir. No es un punto de rechazo: lo que falta es evidencia.

### [3] ¿Se ratifican los cambios «aprobados» sin acta (PRY-200, 202, 206, 209)?
**Quién decide:** no determinable (ver punto 1) · **Si no se decide hoy:** hay 4 cambios con efecto de cronograma y costo ya aplicado, sin decisión registrada.

| Proyecto | Cambio | Tiempo | Costo | Qué consta |
|---|---|---|---|---|
| PRY-200 | CC-01 | +41 días (10.7% sobre original) | 82.000.000 COP | «el comité», sin nombre ni acta |
| PRY-202 | CC-01 | +115 días (25.8% sobre original) | 230.000.000 COP | «Comité», según la propia solicitud; sin minuta |
| PRY-206 | CC-01 | +47 días (11.5% sobre original) | 94.000.000 COP | «el comité», sin nombre ni acta; **la línea base no se actualizó** |
| PRY-209 | CC-01 | +51 días (17.3% sobre original) | 102.000.000 COP | «el comité», sin nombre ni acta |

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ratificar los cuatro hoy y levantar acta | Se amplía en los cuatro | Se confirman los días de la tabla | Se confirman los montos de la tabla |
| B. Ratificar solo los que tengan sustento; devolver el resto | Variable | Variable | Variable |
| C. Tratarlos como no aprobados hasta que haya acta | No se amplía | Se revierte a la base anterior | Sin costo adicional |

**Recomendación:** B, con una condición: PRY-206 se ratifica solo si se registra su línea base nueva, y PRY-202 solo si se le da cobertura de costo (punto 5, proyección 28.9% sobre lo aprobado). El motivo es que los cuatro superan el 10% de desviación de tiempo que fija la configuración.

### [4] ¿Se retienen los pagos a proveedores con facturación sin entrega aceptada?
**Proyectos:** PRY-201, 204, 207, 208 · **Quién decide:** no determinable · **Si no se decide hoy:** las facturas ya emitidas siguen sin entregable aceptado.

| Proyecto · proveedor · contrato | Facturado | Aceptado | Entregables vencidos |
|---|---|---|---|
| PRY-201 · Geotecnia Aplicada · CT-393 | 337.474.541 | 0 | 2 (102 y 25 días) |
| PRY-201 · Geotecnia Aplicada · CT-663 | 546.514.606 | 402.930.357 (diferencia 143.584.249) | 0 |
| PRY-204 · Ingeniería Minera del Sur · CT-734 | 213.183.796 | 0 | 2 (331 y 189 días) |
| PRY-207 · Geotecnia Aplicada · CT-367 | 312.596.415 | 0 | 1 (31 días) |
| PRY-208 · Geotecnia Aplicada · CT-929 | 319.737.266 | 0 | 2 (100 y 8 días) |

Geotecnia Aplicada aparece en tres proyectos (201, 207, 208), así que esto afecta a más de un proyecto y excede a cualquier gerente.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Retener pagos y notificar a ambos proveedores hasta que haya acta de recibo | Sin cambio | Puede frenar al proveedor | Sin costo directo; el riesgo contractual no está evaluado |
| B. Retener solo la diferencia de PRY-201 CT-663 y revisar el resto | Sin cambio | Menor fricción | La diferencia de 143.584.249 queda retenida |
| C. No retener | Sin cambio | Sin fricción | Se mantiene el pago sin entrega |

**Recomendación:** A para los contratos con aceptado en 0, y B para CT-663. Los contratos con 0 entregables aceptados son los que más preocupan. No tengo los contratos, así que no sé qué permiten.

### [5] PRY-211 · ¿cómo se cubre la proyección de 20.3% sobre el presupuesto aprobado?
**Proyecto:** PRY-211 Control de polvo en vías · **Quién decide:** no determinable · **Si no se decide hoy:** no hay solicitud de cambio abierta y el informe del 2026-10-14 declara amarillo; el sobrecosto proyectado no tiene dueño.

Presupuesto aprobado 6.800.000.000 COP; proyección 8.178.934.417 COP.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ampliar el presupuesto con solicitud de cambio formal | Sin cambio | Sin cambio | Hasta 8.178.934.417 COP en total |
| B. Reducir alcance hasta la cifra aprobada | Se reduce; qué sale no consta | Sin calcular | 6.800.000.000 COP |
| C. Pedir al gerente un plan de recuperación antes de decidir | Sin cambio | Una ronda | Sin costo; el sobrecosto sigue |

**Recomendación:** C. Hay 3 hitos declarados cumplidos sin evidencia y un avance declarado de 39% contra 75%–100% que respalda el plan. Antes de ampliar presupuesto hay que saber dónde está el proyecto de verdad.

## Escalamientos sin decisión asociada
| Proyecto | Qué | Desde cuándo | Qué se necesita |
|---|---|---|---|
| PRY-201 | Hito «Licencia y permisos obtenidos» vencido; informe declara verde | Venció el 2026-10-06 (11 días) | Fecha comprometida y quién la responde |
| PRY-202 | 3 compromisos reprogramados 5 o 6 veces (Javier Hoyos 6, Gustavo Neira 5, Camilo Beltrán 5), más 5 vencidos y 2 sin fecha | Desde 2026-09-08 el más antiguo | Que el patrocinador (Laura Vélez, según el acta) intervenga o reasigne |
| PRY-202 | Informe verde con 89% de avance; el plan respalda 40%–60%, con proyección de costo 28.9% sobre lo aprobado y 25.8% de atraso | Informe del 2026-10-16 | Que el gerente justifique el estado o lo cambie |

No hay proyectos en silencio: el mayor es PRY-208 con 13 días, bajo el umbral de 15.

## Para conocimiento
- **PRY-199:** sin alertas. Verde, 20%, respaldado por el plan (20%–40%).
- **PRY-200:** amarillo; 2 hitos cumplidos sin evidencia y 1 compromiso vencido (7 días, Óscar Ramírez).
- **PRY-203:** amarillo; 27% declarado contra 100% del plan, que marca 5 hitos de 5 como cumplidos sin evidencia. Cierre planeado 2026-09-17, vencido hace 30 días.
- **PRY-204:** verde contradicho; plan 100% contra 31% declarado; 5 hitos sin evidencia; fin 2026-07-24.
- **PRY-206:** rojo declarado; 52% contra 100% en el plan; 5 hitos sin evidencia.
- **PRY-207:** verde con licenciamiento vencido y facturación sin entrega (punto 4).
- **PRY-208:** amarillo; 2 hitos sin evidencia, 2 entregables vencidos (punto 4).
- **PRY-209:** verde contradicho; 3 hitos sin evidencia; 1 compromiso vencido (20 días, Rubén Cárdenas).
- **PRY-210:** verde; solo 2 hitos sin evidencia.
- **PRY-201, 205, 211:** ver arriba.

## Anexo
**Hitos declarados «cumplidos» sin evidencia de aceptación:** en 11 de 13 proyectos (todos menos PRY-199 y PRY-207). La mayoría de las fichas no tiene ninguna fuente marcada como evidencia (`evidence: 0` en las 13), y las demás son declaraciones del gerente o fuentes sin marcar. Esto no es una decisión del comité, pero explica por qué los puntos 2 a 5 reciben recomendación condicionada.

**Informes en verde contradichos por alertas propias (7):** PRY-201, 202, 204, 205, 207, 209, 210.

**Vacíos de información:**
- Autoridad de aprobación: 13 de 13 sin dato. Fase del proyecto: 13 de 13 sin dato.
- Producto vinculado vacío o sin dato en PRY-201, 202, 205, 206, 209, 210 y 211.
- Datos con más de 12 meses de antigüedad en PRY-200, 203, 204, 205, 206 y 211 (identidad, plan, presupuesto y, en 204, proveedor).
- PRY-202 trae además un `pm_record` propio con los mismos campos vacíos; no lo cotejé con la ficha de portafolio.
- No leí los documentos fuente de nuevo en esta corrida: todo sale de las fichas y de `compute`.
- No conozco los contratos, así que ignoro las cláusulas de pago a proveedores.

**Contradicciones de portafolio abiertas:** ninguna reportada por `compute` (`conflicts` vacío en los 13).

---
Criterio plugin criterio-portfolio v0.3.13 · 13 fichas (corte 2026-10-17) · campos inciertos: autoridad, fase, evidencia de hitos y de entregables, datos viejos listados arriba · Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Después:** cuando el comité sesione, puedo registrar sus decisiones en las fichas. Con eso se cierra el ciclo y el material del próximo comité parte de lo decidido. En esta prueba no pregunté nada y no registré ninguna decisión.