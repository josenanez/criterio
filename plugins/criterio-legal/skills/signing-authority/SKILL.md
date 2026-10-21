---
name: signing-authority
description: "Cómo se compara quién firmó un contrato con la matriz de atribuciones de la organización —tipo, monto y vigencia de la facultad, otrosíes incluidos—, cuándo un documento no tiene la firma de las dos partes y cuándo el certificado de la contraparte estaba vencido al firmar. Úsalo al configurar la matriz de atribuciones o al revisar las firmas. Signing authority matrix, delegation of authority."
---

# Quién firmó, y con qué facultad

## La matriz de atribuciones

La define la organización —sus estatutos, su junta, sus poderes—; Fidel no la trae ni la deduce. Va en `00-referencia/matriz-atribuciones.csv` o `.xlsx`, una fila por facultad, con el modelo de `references/matriz-atribuciones.csv`:

| Columna | Qué va |
|---|---|
| `nombre` | La persona, escrita como firma en los contratos |
| `cargo` | Su cargo |
| `tipo` | El tipo de contrato que puede firmar, o `todos` |
| `monto_maximo` | El monto hasta el que puede firmar, en la moneda de la entidad |
| `desde`, `hasta` | La vigencia de la facultad; vacía si no vence |

Si una persona tiene facultades distintas por tipo, va una fila por tipo. Si la organización no tiene matriz, el chequeo queda sin hacer y el reporte lo dice: no se reemplaza por lo que «normalmente» puede firmar un gerente.

## Lo que compara el motor

- **Cada firmante de la entidad contra su facultad a la fecha de firma**, por tipo y por monto. Basta con que uno de los firmantes de la entidad tenga la facultad.
- **Cada otrosí con el monto acumulado**: un otrosí que lleva el contrato por encima de la facultad de quien lo firma levanta la señal, aunque el contrato original estuviera dentro.
- **La firma de las dos partes**: un contrato que ya empezó o un otrosí ya fechado sin la firma de las dos partes.
- **El certificado de la contraparte**: los días entre su expedición y la firma, contra la antigüedad máxima de la configuración.

## Lo que nunca se hace

- Decir si el contrato es válido, anulable o si obliga a la entidad. El motor compara con la matriz; las consecuencias las evalúa una persona.
- Suponer una facultad que la matriz no tiene, o un poder que no está en la carpeta.
- Corregir el nombre de un firmante para que cruce: si no coincide con la matriz, se pregunta.
