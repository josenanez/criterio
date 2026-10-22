# /criterio-finance:ledger-check 

El cuadre de 2026-09 sale sin diferencia: los débitos y los créditos coinciden. Los términos (versión 1.2) ya estaban aceptados para la versión 0.8.0, así que no registré la aceptación otra vez. El reporte no cita ningún documento.

# Cuadre del balance y el mayor · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `ledger-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

Débitos 127.064.500,00 · créditos 127.064.500,00 · diferencia 0,00.

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

Dejé la corrida registrada como `2026-10-06-ledger-check-1`, con 0 hallazgos. La salida completa quedó en `estado-finanzas/900000001-distribuidora-control/corridas/salida-ledger-check.md`.