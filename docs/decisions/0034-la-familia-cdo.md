# 0034 · La familia CDO: los datos, con dos agentes sobre el gobierno, la calidad y el linaje

**Fecha:** 2026-11-24 · **Estado:** aceptada: los nombres y la estructura, por José el 2026-11-25. Las fuentes se verifican una a una (abajo, con la fecha de cada verificación) ·
**Modifica:** [0015](0015-scope-datos-cdo.md), la propuesta de alcance de la CDO, que esta decisión reemplaza

## Contexto

José Francisco Ñáñez fijó el orden de los nuevos diseños: primero la CAE, construida en la 0.1.0
([decisión 0033](0033-la-familia-cae.md)); después la CDO, los datos. Esta decisión la define.

La [decisión 0015](0015-scope-datos-cdo.md), del 23 de octubre de 2026, propuso el alcance: un agente que
contrasta la cifra publicada con su fuente y su linaje, y la política de datos con su cumplimiento, sobre
las tres áreas de DAMA-DMBOK que se trabajan contra documentos —el gobierno, la calidad y los metadatos con
el linaje—. Y tres reglas que esta decisión conserva: **procesa exportaciones y nunca se conecta a una
base; no procesa los datos personales en sí, solo sus metadatos; y la ley de cada país se verifica antes de
citarse.**

Lo que cambia: dos agentes en lugar de uno, porque son dos personas distintas en el área —quien gobierna
los datos (el catálogo, los dueños, las políticas) y quien responde por la cifra que llega a la dirección
(su calidad y su linaje)—, y en banca el marco de los principios de agregación de datos de riesgo del
Comité de Basilea (BCBS 239).

| Marco | Qué aporta | Estado de la fuente |
|---|---|---|
| DAMA-DMBOK, segunda edición (DAMA International) | Las áreas de la gestión de datos; la familia toma el gobierno, la calidad y los metadatos con el linaje | Verificado el 2026-11-24 en dama.org: la segunda edición es la vigente, con una revisión lanzada en 2024 y un proyecto de tercera edición desde 2025; es un libro de pago. **Por verificar:** el número de áreas y el lugar del gobierno, en el libro |
| Comité de Basilea, BCBS 239: principios para la agregación eficaz de datos de riesgo y la presentación de informes de riesgo | La exactitud, la integridad y la oportunidad de la cifra de riesgo que llega a la junta | Verificado el 2026-11-24 en bis.org: publicado el 9 de enero de 2013, vigente; informe de avance del 28 de noviembre de 2023 sobre 31 bancos sistémicos. Verificado el 2026-11-24 en el documento: catorce principios en cuatro grupos —el gobierno y la infraestructura (1 y 2), la capacidad de agregar los datos de riesgo (3 a 6: exactitud e integridad, completitud, oportunidad, adaptabilidad), la presentación de informes de riesgo (desde el 7: exactitud, exhaustividad, claridad y utilidad) y la revisión de los supervisores—; se dirigen primero a los bancos sistémicos, en el grupo y en cada entidad (párrafo 13), y a los sistémicos locales tres años después de su designación (párrafo 15). Ariadna trabaja sobre los principios 3, 4, 5 y 7. **Por verificar:** los títulos de los principios 10 a 14 y la página de cada uno |
| ISO/IEC 25012, el modelo de calidad de datos | Las características de calidad con las que se escribe una regla | Verificado el 2026-11-24 en la tienda de la IEC y en la muestra oficial de la norma: primera edición, de diciembre de 2008, dentro de la serie SQuaRE; quince características desde dos puntos de vista, el inherente al dato y el que depende del sistema. **Por verificar:** el nombre de cada característica y si sigue vigente; su página en iso.org no respondió |
| ISO 8000, la calidad de datos | La calidad de los datos maestros | **Por verificar:** la parte 1 de 2011 está retirada y la reemplaza la de 2022; las partes 8 y 61, sin verificar |

**La ley de datos personales de cada país** ya está verificada en la [decisión 0031](0031-la-familia-chro.md)
para ocho países (Colombia, México, Argentina, Chile, Ecuador, Perú, Panamá y Costa Rica), por sus datos
sensibles. Lo que la CDO necesita de ella es otra cosa —el registro de las bases de datos personales, como
el Registro Nacional de Bases de Datos de Colombia ante la SIC— y está **por verificar** país por país.

## Decisión

**Criterio CDO · Los datos.** Dos agentes y Rostrum, como en las demás familias:

| Agente | Plugin | Lo que hace |
|---|---|---|
| **Custodia**, del latín *custodia*, la guarda: cada dato con quien responde por él | `criterio-data-governance` | Contrasta el catálogo de datos con sus dueños, su clasificación, su conservación y sus políticas: el conjunto sin dueño o sin clasificar, la política con la revisión vencida, el dato que se conserva más de lo que dice la política, el término del informe que no está en el glosario y la base de datos personales que no aparece en el registro que pide la ley del país |
| **Ariadna**, la del hilo que lleva de vuelta por el laberinto: cada cifra hasta su fuente | `criterio-data-quality` | Contrasta cada cifra de un informe de dirección con su fuente y su linaje, y cada regla de calidad con su umbral: la cifra sin fuente, la que no coincide con su fuente en el mismo corte, el linaje que se corta, la regla bajo su umbral y la que no corrió en el periodo |

### Las señales que calcularía el código

| Agente | Señal | Cuándo |
|---|---|---|
| Custodia | `dataset_without_owner` | Un conjunto de datos del catálogo no tiene un dueño de negocio |
| Custodia | `dataset_without_classification` | Un conjunto no tiene su clasificación de confidencialidad |
| Custodia | `policy_review_overdue` | Una política de datos o de conservación pasó su fecha de revisión |
| Custodia | `retention_exceeded` | Un conjunto se conserva más tiempo del que fija la política para su tipo |
| Custodia | `term_not_in_glossary` | Un indicador de un informe de dirección no tiene su definición en el glosario de negocio |
| Custodia | `personal_data_unregistered` | Un conjunto con datos personales no aparece en el registro que exige la ley del país (por verificar en cada país) |
| Ariadna | `figure_without_source` | Una cifra de un informe de dirección no tiene fuente en el catálogo ni en el linaje exportado |
| Ariadna | `figure_differs_from_source` | La cifra del informe no coincide con la de su fuente para el mismo corte, más allá de la tolerancia que fija la organización |
| Ariadna | `cutoff_mismatch` | La cifra del informe sale de un corte distinto al que el informe declara |
| Ariadna | `lineage_broken` | Un paso del linaje de una cifra no tiene su sistema de origen |
| Ariadna | `quality_rule_below_threshold` | El resultado exportado de una regla de calidad está bajo su umbral |
| Ariadna | `quality_rule_not_run` | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo |
| Ariadna | `critical_data_without_rule` | Un dato marcado como crítico no tiene ninguna regla de calidad |

**Las tolerancias, los umbrales, los plazos de revisión y de conservación los fija la organización**, en
su política de datos: el código calcula y la persona decide.

### Lo que nunca hace

- **Conectarse a una base de datos o a un sistema.** Procesa las exportaciones del catálogo, del linaje, de
  los resultados de calidad y los informes.
- **Procesar un dato personal.** Solo sus metadatos: la configuración excluye por omisión las extracciones
  con registros de personas.
- **Modificar un dato, asignar un dueño o decidir una clasificación.** Dice qué falta; la decisión es del
  área.

### Lo que cruza con las otras familias

| Lo que procesa | Con qué familia |
|---|---|
| Las cifras de los estados financieros y del informe al supervisor contra la contabilidad | CFO (Clara) |
| La clasificación y los accesos de un conjunto | CISO (Alexis) |
| Los datos de candidatos y su conservación | CHRO (Cándido) |
| El hallazgo de auditoría sobre la calidad de un dato | CAE (Remedios) |

### Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| La política de datos, la de conservación y el glosario de negocio | Word, PDF o Excel | Los dos |
| La exportación del catálogo de datos: cada conjunto con su dueño, su clasificación, su tipo y sus fechas | Excel o CSV, con el mapeo de columnas del setup | Custodia |
| El registro de bases de datos personales de la organización | Excel, CSV o PDF | Custodia |
| Los informes de dirección y del supervisor, con sus cifras | PDF, Excel o Word | Ariadna |
| La exportación del linaje: cada cifra con sus pasos y su sistema de origen | Excel o CSV | Ariadna |
| Los resultados de las reglas de calidad por periodo | Excel o CSV | Ariadna |

### La prueba

- **Organizaciones sintéticas** de banca, seguros y retail, más dos controles, con su catálogo, su linaje,
  sus reglas de calidad, sus informes y sus políticas. Ninguna con registros de personas.
- **Versiones:** la 0.1.0, construida con su motor probado; la 0.2.0, con la ronda de los dos agentes.

## Lo que queda abierto

1. **Las fuentes por verificar**: las áreas de DAMA-DMBOK, los títulos de los principios 10 a 14 de BCBS 239, ISO/IEC 25012, las
   partes de ISO 8000 y el registro de bases de datos personales de cada país.
2. **Los formatos de exportación** de los catálogos y del linaje más usados —Collibra, Alation, Microsoft
   Purview, Informatica—, cada uno con su fuente o con los encabezados de una exportación real, como en la
   CFO.
3. **La primera fuente de cifras**, de la decisión 0015: el informe al supervisor contra la contabilidad,
   con la CFO.
