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

## Umbrales por defecto

Son los valores que quedan en la mayoría de las instalaciones. Están calibrados para que el agente hable poco y cuando habla importe. Se cambian en `umbrales.yaml` del estándar.

| Señal | Habla cuando |
|---|---|
| Hito vencido | La fecha pasó y no hay evidencia de cumplimiento |
| Proyecto en silencio | 15 días sin documento nuevo |
| Desviación contra línea base | Supera 10% en tiempo o en costo |
| Compromiso vencido | Pasó la fecha y no hay evidencia |
| Contradicción entre documentos | Siempre — no lleva número |
| Presupuesto | Ejecutado supera 90% de lo comprometido |
| Cambio de gobierno | Siempre |

**El silencio cuando no pasó nada es la característica, no la falla.** Un agente que reporta todos los lunes haya o no noticia se ignora en un mes.

## Las tres defensas contra el dato viejo

Un campo deja de ser cierto sin que ningún archivo cambie. Contra eso hay exactamente tres mecanismos, y los tres se usan.

**1. Antigüedad.** Todo dato se reporta con la fecha de su fuente. Nunca *"el patrocinador es X"*; siempre *"según el acta de 2025-03, el patrocinador es X, sin confirmación posterior"*.

**2. Contradicción cruzada.** La minuta de la semana pasada nombra a otra persona que el acta de constitución. Es el hallazgo de más valor que produce el agente. Se reporta siempre, con las dos fuentes y las dos fechas, y va con pregunta al gerente.

**3. Confirmación periódica.** Mensual. **Cinco campos por corrida**, elegidos por importancia y no por antigüedad: patrocinador, gerente asignado, presupuesto aprobado, fecha comprometida de cierre y alcance. Un campo secundario simplemente carga su antigüedad visible en el informe y no gasta una pregunta.

Si preguntas por cuarenta campos, no responde nadie. Si preguntas por cinco, los responden.

## Qué se reporta del portafolio, y en qué orden

1. **Lo que cambió desde la corrida anterior.** Es lo primero porque es lo único que el gerente no sabe ya.
2. **Contradicciones abiertas.**
3. **Hitos vencidos sin evidencia.**
4. **Proyectos en silencio**, con cuántos días.
5. **Dependencias cruzadas rotas**: un plan declara que depende de otro proyecto, y ese otro se movió.
6. **Vacíos de información**: proyectos sin presupuesto declarado, sin doliente, sin fecha de cierre.
7. **Lo que sigue igual**, en una línea. No se reexplica lo que no se movió.

## Lo que este skill no hace

No calcula. La desviación, los días de silencio y las proyecciones salen del script sobre las fichas. Este skill define **qué significa** cada número y **cuándo merece alerta**, no cómo se obtiene.

No opina sobre si un proyecto debe continuar. Eso es decisión de comité, y el material para tomarla lo prepara `steering-pack`.

No convierte un vacío en un juicio. Un proyecto sin documentación no está mal gestionado: está sin documentar, y eso es lo que se reporta.
