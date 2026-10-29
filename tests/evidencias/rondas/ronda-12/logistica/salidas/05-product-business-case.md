# /criterio-product:product-business-case 

# Caso de negocio — Logística de frío (PRD-303) · borrador del 2026-10-28

Los términos v1.3 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-28, así que no registré nada nuevo. Con lo que hay en la carpeta no se puede evaluar este caso de negocio: no tiene costo, ni retorno cifrado, ni criterio de éxito.

**Cifras con fuente: 0 de 1.** La única cifra es `volumen_mensual` = 70.118, y el caso de negocio la cita a sí mismo como fuente. No hay estudio, contrato ni conteo detrás.

**Problema y para quién:** la definición dice que el segmento Farmacéuticas no tiene logística de frío. Lo único que lo sostiene es una entrevista de hace 12 meses (2025-10-13) a un cliente sin nombre: «Lo necesito y hoy no lo tengo.» La entrevista no dice que ese cliente sea farmacéutico.

**Qué se construye:** la definición dice solo «Propuesta principal», sin explicar qué es.
- **Aceptados:** hay 13 requerimientos aceptados.
  - 10 se apoyan solo en esa entrevista, que no nombra ninguno.
  - 3 no tienen evidencia: REQ-2028, REQ-4301 y REQ-4312.
- **Sin decidir:** REQ-4308 y REQ-4309 quedan fuera del caso.
- **Quién decidió:** en el acta no consta quién decidió ninguno de los aceptados.

**Las cifras**

| Cifra | Valor | Clase | Fuente |
|---|---|---|---|
| volumen_mensual | 70.118 | Declarada | El mismo caso, 2026-05-27 |
| Retorno esperado | «en 24 meses» | Supuesta | Sin valor ni base de cálculo |

- **Medida:** no hay ninguna cifra medida.
- **Declarada contra medida:** no hay serie con la cual contrastar el 70.118. No es una contradicción, es que nadie lo mide.

**Costos:** vacíos. Ningún documento trae el costo de construir, contratos, cotizaciones ni el costo del equipo. El costo de construir es el primer vacío, y sin él lo que hay es una propuesta.

**Supuestos:** el del precio del combustible aparece como verificado, pero el anexo del 2026-09-06 solo dice «se confirmó». No trae la medición del piloto ni cifra alguna. También son supuestos que nadie ha verificado: que todo el segmento carezca de logística de frío, el volumen de 70.118 y el retorno en 24 meses.

**Vacíos principales**
- Costo de construir y operar.
- Origen del 70.118.
- Cifra, base y supuestos del retorno.
- Qué se construye.
- Qué pasa si no se hace.
- Alternativas consideradas.
- Autoridad que decide.
- Medición del piloto.
- País y obligaciones sanitarias (revisión jurídica).
- Proyecto que lo construye.

**Cómo se sabrá si funcionó:** no está declarado, ni la métrica ni la fecha de corte.

**Otros productos:** no hay otros productos publicados a la vista, así que no pude hacer el cruce de `/product-overlap`.

**Siguientes pasos:**
- Pasar los supuestos al seguimiento con assumption-tracking.
- `/product-charter` todavía no corresponde: faltan criterio de éxito, autoridad y costo.

Este documento no calcula rentabilidad ni recomienda aprobar o rechazar.

La salida completa quedó en `/home/claude/r12/logistica/espacio/estado-producto/PRD-303/corridas/salida-product-business-case.md`. La corrida quedó registrada como `2026-10-28-product-business-case-1` y duró 32 segundos.