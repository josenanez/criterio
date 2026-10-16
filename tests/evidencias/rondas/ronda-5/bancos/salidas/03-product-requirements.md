# /criterio-product:product-requirements 

## Registro — Cuenta PyME (PRD-303) · al 2026-10-16

El registro tiene 17 requerimientos y 12 están decididos. El 83,3 % de lo decidido tiene evidencia y ningún requerimiento tiene un proyecto vinculado. Los términos ya estaban vigentes (v1.1, aceptados a nombre de José Francisco Ñáñez), así que no registré nada nuevo.

Corrí sin fichas de proyecto porque no existen. Por eso "sin proyecto" quiere decir que ningún documento lo vincula, no que se haya comprobado que nadie lo construye.

**Vacíos, en el orden de lectura**
1. **Se va a construir y nadie lo pidió:** REQ-4305 y REQ-4309 están aceptados sin ninguna evidencia. Los otros 10 aceptados se apoyan en la misma cita de una sola entrevista, del 2025-10-09.
2. **Decidido y nadie lo construye:** los 12 aceptados, todos decididos ayer, 2026-10-15. Todavía no es un atraso, pero conviene correr `/product-trace`.
3. **Sin doliente:** REQ-4306 (aceptado) y REQ-4311 (propuesto). Lo cierra Javier Hoyos asignando una persona.
4. **Sin criterio de aceptación:** ninguno de los decididos. El criterio de REQ-4305, "se verifica en producción", no es medible.
5. **Decidido sin quién decidió:** el acta del comité del 2026-10-15 existe y respalda la decisión. Pero en los 12 aceptados no consta quién decidió, y el acta cierra con "Se mantiene el plan".
6. **Lleva meses sin decidirse:** cinco propuestos pasan del umbral de 60 días. REQ-4308 lleva 213 días, REQ-4311 151, REQ-4300 y REQ-4307 138, y REQ-4315 124. La facultad de decidir es del Comité de producto. Propongo decidirlos, no cerrarlos por viejos.
7. **Evidencia vieja:** 14 requerimientos tienen como evidencia más nueva la del 2025-10-09, que ya cumplió los 12 meses del umbral.

**De la definición del producto**
- Un supuesto lleva 90 días sin verificar: "El segmento paga por esto".
- El criterio de éxito no está dicho.
- El caso de negocio declara un volumen mensual de 149 630 y no hay medición para contrastarlo.

**Por estado:** propuesto 5, aceptado 12; en construcción, entregado y descartado, 0.

No hay ningún requerimiento listo para `/product-charter` mientras los aceptados tengan evidencia vieja o ausente.

La corrida quedó registrada como `2026-10-16-product-requirements-1`: 36 hallazgos, 28 segundos. La salida completa está en `estado-producto/PRD-303/corridas/salida-product-requirements.md`.