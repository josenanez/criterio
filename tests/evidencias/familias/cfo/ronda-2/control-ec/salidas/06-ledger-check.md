# /criterio-finance:ledger-check 

Términos vigentes (versión 1.2, ya aceptada). Corrí el cuadre del periodo 2026-09.

# Cuadre del balance y el mayor · Comercial Control · periodo 2026-09

**Entidad:** Comercial Control (1790000001001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `ledger-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

Débitos 372,041.26 · créditos 372,041.26 · diferencia 0.00.

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

Quedó registrada la corrida `2026-10-06-ledger-check-1`, con 0 hallazgos. Dos aclaraciones sobre cómo la hice:
- **Aceptación de términos:** el motor mostró los términos como ya vigentes, así que no volví a registrar la aceptación de José Francisco Ñáñez.
- **Periodo:** el comando no recibió uno, así que usé 2026-09. Es el último con contabilidad cargada, según el propio reporte.

El reporte del motor está en `estado-finanzas/1790000001001-comercial-control/cierre/2026-09/reporte-ledger-check.md`. Lo que te mostré está en `estado-finanzas/1790000001001-comercial-control/corridas/salida-ledger-check.md`.