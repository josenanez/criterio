# /criterio-budget:budget-setup finanzas/900123456-banco-andino

## Listo — Banco Andino · presupuesto 2026

La instalación quedó hecha y la primera ejecución contra lo aprobado está calculada. Corté en 2026-09. Pasé `--today 2026-10-06` en las llamadas que lo aceptan. La configuración está en `.criterio/presupuesto/900123456-banco-andino/config.json` y pasó la validación.

**Lo que miré:**
- 2 versiones del presupuesto: v1 del 2026-01-15 y v2 del 2026-06-30.
- Contabilidad de 2026-01 a 2026-09, 9 periodos.
- 3 actas.

**Versión aprobada:**
- El motor toma como vigente la v2.
- El único acta de aprobación (acta 01, 2026-01-20) dice «se aprueba el presupuesto 2026, versión 1». Ninguna acta aprueba la v2 como tal.
- El acta 05 (2026-06-28) aprueba trasladar 3,000,000.00 de Publicidad a Eventos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.9.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.9.0-2026-10-06.md` y `.pdf`.

**Respuestas que tomé sin preguntar:**
- **Umbrales:** los del ejemplo: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- **Comité:** 2026-10-15, la fecha del ejemplo. Ningún documento da otra.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Estado:** `estado-finanzas/900123456-banco-andino`, fuera de los documentos.
- **Marca de la raíz:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie podía autorizarlo.

**Lo que hay que atender (6 señales):**
1. **Administración · Servicios públicos:** ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %).
2. **PRY-310:** la ficha dice 64.800.000,00 y el área tiene asignado 72.000.000,00.
3. **Cuatro cambios entre v1 y v2 sin acta registrada:** Transporte +4.800.000,00, Licencias -4.800.000,00, Eventos +3.000.000,00 y Publicidad -3.000.000,00.
   - Eventos y Publicidad coinciden con lo que describe el acta 05. Su ficha aún no está registrada, y por eso el motor los cuenta como sin acta.
   - Transporte y Licencias no tienen acta en la carpeta.

**Ejecución contra aprobado, versión 2, corte 2026-09**

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

**Lo que no se pudo procesar:** nada; todo lo que llegó se procesó.

**Pendientes:**
- No registré la ficha del acta 05 ni el compromiso del acta 06 (Administración revisa el contrato de vigilancia antes del próximo comité).
- Con la ficha del acta 05 registrada, dos de las cuatro señales de traslado se resolverían.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La salida completa está en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-setup.md`, y la corrida quedó registrada como `2026-10-06-budget-setup-1`. Los reportes del motor están en `estado-finanzas/900123456-banco-andino/presupuesto/2026/`.