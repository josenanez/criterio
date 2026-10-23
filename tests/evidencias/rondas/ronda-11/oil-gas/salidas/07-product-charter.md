# /criterio-product:product-charter REQ-4200

Dejé el borrador del acta de REQ-4200, pero tiene vacíos grandes y quedó sin firmar. No creé la ficha del proyecto ni escribí estado declarado.

Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez), así que no registré nada nuevo. Nadie podía responder, así que seguí con las faltas marcadas como vacíos del acta y no las rellené.

**Lo que no sostiene el registro de REQ-4200:**
- **Aceptación:** figura «aceptado» desde 2026-05-27, pero el acta del comité no dice quién lo aceptó. La única decisión escrita es «Se mantiene el plan», que no nombra el requerimiento.
- **Criterio de éxito:** el único criterio es «se verifica en producción», sin métrica, umbral ni responsable. El cierre no se podrá juzgar contra eso.
- **Demanda:** una entrevista del 2026-05-20 a «Cliente entrevistado» («Lo necesito y hoy no lo tengo»), que no nombra el requerimiento.
- **Necesidad del requerimiento:** no está dicha en ningún documento. La propuesta del producto es un marcador («Propuesta principal»).
- **Gobierno:** no hay patrocinador, gerente propuesto ni autoridad del gerente. El acta solo nombra «Comité de producto», con Diana Molina como único asistente.
- **Supuesto:** «La comunidad respalda el proyecto» lleva 124 días sin verificar (el umbral es 30). Pasa al proyecto como riesgo sin doliente.
- **Normativa:** no evaluada, porque la definición no dice qué se ofrece.
- **Cifras:** el caso declara 115.628 de volumen mensual y el tablero mide 98.962. La brecha es 14,4 %, por debajo del umbral de 20 %, así que no es hallazgo.
- **Exclusiones:** ningún documento da razón para dejar fuera los otros 17 requerimientos. El apartado «No entra» solo muestra el estado que trae el comité y la razón la pone quien firma.

**Qué sigue:** firma quien decida por el Comité de producto (no está dicho quién es). Después, el gerente del proyecto instala `criterio-project` y corre `/pm-setup`. Cuando publique su ficha con `/pm-publish`, `/product-trace` podrá confirmar la traza.

La corrida quedó registrada como `2026-10-23-product-charter-1`, con 31 hallazgos sobre los 18 requerimientos del producto.

Archivos en `estado-producto/PRD-302/corridas/`:
- `salida-product-charter.md`