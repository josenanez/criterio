# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

**Miré:** 78 documentos en 13 proyectos. Hay 37 .md, 15 .docx, 13 .pdf, 7 .xlsx, 4 .csv, 1 .json y 1 .txt. El más reciente es del 2026-10-17.
**Eres:** PMO del portafolio. Lo propuse porque hay varios proyectos.
**Te aviso:** dos días antes del comité. Lo configuré semanal, con el próximo el 2026-10-20. Esa fecha es mi suposición: nadie la confirmó.
**En:** presentación, el valor sugerido.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-17 (versión 0.3.13, términos 1.1). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`, con SHA-256 6d4b67767ea3a1ea…
**Preguntas:** 0. La sesión no tenía interfaz y tomé las respuestas sugeridas.

La configuración quedó en `.criterio/portafolio/config.json` y pasó la verificación. Lo que voy encontrando va en `estado/` y los informes irán a `reportes/`.

### Probé con tres proyectos

Probé con PRY-202, PRY-203 y PRY-208, que tenían la documentación más reciente. Eran 35 documentos y el cálculo levantó 31 señales.

- **PRY-203 Open Banking declara verde, pero los datos no lo sostienen.**
  - Declara 39% de avance. Con 3 de 4 hitos cerrados, el cronograma sostiene entre 75% y 100%.
  - La proyección al cierre es 19,1% mayor que lo aprobado.
  - Ya está comprometido el 90,4% del presupuesto.
  - Dos hitos figuran cerrados sin acta que lo pruebe.
  - Hay un compromiso vencido hace 5 días.
- **PRY-202 Migración a la nube movió el cierre 76 días sin que nadie lo autorizara.**
  - La solicitud CC-01 sigue pendiente de comité.
  - Seis compromisos están vencidos y tres no tienen fecha.
  - Dos compromisos se han reprogramado 6 y 5 veces.
  - Dos hitos figuran cerrados sin acta.
  - Datacore tiene un entregable retrasado 196 días y otro 149.
  - La "Bolsa de horas" aparece recibida y facturada sin acta de recibo.
  - El gerente publicó su propia ficha (`ficha-pm.json`). La guardé aparte y no la mezclé con mi lectura.
- **PRY-208 Motor de decisión declara rojo.**
  - Declara 57% de avance. Con 4 de 5 hitos cerrados, el plan sostiene entre 80% y 100%.
  - La proyección al cierre es 26,9% mayor que lo aprobado.
  - Dos hitos figuran cerrados sin acta.
  - La "Parametrización del tarifario" lleva 91 días de retraso.
  - La "Bolsa de horas" figura recibida sin acta.

En PRY-202 la ficha muestra lo ejecutado (3.907 M COP) por encima de lo comprometido (3.838 M COP). El cálculo no lo levantó como señal, así que lo dejo solo como nota.

### El portafolio completo

Faltan 10 proyectos, con 43 documentos. Estimo entre 15 y 20 minutos. Es una estimación, no una medición.

### Lo que le falta a tu carpeta

- Ninguna de las tres actas dice hasta dónde puede decidir el gerente sin subir a comité.
- Los tres proyectos declaran hitos cerrados sin el acta que lo prueba.
- Las tres actas dicen "Dependencias: ninguna declarada". Los informes de PRY-203 y PRY-208, en cambio, mencionan una dependencia con el core.
- PRY-206, PRY-207 y PRY-209 no tienen cronograma.
- PRY-200, PRY-206, PRY-207 y PRY-209 no tienen actas de reunión.

Nada de esto bloquea el análisis.

La corrida quedó registrada como `2026-10-17-portfolio-setup-1`, con la salida en `estado/corridas/salida-portfolio-setup.md`.

¿Corro el portafolio completo?