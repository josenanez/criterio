# /criterio-portfolio:project-closure PRY-200

**PRY-200 no se puede cerrar por cumplimiento.** El acta sí declaró criterio de éxito ("Mantenimiento predictivo de camiones en producción y medido"). Pero ningún documento muestra el sistema en producción ni una medición, así que el cumplimiento es "no se puede determinar". Cerrarlo ahora sería una decisión, no un cumplimiento.

Una nota sobre la ejecución: los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré de nuevo. Las preguntas sin respuesta las tomé con el valor sugerido.

- **Hitos:** 3 de los 5 figuran cerrados en el cronograma sin ninguna evidencia: ingeniería básica, ingeniería de detalle y licencia y permisos. Los otros dos tienen acta de recibo, pero muy tarde. Pruebas en operación se recibió el 2026-10-11 (comprometido: 2026-04-06). Montaje e instalación se recibió el 2026-10-21 (comprometido: 2026-02-26), es decir, después de Pruebas y del informe del 2026-10-18.
- **Estado declarado:** el informe del 2026-10-18 dice verde y 77 % de avance, mientras el plan da 100 % por hitos. La diferencia es de 23.0 puntos. El cálculo marca 3 señales abiertas contra ese verde.
- **Alcance:** el acta lista "Componente 1, 2 y 3" sin describirlos y la exclusión es "lo que otro proyecto cubre". No se puede contrastar lo entregado contra lo comprometido. No hay solicitudes de cambio registradas.
- **Números:** hay 0 replanificaciones y la fecha de cierre sigue en 2026-04-06. La desviación real en días no está calculada, porque el script solo compara fechas planeadas. No hay costo final. Al corte del 2026-10-18 la proyección es de 2.479.870.475 COP, 3.3 % sobre los 2.400.000.000 aprobados. El ejecutado es de 446.036.134 COP, menos que lo facturado por el proveedor (551.792.512 COP).
- **Proveedor (contrato CT-326):**
  - Dos entregables siguen pendientes y vencidos: Licenciamiento del software (352 días de atraso) y Soporte del primer trimestre (223 días).
  - La Calibración de sensores figura aceptada, pero no tiene acta de recibo. El contrato exige un acta firmada para facturar.
- **Riesgos y compromisos abiertos sin responsable:** quedan un riesgo y una incidencia (un hallazgo de auditoría de seguridad), sin responsable ni fecha. Hay además 2 compromisos del comité: "punto 4", que vence hoy, y "punto 33", sin fecha. Por eso no se puede dar por cerrado.
- **Lecciones:** dejé 4, todas ancladas a un hecho documentado. No incluí lecciones sobre las causas del atraso, porque ningún documento las explica.
- **Archivo:** no recomiendo mover la carpeta a `archivo/` todavía. Quedaría fuera del barrido diario con todo esto abierto.
- **Autoridad de cierre:** la ficha no encuentra quién puede declarar el cierre (`identity.authority`).

La corrida quedó registrada como `2026-10-23-project-closure-1`.

Archivos en `/tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/mineria/espacio/estado/corridas/`:
- `salida-project-closure.md`