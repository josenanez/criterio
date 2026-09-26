# criterio-pm

**Samuel**, el agente del gerente de proyecto. Una instancia por proyecto.

[English](README.md) · Apache 2.0

**Estado: en construcción.** El diseño está cerrado, y los scripts y los ocho skills que
comparte con `criterio-pmo` ya están aquí y verificados. **Todavía no hay comandos**, así
que no hay nada que invocar — pero los skills se cargan solos cuando el tema aparece.
Nada se anuncia como terminado hasta que pasen los criterios de aceptación.

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

**Escribe su propia ficha, y no la de nadie más.** Samuel y Vera leen los mismos
documentos y escriben dos fichas distintas que **nunca se fusionan**. Samuel publica la
suya en la carpeta de gobierno del proyecto, Vera la lee como lee cualquier documento,
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

## Los ocho skills que ya trae

Se cargan solos cuando el tema aparece, así que **instalarlo hoy sí hace algo**: el
método está, aunque todavía no haya comandos que lo pongan en marcha. Son copias
literales de `criterio-pmo`, porque un riesgo es un riesgo lo mire quien lo mire y la
ficha es el contrato de datos de toda la familia.

| Skill | Qué encapsula |
|---|---|
| `project-record` | La ficha: esquema, reglas de extracción, citación, estados de campo, qué hacer cuando dos documentos se contradicen |
| `document-intake` | Qué documento hay que releer y cuál no, qué formatos se pueden leer y con qué |
| `commitment-tracking` | **La función central de Samuel.** Compromisos dichos en reuniones: extracción, estados, qué cuenta como evidencia, y el que se repite con fecha nueva cada vez |
| `raid-taxonomy` | Las cuatro categorías y cómo distinguirlas, valoración, criterio de escalamiento |
| `baseline-variance` | Línea base de solo agregar, desviación contra la original y contra la vigente, las cuatro cifras del presupuesto |
| `governance-artifacts` | Acta, comité, control de cambios y cierre: qué contiene cada uno y quién decide qué |
| `vendor-control` | Contrato contra evidencia de recibo contra facturación, con monto por entregable |
| `project-diagnosis` | El diagnóstico desde cero: en qué orden se lee y cuándo la respuesta es que no se puede diagnosticar |

Lo que **no** trae, por alcance y no por casualidad: `portfolio-health` y
`portfolio-history` solo tienen sentido mirando el conjunto, y un gerente de proyecto no
mira el conjunto. Para eso está [`criterio-pmo`](../criterio-pmo/README.es.md).

## Criterios de aceptación


En [ACCEPTANCE.md](ACCEPTANCE.md). Nada se publica hasta que pasen.
