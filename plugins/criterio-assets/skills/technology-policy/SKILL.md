---
name: technology-policy
description: "La política de cambios y de niveles de servicio de la organización en la configuración de los dos agentes: los días para revisar un cambio de emergencia y para registrar el problema de un incidente mayor, el porcentaje de licencias sin uso que se tolera, la tolerancia sobre el presupuesto de la nube y lo que nunca se decide. Úsalo en el setup de cada agente y cuando la política cambie. Change and service level policy, deadlines, thresholds."
---
<!-- COPIA · la fuente es plugins/criterio-changes/skills/technology-policy/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# La política de tecnología en la configuración

**Los plazos, los niveles y los umbrales los fija la organización** en su política de cambios y de niveles de servicio, en `00-politica/`. Si la política no trae un valor, **no se inventa**: se le pregunta a la persona y se registra su respuesta con la fecha.

| Valor | Dónde va | Lo usa |
|---|---|---|
| Los días para revisar un cambio de emergencia después de implementarlo | `methodology.emergency_review_days` de la configuración, por ejemplo `5` | Fausto |
| Los días para registrar el problema de un incidente mayor, con su causa, después de resolverlo | `methodology.problem_days`, por ejemplo `10` | Fausto |
| El nivel acordado de cada servicio | el catálogo de servicios de `00-politica/` | Fausto |
| Qué cambio es normal, estándar o de emergencia, y quién lo aprobó | la exportación de cambios de `10-cambios/` y las actas del comité de cambios | Fausto |
| El porcentaje de licencias pagadas sin uso que se tolera | `methodology.unused_license_pct`, por ejemplo `15` | Domingo |
| El porcentaje que se tolera por encima del presupuesto de cada cuenta de la nube | `methodology.cloud_tolerance_pct`, por ejemplo `5` | Domingo |
| El nivel de servicio y el crédito de cada proveedor | sus contratos, en `40-proveedores/` | Domingo |

Un cambio estándar está preaprobado: no se le pide una aprobación por cambio. Un cambio de emergencia se aprueba por la vía de emergencia y se revisa después, en el plazo de la política.

## Lo que nunca se decide

Ningún agente aprueba un cambio, decide una arquitectura, califica un incidente, elige un proveedor, decide renovar o retirar un activo ni interpreta un contrato. Dicen qué falta y con qué cita; la decisión es del comité de cambios, del comité de arquitectura, del área de tecnología y de legal.

## Lo que viene de fuera

La gestión del servicio —los cambios, los incidentes y los niveles de servicio— es la de ISO/IEC 20000-1 (F-01); la gestión de los activos de TI, la de ISO/IEC 19770-1 (F-02). En una entidad vigilada de Colombia, lo que se pacta con un proveedor de nube —la disponibilidad, los tiempos de recuperación y el manejo de incidentes— es el de la Circular Externa 005 de 2019 de la Superintendencia Financiera (F-10). Se citan por su nombre, nunca por su texto. ITIL 4, COBIT 2019 y la norma de los demás países están por verificar, y no sostienen ninguna señal.
