# /criterio-product:product-setup documentos/productos/PRD-308

## Listo — Permisos de trabajo digitales (PRD-308)

**Lo que miré:** 5 documentos y 1 solo de descubrimiento: una entrevista del 2025-09-27 con un cliente y una frase. Hay una definición y un caso de negocio, ambos del 2025-10-01. Lo más reciente es el acta del comité del 2026-10-15. Todo se pudo leer.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.5.0 (términos 1.1).
- El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.5.0-2026-10-18.md` y en el `.pdf` con el mismo nombre.
- SHA-256 del .md: `05a6d5118354…`; del .pdf: `335e499393eaf35a…`.

**Preguntas:** nadie respondió, así que tomé las sugeridas. Javier Hoyos es el gerente. Decide el «Comité de producto», porque el acta lo nombra, aunque ningún documento dice qué persona decide. El estado quedó en `estado-producto/PRD-308`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Los Supervisores no tienen permisos digitales | Una entrevista con un cliente que dice «Lo necesito y hoy no lo tengo». No dice que sea supervisor. | 2025-09-27 |
| volumen_mensual = 98.890 | Solo el propio caso de negocio. No hay serie medida. | 2025-10-01 |
| Retorno esperado en 24 meses | Nada: no hay monto. | 2025-10-01 |
| Supuesto «Operaciones adopta la herramienta», «se confirmó» | Una entrevista con doce clientes del 2026-08-08 que no está en la carpeta | 2026-08-08 |
| 12 requerimientos (9 aceptados, 3 propuestos) | El acta del comité. 5 de los 9 aceptados llevan evidencia (55.6 %), y es la misma entrevista. | 2026-10-15 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** El cierre no tendrá contra qué juzgarse.
- **Nadie mide el volumen mensual.** Hay una cifra declarada y ninguna serie, así que no se puede contrastar.
- **La propuesta.** Dice solo «Propuesta principal».
- **El retorno.** No tiene monto.
- **Quién decide, como persona.**
- **La entrevista de doce clientes** que sostiene la verificación del supuesto.
- **Qué es «el plan»** que el comité mantiene.
- **El problema de cada requerimiento.** Los 12 se llaman «Requerimiento REQ-48xx».
- **Un proyecto que construya algo.** 0 de los 9 aceptados lo tienen.

### Señales del cálculo
- 9 aceptados sin proyecto.
- 4 aceptados sin evidencia de demanda: REQ-4802, 4803, 4806 y 4809.
- 4 aceptados sin criterio de aceptación: REQ-4803, 4805, 4806 y 4808.
- 1 aceptado sin doliente: REQ-4809.
- 3 propuestos sin decidir desde hace 60 días o más: REQ-4801 (120 días), REQ-4804 (213) y REQ-4810 (86).
- 8 requerimientos con evidencia vencida (12 meses), toda de la misma entrevista.
- 1 supuesto sin verificar documentado, 158 días después de declararse.

### Supuesto
«Operaciones adopta la herramienta» se declaró el 2026-05-13, siete meses después de la definición. Habla de Operaciones, pero el segmento de la definición es Supervisores. Lo dejé como no verificado hasta que aparezca esa entrevista.

### Qué le falta a tu carpeta
- Las transcripciones de la entrevista de doce clientes y de cualquier otra reciente.
- La serie medida del volumen mensual, con su fuente.
- Las decisiones del comité con fecha y descartados.
- El criterio de éxito y la propuesta en palabras.

**Una advertencia:** el acta atribuye 8 requerimientos a «Cliente entrevistado». Como hay una sola entrevista, los até a ella como evidencia. Si hubo otras entrevistas, el registro sobrestima una sola fuente.

**Corridas:** la corrida `…-product-setup-1` quedó sin salida porque la carpeta `corridas/` no existía cuando la registré. La válida es `2026-10-18-product-setup-2`. La salida completa está en `estado-producto/PRD-308/corridas/salida-product-setup.md`. Los minutos hasta el primer resultado no se midieron.

**Siguiente paso:** `/product-discovery` sobre las entrevistas.