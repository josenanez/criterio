---
name: selection-policy
description: "La política de selección de la organización y los registros de Cándido: el plazo de cobertura de una vacante, los días de conservación de los datos de los candidatos, el registro de vacantes, el de autorizaciones y la exportación del ATS con sus columnas. Úsalo en el setup de Cándido y cuando una tabla no trae las columnas esperadas. Selection policy, retention, consent register, ATS export."
---

# La política de selección

**Los plazos los fija la organización.** Salen de su política de selección, en `00-referencia/`, y van a la configuración con su cita:

- `selection.vacancy.target_days`: los días que da la política para cubrir una vacante, contados desde su apertura. Una vacante puede traer su propio plazo en el registro (`plazo_dias`), y ese manda.
- `selection.data.retention_days`: los días que la política conserva los datos de un candidato cuyo proceso terminó sin quedar en el cargo, contados desde la fecha en que terminó.
- `selection.prohibited_requirements`: lo que la política prohíbe pedir en un perfil —la edad, el sexo, el estado civil, la fotografía—. Se suma a los datos sensibles de la ley del país.
- `selection.publish`: si los reportes de candidatos se publican en Rostrum. Por omisión, no: se publican los perfiles y el estado de las vacantes, y los candidatos solo con su identificador si la configuración lo dice.

Si la política no trae un plazo, **no se inventa**: se le pregunta a la persona y se registra su respuesta con la fecha.

## Los registros

- **El registro de vacantes** (`20-vacantes/`): cada vacante con su perfil, su fecha de apertura y la de su cierre. Abierta es la que no tiene cierre.
- **El registro de autorizaciones** (`40-autorizaciones/`): una fila por candidato con la fecha en que autorizó el tratamiento de sus datos. Una autorización posterior a recibir sus datos es una señal: la ley de cada país la pide antes (F-10 a F-17).
- **La exportación del ATS** (`50-ats/`): cada candidato con su vacante, su postulación, su etapa y la fecha de esa etapa. Un proceso terminado —no seleccionado, retirado, descartado— empieza a contar la conservación.

Las columnas que el motor reconoce están en **talent-intake**. Lo que no reconozca va en `columns`, con su cabecera tal cual.
