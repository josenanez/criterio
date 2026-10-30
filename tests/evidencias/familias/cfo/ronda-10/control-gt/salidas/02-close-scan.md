# /criterio-finance:close-scan 

66 archivos nuevos, 0 cambiados y 0 borrados; 0 señales nuevas respecto de la corrida anterior.

Los términos de la versión 1.3 están vigentes. Solo el correo del 2026-10-05 de Sofía León declara el estado del cierre ("en curso"), y ya estaba en la ficha. Convertí el correo y los 5 soportes PDF a texto. Las tablas y las facturas electrónicas las procesa el motor directamente.

# Qué cambió en el cierre · Comercial Control de Guatemala · periodo 2026-09

**Entidad:** Comercial Control de Guatemala (97217352) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `close-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su identificación, país y moneda? → Comercial Control de Guatemala, 97217352, GT, GTQ (tomado del nombre de la carpeta; sin sí explícito de la persona)
- ¿Qué marco contable aplica? → NIIF (propuesto por defecto; Guatemala no figura entre los marcos del comando y ningún documento lo confirma)
- ¿Cuál es el periodo que se está cerrando? → 2026-09
- ¿Qué cuentas cruzan las facturas? → ventas 4135; IVA generado 2408; compras 5135, 5145, 5195; IVA descontable 2408 (las que sostienen facturas del periodo)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (con auxiliar en 2026-08 y 2026-09); bancos andino-9701 y pacifico-9702
- ¿Qué checklist se usa? → 00-referencia/checklist-cierre.xlsx de la organización, sin aprobar hasta que una persona lo apruebe
- ¿Quién aprueba el cierre y qué festivos hay? → Contralor (por defecto); sin festivos
- ¿Dónde se guarda el estado? → estado-finanzas/97217352-comercial-control-de-guatemala
- ¿Se aceptan los términos? → Sí, José Francisco Ñáñez, 2026-10-06 (indicado en la instrucción de la prueba)
- ¿Se marca la carpeta con _CRITERIO_FINANZAS.txt? → No; no se escribe nada dentro de los documentos en esta prueba

## Fuentes

- Sin documentos citados.

---
Dos notas sobre esta corrida:
- El motor devolvió 0 señales y el reporte salió vacío en "El resultado". Todos los archivos eran nuevos, así que el cero es plausible, pero no lo verifiqué contra los datos.
- La corrida quedó registrada como `2026-10-06-close-scan-1`.