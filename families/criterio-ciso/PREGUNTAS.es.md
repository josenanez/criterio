# Preguntas frecuentes · Criterio CISO

Las respuestas cortas a lo que suele preguntar quien llega a la familia de la seguridad de la información. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hacen Alexis, Guillermo y Amparo?

Alexis pone cada control de la declaración de aplicabilidad al lado de la evidencia de que operó, y dice qué revisión de accesos, qué evaluación de un tercero crítico y qué aceptación de riesgo venció. Guillermo pone cada vulnerabilidad del escáner al lado del plazo de su severidad, del catálogo KEV de lo que se explota y del escaneo que prueba su cierre. Amparo pone cada incidente al lado del plazo de contención de su severidad y de cada notificación que pide la matriz, y cada prueba de continuidad al lado de su calendario.

### ¿Reemplazan al responsable de seguridad?

No. Procesan y contrastan. Aceptar un riesgo, aprobar una excepción, notificar a un supervisor y declarar cumplido un control lo decide siempre una persona.

### ¿Certifican a mi organización contra la ISO/IEC 27001?

No. No califican la madurez ni certifican contra ninguna norma. Toman los controles de la declaración de aplicabilidad de la organización, con el número y el nombre que ella les da, y dicen cuál no tiene la evidencia de que operó.

### ¿Qué no hacen nunca?

No corren un escaneo, no se conectan a un sistema, a una consola ni a internet, no aceptan un riesgo, no aprueban una excepción, no notifican a nadie, no ejecutan una prueba ni una restauración, y no abren credenciales, llaves ni respaldos.

## Cómo se usa

### ¿Se conectan a mi escáner o a mi SIEM?

No. Procesan lo que la organización exporta y deja en la carpeta: las exportaciones del escáner en CSV o Excel, el catálogo KEV como lo descarga, los informes y los registros. Una conexión directa sería otra decisión, con su revisión de seguridad.

### ¿Qué escáner sirve?

Cualquiera que exporte en CSV o Excel. Guillermo reconoce las cabeceras de uso común —host, CVE, severity, CVSS— y, si no las reconoce, pregunta qué columna trae cada dato y lo deja en la configuración. Los formatos propios de Tenable, Qualys, Rapid7 y Microsoft Defender entran en un incremento posterior, cada uno desde su fuente.

### ¿De dónde salen los plazos?

De la política de la organización. En el setup, el agente la lee y propone los días de corrección de cada severidad o las horas de contención, con la página de donde salen, y la persona confirma. Si la política no los dice, se le preguntan. Ningún plazo lo pone el agente.

### ¿Qué es el catálogo KEV?

La lista de CISA de las vulnerabilidades que se están explotando, con su fecha de corrección. Guillermo la cruza con lo abierto. La fecha la fija una directiva para las agencias federales de los Estados Unidos: para la organización es una referencia, y su plazo sigue siendo el de su política.

### ¿Cómo sabe que una notificación se hizo tarde?

Por la hora de su constancia —el radicado, el correo enviado, el acuse— contra el plazo de la matriz de la organización, contado desde la hora de la detección que dice el informe del incidente.

### ¿Cuánto tarda el primer resultado?

Cada comando de instalación pide unos quince minutos: mira la carpeta, dice qué no va a abrir, hace las preguntas que ningún documento responde y muestra el primer reporte.

### ¿En qué países sirve?

La familia se define sobre estándares internacionales, no sobre la ley de cada país: sirve igual en cualquiera de los países del registro. La regulación de cada país —la circular del supervisor, la ley de datos— entra a la matriz de notificaciones de la organización.

## Los datos

### ¿Abren mis credenciales o mis respaldos?

No. Un archivo de llaves, una bóveda de contraseñas, un volcado de base de datos, un archivo comprimido o uno cuyo nombre dice que es un secreto queda excluido por omisión. El reporte dice cuáles excluyó, para que la persona los saque de la carpeta.

### ¿Se publican las vulnerabilidades en Rostrum?

No, salvo que la configuración de Guillermo lo diga. Un informe de vulnerabilidades abiertas es un mapa para un atacante.

### ¿Dónde se procesan mis documentos?

En la infraestructura de la plataforma de IA sobre la que corre el agente, no solo en tu equipo. Confirma que sea admisible bajo tus políticas antes de apuntarla a material confidencial.

## El estado

### ¿Está lista para usar?

Se puede instalar, y es de laboratorio, en su versión 0.1.0: el motor está probado sobre material sintético de banca, retail, salud y tecnología, con una clave que no ve y dos entidades de control. La ronda con los tres agentes es el siguiente paso.

### ¿Es estable?

No todavía. Una familia se declara estable cuando su ronda con los agentes pasa el piso del margen del 95 % en señales y en datos.
