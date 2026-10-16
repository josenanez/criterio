# /criterio-product:product-charter REQ-4900

Dejé un borrador del acta de constitución para REQ-4900 (producto PRD-309, Microseguros). No creé la ficha del proyecto, porque nadie ha firmado el acta, y el acta tiene ocho vacíos abiertos.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no hubo que registrarlos de nuevo.

**Faltan cuatro cosas para poder redactarla**
- **Aceptación:** REQ-4900 está aceptado (acta del comité del 2026-10-12, desde el 2026-08-19), pero el acta no dice quién lo decidió.
- **Criterio de éxito:** el único criterio es «se verifica en producción», que no dice qué se mide ni con qué umbral.
- **Evidencia de demanda:** no hay ninguna. En el acta «Quién lo pidió» es «—» y el registro no tiene evidencia.
- **Autoridad:** ningún documento nombra quién decide. «Comité de producto» es el valor por defecto de la instalación y lo dejé marcado como supuesto.

Como nadie podía responder, seguí sin esos cuatro puntos y los dejé como vacíos del acta, sin rellenarlos.

**Otros vacíos del acta**
- **Necesidad del requerimiento:** el acta solo trae el código, no el problema que resuelve REQ-4900.
- **Patrocinador y gerente del proyecto:** no están nombrados en ningún documento.
- **Barrido normativo:** no lo hice, así que el acta no cita ninguna norma. Hay que hacerlo antes de firmar.
- **Cifra del caso de negocio:** el volumen mensual declarado es 276.481 y el medido es 194.582, una brecha de 29,6 %. El umbral configurado es 20 %.

El acta incluye también el supuesto «El proveedor cumple el tiempo pactado», que dice «verificado» sin citar con qué; lo marqué para pasarlo a riesgo del proyecto con doliente. En «No entra» no puse los otros 15 requerimientos, porque el acta se pidió solo para REQ-4900 y los documentos no dan razón de exclusión.

**Siguiente paso**
Cuando el acta se firme, el gerente del proyecto instala `criterio-project` y corre `/pm-setup`. Después publica su ficha con `/pm-publish`, y `/product-trace` podrá confirmar la traza contra ella.

La corrida quedó registrada como `2026-10-16-product-charter-1`: 16 requerimientos, 36 hallazgos, 33 segundos.

Archivos en `estado-producto/PRD-309/corridas/`:
- `salida-product-charter.md`