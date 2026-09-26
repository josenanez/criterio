---
name: raid-taxonomy
description: "Riesgos, supuestos, incidencias y dependencias: qué es cada uno, cómo se distinguen, cómo se valoran y cuándo escalan. Úsalo al levantar o revisar un registro RAID, al leer minutas buscando riesgos que nadie registró, al preparar comité, o cuando alguien confunda un riesgo con un problema. RAID log, risks, assumptions, issues, dependencies."
---
<!-- COPIA · la fuente es plugins/criterio-pmo/skills/raid-taxonomy/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# RAID

## Por qué importa la distinción

Las cuatro categorías se confunden a diario, y la confusión tiene consecuencias operativas: un riesgo se mitiga, una incidencia se resuelve, un supuesto se valida y una dependencia se coordina. Llamar "riesgo" a algo que ya ocurrió hace que se le asigne un plan de mitigación a un problema que necesita una decisión hoy.

| | Qué es | Tiempo verbal | Qué se hace |
|---|---|---|---|
| **Riesgo** | Algo que puede pasar y dañaría el proyecto | Futuro, incierto | Se mitiga o se acepta |
| **Supuesto** | Algo que se está dando por cierto sin haberlo verificado | Presente, no verificado | Se valida o se convierte en riesgo |
| **Incidencia** | Algo que ya pasó y está afectando el proyecto | Presente, cierto | Se resuelve, con doliente y fecha |
| **Dependencia** | Algo que el proyecto necesita de otro y no controla | Futuro, ajeno | Se coordina y se confirma |

**La prueba rápida:** si ya pasó, es incidencia. Si depende de alguien fuera del proyecto, es dependencia. Si se está asumiendo sin verificar, es supuesto. Lo que queda es riesgo.

## El supuesto es el que más daño hace

Nadie levanta supuestos porque no duelen. Un supuesto que falla se convierte en incidencia sin haber pasado nunca por riesgo, y entonces el registro muestra un problema que "apareció de la nada".

Los supuestos que más veces fallan y conviene buscar explícitamente: disponibilidad de una persona clave, que un tercero entregue a tiempo, que un ambiente o una licencia esté listo, que una aprobación sea trámite, que el alcance no cambie, que el equipo siga completo.

## La dependencia es la menos gestionada

Un proyecto declara que depende de otro. El otro no lo sabe, o lo sabe y se movió.

Por eso toda dependencia se registra **con el código del proyecto del que depende**, no con una frase. Eso permite que el cruce de portafolio detecte que el proyecto B declaró una dependencia del proyecto A, y que A movió la fecha. Ese cruce es de los hallazgos que un gerente de PMO no puede obtener hoy de ninguna herramienta.

Una dependencia sin confirmar por la contraparte es una dependencia **declarada**, no acordada. La diferencia se reporta.

## Valoración

Cada riesgo lleva probabilidad e impacto, en la escala que use la organización — si no hay una definida, alta, media y baja, y se dice que se usó esa. No se inventa una escala numérica que aparente precisión donde no la hay.

Lo que sí es obligatorio, y casi nunca está: **doliente y fecha**. Un riesgo sin doliente no se gestiona, es decoración. Cuando falte, se reporta como hallazgo, no se rellena.

## Riesgos que nadie registró

Las minutas y las transcripciones están llenas de riesgos dichos al pasar: *"si el proveedor no entrega en octubre estamos en problemas"*, *"eso depende de que aprueben el presupuesto"*. Nadie los pasa al registro.

Recogerlos es una de las cosas de más valor que hace este plugin. Cada uno entra citando la reunión y la fecha en que se dijo, y se marca como **no registrado formalmente**, para que el gerente decida si lo formaliza. No se inventan riesgos que nadie mencionó.

## Cuándo escala

Un ítem sube al comité cuando cumple cualquiera de estas:

- Excede la autoridad del gerente de proyecto, en monto o en alcance.
- Afecta a otro proyecto del portafolio.
- Lleva más de dos períodos de reporte sin movimiento y sigue abierto.
- Su doliente está fuera del proyecto y no ha respondido.
- La mitigación acordada venció sin evidencia.

Escalar no es quejarse: es llevar una decisión que alguien más tiene que tomar. Por eso lo que sube al comité lleva la decisión formulada, no solo el problema.
