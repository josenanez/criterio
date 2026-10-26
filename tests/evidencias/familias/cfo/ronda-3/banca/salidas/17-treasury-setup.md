# /criterio-treasury:treasury-setup finanzas/900123456-banco-andino

Soy Áurea. Pongo la caja, los pagos y la deuda al lado de su política, y le digo dónde no cuadran. No muevo dinero.

Nadie podía contestar en esta sesión, así que tomé las respuestas sugeridas de los documentos:
- **Umbrales:** los de `config.example.json`.
- **Estado:** `estado-finanzas/900123456-banco-andino`.
- **Moneda:** sin cuentas en otra moneda.
- **Aprueba:** Sofía León, como en la configuración de Clara.

## Listo — Banco Andino · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto · programa de pagos sí · política sí · registro de deuda sí.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.9.0 (términos 1.2), el 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.9.0-2026-10-06.md`.

# La posición de caja · Banco Andino · periodo 2026-09

**Caja consolidada:** 43.273.400,00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-1101 | COP | 13.273.400,00 | 16.928.080,00 | 13.273.400,00 | 0,00 |
| pacifico-1102 | COP | 30.000.000,00 | 14.000.000,00 | 30.000.000,00 | 0,00 |

**Señal:** andino-1101 queda por debajo del mínimo de la política por 3.654.680,00. Las fuentes son `2026-09/20-bancos/andino-1101/extracto.xlsx` fila 17 y `00-referencia/politica-tesoreria.csv` fila 2.

El cálculo también detectó un pago sin aprobación y un covenant en riesgo. Su detalle sale con `payment-check` y `debt-watch`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

## Lo que quedó escrito

- **Configuración:** `.criterio/tesoreria/900123456-banco-andino/config.json`, que el motor validó sin problemas.
- **Reporte del motor:** `estado-finanzas/900123456-banco-andino/tesoreria/2026-09/reporte-cash-position.md`.
- **Salida de esta corrida:** `estado-finanzas/900123456-banco-andino/corridas/salida-treasury-setup.md`.
- **Corrida registrada:** `2026-10-06-treasury-setup-1`, con 3 hallazgos.

No hice preguntas. No medí los minutos hasta el primer resultado. No marqué la raíz con `marcar-raiz`: la carpeta ya traía la marca de Clara y Tomás.