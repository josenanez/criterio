# /criterio-budget:budget-setup finanzas/30714520780-almacenes-del-plata

## Listo — Almacenes del Plata · presupuesto 2026

El presupuesto 2026 de Almacenes del Plata quedó instalado y calculado contra la versión 2, con corte a septiembre. Salieron 3 señales, todas en Administración.

**Lo que miré:** 2 versiones (v1 de 2026-01-15, v2 de 2026-06-30) · contabilidad de 2026-01 a 2026-09 · 3 actas
**Versión aprobada:** la 2, que es la vigente por ser la más reciente. Nace del traslado del acta 05 (`presupuesto-2026/40-actas/acta-05-traslado.docx`, 2026-06-28). La v1 la aprobó el acta 01 (`presupuesto-2026/40-actas/acta-01-aprobacion.docx`, 2026-01-20). No fijé `approved_version`.
**Términos:** aceptados para la versión 1.0.0 por José Francisco Ñáñez, el 2026-10-06. El comprobante está en `.criterio/terminos/`.

### Lo que hay que atender

1. **Administración dice que va dentro del presupuesto y Servicios públicos no lo sostiene.** Lo dice el correo del 2026-10-01 (`presupuesto-2026/30-proyecciones/correo-administracion.md`). Esa línea está 6.075.000,00 por encima de lo aprobado.
2. **Administración · Servicios públicos:** ejecutado 46.575.000,00 contra 40.500.000,00 aprobado al corte (+15,0 %).
3. **Administración · Mantenimiento:** ejecutado más comprometido es el 96,0 % de lo aprobado en el año. Quedan 1.425.000,00 de disponible.

### Ejecución por área y línea (corte 2026-09)

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 54.000.000,00 | 40.500.000,00 | 46.575.000,00 | 1.350.000,00 | 6.075.000,00 | 6.075.000,00 | 15,00 |
| Administración | Mantenimiento | 36.000.000,00 | 27.000.000,00 | 26.190.000,00 | 8.385.000,00 | 1.425.000,00 | -810.000,00 | -3,00 |
| Comercial | Eventos | 31.500.000,00 | 22.500.000,00 | 21.825.000,00 | 900.000,00 | 8.775.000,00 | -675.000,00 | -3,00 |
| Comercial | Publicidad | 67.500.000,00 | 51.750.000,00 | 50.197.500,00 | 1.575.000,00 | 15.727.500,00 | -1.552.500,00 | -3,00 |
| Operaciones | Transporte | 63.000.000,00 | 47.250.000,00 | 45.832.500,00 | 1.575.000,00 | 15.592.500,00 | -1.417.500,00 | -3,00 |
| Tecnología | Licencias | 90.000.000,00 | 67.500.000,00 | 65.475.000,00 | 2.250.000,00 | 22.275.000,00 | -2.025.000,00 | -3,00 |
| Tecnología | PRY-310 | 108.000.000,00 | 81.000.000,00 | 78.570.000,00 | 2.700.000,00 | 26.730.000,00 | -2.430.000,00 | -3,00 |
| Personal | Nómina | 360.000.000,00 | 270.000.000,00 | 270.000.000,00 | 9.000.000,00 | 81.000.000,00 | 0,00 | 0,00 |

Todo lo que llegó se procesó. El reporte completo, con sus citas, está en `estado-finanzas/30714520780-almacenes-del-plata/presupuesto/2026/reporte-variance-report.md`.

### Las preguntas que resolví yo, sin que nadie contestara

- **Versión aprobada:** la v2, por ser la más reciente de `10-aprobado/`.
- **Umbrales:** los del ejemplo, 10 % de desviación, 95 % de comprometido y 45 días de proyección vencida. Son configuración, no norma.
- **Fechas del comité:** no están en los documentos, así que quedaron vacías.
- **Fichas de proyectos PMO:** las encontré en `estado-pmo/records`, con `PRY-310.json`.
- **Marca de la raíz** (`_CRITERIO_FINANZAS.txt`): no la dejé. En una sesión sin interfaz no hay quien la autorice.

El compromiso del acta 06 (Administración revisa el contrato de vigilancia antes del próximo comité) quedó registrado como abierto.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La configuración está en `.criterio/presupuesto/30714520780-almacenes-del-plata/config.json`. La corrida quedó registrada como `2026-10-06-budget-setup-1`.