# 0031 · La familia CHRO: el talento, con dos agentes sobre estándares de ocupaciones y competencias

**Fecha:** 2026-11-13 · **Estado:** aceptada: los nombres, por José el 2026-11-13; la estructura, por José el 2026-11-16. Las fuentes se verifican una a una (abajo, con la fecha de cada verificación) ·
**Modifica:** —

## Contexto

José Francisco Ñáñez pidió diseñar la familia del área de gestión humana: buscar talento, validar
hojas de vida, crear perfiles de cargo basados en estándares y analizar perfiles, sobre estándares
de la industria, más las demás funciones del área que se analicen después.

Esta familia es distinta de las anteriores en un punto que manda sobre todo el diseño: **procesa
datos de personas para decidir sobre personas**. En la Unión Europea, un sistema de inteligencia
artificial que filtra hojas de vida o evalúa candidatos está entre los de alto riesgo (Reglamento
(UE) 2024/1689, anexo III, punto 4). En Brasil, la persona tiene derecho a pedir la revisión de una
decisión tomada solo con tratamiento automatizado (LGPD, art. 20). Y cada país donde Criterio se
prueba tiene su ley de datos personales. La familia se diseña para que **ninguna decisión sobre una
persona la tome el agente**, y para que eso se pueda probar.

Como la CISO, el rol se define sobre estándares internacionales, no sobre la ley de cada país:

| Marco | Qué aporta | Estado de la fuente |
|---|---|---|
| ESCO, la clasificación europea de capacidades, competencias, cualificaciones y ocupaciones | Cada ocupación con sus capacidades esenciales y opcionales, enlazada a la CIUO-08 | Verificado el 2026-11-16 en esco.ec.europa.eu/en/use-esco/download: versión vigente v1.2.1, descarga gratuita en «all 28 ESCO languages», en CSV, ODS, RDF, TTL, XML y JSON-LD. Por verificar: que el español y el portugués estén entre los 28, y los términos de reutilización (la página de términos no respondió) |
| O*NET (Departamento de Trabajo de los Estados Unidos), base 31.0 | Tareas, capacidades, conocimientos y nivel de preparación de cada ocupación | Verificado el 2026-11-16 en onetcenter.org: «O*NET® 31.0 Database», en Excel, CSV y JSON; licencia CC BY 4.0 con la atribución que fija la página de licencia (onetcenter.org/license_db.html), y la mención de que se modificó cuando se modifique |
| CIUO-08 (OIT) y su adaptación en cada país —la CUOC en Colombia— | El código de ocupación que conecta el perfil con el estándar, y el nivel de competencia de cada gran grupo | CIUO-08, verificada el 2026-11-16 en ilostat.ilo.org: 10 grandes grupos; nivel de competencia 3 y 4 para directores, 4 para profesionales, 3 para técnicos, 2 para los grupos 4 a 8 y 1 para las ocupaciones elementales; uso libre «without prior authorization». CUOC, verificada el mismo día en dane.gov.co: la actualización 2026, con la Resolución 1344 del 28 de octubre de 2026 en su página, 682 ocupaciones en 10 grandes grupos, y la estructura, el índice y los perfiles ocupacionales en Excel. Las demás adaptaciones, por verificar |
| ISO 30414:2025, el informe de capital humano | Las métricas del área —reclutamiento, rotación, capacitación, sucesión— con su definición | Norma de pago: se citan su número y sus áreas, nunca su texto. Verificada el 2026-11-16 en iso.org/standard/30414: edición 2, publicada en 2025-08 |
| ISO 10667-1 y 10667-2:2020, la evaluación de personas en el trabajo | Qué debe cumplir un proceso de evaluación: propósito declarado, idoneidad del método, información al evaluado | Norma de pago, como la anterior. La 10667-2, verificada el 2026-11-16 en iso.org/standard/74717: edición 2, 2020-11, en revisión («to be revised»). La 10667-1 (iso.org/standard/74716), por verificar: la página no respondió |
| ISO 30405:2023, las directrices de reclutamiento | Las etapas del reclutamiento y lo que se espera de cada una | Norma de pago. Por verificar en iso.org/standard/79488: la página no respondió |
| SFIA 9, para los perfiles de tecnología | Las capacidades de tecnología por nivel de responsabilidad | Verificado el 2026-11-16 en sfia-online.org: gratis para el uso interno de una organización; una herramienta «that contains or supports SFIA use» lleva la licencia de socio, de pago. **Fuera de la 0.1.0** hasta confirmar con la SFIA Foundation si una herramienta de código abierto que la cita necesita esa licencia |

**La regulación que limita la familia**, por verificar en su fuente antes de construir:

| Norma | Qué exige a esta familia |
|---|---|
| Reglamento (UE) 2024/1689, anexo III, punto 4, y art. 6(3) | Alto riesgo para los sistemas de reclutamiento o selección —publicar vacantes dirigidas, filtrar solicitudes, evaluar candidatos— y para los que deciden sobre la relación laboral. El art. 6(3) exceptúa la tarea procedimental acotada o preparatoria, salvo cuando el sistema hace perfiles de personas: entonces es siempre de alto riesgo. Verificado el 2026-11-16 en el texto consolidado del AI Act Service Desk de la Comisión. El Reglamento (UE) 2026/1744, el Digital Omnibus sobre IA, del 8 de julio de 2026, en vigor desde el 27 de julio de 2026: según la página de la Comisión, las obligaciones del anexo III se aplican desde el 2 de diciembre de 2027. Por verificar en el artículo del Reglamento 2026/1744 que modifica el art. 113 |
| LGPD (Brasil), art. 20 | El titular puede pedir la revisión de una decisión tomada solo con tratamiento automatizado. Por verificar: el texto de Planalto rechaza la consulta automática |
| La ley de datos personales de cada país | Los datos sensibles, la autorización y las decisiones automatizadas. Verificado el 2026-11-16: Colombia, Ley 1581 de 2012, arts. 5, 6 y 9 (secretariasenado.gov.co); México, LFPDPPP con la reforma del DOF del 14-11-2025, arts. 2 fr. VI, 7, 8 y 26 fr. II (diputados.gob.mx); Argentina, Ley 25.326, arts. 2, 5, 7 y 20 (infoleg.gob.ar); Chile, Ley 21.719, arts. 2 g), 8 bis, 12 y 16, que entra en vigencia el primer día del mes 24 después de su publicación del 13-12-2024 (bcn.cl); Ecuador, LOPDP, arts. 4, 20 y 26 (copia del Registro Oficial Suplemento 459 en finanzaspopulares.gob.ec). Por verificar: Brasil, Perú, Panamá y Costa Rica (sus textos oficiales no se pudieron procesar), y Paraguay, Guatemala y Honduras, que no tienen una ley general |
| NYC Local Law 144 (referencia) | La auditoría de sesgo de una herramienta automatizada de decisión de empleo: la prueba de la familia toma su idea, no su obligación |

## Decisión

**Criterio CHRO · El talento.** Dos agentes, uno por cada trabajo recurrente que hoy se hace a mano
contra documentos, y Rostrum, como en las demás familias:

| Agente | Plugin | Lo que hace |
|---|---|---|
| **Norma**, del latín *norma*, la escuadra del carpintero: cada perfil sobre un estándar | `criterio-roles` | Crea el perfil de cargo desde la ocupación de ESCO, O*NET o la clasificación del país, con cada requisito atado a una tarea; y analiza los perfiles que ya existen contra su estándar, contra los demás perfiles y contra lo que la ley no permite pedir |
| **Cándido**, del latín *candidus*, «blanco»: de ahí *candidato*, el que en Roma vestía la toga blanca para pedir un cargo. Cada afirmación de la hoja de vida contra su soporte | `criterio-talent` | Prepara la búsqueda —las cadenas para el buscador de quien recluta, el cruce con la base interna y con las exportaciones del ATS—, valida cada hoja de vida contra sus soportes y contrasta cada candidato con el perfil, requisito por requisito y con la cita de dónde sale |

### Las señales que calcula el código

| Agente | Señal | Cuándo |
|---|---|---|
| Norma | `profile_without_occupation` | El perfil no tiene un código de ocupación que lo ate a un estándar |
| Norma | `essential_skill_missing` | Una capacidad esencial de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica |
| Norma | `requirement_without_task` | Un requisito del perfil no se apoya en ninguna de sus tareas |
| Norma | `requirement_not_allowed` | El perfil pide algo que no se puede pedir: edad, sexo, estado civil, fotografía, origen, religión, afiliación política o sindical, o el dato que la ley del país prohíba |
| Norma | `education_level_inconsistent` | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación |
| Norma | `profiles_overlap` | Dos perfiles comparten la ocupación y la mayor parte de sus requisitos |
| Norma | `profile_review_overdue` | El perfil pasó su fecha de revisión |
| Cándido | `claim_without_support` | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte |
| Cándido | `certification_expired` | Una certificación que el perfil exige venció antes de la fecha de la vacante |
| Cándido | `employment_dates_differ` | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral |
| Cándido | `requirement_not_evidenced` | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes |
| Cándido | `protected_data_received` | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud— y se excluye del análisis |
| Cándido | `consent_missing` | No hay autorización de tratamiento de datos del candidato |
| Cándido | `retention_exceeded` | Los datos de un candidato pasaron el tiempo de conservación de la política |
| Cándido | `vacancy_past_target` | La vacante sigue abierta después del plazo de cobertura de la política |

**Los plazos y los requisitos los fija la organización**, en su política de selección y en sus
perfiles, como en la CLO y la CISO: el código calcula y la persona decide. Lo que viene de fuera es
la ocupación y sus capacidades, del estándar que la organización elija.

### Lo que nunca hace

- **Decidir sobre una persona.** No rechaza, no descarta, no asigna un puntaje único y no ordena
  candidatos por un número. Presenta cada requisito con su evidencia, y quien selecciona decide.
- **Usar un dato protegido.** El motor no recibe la fotografía, la edad, el sexo, el estado civil, el
  origen ni la salud de un candidato: el agente los excluye antes de procesar y dice qué excluyó.
- **Inferir lo que no está escrito.** Ni la personalidad, ni la «cultura», ni el potencial: solo lo
  que un documento afirma y lo que lo soporta.
- **Buscar a una persona fuera de lo que la organización le entrega.** No entra a LinkedIn ni a otra
  red, no compra bases y no hace verificaciones de antecedentes: prepara la búsqueda para que la
  corra quien recluta, y procesa las exportaciones y los documentos que llegan.
- **Penalizar una interrupción en la historia laboral.** Una brecha entre dos empleos no es una señal.
- **Publicar en Rostrum datos de un candidato.** Rostrum publica los perfiles y el estado de las
  vacantes; los candidatos, solo con su número y sin su nombre, y solo si la configuración lo dice.

### La prueba de sesgo

Además del material con su clave, como en todas las familias, la CHRO lleva una prueba que ninguna
otra necesita: **pares de candidatos idénticos salvo en un dato protegido** —el nombre, el sexo, la
edad, el país de origen, una fotografía—. El motor y el agente tienen que entregar exactamente lo
mismo para los dos miembros de cada par; cualquier diferencia es un defecto que bloquea la versión.

### Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| Los perfiles de cargo y el manual de funciones | Word, Excel o PDF | Norma |
| La clasificación de ocupaciones que la organización elige (ESCO, O*NET o la del país) | El archivo oficial de cada una | Norma |
| La política de selección: plazos de cobertura, conservación de los datos, quién aprueba | Word o PDF | Cándido |
| Las hojas de vida | PDF o Word | Cándido |
| Los soportes: diplomas, actas de grado, certificaciones, certificados laborales | PDF o imagen con texto | Cándido |
| La exportación del ATS o del buscador de quien recluta, y la base de talento interna | Excel o CSV, con el mapeo de columnas del setup | Cándido |
| Las autorizaciones de tratamiento de datos | El registro de la organización | Cándido |

### Los comandos

Cada agente tiene su instalación (`*-setup`), su revisión completa (`*-scan`), un reporte por cada
grupo de señales y su despertador (`*-wake`):

- **Norma:** `profile-build` (un perfil nuevo desde una ocupación), `profile-check` (los perfiles
  contra su estándar), `profile-language` (lo que no se puede pedir), `profile-map` (los perfiles que
  se solapan y los que faltan).
- **Cándido:** `talent-search` (las cadenas de búsqueda y el cruce con la base interna), `cv-check`
  (cada hoja de vida contra sus soportes), `candidate-fit` (cada candidato contra el perfil, requisito
  por requisito), `privacy-check` (autorizaciones y conservación), `vacancy-status` (las vacantes
  contra su plazo).

### La prueba

- **Organizaciones sintéticas** de banca, retail y tecnología, más dos controles, con perfiles de
  cargo, hojas de vida, soportes, la política de selección y la exportación de un ATS. Nombres,
  documentos y empresas inventados; ninguna persona real.
- **La clave** siembra las señales de los dos agentes y los pares para la prueba de sesgo.
- **Versiones:** la 0.1.0, construida con su motor probado y la prueba de sesgo; la 0.2.0, con la
  ronda de los dos agentes.

## Las demás funciones del área, para analizar

En orden de lo que hoy se hace a mano contra documentos y de cuánto se cruza con las otras familias:

| Función | Qué cruzaría | Con qué familia |
|---|---|---|
| Nómina contra contratos y novedades | Cada pago contra el contrato, el salario vigente y las novedades aprobadas | CFO (Clara y Tomás) |
| Planta contra presupuesto | Cada cargo ocupado y cada vacante contra la planta aprobada y su presupuesto | CFO (Tomás) |
| Capacitación obligatoria | Cada persona contra la formación que su cargo o la regulación exige, con su vencimiento | CLO (Constanza), CISO (Alexis) |
| Seguridad y salud en el trabajo | Los exámenes, las capacitaciones y los comités contra su calendario legal | CLO (Constanza) |
| Evaluación del desempeño | Cada evaluación contra los objetivos acordados y su evidencia, y los planes de mejora contra su plazo | — |
| Ingreso y retiro | Lo que pide cada ingreso y cada retiro —afiliaciones, accesos, entregas— contra su lista | CISO (Alexis, los accesos) |
| Sucesión | Los cargos críticos contra sus sucesores identificados y su preparación | EA (Ofelia) |
| El informe de capital humano | Las métricas de la ISO 30414 calculadas desde los registros, con su fuente | — |

Una tercera agente, para la operación del área —nómina, planta, capacitación e ingreso y retiro—,
se decide cuando se acepte esta propuesta.

## Lo que queda abierto

1. **Los nombres**: Norma y Cándido, aceptados por José el 2026-11-13. Queda cerrado.
2. **Las fuentes:** verificadas el 2026-11-16 las que dice la tabla; el motor no usa una fuente
   sin verificar. Los archivos de ocupaciones —O*NET 31.0, la CUOC 2026 y ESCO v1.2.1— se procesan
   desde su descarga oficial, y sus encabezados salen de esa descarga.
3. **El estándar de ocupaciones por omisión:** ESCO, por estar en español y en portugués y enlazada a
   la CIUO-08, con O*NET y la clasificación del país como alternativas. Por decidir.
4. **Los formatos de exportación:** los ATS que más se usan en la región —Workday, SAP SuccessFactors,
   Buk, Gupy, Factorial— y la exportación del buscador de LinkedIn, cada uno con su fuente verificada
   o con encabezados de una exportación real, como en la CFO.
5. **La regulación de cada país:** qué datos no se pueden pedir ni tratar en una selección, país por
   país, para la señal `requirement_not_allowed` y para `protected_data_received`.
6. **La tercera agente** y las funciones de la tabla anterior.
