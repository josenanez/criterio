# criterio-cmo · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0036](../../docs/decisions/0036-la-familia-cmo.md), regla 1).

## Los marcos del mercadeo

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | Cámara de Comercio Internacional (ICC) · Código de Publicidad y Comunicaciones de Mercadeo, undécima edición | 2024 | [iccwbo.org](https://iccwbo.org/wp-content/uploads/sites/3/2024/09/ICC_2024_MarketingCode_2024.pdf) | 2026-11-25 | Verificada: Verificado en su índice: honestidad (art. 4), veracidad (art. 5), soporte de lo que se afirma (art. 6), identificación (art. 7), testimonios e influenciadores (art. 18), niños y adolescentes (art. 20), protección de datos (art. 22) y el capítulo D, sobre las afirmaciones ambientales. Se cita por su nombre y sus artículos, nunca por su texto. Por verificar: el texto de cada artículo | El estándar de autorregulación de lo que se anuncia: el soporte de cada afirmación, la identificación de la publicidad y las bases de datos, que son las señales de Lucía |
| F-02 | Media Rating Council (MRC), con ANA, 4A's y ACA · Outcomes and Data Quality Standards | Versión final, septiembre de 2022 | [mediaratingcouncil.org](https://mediaratingcouncil.org/sites/default/files/Standards/MRC%20Outcomes%20and%20Data%20Quality%20Standards%20%28Final%29.pdf) | 2026-11-25 | Verificada: Verificado en el documento: su sección 1.1 fija estándares para la calidad de los datos y la atribución de resultados a la exposición y la interacción con la publicidad, y trae una sección de guías de auditoría. Se cita por su nombre, nunca por su texto | El resultado reportado de una campaña, contra la medición de la plataforma: las señales de Próspero |

## La regulación de la publicidad y del consumidor

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-10 | Colombia · Ley 1480 de 2011, Estatuto del Consumidor | 12 de octubre de 2011 | [normograma de la Cancillería](https://www.cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1480_2011.htm) | 2026-11-25 | Verificada: Verificada en el texto de la ley: lo que se anuncia obliga a quien lo anuncia (art. 29); la publicidad engañosa está prohibida y de ella responde el anunciante (art. 30); las promociones informan sus condiciones de tiempo, modo y lugar (art. 33); y sus definiciones de publicidad (art. 5, num. 12), publicidad engañosa (num. 13) y promociones y ofertas (num. 10) | Las condiciones de una promoción y la responsabilidad por lo que se anuncia, en una entidad de Colombia |
| F-11 | Colombia · Ley 2300 de 2023, los horarios y canales de contacto con los consumidores | 2023 |  | 2026-11-25 | Por verificar: Su página en Función Pública no respondió. Fuera de la 0.1.0 hasta verificarla | Los horarios y canales de contacto de una campaña, cuando entre |
| F-12 | Colombia · Ley 1581 de 2012, protección de datos personales | 2012 |  | 2026-11-25 | Por verificar: Ya citada en la decisión 0031. Por verificar: lo que pide para el uso de una base con fines de mercadeo | La autorización de una base de contactos para mercadeo, cuando entre |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **7,7 %** de los ingresos de la empresa es el presupuesto de mercadeo, igual que el año anterior | [Gartner, 2025 CMO Spend Survey](https://www.gartner.com/en/newsroom/press-releases/2025-05-12-gartner-2025-cmo-spend-survey-reveals-marketing-budgets-have-flatlined-at-seven-percent-of-overall-company-revenue) | 2025 | 402 líderes de mercadeo de Norteamérica, el Reino Unido y Europa | Verificada: Verificada en el comunicado de Gartner del 12 de mayo de 2025: los presupuestos de mercadeo de 2025 siguen en el 7,7 % de los ingresos de la empresa. |
| C-02 | **59 %** de los CMO dicen que no tienen presupuesto suficiente para ejecutar su estrategia | [Gartner, 2025 CMO Spend Survey](https://www.gartner.com/en/newsroom/press-releases/2025-05-12-gartner-2025-cmo-spend-survey-reveals-marketing-budgets-have-flatlined-at-seven-percent-of-overall-company-revenue) | 2025 | 402 líderes de mercadeo de Norteamérica, el Reino Unido y Europa | Verificada: Verificada en el comunicado de Gartner del 12 de mayo de 2025: el 59 % de los CMO dice que no tiene presupuesto suficiente para ejecutar su estrategia en 2025. |
| C-03 | **36 centavos** de cada dólar que entra a una plataforma de compra programática llegan al consumidor | [Association of National Advertisers (ANA), Programmatic Media Supply Chain Transparency Study](https://www.ana.net/content/show/id/media-programmatic-transparency) | 2023 | los datos de registro de 21 anunciantes | Verificada: Verificada en la página del estudio de la ANA, publicado en diciembre de 2023: solo 36 centavos de cada dólar que entra a una plataforma del lado de la demanda llegan efectivamente al consumidor. |

## Cómo se agrega una fuente

1. Se agrega en `fuentes.json` con el siguiente identificador libre —F-NN para fuentes técnicas
   y normativas, C-NN para cifras de terceros— y la fila entera: versión, enlace al emisor, fecha
   de consulta, estado y uso. Después se corre `python3 scripts/familias.py`.
2. Un campo de factura que procese el motor va en la lista de campos de su fuente, con su
   identificador en el anexo; la puerta falla si el motor usa uno que no está verificado.
3. Mientras diga «por verificar», nada se construye sobre ella: la puerta falla si un comando
   la cita.
4. Cuando una fuente cambia de versión, se agrega la nueva fila y la anterior se marca como
   reemplazada, sin borrarla: el material de prueba generado con ella sigue citándola.
