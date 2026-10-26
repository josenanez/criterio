# /criterio-treasury:treasury-setup finanzas/1790012345001-cooperativa-sierra-alta

Áurea quedó instalada para Cooperativa Sierra Alta, pero la posición de caja cubre solo una de las dos cuentas. A `pacifico-2302` le falta el extracto. Nadie respondió preguntas, así que tomé las respuestas de los documentos. Los términos los registré a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Las cifras salen del motor.

**Lo que miré**
- Hay extracto solo de `andino-2301`; `pacifico-2302` trae únicamente el auxiliar de libros.
- Están el programa de pagos, la política de tesorería y el registro de deuda.

**Lo que decidí sin preguntar**
- **Periodo y moneda:** 2026-09, todo en USD, sin cuentas en otra moneda.
- **Umbrales:** los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant.
- **Estado:** `estado-finanzas/1790012345001-cooperativa-sierra-alta`.
- **Marca de la raíz:** no puse `_CRITERIO_FINANZAS.txt` en la carpeta de documentos porque nadie lo autorizó.

**Primera posición de caja**
- **Caja consolidada:** 6,560.00, que es solo `andino-2301`.
- **Mínimo de la política:** 2,280.00, así que la cuenta está por encima.
- **Contra la proyección:** el saldo es 6,560.00 y lo proyectado 8,528.00, una desviación de -23.08 % (1,968.00 de diferencia). Supera el umbral y quedó como señal para atender.
- **Otras señales:** el cálculo dejó dos más que este reporte no trae, un firmante sin autoridad y un vencimiento cercano. El registro de deuda lista un crédito de tesorería con vencimiento 2026-10-26.

El reporte completo y todo lo que te mostré está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-treasury-setup.md`, y la corrida quedó registrada con el id `2026-10-06-treasury-setup-1`. El comprobante de los términos está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md` y en PDF.

Cuando llegue el extracto de `pacifico-2302`, la caja consolidada cambia, así que conviene volver a correr `cash-position`.