# /criterio-treasury:treasury-setup finanzas/0990054321001-minera-condor

Áurea quedó instalada sobre Minera Cóndor y ya tiene su primera posición de caja del periodo 2026-09. Nadie respondió preguntas; tomé las respuestas de los documentos.

**Lo que miré:** 2 cuentas con extracto (andino-4101 y pacifico-4102). También hay programa de pagos, política de tesorería y registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2), con fecha 2026-10-06. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md`, con su versión en PDF.

**Posición de caja al 2026-09-30** (copiada del reporte del motor):

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-4101 | USD | 25,089.00 | 10,544.50 | 25,089.00 | 0.00 |
| pacifico-4102 | USD | 60,000.00 | 28,000.00 | 78,000.00 | -23.08 |

- **Caja consolidada:** 85,089.00.
- **Señal que atender:** pacifico-4102 está 18,000.00 por debajo de su proyección, un -23.08 % frente al umbral del 10 %. Ninguna cuenta está bajo su mínimo.
- **Otras señales:** el cálculo detectó además un pago sin aprobación suficiente y un covenant en riesgo. Quedaron registradas en los resultados y todavía no las revisé; las detallan `payment-check` y `debt-watch`.
- **Procesamiento:** todo lo que llegó se procesó.

**Cómo quedó configurada:**
- **Entidad:** tomé los datos de la configuración de Clara: Ecuador, USD, aprueba Sofía León.
- **Monedas:** no hay cuentas en otra moneda, así que `treasury.currencies` quedó vacío.
- **Umbrales:** usé los de `config.example.json`: desviación 10 %, vencimiento 30 días, margen del covenant 10 %. Son configuración, no norma.
- **Estado:** el mismo de Clara, `estado-finanzas/0990054321001-minera-condor`.
- **No hice:** no marqué la carpeta raíz, porque no hubo un sí para eso.

**Archivos:**
- Configuración: `.criterio/tesoreria/0990054321001/config.json`
- Reporte: `estado-finanzas/0990054321001-minera-condor/tesoreria/2026-09/reporte-cash-position.md`
- Salida de esta instalación: `estado-finanzas/0990054321001-minera-condor/corridas/salida-treasury-setup.md`
- Corrida registrada: `2026-10-06-treasury-setup-1` (3 hallazgos).

**Cuándo vuelve Áurea:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.