# Preguntas frecuentes · Criterio CLO

Las respuestas cortas a lo que suele preguntar quien llega a la familia de contratos y cumplimiento. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hacen Fidel y Constanza?

Procesan lo que la empresa firmó y lo que se obligó a cumplir. Fidel lleva el registro de contratos contra sus documentos, los vencimientos y los preavisos de renovación, las obligaciones con su evidencia, quién firmó con qué facultad y lo pagado contra lo pactado y sus garantías. Constanza lleva la matriz de obligaciones de la organización contra su evidencia, la revisión de las políticas, las normas nuevas con su evaluación y el canal de denuncias con sus plazos.

### ¿Reemplazan al área legal o al oficial de cumplimiento?

No. Preparan el trabajo y lo contrastan contra todos los soportes: qué vence, qué no tiene evidencia, quién firmó sin facultad y qué se pagó por fuera de lo pactado. La decisión —renovar, terminar, cómo se interpreta una cláusula o una norma— la toma siempre una persona.

### ¿Dan opinión jurídica?

No. Ninguno de los dos interpreta una cláusula, califica la validez de un contrato o de una firma, ni dice qué exige una norma. Lo que una obligación exige lo define la organización en su matriz, con la cita de su fuente.

### ¿Qué no hacen nunca?

No deciden renovar ni terminar, no redactan, negocian, firman ni envían contratos, otrosíes ni preavisos, y no declaran el estado del cumplimiento. No responden casos del canal de denuncias ni procesan datos de quién denunció.

## Cómo se usa

### ¿Qué documentos procesan?

Los que el área ya tiene, como estén: el registro de contratos, cada contrato con sus otrosíes, las pólizas y garantías, los certificados de la contraparte, los pagos, la matriz de atribuciones, la matriz de obligaciones, el índice de políticas, el registro normativo y el registro de casos del canal.

### ¿Cómo organizo la carpeta?

Como esté: los agentes la procesan así. Si se arranca de cero, la familia recomienda una carpeta por entidad con su registro, sus políticas, la normativa y el canal; una por contrato, con el contrato, las garantías, la contraparte y la ejecución; y una por periodo de cumplimiento. El setup busca la carpeta raíz de la entidad, la propone y, si dices que sí, la marca con un archivo visible, `_CRITERIO_LEGAL.txt`. Es lo único que escribe entre tus documentos.

### ¿Cuánto tarda el primer resultado?

En los primeros quince minutos, `legal-setup` deja ver el calendario de los contratos: lo que vence, los preavisos que se acercan o que ya pasaron sin decisión y las obligaciones vencidas sin evidencia, con las señales que el motor levantó en el registro, las firmas y los pagos.

### ¿Dónde veo lo que encontraron?

En el reporte de cada comando y en Rostrum, el portal de todas las familias. Allí está lo último que escribió el motor de cada uno, lo que vence con fecha —el preaviso de un contrato con renovación automática, la obligación que vence— y la ruta completa de la carpeta donde trabaja cada agente.

## Cómo se prueba

### ¿Con qué datos se probó?

Con material sintético de cuatro industrias —banca y retail en Colombia, cooperativas y minería en Ecuador— y una entidad de control por país, sin ningún defecto, en la que cualquier señal es una falla. Cada señal de la familia se siembra al menos una vez.

### ¿Cómo se sabe si el motor acertó?

El material trae una clave con lo que se sembró, y el motor no la ve. La prueba compara cada señal por su nombre y su clave: una de más cuenta igual que una de menos. La puerta que lo comprueba corre con cada cambio del repositorio.

### ¿Ya está probada la familia completa?

El motor sí. La extracción del agente sobre cada contrato —partes, valor, fechas, renovación, preaviso, firmantes, otrosíes, garantías y obligaciones— se prueba en la ronda con el agente, que es el paso siguiente. La familia se declara probada con una ronda completa.

## Datos y privacidad

### ¿Mis contratos salen de mi organización?

Se procesan en la plataforma de IA donde corre el agente, como cualquier conversación con ella. Los plugins no se conectan a internet ni nos envían nada.

### ¿Qué queda guardado y dónde?

En tu equipo: las fichas de los contratos y del cumplimiento, los reportes, el registro de cada corrida y el comprobante de aceptación de los términos, que cada versión de la familia pide de nuevo.
