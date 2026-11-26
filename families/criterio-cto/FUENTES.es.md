# criterio-cto · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0037](../../docs/decisions/0037-la-familia-cto.md), regla 1).

## Los marcos de la tecnología

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | ISO/IEC 20000-1 · Tecnología de la información — Gestión del servicio — Parte 1: requisitos del sistema de gestión del servicio | Tercera edición, septiembre de 2018; revisada y confirmada en 2023, con la enmienda 1 de 2024 | [iso.org](https://www.iso.org/standard/70636.html) | 2026-11-26 | Verificada: Verificada en iso.org: especifica los requisitos para establecer, implementar, mantener y mejorar un sistema de gestión del servicio, que cubren el diseño, la transición, la entrega y la mejora de los servicios. Se cita por su nombre, nunca por su texto. Por verificar: el texto de sus cláusulas de cambios, incidentes y niveles de servicio | La gestión del servicio: cada cambio, cada incidente y cada nivel acordado, que son las señales de Fausto |
| F-02 | ISO/IEC 19770-1 · Tecnología de la información — Gestión de activos de TI — Parte 1: requisitos del sistema de gestión de activos de TI | Tercera edición, diciembre de 2017; revisada y confirmada en 2024 | [iso.org](https://www.iso.org/standard/68531.html) | 2026-11-26 | Verificada: Verificada en iso.org: especifica los requisitos de un sistema de gestión de activos de TI, para todo tipo de activo y de organización, como extensión de ISO 55001. Se cita por su nombre, nunca por su texto | Los activos de TI: cada activo con su dueño y su soporte, y cada licencia contra su uso, que son las señales de Domingo |
| F-03 | PeopleCert · ITIL 4, la práctica de habilitación del cambio | ITIL 4 | [su descripción, citada por AWS](https://docs.aws.amazon.com/wellarchitected/latest/change-enablement-in-the-cloud/change-enablement-in-itil4.html) | 2026-11-26 | Por verificar: Verificado solo en su descripción: maximizar los cambios exitosos evaluando su riesgo, autorizándolos y llevando su calendario. Por verificar: la guía de la práctica, de PeopleCert. Fuera de la 0.1.0 hasta verificarla | La autoridad de cambio y los tipos de cambio, cuando entre |
| F-04 | ISACA · COBIT 2019, los objetivos BAI06 (los cambios de TI) y APO10 (los proveedores) | 2019 | [la comparación de ISACA con COBIT 5](https://www.isaca.org/resources/news-and-trends/industry-news/2020/cobit-2019-and-cobit-5-comparison) | 2026-11-26 | Por verificar: Verificado solo en la comparación de ISACA: BAI06 trata de los cambios de TI y APO10 de los proveedores. Por verificar: el texto de cada objetivo. Fuera de la 0.1.0 hasta verificarlo | El gobierno de los cambios y de los proveedores, cuando entre |

## La regulación de la tecnología

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-10 | Superintendencia Financiera de Colombia · Circular Externa 005 de 2019, la computación en la nube | 11 de marzo de 2019; agrega el capítulo VI al título I de la parte I de la Circular Básica Jurídica | [la copia compilada del normograma de Colpensiones](https://normativa.colpensiones.gov.co/colpensiones/docs/circular_superfinanciera_0005_2019.htm) | 2026-11-26 | Verificada: Verificada en la copia compilada del normograma de Colpensiones: la entidad vigilada gestiona el riesgo de la nube en el SARO, pacta en el contrato la capacidad, la disponibilidad, los tiempos de recuperación y el manejo de incidentes, incluye la nube en su plan de continuidad y avisa a la Superintendencia 15 días antes de procesar. Se cita por su nombre, nunca por su texto | El nivel de servicio pactado con un proveedor de nube, en una entidad vigilada de Colombia |
| F-11 | Perú · la norma de la SBS sobre la seguridad de la información y la tecnología |  |  | 2026-11-26 | Por verificar: Por verificar en el sitio de la SBS. Fuera de la 0.1.0 hasta verificarla | La tecnología de una entidad vigilada del Perú, cuando entre |
| F-12 | Brasil · Resolución CMN 4.893 de 2021, la ciberseguridad y la nube | 2021 |  | 2026-11-26 | Por verificar: Por verificar en la fuente primaria del Banco Central do Brasil. Fuera de la 0.1.0 hasta verificarla | La nube en una entidad vigilada de Brasil, cuando entre |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **84 %** de las organizaciones dice que gestionar el gasto en la nube es su mayor reto | [Flexera, 2025 State of the Cloud Report](https://www.flexera.com/about-us/press-center/new-flexera-report-finds-84-percent-of-organizations-struggle-to-manage-cloud-spend) | 2025 | más de 750 profesionales técnicos y directivos de todo el mundo | Verificada: Verificada en el comunicado de Flexera del 19 de marzo de 2025: el 84 % de los encuestados cree que gestionar el gasto en la nube es el mayor reto de la nube para las organizaciones hoy. |
| C-02 | **57 %** dice que su última caída mayor costó más de 100.000 dólares | [Uptime Institute, Annual Global Data Center Survey 2025, citada en su Annual Outage Analysis 2026](https://www.businesswire.com/news/home/20260513289344/en) | 2025 | más de 800 dueños y operadores de centros de datos | Verificada: Verificada en el comunicado del Annual Outage Analysis 2026 de Uptime Institute, del 13 de mayo de 2026: en su encuesta anual de 2025, el 57 % dijo que su caída mayor más reciente costó más de 100.000 dólares. La muestra, en el comunicado de la encuesta del 30 de julio de 2025. |
| C-03 | **1 de cada 5** reporta caídas de más de un millón de dólares, por segundo año seguido | [Uptime Institute, Annual Global Data Center Survey 2025, citada en su Annual Outage Analysis 2026](https://www.businesswire.com/news/home/20260513289344/en) | 2025 | más de 800 dueños y operadores de centros de datos | Verificada: Verificada en el comunicado del Annual Outage Analysis 2026 de Uptime Institute, del 13 de mayo de 2026: por segundo año seguido, 1 de cada 5 reporta costos de más de un millón de dólares. |

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
