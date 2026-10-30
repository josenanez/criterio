# /criterio-legal:legal-setup legal/08010003991010-instituto-publico-de-occidente

Fidel quedó instalado sobre Instituto Público de Occidente. Procesé los 6 contratos, sin errores en las fichas, y registré la corrida.

**Lo que se hizo**
- **Carpeta:** usé la ruta que diste, así que no corrí la búsqueda. No escribí la marca `_CRITERIO_LEGAL.txt`, porque nadie podía responder esa pregunta.
- **Inventario:** 64 archivos, con 6 contratos y 3 periodos de cumplimiento. Están el registro y la matriz de atribuciones. `00-referencia/politica-contratacion.md` está fuera de lugar: iría en `20-politicas/`. No moví nada.
- **Configuración:** quedó en `.criterio/legal/08010003991010/config.json` y el motor la validó sin problemas. Los datos son:
  - Honduras, HNL, RTN 08010003991010.
  - Entidad pública, porque lo dice la política de contratación.
  - Avisos de 60 y 30 días, y certificado de 30 días, tomados de `config.example.json`.
  - `guarantee_threshold` en vacío: Honduras no usa umbral.
- **Términos:** versión 1.3, aceptada por José Francisco Ñáñez el 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/`, en Markdown y PDF.
- **Fichas:** escribí una por contrato en `estado-legal/08010003991010-instituto-publico-de-occidente/contratos/`, cada dato con su cita.

**Lo que muestra el calendario al 2026-10-06**
- Vencen CTR-4305 el 2026-11-20 (en 45 días) y CTR-4303 el 2026-12-31 (en 86 días). Ambos tienen su informe final y acta de liquidación sin evidencia.
- La acta del 2026-09-18 registra la decisión de renovar CTR-4305.
- CTR-4301 tenía su reporte de cumplimiento para el 2026-09-30, y el archivo de evidencia dice que se entregó ese día.
- `compute` marcó 2 señales de garantía pública por debajo del mínimo de la ley, pero no dice cuáles contratos. No corrí el comando que las detalla.

**Una duda que quedó**
La cláusula 5 de CTR-4306 pide «el de agosto» con fecha 2026-07-06. Lo registré tal cual, sin interpretarlo.

El reporte está en `estado-legal/08010003991010-instituto-publico-de-occidente/contratos/reporte-obligations-calendar.md`. Lo que te mostré quedó en `.../corridas/salida-legal-setup.md`.