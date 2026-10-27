# /criterio-budget:budget-setup finanzas/76083001-1-tiendas-pacifico

## Listo — Tiendas Pacífico · presupuesto 2026

**Lo que miré:** 2 versiones (v1 de 2026-01-15, v2 de 2026-06-30) · contabilidad de 2026-01 a 2026-09 · 3 actas.

**Versión aprobada:** 2, la más reciente de `10-aprobado/`. Nace del traslado de Publicidad a Eventos que aprueba el acta 05 del 2026-06-28 (`presupuesto-2026/40-actas/acta-05-traslado.md`). La v1 la aprueba el acta 01 del 2026-01-20.

**Términos:** aceptados por José Francisco Ñáñez (2026-10-06) para la versión 0.10.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.10.0-2026-10-06.md` y `.pdf`.

**Otras señales que calculó el motor y el reporte no lista:**
- **Proyección sobre lo aprobado:** Tecnología · PRY-310. La proyección del área es 19.800.000,00 contra 18.000.000,00 aprobado.
- **Dos cambios sin acta (`transfer_without_approval`):** entre la v1 y la v2, Operaciones · Transporte cambió 1.200.000,00 y Tecnología · Licencias cambió -1.200.000,00. Ningún acta los aprueba.

**Compromiso del comité (acta 06, 2026-09-10):** Administración revisa el contrato de vigilancia antes del próximo comité. Sigue abierto y sin evidencia.

# Ejecución contra aprobado · Tiendas Pacífico · presupuesto 2026, corte 2026-09

**Entidad:** Tiendas Pacífico (76083001-1) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Contralor

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 175.000,00 en 2026-08 sin línea presupuestal | 175.000,00 | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 6.000.000,00 | 4.500.000,00 | 4.850.000,00 | 150.000,00 | 1.000.000,00 | 350.000,00 | 7,78 |
| Administración | Servicios públicos | 9.000.000,00 | 6.750.000,00 | 6.547.500,00 | 225.000,00 | 2.227.500,00 | -202.500,00 | -3,00 |
| Comercial | Eventos | 5.250.000,00 | 3.750.000,00 | 3.637.500,00 | 150.000,00 | 1.462.500,00 | -112.500,00 | -3,00 |
| Comercial | Publicidad | 11.250.000,00 | 8.625.000,00 | 8.366.250,00 | 262.500,00 | 2.621.250,00 | -258.750,00 | -3,00 |
| Operaciones | Transporte | 11.700.000,00 | 8.475.000,00 | 8.220.750,00 | 322.500,00 | 3.156.750,00 | -254.250,00 | -3,00 |
| Tecnología | Licencias | 13.800.000,00 | 10.650.000,00 | 10.330.500,00 | 315.000,00 | 3.154.500,00 | -319.500,00 | -3,00 |
| Tecnología | PRY-310 | 18.000.000,00 | 13.500.000,00 | 13.095.000,00 | 450.000,00 | 4.455.000,00 | -405.000,00 | -3,00 |
| Personal | Nómina | 60.000.000,00 | 45.000.000,00 | 45.000.000,00 | 1.500.000,00 | 13.500.000,00 | 0,00 | 0,00 |

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Respuestas por defecto (sesión sin interfaz):**
- Las áreas salen del presupuesto. No hay responsables nombrados, porque ningún documento los trae.
- Los umbrales son los de `config.example.json`: desviación 10 %, comprometido 95 %, proyección vencida a 45 días.
- No hay fechas de comité.
- Las fichas del PMO están en `estado-pmo/records`.
- El estado queda en `estado-finanzas/76083001-1-tiendas-pacifico`.
- No creé la marca `_CRITERIO_FINANZAS.txt`, porque nadie la autorizó.
- El mapeo de cuentas a líneas ya estaba en `00-referencia/mapeo-presupuesto.csv`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

**Qué escribí:**
- Escribí la configuración en `.criterio/presupuesto/76083001-1-tiendas-pacifico/config.json`. La de finanzas que ya había no sirve para este agente.
- Escribí la ficha en `estado-finanzas/76083001-1-tiendas-pacifico/presupuesto/2026/ficha.json`.
- Dejé esta salida en `corridas/salida-budget-setup.md` y registré la corrida como `2026-10-06-budget-setup-1`.