# /criterio-portfolio:document-index 

## Carpeta al 2026-10-15

**Documentos:** 82 · **Sin cambio:** 82 · **Hay que releer:** 0

No cambió ningún contenido. No hay documentos solo reguardados, renombrados, movidos ni borrados. El índice no reporta formatos ilegibles.

### Citas que dejaron de resolver
Hay 33 citas rotas, todas de PRY-203, repartidas en 4 documentos citados:

| Documento citado | Campos | Cuáles |
|---|---|---|
| `00-gobierno/2025-11-25-acta-constitucion.docx` | 13 | identidad, fechas del plan, alcance y exclusiones |
| `20-seguimiento/2026-10-12-informe-avance.pdf` | 8 | estado declarado y cifras de dinero |
| `10-plan/2026-10-12-cronograma-v2.csv` | 12 | los tres hitos (nombre, fechas y estado) |
| `2026-10-15-notas-reunion.txt` | 2 | última fecha de documento y de reunión |

Los cuatro archivos existen en la carpeta de PRY-203 y el índice los cuenta como sin cambio. Lo que falla es la ruta de la cita. La ficha de PRY-203 cita sin el prefijo de carpeta del proyecto (`00-gobierno/…`). Las fichas de los demás proyectos citan `PRY-2xx-nombre/00-gobierno/…`. Es la causa probable; no la verifiqué contra el código del índice.

Mientras no se corrija, el informe sigue mostrando esos 33 datos como sustentados aunque ya no se pueden comprobar.

### Siguiente paso
No hace falta barrido, porque no hay nada que releer. Puedo corregir las 33 citas de PRY-203 anteponiendo `PRY-203-aportes-sociales-en-línea/`, mostrando cada cambio. No he tocado ninguna ficha.

### Términos y registro
- **Términos:** ya estaban vigentes (v0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.
- **Corrida:** quedó registrada en `estado/corridas/` (id `2026-10-15-document-index-1`, 23 s), con la salida completa guardada en `estado/corridas/salida-document-index.md`.
- **Hallazgos de otras señales:** la corrida registró 64 en las fichas (hitos cumplidos sin evidencia, atrasos de proveedor y otros). No salen de este comando, que solo compara documentos.