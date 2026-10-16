# /criterio-product:product-wake 

## Microseguros (PRD-306) · 2026-10-16

**Términos:** ya estaban vigentes (versión 1.1, familia 0.3.12). José Francisco Ñáñez los aceptó el 2026-10-16, así que no hubo que pedirlos de nuevo.

**Qué tocaba:** la revisión (`review`), que nunca se había corrido. No había corte anterior, así que esta corrida fija la línea base y no reporta señales nuevas. Desde la próxima corrida solo se reportará lo que cruce un umbral después de hoy.

### Revisión del registro contra la carpeta
- **Documentos:** los 4 están sin cambios desde la última lectura, sin renombrados ni borrados. El más reciente es el acta del comité del 2026-10-14. No ofrezco `/product-discovery` ni `/product-definition` porque no hay documentos nuevos.
- **Fuentes que no resuelven:** el índice marca 8 campos con `source_missing`. Los archivos citados existen en disco, así que parece un desajuste de ruta y no documentos perdidos. No lo resolví; alguien debe confirmarlo.

### Las trazas
- **Ninguna se puede dar por confirmada.** Usé `estado/records` como carpeta de fichas, que tiene 13 fichas de proyecto, de PRY-199 a PRY-211.
- **Ninguna ficha nombra PRD-306 ni "Microseguros".** Ninguno de los 12 requerimientos aceptados tiene proyecto (0 %).

### Estado de base (16 requerimientos: 12 aceptados, 4 propuestos)

**Necesitan decisión del comité**

| Qué | REQ | Cuánto lleva | Qué se necesita | Quién |
|---|---|---|---|---|
| Sin decidir | REQ-4609 | 197 días | Decisión; además no tiene evidencia ni criterio de aceptación | Diana Molina |
| Sin decidir | REQ-4601 | 154 días | Decisión | Laura Vélez |
| Sin decidir | REQ-4607 | 143 días | Decisión | Laura Vélez |
| Sin decidir | REQ-4611 | 111 días | Decisión | Jorge Medina |
| Supuesto sin verificar: «El proveedor cumple el tiempo pactado» | — | 110 días (umbral 30) | Evidencia de que el proveedor cumple, o registrarlo como riesgo | — |

El acta del comité no dice quién tiene la facultad de decidir. "Comité de producto" quedó como autoridad propuesta por defecto, y ese es el dato que falta para los cuatro requerimientos.

**Aceptados sin sustento**
- **Sin evidencia de demanda:** REQ-4603, REQ-4614, REQ-4615.
- **Sin criterio de aceptación:** REQ-4606, REQ-4613, REQ-4614, REQ-4615.
- **Sin doliente:** REQ-4602.
- **Sin proyecto que los construya:** los 12 aceptados.

**Evidencia vencida:** afecta a 12 requerimientos. Toda la evidencia es una sola entrevista del 2025-10-05, que cumple 12 meses. Además, la entrevista no nombra los requerimientos; es solo la más cercana. La definición se queda sin sustento de demanda actual.

**Definición:** el criterio de éxito no está en ningún documento. El volumen mensual declarado en el caso de negocio (204.945) no tiene medición contra la cual contrastarlo.

**Vuelvo el 2026-11-15.**

La salida quedó guardada en `estado-producto/PRD-306/corridas/salida-product-wake.md`. La corrida quedó registrada como `2026-10-16-product-wake-1`, con 37 hallazgos y 36 segundos medidos.