# /criterio-finance:close-scan 

Se leyeron 66 archivos nuevos y 0 cambiados; hay 4 señales abiertas. Es la primera corrida de close-scan, así que las 4 son nuevas. El correo del 2026-10-05 declara el cierre «en curso», y la ficha ya traía esa declaración y el R-09 de la carta del auditor.

# Qué cambió en el cierre · Minera del Motagua · periodo 2026-09

**Entidad:** Minera del Motagua (89090314) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Factura electrónica duplicada (`einvoice_duplicate`) | El mismo UUID A1F089AB-1000102 aparece en 2 archivos | 98,000.00 | — | — | `2026-09/30-facturacion/emitidas/fe-A1F089AB-1000102-reenviada.xml` · `…/fe-A1F089AB-1000102.xml` |
| 2 | Registro sin factura electrónica (`recorded_without_einvoice`) | Documento B2E089AB-1000202 en las cuentas de compras, sin factura en recibidas/ | 84,875.00 | — | — | `2026-09/10-contabilidad/libro-mayor.xlsx` filas 56 y 57 |
| 3 | Banco sin conciliar (`bank_unreconciled`) | andino-8901: nota débito sin registrar del 2026-09-30, sin referencia | -10,000.00 | — | 0 | `2026-09/20-bancos/andino-8901/extracto.pdf` fila 17 |
| 4 | Requerimiento del auditor sin respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv` fila 6 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Entidad, país y moneda → Minera del Motagua, NIT 89090314, Guatemala, GTQ (por las facturas FEL de la SAT en quetzales)
- Marco contable → No encontrado: ningún documento lo declara; queda por confirmar
- Periodo que se cierra → 2026-09, el último con 10-contabilidad/
- Cuentas que cruzan las facturas → Ventas 4135; compras 5135, 5145 y 5195; IVA 2408
- Cuentas a conciliar y bancos → 1305 y 2205; andino-8901 y pacifico-8902
- Checklist → 00-referencia/checklist-cierre.csv; sin aprobación, queda como no aprobado
- Quién aprueba y festivos → Sofía León; festivos: ninguno a la mano
- Dónde se guarda el estado → estado-finanzas/89090314-minera-del-motagua
- Archivo marcador `_CRITERIO_FINANZAS.txt` → No se escribe nada en los documentos sin autorización

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.xlsx`
- `2026-09/20-bancos/andino-8901/extracto.pdf`
- `2026-09/30-facturacion/emitidas/fe-A1F089AB-1000102-reenviada.xml`
- `2026-09/30-facturacion/emitidas/fe-A1F089AB-1000102.xml`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv`

La corrida quedó registrada como `2026-10-06-close-scan-1`. Todo lo que se ve arriba está en `corridas/salida-close-scan.md`.

Dos cosas que no coinciden con el comando:
- Lo de arriba resume las preguntas en una línea cada una, no con el texto completo del reporte. El texto completo está en `cierre/2026-09/reporte-close-scan.md`.
- La sección «El resultado» salió vacía del motor. No la rellené.