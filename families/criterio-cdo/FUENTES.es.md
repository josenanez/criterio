# criterio-cdo · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0034](../../docs/decisions/0034-la-familia-cdo.md), regla 1).

## Los marcos de la gestión de datos

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | DAMA International · DAMA-DMBOK, Data Management Body of Knowledge, segunda edición | Segunda edición, vigente; revisión lanzada en 2024 y proyecto de tercera edición desde 2025 | [dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/) | 2026-11-24 | Verificada: Verificada en dama.org: la segunda edición es la vigente. Libro de pago: se citan sus áreas por su nombre, nunca su texto. Por verificar en el libro: el número de áreas y el lugar del gobierno | Las tres áreas que trabaja la familia: el gobierno de datos (Custodia), la calidad y los metadatos con el linaje (Ariadna) |
| F-02 | Comité de Supervisión Bancaria de Basilea · BCBS 239, Principios para la agregación eficaz de datos de riesgo y la presentación de informes de riesgo | Enero de 2013, vigente; informe de avance del 28 de noviembre de 2023 | [bis.org/publ/bcbs239](https://www.bis.org/publ/bcbs239.pdf) · [informe de avance de 2023](https://www.bis.org/bcbs/publ/d559.htm) | 2026-11-25 | Verificada: Catorce principios en cuatro grupos. Verificados en el documento: el gobierno y la infraestructura (1 y 2), la capacidad de agregar los datos de riesgo (3 a 6: exactitud e integridad, completitud, oportunidad y adaptabilidad) y la presentación de informes (desde el 7: exactitud, exhaustividad, claridad y utilidad). Se dirigen primero a los bancos sistémicos (párrafo 13), y los supervisores deberían aplicarlos a los sistémicos locales tres años después de su designación (párrafo 15). Por verificar: los títulos de los principios 10 a 14 | La cifra de riesgo que llega a la junta, contra su fuente y su corte, en una entidad financiera: las señales de las cifras de Ariadna |
| F-03 | ISO/IEC 25012 · Modelo de calidad de datos (SQuaRE) | Primera edición, diciembre de 2008 | [IEC webstore](https://webstore.iec.ch/publication/11246) | 2026-11-25 | Verificada: Verificada en la tienda de la IEC y en la muestra oficial de la norma: quince características desde dos puntos de vista, el inherente al dato y el que depende del sistema. Norma de pago. Por verificar: el nombre de cada característica y si sigue vigente; su página en iso.org no respondió | La característica de calidad con que la organización escribe cada regla |
| F-04 | ISO 8000 · Calidad de datos | La parte 1 de 2011 está retirada y la reemplaza la de 2022 | [iso.org](https://www.iso.org/standard/81745.html) | 2026-11-24 | Por verificar: Las partes 8 y 61, sin verificar. Fuera de la 0.1.0 hasta verificar sus partes vigentes | La calidad de los datos maestros, cuando entre |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **2 de 31** bancos sistémicos globales cumplían todos los principios de agregación de datos de riesgo en la evaluación del Comité de Basilea | [Comité de Supervisión Bancaria de Basilea, Progress in adopting the Principles for effective risk data aggregation and risk reporting](https://www.bis.org/bcbs/publ/d559.htm) | 2023 | 31 bancos sistémicos globales designados entre 2011 y 2021 | Verificada: Verificada en el informe del 28 de noviembre de 2023: de los 31 bancos evaluados, solo dos cumplen plenamente todos los principios, y ningún principio está plenamente aplicado en todos los bancos. |
| C-02 | **3 %** de las evaluaciones de calidad de datos alcanzaron el nivel aceptable, 97 de cada 100 registros sin errores | [Nagle, Redman y Sammon, Assessing data quality: A managerial call to action, Business Horizons, vol. 63, n.º 3](https://research.ucc.ie/en/publications/assessing-data-quality-a-managerial-call-to-action/) | 2020 | 75 evaluaciones de calidad de datos recogidas durante dos años | Verificada: Verificada en el resumen del artículo, publicado el 1 de mayo de 2020. |
| C-03 | **47 %** de los registros recién creados tiene al menos un error crítico | [Nagle, Redman y Sammon, Assessing data quality: A managerial call to action, Business Horizons, vol. 63, n.º 3](https://research.ucc.ie/en/publications/assessing-data-quality-a-managerial-call-to-action/) | 2020 | 75 evaluaciones de calidad de datos recogidas durante dos años | Verificada: Verificada en el resumen del artículo, publicado el 1 de mayo de 2020: en promedio. |

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
