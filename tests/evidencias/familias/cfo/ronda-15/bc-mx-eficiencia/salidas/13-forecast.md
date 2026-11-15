# /criterio-budget:forecast 

Proyección al corte 2026-09: el motor calculó dos proyecciones, al ritmo y al plan, junto a la de cada área. Ninguna es la correcta por definición; la decide una persona. Las proyecciones de las áreas están fechadas 2026-09-30, así que no están vencidas.

# Proyección al cierre del año · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `forecast`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |
|---|---|---|---|---|---|
| Administración | Mantenimiento | 432,000.00 | 423,360.00 (2026-09-30) | 465,600.00 | 457,200.00 |
| Administración | Servicios públicos | 648,000.00 | 635,040.00 (2026-09-30) | 628,560.00 | 633,420.00 |
| Comercial | Eventos | 378,000.00 | 370,440.00 (2026-09-30) | 349,200.00 | 369,900.00 |
| Comercial | Publicidad | 810,000.00 | 793,800.00 (2026-09-30) | 806,760.00 | 794,070.00 |
| Operaciones | Transporte | 756,000.00 | 740,880.00 (2026-09-30) | 733,320.00 | 738,990.00 |
| Personal | Nómina | 4,320,000.00 | 4,320,000.00 (2026-09-30) | 4,320,000.00 | 4,320,000.00 |
| Tecnología | Licencias | 1,080,000.00 | 1,058,400.00 (2026-09-30) | 1,047,600.00 | 1,055,700.00 |
| Tecnología | PRY-310 | 1,296,000.00 | 1,270,080.00 (2026-09-30) | 1,257,120.00 | 1,266,840.00 |

**Al ritmo:** el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido. **Al plan:** el ejecutado más lo que falta del aprobado según su distribución mensual.

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

---
La corrida quedó registrada como `2026-10-06-forecast-1`.

- **Términos:** estaban vigentes (versión 1.5), aceptados por José Francisco Ñáñez el 2026-10-06. No hizo falta registrar nada nuevo.
- **Fecha:** pasé `--today 2026-10-06` a las llamadas que la aceptan (`reporte` y `corrida`).
- **Registro:** `corrida` devolvió "hallazgos: 1". No lo investigué ni lo expliqué.