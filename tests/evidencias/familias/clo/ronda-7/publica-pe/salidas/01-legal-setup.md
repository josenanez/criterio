# /criterio-legal:legal-setup legal/20910000013-organismo-publico-del-rimac

Fidel quedó instalado sobre el Organismo Público del Rímac (RUC 20910000013, Perú, PEN). Procesó los 6 contratos, CTR-2101 a CTR-2106, y no quedó ninguna ficha con datos faltantes (`record_issues` vacío).

Dos cosas del resultado:
- **Garantías:** el motor marcó 2 señales `public_guarantee_below_law` (garantía pública menor que el mínimo de la ley). Las registré sin interpretarlas.
- **Obligaciones que vencen:** el reporte no marcó nada abierto.
  - **Ya vencida:** el reporte al oficial de cumplimiento de CTR-2101, del 2026-09-30, tiene su evidencia entregada.
  - **Próximas a vencer:** la terminación de CTR-2105 es el 2026-11-20 (en 45 días) y la de CTR-2103 el 2026-12-31 (en 86 días). Cada una trae su informe final y acta de liquidación, sin evidencia todavía.
  - **Decisión ya tomada:** el comité decidió renovar CTR-2105 el 2026-09-18.

Qué hice al configurar, tomando las respuestas de los documentos, ya que nadie respondía:
- **Avisos:** 60 días para vencimientos y 30 para preavisos de renovación, los del ejemplo del motor. El certificado de la contraparte puede tener hasta 30 días de antigüedad.
- **Entidad pública:** sí, porque la política de contratación dice que publica en SEACE. El umbral de garantía quedó vacío, porque no aplica a Perú.
- **Feriados:** dejé la lista vacía. El ejemplo traía un feriado de otro país y ningún documento da los de Perú.
- **Términos:** la versión 1.3 quedó aceptada por José Francisco Ñáñez (2026-10-06). Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Marca de la carpeta:** dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Lo tomé como la respuesta sugerida; es lo único que escribí dentro de ella.
- **Fuera de estructura:** `00-referencia/politica-contratacion.md` iría en `20-politicas/`. No lo moví.

La salida de esta sesión quedó guardada en `estado-legal/20910000013-organismo-publico-del-rimac/corridas/salida-legal-setup.md` y registrada como la corrida `2026-10-06-legal-setup-1`. La configuración está en `.criterio/legal/20910000013-organismo-publico-del-rimac/config.json`.