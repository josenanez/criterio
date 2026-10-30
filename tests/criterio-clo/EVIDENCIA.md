# criterio-clo · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada
vez, byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el
generador al sembrar cada defecto; el motor no la ve. Los nombres, las normas y las cifras son
sintéticos.

## Las entidades

| Carpeta del material | País | Industria | Defectos sembrados | Señales esperadas |
|---|---|---|---:|---:|
| `banca` | Colombia | banca | 10 | 10 |
| `cooperativas` | Ecuador | cooperativas | 9 | 9 |
| `retail` | Colombia | retail | 9 | 9 |
| `mineria` | Ecuador | minería | 9 | 9 |
| `control-co` | Colombia | — | 0 | 0 |
| `control-ec` | Ecuador | — | 0 | 0 |
| `banca-pe` | Perú | banca | 10 | 10 |
| `mineria-pe` | Perú | minería | 9 | 9 |
| `control-pe` | Perú | — | 0 | 0 |
| `retail-cl` | Chile | retail | 9 | 9 |
| `mineria-cl` | Chile | minería | 9 | 9 |
| `control-cl` | Chile | — | 0 | 0 |
| `banca-mx` | México | banca | 10 | 10 |
| `retail-mx` | México | retail | 10 | 10 |
| `control-mx` | México | — | 0 | 0 |
| `banca-br` | Brasil | banca | 10 | 10 |
| `retail-br` | Brasil | retail | 10 | 10 |
| `control-br` | Brasil | — | 0 | 0 |

Cada una trae su carpeta legal al 6 de octubre de 2026: la matriz de atribuciones y la de
obligaciones, el registro de contratos y la exportación de pagos, el índice de políticas con
cada política, el registro normativo, el registro de casos del canal, seis contratos con su
carpeta —el contrato, un otrosí que adiciona el valor y cambia la terminación, la póliza, el
certificado de la contraparte, la evidencia de cada obligación y, en uno, el acta que decide su
renovación— y tres periodos de cumplimiento, de julio a septiembre, con la evidencia de cada
obligación y el informe del periodo.

**Brasil, en portugués.** Las tres entidades de Brasil traen la misma carpeta en portugués, como la
tiene una empresa de allá: el contrato con sus cláusulas, el termo aditivo, la apólice de
seguro-garantia, la certidão de la Junta Comercial, la ata del comité, la matriz de alçadas y la de
obrigações, el registro de contratos y de pagamentos, las políticas, el boletim normativo y el
relatório de compliance. La ficha guarda sus valores como los define el skill —el tipo de contrato,
la garantía, la parte, la decisión—, y el arnés acepta el mismo valor dicho en portugués; lo que es
texto del documento —lo que se entrega, el cargo de quien firma— va en la clave como lo dice él.

## Lo que se siembra, y la señal que tiene que levantar

La columna «Dónde» nombra las entidades de Colombia y Ecuador. Las de Perú, Chile y México siembran los mismos casos con la identificación fiscal de su país; la lista exacta de cada una está en su clave, `material/<entidad>/clave.json`, en `siembra` y `esperado`.

**Fidel**

| Defecto | Señal | Dónde |
|---|---|---|
| Un contrato con renovación automática cuyo preaviso vence en 26 días, sin decisión | `notice_deadline_near` | banca |
| Un preaviso que venció el 1 de octubre sin decisión | `renewal_notice_missed` | minería |
| Un contrato sin renovación automática que vence en 50 días, sin decisión | `contract_expiring` | retail |
| Un contrato que terminó el 31 de agosto y el registro reporta vigente | `contract_expired_active` | cooperativas |
| Un contrato con carpeta y sin fila en el registro; una fila del registro sin documento | `register_mismatch` | cooperativas, retail |
| El registro con un valor mayor que el del documento | `register_differs_from_contract` | banca |
| El informe mensual que pedía el contrato, sin evidencia en `40-ejecucion/` | `contract_obligation_overdue` | banca |
| Un contrato de servicios firmado por quien solo puede firmar suministros | `signed_without_authority` | banca, minería |
| Un otrosí que lleva el contrato por encima de la facultad de quien lo firma | `signed_without_authority` | retail |
| Un contrato que empezó sin la firma de la contraparte | `unsigned_contract` | minería |
| El certificado de la contraparte con 75 días cuando se firmó | `counterparty_certificate_stale` | cooperativas |
| Pagos por encima del valor con su otrosí | `payments_over_value` | cooperativas |
| Un pago de septiembre a un contrato que terminó en julio | `payment_after_termination` | retail |
| La garantía de calidad exigida sin póliza | `guarantee_missing` | banca, minería |
| Una póliza que cubre dos meses después de la terminación cuando el contrato exige cuatro | `guarantee_expires_early` | retail |

**Constanza**

| Defecto | Señal | Dónde |
|---|---|---|
| Una obligación mensual que vencía el 5 de octubre sin evidencia de septiembre | `compliance_obligation_overdue` | banca, retail |
| Una obligación que la matriz declara cumplida sin evidencia | `compliance_done_without_evidence` | cooperativas, minería |
| Una obligación en plazo cuyo ciclo anterior tampoco tuvo evidencia | `compliance_evidence_stale` | cooperativas, minería |
| Una fila sin responsable; una sin fuente | `obligation_without_owner`, `obligation_without_source` | banca, retail |
| La matriz deja de citar la obligación de cumplimiento de un contrato | `contract_obligation_not_in_matrix` | banca, minería |
| El informe declara cumplido un periodo con señales abiertas | `declared_compliance_vs_evidence` | banca, retail |
| Una política con la revisión vencida | `policy_review_overdue` | retail |
| Una norma registrada hace 53 días sin evaluación; una que llegó en un boletín hace 42 días y no está en el registro | `regulatory_change_unassessed` | banca, minería, cooperativas |
| Una norma que aplica y ninguna obligación cita | `applicable_norm_not_in_matrix` | cooperativas |
| Un caso del canal abierto hace 39 días con un plazo de 15 | `report_case_overdue` | cooperativas, minería |

Las 25 señales de la familia se siembran al menos una vez. **Los controles no tienen ningún
defecto, y sí los casos que se parecen a uno**: un contrato que vence en 45 días con el acta
que decide renovarlo, un preaviso a 26 días con su decisión registrada (Ecuador), un otrosí
que cambia la terminación y el registro que la sigue, un contrato terminado que el registro
reporta terminado, una norma que llegó por boletín hace 8 días, un caso abierto dentro del
plazo y un informe que declara cumplido un periodo que lo está. Cualquier señal ahí es una
falla.

## Cómo se califica

`evaluar.py` arma la configuración que dejaría el setup, escribe la ficha de cada contrato y la
del periodo con lo que el agente tendría que extraer —está en la clave—, corre el motor de
Fidel y el de Constanza y compara cada señal por su nombre y su clave. **Una señal de más
cuenta igual que una de menos.** En los controles comprueba además que el estado de cada
contrato según sus fechas sea el del registro, que ningún saldo quede negativo, que ninguna
obligación esté vencida o sin evidencia y que la obligación de cumplimiento del contrato
cruce con la matriz.

## Lo que no prueba

La extracción. Que el agente procese el contrato, el otrosí, la póliza, el acta del comité, el
informe del periodo o el boletín y lo registre bien en la ficha lo prueba la ronda con el
agente, sobre este mismo material y contra esta misma clave. Tampoco prueba que el agente se
abstenga de opinar sobre la validez de un contrato: eso es una regla de los comandos, y la
pone a prueba la ronda.
