# /criterio-budget:budget-setup finanzas/40217355000151-comercial-controle-paulista

## Listo — Comercial Controle Paulista · presupuesto 2026

Soy Tomás. Dejé la instalación hecha y la primera ejecución contra lo aprobado calculada al corte 2026-09, sin señales abiertas.

**Lo que miré:**
- 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30).
- Contabilidad de 2026-01 a 2026-09.
- 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`.
- Nace del acta 05 (`ata-05-remanejamento.md`), que traslada 12.000,00 de Publicidade a Eventos.
- La v1 la aprueba el acta 01 (`ata-01-aprovacao.docx`).
- No fijé `approved_version` por mi cuenta.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.12.1, con fecha 2026-10-06. Los comprobantes están en `.criterio/terminos/`. Un primer intento dejó un comprobante en una carpeta equivocada por un `cd` mío; lo borré y repetí el registro desde la raíz.

**Respuestas que tomé yo de los documentos** (sin interfaz, nadie contestó):
- **Umbrales:** los de `config.example.json`: desviación 10 %, comprometido 95 %, proyección vencida 45 días. Son configuración, no norma.
- **Fechas del comité:** quedó vacío. Ningún documento trae una fecha futura; el acta 06 es del 2026-09-10.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Prefijo de gasto:** `51`. Las cuentas del mapeo van de la 5105 a la 5195.
- **Marca de la raíz:** no escribí `_CRITERIO_FINANZAS.txt`. Era una pregunta con autorización y no hubo quién la diera.

**Ejecución contra lo aprobado**, copiada de la salida del motor:

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administração | Manutenção | 96.000,00 | 72.000,00 | 69.840,00 | 2.400,00 | 23.760,00 | -2.160,00 | -3,00 |
| Administração | Serviços públicos | 144.000,00 | 108.000,00 | 104.760,00 | 3.600,00 | 35.640,00 | -3.240,00 | -3,00 |
| Comercial | Eventos | 84.000,00 | 60.000,00 | 58.200,00 | 2.400,00 | 23.400,00 | -1.800,00 | -3,00 |
| Comercial | Publicidade | 180.000,00 | 138.000,00 | 133.860,00 | 4.200,00 | 41.940,00 | -4.140,00 | -3,00 |
| Operações | Transporte | 168.000,00 | 126.000,00 | 122.220,00 | 4.200,00 | 41.580,00 | -3.780,00 | -3,00 |
| Tecnologia | Licenças | 240.000,00 | 180.000,00 | 174.600,00 | 6.000,00 | 59.400,00 | -5.400,00 | -3,00 |
| Tecnologia | PRY-310 | 288.000,00 | 216.000,00 | 209.520,00 | 7.200,00 | 71.280,00 | -6.480,00 | -3,00 |
| Pessoal | Folha de pagamento | 960.000,00 | 720.000,00 | 720.000,00 | 24.000,00 | 216.000,00 | 0,00 | 0,00 |

Todo lo que llegó se procesó. El reporte completo, con las preguntas y las fuentes, está en `estado-finanzas/40217355000151-comercial-controle-paulista/presupuesto/2026/reporte-variance-report.md`. La salida entera quedó en `corridas/salida-budget-setup.md` y la corrida se registró como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.