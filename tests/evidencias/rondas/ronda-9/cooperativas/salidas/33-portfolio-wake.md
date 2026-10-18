# /criterio-portfolio:portfolio-wake 

## 2026-10-17

El barrido y la confirmación de hoy están hechos y la corrida quedó registrada. Los 67 documentos no cambiaron. No corrí `/portfolio-scan` porque no había nada que releer. No había peticiones en el servidor. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no tuve que registrarlos.

Es el primer barrido, así que no hay corrida anterior con la que comparar. Lo que sigue es lo que hoy está por encima del umbral, no lo que cambió desde ayer.

**Por encima del umbral**
- **PRY-202 Core cooperativo:** el costo proyectado es 1.498 M contra 1.200 M aprobados (+24,8 %). Declara verde. Natalia Ospina tiene un compromiso vencido hace 7 días.
- **PRY-210 Corresponsales rurales:** el costo proyectado es 11.282 M contra 9.500 M (+18,8 %). Declara verde.
- **PRY-204 Tarjeta débito:** lleva 80 días de atraso contra la línea base original (26,7 %). Declara verde.
- **PRY-201 Apertura de ahorro en línea:** el proveedor Integración Financiera del Sur tiene facturados 117 M por encima de lo aceptado.
- **PRY-203 Aportes sociales en línea:** lleva 24 días en silencio (el umbral es 15). Declara verde.
- **PRY-208 Motor de crédito:** declara 31 % de avance, pero marca 5 de 5 hitos como cumplidos sin evidencia. Un entregable del proveedor lleva 133 días vencido.
- **PRY-209 Convenios de libranza:** tiene 5 compromisos vencidos y 4 sin fecha. Tiene 3 reprogramados, uno de ellos 6 veces (Jorge Medina, «Cerrar la prueba 2»).
- **Hitos sin evidencia:** hay hitos marcados como cumplidos sin evidencia de recibo en PRY-201, 202, 203, 204, 208, 210 y 211.

**Citas rotas en PRY-209**
`index` reporta 15 citas que no resuelven, todas dentro de `pm_record` (la ficha del gerente, `ficha-pm.json`). Los archivos citados sí existen. Las rutas están escritas relativas a la carpeta del proyecto y el índice las busca desde la raíz de documentos. No lo corregí, porque esa ficha no es mía. Queda como hallazgo.

**Preguntas de confirmación**
Nadie puede responder en esta corrida. Quedan preguntadas hoy y no se repiten:
1. PRY-202: ¿hay un cambio aprobado que explique la proyección de 1.498 M?
2. PRY-210: ¿tiene aprobación la proyección de 11.282 M?
3. PRY-204: ¿se movió la línea base con aprobación?
4. PRY-201: ¿existe acta de recibo que cubra los 117 M facturados de más?
5. PRY-203: ¿sigue en marcha? Su último documento es del 2026-09-23.

La corrida tardó 45 segundos y quedó en `estado/corridas/2026-10-17-portfolio-wake-1`. El texto completo está en `estado/corridas/salida-portfolio-wake.md`.

**Vuelvo el 2026-10-18.**