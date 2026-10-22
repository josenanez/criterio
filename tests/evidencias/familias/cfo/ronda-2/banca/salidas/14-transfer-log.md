# /criterio-budget:transfer-log 

Los términos 1.2 ya estaban vigentes y registrados a nombre de José Francisco Ñáñez (2026-10-06). Las tres actas ya estaban convertidas y sus movimientos ya estaban en la ficha, así que no hubo nada nuevo que registrar.

De la v1 a la v2 del presupuesto hay cuatro cambios de línea. El traslado Publicidad → Eventos tiene su acta (la 05). Los de Operaciones · Transporte y Tecnología · Licencias no tienen acta.

# Traslados y sus actas · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `transfer-log`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | 4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | -4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |

## El resultado

| Versión | Área | Línea | Valor | Tipo | Acta | Estado |
|---|---|---|---|---|---|---|
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Eventos | 3.000.000,00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Publicidad | -3.000.000,00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Operaciones | Transporte | 4.800.000,00 | traslado | — | sin acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Tecnología | Licencias | -4.800.000,00 | traslado | — | sin acta |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La 1: el acta 01 del 2026-01-20 es la única que aprueba una versión. La v2 (2026-06-30) no tiene acta de aprobación; el acta 05 solo aprueba un traslado de 3,000,000.00.
- ¿Quién es el responsable de cada área? → No encontrado en los documentos; sin responsable asignado.
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- ¿Fechas del comité de presupuesto? → No encontradas; el acta 06 habla de «el próximo comité» sin fecha.
- ¿Fichas PMO? → estado-pmo/records, con PRY-310.json.
- ¿Marcar la carpeta con _CRITERIO_FINANZAS.txt? → No: nadie lo autorizó; no se escribió nada en los documentos.

## Fuentes

- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

La corrida quedó registrada como `2026-10-06-transfer-log-1`, con la salida en `estado-finanzas/900123456-banco-andino/corridas/salida-transfer-log.md`.