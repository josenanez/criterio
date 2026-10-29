# /criterio-product:product-charter REQ-4300

# Acta de constitución — REQ-4300 · borrador del 2026-10-28
**Producto:** PRD-303 Logística de frío · **Requerimientos:** REQ-4300

**Términos:** ya estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no los registré otra vez.

**REQ-4300 no pasa la verificación del paso 1.** Le faltan criterios de aceptación y la autoridad del gerente no está declarada. Como nadie podía responder, tomé la respuesta sugerida: seguir y marcar cada falta como vacío, sin rellenarla. Con estos vacíos no recomiendo firmar el acta tal cual.

## Qué problema resuelve
«El segmento Farmacéuticas no tiene logística de frío.» (`documentos/productos/PRD-303/00-definicion/2026-05-27-definicion-producto.md`, 2026-05-27). Qué parte de ese problema cubre REQ-4300 no consta: el registro no tiene su necesidad y el título es genérico.

## Criterio de éxito
**Vacío.** REQ-4300 no tiene criterios de aceptación: la columna del acta del comité dice «—» (`30-decisiones/2026-10-15-comite-producto.docx`). La definición del producto tampoco declara criterio de éxito. Lo cierra Ricardo Salas; no lo redacté yo.

## Alcance
### Entra
| REQ | Título | Evidencia que lo sostiene |
|---|---|---|
| REQ-4300 | Requerimiento REQ-4300 (título genérico) | Cliente entrevistado, 2025-10-13: «Lo necesito y hoy no lo tengo.» (`10-descubrimiento/2025-10-13-entrevistas.md`). La entrevista no nombra este requerimiento y tiene 12 meses. |

### No entra
| REQ | Título | Por qué no |
|---|---|---|
| REQ-2028, 4301–4313 | Los otros 14 requerimientos del registro | Esta acta es solo de REQ-4300. Si van en el mismo proyecto, se agregan antes de firmar. Ningún documento da la razón de excluir cada uno. |

## Gobierno
- **Patrocinador:** no consta.
- **Gerente propuesto:** no consta. Ricardo Salas es gerente de producto y doliente de REQ-4300. No propongo que sea también gerente del proyecto con esta evidencia.
- **Comité:** Comité de producto (configuración y acta del 2026-10-15). El único asistente registrado es Ricardo Salas.
- **Autoridad del gerente del proyecto:** vacío. La definición no declara la autoridad del producto.
- **Quién decidió aceptar REQ-4300:** no consta. El acta fecha la aceptación en 2026-05-17, cinco meses antes del propio documento, y su único acuerdo es «Se mantiene el plan».

## Supuestos que se llevan al proyecto
| Supuesto | Verificado | Se convierte en riesgo de |
|---|---|---|
| El precio del combustible se sostiene | El anexo del 2026-09-06 dice «se confirmó», pero no trae la medición del piloto. | Doliente por designar (gerente del proyecto). |
| Volumen mensual de 70.118 | No. La única fuente es el propio caso de negocio y no hay serie medida. | Doliente por designar. |

El «retorno esperado en 24 meses» del caso de negocio no trae cifra.

## Restricciones normativas sin resolver
| Qué toca | Obligación | Norma | Estado |
|---|---|---|---|
| Nada declarado | Ningún documento de PRD-303 menciona obligaciones | — | No barrido. Es logística de frío para farmacéuticas, así que es razonable que existan. No las inventé ni las descarté. |

## Vacíos de este acta
| Qué falta | Consecuencia de firmar sin eso | Quién lo cierra |
|---|---|---|
| Criterios de aceptación de REQ-4300 | El cierre no se podrá juzgar | Ricardo Salas |
| Criterio de éxito del producto | Nada contra qué medir el proyecto | Ricardo Salas |
| Autoridad del gerente | No sabrá qué decidir y qué escalar | Comité de producto |
| Quién decidió aceptar, y cuándo | La decisión no es trazable | Comité de producto |
| Evidencia de demanda específica | Se construye sobre una frase genérica de hace 12 meses | Ricardo Salas |
| Patrocinador y gerente del proyecto | No hay a quién entregar la ficha | Quien pueda asignarlos |
| Barrido normativo | Obligaciones sin descubrir hasta que cuesten | Quien corra el barrido |
| Título y necesidad de REQ-4300 | No está claro qué se construye | Ricardo Salas |

---
**Esto es un borrador.** Lo firma una persona con facultad para hacerlo; no consta quién, y no la nombro. **La ficha del proyecto no se creó:** se crea solo después de la firma, y el estado declarado no lo escribo nunca.

**Después:** con la firma y un gerente de proyecto, esa persona instala `criterio-project` y corre `/pm-setup`. Cuando publique con `/pm-publish`, `/product-trace` podrá confirmar la traza.

**Corrida registrada** como `2026-10-28-product-charter-1`: 40 segundos, 15 requerimientos y 35 hallazgos abiertos. Los de REQ-4300 son evidencia vieja, sin proyecto y sin criterio de aceptación. El texto completo quedó en `estado-producto/PRD-303/corridas/salida-product-charter.md`.