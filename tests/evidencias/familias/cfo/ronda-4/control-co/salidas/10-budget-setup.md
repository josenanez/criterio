# /criterio-budget:budget-setup finanzas/900000001-distribuidora-control

## Listo — Distribuidora Control (900000001) · presupuesto 2026

- **Qué miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.
- **Versión que rige:** la 2, del 2026-06-30. Es la más reciente de `10-aprobado/`, y no fijé `approved_version` por mi cuenta.
- **Actas registradas en la ficha:**
  - El acta 01 (2026-01-20) aprueba la v1.
  - El acta 05 (2026-06-28) traslada 1.500.000 de Comercial · Publicidad a Comercial · Eventos.
  - El acta 06 (2026-09-10) deja a Administración el compromiso de revisar el contrato de vigilancia.
- **Términos:** aceptados a nombre de José Francisco Ñáñez para la versión 0.10.0 (términos 1.2, 2026-10-06). El comprobante quedó en `.criterio/terminos/`.
- **Señales:** el primer `compute` mostró `transfer_without_approval` con 2. Al registrar el acta 05 en la ficha, el segundo `compute` dio 0 señales y el reporte no tiene nada abierto.

| Área | Línea | Aprobado | Ejecutado | Comprometido | Disponible | Desviación % |
|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 12.000.000,00 | 8.730.000,00 | 300.000,00 | 2.970.000,00 | -3,00 |
| Administración | Servicios públicos | 18.000.000,00 | 13.095.000,00 | 450.000,00 | 4.455.000,00 | -3,00 |
| Comercial | Eventos | 10.500.000,00 | 7.275.000,00 | 300.000,00 | 2.925.000,00 | -3,00 |
| Comercial | Publicidad | 22.500.000,00 | 16.732.500,00 | 525.000,00 | 5.242.500,00 | -3,00 |
| Operaciones | Transporte | 21.000.000,00 | 15.277.500,00 | 525.000,00 | 5.197.500,00 | -3,00 |
| Tecnología | Licencias | 30.000.000,00 | 21.825.000,00 | 750.000,00 | 7.425.000,00 | -3,00 |
| Tecnología | PRY-310 | 36.000.000,00 | 26.190.000,00 | 900.000,00 | 8.910.000,00 | -3,00 |
| Personal | Nómina | 120.000.000,00 | 90.000.000,00 | 3.000.000,00 | 27.000.000,00 | 0,00 |

La tabla del reporte tiene también la columna «Al corte»; aquí la omití. Lo demás sale tal cual del reporte del motor.

**Respuestas por defecto, sin nadie que contestara:**
- **Umbrales:** los de `config.example.json`. La desviación es 10 %, lo comprometido 95 % y una proyección vence a los 45 días.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Fechas del comité:** quedó vacío, porque ningún documento trae una fecha futura.
- **`expense_prefixes`:** quedó `["51","52"]`, como en el ejemplo, aunque el mapeo solo usa cuentas 51xx.
- **Marca de la raíz:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie la autorizó.

**Cosas por revisar:**
- El reporte dice «Sin documentos citados» en Fuentes, aunque la ficha cita las actas y el correo de Administración. Lo dejo como lo dio el motor.
- No medí los minutos hasta el primer resultado.

**Dónde quedó todo:**
- Configuración: `.criterio/presupuesto/900000001/config.json`.
- Ficha: `estado-finanzas/900000001-distribuidora-control/presupuesto/2026/ficha.json`.
- Reporte: `estado-finanzas/900000001-distribuidora-control/presupuesto/2026/reporte-variance-report.md`.
- Corrida registrada como `2026-10-06-budget-setup-1`.

Vuelvo cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.