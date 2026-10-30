# /criterio-legal:contract-scan 

Las 7 fichas de contrato (CTR-4101 a CTR-4107) ya existían de la corrida de `legal-setup`. El inventario las marca todas como nuevas porque no tenía una corrida anterior contra la cual compararlas. No revisé las fichas contra sus documentos, así que no cambié ninguna. El cálculo no trae `record_issues` y todo lo que llegó se procesó.

Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06, así que no hubo que registrar nada.

# Qué cambió en los contratos · Almacenes del Valle de Sula · al 2026-10-06

**Entidad:** Almacenes del Valle de Sula (08010006129040) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.2.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Firma sin facultad según la matriz de atribuciones (`signed_without_authority`) | CTR-4102 · OT-1: María José Funes firmó el otrosí que lleva el contrato a 12,100,000.00 sin facultad para ese monto | 7,700,000.00 | — | `contratos/CTR-4102-empaques-de-san-pedro-sula-s-a/10-contrato/otrosi-1.md` |
| 2 | Contrato por vencer sin decisión de renovar o terminar (`contract_expiring`) | CTR-4103: vence el 2026-11-25, sin decisión registrada | 6,600,000.00 | 50 | `contratos/CTR-4103-centro-comercial-del-norte-s-a/10-contrato/contrato.md` |
| 3 | Garantía exigida sin póliza aportada (`guarantee_missing`) | CTR-4103: exige la garantía de calidad y no hay póliza en 20-garantias/ | — | — | `contratos/CTR-4103-centro-comercial-del-norte-s-a/10-contrato/contrato.md, cláusula 9` |
| 4 | Contrato sin fila en el registro (`register_mismatch`) | CTR-4107: está en la carpeta y no en el registro | — | — | `contratos/CTR-4107-vigilancia-integral-s-a/` |
| 5 | El registro no coincide con el documento (`register_differs_from_contract`) | CTR-4102: valor 6,600,000.00 en el registro y 12,100,000.00 en el documento | — | — | `10-registro/registro-contratos.csv` fila 3 · `contratos/CTR-4102-empaques-de-san-pedro-sula-s-a/10-contrato/contrato.md` |

## Preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `10-registro/registro-contratos.csv`
- `contratos/CTR-4102-empaques-de-san-pedro-sula-s-a/10-contrato/contrato.md`
- `contratos/CTR-4102-empaques-de-san-pedro-sula-s-a/10-contrato/otrosi-1.md`
- `contratos/CTR-4103-centro-comercial-del-norte-s-a/10-contrato/contrato.md`
- `contratos/CTR-4107-vigilancia-integral-s-a/`

(El archivo del reporte lleva la tabla completa del motor, con la columna «Responsable»; aquí la acorté. En la salida también quedó una sección «El resultado» sin contenido.)

La corrida quedó registrada como `2026-10-06-contract-scan-1` (5 hallazgos). El reporte completo está en `estado-legal/08010006129040-almacenes-del-valle-de-sula/contratos/reporte-contract-scan.md`, y la salida de la corrida en `corridas/salida-contract-scan.md`.

Escribí el archivo de salida de la corrida con el texto del reporte del motor y una línea inicial. Ese archivo no es lo que pegué arriba: aquí acorté la tabla y las citas.