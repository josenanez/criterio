# /criterio-legal:legal-setup legal/52934187-almacenes-del-altiplano

Dejé a Fidel instalado sobre Almacenes del Altiplano: procesé los 6 contratos de `contratos/` y el motor calculó 5 señales. En el calendario sale una: el CTR-3403 (arrendamiento de la sede principal) vence el 2026-11-25, en 50 días, y no tiene decisión de renovar ni de terminar. Esa decisión es de una persona.

Las otras 4 señales están en el motor, pero este comando no las detalla:
- **Facultad de firma:** una firma sin facultad.
- **Pagos:** un pago después de la terminación.
- **Garantía:** una garantía que vence antes de lo exigido.
- **Registro:** una diferencia entre el registro y los documentos.

Las muestran `/authority-check`, `/contract-execution` y `/contract-register`.

**Preguntas:** nadie respondió, así que tomé las respuestas sugeridas por los documentos y las dejé escritas en la salida de la corrida.
- Los datos de la entidad salieron de los contratos: NIT 52934187, Guatemala, moneda GTQ.
- Usé la matriz de atribuciones que ya estaba en la carpeta.
- Dejé los avisos en 60 días para vencimientos y 30 para preavisos, y el certificado en 30 días máximo. Son los valores de `config.example.json`.
- La entidad no es pública.
- Dejé la lista de festivos vacía, porque no conozco los de Guatemala y no quise inventarlos.
- No dejé el archivo `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Nadie autorizó escribir ahí y lo único que escribo en los documentos es esa marca.

**Términos:** mostré la versión 1.3 y la registré a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/`.

**Faltantes:**
- **CTR-3409:** Publicidad Exterior S.A.S. figura en el registro, pero no tiene carpeta ni documento. No le hice ficha.
- **Pólizas:** las pólizas no traen monto asegurado ni fecha de entrega, y los dejé vacíos.

**Dónde quedó:**
- Configuración: `.criterio/legal/52934187/config.json`
- Fichas y reporte: `estado-legal/52934187-almacenes-del-altiplano/contratos/`
- Salida de la corrida: `estado-legal/52934187-almacenes-del-altiplano/corridas/salida-legal-setup.md`