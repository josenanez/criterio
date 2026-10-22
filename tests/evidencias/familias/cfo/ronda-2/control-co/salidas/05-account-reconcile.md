# /criterio-finance:account-reconcile 

Corrí la conciliación de 2026-09 y las dos cuentas (1305 y 2205) cuadran: el mayor y el auxiliar coinciden y la diferencia es 0,00 en ambas. Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06, así que no hubo nada que registrar. El periodo lo tomé de la configuración.

# Conciliación de cuentas · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia | 0–30 | 31–60 | 61–90 | Más de 90 |
|---|---|---|---|---|---|---|---|---|
| 1305 | Clientes | 11.395.000,00 | 11.395.000,00 | 0,00 | 9.520.000,00 | 1.875.000,00 | 0,00 | 0,00 |
| 2205 | Proveedores | -11.543.000,00 | -11.543.000,00 | 0,00 | -11.543.000,00 | 0,00 | 0,00 | 0,00 |

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

La corrida quedó registrada como `2026-10-06-account-reconcile-1` y la salida quedó guardada en `estado-finanzas/900000001-distribuidora-control/corridas/salida-account-reconcile.md`. No dejó hallazgos.

Dos cosas que no se verificaron:
- **Reporte del motor:** se mostró arriba, pero no revisé que el archivo `reporte-account-reconcile.md` exista en `cierre/2026-09/`.
- **Marco contable:** el Grupo 2 es un valor propuesto por defecto y sigue por confirmar.