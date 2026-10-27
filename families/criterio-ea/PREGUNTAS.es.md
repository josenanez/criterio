# Preguntas frecuentes · Criterio EA

Las respuestas cortas a lo que suele preguntar quien llega a la familia de la oficina de dirección. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hace Ofelia?

Prepara el trabajo de la oficina del ejecutivo. Pone la semana al lado de las sesiones y los compromisos, arma el paquete de la próxima sesión de cada órgano con la ficha de cada decisión, levanta el borrador del acta desde las notas, sigue los compromisos de cada acta y dice qué correo espera respuesta.

### ¿Reemplaza a quien asiste al ejecutivo?

No. Prepara y contrasta: qué reuniones se cruzan, qué sesión no tiene material, qué acta sigue sin firmar, qué acuerdo no tiene responsable o fecha. Lo que se acepta, se envía y se prioriza lo decide siempre una persona.

### ¿Recomienda qué decidir?

No. Cada decisión llega con las opciones que traen los documentos, en el orden en que las traen, con la evidencia de cada una, lo que falta saber y la fecha que fija el plazo. El motor rechaza una ficha que ordene las opciones o marque una como recomendada.

### ¿Qué no hace nunca?

No envía, no agenda, no acepta ni mueve nada. No edita actas, agendas ni correos originales, no declara cumplido un compromiso sin un documento que lo sostenga y no evalúa a una persona ni a un área.

## Cómo se usa

### ¿Qué documentos procesa?

Los que la oficina exporta: la agenda en .ics, los correos guardados como archivo, y la convocatoria, el material, las notas y el acta firmada de cada sesión. No se conecta al buzón ni al calendario: una conexión directa es otra decisión, con su revisión de privacidad.

### ¿Cómo organizo la carpeta?

Como esté: Ofelia la procesa así. Si se arranca de cero, la familia recomienda una carpeta por ejecutivo con su referencia, su agenda, su correspondencia, los borradores y una carpeta por sesión de cada órgano. El setup busca la carpeta de la oficina, la propone y, si dices que sí, la marca con un archivo visible, `_CRITERIO_DIRECCION.txt`. Entre tus documentos, además de esa marca, solo escribe sus borradores, en `90-borradores/`.

### ¿Cuánto tarda el primer resultado?

En los primeros quince minutos, `ea-setup` deja ver la agenda de las próximas dos semanas con sus cruces, las sesiones sin material y las que siguen sin acta.

### ¿En qué países sirve?

En cualquiera. Ofelia no procesa facturas ni normas, sino la agenda, las actas y el correo, así que el país de la oficina es un dato y no un límite. Lo que sí cambia de una oficina a otra es cómo exporta su proveedor de calendario y de correo: eso es lo siguiente que se prueba.

### ¿Dónde veo lo que encontró?

En el reporte de cada comando, en la carpeta de su estado. Su informe no se publica en Rostrum salvo que la configuración lo diga.

## Cómo se prueba

### ¿Con qué datos se probó?

Con material sintético de dos países —Colombia y Ecuador—: la oficina de una presidencia y la de una gerencia general con defectos sembrados, y una oficina de control por país, sin ningún defecto, en la que cualquier señal es una falla. Cada señal se siembra al menos una vez, y el material prueba además las reglas de la operación real: una reunión en otra zona horaria que solo se cruza después del cambio de hora, una agenda vieja que no da cruces, un borrador puesto en `40-acta/` y una carpeta excluida.

### ¿Cómo se sabe si el motor acertó?

El material trae una clave con lo que se sembró, y el motor no la ve. La prueba compara cada señal por su nombre y su clave: una de más cuenta igual que una de menos. La puerta que lo comprueba corre con cada cambio del repositorio.

### ¿Ya está probada la familia?

El motor sí, contra la clave de las cuatro oficinas. La extracción de la agente —los acuerdos, los compromisos y las decisiones de cada acta, y lo que pide cada correo— se prueba en la ronda con la agente sobre las mismas cuatro oficinas, publicada con cada salida, su costo y su calificación. Nada ha corrido todavía sobre la oficina de un ejecutivo real.

## Datos y privacidad

### ¿La agenda y los correos salen de mi organización?

Se procesan en la plataforma de IA donde corre la agente, como cualquier conversación con ella. El plugin no se conecta a internet ni nos envía nada. La oficina del ejecutivo es de lo más sensible que tiene una organización: por eso procesa exportaciones y no cuentas, y respeta las carpetas que se excluyan.

### ¿Qué queda guardado y dónde?

En tu equipo: las fichas de las sesiones y de la correspondencia, los reportes, los borradores, el registro de cada corrida y el comprobante de aceptación de los términos, que cada versión pide de nuevo.
