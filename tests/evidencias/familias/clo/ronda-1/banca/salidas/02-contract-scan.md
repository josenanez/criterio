# /criterio-legal:contract-scan 

Los 28 documentos de los contratos se convirtieron. Las seis fichas que ya existían coinciden con ellos, así que no cambié ninguna. El motor marcó cinco señales.

# Qué cambió en los contratos · Banco Andino · al 2026-10-06

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-06 · **Agente:** Fidel, versión 0.7.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Firma sin facultad según la matriz (`signed_without_authority`) | CTR-101: Diana Cruz firmó por 400.000.000,00 y la matriz de atribuciones no le da facultad para ese tipo y monto | — | `CTR-101…/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | Obligación vencida sin evidencia (`contract_obligation_overdue`) | CTR-104 · OBL-1 · Informe mensual de ejecución: venció el 2026-09-05 y no hay evidencia en 40-ejecucion/. Responsable: Licencias del Norte S.A.S. | 31 | `CTR-104…/10-contrato/contrato.md, cláusula 5` |
| 3 | Preaviso de no renovación cercano (`notice_deadline_near`) | CTR-104: el preaviso vence el 2026-11-01, en 26 días, y nadie decidió | 26 | `CTR-104…/10-contrato/contrato.md` |
| 4 | Garantía exigida sin póliza (`guarantee_missing`) | CTR-103: exige la garantía de calidad y no hay póliza aportada en 20-garantias/ | — | `CTR-103…/10-contrato/contrato.md, cláusula 9` |
| 5 | El registro no coincide con el documento (`register_differs_from_contract`) | CTR-102: valor 300.000.000,00 en el registro y 250.000.000,00 en el documento | — | `10-registro/registro-contratos.csv` fila 3 · `CTR-102…/10-contrato/contrato.md` |

La sección «El resultado» salió vacía en el reporte del motor, y la dejé así.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.
**Preguntas que hice:** ninguna en esta corrida.

**Fuentes:** `00-referencia/matriz-atribuciones.csv`, `10-registro/registro-contratos.csv` y los contratos de CTR-101, CTR-102, CTR-103 y CTR-104.

La corrida quedó registrada como `2026-10-06-contract-scan-1`. El reporte está en `estado-legal/900123456-banco-andino/contratos/reporte-contract-scan.md` y lo mostrado en `estado-legal/900123456-banco-andino/corridas/salida-contract-scan.md`.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-06, así que no hubo que registrarlos de nuevo.