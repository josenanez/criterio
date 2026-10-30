# /criterio-budget:budget-setup finanzas/28903114000160-mineracao-serra-azul

## Listo — Mineração Serra Azul · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/` (fechada 2026-06-30). La v1 la aprueba el acta `presupuesto-2026/40-actas/ata-01-aprovacao.docx`. No hay acta que apruebe la v2.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.12.1 (términos 1.3). El comprobante quedó en `.criterio/terminos/`.

**Configuración:** `.criterio/presupuesto/28903114000160/config.json`. Es válida.

**Ejecución contra lo aprobado, al corte 2026-09:**

| Área | Línea | Aprobado | Ejecutado | Comprometido | Disponible | % |
|---|---|---|---|---|---|---|
| Administração | Manutenção | 240.000,00 | 174.600,00 | 6.000,00 | 59.400,00 | -3,00 |
| Administração | Serviços públicos | 360.000,00 | 261.900,00 | 9.000,00 | 89.100,00 | -3,00 |
| Comercial | Eventos | 210.000,00 | 145.500,00 | 6.000,00 | 58.500,00 | -3,00 |
| Comercial | Publicidade | 450.000,00 | 334.650,00 | 10.500,00 | 104.850,00 | -3,00 |
| Operações | Transporte | 468.000,00 | 328.830,00 | 12.900,00 | 126.270,00 | -3,00 |
| Tecnologia | Licenças | 552.000,00 | 413.220,00 | 12.600,00 | 126.180,00 | -3,00 |
| Tecnologia | PRY-310 | 720.000,00 | 523.800,00 | 18.000,00 | 178.200,00 | -3,00 |
| Pessoal | Folha de pagamento | 2.400.000,00 | 1.800.000,00 | 60.000,00 | 540.000,00 | 0,00 |

El reporte completo está en `estado-finanzas/28903114000160-mineracao-serra-azul/presupuesto/2026/reporte-variance-report.md`. En esa tabla faltan las columnas "Al corte" y "Desviación" de ese reporte.

**Señales que el reporte no muestra.** `compute` levantó 5:
- `transfer_without_approval`: 2.
- `budget_version_mismatch`: 2.
- `forecast_stale`: 1.

Esas señales corresponden a otros comandos. Se revisan con `/transfer-log` y `/forecast`.

**Decisiones por defecto, porque nadie respondió:**
- **Corte:** 2026-09.
- **Umbrales:** los de `config.example.json` (10 % de desviación, 95 % comprometido, 45 días de proyección vencida).
- **Gasto:** cuentas con prefijo `51`.
- **Fechas del comité:** no las encontré en los documentos, así que quedan vacías.
- **Fichas PMO:** apunté a `estado-pmo/records`, donde existe `PRY-310.json`.
- **Estado:** `estado-finanzas/28903114000160-mineracao-serra-azul`, que ya existía.
- **Marca de la raíz:** no la escribí, porque nadie autorizó dejar `_CRITERIO_FINANZAS.txt`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La corrida quedó registrada como `2026-10-06-budget-setup-1`, y lo que te mostré está en `estado-finanzas/28903114000160-mineracao-serra-azul/corridas/salida-budget-setup.md`.