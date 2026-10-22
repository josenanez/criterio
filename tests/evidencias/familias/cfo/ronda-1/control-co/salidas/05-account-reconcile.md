# /criterio-finance:account-reconcile 

Las dos cuentas del periodo 2026-09 cuadran con su auxiliar, sin diferencias. Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-06, así que no hubo que registrarlos de nuevo. Usé el periodo 2026-09 porque es el que trae la configuración.

# Conciliación de cuentas · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

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

- ¿Cuál es la entidad, su NIT, país y moneda? → Distribuidora Control, NIT 900000001, Colombia, COP (sesión sin interfaz: tomado de la carpeta y las facturas)
- ¿Qué marco o grupo NIIF aplica? → No encontrado en los documentos; queda 'por confirmar'
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (traen auxiliar); bancos andino-5301 y pacifico-5302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv, sin aprobar
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900000001-distribuidora-control
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta? → No: sin interfaz no hay un sí para escribir dentro de los documentos

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-account-reconcile-1` con 0 hallazgos. La salida está en `estado-finanzas/900000001-distribuidora-control/corridas/salida-account-reconcile.md`.