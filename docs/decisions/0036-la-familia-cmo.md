# 0036 · La familia CMO: el mercadeo, con dos agentes sobre lo que se anuncia y lo que se invierte

**Fecha:** 2026-11-25 · **Estado:** propuesta. Los nombres y la estructura están por aceptar por José, y cada fuente se verifica una a una (abajo, con la fecha de cada verificación).

## Contexto

José Francisco Ñáñez pidió el 25 de noviembre de 2026 montar los diseños de la CMO, la CRO y la CDO. Esta
decisión propone la CMO.

La [decisión 0019](0019-scope-comercial-cso.md) eligió la función comercial antes que el mercadeo, por tres
razones:

- el mercadeo vive sobre todo en plataformas de pauta y tableros;
- la función comercial cruza más familias;
- el mercadeo se apoya en ella después.

Esta propuesta toma del mercadeo solo lo que vive en documentos, y deja las plataformas en sus exportaciones:

- **lo que se anuncia**: cada afirmación de una pieza, con su soporte, y cada promoción, con sus condiciones;
- **lo que se invierte**: el presupuesto, la pauta facturada y el resultado medido de cada campaña.

| Marco | Qué aporta | Estado de la fuente |
|---|---|---|
| Código de Publicidad y Comunicaciones de Mercadeo de la Cámara de Comercio Internacional (ICC), undécima edición, 2024 | El estándar de autorregulación: honestidad (art. 4), veracidad (art. 5), soporte de lo que se afirma (art. 6), identificación (art. 7), testimonios e influenciadores (art. 18), niños y adolescentes (art. 20) y protección de datos (art. 22); el capítulo D, sobre las afirmaciones ambientales | Verificado el 2026-11-25 en su índice, en iccwbo.org. **Por verificar:** el texto de cada artículo |
| Colombia · Ley 1480 de 2011, Estatuto del Consumidor | Lo que se anuncia obliga a quien lo anuncia (art. 29). La publicidad engañosa está prohibida y de ella responde el anunciante (art. 30). Las promociones informan sus condiciones de tiempo, modo y lugar (art. 33) | Verificado el 2026-11-25 en el texto de la ley, en el normograma de la Cancillería. También sus definiciones: publicidad (art. 5, num. 12), publicidad engañosa (num. 13) y promociones y ofertas (num. 10) |
| Colombia · Ley 2300 de 2023 | Los horarios y canales de contacto con los consumidores | **Por verificar:** su página en Función Pública no respondió |
| Colombia · Ley 1581 de 2012 | La autorización para tratar los datos de las bases de mercadeo | Ya citada en la [decisión 0031](0031-la-familia-chro.md). **Por verificar:** lo que pide para el uso con fines de mercadeo |
| México, Perú y Brasil | La ley del consumidor y la de publicidad de cada país | **Por verificar** país por país |

## Decisión propuesta

**Criterio CMO · El mercadeo.** Dos agentes y Rostrum, como en las demás familias:

| Agente | Plugin | Lo que hace |
|---|---|---|
| **Lucía**, del latín *lux*, la luz: cada afirmación, a la luz de su soporte | `criterio-claims` | Contrasta cada pieza aprobada con su soporte, cada promoción con sus condiciones publicadas y cada base de contactos con su autorización. Señala la afirmación sin soporte, la comparativa sin fuente, la promoción sin vigencia o sin condiciones, la pieza de un influenciador sin su identificación como publicidad, la pieza publicada sin la aprobación de legal y la base usada sin autorización para mercadeo. |
| **Próspero**, del latín *prosperus*, el que hace que algo rinda: cada peso de la pauta contra lo que produjo | `criterio-campaigns` | Contrasta el presupuesto de cada campaña con la pauta facturada y con su resultado medido. Señala la campaña que pasó su presupuesto, la factura de pauta sin campaña ni orden, la campaña sin su meta ni su medición, el resultado que no coincide con la exportación de la plataforma y la campaña que siguió después de su fecha de fin. |

### Las señales que calcularía el código

| Agente | Señal | Cuándo |
|---|---|---|
| Lucía | `claim_without_substantiation` | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes |
| Lucía | `comparative_claim_without_source` | Una afirmación comparativa no cita su fuente ni su fecha |
| Lucía | `promotion_terms_missing` | Una promoción no publica su vigencia o sus condiciones de tiempo, modo y lugar |
| Lucía | `sponsored_content_unidentified` | Una pieza pagada a un influenciador no se identifica como publicidad |
| Lucía | `piece_published_unapproved` | Una pieza se publicó sin la aprobación que pide la política, o antes de ella |
| Lucía | `contact_base_without_consent` | Una base de contactos usada en una campaña no tiene autorización para mercadeo |
| Próspero | `campaign_over_budget` | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política |
| Próspero | `media_invoice_unmatched` | Una factura de pauta no tiene campaña ni orden de compra |
| Próspero | `campaign_without_goal` | Una campaña no tiene meta ni indicador de medición |
| Próspero | `result_differs_from_platform` | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte |
| Próspero | `campaign_ran_past_end` | Hay pauta facturada después de la fecha de fin de la campaña |

**Las tolerancias, las metas y quién aprueba cada pieza los fija la organización**, en su política. El código
calcula y la persona decide.

### Lo que nunca hace

- **Aprobar una pieza, juzgar la creatividad ni decir si una afirmación es verdadera.** Dice si tiene soporte; si el soporte basta lo decide legal.
- **Conectarse a una plataforma de pauta ni de analítica.** Procesa sus exportaciones.
- **Procesar los datos de una persona.** De las bases de contactos solo procesa su registro: cuántos registros, con qué autorización y desde cuándo.

### Lo que cruza con las otras familias

| Lo que procesa | Con qué familia |
|---|---|
| Las facturas de pauta contra la contabilidad | CFO (Clara) |
| Los contratos con agencias, medios e influenciadores | CLO (Fidel) |
| La campaña contra las oportunidades y los cierres que produjo | CCO (Augusto y Valeria) |
| La autorización de las bases de datos | CDO (Custodia), si se acepta la decisión 0034 |

### Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| La política de publicidad y de aprobación de piezas | Word o PDF | Los dos |
| Las piezas aprobadas, con su texto | PDF, Word o imagen con su texto transcrito | Lucía |
| Los soportes de cada afirmación | PDF o Excel | Lucía |
| Las bases de términos y condiciones de cada promoción | Word o PDF | Lucía |
| El registro de bases de contactos con su autorización | Excel o CSV | Lucía |
| El plan de mercadeo con el presupuesto por campaña | Excel | Próspero |
| Las órdenes y las facturas de pauta | PDF o Excel | Próspero |
| Las exportaciones de resultados de las plataformas | Excel o CSV | Próspero |

### La prueba

- **Organizaciones sintéticas** de retail, banca y consumo masivo, más dos controles.
- **Versiones:** la 0.1.0, construida con su motor probado; la 0.2.0, con la ronda de los dos agentes.

## Lo que queda abierto

1. **Los nombres** Lucía y Próspero, por aceptar por José.
2. **La estructura**: dos agentes, sus señales y sus documentos, por aceptar por José.
3. **Las fuentes por verificar**: el texto de los artículos del Código ICC, la Ley 2300 de 2023, lo que pide la Ley 1581 para el mercadeo, y la ley de publicidad de México, Perú y Brasil.
4. **Las exportaciones de las plataformas**, como Google Ads, Meta y LinkedIn, cada una con su fuente o con los encabezados de una exportación real, como en la CFO.
