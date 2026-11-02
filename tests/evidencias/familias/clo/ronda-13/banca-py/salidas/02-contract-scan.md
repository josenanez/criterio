# /criterio-legal:contract-scan 

Corrida de prueba sin interfaz: las seis fichas existentes (CTR-4401 a CTR-4406) coinciden con sus documentos, así que no corregí nada. Hay una duda para la persona: CTR-4405 y CTR-4406 traen el mismo RUC de contraparte (88440006-9) con nombres distintos. Lo dejé como lo dicen los documentos.

# Qué cambió en los contratos · Banco del Tebicuary Sintético · al 2026-10-06

**Entidad:** Banco del Tebicuary Sintético (88457812-7) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.3.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-4402 · OT-1: Hugo Duarte firmó el otrosí que lleva el contrato a 4.950.000.000,00 sin facultad para ese monto | 3.150.000.000,00 | — | — | `contratos/CTR-4402-papeleria-del-centro-sintetica-s-a/10-contrato/otrosi-1.md` |
| 2 | Lo pagado supera el valor del contrato más sus otrosíes (`payments_over_value`) | CTR-4402: pagado 5.247.000.000,00 contra un valor de 4.950.000.000,00 con sus otrosíes | 297.000.000,00 | — | — | `10-registro/pagos-2026-09-30.csv` fila 6 · `10-registro/pagos-2026-09-30.csv` fila 7 · `contratos/CTR-4402-papeleria-del-centro-sintetica-s-a/10-contrato/contrato.md` |
| 3 | Una obligación del contrato pasó su fecha sin evidencia (`contract_obligation_overdue`) | CTR-4404 · OBL-1 · Informe mensual de ejecución (agosto): venció el 2026-09-05 y no hay evidencia en 40-ejecucion/ | — | Licencias Digitales Sintética S.A. | 31 | `contratos/CTR-4404-licencias-digitales-sintetica-s-a/10-contrato/contrato.md, cláusula 5` |
| 4 | La fecha límite del preaviso de no renovación de un contrato con renovación automática cae dentro de los días configurados (`notice_deadline_near`) | CTR-4404: el preaviso de no renovación vence el 2026-11-01, en 26 días, y nadie decidió | — | — | 26 | `contratos/CTR-4404-licencias-digitales-sintetica-s-a/10-contrato/contrato.md` |
| 5 | El contrato exige una garantía y no hay póliza aportada (`guarantee_missing`) | CTR-4403: exige la garantía de calidad y no hay póliza aportada en 20-garantias/ | — | — | — | `contratos/CTR-4403-inmobiliaria-carmelitas-sintetica-s-a/10-contrato/contrato.md, cláusula 9` |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-registro/pagos-2026-09-30.csv`
- `contratos/CTR-4402-papeleria-del-centro-sintetica-s-a/10-contrato/contrato.md`
- `contratos/CTR-4402-papeleria-del-centro-sintetica-s-a/10-contrato/otrosi-1.md`
- `contratos/CTR-4403-inmobiliaria-carmelitas-sintetica-s-a/10-contrato/contrato.md, cláusula 9`
- `contratos/CTR-4404-licencias-digitales-sintetica-s-a/10-contrato/contrato.md`
- `contratos/CTR-4404-licencias-digitales-sintetica-s-a/10-contrato/contrato.md, cláusula 5`

La corrida quedó registrada como `2026-10-06-contract-scan-1`, con 5 hallazgos. Todo lo que mostré está en `corridas/salida-contract-scan.md`. Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez con fecha 2026-10-06.