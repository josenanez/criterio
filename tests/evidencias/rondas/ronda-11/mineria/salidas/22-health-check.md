# /criterio-portfolio:health-check PRY-200

# Diagnóstico · PRY-200 Mantenimiento predictivo de camiones · 2026-10-23

**Términos:** ya estaban vigentes (v0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23). No hubo que registrarlos de nuevo.

**Leí:** 9 documentos de 2025-09-04 a 2026-10-21: 4 PDF, 2 DOCX, 2 MD y 1 CSV. También busqué el proyecto en el resto del portafolio por código, nombre, proveedor y contrato. Solo apareció el proveedor, en PRY-209 (CT-611), sin vínculo documentado con PRY-200. No quedó nada sin leer.

## Dictamen
**Sostenido:** 9 · **Sin sustento:** 9 · **Contradicho:** 3. Es un conteo mío sobre 21 afirmaciones, y las listas están en el archivo de salida.

- **Qué se puede afirmar:**
  - Quién gobierna el proyecto: patrocinador Andrés Lozano, gerente Carlos Peña, Comité de Operaciones.
  - El presupuesto aprobado.
  - Las actas de recibo de Montaje e instalación y de Pruebas en operación.
  - El acta de recibo de la Bolsa de horas.
  - Dos entregables del contrato siguen pendientes con fecha vencida.
- **Qué no se puede afirmar:**
  - Que esté en verde.
  - Que el avance sea 77 %.
  - Las cifras de comprometido, ejecutado y proyección. Todas salen del informe de avance, que es una declaración.

## Lo principal
- **Gobierno:** el acta no declara la autoridad del gerente. El alcance son «Componente 1, 2, 3» sin nombre. El contrato se firmó antes de aprobarse el acta.
- **Plan:** hay una sola línea base y ninguna replanificación. El cierre planeado (2026-04-06) ya pasó. El script da desviación 0 solo porque nadie movió las fechas.
- **Hitos cerrados sin documento** (días vencidos, calculados por el script):
  - Ingeniería básica: 356.
  - Ingeniería de detalle: 317.
  - Licencia y permisos: 278.
- **Proveedor (CT-326):**
  - Licenciamiento lleva 352 días vencido y Soporte del primer trimestre 223.
  - Calibración de sensores figura como recibida, pero no hay acta.
  - La factura FV-1326 por 551.792.512 cubre dos entregables y solo hay un acta de recibo. El contrato exige acta para facturar.
- **Dinero (COP):** aprobado 2.400.000.000, comprometido 1.356.662.777 (56,5 %), ejecutado 446.036.134 (18,6 %), proyección 2.479.870.475 (3,3 % sobre lo aprobado), disponible real 1.043.337.223.
  - El ejecutado declarado es menor que la sola factura radicada. Puede ser que aún no se haya pagado, y ningún documento lo aclara.
- **Contradicho:**
  - El estado «Verde» contra el contrato, que tiene dos entregables vencidos.
  - El avance de 77 % contra el cronograma, que marca 5 de 5 hitos cerrados.
  - Las fechas vigentes del cronograma contra las fechas de las actas de recibo. Las pruebas se recibieron antes que el montaje, al revés del plan.
- **Dicho y no registrado:**
  - Un hallazgo de auditoría de seguridad sin dueño ni fecha.
  - Un «riesgo» del proveedor que ya es una incidencia.
  - Dos compromisos de la minuta del 19 de octubre:
    - Liliana Torres, «punto 4», para el 2026-10-23, que vence hoy.
    - Beatriz Cuéllar, «punto 33», sin fecha.
- **Silencio:** la carpeta no tiene ningún documento entre 2026-01-07 y 2026-09-02, así que el silencio es del proyecto entero y no solo de quien reporta.

Como pide el comando, no recomiendo detener, continuar ni reestructurar.

**Siguiente paso posible:** preparar el punto de comité con lo que falta, o llevarle al gerente las contradicciones como preguntas, una por una.

## Registro de la corrida
- Salida completa, con todas las tablas y el pie de rigor: `/tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/mineria/espacio/estado/corridas/salida-health-check.md`
- Corrida `2026-10-23-health-check-1` registrada para el caso PRY-200.
- **Reservas sobre la medición:**
  - El script midió 120 segundos y lo registró como medido.
  - Los documentos no quedaron contados (`documentos: null`).
  - El campo `proyectos` quedó en 13 y las señales abiertas en 80, porque cuentan todo el portafolio. Solo 9 señales son de PRY-200.

*Pie de rigor: este es un borrador de trabajo, no una decisión ni una asesoría. Se basa solo en los 9 documentos leídos y no sabe lo que se habló fuera de ellos. Verificarlo es responsabilidad de quien lo use. Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.8.0*