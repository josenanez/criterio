# /criterio-finance:close-scan 

Inventario: 66 archivos nuevos, 0 cambiados, 0 borrados y ninguno fuera de lugar. Es el primer barrido, así que todo cuenta como nuevo. Señales nuevas respecto de la corrida anterior: 0 (total 0). Los términos (versión 1.2) estaban vigentes.

El cálculo informa `no_procesado: 15`, pero el reporte dice que todo se procesó y no detalla qué es. Queda como discrepancia por revisar.

# Qué cambió en el cierre · Comercial Control Andes · periodo 2026-09

**Entidad:** Comercial Control Andes (76097001-8) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.10.0 · **Aprueba:** Contralor · **Comando:** `close-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

(El reporte no trae cifras en esta sección.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de la entidad? → finanzas/76097001-8-comercial-control-andes (la del argumento)
- ¿País, moneda y marco? → Chile, CLP, NIIF adoptadas por el Colegio de Contadores de Chile (F-18); sale de las facturas DTE del SII y del RUT
- ¿Qué periodo se cierra? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → ventas 4135, compras 5135/5145/5195, IVA generado y descontable 2408, las que sostienen facturas según el motor
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (auxiliar en 2026-08 y 2026-09); bancos andino-9701 y pacifico-9702
- ¿El checklist está aprobado? → No consta aprobación en los documentos; se usa el de 00-referencia/checklist-cierre.xlsx como no aprobado
- ¿Quién aprueba el cierre? → Contralor, valor por defecto; ningún documento nombra a otra persona

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-close-scan-1`. El texto mostrado está en `estado-finanzas/76097001-8-comercial-control-andes/corridas/salida-close-scan.md`.

Dos cosas que no hice:
- No cambié la ficha: ya traía la declaración de Sofía León del 2026-10-05 ("en curso") y ningún requerimiento del auditor llegó fuera de la tabla.
- El motor no registró en la corrida el nombre de quien acepta los términos, porque `terminos` no lo pedía; estaban vigentes y aceptados desde la ejecución anterior.