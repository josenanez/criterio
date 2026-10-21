# criterio-clo · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0009](../../docs/decisions/0009-scope-clo.md), regla 1).

## Marcos de referencia

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | ISO 37301:2021 · Sistemas de gestión del cumplimiento — Requisitos con orientación para su uso | Edición 1, abril de 2021; confirmada en su revisión sistemática de 2026 | [iso.org](https://www.iso.org/standard/75080.html) | 2026-10-20 | Verificada: Se consultó la ficha de la norma en ISO: título, edición, estado y alcance —establecer, desarrollar, implementar, evaluar, mantener y mejorar un sistema de gestión del cumplimiento—. Se usa como modelo de la matriz de obligaciones: cada obligación con su fuente, su responsable y su evidencia. No se transcribe su contenido | El modelo de la matriz de obligaciones que procesa Constanza; ninguna obligación sale de aquí: las define la organización |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **8,6 %** del valor de los contratos se erosiona en promedio por una gestión contractual deficiente; los mejores, poco más de 3 %, los peores, más de 20 % | [World Commerce & Contracting con Deloitte](https://www.deloitte.com/us/en/services/tax/articles/contract-management-lifecycle-insights.html) | 2022 | Más de 1.200 organizaciones | Verificada: Actualización de 2022 de la investigación de 2014, que daba 9,2 %; la nota de Deloitte dice «más de 1.200 organizaciones», no un número exacto |
| C-02 | **90 %** de las organizaciones tiene dificultad para encontrar sus propios contratos | [EY Law y Harvard Law School Center on the Legal Profession](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) | 2021 | 1.000 líderes de contratación, dentro de una investigación de más de 2.000 personas en 22 países, enero de 2021 | Verificada: Página 7 del informe |
| C-03 | **19.000** contratos al año gestiona en promedio el equipo de contratación de una organización grande | [EY Law y Harvard Law School Center on the Legal Profession](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) | 2021 | 1.000 líderes de contratación, enero de 2021 | Verificada: Página 14 del informe |

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
