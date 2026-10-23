# /criterio-portfolio:portfolio-scan 

El barrido terminó y las fichas de los 10 proyectos que cambiaron quedaron escritas y selladas. Dejé sin tocar a PRY-201, PRY-209 y PRY-210, porque sus documentos no cambiaron.

- **Lo leído:** de 74 documentos, leí 51 (los de PRY-199 a PRY-208 y PRY-211) y 23 no cambiaron. Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-22, así que no los registré de nuevo.
- **Formatos:** el plan marcó 4 cronogramas `.xml` como ilegibles, pero `texto.py` los convirtió sin instalar nada. No quedó ningún archivo sin leer.
- **Carpeta `entrada/`:** no existe, así que no moví ni dejé pendiente ningún archivo.
- **Campos sin dato:** son 45 en total. La autoridad y la fase faltan en los 10 proyectos, y el producto en 6. El resto es evidencia de hitos cerrados, de los entregables del contrato CT-199 y de su facturación, los cronogramas que no existen en PRY-207 y PRY-208, y quién decide la solicitud de cambio de PRY-208.
- **Estado y avance:** guardé el estado y el avance que reportan los gerentes como declaración, no como evidencia.

Lo que más llama la atención:
- **Hitos cerrados sin acta de recibo:** son 17 en el cálculo del script, y las 17 señales cubren también los hitos de PRY-209 y PRY-210 que no toqué. Los hitos de PRY-200, PRY-203, PRY-204, PRY-205 y PRY-211 dicen "cerrado" en el cronograma y ningún documento lo prueba. Los cuatro de PRY-205 están en ese caso.
- **PRY-205 y PRY-207:** ambos tienen la fecha de cierre vencida y reportan 34 % y 32 % de avance en verde.
- **Solicitudes de cambio fechadas después del cronograma:** en PRY-200, PRY-203 y PRY-204 el cronograma nuevo parece reflejarlas, pero las solicitudes llevan una fecha posterior (en PRY-203, la misma del cronograma v3). Además falta el cronograma v2 de PRY-203.
- **Compromisos vencidos:** en estos 10 proyectos son 4, de PRY-200, PRY-203 (dos) y PRY-206.
- **Ejecutado por encima de lo comprometido:** ocurre en PRY-206 y PRY-211.
- **Contrato que no cuadra:** el contrato CT-199 de PRY-199 es de acero de refuerzo, horas de ingeniería e izaje, y el proyecto es una pintura. Lo registré tal cual y conviene confirmar que esté bien archivado.

La corrida quedó registrada como `2026-10-22-portfolio-scan-1`, con el snapshot y la salida completa guardados. El script contó 54 señales en los 13 proyectos. Esas cifras son las que valen para el informe. Mi lista de hallazgos es solo lo que vi al leer, y el script no marcó el cierre vencido de PRY-207.

El siguiente paso, si lo quieres, es el informe consolidado con `/criterio-portfolio:portfolio-report`.

Los archivos están en `estado/`:
- `records/PRY-199.json` y los otros nueve que cambiaron
- `corridas/salida-portfolio-scan.md`