# /criterio-portfolio:portfolio-scan 

## Barrido — 2026-10-16

**Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Documentos:** hay 72. Leí 47, 25 no cambiaron y ninguno fue ilegible.
**Proyectos:** hay 13. Escribí y sellé 10 fichas en un solo lote, sin subagentes. No toqué PRY-201, PRY-208 ni PRY-211 porque sus documentos no cambiaron. No hay proyectos nuevos y tampoco existe la carpeta `entrada/`, así que no moví nada.

### Campos sin dato (`not_found`)

- Autoridad y fase faltan en los 10 proyectos.
- El producto falta en PRY-202, PRY-205 y PRY-210, cuyas actas dicen «No aplica».
- PRY-205, PRY-207 y PRY-209 no tienen cronograma, así que no hay hitos.
- Nadie registró lo facturado del contrato CT-199 de PRY-199.
- El informe de PRY-209 menciona un proveedor, pero ningún documento trae su contrato.

### Lo que vi al leer

- **PRY-200:** el cronograma v3 (2026-10-04) mueve «Integración con el core» 139 días, de 2027-07-18 a 2027-12-04. Eso es justo CC-01 (+99) más CC-02 (+40), y ambos siguen pendientes del comité. Además falta el cronograma v2, y el hito movido queda después del cierre del acta (2027-09-21).
- **PRY-204:** CC-01 dice «autorizada por el comité», sin acta ni nombre. El cronograma v2 mueve el piloto a 2026-05-23, tres días después del cierre del acta (2026-05-20), que ya pasó con 71% de avance.
- **Compromisos que nacen vencidos:** el de Beatriz Cuéllar en PRY-203 (para 2026-09-30, dicho el 2026-10-14) y el de Rubén Cárdenas en PRY-204 (para 2026-10-03, dicho el 2026-10-12).
- **Otros compromisos:** el de Liliana Torres (PRY-202) no tiene fecha. El de Carlos Peña (PRY-199) es de alguien que no asistió al comité.
- **Hitos cerrados sin acta:** ocurre en PRY-202, 204, 206 y 210. En PRY-202, «Integración con el core» (2026-10-13) sigue en curso y ya venció.
- **Cierres ya pasados:** PRY-205 (2026-08-24, avance 77%), PRY-206 (2026-02-09, 62%) y PRY-207 (2026-06-19, 37%).
- **Dependencia del core sin proyecto:** los informes de PRY-200, 203 y 210 la mencionan sin nombrar el proyecto, y las actas dicen «Ninguna declarada».
- **PRY-211:** su ficha del gerente cita fuentes sin el prefijo de la carpeta del proyecto, y por eso el índice marca 17 campos como «fuente no encontrada». No lo corregí, porque esa ficha es del gerente.

### Qué no hice

- No calculé desviaciones ni semáforos.
- Marqué como vencidos los dos compromisos de arriba por la fecha del propio documento. El script los recalcula.

### Señales que calculó el script al registrar la corrida

- Son 50 hallazgos en los 13 proyectos.
- Los más frecuentes son 13 hitos cerrados sin evidencia, 9 compromisos vencidos, 6 declarado contra evidencia, 5 compromisos sin fecha, 4 de costo y 4 de avance contra plan.
- También salieron 3 de desviación en tiempo, 1 replanificación sin autorización (PRY-200), 1 hito vencido (PRY-202), 1 proyecto en silencio (PRY-207) y 1 diferencia entre la ficha del gerente y la mía (PRY-211).
- No aparece ningún hallazgo en PRY-199, PRY-205 ni PRY-209.

La corrida quedó registrada como `2026-10-16-portfolio-scan-1`, con la salida en `estado/corridas/salida-portfolio-scan.md`. Ese archivo es el texto de mi informe de lectura y no incluye el resumen de señales de arriba.

Como hay más de un proyecto, puedo correr `/criterio-portfolio:portfolio-report` para el informe consolidado. Conviene mirar antes del comité del 2026-10-21 lo de PRY-200 y PRY-204, y los dos compromisos vencidos.

Criterio Portfolio 0.3.11 · Fichas tocadas: PRY-199, 200, 202, 203, 204, 205, 206, 207, 209 y 210 · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.11