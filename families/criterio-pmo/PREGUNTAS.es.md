# Preguntas frecuentes · Criterio PMO

Las respuestas cortas a lo que suele preguntar quien llega a la familia de gobierno de proyectos. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hacen Vera, Samuel, Alba y Rostrum?

Procesan lo que la oficina de proyectos ya escribió. Vera arma una ficha por proyecto con la cita de cada dato y consolida el portafolio; Samuel lleva los compromisos de cada reunión de un proyecto; Alba contrasta la definición de un producto contra la evidencia de demanda; Rostrum publica el informe para quien no abre una carpeta.

### ¿Reemplazan a la PMO?

No. Preparan borradores de trabajo y dicen qué cambió, qué se contradice y qué ningún documento sostiene. Ningún agente declara el estado de un proyecto: lo declara una persona.

### ¿Qué necesito para usarlos?

Un plan pago de Claude, la aplicación de escritorio si los documentos viven en tu equipo, y una carpeta con la documentación como esté. Una carpeta desordenada es el caso normal.

### ¿Cómo organizo la carpeta?

Como esté: los agentes la procesan así, y las pruebas lo comprueban con cuatro disposiciones distintas. Si se arranca de cero, la familia recomienda una carpeta por proyecto y una por producto, cada una con su código al inicio, y adentro cuatro carpetas: gobierno, plan, seguimiento y reuniones para un proyecto; definición, descubrimiento, métricas y decisiones para un producto. El detalle está en el README de la familia.

## Cómo se prueba

### ¿Con qué datos se probó?

Con datos de prueba de cuatro industrias —entidades financieras (bancos y cooperativas), retail y minería de Suramérica—, construidos para ser más exigentes que la documentación habitual de esas organizaciones: más de 500 documentos por ronda en Markdown, Word, PDF, Excel y CSV; contradicciones entre documentos; compromisos movidos hasta seis veces; hitos declarados cumplidos sin acta; proyectos en silencio; entregas de proveedor sin evidencia; y en cada industria un proyecto sano que no debe levantar ninguna alerta.

### ¿Cómo se sabe si un agente acertó?

Cada ronda trae una clave con lo que el material contiene, derivada de los hechos que el generador escribió. Ningún agente la ve: cada sesión se audita y se publica cuántas veces se leyó (cero en todas). Cada cifra se publica con su conteo y su margen de confianza del 95 %.

### ¿Dónde está la evidencia?

En el repositorio, en `tests/evidencias/`: lo que mostró cada comando en cada ronda, la clave, la calificación, y cada defecto con su origen, el commit que lo corrige y la ronda que lo verificó. La página de la familia la resume.

### ¿Se ha usado ya en una organización?

Todavía no sobre la documentación de una organización concreta. No hace falta para que la familia avance: Criterio desarrolla, prueba y libera cada versión. Si tu PMO la prueba sobre sus documentos y quiere compartir lo que encontró, abre un issue en el repositorio; lo que traiga entra en un incremento con su prueba.

## Datos y privacidad

### ¿Mis documentos salen de mi organización?

Se procesan en la plataforma de IA donde corre el agente, como cualquier conversación con ella. Los plugins no se conectan a internet ni nos envían nada.

### ¿Qué queda guardado y dónde?

En tu equipo: las fichas, los informes, el registro de cada corrida y el comprobante de aceptación de los términos. Nada de eso viaja a ninguna parte.

### ¿Recogen estadísticas de uso?

No. Hoy el único canal de vuelta es el que tú eliges: un issue en GitHub. Compartir hallazgos para mejorar la familia será siempre una pregunta, y nunca se envía nada sin un sí.

## Versiones y licencia

### ¿Es una versión estable?

Sí. Lo dice la evidencia, no el número (decisión 0020): una versión es estable cuando su ronda más reciente tiene el piso del margen de confianza del 95 % en 95 % o más en cada agente —la precisión y la cobertura de Vera, los compromisos de Samuel, la cobertura de Alba— y ningún proyecto de control levanta una alerta; si no, es de laboratorio. Cada número entero tiene diez versiones: la PMO pasó la 0.9, y su próxima versión, con telecomunicaciones y logística, es la 1.0.

### ¿Cuánto cuesta?

Nada. Es código abierto bajo Apache 2.0: úsalo en tu organización sin pedir permiso y adáptalo. La contribución en la página es voluntaria y no desbloquea nada.

### ¿Qué acepto antes de usarlo?

Los términos de cada versión. El agente los muestra, pide un sí explícito y deja un comprobante en Markdown y PDF con la huella SHA-256 de los términos. Cada versión nueva se acepta de nuevo.

## Ayuda

### ¿Cómo reporto un error?

Con un issue en el repositorio y el documento que lo demuestra, sin datos reales de nadie. Las fallas de seguridad van por el reporte privado de GitHub, nunca en un issue público.

### ¿Puedo construir un agente para otra función?

Sí. El repositorio explica el método y los criterios de aceptación, y las familias de finanzas y legal están declaradas y sin construir: el agente de una función lo debe escribir quien conoce el trabajo.
