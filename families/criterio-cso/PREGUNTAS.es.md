# Preguntas frecuentes · Criterio CSO

Las respuestas cortas a lo que suele preguntar quien llega a la familia de la función comercial. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hacen Augusto y Valeria?

Augusto pone el embudo del CRM al lado de su evidencia y el pronóstico al lado de lo que lo sostiene: qué oportunidad no tiene el documento que exige su etapa, cuál está detenida, cuál corre su cierre, cuánto de lo comprometido tiene respaldo y cómo va lo cerrado contra la meta. Valeria pone cada venta al lado de su política, su contrato y su factura: el descuento contra su nivel de aprobación, lo ganado contra los contratos de Fidel, lo firmado contra las facturas de Clara y la comisión contra el plan.

### ¿Reemplazan al responsable comercial?

No. Procesan y contrastan. El pronóstico que se compromete, el descuento que se aprueba, la meta y la comisión los decide siempre una persona.

### ¿Califican a los vendedores?

No. La señal es de la oportunidad, no de quien la lleva. Ningún reporte ordena ni compara a las personas del equipo, y si alguien pide el pronóstico o la meta por vendedor, el agente lo dice y no lo arma.

### ¿Qué no hacen nunca?

No escriben ni cambian nada en el CRM, no contactan a un cliente, no aprueban un descuento ni una excepción de precio, no fijan una meta y no liquidan ni corrigen una comisión.

## Cómo se usa

### ¿Se conectan a mi CRM?

No. Procesan lo que el CRM exporta, en CSV o Excel, con la fecha de la exportación en el nombre. Una conexión directa sería otra decisión, con su revisión de seguridad.

### ¿Qué CRM sirve?

Salesforce y HubSpot, cada uno con su lector verificado contra la documentación que publica: los campos de la oportunidad de Salesforce y las propiedades del negocio de HubSpot. Cualquier otro CRM sirve con su exportación en CSV o Excel y el mapeo de columnas que deja el setup. Microsoft Dynamics y Zoho, con su propio lector, están en la hoja de ruta.

### ¿Cómo sabe que una oportunidad no tiene evidencia?

Por la tabla de etapas de la organización: cada etapa dice qué documento exige —la propuesta enviada, la orden de compra— y una etapa exige también lo de las anteriores. El agente lleva a la ficha cada documento de la carpeta de evidencia con su oportunidad y su tipo, y el motor cruza.

### ¿Cómo sabe que un cierre se corrió?

Comparando cada exportación con la anterior: cada vez que la fecha de cierre de una oportunidad abierta pasa a una posterior, cuenta. Si el CRM exporta el historial de campos, como Salesforce, cuenta desde el historial.

### ¿De dónde sale el pronóstico comprometido?

Del acta o el paquete del comité comercial: el agente lleva a la ficha el valor que se comprometió para el periodo, con su cita. Si el acta no compromete un valor, el reporte dice que falta y no lo inventa.

### ¿Necesito a Fidel y a Clara?

Para el cruce de lo ganado con lo firmado y lo facturado, sí: Valeria toma el contrato de las fichas de Fidel y la factura de las de Clara, y no vuelve a procesarlos. Lo demás —el embudo, el pronóstico, la meta, el descuento— funciona sin ellos.

### ¿Cuánto tarda el primer resultado?

En los primeros quince minutos, `sales-setup` reconoce cada exportación del CRM y deja ver el embudo contra su evidencia, y `revenue-setup` deja ver lo ganado contra lo firmado y lo facturado.

### ¿En qué países sirve?

La primera versión se prueba en Colombia y México. Ecuador, Perú y Chile, que ya están en el registro de países de las demás familias, siguen en la hoja de ruta.

## Los datos

### ¿Guardan los datos de contacto de mis clientes?

No. La ficha guarda la cuenta y la oportunidad, no el correo ni el teléfono de una persona, y el motor marca como problema una ficha que los traiga.

### ¿Se publican las comisiones?

No, por omisión. Son la remuneración de personas identificables: el reporte de comisiones no sale en Rostrum salvo que la configuración de Valeria lo diga.

### ¿Dónde se procesan mis documentos?

En la infraestructura de la plataforma de IA, no solo en tu equipo. Confirma que sea admisible bajo tus políticas antes de apuntarla a material confidencial.

## El estado

### ¿Está lista para usar?

Todavía no: está en construcción. El motor pasa su prueba determinista sobre material sintético de Colombia y México; la ronda con los agentes, con una clave que no ven, es lo que la declara probada, y con ella sale su primera versión, la de laboratorio.

### ¿Cuándo llega la 1.0?

Cuando Criterio la declare, con las tres condiciones de la decisión 0018: su alcance planeado liberado, dos rondas completas seguidas sin defectos nuevos, y el esquema de la ficha fijo.
