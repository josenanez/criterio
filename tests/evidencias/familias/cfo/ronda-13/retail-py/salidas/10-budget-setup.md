# /criterio-budget:budget-setup finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica

## Listo — Distribuidora del Ybytyruzú (sintética) · presupuesto 2026

**Lo que miré:** 2 versiones aprobadas, contabilidad de 2026-01 a 2026-09 y 3 actas.
**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`.
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) traslada 30.000.000,00 de Comercial · Publicidad a Comercial · Eventos.

**Términos:** aceptados para la versión 1.2.0 por José Francisco Ñáñez, con el comprobante en `.criterio/terminos/`.

**Respuestas que tomé por defecto (nadie contestó):**
- Estado en `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica`, la misma carpeta que ya usaba Clara.
- Fichas PMO en `estado-pmo/records`, donde está PRY-310.
- Fechas del comité: ninguna, porque los documentos no traen una futura. El campo queda vacío.
- Umbrales de `config.example.json`: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie lo autorizó.

El resumen de la corrida se registró con 0 preguntas a la persona. Los minutos hasta el primer resultado no los medí.

# Ejecución contra aprobado · presupuesto 2026, corte 2026-09

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`).

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Gasto sin línea presupuestal (`spend_without_budget_line`) | Cuenta 5135 · centro ZZZ: 7.000.000,00 en 2026-08 | 7.000.000,00 | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |
| 2 | Ejecutado más comprometido sin holgura (`committed_near_approved`) | Administración · Mantenimiento: 96,0 % de lo aprobado en el año | -9.500.000,00 | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.csv` fila 4 · `2026-02/10-contabilidad/libro-mayor.csv` fila 4 |

## El resultado

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 240.000.000,00 | 180.000.000,00 | 174.600.000,00 | 55.900.000,00 | 9.500.000,00 | -5.400.000,00 | -3,00 |
| Administración | Servicios públicos | 360.000.000,00 | 270.000.000,00 | 261.900.000,00 | 9.000.000,00 | 89.100.000,00 | -8.100.000,00 | -3,00 |
| Comercial | Eventos | 210.000.000,00 | 150.000.000,00 | 145.500.000,00 | 6.000.000,00 | 58.500.000,00 | -4.500.000,00 | -3,00 |
| Comercial | Publicidad | 450.000.000,00 | 345.000.000,00 | 334.650.000,00 | 10.500.000,00 | 104.850.000,00 | -10.350.000,00 | -3,00 |
| Operaciones | Transporte | 420.000.000,00 | 315.000.000,00 | 305.550.000,00 | 10.500.000,00 | 103.950.000,00 | -9.450.000,00 | -3,00 |
| Tecnología | Licencias | 600.000.000,00 | 450.000.000,00 | 436.500.000,00 | 15.000.000,00 | 148.500.000,00 | -13.500.000,00 | -3,00 |
| Tecnología | PRY-310 | 720.000.000,00 | 540.000.000,00 | 523.800.000,00 | 18.000.000,00 | 178.200.000,00 | -16.200.000,00 | -3,00 |
| Personal | Nómina | 2.400.000.000,00 | 1.800.000.000,00 | 1.800.000.000,00 | 60.000.000,00 | 540.000.000,00 | 0,00 | 0,00 |

**Nota:** `compute` devolvió tres señales, pero el reporte muestra dos. La tercera, `forecast_stale`, no aparece en el reporte. Casi seguro es la proyección de Operaciones, que es del 2026-07-15 mientras las demás son del 2026-09-30. Es una inferencia por el nombre del archivo y no la verifiqué.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

**Archivos:**
- Configuración: `.criterio/presupuesto/88612904-4/config.json`
- Ficha: `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica/presupuesto/2026/ficha.json`
- Reporte: `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica/presupuesto/2026/reporte-variance-report.md`
- Salida de la corrida: `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-budget-setup.md`