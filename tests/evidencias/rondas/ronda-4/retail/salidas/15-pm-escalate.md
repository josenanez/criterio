# /criterio-project:pm-escalate 

Armé el paquete de escalamiento de PRY-209 (Migración del ERP). Escala un solo punto: el acta de constitución no declara qué puede decidir Camilo Beltrán como gerente. Leí el acta completa y no tiene ninguna sección de autoridad.

**La pregunta cerrada:** ¿se declara por escrito qué puede decidir Camilo (fechas de hitos, quitar bloqueos a compromisos de terceros, gasto) y hasta dónde, o toda decisión de esas clases pasa por el comité?
- **Quién decide:** el acta no lo dice. Lo razonable es el patrocinador (Gustavo Neira) con el Comité de Cadena de Abastecimiento, que aprobó el acta, pero eso es inferencia mía. Confírmala antes de llevar el punto.
- **Si no se decide:** el comité siguiente es el 2026-10-29. Hasta entonces, el hito «Ambiente de pruebas certificado», vencido desde el 2026-10-05, no se puede clasificar como decisión del gerente o del comité. Lo mismo vale para el bloqueo de «Enviar el documento 1», que lleva seis reprogramaciones.
- **Opciones:** A es una adenda al acta con la autoridad del gerente y sus topes. B es no tener adenda y escalar caso a caso. Ningún documento trae cifras de costo o de días para ninguna de las dos, y no las inventé.
- **Recomendación:** A. Con B el comité recibiría cada compromiso movido como un punto aparte, y la ficha ya tiene 26 compromisos. Los números de los topes son del comité.

**Efecto sobre otros proyectos:** nadie propuso un cambio de fecha, así que no calculé efecto. Corrí `impact` con 14 días solo para ver cómo funciona; ese número es inventado y no sustenta nada. El acta dice «Ninguna declarada» en dependencias, lo que no prueba que no existan. Los hitos pendientes que un corrimiento tocaría son Integración con el ERP (2026-12-05, a 51 días) y Piloto en tiendas (2027-02-03, a 111 días).

**Lo que no escala todavía:**
- **Bloqueo de Felipe Arango y Diana Molina:** depende de lo que salga el 10-29, y con la autoridad escrita se sabría si lo decide Camilo.
- **Mover la fecha de «Ambiente de pruebas certificado»:** es control de cambios, no escalamiento.
- **Riesgo del proveedor sin dueño y compromisos sin fecha:** son del gerente.

**Lo que no sé:** quién tiene hoy la facultad, cuántos días se mueve cada proyecto alcanzado (la ficha no tiene holgura por actividad) y si existe un documento de autoridad fuera de la carpeta.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-15, v0.3.10), así que no los registré de nuevo. La corrida quedó registrada como `2026-10-15-pm-escalate-1`.

Archivos:
- `/home/claude/banco/ronda-4/retail/espacio/estado/PRY-209-migración-del-erp/corridas/salida-pm-escalate.md`