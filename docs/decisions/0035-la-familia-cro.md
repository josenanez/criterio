# 0035 · La familia CRO: los riesgos de la organización, con dos agentes sobre el apetito y los eventos

**Fecha:** 2026-11-25 · **Estado:** propuesta. Los nombres y la estructura están por aceptar por José, y cada fuente se verifica una a una (abajo, con la fecha de cada verificación).

## Contexto

José Francisco Ñáñez pidió el 25 de noviembre de 2026 montar los diseños de la CMO, la CRO y la CDO. Esta
decisión propone la CRO. **Aquí CRO es Chief Risk Officer**, el responsable de la gestión integral de riesgos
de la segunda línea. No es Chief Revenue Officer: esa lectura se descartó en la [decisión 0022](0022-la-familia-comercial-es-la-cco.md),
y la función comercial es la familia CCO.

Las demás familias ya tocan el riesgo, cada una desde su área. La CISO procesa el riesgo de seguridad de la
información, y Prudencia, de la CAE, pone el plan de auditoría al lado de la matriz de riesgos de la segunda
línea. Lo que nadie procesa todavía es el marco que gobierna todos los riesgos juntos: la declaración de
apetito con sus límites, los indicadores que avisan antes y la base de eventos de pérdida. Esos documentos
son los del CRO.

| Marco | Qué aporta | Estado de la fuente |
|---|---|---|
| ISO 31000:2018, *Risk management — Guidelines* | Los principios, el marco y el proceso de la gestión del riesgo, en cualquier organización | Verificado el 2026-11-25 en iso.org: segunda edición, de febrero de 2018; la página dice que se revisó y confirmó en 2023, y la marca «para revisarse». **Por verificar:** el borrador de la revisión |
| COSO, *Enterprise Risk Management — Integrating with Strategy and Performance* (2017) | El apetito por riesgo atado a la estrategia y al desempeño | **Por verificar** |
| Colombia · Superintendencia Financiera, Circular Externa 018 de 2021 | El Sistema Integral de Administración de Riesgos (SIAR) | Verificado el 2026-11-25 en el texto de la circular, del 22 de septiembre de 2021. Crea el Capítulo XXXI de la Circular Básica Contable y Financiera y el XXXII (SARE, para las entidades exceptuadas). Integra los riesgos de crédito, mercado, operacional, liquidez, contraparte, garantía, seguros y país. Su Parte I trae el marco de apetito de riesgo y el gobierno de riesgos, y su Parte II, la agregación de datos y los informes. Rige desde el 1 de junio de 2023. **Por verificar:** el texto del Capítulo XXXI, que trae el contenido del marco de apetito, los indicadores y el papel de la junta |
| Perú · SBS, Resolución 272-2017 | El Reglamento de Gobierno Corporativo y de la Gestión Integral de Riesgos | Verificado el 2026-11-25 en su texto, publicado el 23 de enero de 2017 y vigente desde el 1 de abril de 2018. Define el apetito, la capacidad y los límites de riesgo (art. 2). El directorio aprueba el sistema de apetito (art. 7) y firma una declaración anual de cumplimiento (art. 8). La unidad de riesgos es independiente de las de negocio (art. 25), y su jefe tiene nivel gerencial y reporta al directorio, a la gerencia o al comité de riesgos (art. 26). La empresa envía a la SBS un informe anual de riesgos (art. 27). |
| Brasil · CMN, Resolución 4.557 de 2017 | La estructura de gestión de riesgos y de capital | Verificado el 2026-11-25 en su versión en inglés del Banco Central: la declaración de apetito por riesgos, la RAS (art. 5), las pruebas de estrés (arts. 11 a 19) y los segmentos S1 a S4 (art. 2), con una estructura simplificada para S5 (art. 3). **Por verificar:** los artículos sobre el CRO y el comité de riesgos, y las reformas posteriores, en el texto vigente en portugués |

## Decisión propuesta

**Criterio CRO · Los riesgos.** Dos agentes y Rostrum, como en las demás familias:

| Agente | Plugin | Lo que hace |
|---|---|---|
| **Severo**, del latín *severus*, el que no hace concesiones: cada exposición contra su límite | `criterio-risk-appetite` | Contrasta la declaración de apetito con sus límites y cada límite con la exposición que reportan las áreas. Señala el límite excedido sin su plan, el que no tiene dueño ni fecha de revisión, la exposición reportada fuera de plazo, el riesgo de la matriz sin límite ni indicador, y la declaración que la junta no ha revisado en el plazo que fija el marco. |
| **Casandra**, la que anunciaba lo que venía: cada indicador que avisa antes | `criterio-risk-events` | Contrasta los indicadores clave de riesgo con sus umbrales y la base de eventos de pérdida con sus registros. Señala el indicador en alerta sin acción, el evento sin causa, sin monto o fuera del plazo de registro, el evento que se repite en el mismo proceso y el que no está en la matriz de riesgos. |

### Las señales que calcularía el código

| Agente | Señal | Cuándo |
|---|---|---|
| Severo | `limit_breached_without_plan` | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso |
| Severo | `limit_without_owner` | Un límite no tiene dueño |
| Severo | `limit_review_overdue` | Un límite pasó su fecha de revisión |
| Severo | `exposure_report_late` | Un área reportó su exposición después del plazo del marco |
| Severo | `risk_without_limit` | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador |
| Severo | `appetite_statement_outdated` | La declaración de apetito no tiene la revisión de la junta en el plazo que fija el marco |
| Casandra | `kri_alert_without_action` | Un indicador está en su umbral de alerta o de límite y no tiene acción registrada |
| Casandra | `kri_not_reported` | Un indicador no tiene valor en el periodo |
| Casandra | `loss_event_incomplete` | Un evento de pérdida no tiene causa, monto o proceso |
| Casandra | `loss_event_registered_late` | Un evento se registró después del plazo de la política |
| Casandra | `loss_event_repeated` | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política |
| Casandra | `loss_event_risk_unmapped` | Un evento no corresponde a ningún riesgo de la matriz |

**El apetito, los límites, los umbrales y los plazos los fija la organización** en su marco de apetito. El
código calcula y la persona decide.

### Lo que nunca hace

- **Fijar o cambiar un límite, aprobar un exceso ni aceptar un riesgo.** Dice qué está fuera; la decisión es de la junta, del comité y de las áreas.
- **Calcular capital, valor en riesgo ni pérdida esperada.** Procesa las cifras que reportan las áreas y los modelos de la organización; no los reemplaza.
- **Conectarse a un sistema.** Procesa las exportaciones de la matriz, de los límites, de los indicadores y de la base de eventos.

### Lo que cruza con las otras familias

| Lo que procesa | Con qué familia |
|---|---|
| Los incidentes de seguridad como eventos de riesgo operacional | CISO (Amparo) |
| La matriz de riesgos que usa el plan de auditoría | CAE (Prudencia) |
| Las cifras de exposición contra la contabilidad | CFO (Clara) |
| Los indicadores que dependen de la calidad de un dato | CDO (Ariadna), si se acepta la decisión 0034 |

### Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| El marco y la declaración de apetito, con sus límites | Word, PDF o Excel | Severo |
| La matriz de riesgos de la segunda línea | Excel o CSV | Los dos |
| Los reportes de exposición de las áreas por periodo | Excel o CSV | Severo |
| Las actas del comité de riesgos y de la junta | Word o PDF | Severo |
| Los indicadores clave de riesgo con sus umbrales y sus valores | Excel o CSV | Casandra |
| La base de eventos de pérdida | Excel o CSV | Casandra |

### La prueba

- **Organizaciones sintéticas** de banca, seguros y una cooperativa en Colombia, Perú y Brasil, más dos controles.
- **Versiones:** la 0.1.0, construida con su motor probado; la 0.2.0, con la ronda de los dos agentes.

## Lo que queda abierto

1. **Los nombres** Severo y Casandra, por aceptar por José.
2. **La estructura**: dos agentes, sus señales y sus documentos, por aceptar por José.
3. **Las fuentes por verificar**: COSO ERM 2017, el texto del Capítulo XXXI de la Superintendencia Financiera, los artículos del CRO y del comité en la Resolución CMN 4.557 vigente, y la revisión de ISO 31000.
4. **Fuera de la banca**: la familia sirve a cualquier organización con un marco de apetito. La regulación de cada país solo se cita en las entidades vigiladas.
