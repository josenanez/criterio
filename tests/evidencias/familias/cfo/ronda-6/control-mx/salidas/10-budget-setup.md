# /criterio-budget:budget-setup finanzas/CCM120615R59-comercial-control-centro

## Listo: Comercial Control Centro, presupuesto 2026

**Lo que miré:**
- 2 versiones del presupuesto: v1 y v2.
- Contabilidad de 2026-01 a 2026-09.
- 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. No fijé `approved_version` por mi cuenta. Las actas que la respaldan:
- El acta 01, del 2026-01-20, aprueba la v1.
- El acta 05, del 2026-06-28, aprueba el traslado de 36,000.00 de Publicidad a Eventos.

**Términos:** aceptados por José Francisco Ñáñez, con fecha 2026-10-06, para la versión 0.11.0. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.

**Respuestas por defecto** (nadie respondió, así que usé las sugeridas):
- Los umbrales son los de `config.example.json`: desviación 10 %, comprometido 95 % y proyección vencida a 45 días.
- No registré fechas de comité, porque el acta 06 solo dice «próximo comité».
- Las fichas PMO están en `estado-pmo/records`.
- El estado quedó en `estado-finanzas/CCM120615R59-comercial-control-centro`.
- No dejé la marca `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie la autorizó.

**Resultado al corte 2026-09.** El motor no levantó ninguna señal. El reporte dice «Nada abierto en lo que procesa este comando».

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 288,000.00 | 216,000.00 | 209,520.00 | 7,200.00 | 71,280.00 | -6,480.00 | -3.00 |
| Administración | Servicios públicos | 432,000.00 | 324,000.00 | 314,280.00 | 10,800.00 | 106,920.00 | -9,720.00 | -3.00 |
| Comercial | Eventos | 252,000.00 | 180,000.00 | 174,600.00 | 7,200.00 | 70,200.00 | -5,400.00 | -3.00 |
| Comercial | Publicidad | 540,000.00 | 414,000.00 | 401,580.00 | 12,600.00 | 125,820.00 | -12,420.00 | -3.00 |
| Operaciones | Transporte | 504,000.00 | 378,000.00 | 366,660.00 | 12,600.00 | 124,740.00 | -11,340.00 | -3.00 |
| Tecnología | Licencias | 720,000.00 | 540,000.00 | 523,800.00 | 18,000.00 | 178,200.00 | -16,200.00 | -3.00 |
| Tecnología | PRY-310 | 864,000.00 | 648,000.00 | 628,560.00 | 21,600.00 | 213,840.00 | -19,440.00 | -3.00 |
| Personal | Nómina | 2,880,000.00 | 2,160,000.00 | 2,160,000.00 | 72,000.00 | 648,000.00 | 0.00 | 0.00 |

- **Registrados en la ficha:** el compromiso abierto del acta 06 (Administración revisa el contrato de vigilancia) y la declaración de Administración de que va dentro del presupuesto. Ninguno generó señal.
- **Sección «Fuentes»:** el reporte del motor dice «Sin documentos citados». No lo corregí.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La salida completa quedó en `estado-finanzas/CCM120615R59-comercial-control-centro/corridas/salida-budget-setup.md`. La corrida quedó registrada con el id `2026-10-06-budget-setup-1`.