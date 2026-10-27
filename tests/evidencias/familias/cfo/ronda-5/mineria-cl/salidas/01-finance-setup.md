# /criterio-finance:finance-setup finanzas/76089001-4-minera-atacama-norte

## Listo — Minera Atacama Norte

**Lo que miré:** 63 archivos, periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno quedó fuera de la estructura.
**Términos:** aceptados a nombre de José Francisco Ñáñez para la versión 0.10.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y `.pdf`.

Nadie respondió preguntas en esta sesión, así que tomé cada respuesta de los documentos. Quedan registradas en la ficha del cierre. No marqué la carpeta con `_CRITERIO_FINANZAS.txt` porque nadie lo autorizó.

**Estado del cierre de 2026-09:**
- **Lo declarado:** Sofía León escribió el 2026-10-05 que el cierre está «en curso» (`2026-09/40-soportes/correo-estado-del-cierre.md`).
- **Avance:** 46,15 % con evidencia, igual que el declarado. C-01 a C-04 tienen su soporte firmado.
- **Lo que hay que atender:** C-05 (provisiones y causaciones, de Jorge Vela) venció el 2026-10-05 y no tiene evidencia.
- **Ruta crítica:** C-05 → C-07 → C-08 → C-09. C-07, C-08 y C-09 quedan bloqueadas hasta que se cierre C-05.
- **Checklist:** no está aprobado. Una persona tiene que aprobarlo antes de darlo por bueno.

**Lo que `compute` encontró y el reporte no muestra:** levantó 7 señales en total, y `close-status` muestra solo la de C-05. Las otras seis son:
- 1 factura electrónica sin registro contable.
- 1 registro contable sin factura electrónica.
- 2 cuentas bancarias sin conciliar.
- 1 requerimiento de auditoría sin respuesta.
- 1 partida conciliatoria antigua.

El detalle sale con `einvoice-check`, `bank-reconcile`, `account-reconcile` y `audit-pack`.

**Qué falta para que esto sea mejor:**
- Que alguien apruebe el checklist.
- Que alguien confirme lo que tomé de los datos: la entidad (sale del nombre de la carpeta) y las cuentas 4135, 5135, 5145, 5195, 2408, 1305 y 2205.

**Dónde quedó todo:**
- La configuración está en `.criterio/finanzas/76089001-4-minera-atacama-norte/config.json`.
- El reporte está en `estado-finanzas/76089001-4-minera-atacama-norte/cierre/2026-09/reporte-close-status.md`.
- La salida de esta corrida está en `estado-finanzas/76089001-4-minera-atacama-norte/corridas/salida-finance-setup.md`, y la corrida quedó registrada con 7 hallazgos.
- No medí los minutos hasta el primer resultado.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.