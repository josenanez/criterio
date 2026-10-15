# /criterio-product:product-charter REQ-4600

Dejé el borrador del acta de REQ-4600 del producto PRD-306 (Almacén de repuestos), sin firma y sin ficha de proyecto. El acta tiene muchos vacíos de gobierno. Mi recomendación es no firmarla hasta cerrar al menos cuatro: quién aceptó el requerimiento, el patrocinador, la autoridad y un criterio de éxito verificable.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar.

REQ-4600 pasa dos de las cuatro verificaciones previas solo en parte. En cada una tomé la respuesta sugerida, que es seguir y marcar el vacío sin rellenarlo.
- **Aceptación:** consta como aceptado desde 2026-04-21, pero ningún documento dice quién lo aceptó. El acta del comité solo dice «Se mantiene el plan».
- **Criterio de aceptación:** el único es «se verifica en producción». No dice qué se mide, con qué umbral ni quién lo verifica.
- **Evidencia de demanda:** es una sola entrevista de hace 12 meses, de un cliente sin nombre. El requerimiento tampoco declara la necesidad.
- **Autoridad:** ningún documento dice quién decide. «Comité de producto» es solo una propuesta por defecto.

Otros puntos que quedan en el borrador:
- **Alcance:** entra solo REQ-4600. Los otros 13 requerimientos quedan fuera, cada uno con su razón.
- **Supuesto del proveedor:** «El proveedor cumple el tiempo pactado» lleva 205 días sin verificar y nadie lo tiene a cargo. Pasa al proyecto como riesgo sin doliente.
- **Cifra del caso de negocio:** declara 249.273 de volumen mensual y el tablero mide 153.324, un 38,5 % menos.
- **Faltan** patrocinador, presupuesto, hitos, propuesta de valor y proyecto que lo construya. El «retorno esperado en 24 meses» no trae cifra ni cálculo.
- **Normativa:** no identifiqué nada, pero el país no está declarado, así que queda pendiente la revisión jurídica.

No corrí `portafolio.py init`, así que no existe ficha, y no escribí estado declarado. Cuando haya acta firmada, el gerente del proyecto instala `criterio-project` y corre `/pm-setup`.

Registré la corrida (id `2026-10-15-product-charter-1`, 40 s, 31 señales abiertas sobre 14 requerimientos).

Archivos en `estado-producto/PRD-306/corridas/`:
- `salida-product-charter.md`