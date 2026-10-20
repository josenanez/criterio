# criterio-cfo · las fuentes

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), regla 1).

## Formatos de factura y comprobantes electrónicos

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | DIAN · Anexo técnico de la factura electrónica de venta | 1.9 | [dian.gov.co](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo-Tecnico-Factura-Electronica-de-Venta-vr-1-9.pdf) | 2026-10-20 | Por verificar: confirmar que la 1.9 sigue vigente; hay un proyecto de resolución sobre anexos técnicos | Lector del XML de Colombia; material de prueba |
| F-02 | DIAN · Resolución 000165 de 2023 (sistema de facturación electrónica) | — | [normograma](https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0165_2023.htm) | 2026-10-20 | Verificada como norma que adopta los anexos | Contexto de F-01 |
| F-03 | DIAN · Resolución 000008 de 2024 (fija el 1 de mayo de 2024 para adoptar la versión 1.9) y Concepto 1531 de 2024 | — | [Resolución](https://normograma.icfes.gov.co/docs/pdf/resolucion_dian_0008_2024.pdf) · [Concepto](https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_1531_2024.htm) | 2026-10-20 | Verificada | Vigencia de F-01 |
| F-04 | SRI · Ficha técnica de comprobantes electrónicos, esquema offline | 2.32 (noviembre de 2025) | [sri.gob.ec](https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/29562323-2e76-42f5-abb6-cb7ac542c3c6/FICHA%20TE%CC%81CNICA%20COMPROBANTES%20ELECTRO%CC%81NICOS%20ESQUEMA%20OFFLINE%20Versio%CC%81n%202.32.pdf) | 2026-10-20 | Por verificar campo por campo antes del lector | Lector del XML de Ecuador (clave de acceso de 49 dígitos, tipos 01, 03, 04, 05, 06, 07); material de prueba |

## Marco contable

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-05 | Colombia · Ley 1314 de 2009 y Decreto Único Reglamentario 2420 de 2015 (normas de información financiera, grupos 1, 2 y 3) | Con sus modificaciones | Por enlazar al texto oficial | — | Por verificar | Pregunta de `finance-setup` sobre el grupo de la entidad; ninguna opinión de tratamiento en la primera versión |
| F-06 | Ecuador · Superintendencia de Compañías, Resolución 08.G.DSC de 20 de noviembre de 2008 (adopción de NIIF por fases, 2010–2012) | — | [IAS Plus](https://iasplus.com/content/596f5d4d-01e2-4c37-9ee8-7a8b6524b02d) | 2026-10-20 | Por verificar en la fuente oficial de la Superintendencia | Pregunta de `finance-setup` sobre el marco de la entidad |

## Cifras de terceros

| Id | Cifra | Fuente | Muestra | Estado |
|---|---|---|---|---|
| F-10 | 44 % cerraba el trimestre en seis días hábiles en 2023, contra 49 % en 2019 | Ventana Research / ISG, investigación Smart Financial Close, 2023 | No indicada en la nota | Verificada (registro de cifras del proyecto) |
| F-11 | En las organizaciones encuestadas, 45 % de los controles SOX son manuales; las horas del programa subieron 32 % en dos años (11.800 a 15.580) | KPMG, SOX Survey 2025 | ~150 profesionales SOX | Verificada (la fuente dice «manuales», no «totalmente manuales») |
| F-12 | Cierre anual: 10 días los mejores, 18 la mediana, 35 los rezagados | APQC, abril de 2026 | — | Por verificar |
| F-13 | 18 % de los contadores comete errores a diario y 59 % varios al mes | Gartner, febrero de 2024 | 497 contadores | Por verificar |

## Cómo se agrega una fuente

1. Se le da el siguiente identificador libre y se llena la fila entera: versión, enlace al
   emisor, fecha de consulta, estado y uso.
2. Mientras diga «por verificar», nada se construye sobre ella.
3. Cuando una fuente cambia de versión, se agrega la nueva fila y la anterior se marca como
   reemplazada, sin borrarla: el material de prueba generado con ella sigue citándola.
