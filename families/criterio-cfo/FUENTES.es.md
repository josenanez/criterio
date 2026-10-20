# criterio-cfo · las fuentes

<!-- generado por scripts/cfo.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/cfo.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), regla 1).

## Formatos de factura y comprobantes electrónicos

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | DIAN · Anexo técnico de la factura electrónica de venta | 1.9 | [dian.gov.co](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo-Tecnico-Factura-Electronica-de-Venta-vr-1-9.pdf) | 2026-10-20 | Verificada: La DIAN publica la versión 1.9 con la Resolución 000165 de 2023 (F-02); rige desde el 1 de mayo de 2024 (F-03), y la Resolución 227 de 2025 (F-07) mantiene vigentes los anexos de las resoluciones que compila. Se vuelve a consultar antes de cada versión del lector | Lector del XML de Colombia; material de prueba |
| F-02 | DIAN · Resolución 000165 de 2023 (sistema de facturación electrónica) | — | [normograma](https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0165_2023.htm) | 2026-10-20 | Verificada: Como norma que adopta los anexos | Contexto de F-01 |
| F-03 | DIAN · Resolución 000008 de 2024 (fija el 1 de mayo de 2024 para adoptar la versión 1.9) y Concepto 1531 de 2024 | — | [Resolución](https://normograma.icfes.gov.co/docs/pdf/resolucion_dian_0008_2024.pdf) · [Concepto](https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_1531_2024.htm) | 2026-10-20 | Verificada | Vigencia de F-01 |
| F-04 | SRI · Ficha técnica de comprobantes electrónicos, esquema offline | 2.32 (8 de octubre de 2025) | [sri.gob.ec](https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/29562323-2e76-42f5-abb6-cb7ac542c3c6/FICHA%20TE%CC%81CNICA%20COMPROBANTES%20ELECTRO%CC%81NICOS%20ESQUEMA%20OFFLINE%20Versio%CC%81n%202.32.pdf) | 2026-10-20 | Verificada: La portada dice «Actualizado octubre 2025» y el control de cambios fecha la 2.32 el 08/10/2025. Confirmados en el texto: la clave de acceso de 49 dígitos (sección 5.2) y los tipos 01 factura, 03 liquidación de compra, 04 nota de crédito, 05 nota de débito, 06 guía de remisión y 07 comprobante de retención (tabla 3). El resto de los campos se verifica uno por uno al escribir el lector | Lector del XML de Ecuador; material de prueba |
| F-07 | DIAN · Resolución 227 de 2025, Resolución Única en materia tributaria, aduanera y cambiaria (23 de septiembre de 2025, Diario Oficial 53.254) | — | [normograma](https://cancilleria.gov.co/normograma/compilacion/docs/resolucion_dian_0227_2025.htm) | 2026-10-20 | Verificada: Sus considerandos dicen que los anexos de las resoluciones compiladas siguen vigentes como parte del acto; el Título 5 compila el sistema de facturación | Vigencia de F-01 |

## Marco contable

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-05 | Colombia · Ley 1314 de 2009 (13 de julio de 2009) y Decreto Único Reglamentario 2420 de 2015 (14 de diciembre de 2015), con los grupos 1, 2 y 3 de información financiera | Con sus modificaciones; el anexo 1 lo modificó el Decreto 1432 de 2020 | [Ley 1314](https://normograma.supersalud.gov.co/compilacion/docs/ley_1314_2009.htm) · [Decreto 2420](https://www.funcionpublica.gov.co/eva/gestornormativo/norma_pdf.php?i=76745) | 2026-10-20 | Verificada: El decreto define el grupo 1 (anexo 1), el grupo 2 (anexo 2, NIIF para las Pymes) y el grupo 3 (anexo 3, microempresas); el gestor normativo advierte que la vigencia se confirma en cada consulta | Pregunta de `finance-setup` sobre el grupo de la entidad; ninguna opinión de tratamiento en la primera versión |
| F-06 | Ecuador · Superintendencia de Compañías, Resolución 08.G.DSC.010 de 20 de noviembre de 2008 (Registro Oficial 498, 31 de diciembre de 2008): adopción obligatoria de las NIIF en tres grupos, 2010 a 2012 | — | [Superintendencia](https://www.supercias.gob.ec/bd_supercias/descargas/niif/Diferencias%20entre%20NIIF%20completas%20y%20NIIF%20para%20las%20PYMES%20y%20su%20aplicacion%20a%20las%20partidas%20contables.pdf) · [Texto en IAS Plus](https://iasplus.com/content/596f5d4d-01e2-4c37-9ee8-7a8b6524b02d) | 2026-10-20 | Verificada: El número, la fecha, el Registro Oficial y el cronograma los confirma un documento de la Superintendencia; el texto completo de la resolución se consultó en IAS Plus | Pregunta de `finance-setup` sobre el marco de la entidad |
| F-08 | Ecuador · Superintendencia de Compañías, Resolución SC.INPA.UA.G-10.005 de 5 de noviembre de 2010 (Registro Oficial 335, 7 de diciembre de 2010): clasificación de las compañías para aplicar la NIIF para las Pymes | — | [Superintendencia](https://www.supercias.gob.ec/bd_supercias/descargas/niif/Diferencias%20entre%20NIIF%20completas%20y%20NIIF%20para%20las%20PYMES%20y%20su%20aplicacion%20a%20las%20partidas%20contables.pdf) | 2026-10-20 | Por verificar: La cita el mismo documento de la Superintendencia, con los límites de activos, ventas y trabajadores; falta consultar el texto de la resolución y sus reformas antes de usar esos límites | Pregunta de `finance-setup` sobre si la entidad aplica la NIIF para las Pymes |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| F-10 | **44 %** cerraba el trimestre en seis días hábiles en 2023, contra 49 % en 2019 | [Ventana Research / ISG, investigación Smart Financial Close](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) | 2023 | No indicada en la nota | Verificada: Registro de cifras del proyecto |
| F-11 | **45 %** de los controles SOX son manuales en las organizaciones encuestadas; las horas del programa subieron 32 % en dos años, de 11.800 a 15.580 | [KPMG, SOX Survey](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) | 2025 | Cerca de 150 profesionales SOX | Verificada: La fuente dice «manuales», no «totalmente manuales» |
| F-12 | **18 días** es la mediana del cierre anual; los mejores lo hacen en 10 días o menos y los más lentos en 35 | [APQC, blog del 8 de abril de 2026, y su medida de Open Standards Benchmarking del cierre anual a nivel de sitio](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-year-end-close) | 2026 | La nota no la indica; la medida de benchmarking reporta la mediana de 18,0 días con 2.214 organizaciones | Verificada: Los cuartiles de la medida de benchmarking son de acceso restringido; las cifras de 10 y 35 días salen de la nota |
| F-13 | **18 %** de las personas de la función de contraloría comete errores al menos a diario, y 59 % varios al mes, por restricciones de capacidad | [Gartner, comunicado del 21 de febrero de 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) | 2024 | 497 personas de la función de contraloría, encuesta de julio de 2023 | Verificada: La muestra es de la función de contraloría, no solo de contadores |

## Cómo se agrega una fuente

1. Se agrega en `fuentes.json` con el siguiente identificador libre —F-01 a F-09 para fuentes
   técnicas y normativas, desde F-10 para cifras de terceros— y la fila entera: versión, enlace
   al emisor, fecha de consulta, estado y uso. Después se corre `python3 scripts/cfo.py`.
2. Mientras diga «por verificar», nada se construye sobre ella: la puerta falla si un comando
   la cita.
3. Cuando una fuente cambia de versión, se agrega la nueva fila y la anterior se marca como
   reemplazada, sin borrarla: el material de prueba generado con ella sigue citándola.
