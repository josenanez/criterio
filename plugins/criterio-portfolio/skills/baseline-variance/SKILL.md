---
name: baseline-variance
description: "Línea base de solo agregar y cálculo de desviación en tiempo y en costo: contra la línea base original y contra la vigente, presupuesto aprobado, comprometido, ejecutado y proyección. Úsalo al medir avance o atraso, al replanificar, al aprobar un cambio de fechas o de presupuesto, y al reportar cumplimiento de hitos. Baseline, variance, budget control."
---

# Línea base y desviación

## La regla que sostiene todo

**La línea base es de solo agregar.**

Cuando cambia el plan, si se sobrescribe la línea base desaparece el historial de atraso. Así es exactamente como las organizaciones esconden el atraso: se replanifica, el semáforo vuelve a verde, y a nadie le queda rastro de que el proyecto llevaba ocho meses de retraso acumulado.

Cada nueva línea base entra como registro nuevo, con su fecha, su motivo y el documento que la aprobó. Ninguna reemplaza a la anterior.

## Dos desviaciones, siempre las dos

Toda medición de avance se reporta contra dos referencias:

- **Contra la línea base original** — cuánto se ha desviado el proyecto desde que se aprobó. Es el número que nadie quiere ver y el único que dice la verdad acumulada.
- **Contra la línea base vigente** — cuánto se está desviando del plan actual. Es el número operativo, el que le sirve al gerente esta semana.

Reportar solo la vigente es lo que hace que un proyecto con tres replanificaciones se vea sano. Reportar solo la original es injusto con un gerente que heredó el proyecto. Van las dos, una al lado de la otra, con el número de replanificaciones entre paréntesis.

## Cómo se lee una replanificación

Tres replanificaciones en un año no es un dato neutro: es un hallazgo. Se reporta el conteo, las fechas y el motivo declarado de cada una. Si alguna no tiene motivo documentado, eso también se dice.

## La replanificación contra lo que se autorizó

Que la línea base no se sobrescriba conserva el historial. No prueba que la replanificación se haya quedado dentro de lo que el comité aprobó, y esa es una resta:

**días que se movió la línea base** − **días que autorizaron los cambios aprobados** = **días que nadie autorizó**

El script la hace y devuelve `changes.baseline_moved_days`, `changes.approved_time_days` y `changes.unauthorized_days`; si sobran días levanta `rebaseline_unauthorized`. Cuando no hay ni un cambio registrado y la línea base se movió, el resultado es el total del movimiento, que es justo el caso que hay que ver.

Cómo se nombra importa. **No es que alguien haya movido fechas sin permiso: es que ningún documento de la carpeta autoriza esa diferencia.** La autorización puede haber existido en un comité que no dejó acta. Se reporta el hueco documental y se pregunta, no se acusa.

Dos casos más que el script separa en vez de resolver por su cuenta:

- Un cambio aprobado con impacto en tiempo y sin línea base nueva posterior sale en `approved_without_new_baseline`. La decisión existe y el plan no la refleja.
- Un impacto escrito en meses —*"dos meses"*— queda en `time_impact_unreadable` y no entra en la suma. Un mes no tiene un número fijo de días, y un número inventado aquí contamina todo lo demás. Las semanas sí convierten.

  Con una consecuencia que conviene tener presente al leer un informe, y que salió de la
  corrida sintética: si el impacto no se pudo leer, el cambio no suma a
  `approved_time_days` **ni** aparece en `approved_without_new_baseline`. Solo sale en la
  lista de ilegibles. Cada paso es correcto y el resultado es que un cambio aprobado real
  queda fuera del control de replanificación. Un impacto en meses hay que preguntarlo.

## Desviación en tiempo

Se calcula sobre hitos, no sobre porcentajes de avance declarados. Un porcentaje lo declara el gerente; una fecha de hito la sustenta un documento.

Para cada hito: fecha de línea base, fecha vigente, y si ya pasó, si hay evidencia de cumplimiento. Un hito cuya fecha pasó sin evidencia no está "en curso": está **vencido sin evidencia**, y así se nombra.

## Desviación en costo

Cuatro cifras, y ninguna se asume:

| Cifra | Qué es |
|---|---|
| **Aprobado** | Lo que autorizó el comité o la instancia que corresponda |
| **Comprometido** | Lo que ya está amarrado en contratos y órdenes, se haya pagado o no |
| **Ejecutado** | Lo efectivamente causado o pagado |
| **Proyección** | Lo que el proyecto declara que costará al cierre |

Los errores frecuentes que hay que nombrar cuando aparezcan:

- Reportar ejecutado contra aprobado ignorando el comprometido. Un proyecto con 40% ejecutado y 95% comprometido no tiene holgura; tiene el presupuesto agotado.
- Tratar la proyección como un dato duro. Es una declaración: lleva su fuente y su fecha como cualquier otra.
- Mezclar monedas. Si hay contratos en otra moneda, se dice, y no se convierte sin declarar la tasa y su fecha.

## Lo que hace el script y lo que haces tú

El script calcula: días de desviación, porcentajes, conteo de replanificaciones, saldos, proyecciones aritméticas. No se calcula a mano ni dentro del razonamiento.

Tú interpretas: qué significa esa desviación, si el motivo declarado explica el atraso, si la replanificación fue un ajuste razonable o una forma de limpiar el semáforo.

## Una cifra se copia, no se reescribe

**Ninguna cifra que el script calculó se vuelve a teclear.** Se copia del campo, tal cual,
con todos sus dígitos. Suena obvio y no lo es: en una corrida sobre cincuenta proyectos el
agente escribió el presupuesto aprobado con tres ceros de más —303.100.000.000.000 en vez
de 303.100.000.000— mientras las otras tres cifras del mismo cuadro salían exactas y la
desviación quedaba bien calculada. El script tenía razón; el error fue al transcribir.

Un presupuesto mil veces mayor no es un defecto de formato. Es la primera cosa que mira un
director financiero, y destruye la credibilidad del documento entero antes de que nadie
llegue al hallazgo que importa.

Las tres reglas que lo evitan:

- **Se copia del campo del script**, nunca de una lectura del documento ni de una suma
  hecha en el razonamiento.
- **La misma cifra aparece igual en todas partes del informe.** Si el resumen dice
  «$303.100M» y el detalle dice otra cosa, una de las dos está mal y el lector no sabe
  cuál. Antes de entregar, se comparan.
- **Un total se contrasta con sus partes.** Si el aprobado no está entre el comprometido y
  algo del mismo orden de magnitud que la proyección, no se publica: se revisa.

## Cuando no hay línea base

Es el caso más común en una PMO real: el proyecto arrancó sin plan aprobado, o el plan existe pero nadie lo marcó como línea base.

No se inventa una. Se reporta que **no hay línea base**, se nombra el documento más antiguo que declare fechas, y se ofrece tomarlo como línea base cero con la aprobación del gerente. Sin esa aprobación, el proyecto se reporta sin desviación medible, que es la verdad.
