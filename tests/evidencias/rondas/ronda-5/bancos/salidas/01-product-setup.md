# /criterio-product:product-setup documentos/productos/PRD-303

Alba quedó instalada para PRD-303 · Cuenta PyME. La corrida válida es `2026-10-16-product-setup-2`, con la salida guardada.

**Lo que hice**
- **Configuración:** `.criterio/producto/PRD-303/config.json`, verificada. Quien decide quedó como «Comité de producto». Ese nombre es lo que sugiere el acta, y ningún documento nombra a una persona que decida.
- **Términos:** aceptados a nombre de José Francisco Ñáñez, 2026-10-16, versión 0.3.11 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.11-2026-10-16.md` y `.pdf`.
- **Registro:** levanté `producto.json` y 17 requerimientos en `estado-producto/PRD-303/`, solo con lo que está escrito, y sellé la lectura.

**Lo que no sostiene tu definición**
- **Criterio de éxito:** no existe en ningún documento.
- **Proyectos:** ninguno de los 12 requerimientos aceptados tiene proyecto que lo construya (0,0 %).
- **Métrica:** no hay serie medida para `volumen_mensual` (149.630), así que nada contrasta la cifra del caso de negocio.
- **Evidencia de demanda:** es una sola entrevista del 2025-10-09, de hace 12 meses, y ya cuenta como vencida. Los 10 requerimientos aceptados con evidencia dependen de ella.
- **Aceptados sin evidencia:** REQ-4305 y REQ-4309.
- **Sin doliente:** REQ-4306 y REQ-4311.
- **Supuesto «El segmento paga por esto»:** sin verificar hace 90 días.
- **Propuestos sin decidir:** 5, entre 124 y 213 días.
- **Contradicción:** el problema habla de una cuenta pyme, pero el segmento es «Personas».

**Lo que pasó fuera de lo previsto**
- **Registro de la corrida:** `sellar` exige abrir antes una corrida con `corrida-inicio`, aunque el comando dice que aquí no va. Lo hice y reescribí `producto.json` dentro de la corrida para poder sellar.
- **Primer registro inválido:** la carpeta `corridas/` no existía y la primera corrida (`...-setup-1`) quedó registrada sin salida. Repetí el registro con la salida guardada.

Ofrezco `/product-discovery` sobre las entrevistas como siguiente paso.