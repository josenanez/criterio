# /criterio-budget:transfer-log 

Dos de los cuatro cambios entre la versión 1 y la 2 del presupuesto tienen acta (el traslado de Comercial · Publicidad a Eventos, acta 05); los otros dos, Operaciones · Transporte y Tecnología · Licencias, no la tienen.

# Traslados y sus actas · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.7.0 · **Aprueba:** Contralor · **Comando:** `transfer-log`

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

- ¿Cuál es la versión aprobada y su acta? → Sesión sin interfaz: respuesta sugerida. Acta 01 (2026-01-20) aprueba la versión 1; el acta 05 (2026-06-28) aprueba un traslado y existe la versión 2 del 2026-06-30. Ningún acta dice que apruebe la versión 2 como tal.

## Fuentes

- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

La corrida quedó registrada como `2026-10-06-transfer-log-1`, con 4 hallazgos.