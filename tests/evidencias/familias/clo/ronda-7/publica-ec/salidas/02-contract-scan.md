# /criterio-legal:contract-scan 

Las fichas de los seis contratos ya existían (de `legal-setup`) y coinciden con sus documentos, y no hubo registros con problemas. El motor señala dos garantías por debajo del mínimo de la ley.

# Qué cambió en los contratos · Empresa Pública Sierra Norte EP · al 2026-10-06

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Garantía de cumplimiento menor que el mínimo de la ley (`public_guarantee_below_law`) | CTR-2001: la garantía es de 9,600.00 y la ley pide al menos el 5 % del valor del contrato, 16,000.00 | 6,400.00 | `contratos/CTR-2001-tecnologia-del-estado-s-a/20-garantias/poliza-cumplimiento.md` |
| 2 | Garantía de cumplimiento menor que el mínimo de la ley (`public_guarantee_below_law`) | CTR-2003: la garantía es de 7,200.00 y la ley pide al menos el 5 % del valor del contrato, 12,000.00 | 4,800.00 | `contratos/CTR-2003-edificaciones-oficiales-s-a/20-garantias/poliza-cumplimiento.md` |

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `contratos/CTR-2001-tecnologia-del-estado-s-a/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-2003-edificaciones-oficiales-s-a/20-garantias/poliza-cumplimiento.md`

**Corrida registrada:** `2026-10-06-contract-scan-1`. La salida completa está en `corridas/salida-contract-scan.md` y el reporte en `contratos/reporte-contract-scan.md`, ambos dentro de la carpeta de estado.

Dos cosas que conviene saber:
- **Términos:** el motor los marcó vigentes. En la salida, `aceptada` figura como `1.0.0` (versión del plugin) y la versión de los términos es la 1.3. La configuración ya trae la aceptación de José Francisco Ñáñez del 2026-10-06, así que no registré nada nuevo.
- **Documentos fuera de lugar:** el inventario marcó `00-referencia/politica-contratacion.md`, que iría en `20-politicas/`. No lo moví.