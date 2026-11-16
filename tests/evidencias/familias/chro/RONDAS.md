# criterio-chro · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca-co](ronda-1/banca-co/) | banca · CO | candido, norma | 28 de 29 · 0 de más | 0 de 2 | 8.68 M |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | candido, norma | 1 de 1 · 2 de más | 0 de 2 | 7.81 M |
| ronda-2 | [banca-co-verificacion](ronda-2/banca-co-verificacion/) | banca · CO | candido, norma | 29 de 29 · 0 de más | 2 de 2 | 8.79 M |
| ronda-2 | [control-co-verificacion](ronda-2/control-co-verificacion/) | control · CO | candido, norma | 1 de 1 · 0 de más | 2 de 2 | 7.95 M |

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
| CHRO-7 | 2 | banca-co-verificacion | las instrucciones del agente | De una certificación que la hoja de vida afirma sin soporte, Cándido tomó el vencimiento y la evidencia de la hoja de vida en la verificación y no en la primera ronda: cv-record decía que el vencimiento sale del soporte y no decía qué hacer cuando no llega. | Sin soporte, el vencimiento y la evidencia de la certificación salen de la línea de la hoja de vida que la afirma; la afirmación sigue sin soporte y lo dice su señal. La clave lo sigue, y la verificación se volvió a calificar sin repetir comandos. | 50c030a1 | corregido, por verificar |
