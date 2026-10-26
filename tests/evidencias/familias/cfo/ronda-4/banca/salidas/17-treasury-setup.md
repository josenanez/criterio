# /criterio-treasury:treasury-setup finanzas/900123456-banco-andino

Áurea quedó instalada para Banco Andino (900123456), periodo 2026-09, y la primera posición de caja ya está calculada. La cuenta andino-1101 está por debajo de su mínimo.

**Lo que miré:** 2 cuentas con extracto (andino-1101 y pacifico-1102), programa de pagos, política y registro de deuda. Todos estaban en la carpeta.

**Términos:** acepté la versión 0.10.0 (términos 1.2) a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md`, con su versión en PDF.

**Posición de caja al 2026-09-30** (cifras copiadas del reporte del motor):

| Cuenta | Saldo | Mínimo | Proyectado |
|---|---|---|---|
| andino-1101 | 13.273.400,00 | 16.928.080,00 | 13.273.400,00 |
| pacifico-1102 | 30.000.000,00 | 14.000.000,00 | 30.000.000,00 |

- **Caja consolidada:** 43.273.400,00.
- **Faltante en andino-1101:** 3.654.680,00 contra el mínimo de la política.
- **Otras dos señales:** el cálculo marcó un pago programado sin la aprobación que pide la política y un covenant en riesgo. No las revisé a fondo; las cubren `payment-check` y `debt-watch`.

**Lo que decidí por mi cuenta, porque nadie podía contestar:**
- **Carpeta raíz:** usé la que venía en el argumento y no corrí `buscar-raiz`.
- **Marca `_CRITERIO_FINANZAS.txt`:** no la puse. Escribe dentro de la carpeta de documentos y no hubo autorización.
- **Moneda:** dejé `treasury.currencies` vacío, porque ambas cuentas son COP.
- **Umbrales:** usé los de `config.example.json` (10 % de desviación, 30 días de vencimiento, 10 % de margen de covenant). Son configuración, no norma.
- **Aprobador:** Sofía León, tomada de la configuración de Clara.
- **Estado:** `estado-finanzas/900123456-banco-andino`, el mismo de Clara y Tomás.

**Un tropiezo:** la primera vez escribí la configuración en una ruta equivocada de la carpeta temporal. La borré y la dejé en `.criterio/tesoreria/900123456-banco-andino/config.json`.

Guardé la salida completa en `estado-finanzas/900123456-banco-andino/corridas/salida-treasury-setup.md` y registré la corrida como `2026-10-06-treasury-setup-1`.

Vuelvo cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.