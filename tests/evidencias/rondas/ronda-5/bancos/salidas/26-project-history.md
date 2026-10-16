# /criterio-portfolio:project-history PRY-200

## Historia · PRY-200 Originación digital · 2026-06-17 a 2026-10-13

**Leí:** 7 documentos entre 2026-06-17 y 2026-10-13. Son el acta de constitución, los cronogramas v1 y v3, el informe de avance, CC-01, CC-02 y el acta del comité del 13 de octubre. Los leí desde la copia de texto en caché; las citas apuntan a los originales.

**Trimestres sin un solo documento:** el 3.º de 2026 (julio–septiembre). Entre el acta con el cronograma v1 (2026-06-17) y el siguiente documento (2026-10-04) hay 109 días sin nada escrito.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

### En una línea
El proyecto se aprobó el 2026-06-17 con la integración con el core el 2027-07-18 y sin dependencias declaradas. El cronograma v3 (2026-10-04) movió ese hito al 2027-12-04, sin motivo escrito ni documento que lo apruebe. CC-01 (2026-10-05) y CC-02 (2026-10-11) son posteriores a la v3 y siguen «pendientes de presentación al comité». El acta del comité del 13 de octubre solo registra «Avance» y «Compromisos», y no menciona esas solicitudes.

### Las cuatro cifras
| Replanificaciones | Atraso vs. original | Meses declarando sin sustento | Cambios de gobierno |
|---|---|---|---|
| 1 | 139 días (36.0 %) | No calculable: hay una sola declaración (2026-10-04) | 0 |

### Línea de tiempo
| Fecha | Documento | Qué cambió |
|---|---|---|
| 2026-06-17 | Acta de constitución | Aprobado con 4.200.000.000 COP, inicio 2026-06-27 y cierre 2027-09-21. Dependencias: «Ninguna declarada». |
| 2026-06-17 | Cronograma v1 | Línea base: integración con el core el 2027-07-18. |
| 2026-10-04 | Cronograma v3 | La integración con el core pasa al 2027-12-04. No hay v2 en la carpeta. |
| 2026-10-04 | Informe de avance | Declara estado rojo y 24 % de avance. Reporta un hallazgo de seguridad y dos historias fuera del sprint por dependencia con el core. Proyección al cierre: 4.643.424.770 COP. |
| 2026-10-05 | CC-01 | Ampliación de alcance: +99 días y +198.000.000 COP. Pendiente. |
| 2026-10-11 | CC-02 | Ampliación de alcance: +40 días y +80.000.000 COP. Pendiente. |
| 2026-10-13 | Acta del comité | Un compromiso: Javier Hoyos, «Entregar el punto 38», para 2026-11-10. |

### Replanificaciones
Hay una, del 2026-10-04: cierre nuevo 2027-12-04, sin motivo documentado y sin documento que la apruebe. Contra la línea base vigente el atraso es 0, porque la v3 ya incorporó el movimiento. El script marca `rebaseline_unauthorized`: 139 días movidos y 0 autorizados.

### Gobierno y compromisos
- **Gobierno:** no hay cambios de patrocinador, gerente ni comité en los documentos leídos.
- **Compromisos:** ninguno se repitió. Solo hay uno abierto, con una fecha prometida.

### Desde cuándo lo declarado no se sostiene
No puedo fechar un deslizamiento: hay una sola declaración y ningún informe anterior con el que compararla. Lo que sí se ve:
- **Cuadra con el rojo:** las señales abiertas son atraso de 139 días, proyección de costo 10.6 % sobre lo aprobado y movimiento de línea base sin autorizar. El informe no explica ninguna de las tres.
- **Dentro del rango del plan:** el 24 % tiene detrás 0 de 3 hitos cumplidos, y el plan sustenta entre 0 % y 33 %. No hay evidencia de cumplimiento de ningún hito.

### Lecciones ancladas a un hecho
1. **La línea base se movió antes de que existiera la solicitud que la justificaría.** La v3 es del 2026-10-04 y CC-01 y CC-02 son del 10-05 y 10-11. El efecto son 139 días de atraso sobre la original sin autorización registrada.
2. **Apareció una dependencia que el acta no tenía.** El acta dice «Ninguna declarada» y el informe del 2026-10-04 habla de «dependencia con el core» sin nombrar el proyecto. El efecto es una dependencia sin dueño ni fecha, justo sobre el hito que se movió.
3. **Hay un trimestre sin documentos.** Nada entre 2026-06-17 y 2026-10-04 (109 días). Por eso no se puede saber cuándo se supo del desvío.

### Lo que no sé
- Por qué se movió la integración con el core.
- Dónde está el cronograma v2 y quién aprobó la v3.
- Contra qué fecha medir el atraso. El script usa 2027-07-18 (último hito de la v1) como cierre original, pero el acta fija el cierre en 2027-09-21. No recalculé contra la fecha del acta; hay que confirmar cuál es la referencia.
- Si CC-01 y CC-02 explican el movimiento de la v3.
- Quién responde por las dos incidencias y el riesgo abiertos en el informe, que no tienen dueño.
- La autoridad y la fase del proyecto: no figuran en ningún documento.

Esta historia no atribuye intención. Que el movimiento no tenga motivo escrito no dice por qué ocurrió ni quién decidió qué; eso se averigua hablando con las personas. Es un borrador de trabajo hecho con los 7 documentos de la carpeta, y la verificación es de quien lo lea.

**Siguiente paso:** puedo llevar la historia al cierre del proyecto o al comité del 2026-10-21. Allí hay una decisión pendiente sobre CC-01, CC-02 y la v3 ya publicada.

La corrida quedó registrada como `2026-10-16-project-history-1`. Tardó 54 segundos. La salida completa está en `estado/corridas/salida-project-history.md`.