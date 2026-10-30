# /criterio-finance:finance-setup finanzas/30709031143-minera-cordillera-de-cuyo

Soy Clara. Proceso los documentos de tu cierre y te muestro qué cuadra, qué no y qué no tiene soporte.

Nadie respondió preguntas en esta prueba, así que tomé las respuestas sugeridas por los documentos. Están en «Las preguntas que hizo» del reporte. El marco contable (NIIF adoptadas por la FACPCE, RT 26) no sale de ningún documento y queda por confirmar. No marqué la carpeta con `_CRITERIO_FINANZAS.txt` porque no hubo un sí.

## Listo — Minera Cordillera de Cuyo

- **Lo que miré:** 67 archivos, los periodos 2026-01 a 2026-09 y presupuesto-2026. Ninguno quedó fuera de la estructura.
- **Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.0.0 (términos 1.3). El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.
- **Estado del cierre 2026-09:** el correo de Sofía León del 2026-10-05 lo declara «en curso». El avance con evidencia es 53,85 %, igual que el declarado.
- **Checklist:** no está aprobado, así que una persona tiene que aprobarlo antes de dar el estado por bueno.
- **Tareas:** C-01 a C-05 están cumplidas con soporte. C-06 y C-07 están en plazo. C-08 y C-09 están bloqueadas.
- **Ruta crítica:** C-07 → C-08 → C-09.
- **Señales abiertas:** el motor encontró 4: una factura duplicada, una factura sin registro, una cuenta bancaria sin conciliar y un requerimiento del auditor sin respuesta. Son de einvoice-check, bank-reconcile y audit-pack. El reporte de estado del cierre dice «Nada abierto» porque no las desarrolla.
- **Para mejorar:** falta que una persona apruebe el checklist, confirmar el marco contable y cargar los festivos. También falta responder el requerimiento R-09 (partidas conciliatorias de más de 90 días), que vence el 2026-10-09.
- **Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

**Dónde quedó todo:**
- La configuración está en `.criterio/finanzas/30709031143/config.json`.
- El reporte está en `estado-finanzas/30709031143-minera-cordillera-de-cuyo/cierre/2026-09/reporte-close-status.md`.
- La salida completa y la corrida registrada (`2026-10-06-finance-setup-1`) están en `estado-finanzas/30709031143-minera-cordillera-de-cuyo/corridas/`.