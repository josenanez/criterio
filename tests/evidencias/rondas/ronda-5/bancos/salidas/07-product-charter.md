# /criterio-product:product-charter REQ-4301

Escribí el borrador del acta de constitución para REQ-4301 (producto PRD-303, Cuenta PyME). **No creé la ficha del proyecto**, porque nadie firmó el acta.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16). No registré nada nuevo. Donde el comando ofrece seguir sin un elemento faltante, tomé la respuesta sugerida: seguí y dejé el faltante marcado como vacío, sin rellenarlo.

Cuatro condiciones del requerimiento quedan flojas o ausentes:
- **Aceptación sin autor:** el requerimiento figura como «aceptado» desde 2026-06-28. Pero el acta del comité solo cierra con «Se mantiene el plan» y no dice quién decidió.
- **Criterio de aceptación sin forma de verificarse:** el único criterio es «se verifica en producción». No dice qué se mide, con qué umbral ni quién lo verifica.
- **Evidencia débil y vencida:** hay una sola cita anónima, «Lo necesito y hoy no lo tengo» (2025-10-09). No nombra la cuenta pyme y tiene 12 meses y 7 días contra un umbral de 12.
- **Autoridad del gerente sin declarar:** ningún documento dice qué puede decidir el gerente.

**Otros vacíos y contradicciones del acta**
- **Problema contradictorio:** la definición dice «El segmento Personas no tiene cuenta pyme», que se contradice sola.
- **Sin criterio de éxito ni gobierno:** la definición no trae criterio de éxito, y ningún documento nombra patrocinador ni gerente del proyecto. No propuse a nadie.
- **Supuesto sin verificar:** «El segmento paga por esto» lleva 90 días sin verificar contra un umbral de 30. Pasa al proyecto como riesgo, con doliente sin asignar.
- **Normativa sin barrido:** una cuenta para pymes toca depósitos, datos personales y consumidor financiero, pero no corrí el barrido normativo ni cité ninguna norma.
- **Fuera del alcance:** los demás requerimientos quedan fuera por no haberse pedido. Los propuestos tampoco están aceptados.

**Qué sigue:** alguien con autoridad firma el acta y cierra los vacíos. Entonces se crea la ficha con `portafolio.py init`. El gerente del proyecto, una vez nombrado, instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada como `2026-10-16-product-charter-1`. No se escribió estado declarado.

Archivos están en `estado-producto/PRD-303/corridas/`:
- salida-product-charter.md