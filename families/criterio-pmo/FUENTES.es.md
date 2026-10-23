# criterio-pmo · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0005](../../docs/decisions/0005-scope-pmo-only.md), regla 1).

## El rol

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | PMI · The Standard for Portfolio Management | Cuarta edición, 2017 | [pmi.org](https://www.pmi.org/standards/for-portfolio-management) | 2026-10-23 | Verificada: Se consultó la ficha del estándar en el PMI: título, edición y año. Define la gestión de un portafolio de proyectos, programas y otro trabajo para que sirva al plan estratégico de la organización | El marco del rol de Vera, quien responde por el portafolio |
| F-02 | PMI · PMBOK Guide y The Standard for Project Management | Octava edición, noviembre de 2025 | [pmi.org](https://www.pmi.org/standards/pmbok) | 2026-10-23 | Verificada: Se consultó la ficha de la guía en el PMI: octava edición, publicada en noviembre de 2025, junto con The Standard for Project Management | El marco del rol de Samuel, quien responde por un proyecto |
| F-03 | AIPMM · The Guide to the Product Management and Marketing Body of Knowledge (ProdBOK) | — | [aipmm.com](https://aipmm.com/bok/) | 2026-10-23 | Verificada: Se consultó la ficha de la guía en la AIPMM: título, editor y alcance —el marco de la gestión de producto para llevar productos y servicios al mercado—. La ficha no dice la edición | El marco del rol de Alba, quien define qué se construye |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **73 %** de sobrecosto medio en proyectos de TI; el 18 % se pasa en más de la mitad | [Flyvbjerg, Budzier, Aaen, Keil y Zottoli, The Uniqueness of IT Cost Risk, Project Management Journal](https://journals.sagepub.com/doi/10.1177/87569728251340590) | 2026 | 11.011 proyectos de 23 tipos en 126 países; 5.360 de TI | Verificada: Tabla 1: media de 1,73 para TI (N = 5.360); tabla 2: 18,26 % con sobrecosto mayor al 50 %. Publicado en línea el 7 de julio de 2025, en el volumen de 2026 |
| C-02 | **31 %** de los proyectos complejos no alcanza los beneficios que se propuso | [PMI, Pulse of the Profession 2026](https://www.pmi.org/about/press-media/2026/pulse-why-complex-projects-fail-best-practices-are-not-enough-system-thinking) | 2026 | No indicada en la nota de prensa | Verificada: La nota de prensa del PMI dice «casi un tercio (31 %) de los proyectos complejos no logra el alcance completo de sus beneficios», más del doble que los proyectos en general. La muestra que publicábamos (2.534 encuestados, 35 países) no está en la nota: se quitó |
| C-03 | **1 de 3** proyectos no tiene línea base, y la mitad de las organizaciones no tiene indicadores en tiempo real | [Wellingtone, The State of Project Management 2026](https://wellingtone.co.uk/publications/state-of-project-management-research/) | 2026 | Cientos de participantes de más de 150 organizaciones | Verificada: Se consultó el informe: un tercio de los proyectos sin línea base y la mitad de las organizaciones sin indicadores en tiempo real. El 22 % que planifica en Excel, que publicábamos, no se pudo confirmar en el texto: se quitó |
| C-04 | **72 %** dedica medio día o más cada mes solo a consolidar informes a mano | [Wellingtone, The State of Project Management 2026](https://wellingtone.co.uk/publications/state-of-project-management-research/) | 2026 | Cientos de participantes de más de 150 organizaciones | Verificada: Lo dicen el informe y su nota de prensa del 16 de marzo de 2026 |

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

