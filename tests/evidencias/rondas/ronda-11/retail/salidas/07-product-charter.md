# /criterio-product:product-charter REQ-4100

He escrito el borrador del acta de constitución de REQ-4100 (PRD-301, Puntos de fidelización). No creé la ficha del proyecto, porque una persona tiene que firmar el acta antes y nadie lo ha hecho. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré de nuevo.

REQ-4100 no cumple limpio las cuatro condiciones. Seguí adelante marcando cada falta como vacío del acta, sin rellenarla:
- **Aceptación:** consta como aceptado desde el 2026-08-06, pero ningún documento dice quién lo aceptó.
- **Criterio de éxito:** el único criterio es «se verifica en producción». Eso dice dónde se verifica, no qué se mide, y la definición del producto tampoco trae criterio de éxito.
- **Demanda:** la única cita es «Lo necesito y hoy no lo tengo.», de la entrevista del 2025-08-29. No nombra este requerimiento y tiene unos 14 meses, por encima del umbral de 12.
- **Autoridad:** ningún documento la declara. «Comité de producto» es una propuesta de la instalación que nadie confirmó.

El acta también deja sin dato el patrocinador y el gerente propuesto. Lleva un supuesto sin verificar, «Las tiendas soportan el volumen», que queda sin doliente hasta que haya gerente del proyecto. Marca el barrido normativo como pendiente, porque un programa de puntos para jóvenes toca datos personales. No cité ninguna norma, porque ningún documento la menciona.

En «No entra» quedaron REQ-4101 a REQ-4115 y REQ-2030, porque este acta cubre solo REQ-4100. Los motivos por requerimiento los dejé resumidos en una sola fila.

La corrida quedó registrada con 17 requerimientos revisados y 40 hallazgos. Dejé además una nota sobre el vacío de demanda.

Lo que sigue: alguien con autoridad sobre el Comité de producto firma el acta y se nombra al gerente del proyecto. Ese gerente instala `criterio-project` y corre `/pm-setup`. La ficha se crea entonces con `portafolio.py init`, dejando vacío el estado declarado.

El borrador completo está en `/tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/retail/espacio/estado-producto/PRD-301/corridas/salida-product-charter.md`.