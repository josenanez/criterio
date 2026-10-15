# /criterio-portfolio:portfolio-scan 

Barrido terminado: leí 51 de los 74 documentos y escribí y sellé 10 fichas nuevas. Los términos ya estaban vigentes (versión 0.3.8, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los pedí otra vez.

**Qué se leyó**
- Del plan salió un solo lote de 10 proyectos, ejecutado uno tras otro y sin subagentes.
- Las 10 fichas nuevas son PRY-199, 200, 202, 203, 204, 205, 207, 208, 209 y 210.
- PRY-201, 206 y 211 no cambiaron y conservan su ficha.
- Ningún archivo fue ilegible.
- No hay carpeta `entrada/`, así que no se movió ni quedó pendiente nada.
- La `ficha-pm.json` de PRY-205 quedó entera en el campo `pm_record`, separada de mi lectura.

**Señales calculadas por el script (60 en 12 de los 13 proyectos)**
- **Hitos cerrados sin acta:** 29 señales, en 12 de los 13 proyectos; solo PRY-199 se salva.
- **Estado verde contradicho:** PRY-202, 203 y 205 lo declaran verde.
- **Cierres vencidos con proyecto activo:** PRY-203, 205 y 209.
- **Sobrecosto proyectado:** PRY-204 proyecta 11.623.833.685 COP contra 9.500.000.000 aprobados; PRY-205 proyecta 8.542.694.050 contra 6.800.000.000.
- **Cambios de PRY-208:** la solicitud CC-01 sigue pendiente de comité, y la línea base v2 se publicó sin motivo ni autorización documentados.
- **Compromisos vencidos:** PRY-204, 207 y 208.
- **Compromisos sin fecha:** PRY-205 y 209.
- **Riesgo sin registrar:** en las notas del 2026-10-15 de PRY-205 se dijo que el proveedor podría no llegar con el equipo completo, y nadie lo anotó como riesgo.

**Campos sin dato**
- La autoridad del gerente y la fase están en `not_found` en todas las fichas nuevas.
- El producto está en `not_found` en PRY-202, 203, 209 y 210, porque el acta dice «No aplica».

El resultado completo quedó en `estado/corridas/salida-portfolio-scan.md`. La instantánea del 2026-10-15 y el registro de la corrida (`2026-10-15-portfolio-scan-1`, 167 segundos) también se escribieron. Con más de un proyecto, el siguiente paso natural es `/criterio-portfolio:portfolio-report`.

Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.8