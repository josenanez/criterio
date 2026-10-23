# /criterio-portfolio:portfolio-setup documentos/proyectos

Vera quedó configurada y probé con tres proyectos: PRY-206, PRY-201 y PRY-208.

**Cómo se configuró.** Nadie contestó preguntas, así que tomé la respuesta sugerida en cada una.
- **Rol:** PMO del portafolio.
- **Comité:** semanal, con el próximo el 2026-10-30. Esa fecha la supuse, porque ningún documento la dice.
- **Informe:** en HTML, como presentación.
- **Organización:** quedó como «Portafolio de proyectos», porque no aparece en los documentos.
- **Marca de la carpeta:** no dejé `_CRITERIO_PORTAFOLIO.txt` en `documentos/proyectos`, porque no hubo un sí y no escribo ahí sin él.

La configuración está en `.criterio/portafolio/config.json`. Registré los términos (versión 1.2) a nombre de José Francisco Ñáñez, con comprobante en `.criterio/terminos/` (`.md` y `.pdf`, SHA-256 `fe830b9a4eee0bc9…`).

**Qué encontré.** El inventario son 77 documentos en 13 proyectos. De estos hallazgos, 22 de 23 son de PRY-206 y PRY-201:
- **PRY-206 (declara verde, 84%):** los documentos lo contradicen.
  - Hay 4 compromisos vencidos sin evidencia.
  - Hay 3 compromisos reprogramados entre 4 y 6 veces.
  - Hay 3 compromisos sin fecha y 2 hitos cerrados sin acta.
  - El proveedor Talento Digital tiene 2 entregables atrasados.
  - Una factura de Integra Sistemas (71.307.259 COP) cobra un entregable que figura como recibido sin acta.
- **PRY-201 (declara rojo, 90%):**
  - 4 hitos cerrados sin acta.
  - Proyección al cierre 17,2 % por encima del presupuesto aprobado.
  - 2 entregables del proveedor atrasados.
- **PRY-208 (declara verde, 63%):** el cálculo no levantó ninguna señal. Sus datos salen de un acta de hace 17 meses. Tampoco tiene cronograma ni minutas, y su única fecha de cierre (2026-05-21) ya pasó. No lo presento como hallazgo porque el cálculo no lo marcó.

**Una fecha a confirmar.** En PRY-206, las notas del 2026-10-23 dicen «09/01/2027». La leí como 9 de enero de 2027.

**Lo que le falta a la carpeta:**
- Cuatro cronogramas en XML no se leen sin instalar algo; los proyectos son PRY-202, 207, 210 y 211.
- PRY-203, 207 y 208 no tienen minutas.
- Ningún proyecto declara autoridad ni fase.

**Una corrección a lo que escribí.** El informe estima unos 20 minutos para los 10 proyectos que faltan. Esa cifra salió de una proporción y no la medí. La corrida de los tres proyectos tardó 182 segundos, así que el resto debería tomar unos 6 minutos. El informe guardado conserva la estimación vieja. Tampoco cronometré el tiempo hasta el primer resultado.

**Dónde quedó:**
- `estado/records/` (las tres fichas)
- `estado/corridas/salida-portfolio-setup.md` (el informe completo)
- La corrida `2026-10-23-portfolio-setup-1` quedó registrada.

¿Corro el portafolio completo?