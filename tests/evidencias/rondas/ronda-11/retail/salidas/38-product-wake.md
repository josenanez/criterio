# /criterio-product:product-wake 

Corrí la revisión de PRD-301 (Puntos de fidelización). Como no había un corte anterior, esta corrida es la línea base y no una lista de novedades. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré otra vez.

- **Sin decidir:** 4 requerimientos propuestos llevan más de 60 días sin decisión:
  - REQ-4104: 186 días.
  - REQ-4108: 117 días.
  - REQ-4105: 113 días, y además no tiene dueño.
  - REQ-4113: 75 días.
- **Supuesto sin verificar:** "Las tiendas soportan el volumen" lleva 119 días, con umbral de 30. Ya pasó el punto en que conviene tratarlo como riesgo registrado.
- **Evidencia vencida:** 14 requerimientos se apoyan solo en la ronda de entrevistas del 2025-08-29, que tiene 13 meses y no nombra ninguno de ellos.
- **Aceptados sin sustento:**
  - REQ-2030 y REQ-4115 no tienen evidencia de demanda.
  - REQ-4101, 4103, 4106, 4109 y 4110 no tienen criterio de aceptación.
  - REQ-4103 tampoco tiene dueño.
- **Trazas:** ninguno de los 12 requerimientos aceptados tiene proyecto, y ninguna de las 13 fichas nombra PRD-301.
- **Sin hallazgo:** el volumen mensual declarado (297.074) frente al medido (310.136) difiere 4,4 %, por debajo del umbral de 20 %.
- **Sin dato:** la definición no declara criterio de éxito. Tampoco sé quién es el dueño del supuesto ni quién asigna dueño a REQ-4105.

Dejé el corte en `estado-producto/PRD-301/snapshots/2026-10-23.json`. La corrida quedó registrada con el informe completo en `estado-producto/PRD-301/corridas/salida-product-wake.md`. Vuelvo el 2026-11-22.

No decidí, verifiqué ni escribí a nadie.