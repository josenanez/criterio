# Preguntas frecuentes · Criterio CTO

Las respuestas cortas a lo que suele preguntar quien llega a la familia de la tecnología. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hacen Fausto y Domingo?

Fausto pone cada cambio en producción al lado de su aprobación y su revisión, cada despliegue al lado de su cambio, cada incidente mayor al lado de su causa y cada servicio al lado del nivel acordado con el negocio. Domingo pone cada activo al lado de su dueño y del soporte de su fabricante, cada licencia al lado de su uso, cada proveedor al lado de su nivel de servicio y la factura de la nube al lado de su presupuesto.

### ¿Aprueban cambios o eligen proveedores?

No. Ningún agente aprueba un cambio, decide una arquitectura, califica un incidente, elige un proveedor, decide renovar o retirar un activo ni interpreta un contrato. Dicen qué falta y dónde, con la cita; la decisión es del comité de cambios, del comité de arquitectura, del área de tecnología y de legal.

### ¿Y la seguridad?

Es de la familia CISO: las vulnerabilidades, los controles y los incidentes de seguridad los procesan Alexis, Guillermo y Amparo. La CTO toma de la tecnología lo que no es seguridad.

### ¿Sobre qué marcos trabajan?

Sobre ISO/IEC 20000-1, la gestión del servicio, para los cambios, los incidentes y los niveles de servicio, e ISO/IEC 19770-1, la gestión de los activos de TI. En una entidad vigilada de Colombia, también la Circular Externa 005 de 2019 de la Superintendencia Financiera, sobre la nube. Se citan por su nombre, nunca por su texto.

## Cómo se usa

### ¿Se conecta a ServiceNow, Jira o a mi nube?

No. Procesa las exportaciones en Excel o CSV de los cambios, los despliegues, los incidentes, el inventario, las licencias y la factura de la nube, y los documentos que la organización deja en su carpeta: la política, el catálogo de servicios, las actas de los comités y los contratos con los proveedores.

### ¿Quién fija los plazos y los niveles?

La organización, en su política de cambios y de niveles de servicio y en su catálogo de servicios. El setup propone los plazos y los umbrales desde esos documentos y la persona los confirma; quién aprobó cada cambio lo dicen las actas del comité.

## Estado

### ¿Está probada?

El motor está probado contra todo su material sintético, con una clave que los agentes no ven y dos entidades de control sin ninguna señal. La ronda con los dos agentes viene en la 0.2.0. No se ha probado sobre la documentación de una organización concreta.
