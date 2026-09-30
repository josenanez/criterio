---
name: project-record
description: "La ficha de proyecto: el contrato de datos de Criterio. Define qué se sabe de un proyecto, cómo se extrae de la documentación que exista, cómo se cita, y cómo se declara lo que no está. Úsalo siempre que haya que leer documentación de proyectos, llenar o actualizar una ficha, consolidar portafolio, o cuando se hable de estado, avance, hitos, presupuesto o riesgos de un proyecto. Project record schema and extraction rules."
---
<!-- COPIA · la fuente es plugins/criterio-portfolio/skills/project-record/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# La ficha de proyecto

## Para qué existe

Es la espina de todo el plugin. Cada comando lee o escribe fichas; ningún comando lee documentos crudos por su cuenta. Eso es lo que permite consolidar cuarenta proyectos sin volver a leerlos, calcular en vez de opinar, y comparar una corrida contra la anterior.

Sin la ficha esto sería un juego de plantillas. Con la ficha es un sistema.

## Dos fuentes que no se mezclan

La ficha del gerente de proyecto es una **declaración**: lo que él afirma de su proyecto.
El hallazgo de la PMO es **evidencia**: lo que dicen los documentos.

Las dos se guardan. **La diferencia entre ambas es el hallazgo de más valor del sistema.** "El gerente reporta el hito en verde; la última minuta dice que el proveedor no entregó" es la conversación que hoy no se puede tener.

Nunca sobrescribas una con la otra.

## Dónde vive y en qué formato

Una ficha por proyecto, en `<estado>/records/<codigo>.json`. **Se almacena en JSON**, no en YAML: leer YAML exigiría instalar PyYAML en el equipo de quien lo use, y el script no tiene dependencias.

El esquema está en [references/schema.yaml](references/schema.yaml), en YAML porque es la especificación y se lee mejor con comentarios. Léelo antes de llenar una ficha.

Cada campo se guarda con cuatro cosas:

```yaml
sponsor:
  value: "María Restrepo, VP Operaciones"
  source: "20-seguimiento/2026-03-12-acta-comite.md"
  source_date: 2026-03-12
  state: found
```

- **value** — el dato.
- **source** — la ruta del documento de donde salió, exacta.
- **source_date** — la fecha del documento, no la de hoy. Es lo que permite saber si el dato envejeció.
- **state** — `found`, `not_found` o `ambiguous`.

## Reglas de extracción

**1. Todo campo lleva su cita, o declara que no está.** No hay tercera opción. Un campo sin `source` es un campo inventado.

**2. `not_found` es una respuesta correcta y esperada.** Escribirlo no es fallar. Adivinarlo sí. Si el presupuesto no aparece en ningún documento, el campo va `not_found` y el informe lo reporta como vacío de información, que es un hallazgo en sí mismo.

**3. Nunca leas un dato del documento base sin verificar si otro posterior lo reemplazó.** Un plan `v3` al lado de un `v2`, un otrosí, un acta de comité que cambió una fecha. El dato vigente es el del documento más reciente que hable de ese campo, y la cita apunta a ese documento, no al original.

**4. La fecha del documento sale del nombre del archivo cuando esté ahí.** La convención es `AAAA-MM-DD-tema.ext`. Leer la fecha del nombre no cuesta nada; abrir el archivo para buscarla, sí. Si el nombre no la trae, se toma de dentro del documento y se deja nota.

**5. No extraigas de nuevo lo que no cambió.** Si el hash del documento es el mismo de la corrida anterior, el campo que salió de ahí se conserva tal cual. La ficha es el caché.

**6. El modelo extrae; el script calcula.** Leer una fecha de hito es extracción. Restar días, proyectar desviación, sumar ejecutado contra comprometido es aritmética, y la aritmética no va aquí: va en el script. Si te encuentras calculando, estás haciendo el trabajo del lugar equivocado.

## Cuando dos documentos se contradicen

No elijas. Registra los dos:

```yaml
end_date:
  value: "2026-11-30"
  source: "10-plan/2026-02-01-cronograma-v2.xlsx"
  source_date: 2026-02-01
  state: ambiguous
  conflict:
    value: "2027-02-28"
    source: "20-seguimiento/2026-08-14-acta-comite.md"
    source_date: 2026-08-14
```

El campo queda `ambiguous`, `value` lleva el del documento más reciente, y la contradicción se levanta como alerta. **La contradicción entre documentos siempre se reporta, sin umbral.**

## Antigüedad del dato

Un campo no deja de ser cierto porque cambie el archivo. Deja de ser cierto porque cambió el mundo y nadie actualizó nada: despiden al patrocinador y el acta sigue nombrándolo.

Por eso `source_date` no es decorativo. Un dato tomado de un documento de hace dieciocho meses se reporta así: *"según el acta de 2025-03, sin confirmación posterior"*. Nunca como si fuera de hoy.

Los campos que envejecen peor son cinco: patrocinador, gerente asignado, presupuesto aprobado, fecha comprometida de cierre y alcance. Esos son los que la confirmación periódica pregunta.

## Cambio de gobierno

Nadie reexpide el acta de constitución porque se fue el patrocinador. Aparece en un correo o en una minuta.

Entonces cuando un documento reciente nombra a una persona distinta en un rol, **eso se levanta como evento**, no se sobrescribe en silencio: el campo queda `ambiguous` con las dos fuentes, igual que cualquier contradicción, y el cálculo lo separa como `governance_change` porque no es un defecto de la ficha. Cambio de patrocinador, de gerente o de composición del comité es hallazgo de portafolio aunque ningún cronograma se haya movido. Qué hace la señal está en `portfolio-health`.


## Cuando el proyecto tiene su propio agente

Un proyecto gestionado con `criterio-project` publica su ficha en la carpeta de gobierno,
como **`ficha-pm.json`**. Es un documento más del proyecto y se lee como tal.

**No la fusiones con la tuya.** Va entera en el campo `pm_record` de la ficha del
portafolio, tal como la leíste, y las dos conviven:

```json
{
  "identity": { "...": "tu lectura" },
  "pm_record": { "identity": { "...": "lo que publicó el gerente" } }
}
```

Es la séptima invariante —**una ficha, un escritor**— y la razón es que lo que sería un
conflicto de escritura se vuelve la señal: el código contrasta ocho campos y emite
`pm_vs_pmo` cuando los dos citan y no coinciden. **Tú no decides quién tiene razón**, y
tampoco copias un dato de la ficha del gerente a la tuya para «corregirla»: tu ficha es
tu lectura de los documentos, y si el gerente vio algo que tú no, el hallazgo es
exactamente eso.

Si no hay `ficha-pm.json`, `pm_record` no existe y no pasa nada. Es el caso normal.


## Estado declarado y evidencia son dos campos, y no se mezclan

Un hito y un entregable llevan `state` y `evidence`, y cada uno responde a una pregunta
distinta:

- **`state`** es lo que el documento declara. Si el cronograma dice `cerrado`, `state`
  es `met`; si dice `pendiente` o `en curso`, `pending`; si el informe dice que no se
  cumplió, `missed`. Se copia la declaración tal cual, con su fuente.
- **`evidence`** es la ruta del documento que **prueba** que se cumplió: un acta de
  recibo, un acta de comité que lo da por cerrado con fecha, un correo de aceptación.
  Si no existe, `evidence` queda vacío. Y nada más.

Lo que no se hace es dejar el hito en `pending` porque no encontraste el acta. La
primera medición real lo mostró en un barrido sobre cincuenta proyectos: el cronograma
declaraba cinco hitos cerrados, el agente no halló acta para ninguno, y los registró
como abiertos. El código vio cinco hitos vencidos y abiertos —`milestone_overdue`— cuando
lo que había era cinco hitos **declarados cerrados sin un documento que lo pruebe**
—`milestone_met_without_evidence`—, que es la señal que este sistema existe para dar y
que pide una acción distinta: no "apúrense", sino "muéstrenme el acta". Cincuenta y
cinco señales quedaron con el nombre equivocado por esa sola decisión.

La regla es una frase: **`state` dice lo que declaran; `evidence` dice lo que prueban.**
Que no haya prueba nunca cambia la declaración. Lo mismo vale para los entregables de un
proveedor: `accepted` es lo que el contrato o el informe afirma, y `evidence` es el acta
de recibo, o nada.

Y un acta de recibo cuenta como evidencia solo del hito o entregable que nombra. El acta
que certifica el ambiente de pruebas no prueba la integración con el core.

## Lo que nunca se hace

- Inventar un dato que no está en ningún documento.
- Citar un documento sin haberlo leído.
- Reportar un valor sin su fuente.
- Sobrescribir la línea base original. Ver el skill `baseline-variance`.
- Calcular dentro de la ficha.
- Afirmar un estado que ningún documento sustenta. "No está declarado en ninguna parte" es la respuesta correcta.
- Cambiar `state` porque falta la evidencia. Se registra la declaración y el vacío de prueba, y el código nombra la señal.
