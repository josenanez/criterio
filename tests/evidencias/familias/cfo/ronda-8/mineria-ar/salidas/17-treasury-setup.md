# /criterio-treasury:treasury-setup finanzas/30709031143-minera-cordillera-de-cuyo

Áurea quedó instalada para Minera Cordillera de Cuyo. La primera posición de caja de 2026-09 ya está calculada y la corrida quedó registrada.

**Caja consolidada al 2026-09-30:** 147.814.500,00 ARS. Las dos cuentas están por encima de su mínimo y sin desviación contra la proyección.

| Cuenta | Saldo | Mínimo |
|---|---|---|
| andino-6701 | 57.814.500,00 | 25.907.250,00 |
| pacifico-6702 | 90.000.000,00 | 42.000.000,00 |

- **Señales fuera de este reporte:** el motor detectó 3: un pago sin aprobación, un vencimiento cercano y un covenant en riesgo. El reporte de caja no las muestra. Se revisan con `/payment-check` y `/debt-watch`; todavía no las corrí.
- **Términos:** José Francisco Ñáñez los aceptó (términos 1.3, familia 1.0.0). Los comprobantes quedaron en `.criterio/terminos/`.
- **Respuestas por defecto:** nadie podía contestar, así que tomé las sugeridas de los documentos. Usé la moneda ARS y el aprobador Sofía León de la configuración de Clara. Los umbrales son los del ejemplo (10 %, 30 días, 10 %). No declaré cuentas en otra moneda, porque el motor toma la moneda de la columna del extracto.
- **Marca de la raíz:** no puse `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie lo autorizó.

Archivos creados:
- `.criterio/tesoreria/30709031143/config.json`
- `estado-finanzas/30709031143-minera-cordillera-de-cuyo/tesoreria/2026-09/reporte-cash-position.md`
- `estado-finanzas/30709031143-minera-cordillera-de-cuyo/corridas/salida-treasury-setup.md`