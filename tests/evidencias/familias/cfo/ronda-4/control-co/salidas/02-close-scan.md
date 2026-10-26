# /criterio-finance:close-scan 

Inventario: 64 archivos, todos nuevos (0 cambiados, 0 borrados, 0 fuera de lugar). El motor calculó 0 señales. Se convirtieron los 6 documentos de `40-soportes` y los 4 de `50-auditoria`. La ficha ya recogía el correo de Sofía León del 2026-10-05, que dice que el cierre está «en curso».

# Qué cambió en el cierre · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dónde está la carpeta de documentos? → finanzas/900000001-distribuidora-control (la del argumento)
- ¿Cuál es la entidad, su NIT, país y moneda? → Distribuidora Control, NIT 900000001, CO, COP (del nombre de la carpeta)
- ¿Qué marco aplica? → grupo 1 (propuesta por defecto: ningún documento lo dice)
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → ventas 4135; compras 5135, 5145, 5195; IVA 2408 (las que sostienen facturas en el mayor)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (hay auxiliares); bancos andino-5301 y pacifico-5302
- ¿Qué checklist se usa? → 00-referencia/checklist-cierre.xlsx de la organización, sin aprobar
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900000001-distribuidora-control
- ¿Se marca la carpeta con _CRITERIO_FINANZAS.txt? → No, no se escribe nada en los documentos en esta prueba

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-close-scan-1`, con la salida completa en `corridas/salida-close-scan.md`.

Los términos ya estaban aceptados en la configuración (versión 1.2, José Francisco Ñáñez, 2026-10-06), así que no hubo que registrarlos de nuevo.