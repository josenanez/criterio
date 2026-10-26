# /criterio-budget:budget-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera (20710000019) · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** el acta 01 (2026-01-20) aprueba la versión 1. El acta 05 (2026-06-28) solo aprueba trasladar 12,000.00 de Publicidad a Eventos, de julio a diciembre. Ningún acta aprueba la versión 2 como tal. El motor trabaja con la 2 porque es la más reciente, así que conviene que lo confirmes.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.9.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.9.0-2026-10-06.md`. No mostré el texto de `en_corto` antes de registrar la aceptación; lo hice por tu instrucción de la prueba.

**Señales del motor:** 4 de `transfer_without_approval` y 1 de `variance_over_threshold`. El reporte detalla solo la de desviación. Los 4 traslados sin acta se ven con `transfer-log`, que no corrí en esta sesión.

**Respuestas que tomé por ti** (nadie podía contestar):
- **Entidad y año:** Banco Ribera, año 2026, corte 2026-09, aprueba Sofía León.
- **Umbrales:** los del ejemplo, 10 % de desviación, 95 % comprometido y 45 días de proyección vencida.
- **Cuentas de gasto:** prefijo 51.
- **Fichas PMO:** `estado-pmo/records`, donde encontré `PRY-310.json`.
- **Estado:** `estado-finanzas/20710000019-banco-ribera`.
- **Fechas de comité:** ninguna, porque ningún documento trae una.
- **Marca `_CRITERIO_FINANZAS.txt`:** no la dejé, porque nadie autorizó escribir en los documentos.

La configuración está en `.criterio/presupuesto/20710000019/config.json`. Ya existía una de finanzas para esta entidad en otra ruta y no la toqué.

# Ejecución contra aprobado · Banco Ribera · presupuesto 2026, corte 2026-09

**Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `variance-report`

### Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | `variance_over_threshold` | Administración · Servicios públicos: ejecutado 124,200.00 contra 108,000.00 aprobado al corte (+15.0 %) | 16,200.00 | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 2 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 2 |

### El resultado

Versión vigente: **2**. Periodos procesados: 2026-01 a 2026-09.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 144,000.00 | 108,000.00 | 124,200.00 | 3,600.00 | 16,200.00 | 16,200.00 | 15.00 |
| Administración | Mantenimiento | 96,000.00 | 72,000.00 | 69,840.00 | 2,400.00 | 23,760.00 | -2,160.00 | -3.00 |
| Comercial | Eventos | 84,000.00 | 60,000.00 | 58,200.00 | 2,400.00 | 23,400.00 | -1,800.00 | -3.00 |
| Comercial | Publicidad | 180,000.00 | 138,000.00 | 133,860.00 | 4,200.00 | 41,940.00 | -4,140.00 | -3.00 |
| Operaciones | Transporte | 187,200.00 | 135,600.00 | 131,532.00 | 5,160.00 | 50,508.00 | -4,068.00 | -3.00 |
| Tecnología | Licencias | 220,800.00 | 170,400.00 | 165,288.00 | 5,040.00 | 50,472.00 | -5,112.00 | -3.00 |
| Tecnología | PRY-310 | 288,000.00 | 216,000.00 | 209,520.00 | 7,200.00 | 71,280.00 | -6,480.00 | -3.00 |
| Personal | Nómina | 960,000.00 | 720,000.00 | 720,000.00 | 24,000.00 | 216,000.00 | 0.00 | 0.00 |

**Lo que no se pudo procesar:** todo lo que llegó se procesó.
**Preguntas que hizo el motor:** ninguna.
**Fuentes:** los libros mayores de 2026-01 y 2026-02 y la versión 2 del presupuesto.

La salida quedó en `estado-finanzas/20710000019-banco-ribera/corridas/salida-budget-setup.md`, y la corrida quedó registrada como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.