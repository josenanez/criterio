# /criterio-risk-appetite:appetite-setup riesgos/20607773331-seguros-del-sur-sintetica

Severo ya está instalado sobre Seguros del Sur Sintética (RUC 20607773331). La configuración quedó escrita y validada, los términos aceptados y la carpeta marcada.

**Lo que quedó escrito**
- **Configuración:** `.criterio/apetito/20607773331/config.json`. Las respuestas salen de los documentos:
  - Periodo 2026-10.
  - Las áreas reportan su exposición dentro de los 10 días después del cierre, según la declaración de apetito.
  - La junta revisa la declaración cada 12 meses, según la declaración de apetito.
  - Para Casandra, los eventos se registran en 30 días y la ventana de eventos repetidos es de 12 meses, según la política de riesgo operacional.
  - Lo que encuentro se publica en Rostrum.
- **Términos v1.6:** aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.2.0-2026-11-25.md` y en `.pdf`.
- **Marca:** dejé `_CRITERIO_RIESGOS.txt` en `riesgos/20607773331-seguros-del-sur-sintetica`.
- **Ficha 2026-10:**
  - La declaración, que la junta revisó el 2025-08-28.
  - Tres excesos que aprobó el comité: L-04 (hasta el 2027-01-31), L-06 (hasta el 2027-02-28) y L-07 (hasta el 2027-03-31).
  - Sobre L-03, el acta dice que el comité solo «toma nota» del plan de acción. Por eso no lo registré como aprobación.

**Lo que hay que atender (reporte `limit-check`)**
1. **L-12, cartera vencida de vivienda:** la exposición es 4.6 % y el límite máximo es 4. No tiene plan de acción ni aprobación del exceso. El dueño es la Vicepresidencia de crédito.
2. **L-01, cartera vencida de consumo:** la exposición es 6.4 % y el límite máximo es 6. No tiene plan de acción ni aprobación del exceso. El dueño es la Vicepresidencia de crédito.
3. **L-02:** Tesorería reportó el 2026-11-18, 8 días después del plazo, que vencía el 2026-11-10.
4. **L-42:** Tesorería reportó el 2026-11-16, 6 días después del mismo plazo.

El motor encontró otras 7 señales que no salen en este reporte:
- 2 riesgos que no tienen límite.
- 2 límites sin dueño.
- 2 límites con la revisión vencida.
- La declaración de apetito vencida.

Las muestran `/criterio-risk-appetite:coverage-check` y `/criterio-risk-appetite:framework-check`.

El reporte completo está en `estado-riesgos/20607773331-seguros-del-sur-sintetica/apetito/2026-10/reporte-limit-check.md`. Lo que se mostró en esta sesión quedó en `estado-riesgos/20607773331-seguros-del-sur-sintetica/corridas/salida-appetite-setup.md`, y la corrida quedó registrada como `2026-11-25-appetite-setup-1`.

**Cuándo vuelvo:** sin reloj. La tarea diaria solo se programa con un sí explícito, y en esta prueba nadie lo dio. Para correrlo a mano: `/criterio-risk-appetite:appetite-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.