# /criterio-portfolio:portfolio-scan 

## Barrido — 2026-10-28

Leí 66 de los 92 documentos de `documentos/proyectos` y creé 10 fichas nuevas, de PRY-199 a PRY-207 y PRY-209. Los otros 26 documentos son de PRY-208, PRY-210 y PRY-211. No cambiaron, así que no los abrí y sus fichas quedan como estaban.

Los términos ya estaban vigentes (versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no los registré otra vez. Con `workers: 1` leí los proyectos uno tras otro, sin subagentes. La corrida tardó 205 segundos y las 10 fichas quedaron selladas.

**Documentos:** 92 en la carpeta · 66 leídos · 26 sin cambio · 0 ilegibles
**Proyectos:** 13 con ficha · 10 nuevos · 0 sin carpeta propia

### Lo que hay que mirar
- **Hitos cerrados sin acta de recibo:** son 17.
  - PRY-200, PRY-201 y PRY-202 tienen 4 cada uno.
  - PRY-207 tiene 2.
  - PRY-204, PRY-205 y PRY-209 tienen 1 cada uno.
- **Proyectos pasados de su fecha de cierre con avance menor a 100%:**
  - PRY-200: cierre 2025-12-19, 59%, amarillo.
  - PRY-207: cierre 2026-01-03, 35%, verde.
  - PRY-202: cierre 2026-03-18, 52%, verde.
  - PRY-201: cierre 2026-09-02, 51%, verde.
- **Facturas frente a lo recibido:**
  - PRY-209, CT-604: la factura es por 1.164.831.714 COP y no hay ningún acta de recibo.
  - PRY-200, CT-478: la factura cubre dos entregables y hay acta de uno solo.
  - PRY-206, CT-381: la factura es por 267.686.057 COP. El único entregable con acta vale 187.360.587 COP.
- **Entregables con fecha vencida y sin acta:**
  - PRY-201, CT-801: 3.
  - PRY-200, CT-235: 2.
  - PRY-200, CT-478: 1.
  - PRY-209, CT-604: 2.
- **Cambios de alcance:**
  - PRY-206 CC-01 sigue pendiente del comité, pero el cronograma v2 ya mueve el lanzamiento a 2027-12-16. Dejé la fecha de cierre como `ambiguous`.
  - PRY-205 y PRY-209 CC-01 dicen estar autorizados por el comité, pero las minutas del 2026-10-21 y 2026-10-25 no los mencionan.
- **Compromisos vencidos sin evidencia de cumplimiento:**
  - PRY-200: Carlos Peña, «punto 26», para 2026-10-06.
  - PRY-204: Jorge Medina, «punto 8», para 2026-10-20.
  - PRY-206: Ricardo Salas, «punto 35», para 2026-10-25.
  - En los tres casos la fecha es anterior a la minuta que los registra.
- **Ejecutado mayor que comprometido, según el mismo informe:** PRY-203 y PRY-206.
- **PRY-199:** el nombre habla de mobiliario de una sala de espera, pero el contrato y el hito son de red. El informe lo declara verde y dice que la prueba de velocidad en campo no alcanzó el valor pactado.

El script que calcula las señales también marcó cuatro cosas más:
- **Verde sin sustento:** PRY-201, PRY-202 y PRY-207 declaran verde y el cálculo lo contradice con la evidencia.
- **Atraso:** PRY-205, PRY-206 y PRY-209 tienen atraso en tiempo.
- **Sin señales:** PRY-199 y PRY-203 no tienen ninguna.
- **Señales de otras fichas:** PRY-210 y PRY-211 tienen las suyas, que vienen de sus fichas anteriores.

### Nuevos
Todas las fichas quedaron sin `authority` y sin `phase`, porque ningún documento los trae.

| Proyecto | Documentos | Otros campos sin dato |
|---|---|---|
| PRY-199 | 6 | factura de CT-199 |
| PRY-200 | 11 | — |
| PRY-201 | 6 | factura de CT-801 |
| PRY-202 | 4 | producto («No aplica»), contratos, minutas |
| PRY-203 | 2 | producto («No aplica»), cronograma, contratos, minutas |
| PRY-204 | 4 | contratos |
| PRY-205 | 7 | producto («No aplica»), contratos |
| PRY-206 | 10 | producto («No aplica») |
| PRY-207 | 6 | producto («No aplica»), contratos |
| PRY-209 | 10 | producto («No aplica») |

### Actualizados
Ninguno.

### No pude leer
Nada. El inventario marcó como ilegibles 4 cronogramas .xml (PRY-200, 201, 204 y 206). `texto.py` los convirtió sin problema y los leí por su texto. La cita va al .xml original.

### Movidos desde entrada/
Nada. No existe carpeta `entrada/` en la documentación.

### Pendientes de clasificar
Ninguno.

Lo que te mostré arriba está en `estado/corridas/salida-portfolio-scan.md`. No le añadí las señales extra del script ni la duración. La corrida quedó registrada como `2026-10-28-portfolio-scan-1` y la instantánea en `estado/snapshots/2026-10-28.json`.

Hay más de un proyecto con ficha, así que puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`.

---
criterio-portfolio 0.12.1 · fichas tocadas: 10 · `not_found`: `identity.authority` e `identity.phase` en todas; producto (6), cronograma (PRY-203), contratos (PRY-202, 203, 204, 205, 207), minutas (PRY-202, 203) y factura (PRY-199, 201) · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal