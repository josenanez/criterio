# /criterio-finance:account-reconcile 

Los términos estaban vigentes (versión 1.2, aceptada en 0.8.0), así que no hizo falta registrar una aceptación nueva. Las dos cuentas con auxiliar cuadran en el periodo 2026-09.

# Conciliación de cuentas · Comercial Control · periodo 2026-09

**Entidad:** Comercial Control (1790000001001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia | 0–30 | 31–60 | 61–90 | Más de 90 |
|---|---|---|---|---|---|---|---|---|
| 1305 | Clientes | 41,568.75 | 41,568.75 | 0.00 | 34,068.75 | 7,500.00 | 0.00 | 0.00 |
| 2205 | Proveedores | -33,465.01 | -33,465.01 | 0.00 | -33,465.01 | 0.00 | 0.00 | 0.00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta de documentos? → finanzas/1790000001001-comercial-control (la del argumento; única candidata)
- ¿Entidad, país y moneda? → Comercial Control, RUC 1790000001001, Ecuador, USD (por el nombre de la carpeta y las facturas del SRI)
- ¿Qué marco aplica en Ecuador? → No encontrado en los documentos; queda «NIIF (marco por confirmar)»
- ¿Qué periodo se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 1435, 5135, 5145, 5195; IVA 2408 (las del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (tienen auxiliar); bancos andino-6701 y pacifico-6702
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; no aprobado hasta que una persona lo apruebe
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (Contraloría, tarea C-09); festivos: no encontrados, lista vacía
- ¿Dónde se guarda el estado? → estado-finanzas/1790000001001-comercial-control, fuera de la carpeta de documentos
- ¿Se deja el archivo _CRITERIO_FINANZAS.txt en la carpeta? → No se dejó: no hubo una autorización expresa para escribir en los documentos

## Fuentes

- Sin documentos citados.

---

La corrida quedó registrada como `2026-10-06-account-reconcile-1`, con 0 hallazgos. La salida está en `estado-finanzas/1790000001001-comercial-control/corridas/salida-account-reconcile.md`.