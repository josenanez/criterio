# /criterio-legal:legal-setup legal/CCM120615R59-comercial-control-centro

La instalación de Fidel sobre Comercial Control Centro (RFC CCM120615R59) quedó hecha: configuración válida, términos aceptados, 6 fichas calculadas y la corrida registrada.

Nadie contestó preguntas, así que tomé las respuestas de los documentos. Eso incluye dejar `_CRITERIO_LEGAL.txt` en la carpeta de documentos.

**Qué vence.** El calendario al 2026-10-06 no marca nada abierto:
- **CTR-1501:** el reporte al oficial de cumplimiento (OBL-3) venció el 2026-09-30 y tiene evidencia entregada ese mismo día.
- **CTR-1505:** termina el 2026-11-20, a 45 días. El comité decidió renovarlo el 2026-09-18, pero el contrato dice que no se prorroga automáticamente.
- **CTR-1503:** termina el 2026-12-31, a 86 días. Tampoco se prorroga automáticamente.

**Qué falta.** Las otras dos preguntas, quién firmó sin facultad y qué se pagó por fuera de lo pactado, no se contestaron aquí. Eso es de `/authority-check` y `/contract-execution`.

**Cosas por revisar:**
- **Matriz de atribuciones:** cubre a Gabriela Ríos, Arturo Medina y Lorena Castillo. Arturo Medina firmó CTR-1502 (suministro), CTR-1504 y CTR-1505, y en la matriz tiene tope de 1.500.000 para todos los tipos.
- **CTR-1502:** el contrato dice 600.000 MXN y el otrosí suma 150.000, lo que cuadra con los 750.000 del registro.
- **CTR-1506:** el contrato describe el informe mensual como «el de agosto», pero la fecha límite es 2026-07-06. La registré como está escrita.
- **Días festivos:** el ejemplo de configuración traía un festivo de Colombia (2026-10-12), así que dejé la lista vacía. Si quieres los de México, díganlos.

**Un descuido mío.** Generé las fichas con un script en `<temporal>`, no en el scratchpad. No toca los documentos ni el estado.

**Archivos** (todo bajo `<espacio>/`):
- `.criterio/legal/CCM120615R59/config.json` (configuración, con la aceptación de José Francisco Ñáñez, términos 1.2)
- `.criterio/terminos/aceptacion-criterio-legal-0.11.0-2026-10-06.md` (comprobante; hay también un PDF)
- `estado-legal/CCM120615R59-comercial-control-centro/contratos/` (las fichas y el reporte del calendario)
- `estado-legal/CCM120615R59-comercial-control-centro/corridas/salida-legal-setup.md` (lo que te mostré)