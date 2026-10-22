# /criterio-finance:account-reconcile 

Los términos (v1.2) ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-06. El periodo salió de la configuración, 2026-09.

# Conciliación de cuentas · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia | 0–30 | 31–60 | 61–90 | Más de 90 |
|---|---|---|---|---|---|---|---|---|
| 1305 | Clientes | 53,800.00 | 53,800.00 | 0.00 | 48,300.00 | 5,500.00 | 0.00 | 0.00 |
| 2205 | Proveedores | -46,400.20 | -46,400.20 | 0.00 | -46,400.20 | 0.00 | 0.00 | 0.00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de documentos? → finanzas/0990054321001-minera-condor (la del argumento)
- ¿Entidad, país y moneda? → Minera Cóndor, RUC 0990054321001, Ecuador, USD (por el RUC de las facturas y la carpeta)
- ¿Qué marco contable aplica? → No indicado en los documentos; queda registrado así
- ¿Qué periodo se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 41; compras 14/51/52/61; IVA 2408 (los del balance de comprobación)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (tienen auxiliar); andino-4101 y pacifico-4102 (carpetas de 20-bancos)
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin constancia de aprobación, queda como no aprobado
- ¿Quién aprueba el cierre? → Sofía León (responsable de C-09 en el checklist)
- ¿Festivos? → Ninguno a mano; la lista queda vacía

## Fuentes

- Sin documentos citados.

La salida quedó en `estado-finanzas/0990054321001-minera-condor/corridas/salida-account-reconcile.md` y la corrida se registró como `2026-10-06-account-reconcile-1`.