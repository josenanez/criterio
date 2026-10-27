# /criterio-finance:close-scan 

66 archivos nuevos y 0 cambiados; 7 señales abiertas en el periodo 2026-09. El motor no entrega el delta contra la corrida anterior. El correo de Sofía León del 2026-10-05 declara el cierre como cerrado, y el reporte lo contrasta con las demás señales.

# Qué cambió en el cierre · Tiendas Pacífico · periodo 2026-09

**Entidad:** Tiendas Pacífico (76083001-1) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.10.0 · **Aprueba:** Contralor · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El cierre se reporta como cerrado y hay señales abiertas que ese estado no explica (`declared_close_vs_evidence`) | el cierre se reporta cerrado (2026-09/40-soportes/correo-estado-del-cierre.md, 2026-10-05) y hay 6 señales abiertas que ese estado no explica | — | — | — | `2026-09/40-soportes/correo-estado-del-cierre.md` |
| 2 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | el mismo RUT del emisor, tipo y folio aparece en 2 archivos (1000102) | 2.231.250,00 | — | — | `2026-09/30-facturacion/emitidas/fe-1000102-reenviada.xml` · `2026-09/30-facturacion/emitidas/fe-1000102.xml` |
| 3 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | factura 2000201 registrada en 2 asientos (C-021, C-022) | 970.000,00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · fila 54 · fila 56 · fila 57 |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-8301: consignación en tránsito del 2026-09-30 por 892.500,00 (1000107) | 892.500,00 | — | 0 | `2026-09/20-bancos/andino-8301/auxiliar-libros.csv` fila 16 |
| 5 | El saldo de una cuenta en el mayor no es el de su auxiliar (`account_unreconciled`) | cuenta 2205: el mayor dice -6.348.650,00 y el auxiliar suma -5.771.500,00 | -577.150,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 6 · `2026-09/10-contabilidad/auxiliares/2205-proveedores.csv` |
| 6 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura 2000201: base 485.000,00 en el XML y 970.000,00 en libros; IVA 92.150,00 en el XML y 184.300,00 en libros | 577.150,00 | — | — | `2026-09/30-facturacion/recibidas/fr-2000201.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · fila 54 · fila 56 |
| 7 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura 1000104: IVA 190.000,00 en el XML y 190.010,00 en libros | 10,00 | — | — | `2026-09/30-facturacion/emitidas/fe-1000104.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 15 · fila 16 |

## El resultado

(El reporte del motor no trae texto en esta sección.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA generado y descontable 2408
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205; bancos andino-8301 y pacifico-8302
- ¿Qué checklist se usa? → El de la organización, industria retail, sin aprobar
- ¿Quién aprueba el cierre y qué festivos hay? → Contralor; festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/76083001-1-tiendas-pacifico

## Fuentes

Los 9 archivos citados en la tabla de señales.

---

**Notas mías, fuera del reporte:**
- `compute` informó `no_procesado: 17`, pero el reporte dice «Todo lo que llegó se procesó». No pude conciliar esas dos cifras con lo que el motor me dio.
- Dejé el reporte completo en `cierre/2026-09/reporte-close-scan.md` y la corrida quedó registrada como `2026-10-06-close-scan-1`. El texto de arriba abrevia las citas repetidas y la lista de fuentes, así que `corridas/salida-close-scan.md` (reporte completo precedido por la línea de apertura) no es idéntico a lo que ves aquí.