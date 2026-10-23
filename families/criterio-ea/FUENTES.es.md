# criterio-ea · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0012](../../docs/decisions/0012-scope-asistente-ejecutivo.md), regla 1).

## El rol

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | O*NET · 43-6011.00 Executive Secretaries and Executive Administrative Assistants | Datos de 2026 (O*NET OnLine, sitio actualizado el 6 de octubre de 2026) | [onetonline.org](https://www.onetonline.org/link/summary/43-6011.00) | 2026-10-23 | Verificada: Se consultaron las tareas de la ocupación en O*NET OnLine, del Departamento de Trabajo de los Estados Unidos: llevar la agenda del ejecutivo, preparar el orden del día de las reuniones, abrir, clasificar y distribuir la correspondencia, responder la rutinaria y reunir información para el ejecutivo | El marco del rol de Ofelia: de aquí sale lo que hace y, por la frontera con el jefe de gabinete, lo que no hace (ADR 0012) |

## Los formatos que procesa el motor

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-02 | IETF · RFC 5545, Internet Calendaring and Scheduling Core Object Specification (iCalendar) | Septiembre de 2009, Proposed Standard; actualizada por las RFC 5546, 6868, 7529, 7953, 7986, 9073, 9074 y 9253 | [rfc-editor.org](https://rfc-editor.org/info/rfc5545) | 2026-10-23 | Verificada | La agenda exportada en .ics: los eventos, sus repeticiones y sus zonas horarias, que calcula el código |
| F-03 | IETF · RFC 5322, Internet Message Format | Octubre de 2008, Draft Standard; actualizada por la RFC 6854 | [rfc-editor.org](https://rfc-editor.org/info/rfc5322) | 2026-10-23 | Verificada | Los correos guardados como archivo: de quién, para quién, la fecha y el hilo, que procesa el código |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **57 %** del tiempo de trabajo se va en comunicar —reuniones, correo y chat— y el 43 % en crear | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?»](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) | 2023 | Datos agregados de uso de Microsoft 365, no la encuesta; el informe no da el tamaño de esa muestra | Verificada: Lo dice el informe del 9 de mayo de 2023 en microsoft.com: el empleado promedio pasa el 57 % de su tiempo comunicando y el 43 % creando, según las señales de productividad de Microsoft 365 |
| C-02 | **55 %** dice que los próximos pasos al final de una reunión no quedan claros | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?»](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) | 2023 | 31.000 trabajadores de tiempo completo o independientes en 31 mercados | Verificada: Lo dice el mismo informe, entre las ineficiencias de las reuniones |
| C-03 | **68 %** no tiene suficiente tiempo de concentración sin interrupciones en su jornada | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?»](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) | 2023 | 31.000 trabajadores de tiempo completo o independientes en 31 mercados | Verificada: Lo dice el mismo informe |
| C-04 | **72 %** del tiempo de trabajo de un CEO se va en reuniones | [Porter y Nohria, «How CEOs Manage Time», Harvard Business Review](https://www.mckinsey.com/about-us/new-at-mckinsey-blog/how-do-ceos-manage-their-time-the-winners-of-the-60th-annual-hbr-mckinsey-award-explain) | 2018 | 27 CEO, más de 60.000 horas registradas | Por verificar: McKinsey confirma la muestra; el 72 % solo se ha visto en fuentes secundarias. No se publica hasta verlo en el artículo |

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
