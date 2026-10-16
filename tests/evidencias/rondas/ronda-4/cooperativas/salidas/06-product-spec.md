# /criterio-product:product-spec 

**Borrador, no una especificación cerrada. Lo cierra Natalia Ospina, gerente de producto, con el Comité de producto como autoridad. Este agente no aprueba.**

# Especificación — Tarjeta débito (PRD-303) · borrador del 2026-10-15

**Del registro no sale comportamiento que especificar.** Los 12 requerimientos aceptados no tienen la necesidad escrita (`need: not_found`) y su título es «Requerimiento REQ-xxxx». Ninguna sección de comportamiento se puede escribir sin inventarla, así que dejé los huecos a la vista.

Los términos ya estaban vigentes (José Francisco Ñáñez, 2026-10-15), así que no los registré de nuevo.

## Qué problema resuelve
La definición dice solo: «El segmento Microempresarios no tiene tarjeta débito». La propuesta es un marcador vacío («Propuesta principal»).

## Alcance
- **Entra**, solo por estar aceptados en el acta del 2026-10-12 y sin contenido: REQ-2030, 2038, 4300, 4301, 4302, 4304, 4305, 4306, 4307, 4308, 4314 y 4315.
- **No entra:**
  - Los 6 en `propuesto`: REQ-4303, 4309, 4310, 4311, 4312 y 4313.
  - Todo lo que la definición no menciona (canales, límites, emisión, costos). No está dicho en ninguna parte y no lo agrego.

## Comportamiento
Sin secciones, por lo dicho arriba.

## Criterios de aceptación
El único criterio en todo el registro es «se verifica en producción». No pasa la prueba: dos personas distintas no llegarían a la misma respuesta.

| Criterio | Requerimiento | Cómo se verifica | ¿Se puede medir hoy? |
|---|---|---|---|
| «se verifica en producción» | REQ-2038, 4300, 4301, 4304, 4305, 4306, 4307, 4308, 4314, 4315 | No dice qué se observa ni con qué umbral | No hay nada que medir |
| **Sin criterio** | REQ-2030, REQ-4302 | — | — |

## Supuestos sobre los que está escrita
| Supuesto | Verificado | Quién lo verificaría |
|---|---|---|
| «El reglamento vigente lo permite» (declarado el 2026-09-02) | No. Lleva 43 días sin verificar, sobre el umbral de 30. Tampoco es falsable tal como está escrito: no dice qué reglamento ni de qué país | Natalia Ospina, dueña de la definición. La confirmación sería de la revisión jurídica, pero ningún documento nombra a un jurídico |

## Vacíos
| Qué falta decidir | Consecuencia de no decidirlo | Quién lo cierra |
|---|---|---|
| Necesidad de los 12 aceptados | No hay qué construir ni qué verificar | Cada doliente; Natalia Ospina en REQ-4305, 4306 y 4314 |
| Criterio verificable para los 12 | La discusión de «¿quedó bien?» ocurre después de construir | Cada doliente con Natalia Ospina |
| REQ-2030 y REQ-4302 sin ningún criterio | Aceptados sin saber cuándo están hechos | Paula Céspedes; Beatriz Cuéllar |
| REQ-4305, 4306 y 4314 sin doliente | Nadie responde por ellos | Natalia Ospina |
| Evidencia de demanda: una sola entrevista (2025-09-19, «Lo necesito y hoy no lo tengo»), sin vínculo confirmado a ningún requerimiento y con 12,9 meses, sobre el umbral de 12. REQ-4301 no tiene ninguna | Se aceptan requerimientos sin demanda sustentada | Natalia Ospina |
| Decisión sin autor: el acta solo dice «Se mantiene el plan». Las fechas «desde» son las que trae el propio acta | La aceptación no se rastrea a una decisión documentada | Comité de producto |
| Proyecto que ejecuta cada requerimiento: ninguno | Aceptados sin quien los construya | Comité de producto |
| Casos borde (sin conexión, operación duplicada, cancelación a medio camino, tarjeta perdida) | Comportamiento no definido en ningún documento | Natalia Ospina con quien construya |
| Otros equipos: la definición no nombra ninguno, así que las dependencias son desconocidas, no inexistentes | Acuerdos pendientes sin descubrir | Natalia Ospina |
| Obligaciones normativas | Revisión jurídica tardía | Natalia Ospina debe designar a quién |

**Barrido normativo.** Nombra, no dictamina, y es insumo para la revisión jurídica. El país no está dicho en los documentos que leí, y no tengo la norma a la vista, así que no cito ninguna.

| Qué toca | Estado |
|---|---|
| Emisión y uso de un medio de pago | no tengo la norma a la vista |
| Microempresarios como consumidores financieros (información previa, reclamos, cobros) | no tengo la norma a la vista |
| Datos personales de titulares (inferido; la definición no lo dice) | no tengo la norma a la vista |
| «El reglamento vigente lo permite» | sin resolver |

## Requerimientos aceptados que esta especificación no cubre
Ninguno queda cubierto con comportamiento; los 12 van en esta lista.

| REQ | Por qué no |
|---|---|
| REQ-2030 | Sin necesidad, sin criterio de aceptación, sin proyecto |
| REQ-4302 | Sin necesidad ni criterio |
| REQ-4301 | Sin necesidad; criterio no verificable; sin evidencia |
| REQ-4305, 4306, 4314 | Sin necesidad; sin doliente |
| REQ-2038, 4300, 4304, 4307, 4308, 4315 | Sin necesidad; criterio no verificable |

**Pie:** sale del registro `estado-producto/PRD-303/requirements/` (18 requerimientos: 12 aceptados, 6 propuestos), fechado el 2026-10-15 sobre el acta del 2026-10-12. Cubre 0 de 12 aceptados con comportamiento. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal

**No ofrezco `/product-charter`:** los vacíos siguen abiertos y ningún requerimiento tiene criterio de éxito verificable.

La corrida quedó registrada (`2026-10-15-product-spec-1`, 40 s, 18 requerimientos, 42 hallazgos). El texto completo está en `estado-producto/PRD-303/corridas/salida-product-spec.md`.