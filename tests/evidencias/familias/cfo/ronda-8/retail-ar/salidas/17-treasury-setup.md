# /criterio-treasury:treasury-setup finanzas/30714520780-almacenes-del-plata

Áurea quedó instalada para Almacenes del Plata (30714520780), con la primera posición de caja del periodo 2026-09 calculada y la corrida registrada. Nadie respondió preguntas en esta sesión, así que tomé como respuesta lo que sugerían los documentos.

**Lo que había:** 2 cuentas con extracto (`andino-6101` y `pacifico-6102`), programa de pagos, flujo proyectado, política de tesorería, registro de deuda y covenants.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3) con fecha 2026-10-06. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md` y `.pdf`.

**Configuración:** `.criterio/tesoreria/30714520780-almacenes-del-plata/config.json`. Tomé estas respuestas de los documentos:
- **Moneda:** la funcional es ARS, como en la configuración de Clara. El extracto de `pacifico-6102` trae su moneda (USD), así que `treasury.currencies` quedó vacío.
- **Umbrales:** 10 % de desviación, 30 días de vencimiento y 10 % de margen de covenant, los de `config.example.json`.
- **Estado:** `estado-finanzas/30714520780-almacenes-del-plata`, el mismo de Clara y Tomás.

**Lo que muestra el reporte** (cifras copiadas de la salida del motor):
- **Exposición en USD sobre el límite:** `pacifico-6102` equivale a 65.250.000.000,00 ARS con la tasa de la política. El límite es 32.625.000.000,00.
- **Desviación contra la proyección:** `pacifico-6102` tiene 45.000.000,00 de saldo contra 58.500.000,00 proyectado, es decir -23,08 %.
- **`andino-6101`:** 10.778.400,00 ARS, igual a lo proyectado y sobre su mínimo de 3.889.200,00.
- **Caja consolidada:** 65.260.778.400,00.

El motor también marcó una señal de pagos, un firmante sin autoridad (`signatory_without_authority`). No está en este reporte; se revisa con `/payment-check`.

El reporte completo quedó en `estado-finanzas/30714520780-almacenes-del-plata/tesoreria/2026-09/reporte-cash-position.md`. Lo que te mostré aquí está en `estado-finanzas/30714520780-almacenes-del-plata/corridas/salida-treasury-setup.md`.