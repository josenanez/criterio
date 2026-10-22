# /criterio-finance:account-reconcile 

Los términos (versión 1.2) ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06. Las dos cuentas de `accounts.reconcile` tienen auxiliar en el periodo 2026-09, así que no hay conciliación desactualizada.

# Conciliación de cuentas · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

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

- ¿Cuál es la entidad, su NIT, país y moneda? → Banco Andino, NIT 900123456, Colombia, COP (de la carpeta finanzas/900123456-banco-andino)
- ¿Qué marco contable aplica? → Grupo 1 (F-05); solo se registra
- ¿Cuál es el periodo que se está cierrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué prefijos cruzan las facturas? → Ventas 41; compras 14, 51, 52, 61; IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (las que tienen auxiliar); bancos andino-1101 y pacifico-1102 (carpetas de 20-bancos)
- ¿Qué checklist se usa y está aprobado? → El de la organización (00-referencia/checklist-cierre.csv); sin aprobación documentada, queda como no aprobado
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino
- ¿Acepta los términos vigentes? → Sí, José Francisco Ñáñez, versión 1.2, 2026-10-06 (dado en el encargo de la prueba)
- ¿Se deja el archivo _CRITERIO_FINANZAS.txt en la carpeta de documentos? → No; nadie autorizó escribir dentro de los documentos

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-account-reconcile-1`, con la salida guardada en `estado-finanzas/900123456-banco-andino/corridas/salida-account-reconcile.md`.