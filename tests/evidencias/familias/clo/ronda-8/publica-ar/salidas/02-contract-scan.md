# /criterio-legal:contract-scan 

Soy Fidel. Los seis contratos de la carpeta eran nuevos para esta corrida. Sus fichas ya existían de la instalación. Las contrasté con los contratos, el otrosí, las pólizas, los certificados, las constancias y el acta, y no hallé diferencias. El motor no devolvió `record_issues`.

Siguen pendientes dos puntos de la instalación que no resuelve el agente:
- CTR-2801 y CTR-2802 traen el mismo CUIT de la contraparte.
- No hay umbral de garantía registrado para la entidad.

# Qué cambió en los contratos · Organismo Público del Litoral · al 2026-10-06

**Entidad:** Organismo Público del Litoral (30699991011) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.1.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La garantía de cumplimiento de un contrato público es menor que el mínimo de la ley de su país (`public_guarantee_below_law`) | CTR-2801: la garantía de cumplimiento es de 5.120.000,00 y la ley pide al menos el 10 % del valor del contrato, 6.400.000,00 | 1.280.000,00 | — | — | `contratos/CTR-2801-tecnologia-estatal-s-r-l/20-garantias/poliza-cumplimiento.md` |
| 2 | La garantía de cumplimiento de un contrato público es menor que el mínimo de la ley de su país (`public_guarantee_below_law`) | CTR-2803: la garantía de cumplimiento es de 3.840.000,00 y la ley pide al menos el 10 % del valor del contrato, 4.800.000,00 | 960.000,00 | — | — | `contratos/CTR-2803-inmuebles-oficiales-s-a/20-garantias/poliza-cumplimiento.md` |
| 3 | La garantía de cumplimiento de un contrato público se entregó después del plazo de la ley de su país (`public_guarantee_late`) | CTR-2802: la garantía de cumplimiento se entregó el 2025-07-08, y la ley pide entregarla a más tardar el 2025-07-03, 5 días hábiles después de la firma | — | — | 5 | `contratos/CTR-2802-suministros-publicos-s-r-l/20-garantias/poliza-cumplimiento.md` |
| 4 | La garantía de cumplimiento de un contrato público se entregó después del plazo de la ley de su país (`public_guarantee_late`) | CTR-2806: la garantía de cumplimiento se entregó el 2025-10-08, y la ley pide entregarla a más tardar el 2025-10-03, 5 días hábiles después de la firma | — | — | 5 | `contratos/CTR-2806-mantenimiento-publico-s-r-l/20-garantias/poliza-cumplimiento.md` |
| 5 | La garantía de cumplimiento de un contrato público se entregó después del plazo de la ley de su país (`public_guarantee_late`) | CTR-2804: la garantía de cumplimiento se entregó el 2026-03-06, y la ley pide entregarla a más tardar el 2026-03-03, 5 días hábiles después de la firma | — | — | 3 | `contratos/CTR-2804-software-publico-s-r-l/20-garantias/poliza-cumplimiento.md` |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `contratos/CTR-2801-tecnologia-estatal-s-r-l/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-2802-suministros-publicos-s-r-l/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-2803-inmuebles-oficiales-s-a/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-2804-software-publico-s-r-l/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-2806-mantenimiento-publico-s-r-l/20-garantias/poliza-cumplimiento.md`

La corrida quedó registrada como `2026-10-06-contract-scan-1`, con 5 hallazgos. La salida completa está en `estado-legal/30699991011-organismo-publico-del-litoral/corridas/salida-contract-scan.md`.