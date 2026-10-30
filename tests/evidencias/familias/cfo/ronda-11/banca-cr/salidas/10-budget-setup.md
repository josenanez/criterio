# /criterio-budget:budget-setup finanzas/3101457812-banco-del-valle-central-sintetico

## Listo — Banco del Valle Central (sintético) · presupuesto 2026

**Lo que miré:**
- 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30).
- Contabilidad de 2026-01 a 2026-09.
- 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. El acta 01 (2026-01-20) aprueba la v1. El acta 05 (2026-06-28) aprueba el traslado de 3.000.000,00 de Publicidad a Eventos.

**Términos:** aceptados por José Francisco Ñáñez, versión 1.0.0, con comprobante en `.criterio/terminos/`.

**Lo que más pesa:** Administración · Servicios públicos lleva ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte, o sea +15,0 %. El correo de Administración del 2026-10-01 dice que el área va dentro del presupuesto, y los números no lo sostienen.

**Señales del cálculo:** son 4.
- `declared_vs_evidence`: 1.
- `transfer_without_approval`: 2.
- `variance_over_threshold`: 1.

El reporte muestra las dos de Servicios públicos. No traje el detalle de los dos traslados sin acta; ese lo da `transfer-log`.

**Lo que decidí por mi cuenta**, porque nadie respondió:
- Los umbrales son los del ejemplo: 10 % de desviación, 95 % de comprometido y 45 días para una proyección vencida.
- No hay fechas de comité en los documentos. El acta 06 es del 2026-09-10.
- Las fichas del PMO están en `estado-pmo/records`, donde existe `PRY-310.json`.
- No dejé la marca `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque escribir ahí necesita un sí explícito.
- Los responsables de cada área no aparecen en los documentos y quedaron sin registrar.
- Anoté un compromiso abierto del acta 06: Administración revisa el contrato de vigilancia antes del próximo comité.

### Ejecución contra aprobado (corte 2026-09)

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 36.000.000,00 | 27.000.000,00 | 31.050.000,00 | 900.000,00 | 4.050.000,00 | 4.050.000,00 | 15,00 |
| Administración | Mantenimiento | 24.000.000,00 | 18.000.000,00 | 17.460.000,00 | 600.000,00 | 5.940.000,00 | -540.000,00 | -3,00 |
| Comercial | Eventos | 21.000.000,00 | 15.000.000,00 | 14.550.000,00 | 600.000,00 | 5.850.000,00 | -450.000,00 | -3,00 |
| Comercial | Publicidad | 45.000.000,00 | 34.500.000,00 | 33.465.000,00 | 1.050.000,00 | 10.485.000,00 | -1.035.000,00 | -3,00 |
| Operaciones | Transporte | 46.800.000,00 | 33.900.000,00 | 32.883.000,00 | 1.290.000,00 | 12.627.000,00 | -1.017.000,00 | -3,00 |
| Tecnología | Licencias | 55.200.000,00 | 42.600.000,00 | 41.322.000,00 | 1.260.000,00 | 12.618.000,00 | -1.278.000,00 | -3,00 |
| Tecnología | PRY-310 | 72.000.000,00 | 54.000.000,00 | 52.380.000,00 | 1.800.000,00 | 17.820.000,00 | -1.620.000,00 | -3,00 |
| Personal | Nómina | 240.000.000,00 | 180.000.000,00 | 180.000.000,00 | 6.000.000,00 | 54.000.000,00 | 0,00 | 0,00 |

Todo lo que llegó se procesó.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La corrida quedó registrada como `2026-10-06-budget-setup-1`. La configuración está en `.criterio/presupuesto/3101457812/config.json`, y el reporte completo y la ficha están en `estado-finanzas/3101457812-banco-del-valle-central-sintetico/presupuesto/2026/`.