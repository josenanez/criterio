# /criterio-budget:transfer-log 

Los términos están vigentes y no había actas nuevas por registrar: la ficha ya tenía las actas 01 y 05 y el compromiso del acta 06. El traslado de la versión 2 tiene su acta; no aparece ningún cambio sin acta ni acta sin cambio aplicado.

# Traslados y sus actas · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `transfer-log`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Versión | Área | Línea | Valor | Tipo | Acta | Estado |
|---|---|---|---|---|---|---|
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Eventos | 54,000.00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Publicidad | -54,000.00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Distribuidora del Noroeste (DNO190402B43), 2026; tomado de la configuración de la familia y de presupuesto-2026/
- ¿Cuál es la versión aprobada? → Rige la más reciente de 10-aprobado/: versión 2 (2026-06-30), que nace del traslado del acta 05 sobre la versión 1 aprobada en el acta 01 del 2026-01-20
- ¿Áreas y su responsable? → Áreas del presupuesto: Administración, Comercial, Tecnología, Operaciones, Personal. Responsables: no encontrados en los documentos
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida a los 45 días; configuración, no norma
- ¿Fechas del comité? → No encontradas; el acta 06 menciona un próximo comité sin fecha
- ¿Fichas PMO? → estado-pmo/records (PRY-310.json)
- ¿Dónde guardo el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste, el que ya fijó la familia

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-transfer-log-1`. La salida completa está en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-transfer-log.md`.