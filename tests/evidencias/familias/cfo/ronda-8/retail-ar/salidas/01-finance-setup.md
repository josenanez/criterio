# /criterio-finance:finance-setup finanzas/30714520780-almacenes-del-plata

## Listo — Almacenes del Plata

**Lo que miré:** 64 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`. Ninguno está fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.

**Configuración:** `.criterio/finanzas/30714520780-almacenes-del-plata/config.json`.
- Ventas: 4135.
- Compras: 5135, 5145 y 5195.
- IVA generado y descontable: 2408.
- Cuentas que se concilian: 1305 y 2205.
- Bancos: andino-6101 y pacifico-6102.

Esos prefijos salen de las facturas del periodo, no de los nombres de las cuentas. El estado queda en `estado-finanzas/30714520780-almacenes-del-plata`.

### Estado del cierre de 2026-09

- **Declarado:** Sofía León escribió el 2026-10-05 que el cierre de septiembre está cerrado.
- **Con evidencia:** el avance es de 42,31 %, contra 53,85 % declarado.
- **C-02, conciliar cada cuenta bancaria:** figura cumplida y no hay soporte que empiece por C-02 en `2026-09/40-soportes/`. Su responsable es Andrés Paz.
- **Ruta crítica:** C-02 → C-07 → C-08 → C-09. Las tres últimas están bloqueadas por la anterior.
- **Cerrado contra evidencia:** el correo dice «cerrado» y el motor tiene 5 señales abiertas que ese estado no explica.
- **Señales abiertas:** en total son 6. Este reporte detalla solo 2, las del checklist. Las otras cuatro son un banco sin conciliar, una factura registrada sin factura electrónica, una diferencia de monto en una factura y una partida antigua. Salen en bank-reconcile, einvoice-check y account-reconcile.
- **Checklist sin aprobar:** el avance se calcula igual, pero una persona tiene que aprobarlo antes de darlo por bueno.

### Supuestos que conviene confirmar

- **Preguntas:** nadie respondió, así que tomé las respuestas sugeridas de los documentos. Son 11 y quedaron en la ficha.
- **Marco contable:** puse «NIIF (FACPCE)». Ningún documento lo declara.
- **Aprobador:** puse «Contralor» por defecto.
- **Festivos:** no cargué ninguno.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt` porque la prueba no lo autorizó. No escribí nada dentro de los documentos.
- **Tiempo:** no medí los minutos hasta el primer resultado.

### Qué falta para mejorar

- Aprobar el checklist.
- El soporte de C-02, las conciliaciones bancarias.
- Confirmar el marco contable y quién aprueba.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

Todo está en `estado-finanzas/30714520780-almacenes-del-plata/`:
- `cierre/2026-09/reporte-close-status.md`
- `cierre/2026-09/ficha.json`
- `corridas/salida-finance-setup.md`

La corrida quedó registrada con el id `2026-10-06-finance-setup-1`.