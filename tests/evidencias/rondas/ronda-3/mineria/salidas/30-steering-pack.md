# /criterio-portfolio:steering-pack 

Preparé el material de comité para la sesión del 2026-10-19 y dejé la corrida registrada (`2026-10-15-steering-pack-1`, 119 s). El paquete trae 6 decisiones y 7 escalamientos, y 10 de los 13 proyectos tienen hallazgos (63 alertas en total).

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15 (versión 0.3.9), así que no los registré otra vez. Las cifras salen del cálculo de `portafolio.py compute` al corte 2026-10-15 y de las 13 fichas.

Las 6 decisiones:
1. **Autoridad:** quién decide cada cambio. Ninguno de los 13 proyectos la declara y dependen de cinco comités distintos, así que es el primer punto.
2. **CC-01 de PRY-208 y PRY-211:** están pendientes, pero la línea base de cada una ya se movió sin autorización (60 y 54 días). Recomiendo diferirlas hasta que cada gerente sustente el motivo.
3. **CC-01 de PRY-202 y PRY-206:** figuran «aprobadas por el comité» sin acta. Recomiendo pedir el documento primero y ratificar después.
4. **Fecha de cierre de PRY-203 y PRY-204:** el cronograma y el acta dicen fechas distintas en cada una. Recomiendo que los gerentes aclaren con quién se acordó cada fecha.
5. **Mover 30 días la salida a producción de PRY-204:** la solicitud no dice quién la pide, por qué ni cuánto cuesta un mes más. Recomiendo devolverla.
6. **Pagos a Montajes Industriales Ltda.:** el proveedor tiene entregables vencidos en PRY-203 y PRY-204. En PRY-204 hay facturado sin entrega aceptada: 133.892.409 COP (CT-594) y 120.184.897 COP (CT-331). Recomiendo exigir un plan de entrega con fecha antes de la próxima factura.

Los escalamientos sin decisión son PRY-201, PRY-202, PRY-203, PRY-204, PRY-209, seis proyectos en verde contradichos por su propia evidencia, y los riesgos sin doliente repetidos entre proyectos.

Lo que el paquete dice que no sabe:
- **Comité anterior:** no hay registro de uno, así que la tabla de decisiones previas queda vacía.
- **Fecha de la sesión:** la corrida anterior de PRY-203 citaba el 2026-10-29. La configuración dice 2026-10-19 y usé esa.
- **Costos de las solicitudes de cambio:** no sé si los de PRY-208, PRY-211, PRY-202 y PRY-206 ya están en la proyección.
- **Contratos del proveedor:** no sé qué cláusulas tienen los de Montajes Industriales Ltda.

Archivos en `/home/claude/banco/ronda-3/mineria/espacio/estado/corridas/`:
- `salida-steering-pack.md`
- `2026-10-15-steering-pack-1.md`