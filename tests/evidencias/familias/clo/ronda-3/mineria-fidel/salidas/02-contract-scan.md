# /criterio-legal:contract-scan 

Corrida de prueba sin interfaz: los términos ya estaban vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). Los 6 contratos eran nuevos para el inventario. Las fichas ya coincidían con los documentos y no las reescribí. El motor detectó 4 señales.

# Qué cambió en los contratos · Minera Cóndor · al 2026-10-06

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-401: Mauricio León firmó por 400,000.00 y la matriz de atribuciones no le da facultad para ese tipo y monto | 400,000.00 | — | — | `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | Pasó la fecha límite del preaviso de un contrato con renovación automática sin una decisión registrada (`renewal_notice_missed`) | CTR-401: el preaviso venció el 2026-10-01 sin decisión; el contrato se prorroga en sus términos el 2026-10-31 | — | — | 5 | `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md` |
| 3 | El documento no tiene la firma de las dos partes y el contrato ya empezó (`unsigned_contract`) | CTR-405: el documento no tiene la firma de las dos partes y el contrato empezó el 2026-02-01 | 100,000.00 | — | — | `contratos/CTR-405-ambiental-consultores-cia-ltda/10-contrato/contrato.md` |
| 4 | El contrato exige una garantía y no hay póliza aportada (`guarantee_missing`) | CTR-403: exige la garantía de calidad y no hay póliza aportada en 20-garantias/ | — | — | — | `contratos/CTR-403-campamentos-andinos-s-a/10-contrato/contrato.md, cláusula 9` |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-atribuciones.csv`
- `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md`
- `contratos/CTR-403-campamentos-andinos-s-a/10-contrato/contrato.md, cláusula 9`
- `contratos/CTR-405-ambiental-consultores-cia-ltda/10-contrato/contrato.md`

La corrida quedó registrada como `2026-10-06-contract-scan-1` con 4 hallazgos. La salida completa está en `estado-legal/0990054321001-minera-condor/corridas/salida-contract-scan.md`.

La sección «El resultado» salió vacía en el reporte del motor, y no la completé.