# /criterio-portfolio:portfolio-setup documentos/proyectos

Quedó instalado y probé con tres de los 13 proyectos, PRY-206, PRY-203 y PRY-201. Esos tres suman 25 señales y 2 proyectos en verde que los documentos contradicen. No medí cuántos minutos pasaron hasta el primer resultado.

**Lo que miré:** 80 documentos en 13 proyectos, el más reciente del 2026-10-15.

**Cómo lo dejé:** nadie respondió preguntas, así que tomé los valores sugeridos y los dije al decidirlos.
- **Rol:** PMO del portafolio, porque hay 13 proyectos.
- **Comité:** semanal, con el informe dos días antes. El 2026-10-19 como próximo comité es un valor supuesto, no confirmado.
- **Formato:** presentación.
- **Dónde queda cada cosa:** la configuración en `.criterio/portafolio/config.json`, lo que Vera va encontrando en `estado/` y los informes en `reportes/`.
- **Términos:** quedaron aceptados por José Francisco Ñáñez, con comprobante en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.9-2026-10-15.md` y `.pdf`.
- **Verificación:** el chequeo de la configuración pasó sin problemas.

**Hallazgos del cálculo:**
- **PRY-206** declara verde y 87 %, pero el plan sostiene entre 50 y 75 %. Lleva +47 días contra la línea base original, y su hito de ingeniería básica está cerrado sin acta de recibo.
- **PRY-203** declara rojo y 91 %, pero el plan sostiene entre 60 y 80 %. Tiene un entregable del proveedor con 210 días de atraso y un compromiso reprogramado 6 veces. El cierre difiere entre el cronograma (2027-01-05) y el acta (2027-02-21).
- **PRY-201** declara verde, pero proyecta 3.864 M COP contra 3.300 M aprobados (+17,1 %), tiene un hito vencido y un compromiso vencido.

En PRY-203, las notas del 15/10 mencionan un riesgo que nadie registró: que el proveedor no llegue con el equipo completo. Lo dejé en la ficha, pero no lo cuento como hallazgo porque el cálculo no lo levantó.

**El portafolio completo:** faltan 10 proyectos, en 2 lotes uno tras otro. Calculo unos 30 a 40 minutos, pero es una estimación y no la medí.

**Lo que le falta a la carpeta:**
- Ningún proyecto trae la facultad del gerente ni la fase.
- Hay hitos y compromisos dados por cerrados sin acta de recibo.
- CC-01 de PRY-206 dice «autorizada por el comité» sin acta ni fecha.

La corrida quedó registrada con el id `2026-10-15-portfolio-setup-1`, y la salida completa está en `estado/corridas/salida-portfolio-setup.md`.

Como PMO con equipo, puedes publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios. Para correr el portafolio completo, di que sí.