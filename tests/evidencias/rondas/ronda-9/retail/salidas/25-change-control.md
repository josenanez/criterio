# /criterio-portfolio:change-control PRY-200 mover la salida a producción 30 días

## Solicitud de cambio — PRY-200 Tienda en línea — 2026-10-17

Mover la salida a producción 30 días lleva el cierre del 2026-11-23 al 2026-12-23. No se puede aprobar todavía: faltan el solicitante, el motivo, el costo y la autoridad que decide.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17 (versión 0.4.0), así que no registré nada nuevo. Como nadie podía responder, tomé la respuesta sugerida en cada pregunta.

Leí «la salida a producción» como el hito «Despliegue en la cadena» (2026-11-23), que en la línea base coincide con el cierre. Esa lectura es mía.

**Impacto**
| Dimensión | Hoy | Con el cambio | Diferencia |
|---|---|---|---|
| Alcance | Componentes 1, 2 y 3, sin detalle | No declarado | Sin impacto declarado |
| Tiempo | 2026-11-23 | 2026-12-23 | +30 días (6,6 % del plan, bajo el umbral de 10 %) |
| Costo | Proyección 6.859.551.454 COP sobre 6.800.000.000 aprobados | No calculable | Sin dato |

- **Quién absorbe lo no declarado:** el equipo y el proveedor trabajarían un mes más sin presupuesto, o se recortaría alcance sin decirlo.
- **Costo previo:** el proyecto ya proyecta cerrar 59.551.454 COP (0,9 %) por encima de lo aprobado, antes de este cambio.

**Efecto en el portafolio**
- El cálculo no alcanza ningún proyecto. Ninguno declara depender de PRY-200, y PRY-200 declara «Ninguna».
- Eso dice que no hay dependencias declaradas, no que no existan.
- No sé cuántos días se mueve cada actividad, porque la ficha no tiene holgura por actividad.

**Quién decide**
- El acta no declara quién aprueba cambios de fecha. Ese es el hallazgo de fondo.
- Va a comité. Propongo el Comité Comercial, que aprobó el presupuesto, con Carlos Peña (patrocinador) y Sandra Gil (gerente). Es una propuesta mía, no algo que diga el acta.

**Si no se aprueba**
- El cierre sigue el 2026-11-23, a 37 días.
- Hay un hallazgo de seguridad en medios de pago abierto desde el 2026-10-09 y sin responsable.
- Dos entregables del proveedor CT-497 están vencidos y sin acta de recibo: Licenciamiento de la plataforma (2025-12-27) y Configuración del catálogo (2026-09-04), de 445.577.090 COP cada uno.

**Si se aprueba**
- Línea base 2: cierre 2026-12-23, presupuesto sin monto por definir, motivo por registrar. La v1 no se toca.
- Desviación acumulada contra la original: +30 días y +59.551.454 COP de sobrecosto proyectado, más el mes adicional sin calcular.

**Hallazgos que cambian la decisión**
- El informe del 2026-10-09 dice que el despliegue «se reprogramó», pero el plan sigue en 2026-11-23 y no hay línea base 2. Puede haber un movimiento ya hecho que ningún documento autoriza.
- Ese mismo informe declara estado verde, y eso no cuadra con una fecha movida y un hallazgo de seguridad abierto.

**Falta antes de decidir**
1. Quién pide el cambio y por qué, por escrito.
2. La fecha real vigente del despliegue.
3. Las fechas del congelamiento de fin de año, para saber si el 2026-12-23 cae dentro.
4. El costo del mes adicional y quién lo financia.
5. Quién aprueba cambios en este proyecto.
6. Un responsable para el hallazgo de seguridad.

Si el comité lo aprueba, el siguiente paso es registrar la línea base 2. Puedo preparar el paquete para el comité con `/steering-pack`.

Dejé la corrida registrada. El texto completo está en `estado/corridas/salida-change-control.md`.