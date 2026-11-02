# /criterio-treasury:treasury-setup finanzas/88733016-9-comercial-control-del-paraguay-sintetica

Áurea quedó instalada para Comercial Control del Paraguay (sintética) y calculó la primera posición de caja de 2026-09. Corrí todo con `--today 2026-10-06`.

**Lo que encontré**
- Hay 2 cuentas con extracto (`andino-13901` y `pacifico-13902`), programa de pagos, política, matriz de firmas y registro de deuda.
- La caja consolidada es **347.120.000,00 PYG**.
- `andino-13901` tiene 107.120.000,00 contra un mínimo de 45.560.000,00. `pacifico-13902` tiene 240.000.000,00 contra 112.000.000,00. Las dos están por encima del mínimo.
- La desviación contra la proyección es 0,00 % en ambas.
- No hay señales abiertas y todo lo que llegó se procesó.

**Lo que dejé escrito**
- **Configuración:** `.criterio/tesoreria/88733016-9-comercial-control-del-paraguay-sintetica/config.json`. Entidad, moneda (PYG) y estado vienen de la configuración de Clara; no hay cuentas en otra moneda. Los umbrales son los de `config.example.json` (10 %, 30 días, 10 %).
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez para la versión 1.2.0. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`, con el nombre `aceptacion-criterio-treasury-1.2.0-2026-10-06`.
- **Reporte:** `estado-finanzas/88733016-9-comercial-control-del-paraguay-sintetica/tesoreria/2026-09/reporte-cash-position.md`.
- **Corrida:** registrada como `2026-10-06-treasury-setup-1`, con 0 hallazgos. Lo que te mostré quedó en `corridas/salida-treasury-setup.md` dentro del estado.

Como nadie podía contestar, no hice preguntas: tomé las respuestas sugeridas por los documentos. No escribí la marca de la raíz, porque la persona no la autorizó.

Áurea vuelve cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.