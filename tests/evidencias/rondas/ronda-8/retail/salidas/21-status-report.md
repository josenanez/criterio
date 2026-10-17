# /criterio-portfolio:status-report PRY-211

# PRY-211 Pronóstico de demanda — estado al 2026-10-17

*Sale de la ficha `PRY-211.json`, actualizada el 2026-10-17, y de las cifras de `compute` (as_of 2026-10-17). Los términos están vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que volver a registrarlos.*

**Declara la gerente (Beatriz Cuéllar):** verde · 43% · al 2026-09-30 (17 días de antigüedad, dentro del umbral de 30).
**Sustento documental:** contradicho (alerta `declared_vs_evidence`).
**Lo que el semáforo no explica:**
- **Plazo:** el cierre queda 75 días (17.6%) después de la línea base original.
- **Avance:** declara 43% y el plan sostiene entre 80% y 100%, una brecha de 37.0 puntos.
- **Hitos:** 3 hitos declarados cumplidos no tienen acta de recibo.
- **Compromisos:** 1 compromiso vencido.
- **Proveedor:** 2 entregables vencidos y pendientes, y una factura mayor que lo aceptado.

**Último documento:** 2026-10-09 (8 días). **Última reunión:** 2026-10-09, comité semanal. No está en silencio (umbral 15 días).

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2026-12-26 | 2027-03-11 | +75 días (17.6%) contra la original; 0 contra la vigente |
| Presupuesto | No consta una línea base de costo original | 3.300.000.000 COP | No calculable |

Replanificaciones: 1, la v2 del 2026-09-30. Su motivo no consta.

Presupuesto en COP, según el informe del 2026-09-30:

| Concepto | Monto | Porcentaje |
|---|---|---|
| Aprobado | 3.300.000.000 | — |
| Comprometido | 1.100.978.231 | 33.4% |
| Ejecutado | 1.403.708.177 | 42.5% |
| Proyección | 3.055.066.406 | 7.4% por debajo del aprobado |
| Disponible real | 2.199.021.769 | — |

El ejecutado es mayor que el comprometido. El script no lo marca como alerta, pero Finanzas debería explicarlo.

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |
|---|---|---|---|---|
| Diseño de la experiencia aprobado | 2026-01-20 | 2026-01-20 | declarado cumplido | **Ninguna** (270 días desde el vencimiento) |
| Ambiente de pruebas certificado | 2026-04-15 | 2026-04-15 | cumplido | Acta de recibo del 2026-10-09 |
| Integración con el ERP | 2026-07-09 | 2026-07-09 | declarado cumplido | **Ninguna** (100 días) |
| Piloto en tiendas | 2026-10-02 | 2026-10-02 | declarado cumplido | **Ninguna** (15 días) |
| Despliegue en la cadena | 2026-12-26 | 2027-03-11 | pendiente | — |

### Dónde no coincide
- **Verde frente a seis señales abiertas.** El informe del 2026-09-30 declara verde y ninguna de las seis señales de arriba la explica.
- **Avance 43% frente a 4 de 5 hitos «cumplidos».** Las dos cifras no pueden ser ciertas a la vez. O el avance está subdeclarado, o hay hitos marcados como cumplidos sin estarlo.
- **Piloto «cumplido» frente a una incidencia abierta.** El mismo informe dice que la validación con dos tiendas se extendió una semana.
- **CC-01 aprobado, pero la línea base vigente es anterior.** CC-01 es del 2026-10-04 (+75 días, +150.000.000 COP, ampliación de alcance). El cronograma v2 que ya incluye esos 75 días es del 2026-09-30.
  - La aprobó «el comité», sin nombre ni fecha de sesión.
  - El script lo marca como `change_without_baseline`.
- **Los 150.000.000 COP de CC-01** no se ven en los 3.300.000.000 aprobados. No consta si ya están incluidos.
- **Contrato CT-520 (Retail Andino Consultores S.A.S.).**
  - Se facturaron 345.838.436 COP y se aceptaron 246.790.805, es decir, 99.047.631 COP facturados sin aceptación.
  - Solo 1 de 4 entregables tiene acta de recibo.

### Abierto
**Riesgos e incidencias sin movimiento:**
- **Riesgo:** «El proveedor no ha confirmado la fecha de la última entrega». No consta probabilidad, impacto, responsable ni último movimiento. Ya se materializó en parte, porque hay 2 entregables vencidos.
- **Incidencia:** la validación de dos tiendas se extendió una semana. Lleva 17 días abierta desde el 2026-09-30 y no tiene responsable.
- **Incidencia:** **hallazgo de seguridad en los medios de pago.** Lleva 17 días abierta desde el 2026-09-30 y no tiene responsable. Es la más delicada.

**Compromisos vencidos:** Sandra Gil debía «Entregar el punto 11» el 2026-09-29 (18 días de atraso). Ya estaba vencido cuando se anotó en el comité del 2026-10-09, y no tiene reprogramaciones.

**Entregables del proveedor vencidos:**
- Licenciamiento de la plataforma: vencía el 2026-01-28 (262 días), pendiente.
- Bolsa de horas de desarrollo: vencía el 2026-05-02 (168 días), pendiente.
- Soporte del primer trimestre vence el 2026-11-05.

**Dependencias sin confirmar:** ninguna declarada, porque el acta dice «Ninguna declarada». El riesgo del proveedor sí describe una dependencia externa que nadie registró como tal.

### Sin dato
- La línea base de costo original, necesaria para calcular la desviación del presupuesto.
- El motivo de la replanificación v2.
- Quién aprobó CC-01 y en qué sesión.
- Las actas de recibo de 3 hitos (diseño, integración con el ERP, piloto) y de 3 entregables de CT-520.
- Producto asociado, autoridad y fase. El acta dice «No aplica» para el producto.
- Los responsables de las dos incidencias y del riesgo.
- Nueve campos de identidad y plan vienen del acta del 2025-10-17 y llevan 12 meses, así que hay que confirmarlos.
- De las 18 fuentes de la ficha, ninguna está marcada como evidencia, 2 como declaración y 16 sin marcar.

### Después
Hay desviación de tiempo por encima del umbral (17.6% frente a 10%) y una incidencia de seguridad que probablemente excede la autoridad de la gerente. Puedo preparar el punto de comité para el 2026-10-22 con `/steering-pack`. Como el atraso viene de un cambio sin línea base formalizada, también puedo preparar la solicitud de cambio con `/change-control`.

---
*Criterio Portfolio v0.3.13 · ficha PRY-211 del 2026-10-17 · declaración del gerente del 2026-09-30 · campos inciertos: ver «Sin dato» · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13*

La corrida quedó registrada como `2026-10-17-status-report-1`. Duró 32 segundos y cubrió el caso PRY-211. El informe completo está en `estado/corridas/salida-status-report.md`.