# /criterio-budget:transfer-log 

Las tres actas de `40-actas` ya estaban en la ficha con su cita y coinciden con su texto, así que no la cambié. Una sola versión cambia respecto a la anterior (la v2) y su cambio tiene acta.

# Traslados y sus actas · Almacenes Caribe · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `transfer-log`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Versión | Área | Línea | Valor | Tipo | Acta | Estado |
|---|---|---|---|---|---|---|
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Eventos | 2.400.000,00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Publicidad | -2.400.000,00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Sin nadie que conteste, se propone la 2 (presupuesto-2026-v2-2026-06-30.csv), cuyo cambio coincide con el traslado del acta 05 del 2026-06-28; el acta 01 del 2026-01-20 aprueba solo la versión 1 y ningún acta dice 'versión 2'.
- ¿Qué cuentas entran como gasto? → Prefijo 51, el de las cuentas del mapeo-presupuesto (5105, 5135, 5145, 5195).
- ¿Fechas del comité de presupuesto? → No encontrado: el acta 06 no fija fecha del próximo comité.
- ¿Dónde están las fichas PMO? → estado-pmo/records (contiene PRY-310.json).
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta de documentos? → No: nadie autorizó escribir en los documentos.

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-transfer-log-1`, con la salida en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-transfer-log.md`.