# /criterio-finance:ledger-check 

Los términos estaban vigentes (versión 1.2, aceptada por José Francisco Ñáñez el 2026-10-06). Corrí el cuadre del periodo 2026-09, que es el configurado.

# Cuadre del balance y el mayor · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `ledger-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

Débitos 207,302.50 · créditos 207,302.50 · diferencia 0.00.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su RUC, país y moneda? → Cooperativa Sierra Alta, RUC 1790012345001, Ecuador, USD (por el nombre de la carpeta y las facturas del SRI)
- ¿Qué marco contable aplica? → NIIF para PYMES, por confirmar: ningún documento lo dice
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 41, compras 5135/5145/5195, IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (los auxiliares que hay); bancos andino-2301 y pacifico-2302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobación registrada
- ¿Quién aprueba el cierre? → Sofía León, responsable de C-09 en el checklist
- ¿Hay festivos del calendario? → No encontrado: ningún documento los trae

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-ledger-check-1`. Lo que te mostré está guardado en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-ledger-check.md`.