# /criterio-finance:bank-reconcile 

Las dos cuentas bancarias de 2026-09 concilian sin partidas abiertas y con diferencia sin explicar en cero.

# Conciliación bancaria · Comercial Control · periodo 2026-09

**Entidad:** Comercial Control (1790000001001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `bank-reconcile`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |
|---|---|---|---|---|---|---|---|
| andino-6701 | 24,933.75 | 0.00 | 0.00 | 0.00 | 0.00 | 24,933.75 | 0.00 |
| pacifico-6702 | 45,000.00 | 0.00 | 0.00 | 0.00 | 0.00 | 45,000.00 | 0.00 |

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
Los términos ya estaban vigentes (versión 1.2, aceptada en 0.8.0), así que no registré una aceptación nueva. La corrida quedó registrada como `2026-10-06-bank-reconcile-1` con 0 hallazgos.