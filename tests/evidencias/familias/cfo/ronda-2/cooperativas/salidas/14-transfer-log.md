# /criterio-budget:transfer-log 

Las tres actas de `40-actas/` ya estaban en la ficha, así que no registré nada nuevo. La versión 2 del presupuesto trae un traslado y tiene su acta. Ninguna versión trae cambios sin acta, y no hay actas sin cambio aplicado.

# Traslados y sus actas · Cooperativa Sierra Alta · presupuesto 2026, corte 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Comité de presupuesto · **Comando:** `transfer-log`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Versión | Área | Línea | Valor | Tipo | Acta | Estado |
|---|---|---|---|---|---|---|
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Eventos | 3,000.00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Publicidad | -3,000.00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Cooperativa Sierra Alta (RUC 1790012345001), presupuesto 2026; tomado del nombre de la carpeta y de presupuesto-2026/
- ¿Cuál es la versión aprobada y su acta? → El acta 01 (2026-01-20) aprueba la versión 1; el acta 05 (2026-06-28) aprueba un traslado de 3,000.00 que coincide con la versión 2 (2026-06-30), pero ningún acta nombra esa versión. Se registró lo que dicen las actas.
- ¿Áreas y responsables? → No encontrado: ningún documento nombra a los responsables de las áreas. Áreas tomadas del mapeo: Administración, Comercial, Tecnología, Operaciones, Personal.
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma)
- ¿Fechas del comité? → No encontrado en los documentos; quedó vacío
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json)
- ¿Dónde se guarda lo que se encuentra? → estado-finanzas/1790012345001-cooperativa-sierra-alta, fuera de la carpeta de documentos
- ¿Términos? → Aceptados por José Francisco Ñáñez, 2026-10-06, versión 1.2

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-transfer-log-1` (el motor reportó 4 hallazgos). La salida está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-transfer-log.md`.