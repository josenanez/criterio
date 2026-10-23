# Preguntas frecuentes · Criterio CFO

Las respuestas cortas a lo que suele preguntar quien llega a la familia de cierre, control y reporte. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hacen Clara y Tomás?

Procesan lo que la función financiera ya tiene. Clara, contralora, prepara el cierre mensual con su checklist y su evidencia, las conciliaciones bancarias y de cuentas, cada factura electrónica contra su registro y el paquete para el auditor. Tomás, FP&A, pone el presupuesto aprobado al lado de lo ejecutado y lo comprometido, proyecta el cierre del año y prepara el material del comité de presupuesto.

### ¿Reemplazan al contralor o al equipo de presupuesto?

No. Preparan el trabajo y lo contrastan contra todos los soportes: qué no cuadra, qué no tiene soporte y qué se reporta distinto de lo que dicen los documentos. El estado del cierre lo declara el contralor y el del presupuesto, el responsable del área.

### ¿Qué no hacen nunca?

No registran ni corrigen asientos, no presentan declaraciones ni reportes a supervisores, no firman y no declaran el estado del cierre ni del presupuesto. No opinan sobre deducibilidad, tarifas ni tratamientos NIIF, y no dicen de memoria una tarifa, un plazo ni el valor de una unidad tributaria.

### ¿Para qué marco normativo sirven?

La primera versión trabaja con las NIIF adoptadas en Colombia y Ecuador, y con la factura electrónica de la DIAN y del SRI procesada desde su fuente técnica oficial. Cada fuente está en el repositorio con su versión, su enlace y la fecha en que se consultó.

## Cómo se usa

### ¿Qué documentos procesan?

Los que la función financiera ya produce, como estén: el balance de comprobación y el libro mayor exportados del ERP, los auxiliares y extractos de bancos, las facturas electrónicas en XML, el checklist del cierre, los requerimientos del auditor, el presupuesto aprobado y sus versiones, las órdenes de compra y las actas del comité de presupuesto.

### ¿Necesito cambiar mi ERP?

No. Procesan las exportaciones en Excel o CSV que el ERP ya produce. Ninguno de los dos se conecta al ERP ni escribe en él.

### ¿Cómo organizo la carpeta?

Como esté: los agentes la procesan así. Si se arranca de cero, la familia recomienda una carpeta por entidad y, adentro, una por periodo —contabilidad, bancos, facturación, soportes y auditoría— y una por año de presupuesto —aprobado, compromisos, proyecciones y actas—. El setup busca la carpeta raíz de la entidad, la propone y, si dices que sí, la marca con un archivo visible, `_CRITERIO_FINANZAS.txt`. Es lo único que escribe entre tus documentos.

### ¿Cuánto tarda el primer resultado?

En los primeros quince minutos, `finance-setup` deja ver el estado del cierre del periodo: cada tarea del checklist con su evidencia o sin ella, y las señales que el motor levantó en el cuadre, los bancos, las cuentas y las facturas.

### ¿Dónde veo lo que encontraron?

En el reporte de cada comando y en Rostrum, el portal de todas las familias. Allí está lo último que escribió el motor de cada uno, lo que vence con fecha y la ruta completa de la carpeta donde trabaja cada agente.

## Cómo se prueba

### ¿Con qué datos se probó?

Con material sintético de cuatro industrias —banca y retail en Colombia, cooperativas y minería en Ecuador— y una entidad de control por país, sin ningún defecto, en la que cualquier señal es una falla. Las facturas se generan con la estructura oficial de cada país, y cada señal de la familia se siembra al menos una vez.

### ¿Cómo se sabe si el motor acertó?

El material trae una clave con lo que se sembró, y el motor no la ve. La prueba compara cada señal por su nombre y su clave: una de más cuenta igual que una de menos. La puerta que lo comprueba corre con cada cambio del repositorio.

### ¿Ya está probada la familia completa?

El motor sí. La extracción del agente sobre los documentos escritos —lo que solo traen las actas, los correos y las cartas del auditor— pasó la ronda completa con el agente sobre las seis entidades: 45 de 45 señales sin una de más y 48 de 49 datos de las fichas. La familia se declara probada; nada ha corrido todavía sobre los documentos de una organización.

## Datos y privacidad

### ¿Mis documentos salen de mi organización?

Se procesan en la plataforma de IA donde corre el agente, como cualquier conversación con ella. Los plugins no se conectan a internet ni nos envían nada.

### ¿Qué queda guardado y dónde?

En tu equipo: las fichas del cierre y del presupuesto, los reportes, el registro de cada corrida y el comprobante de aceptación de los términos, que cada versión de la familia pide de nuevo.
