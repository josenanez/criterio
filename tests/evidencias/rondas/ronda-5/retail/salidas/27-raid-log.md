# /criterio-portfolio:raid-log portafolio

Levanté el RAID del portafolio de los 13 proyectos y dejé la corrida registrada. Estos son los documentos de los que sale y lo que muestra.

**Sale de:** las fichas de los 13 proyectos, sus informes de avance, las actas de constitución (solo su sección de dependencias), 16 minutas y notas de reunión, y la salida de `compute` al 2026-10-16. Los términos ya estaban vigentes: versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16.

## RAID, portafolio retail, 2026-10-16

| | Riesgos | Supuestos | Incidencias | Dependencias |
|---|---|---|---|---|
| Registro actual | 22 | 0 | 16 | 0 |
| Con mi clasificación | 10 | 7 | 16 | 5 |

- **Doliente y fecha:** los 38 ítems están sin doliente y sin fecha. No relleno ninguno.
- **Valoración:** ninguno trae probabilidad ni impacto. Usaría alta, media y baja, pero no valoré nada porque ninguna fuente lo trae.
- **No registrado formalmente:** 1.

### Necesitan decisión ahora
- **Hallazgo de seguridad en los medios de pago** (PRY-200, 209 y 211). El texto es idéntico en los tres. No sé si es un hallazgo o tres, y en 209 y 211 llama la atención. Hay que confirmarlo con sus gerentes.
- **Cambio en la regulación de datos personales** (PRY-201, 202, 208 y 210). Es un factor externo sobre cuatro proyectos y ninguno lo tiene a su cargo.
- **Disponibilidad de los jefes de tienda para el piloto** (siete proyectos). Todos lo dan por hecho y ninguno lo ha verificado. No sé si son las mismas personas.
- **Despliegue reprogramado en PRY-200.** Ya movió la fecha 27 días en el cronograma v2, pero la solicitud de cambio CC-01 sigue sin decisión.
- **Prueba de carga que no alcanzó el umbral** (PRY-201 y 203). Se repite sin fecha de nueva prueba.
- **El proveedor podría no llegar con el equipo completo** (PRY-209). El informe del 2026-10-12 no lo trae y el proyecto declara verde.

### Detectado en reuniones, no registrado
Solo uno: lo de PRY-209, dicho en las notas del 2026-10-16. Las otras 15 minutas traen compromisos, no riesgos, y no inventé ninguno. Formalizarlo es decisión de Liliana Torres, gerente del proyecto.

### Reclasificaciones que propongo
Son 12 ítems que los informes llaman «riesgo». La ficha no cambia hasta que cada gerente las acepte.
- **Siete a supuesto:** los jefes de tienda.
- **Cinco a dependencia de proveedor, declarada y sin confirmar:** «el proveedor no ha confirmado la fecha». Son PRY-203, 204, 206, 207 y 209. No tienen código de proyecto del cual depender, y en esas carpetas no hay contrato ni nombre de proveedor.

### Lo que no pude hacer
- **Cruzar dependencias entre proyectos.** Las 13 actas dicen «Ninguna declarada». Dejé una pregunta abierta: PRY-203 tiene vencido su hito «Integración con el ERP» y PRY-209 migra el ERP, pero los documentos no dicen que uno dependa del otro.
- **Medir «sin movimiento en dos períodos».** Solo hay una lectura del portafolio.
- **Saber si hay mitigaciones vencidas.** Ninguna fuente menciona mitigaciones.
- **Dar fecha de inicio a las incidencias.** La columna «Visto en» del registro es la fecha del informe donde aparece cada ítem, que no es necesariamente la del hecho.

### Después
- **Comité del 2026-10-23.** Puedo subir los seis ítems de arriba como decisiones formuladas, con `/steering-pack`.
- **Dolientes.** Para los ítems de un solo proyecto, el candidato natural es su gerente según el acta. Para los que cruzan proyectos no hay candidato evidente en los documentos, y elegirlo es de la PMO o del comité.
- **Dependencias.** Pedir a cada patrocinador que las declare. Sin eso este registro no cruza nada.

El registro completo, ítem por ítem con ids provisionales, está en `estado/corridas/salida-raid-log.md`. La corrida quedó registrada como `2026-10-16-raid-log-1`.

**Rigor:** los conteos salen de las fichas y de `compute`, no de cálculo a mano. No leí cronogramas, contratos ni actas de recibo más allá de lo que `compute` ya extrajo. La clasificación de los 12 ítems es propuesta mía y nadie la ha validado. Lo hablado fuera de los documentos no lo conozco.