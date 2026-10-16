# /criterio-portfolio:document-index 

No hay nada que releer en la carpeta, pero 22 citas de PRY-206 no resuelven. Es un problema de ruta, no de documentos borrados. Corrí `/document-index` el 2026-10-16; los términos ya estaban vigentes (v1.1, a nombre de José Francisco Ñáñez), así que no hubo que registrarlos de nuevo.

**Estado de la carpeta:** hay 82 documentos y los 82 están sin cambios. No hay nuevos, cambiados, reguardados, renombrados ni borrados, y el índice no reportó formatos ilegibles. No hace falta `/portfolio-scan`.

**Citas rotas (22, todas de PRY-206):**
- **Dónde:** están en una ficha duplicada, `estado/PRY-206-precios-dinámicos/records/PRY-206.json`.
- **Cuáles cita:** `00-gobierno/2025-11-15-acta-constitucion.docx`, `10-plan/2025-11-15-cronograma-v1.csv`, `20-seguimiento/2026-10-16-informe-avance.pdf` y `20-seguimiento/2026-09-21-factura-ct-914.pdf`.
- **Por qué no resuelven:** los archivos sí existen en `documentos/proyectos/PRY-206-precios-dinámicos/`. Esa ficha los cita sin el prefijo `PRY-206-precios-dinámicos/`, y las demás fichas (incluida `estado/records/PRY-206.json`) sí lo llevan.
- **No corregí nada.** Hay que decidir si se corrige la ruta o se retira la ficha duplicada. Tampoco comparé si su contenido difiere del de `estado/records/PRY-206.json`.

**Registro de la corrida:**
- **Salida:** `/home/claude/banco/ronda-6/retail/espacio/estado/corridas/salida-document-index.md`.
- **Corrida:** quedó registrada como `2026-10-16-document-index-1` y tardó 20 segundos.
- **Señales abiertas:** la corrida contó 76, de otras fuentes del estado y no de este índice. Ejemplos: 30 de hitos cumplidos sin evidencia y 9 de compromisos vencidos.