# /criterio-budget:budget-setup finanzas/31452078000170-lojas-paulistas

## Listo — Lojas Paulistas (31452078000170) · presupuesto 2026

**Lo que miré:**
- 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30).
- Contabilidad de 2026-01 a 2026-09.
- 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. El acta 01 aprueba la v1. El acta 05 respalda el traslado Publicidade → Eventos de 15.000,00.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.12.1 (términos 1.3), con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.12.1-2026-10-06.md` y en su `.pdf`.

**Lo que hay que atender (3 señales):**
- **Administração se reporta dentro del presupuesto, pero Serviços públicos no lo sostiene.** El correo del 2026-10-01 dice "dentro". La línea va +15,0 % sobre lo aprobado al corte (20.250,00).
- **Serviços públicos se pasa del umbral de 10 %.** Lleva 155.250,00 ejecutados contra 135.000,00 aprobados al corte.
- **Manutenção llega a 96,0 % entre ejecutado y comprometido.** Le quedan 4.750,00 disponibles.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administração | Serviços públicos | 180.000,00 | 135.000,00 | 155.250,00 | 4.500,00 | 20.250,00 | 20.250,00 | 15,00 |
| Administração | Manutenção | 120.000,00 | 90.000,00 | 87.300,00 | 27.950,00 | 4.750,00 | -2.700,00 | -3,00 |
| Comercial | Eventos | 105.000,00 | 75.000,00 | 72.750,00 | 3.000,00 | 29.250,00 | -2.250,00 | -3,00 |
| Comercial | Publicidade | 225.000,00 | 172.500,00 | 167.325,00 | 5.250,00 | 52.425,00 | -5.175,00 | -3,00 |
| Operações | Transporte | 210.000,00 | 157.500,00 | 152.775,00 | 5.250,00 | 51.975,00 | -4.725,00 | -3,00 |
| Tecnologia | Licenças | 300.000,00 | 225.000,00 | 218.250,00 | 7.500,00 | 74.250,00 | -6.750,00 | -3,00 |
| Tecnologia | PRY-310 | 360.000,00 | 270.000,00 | 261.900,00 | 9.000,00 | 89.100,00 | -8.100,00 | -3,00 |
| Pessoal | Folha de pagamento | 1.200.000,00 | 900.000,00 | 900.000,00 | 30.000,00 | 270.000,00 | 0,00 | 0,00 |

**Decisiones que tomé por mi cuenta en esta sesión sin interfaz:**
- **Umbrales:** usé los del ejemplo (10 % de desviación, 95 % de comprometido, 45 días de proyección vencida). Son configuración, no norma.
- **Fechas de comité:** ningún documento las trae, así que quedó vacío.
- **Proyectos PMO:** `pmo_records` apunta a `estado-pmo/records`, donde existe `PRY-310.json`.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó. No escribí nada dentro de los documentos.

**Dónde quedó todo:**
- Configuración: `.criterio/presupuesto/31452078000170/config.json`.
- Reporte completo: `estado-finanzas/31452078000170-lojas-paulistas/presupuesto/2026/reporte-variance-report.md`.
- Corrida registrada como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.