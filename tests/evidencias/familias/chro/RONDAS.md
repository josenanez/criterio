# criterio-chro · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca-co](ronda-1/banca-co/) | banca · CO | candido, norma | 28 de 29 · 0 de más | 0 de 2 | 8.68 M |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | candido, norma | 1 de 1 · 2 de más | 0 de 2 | 7.81 M |
| ronda-2 | [banca-co-verificacion](ronda-2/banca-co-verificacion/) | banca · CO | candido, norma | 29 de 29 · 0 de más | 2 de 2 | 8.79 M |
| ronda-2 | [control-co-verificacion](ronda-2/control-co-verificacion/) | control · CO | candido, norma | 1 de 1 · 0 de más | 2 de 2 | 7.95 M |
| ronda-3 | [control-pe](ronda-3/control-pe/) | control · PE | candido, norma | 1 de 1 · 0 de más | 210 de 265 | 4.70 M |
| ronda-3 | [control-pe-verificacion](ronda-3/control-pe-verificacion/) | control · PE | candido, norma | 1 de 1 · 0 de más | 265 de 265 | 4.85 M |
| ronda-3 | [retail-mx](ronda-3/retail-mx/) | retail · MX | candido, norma | 22 de 22 · 4 de más | 305 de 305 | 5.37 M |
| ronda-3 | [tecnologia-cl](ronda-3/tecnologia-cl/) | tecnologia · CL | candido, norma | 20 de 20 · 0 de más | 323 de 323 | 5.55 M |
| ronda-4 | [banca-co](ronda-4/banca-co/) | banca · CO | candido, norma | 29 de 29 · 0 de más | 481 de 481 | 6.37 M |
| ronda-4 | [control-co](ronda-4/control-co/) | control · CO | candido, norma | 1 de 1 · 0 de más | 364 de 364 | 4.99 M |
| ronda-5 | [retail-ec](ronda-5/retail-ec/) | retail · EC | candido, norma | 22 de 22 · 0 de más | 305 de 305 | 8.98 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CHRO-1 | 1 | banca-co | la clave de respuestas | La clave daba por «conocimiento» todo requisito atado a un elemento del estándar, también los que el estándar pone entre las destrezas, y por «otro» uno que el perfil decía de experiencia. Norma los registró bien; la clave los calificó como mal. | El tipo de cada requisito sale de la lista del estándar en que está su elemento —destreza o conocimiento—, y el perfil agrupa sus requisitos por tipo, así que el documento lo dice y no hay que adivinarlo. | dfad78d9 | corregido y verificado |
| CHRO-2 | 1 | banca-co | la clave de respuestas | La clave dejaba fuera lo que Cándido registró como pide cv-record: la tarjeta profesional como evidencia del requisito que atiende, y la fotografía en la hoja de vida que la anuncia y en su archivo. | La clave lleva la evidencia del soporte de la certificación y la fotografía donde llegó. | dfad78d9 | corregido y verificado |
| CHRO-3 | 1 | banca-co | los datos de prueba | La política de selección no decía cada cuánto se revisa un perfil, y el perfil solo decía «cada 12 meses» como próxima revisión. Norma no supuso un plazo, como debe, y la revisión vencida del perfil del contador quedó sin levantar. | La política de cada entidad dice cada cuánto se revisa un perfil; el setup lo toma de ahí. | dfad78d9 | corregido y verificado |
| CHRO-4 | 1 | control-co | las instrucciones del agente | Dos alarmas falsas en el control: un diploma escaneado en imagen se tomó por una fotografía, porque la instrucción decía que una imagen no se abre. El título quedó sin soporte y llegó una «fotografía». | Una imagen cuyo nombre dice que es un documento —diploma, acta, certificado, tarjeta— es un soporte escaneado: se abre solo para confirmarlo y se cita como soporte; cualquier otra imagen es una fotografía, no se abre y se excluye. El diploma del material ahora se ve. | dfad78d9 | corregido y verificado |
| CHRO-5 | 1 | control-co | las instrucciones del agente | cv-record no decía cómo se numeran las afirmaciones ni si el soporte de una certificación es también la evidencia de su requisito, y Cándido lo hizo de una forma en banca y de otra en el control. | Las afirmaciones se numeran en el orden en que la hoja de vida las hace, y el requisito que atiende una afirmación con soporte lleva su evidencia en ese soporte; el ejemplo del skill lo muestra. | dfad78d9 | corregido y verificado |
| CHRO-6 | 2 | control-co-verificacion | el arnés de prueba | Norma registró el elemento del estándar de cada requisito por su nombre, como lo permite profile-record y lo resuelve el motor, y el arnés solo aceptaba el identificador. | Al calificar, un nombre de elemento se traduce al identificador de la ocupación del perfil, con el mismo estándar de la entidad. Se volvió a calificar la corrida, sin repetir comandos. | db55efbe | corregido y verificado |
| CHRO-7 | 2 | banca-co-verificacion | las instrucciones del agente | De una certificación que la hoja de vida afirma sin soporte, Cándido tomó el vencimiento y la evidencia de la hoja de vida en la verificación y no en la primera ronda: cv-record decía que el vencimiento sale del soporte y no decía qué hacer cuando no llega. | Sin soporte, el vencimiento y la evidencia de la certificación salen de la línea de la hoja de vida que la afirma; la afirmación sigue sin soporte y lo dice su señal. La clave lo sigue, y la verificación se volvió a calificar sin repetir comandos. La ronda 4, sobre la misma banca, lo verificó: la certificación sin soporte de CAN-111 llegó con su vencimiento y su evidencia en la línea de la hoja de vida. | 50c030a1 | corregido y verificado |
| CHRO-8 | 3 | retail-mx | los datos de prueba | La política de selección de las tres entidades que usan O*NET no decía desde qué importancia una destreza es exigible. Norma propuso 3,0 en México y Chile, y en México cuatro destrezas quedaron como faltantes de más; en Perú se detuvo sin inventarlo y no armó los perfiles. | La política de cada entidad con O*NET dice el umbral —3,5 sobre 5— y el setup lo toma de ahí. La verificación en Perú armó los perfiles con ese umbral, sin señales de más. | c610e396 | corregido y verificado |
| CHRO-9 | 3 | tecnologia-cl | el arnés de prueba | Cándido citó la evidencia de cada requisito por la sección de la hoja de vida («Perfil profesional»), con la frase, y el arnés solo aceptaba la cita por la página («p. 1»): las dos señalan lo mismo. | Al calificar, la sección se busca en el texto de esa página del PDF. Chile se volvió a calificar sin repetir comandos. | a9084b43 | corregido y verificado |
