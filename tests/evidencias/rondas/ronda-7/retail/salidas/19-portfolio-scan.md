# /criterio-portfolio:portfolio-scan 

El barrido terminó y quedó registrado. Leí 50 de los 80 documentos y escribí y sellé 10 fichas nuevas (PRY-199, 200, 201, 203, 205, 206, 207, 208, 209 y 210). Los otros 30 documentos eran de PRY-202, PRY-204 y PRY-211, que no habían cambiado desde el setup.

Los términos ya estaban vigentes (v0.3.13), aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré otra vez. No hay carpeta `entrada/`, y todos los archivos fueron legibles.

El cálculo da 61 señales en los 13 proyectos. Cinco proyectos declaran verde y los documentos los contradicen: PRY-204 y PRY-211 del setup, y PRY-205, 206 y 207 de este barrido. Lo que conviene mirar:
- **PRY-205 y PRY-209:** sus solicitudes de cambio CC-01 (+75 y +55 días) siguen pendientes de comité, pero el cronograma v2 ya recoge esos días.
- **PRY-206:** da por cerrados en 2025 tres hitos que no tienen acta de recibo, y tiene el cierre original en 2025-12-22 aunque sigue en ejecución.
- **PRY-203:** el hito de integración con el ERP está vencido hace 13 días. El compromiso del punto 27 se anotó el 2026-10-14 con fecha 2026-10-04, así que nació vencido.
- **Cronogramas que no existen:** los informes de PRY-203, 206 y 208 dicen «se reprogramó el despliegue», pero ninguno tiene un cronograma v2.
- **PRY-200 y PRY-210:** no tienen cronograma, así que su avance declarado no se puede contrastar.
- **Facultad del gerente:** no aparece en ninguna de las 13 fichas.

Dos advertencias sobre el registro de la corrida:
- **Relectura:** `corrida` la muestra como 80 sin cambio y 0 releídos. Lo calculó después de sellar, así que no refleja que se leyeron 50. La cifra real es la de arriba y también está en la nota de la corrida.
- **Citas de PRY-211:** 171 citas del `ficha-pm.json` de PRY-211 no resuelven desde la raíz de documentación. No toqué esa ficha porque es del gerente.

La corrida midió 222 segundos. Lo que le mostré aquí está entero en `estado/corridas/salida-portfolio-scan.md`, y las fichas en `estado/records/`. Con las 13 fichas ya puedo preparar el informe consolidado con `/criterio-portfolio:portfolio-report`.

Criterio portfolio 0.3.13 · fichas tocadas: 10 · campos en `not_found`: `identity.authority` ×10, `identity.phase` ×10, `identity.product` ×4 (PRY-203, 206, 209, 210), facturación de CT-199 ×1 · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13