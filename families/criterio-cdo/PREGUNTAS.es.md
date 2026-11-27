# Preguntas frecuentes · Criterio CDO

Las respuestas cortas a lo que suele preguntar quien llega a la familia de los datos. Este archivo es la única fuente: la página de la familia en josenanez.com las lee de aquí.

## Qué es

### ¿Qué hacen Custodia y Ariadna?

Custodia pone cada conjunto del catálogo de datos al lado de su dueño, su clasificación y su plazo de conservación, y dice qué política se venció, qué término de los informes no está en el glosario y qué base con datos personales no está en el registro de la organización. Ariadna sigue cada cifra de los informes de dirección hasta su fuente: la que no coincide, la que sale de otro corte, el linaje que se corta y la regla de calidad que no pasa.

### ¿Corrigen datos o cifras?

No. Ninguna agente asigna un dueño, decide una clasificación, borra un dato ni corrige una cifra. Dicen qué falta y dónde, con la cita; la decisión es del área de datos y de quien firma el informe.

### ¿Sobre qué marcos trabajan?

Sobre las áreas de DAMA-DMBOK —el gobierno, la calidad y los metadatos con el linaje—, los principios BCBS 239 del Comité de Basilea para la cifra de riesgo que llega a la junta e ISO/IEC 25012 para la calidad de los datos. Se citan por su nombre, nunca por su texto.

## Cómo se usa

### ¿Se conecta a mis bases de datos o a mi catálogo?

No. Procesa las exportaciones en Excel o CSV del catálogo, del linaje, de las cifras de la fuente y de las reglas de calidad, y los documentos que la organización deja en su carpeta: las políticas, el glosario y los informes. El setup mapea las columnas de cualquier exportación.

### ¿Procesa datos personales?

No. De una base con datos personales solo procesa sus metadatos: su nombre, su dueño, su clasificación y si está en el registro. Si llega una extracción con registros de personas, no se abre.

### ¿Quién fija la tolerancia, los umbrales y los plazos?

La organización, en su política de datos y de conservación. El setup los propone desde esos documentos y la persona los confirma.

## Estado

### ¿Está probada?

El motor está probado contra todo su material sintético, con una clave que las agentes no ven y dos entidades de control sin ninguna señal. En la 0.2.0, las dos agentes corrieron sobre todas las entidades del material, con una clave que no ven; en la 1.0.0, la ronda 2 en Colombia, México y Perú: 94 señales y 348 datos, con un piso del 96,0 % en las señales y del 98,9 % en los datos, y ningún control con una señal. Es estable y está lanzada. No se ha probado sobre la documentación de una organización concreta.
