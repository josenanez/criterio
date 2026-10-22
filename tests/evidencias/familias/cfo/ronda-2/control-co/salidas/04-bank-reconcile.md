# /criterio-finance:bank-reconcile 

Conciliación de las dos cuentas del periodo 2026-09: ambas cuadran, sin partidas abiertas y con diferencia sin explicar en cero.

# Conciliación bancaria · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `bank-reconcile`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |
|---|---|---|---|---|---|---|---|
| andino-5301 | 10.241.750,00 | 0,00 | 0,00 | 0,00 | 0,00 | 10.241.750,00 | 0,00 |
| pacifico-5302 | 15.000.000,00 | 0,00 | 0,00 | 0,00 | 0,00 | 15.000.000,00 | 0,00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su NIT, país y moneda? → Distribuidora Control, NIT 900000001, Colombia, COP (de la carpeta y las facturas XML)
- ¿Qué marco aplica? → Grupo 2 (propuesto por defecto; ningún documento lo dice, por confirmar)
- ¿Cuál es el periodo que se está cerrando? → 2026-09
- ¿Qué cuentas cruzan las facturas? → Ventas 41, compras 14/51/52/61, IVA 2408 (los del balance)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205; andino-5301 y pacifico-5302 (los que tienen auxiliar y extracto)
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobar hasta que una persona lo apruebe
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde guardo lo que encuentro? → estado-finanzas/900000001-distribuidora-control

## Fuentes

- Sin documentos citados.

---
Corrida registrada como `2026-10-06-bank-reconcile-1` (0 hallazgos). Los términos (v1.2) ya estaban vigentes, así que no hizo falta registrar una aceptación nueva.