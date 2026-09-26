# criterio-pm

**Escuadra**, el agente del gerente de proyecto. Una instancia por proyecto.

[English](README.md) · Apache 2.0

**Estado: declarado, en construcción.** El diseño está cerrado y los scripts que comparte
con `criterio-pmo` ya están aquí y verificados. **Todavía no hay comandos ni skills**, así
que instalarlo hoy no hace nada. Nada se publica hasta que pasen los criterios de
aceptación.

## Qué va a hacer

El agente **no va a la reunión** — el gerente va. Lo que hace es que el gerente llegue con
la semana preparada: la agenda armada antes, el acta redactada después, el plan al día
contra la evidencia, y el informe de avance listo salvo una línea.

Su función central no la hace ninguna herramienta que un gerente use hoy: **el compromiso
dicho y no cumplido.** Las reuniones están llenas de *«yo lo tengo para el viernes»* y
nadie los registra.

## Lo que ya está decidido

**El agente no declara el estado del proyecto.** Eso lo hace el gerente. El agente le
muestra contra qué, y la diferencia entre las dos cosas es el hallazgo de más valor del
sistema.

**Escribe su propia ficha, y no la de nadie más.** Escuadra y Plomada leen los mismos
documentos y escriben dos fichas distintas que **nunca se fusionan**. Escuadra publica la
suya en la carpeta de gobierno del proyecto, Plomada la lee como lee cualquier documento,
y **cuando las dos citan y no coinciden, alguien vio un papel que el otro no vio**. Esa
es la señal.

**Se distribuye aparte de `criterio-pmo`**, con la aritmética copiada de ahí por una regla
que falla si las dos copias se separan. Un gerente de proyecto no necesita diecisiete
comandos de portafolio.

## Dónde está el diseño

Completo, con las tres clases de función, el flujo, lo que sigue siendo de la persona y
lo que falta por construir en orden:
[`docs/agents/project-manager.md`](../../docs/agents/project-manager.md).

El marco de la familia, las siete invariantes y la regla de un dueño por cosa:
[`docs/agents/README.md`](../../docs/agents/README.md).

## Criterios de aceptación

En [ACCEPTANCE.md](ACCEPTANCE.md). Nada se publica hasta que pasen.
