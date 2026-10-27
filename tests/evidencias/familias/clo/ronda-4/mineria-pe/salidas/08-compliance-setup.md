# /criterio-compliance:compliance-setup legal/20730000015-minera-puna-alta

Constanza quedó instalada sobre Minera Puna Alta (RUC 20730000015), y el primer estado del periodo 2026-09 ya está calculado. El reporte muestra 2 señales de las 5 que levantó el motor.

Revisé las 10 obligaciones de la matriz contra su evidencia. El avance con evidencia es de 68.18 %, ponderado por criticidad. El informe del periodo declara «con observaciones».

- **Instalación:** el inventario encontró 65 documentos, todos en su lugar. La carpeta ya tenía la marca `_CRITERIO_LEGAL.txt`, así que no la volví a marcar. No moví ni cambié ningún documento.
- **Configuración:** la escribí en `.criterio/cumplimiento/20730000015/config.json` y el motor la validó sin problemas. Dejé el canal de denuncias a 15 días y la evaluación de normas a 30, los mismos valores de la configuración de Fidel.
- **Feriados:** quedó sin lista de feriados, porque no tengo una comprobada para Perú. Si alguno cae en un plazo, el cálculo no lo descuenta.
- **Términos:** José Francisco Ñáñez los aceptó con fecha 2026-10-06, como indicaste, y mostré el texto corto tal cual. El comprobante en Markdown y PDF está en `.criterio/terminos/`.
- **Preguntas:** respondí 6, todas desde los documentos y sin esperar a nadie. Quedaron en la ficha del periodo, junto con el estado declarado y la norma nueva N-2026-07 del boletín de agosto.

**Lo que hay que atender (las 2 señales del reporte):**
- **OB-10, Declaración mensual de origen de fondos** (responsable: Carmen Rojas): la matriz la da por cumplida, pero no hay ninguna evidencia que empiece por OB-10.
- **OB-11, Monitoreo mensual de listas restrictivas** (responsable: Óscar Mendoza): la última evidencia es de 2026-07 y el ciclo anterior no tiene.

Las otras 3 señales no salen en este reporte: un caso del canal de denuncias vencido, una norma sin evaluar y una norma que aplica y ninguna obligación cita. Las muestran `reports-cases` y `regulatory-watch`.

Los archivos están en `estado-legal/20730000015-minera-puna-alta/`:
- cumplimiento/2026-09/reporte-compliance-status.md
- corridas/salida-compliance-setup.md

La corrida quedó registrada como `2026-10-06-compliance-setup-1`.