# /criterio-product:product-wake 

## Microcrédito (PRD-305) · 2026-10-18

Esta fue la primera revisión mensual y no había corte anterior. Lo que sigue es la línea base, no «lo que cruzó un umbral». Desde la próxima corrida solo se reportará lo que cambie.

Los términos 1.1 ya estaban aceptados hoy por José Francisco Ñáñez, así que no los registré otra vez. No había documentos nuevos ni cambiados (4 de 4 sin cambios), por lo que solo recalculé.

El registro tiene 16 requerimientos: 12 aceptados y 4 propuestos. 9 de 16 tienen evidencia (75 %) y ninguno tiene traza a un proyecto.

**Para el comité**
| Qué | REQ | Cuánto lleva | Quién |
|---|---|---|---|
| Propuesto sin decidir (umbral 60 d) | REQ-4510 | 104 días | Sin doliente |
| Propuesto sin decidir | REQ-4504 | 84 días, sin evidencia | Sin doliente |
| Propuesto sin decidir | REQ-4502 | 74 días | Sin doliente |
| Propuesto sin decidir | REQ-4503 | 64 días | Elena Duarte |
| Supuesto sin verificar (umbral 30 d) | «El proveedor cumple el tiempo pactado» | 146 días | Ricardo Salas |

- **Falta quién decide.** En tres de los cuatro propuestos no hay doliente, y ese es el dato que falta para saber a quién preguntarle.
- **Supuesto del proveedor.** Hace falta verificarlo con el proveedor. Pasado el umbral, conviene registrarlo como riesgo.
- **Aceptados que nadie construye.** Los 12 aceptados están sin traza. Los más antiguos son REQ-4513 (desde 2026-03-28), REQ-4511 (2026-05-06) y REQ-4506 (2026-05-31).
- **Trazas.** Revisé las 13 fichas de `estado/records` y ninguna nombra a PRD-305 ni a sus REQ. No hay trazas que confirmar ni que se hayan perdido.
- **Aceptados con huecos.**
  - Sin evidencia: REQ-4507, REQ-4511 y REQ-4514.
  - Sin criterio de aceptación: REQ-4500 y REQ-4511.
  - Sin doliente: REQ-4505 y REQ-4506.
- **Evidencia que vence.** Todo el sustento es del 2025-12-30 y se vence a los 12 meses, el 2026-12-30.

**Lo que no sé**
- El éxito del producto no está definido en ningún documento.
- No hay medición del volumen mensual declarado (166.254), así que no puedo decir si hay brecha.
- El inventario marcó como «fuente no encontrada» 7 citas de identidad y definición. Parece un problema de ruta relativa, no de contenido, pero conviene revisarlo antes del comité.

Dejé constancia con `ran` y el corte del 2026-10-18 en `snapshots/`. La salida completa y el registro de la corrida están en `estado-producto/PRD-305/corridas/` (`salida-product-wake.md` y `2026-10-18-product-wake-1`).

**Vuelvo el 2026-11-17.**