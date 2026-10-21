# Manual de los comandos de Criterio

Los 38 comandos de la familia PMO y de Rostrum, en el orden en que una PMO los usa: Alba define el producto, Samuel ejecuta un proyecto, Vera consolida el portafolio y Rostrum lo publica. Cada comando se escribe con el prefijo de su plugin; el autocompletado hace el resto.

Este manual se genera con `scripts/manual.py` desde la tabla del README de cada plugin y su `contratos.json`, el mismo contrato que las pruebas comparan contra cada corrida. No se edita a mano.

## Alba · un producto

### `/criterio-product:product-setup`

**Qué hace.** **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y contrasta la definición que ya tengas

**Argumento.** `[ruta de la carpeta del producto] o vacío`

**Lee.** config (si existe); documentos del producto

**Muestra.** qué hay escrito, cuatro preguntas, definición contra evidencia

**Escribe.** `.criterio/producto/<código>/config.json`; `<estado>/ (init)`; `<estado>/producto.json`; `<estado>/requirements/<REQ>.json`; `.criterio/terminos/ (aceptar: comprobante .md, .pdf y .sha256, y aceptaciones.json)`

**Skills.** **demand-evidence**, **document-intake**, **product-metrics**, **requirement-record**

### `/criterio-product:product-discovery`

**Qué hace.** Entrevistas y tickets en temas con la cita de quién lo dijo, y el tema que lleva meses dicho sin que nadie lo convierta en nada

**Argumento.** `[carpeta o archivo] o vacío`

**Lee.** config; material de descubrimiento; `<estado>/requirements/`

**Muestra.** temas por problema, con quién lo dijo y cuándo

**Escribe.** `<estado>/requirements/<REQ>.json (evidence)`

**Skills.** **demand-evidence**, **discovery-synthesis**, **document-intake**, **product-metrics**, **requirement-record**

### `/criterio-product:product-requirements`

**Qué hace.** El registro con sus vacíos: sin doliente, sin criterio, aceptado sin que nadie lo pidiera, y lo que nadie decide

**Argumento.** `[REQ-xxx] o vacío`

**Lee.** config; `<estado>/requirements/`

**Muestra.** vacíos por requerimiento y quién los cierra

**Escribe.** `<estado>/requirements/<REQ>.json`

**Skills.** **product-health**, **requirement-record**

### `/criterio-product:product-definition`

**Qué hace.** La definición contra la evidencia de demanda, y dónde el negocio y los datos no coinciden

**Argumento.** `[ruta de la definición] o vacío`

**Lee.** config; definición; `<estado>/requirements/`; `<estado>/producto.json`

**Muestra.** afirmación por afirmación en tres clases, cifras contrastadas, barrido normativo

**Escribe.** `<estado>/producto.json (definition)`

**Skills.** **assumption-tracking**, **demand-evidence**, **product-metrics**, **raid-taxonomy**, **regulatory-sweep**

### `/criterio-product:product-trace`

**Qué hace.** Requerimiento → decisión → proyecto → entregable, y las dos brechas de arriba

**Argumento.** `[REQ-xxx o proyecto] o vacío`

**Lee.** config; `<estado>/requirements/`; fichas de proyecto

**Muestra.** cadena por requerimiento, cobertura, lo construido sin requerimiento

**Escribe.** nada: no escribe

**Skills.** **requirement-record**

### `/criterio-product:product-spec`

**Qué hace.** El borrador de especificación con criterios verificables y los vacíos señalados, no rellenados

**Argumento.** `[REQ-xxx, …] o vacío`

**Lee.** config; `<estado>/requirements/`

**Muestra.** secciones con sus REQ, criterios verificables, vacíos con dueño

**Escribe.** nada: no escribe

**Skills.** **assumption-tracking**, **regulatory-sweep**, **requirement-record**, **specification-draft**

### `/criterio-product:product-charter`

**Qué hace.** El acta de constitución: donde nace la ficha y el escritor cambia de manos

**Argumento.** `<REQ-xxx>`

**Lee.** config; `<estado>/requirements/`

**Muestra.** borrador, supuestos que pasan al proyecto, qué no entra

**Escribe.** `<estado>/records/<código>.json (solo con acta firmada)`

**Skills.** **assumption-tracking**, **demand-evidence**, **governance-artifacts**, **project-record**, **raid-taxonomy**, **requirement-record**

### `/criterio-product:product-business-case`

**Qué hace.** La estructura del caso de negocio con cada cifra citada, y los vacíos con quién los produce

**Argumento.** `[ruta del caso] o vacío`

**Lee.** config; caso de negocio; `<estado>/requirements/`; `<estado>/producto.json`

**Muestra.** cifras en tres clases (medida, declarada, supuesta), costos, vacíos

**Escribe.** nada: no escribe

**Skills.** **assumption-tracking**, **product-metrics**, **requirement-record**

### `/criterio-product:product-publish`

**Qué hace.** Publica tu ficha donde los demás productos la puedan leer

**Argumento.** `[carpeta de publicados] o vacío`

**Lee.** config; `<estado>/producto.json`; `<estado>/requirements/`

**Muestra.** qué publica y la ruta exacta

**Escribe.** `<publicados>/<código>.json`

### `/criterio-product:product-overlap`

**Qué hace.** Dónde te pisas con otro producto: la misma métrica contada dos veces, el mismo proyecto, el mismo segmento

**Argumento.** `[código de otro producto] o vacío`

**Lee.** config; `<estado>/producto.json`; productos publicados

**Muestra.** métricas compartidas, proyectos compartidos, segmento

**Escribe.** nada: no escribe

**Skills.** **product-metrics**, **requirement-record**

### `/criterio-product:product-wake`

**Qué hace.** **El que se le pone a un reloj.** Lo que cruzó un umbral sin que nadie hiciera nada

**Argumento.** `[AAAA-MM-DD]`

**Lee.** config; `<estado>/cadencia.json`; `<estado>/requirements/`

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/cadencia.json`; `<estado>/snapshots/<fecha>.json`

**Skills.** **assumption-tracking**, **document-intake**, **product-health**

## Samuel · un proyecto

### `/criterio-project:pm-setup`

**Qué hace.** **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y lee tu última minuta

**Argumento.** `[ruta de la carpeta] o vacío`

**Lee.** config (si existe); documentos del proyecto

**Muestra.** qué encontró, cuatro preguntas, compromisos de la última reunión

**Escribe.** `.criterio/proyecto/<código>/config.json`; `<estado>/ (init)`; `<estado>/records/<código>.json`; `.criterio/terminos/ (aceptar: comprobante .md, .pdf y .sha256, y aceptaciones.json)`

**Skills.** **commitment-tracking**, **document-intake**, **project-record**

### `/criterio-project:pm-agenda`

**Qué hace.** La agenda con los puntos que necesitan a alguien en la sala, y con lo que esta reunión no puede mover

**Argumento.** `[fecha de la reunión] o vacío`

**Lee.** config; `<estado>/records/<código>.json`; `<estado>/snapshots/`

**Muestra.** puntos con tiempo y cita; la suma cabe

**Escribe.** nada: no escribe

**Skills.** **raid-taxonomy**

### `/criterio-project:pm-minutes`

**Qué hace.** El acta sobre la transcripción o las notas, con cada cosa atribuida a una persona

**Argumento.** `<ruta de la transcripción o las notas>`

**Lee.** config; la transcripción; `<estado>/records/<código>.json`

**Muestra.** acta con acuerdos, compromisos, decisiones, riesgos y contradicciones

**Escribe.** `<estado>/records/<código>.json (commitments, raid)`; `30-reuniones/<fecha>-acta.md`

**Skills.** **commitment-tracking**, **document-intake**, **raid-taxonomy**

### `/criterio-project:pm-commitments`

**Qué hace.** Quién prometió qué, qué venció sin evidencia, y qué se viene reprogramando reunión tras reunión

**Argumento.** `[ruta de una minuta] o vacío`

**Lee.** config; `<estado>/records/<código>.json`

**Muestra.** compromisos ordenados por lo que necesita a alguien

**Escribe.** `<estado>/records/<código>.json (commitments)`

**Skills.** **commitment-tracking**

### `/criterio-project:pm-report`

**Qué hace.** El informe semanal completo **salvo el estado**, que lo declaras tú

**Argumento.** `[fecha de corte] o vacío`

**Lee.** config; `<estado>/records/<código>.json`; `<estado>/snapshots/`

**Muestra.** informe contra la corrida anterior, declaración contrastada, cuatro cifras

**Escribe.** `<estado>/snapshots/<fecha>.json`

**Skills.** **baseline-variance**

### `/criterio-project:pm-publish`

**Qué hace.** Publica tu ficha donde la PMO la puede leer

**Argumento.** `[confirmar] o vacío`

**Lee.** config; `<estado>/records/<código>.json`

**Muestra.** qué va a publicar, y la ruta exacta

**Escribe.** `00-gobierno/ficha-pm.json`

**Skills.** **project-record**

### `/criterio-project:pm-plan`

**Qué hace.** El primer borrador del plan y la WBS desde el acta, **sin comprometer ninguna fecha**

**Argumento.** `[ruta del acta] o vacío`

**Lee.** config; acta de constitución

**Muestra.** WBS por entregable, supuestos, qué falta para fechar

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**, **raid-taxonomy**

### `/criterio-project:pm-escalate`

**Qué hace.** Lo que excede tu autoridad, como pregunta cerrada, con a quién alcanza calculado

**Argumento.** `[qué se escala] o vacío`

**Lee.** config; `<estado>/records/`

**Muestra.** pregunta cerrada, opciones, efecto, quién decide

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**, **raid-taxonomy**

### `/criterio-project:pm-wake`

**Qué hace.** **El que se le pone a un reloj.** Mira qué toca según tu reunión, y si no toca nada se calla

**Argumento.** `[AAAA-MM-DD]`

**Lee.** config; `<estado>/cadencia.json`

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/cadencia.json`; `<estado>/records/<código>.json (commitments, solo si el barrido trae una minuta)`

**Skills.** **commitment-tracking**, **document-intake**

## Vera · el portafolio

### `/criterio-portfolio:portfolio-setup`

**Qué hace.** **Lo primero que se corre.** Mira tus carpetas, hace cinco preguntas y produce el primer informe sobre tus propios documentos

**Argumento.** `[ruta de la carpeta] o vacío`

**Lee.** config (si existe); documentos

**Muestra.** qué encontró en la carpeta, cinco preguntas, las señales de `compute` sobre tres proyectos

**Escribe.** `.criterio/portafolio/config.json`; `<estado>/ (init)`; `<estado>/records/<código>.json (tres)`; `.criterio/terminos/ (aceptar: comprobante .md, .pdf y .sha256, y aceptaciones.json)`

**Skills.** **commitment-tracking**, **document-intake**, **portfolio-health**, **project-record**

### `/criterio-portfolio:portfolio-wake`

**Qué hace.** **Lo que el reloj invoca.** Mira qué toca hoy, lo hace, y si no toca nada se calla

**Argumento.** `[AAAA-MM-DD para simular otro día]`

**Lee.** config; `<estado>/cadencia.json`; `<estado>/peticiones/`

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/cadencia.json`

**Skills.** **document-intake**, **portfolio-health**

### `/criterio-portfolio:document-index`

**Qué hace.** Qué documentos cambiaron de verdad, qué hay que releer y qué citas dejaron de resolver

**Argumento.** `[código del proyecto]`

**Lee.** config; documentos; `<estado>/records/`

**Muestra.** cuántos releer de cuántos, renombrados, borrados, citas rotas

**Escribe.** nada: no escribe

**Skills.** **document-intake**, **project-record**

### `/criterio-portfolio:portfolio-scan`

**Qué hace.** Lee la carpeta y produce o actualiza una ficha por proyecto. Puerta de entrada

**Argumento.** `[ruta] o vacío para la configurada`

**Lee.** config; documentos; `<estado>/records/`

**Muestra.** plan de lectura (cuántos de cuántos), fichas tocadas, campos not_found

**Escribe.** `<estado>/records/<código>.json`; `<estado>/snapshots/<fecha>.json`

**Skills.** **baseline-variance**, **commitment-tracking**, **document-intake**, **project-record**, **raid-taxonomy**, **vendor-control**

### `/criterio-portfolio:portfolio-report`

**Qué hace.** Informe consolidado: qué cambió, qué se contradice, qué está en silencio, qué no tiene sustento

**Argumento.** `[ppt|pdf|html] o vacío`

**Lee.** config; `<estado>/records/`; `<estado>/snapshots/`

**Muestra.** informe con cifras copiadas de `compute`, diff contra la instantánea anterior

**Escribe.** `<informes>/<fecha>.<formato>`; `<estado>/snapshots/<fecha>.json`

**Skills.** **baseline-variance**, **portfolio-health**

### `/criterio-portfolio:status-report`

**Qué hace.** Estado de un proyecto, y las señales que su semáforo declarado no explica

**Argumento.** `<código del proyecto>`

**Lee.** config; `<estado>/records/<código>.json`

**Muestra.** declarado frente a sustentado, desviación, lo abierto, el silencio

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**, **commitment-tracking**, **project-record**, **raid-taxonomy**

### `/criterio-portfolio:health-check`

**Qué hace.** Diagnostica un proyecto desde cero contra la evidencia, sin asumir nada de su informe

**Argumento.** `<código o nombre del proyecto>`

**Lee.** config; documentos del proyecto

**Muestra.** dictamen por afirmación: sostenida, no sostenida, sin documento

**Escribe.** `<estado>/records/<código>.json`

**Skills.** **baseline-variance**, **commitment-tracking**, **governance-artifacts**, **project-diagnosis**, **project-record**, **raid-taxonomy**

### `/criterio-portfolio:project-history`

**Qué hace.** Qué pasó en un proyecto, con la línea de tiempo y desde cuándo lo declarado no se sostiene

**Argumento.** `<código del proyecto> [desde AAAA-MM]`

**Lee.** config; documentos del proyecto; `<estado>/records/`; `<estado>/corridas.json`

**Muestra.** línea de tiempo, replanificaciones, cambios de gobierno, compromisos repetidos, punto de separación

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**, **commitment-tracking**, **portfolio-history**

### `/criterio-portfolio:steering-pack`

**Qué hace.** Material de comité como paquete de decisiones, no como informe de avance

**Argumento.** `[fecha del comité] o vacío`

**Lee.** config; `<estado>/records/`; `<estado>/corridas.json`

**Muestra.** cada punto como decisión cerrada, con quién decide

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**, **raid-taxonomy**

### `/criterio-portfolio:raid-log`

**Qué hace.** Riesgos, supuestos, incidencias y dependencias, incluidos los que se dijeron y nadie registró

**Argumento.** `<código del proyecto> o 'portafolio'`

**Lee.** config; `<estado>/records/`; actas y minutas

**Muestra.** RAID actualizado y lo dicho sin registrar

**Escribe.** `<estado>/records/<código>.json (raid)`

**Skills.** **raid-taxonomy**

### `/criterio-portfolio:change-control`

**Qué hace.** Evalúa un cambio en alcance, tiempo y costo, calcula a quién alcanza, y crea línea base nueva sin borrar la anterior

**Argumento.** `<código del proyecto> <qué cambia>`

**Lee.** config; `<estado>/records/`

**Muestra.** las tres dimensiones, efecto en el portafolio, quién decide

**Escribe.** `<estado>/records/<código>.json (plan.baseline, changes)`

**Skills.** **baseline-variance**, **governance-artifacts**

### `/criterio-portfolio:budget-tracking`

**Qué hace.** Aprobado, comprometido, ejecutado y proyección, con desviación contra las dos líneas base

**Argumento.** `<código del proyecto> o 'portafolio'`

**Lee.** config; `<estado>/records/`

**Muestra.** las cuatro cifras con fuente y fecha, % comprometido, desviación de costo

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**

### `/criterio-portfolio:vendor-tracking`

**Qué hace.** Entregables contractuales contra evidencia de recibo y contra facturación

**Argumento.** `<código del proyecto> [proveedor]`

**Lee.** config; `<estado>/records/<código>.json`

**Muestra.** entregable por entregable: estado, evidencia, facturado

**Escribe.** nada: no escribe

**Skills.** **commitment-tracking**, **project-record**, **vendor-control**

### `/criterio-portfolio:product-view`

**Qué hace.** El estado de un producto a través de todos los proyectos que lo construyen

**Argumento.** `[nombre del producto]`

**Lee.** config; `<estado>/records/`

**Muestra.** proyectos del producto, señales sumadas, fecha del más tardío, dinero sumado

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**

### `/criterio-portfolio:project-charter`

**Qué hace.** Revisa o redacta el acta, señalando qué falta y qué consecuencia tiene

**Argumento.** `<código del proyecto> [revisar|redactar]`

**Lee.** config; documentos de gobierno

**Muestra.** lo que falta y su consecuencia, o el borrador

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**

### `/criterio-portfolio:project-closure`

**Qué hace.** Cierra contra el criterio de éxito pactado, con lecciones que se puedan sustentar

**Argumento.** `<código del proyecto>`

**Lee.** config; `<estado>/records/<código>.json`; documentos del proyecto

**Muestra.** entregado contra comprometido, números de cierre, RAID cerrado, lecciones

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**, **governance-artifacts**

## Rostrum · el portal de todas las familias

### `/criterio-server:server-setup`

**Qué hace.** El mapa: qué agentes de qué familias hay en la carpeta de trabajo y dónde está el estado de cada uno

**Argumento.** `[carpeta de trabajo] o vacío`

**Lee.** `.criterio/<área>/[<instancia>/]config.json`

**Muestra.** el mapa encontrado, lo que falta y lo que se deja fuera

**Escribe.** `.criterio/rostrum/config.json`; `.criterio/terminos/ (aceptar)`

### `/criterio-server:server-start`

**Qué hace.** El portal levantado sobre el mapa, y qué pedirle a la organización para publicarlo

**Argumento.** `[rato|servicio] o vacío`

**Lee.** `.criterio/rostrum/config.json`; el estado de cada entrada del mapa

**Muestra.** las direcciones del portal y qué se pide para publicarlo

**Escribe.** `<estado>/peticiones/<id>.json (el servidor, por cada petición)`
