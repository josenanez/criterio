# /criterio-finance:account-reconcile 

Las dos cuentas del periodo 2026-09 cuadran: el mayor y el auxiliar coinciden y la diferencia es 0,00 en ambas. Los términos ya estaban vigentes, así que no hizo falta registrar la aceptación.

# Conciliación de cuentas · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia | 0–30 | 31–60 | 61–90 | Más de 90 |
|---|---|---|---|---|---|---|---|---|
| 1305 | Clientes | 34.453.500,00 | 34.453.500,00 | 0,00 | 29.453.500,00 | 5.000.000,00 | 0,00 | 0,00 |
| 2205 | Proveedores | -23.086.000,00 | -23.086.000,00 | 0,00 | -23.086.000,00 | 0,00 | 0,00 | 0,00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su país y su moneda? → Banco Andino, NIT 900123456, Colombia, COP (tomado del nombre de la carpeta)
- ¿Qué marco contable aplica? → grupo 1 (propuesta por defecto; ningún documento lo declara, por confirmar)
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad)
- ¿Qué cuentas cruzan las facturas? → ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408 (visto en el balance)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (hay auxiliar); bancos andino-1101 y pacifico-1102
- ¿Qué checklist se usa? → el de la organización, 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre? → Sofía León (Contraloría, responsable de C-09)
- ¿Festivos del calendario? → 2026-10-12 (festivo por defecto, por confirmar)
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino

## Fuentes

- Sin documentos citados.

---
La corrida quedó registrada como `2026-10-06-account-reconcile-1`, con la salida en `estado-finanzas/900123456-banco-andino/corridas/salida-account-reconcile.md`. Quedan por confirmar el marco contable (grupo 1) y el festivo 2026-10-12, que son valores por defecto.