# /criterio-portfolio:portfolio-scan 

El barrido terminó y dejó 10 fichas nuevas. Nada quedó sin leer.

Términos: estaban vigentes (v1.2, familia 0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23). No hubo que registrar nada.

- **Documentos:** de 86, leí 59 y los otros 27 no habían cambiado. Todos eran legibles. El plan marcó como ilegible el cronograma `.xml` de PRY-209, pero `texto.py` lo convirtió y lo leí.
- **Proyectos:** de 13, escribí y sellé las fichas de PRY-199, 200, 202, 203, 205, 206, 207, 208, 209 y 211. PRY-201, 204 y 210 quedaron como estaban.
- **Corrida:** `2026-10-23-portfolio-scan-1`, 296 segundos medidos, 58 hallazgos.
- **Movidos desde `entrada/`:** nada, porque esa carpeta no existe.

Lo más relevante de la corrida:
- **Hitos cerrados sin acta:** el cronograma los declara cerrados y no hay acta que lo pruebe. Los dejé como se declararon, con la evidencia vacía. El código contó 23 en todo el portafolio, incluidos PRY-201 y 204.
- **PRY-209:**
  - **Cronograma v2:** mueve el despliegue +95 días, y la solicitud de cambio CC-01 sigue pendiente de comité.
  - **CT-140:** se facturó 596.779.430 COP sin ningún acta de recibo.
  - **CT-431:** sus actas y su factura cuadran.
- **PRY-205:** el cronograma v2 es del 2026-10-01 y CC-01, que lo justifica, es del 2026-10-10.
- **PRY-202:** de 26 compromisos, 6 están vencidos. Dos se han reprogramado 5 y 6 veces, y tres personas dijeron «ya lo entregué» sin acta.
  - La ficha del gerente (`ficha-pm.json`) va aparte en `pm_record`. Mi lectura de las minutas coincide con la suya.
- **PRY-206, 208 y 211:** pasaron su fecha de cierre sin replanificar el cierre en ningún documento.

Dos cosas que debes saber:
- El texto de `salida-portfolio-scan.md` cuenta 18 hitos cerrados sin acta en estos 10 proyectos. El código cuenta 17, porque en PRY-209 reconoce 4 de los 5. El texto ya quedó registrado en la corrida y no lo reescribí.
- `authority` y `phase` no aparecen en ningún documento de los 10 proyectos y van `not_found`. `product` va `not_found` en 202, 203, 206, 209 y 211 porque el acta dice «No aplica». PRY-203, 206 y 208 no tienen cronograma, así que no tienen hitos.

El informe consolidado de portafolio está disponible si quieres que lo genere.

Los archivos están en `estado/` (dentro de `espacio`):
- `records/` (las fichas)
- `corridas/salida-portfolio-scan.md`
- `snapshots/2026-10-23.json`