# /criterio-budget:budget-setup finanzas/900000001-distribuidora-control

## Listo — Distribuidora Control (900000001) · presupuesto 2026

La instalación quedó hecha y la corrida registrada como `2026-10-06-budget-setup-1`. La ejecución contra lo aprobado dio −3,00 % de desviación en siete líneas y 0,00 % en Nómina. Ninguna pasa el umbral del 10 % y no quedó ninguna señal abierta.

**Lo que miré:**
- 2 versiones del presupuesto: la v1 del 2026-01-15 y la v2 del 2026-06-30.
- Contabilidad de 2026-01 a 2026-09.
- 3 actas.
- Compromisos y proyecciones de 5 áreas al 2026-09-30.

**Versión aprobada:**
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) aprueba un traslado de 1.500.000,00 de Publicidad a Eventos y no nombra la v2.
- El motor calcula contra la v2, que es la vigente. Esa diferencia queda anotada en la ficha como pregunta.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.8.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.8.0-2026-10-06.md` y `.pdf`.

**Respuestas que tomé yo, porque nadie contestó:**
- **Umbrales:** los de `config.example.json`. Son 10 % de desviación, 95 % de comprometido y 45 días para una proyección vencida.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Fechas del comité:** ninguna, porque ningún documento las trae.
- **Responsables por área:** no los encontré en los documentos. Solo Administración aparece, con el compromiso de revisar el contrato de vigilancia.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt` en la carpeta de documentos porque nadie lo autorizó.

## Ejecución contra lo aprobado, corte 2026-09

Reporte completo del motor: `estado-finanzas/900000001-distribuidora-control/presupuesto/2026/reporte-variance-report.md`.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 12.000.000,00 | 9.000.000,00 | 8.730.000,00 | 300.000,00 | 2.970.000,00 | -270.000,00 | -3,00 |
| Administración | Servicios públicos | 18.000.000,00 | 13.500.000,00 | 13.095.000,00 | 450.000,00 | 4.455.000,00 | -405.000,00 | -3,00 |
| Comercial | Eventos | 10.500.000,00 | 7.500.000,00 | 7.275.000,00 | 300.000,00 | 2.925.000,00 | -225.000,00 | -3,00 |
| Comercial | Publicidad | 22.500.000,00 | 17.250.000,00 | 16.732.500,00 | 525.000,00 | 5.242.500,00 | -517.500,00 | -3,00 |
| Operaciones | Transporte | 21.000.000,00 | 15.750.000,00 | 15.277.500,00 | 525.000,00 | 5.197.500,00 | -472.500,00 | -3,00 |
| Tecnología | Licencias | 30.000.000,00 | 22.500.000,00 | 21.825.000,00 | 750.000,00 | 7.425.000,00 | -675.000,00 | -3,00 |
| Tecnología | PRY-310 | 36.000.000,00 | 27.000.000,00 | 26.190.000,00 | 900.000,00 | 8.910.000,00 | -810.000,00 | -3,00 |
| Personal | Nómina | 120.000.000,00 | 90.000.000,00 | 90.000.000,00 | 3.000.000,00 | 27.000.000,00 | 0,00 | 0,00 |

Antes de registrar el acta 05 en la ficha, `compute` marcaba 2 señales `transfer_without_approval`. Con el acta registrada desaparecieron. El correo de Administración dice que está dentro del presupuesto, y los números lo sostienen.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La salida completa quedó en `estado-finanzas/900000001-distribuidora-control/corridas/salida-budget-setup.md`.