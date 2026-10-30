# Manual de los comandos de Criterio

Los 83 comandos de las familias PMO, CFO, CLO y EA y de Rostrum. Primero la PMO, en el orden en que la usa: Alba define el producto, Samuel ejecuta un proyecto y Vera consolida el portafolio; después la CFO —Clara cierra los libros, Tomás lleva el presupuesto y Áurea la tesorería—, la CLO —Fidel lleva los contratos y Constanza el cumplimiento— y la EA —Ofelia prepara la oficina del ejecutivo—; y al final Rostrum, que publica lo de todas. Cada comando se escribe con el prefijo de su plugin; el autocompletado hace el resto.

Este manual se genera con `scripts/manual.py` desde la tabla del README de cada plugin y su `contratos.json`, el mismo contrato que las pruebas comparan contra cada corrida. No se edita a mano.

## Alba · un producto

### `/criterio-product:product-setup`

**Qué hace.** **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y contrasta la definición que ya tengas

**Argumento.** `[ruta de la carpeta del producto] o vacío`

**Procesa.** config (si existe); documentos del producto

**Muestra.** qué hay escrito, cuatro preguntas, definición contra evidencia

**Escribe.** `.criterio/producto/<código>/config.json`; `<estado>/ (init)`; `<estado>/producto.json`; `<estado>/requirements/<REQ>.json`; `.criterio/terminos/ (aceptar: comprobante .md, .pdf y .sha256, y aceptaciones.json)`; `<raíz>/_CRITERIO_PRODUCTO.txt (marcar-raiz, con permiso)`

**Skills.** **demand-evidence**, **document-intake**, **product-metrics**, **requirement-record**

### `/criterio-product:product-discovery`

**Qué hace.** Entrevistas y tickets en temas con la cita de quién lo dijo, y el tema que lleva meses dicho sin que nadie lo convierta en nada

**Argumento.** `[carpeta o archivo] o vacío`

**Procesa.** config; material de descubrimiento; `<estado>/requirements/`

**Muestra.** temas por problema, con quién lo dijo y cuándo

**Escribe.** `<estado>/requirements/<REQ>.json (evidence)`

**Skills.** **demand-evidence**, **discovery-synthesis**, **document-intake**, **product-metrics**, **requirement-record**

### `/criterio-product:product-requirements`

**Qué hace.** El registro con sus vacíos: sin doliente, sin criterio, aceptado sin que nadie lo pidiera, y lo que nadie decide

**Argumento.** `[REQ-xxx] o vacío`

**Procesa.** config; `<estado>/requirements/`

**Muestra.** vacíos por requerimiento y quién los cierra

**Escribe.** `<estado>/requirements/<REQ>.json`

**Skills.** **product-health**, **requirement-record**

### `/criterio-product:product-definition`

**Qué hace.** La definición contra la evidencia de demanda, y dónde el negocio y los datos no coinciden

**Argumento.** `[ruta de la definición] o vacío`

**Procesa.** config; definición; `<estado>/requirements/`; `<estado>/producto.json`

**Muestra.** afirmación por afirmación en tres clases, cifras contrastadas, barrido normativo

**Escribe.** `<estado>/producto.json (definition)`

**Skills.** **assumption-tracking**, **demand-evidence**, **product-metrics**, **raid-taxonomy**, **regulatory-sweep**

### `/criterio-product:product-trace`

**Qué hace.** Requerimiento → decisión → proyecto → entregable, y las dos brechas de arriba

**Argumento.** `[REQ-xxx o proyecto] o vacío`

**Procesa.** config; `<estado>/requirements/`; fichas de proyecto

**Muestra.** cadena por requerimiento, cobertura, lo construido sin requerimiento

**Escribe.** nada: no escribe

**Skills.** **requirement-record**

### `/criterio-product:product-spec`

**Qué hace.** El borrador de especificación con criterios verificables y los vacíos señalados, no rellenados

**Argumento.** `[REQ-xxx, …] o vacío`

**Procesa.** config; `<estado>/requirements/`

**Muestra.** secciones con sus REQ, criterios verificables, vacíos con dueño

**Escribe.** nada: no escribe

**Skills.** **assumption-tracking**, **regulatory-sweep**, **requirement-record**, **specification-draft**

### `/criterio-product:product-charter`

**Qué hace.** El acta de constitución: donde nace la ficha y el escritor cambia de manos

**Argumento.** `<REQ-xxx>`

**Procesa.** config; `<estado>/requirements/`

**Muestra.** borrador, supuestos que pasan al proyecto, qué no entra

**Escribe.** `<estado>/records/<código>.json (solo con acta firmada)`

**Skills.** **assumption-tracking**, **demand-evidence**, **governance-artifacts**, **project-record**, **raid-taxonomy**, **requirement-record**

### `/criterio-product:product-business-case`

**Qué hace.** La estructura del caso de negocio con cada cifra citada, y los vacíos con quién los produce

**Argumento.** `[ruta del caso] o vacío`

**Procesa.** config; caso de negocio; `<estado>/requirements/`; `<estado>/producto.json`

**Muestra.** cifras en tres clases (medida, declarada, supuesta), costos, vacíos

**Escribe.** nada: no escribe

**Skills.** **assumption-tracking**, **product-metrics**, **requirement-record**

### `/criterio-product:product-publish`

**Qué hace.** Publica tu ficha donde los demás productos la puedan leer

**Argumento.** `[carpeta de publicados] o vacío`

**Procesa.** config; `<estado>/producto.json`; `<estado>/requirements/`

**Muestra.** qué publica y la ruta exacta

**Escribe.** `<publicados>/<código>.json`

### `/criterio-product:product-overlap`

**Qué hace.** Dónde te pisas con otro producto: la misma métrica contada dos veces, el mismo proyecto, el mismo segmento

**Argumento.** `[código de otro producto] o vacío`

**Procesa.** config; `<estado>/producto.json`; productos publicados

**Muestra.** métricas compartidas, proyectos compartidos, segmento

**Escribe.** nada: no escribe

**Skills.** **product-metrics**, **requirement-record**

### `/criterio-product:product-wake`

**Qué hace.** **El que se le pone a un reloj.** Lo que cruzó un umbral sin que nadie hiciera nada

**Argumento.** `[AAAA-MM-DD]`

**Procesa.** config; `<estado>/cadencia.json`; `<estado>/requirements/`

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/cadencia.json`; `<estado>/snapshots/<fecha>.json`

**Skills.** **assumption-tracking**, **document-intake**, **product-health**

## Samuel · un proyecto

### `/criterio-project:pm-setup`

**Qué hace.** **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y lee tu última minuta

**Argumento.** `[ruta de la carpeta] o vacío`

**Procesa.** config (si existe); documentos del proyecto

**Muestra.** qué encontró, cuatro preguntas, compromisos de la última reunión

**Escribe.** `.criterio/proyecto/<código>/config.json`; `<estado>/ (init)`; `<estado>/records/<código>.json`; `.criterio/terminos/ (aceptar: comprobante .md, .pdf y .sha256, y aceptaciones.json)`; `<raíz>/_CRITERIO_PROYECTO.txt (marcar-raiz, con permiso)`

**Skills.** **commitment-tracking**, **document-intake**, **project-record**

### `/criterio-project:pm-agenda`

**Qué hace.** La agenda con los puntos que necesitan a alguien en la sala, y con lo que esta reunión no puede mover

**Argumento.** `[fecha de la reunión] o vacío`

**Procesa.** config; `<estado>/records/<código>.json`; `<estado>/snapshots/`

**Muestra.** puntos con tiempo y cita; la suma cabe

**Escribe.** nada: no escribe

**Skills.** **raid-taxonomy**

### `/criterio-project:pm-minutes`

**Qué hace.** El acta sobre la transcripción o las notas, con cada cosa atribuida a una persona

**Argumento.** `<ruta de la transcripción o las notas>`

**Procesa.** config; la transcripción; `<estado>/records/<código>.json`

**Muestra.** acta con acuerdos, compromisos, decisiones, riesgos y contradicciones

**Escribe.** `<estado>/records/<código>.json (commitments, raid)`; `30-reuniones/<fecha>-acta.md`

**Skills.** **commitment-tracking**, **document-intake**, **raid-taxonomy**

### `/criterio-project:pm-commitments`

**Qué hace.** Quién prometió qué, qué venció sin evidencia, y qué se viene reprogramando reunión tras reunión

**Argumento.** `[ruta de una minuta] o vacío`

**Procesa.** config; `<estado>/records/<código>.json`

**Muestra.** compromisos ordenados por lo que necesita a alguien

**Escribe.** `<estado>/records/<código>.json (commitments)`

**Skills.** **commitment-tracking**

### `/criterio-project:pm-report`

**Qué hace.** El informe semanal completo **salvo el estado**, que lo declaras tú

**Argumento.** `[fecha de corte] o vacío`

**Procesa.** config; `<estado>/records/<código>.json`; `<estado>/snapshots/`

**Muestra.** informe contra la corrida anterior, declaración contrastada, cuatro cifras

**Escribe.** `<estado>/snapshots/<fecha>.json`

**Skills.** **baseline-variance**

### `/criterio-project:pm-publish`

**Qué hace.** Publica tu ficha donde la PMO la puede leer

**Argumento.** `[confirmar] o vacío`

**Procesa.** config; `<estado>/records/<código>.json`

**Muestra.** qué va a publicar, y la ruta exacta

**Escribe.** `00-gobierno/ficha-pm.json`

**Skills.** **project-record**

### `/criterio-project:pm-plan`

**Qué hace.** El primer borrador del plan y la WBS desde el acta, **sin comprometer ninguna fecha**

**Argumento.** `[ruta del acta] o vacío`

**Procesa.** config; acta de constitución

**Muestra.** WBS por entregable, supuestos, qué falta para fechar

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**, **raid-taxonomy**

### `/criterio-project:pm-escalate`

**Qué hace.** Lo que excede tu autoridad, como pregunta cerrada, con a quién alcanza calculado

**Argumento.** `[qué se escala] o vacío`

**Procesa.** config; `<estado>/records/`

**Muestra.** pregunta cerrada, opciones, efecto, quién decide

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**, **raid-taxonomy**

### `/criterio-project:pm-wake`

**Qué hace.** **El que se le pone a un reloj.** Mira qué toca según tu reunión, y si no toca nada se calla

**Argumento.** `[AAAA-MM-DD]`

**Procesa.** config; `<estado>/cadencia.json`

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/cadencia.json`; `<estado>/records/<código>.json (commitments, solo si el barrido trae una minuta)`

**Skills.** **commitment-tracking**, **document-intake**

## Vera · el portafolio

### `/criterio-portfolio:portfolio-setup`

**Qué hace.** **Lo primero que se corre.** Mira tus carpetas, hace cinco preguntas y produce el primer informe sobre tus propios documentos

**Argumento.** `[ruta de la carpeta] o vacío`

**Procesa.** config (si existe); documentos

**Muestra.** qué encontró en la carpeta, cinco preguntas, las señales de `compute` sobre tres proyectos

**Escribe.** `.criterio/portafolio/config.json`; `<estado>/ (init)`; `<estado>/records/<código>.json (tres)`; `.criterio/terminos/ (aceptar: comprobante .md, .pdf y .sha256, y aceptaciones.json)`; `<raíz>/_CRITERIO_PORTAFOLIO.txt (marcar-raiz, con permiso)`

**Skills.** **commitment-tracking**, **document-intake**, **portfolio-health**, **project-record**

### `/criterio-portfolio:portfolio-wake`

**Qué hace.** **Lo que el reloj invoca.** Mira qué toca hoy, lo hace, y si no toca nada se calla

**Argumento.** `[AAAA-MM-DD para simular otro día]`

**Procesa.** config; `<estado>/cadencia.json`; `<estado>/peticiones/`

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/cadencia.json`

**Skills.** **document-intake**, **portfolio-health**

### `/criterio-portfolio:document-index`

**Qué hace.** Qué documentos cambiaron de verdad, qué hay que releer y qué citas dejaron de resolver

**Argumento.** `[código del proyecto]`

**Procesa.** config; documentos; `<estado>/records/`

**Muestra.** cuántos releer de cuántos, renombrados, borrados, citas rotas

**Escribe.** nada: no escribe

**Skills.** **document-intake**, **project-record**

### `/criterio-portfolio:portfolio-scan`

**Qué hace.** Lee la carpeta y produce o actualiza una ficha por proyecto. Puerta de entrada

**Argumento.** `[ruta] o vacío para la configurada`

**Procesa.** config; documentos; `<estado>/records/`

**Muestra.** plan de lectura (cuántos de cuántos), fichas tocadas, campos not_found

**Escribe.** `<estado>/records/<código>.json`; `<estado>/snapshots/<fecha>.json`

**Skills.** **baseline-variance**, **commitment-tracking**, **document-intake**, **project-record**, **raid-taxonomy**, **vendor-control**

### `/criterio-portfolio:portfolio-report`

**Qué hace.** Informe consolidado: qué cambió, qué se contradice, qué está en silencio, qué no tiene sustento

**Argumento.** `[ppt|pdf|html] o vacío`

**Procesa.** config; `<estado>/records/`; `<estado>/snapshots/`

**Muestra.** informe con cifras copiadas de `compute`, diff contra la instantánea anterior

**Escribe.** `<informes>/<fecha>.<formato>`; `<estado>/snapshots/<fecha>.json`

**Skills.** **baseline-variance**, **portfolio-health**

### `/criterio-portfolio:status-report`

**Qué hace.** Estado de un proyecto, y las señales que su semáforo declarado no explica

**Argumento.** `<código del proyecto>`

**Procesa.** config; `<estado>/records/<código>.json`

**Muestra.** declarado frente a sustentado, desviación, lo abierto, el silencio

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**, **commitment-tracking**, **project-record**, **raid-taxonomy**

### `/criterio-portfolio:health-check`

**Qué hace.** Diagnostica un proyecto desde cero contra la evidencia, sin asumir nada de su informe

**Argumento.** `<código o nombre del proyecto>`

**Procesa.** config; documentos del proyecto

**Muestra.** dictamen por afirmación: sostenida, no sostenida, sin documento

**Escribe.** `<estado>/records/<código>.json`

**Skills.** **baseline-variance**, **commitment-tracking**, **governance-artifacts**, **project-diagnosis**, **project-record**, **raid-taxonomy**

### `/criterio-portfolio:project-history`

**Qué hace.** Qué pasó en un proyecto, con la línea de tiempo y desde cuándo lo declarado no se sostiene

**Argumento.** `<código del proyecto> [desde AAAA-MM]`

**Procesa.** config; documentos del proyecto; `<estado>/records/`; `<estado>/corridas.json`

**Muestra.** línea de tiempo, replanificaciones, cambios de gobierno, compromisos repetidos, punto de separación

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**, **commitment-tracking**, **portfolio-history**

### `/criterio-portfolio:steering-pack`

**Qué hace.** Material de comité como paquete de decisiones, no como informe de avance

**Argumento.** `[fecha del comité] o vacío`

**Procesa.** config; `<estado>/records/`; `<estado>/corridas.json`

**Muestra.** cada punto como decisión cerrada, con quién decide

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**, **raid-taxonomy**

### `/criterio-portfolio:raid-log`

**Qué hace.** Riesgos, supuestos, incidencias y dependencias, incluidos los que se dijeron y nadie registró

**Argumento.** `<código del proyecto> o 'portafolio'`

**Procesa.** config; `<estado>/records/`; actas y minutas

**Muestra.** RAID actualizado y lo dicho sin registrar

**Escribe.** `<estado>/records/<código>.json (raid)`

**Skills.** **raid-taxonomy**

### `/criterio-portfolio:change-control`

**Qué hace.** Evalúa un cambio en alcance, tiempo y costo, calcula a quién alcanza, y crea línea base nueva sin borrar la anterior

**Argumento.** `<código del proyecto> <qué cambia>`

**Procesa.** config; `<estado>/records/`

**Muestra.** las tres dimensiones, efecto en el portafolio, quién decide

**Escribe.** `<estado>/records/<código>.json (plan.baseline, changes)`

**Skills.** **baseline-variance**, **governance-artifacts**

### `/criterio-portfolio:budget-tracking`

**Qué hace.** Aprobado, comprometido, ejecutado y proyección, con desviación contra las dos líneas base

**Argumento.** `<código del proyecto> o 'portafolio'`

**Procesa.** config; `<estado>/records/`

**Muestra.** las cuatro cifras con fuente y fecha, % comprometido, desviación de costo

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**

### `/criterio-portfolio:vendor-tracking`

**Qué hace.** Entregables contractuales contra evidencia de recibo y contra facturación

**Argumento.** `<código del proyecto> [proveedor]`

**Procesa.** config; `<estado>/records/<código>.json`

**Muestra.** entregable por entregable: estado, evidencia, facturado

**Escribe.** nada: no escribe

**Skills.** **commitment-tracking**, **project-record**, **vendor-control**

### `/criterio-portfolio:product-view`

**Qué hace.** El estado de un producto a través de todos los proyectos que lo construyen

**Argumento.** `[nombre del producto]`

**Procesa.** config; `<estado>/records/`

**Muestra.** proyectos del producto, señales sumadas, fecha del más tardío, dinero sumado

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**

### `/criterio-portfolio:project-charter`

**Qué hace.** Revisa o redacta el acta, señalando qué falta y qué consecuencia tiene

**Argumento.** `<código del proyecto> [revisar|redactar]`

**Procesa.** config; documentos de gobierno

**Muestra.** lo que falta y su consecuencia, o el borrador

**Escribe.** nada: no escribe

**Skills.** **governance-artifacts**

### `/criterio-portfolio:project-closure`

**Qué hace.** Cierra contra el criterio de éxito pactado, con lecciones que se puedan sustentar

**Argumento.** `<código del proyecto>`

**Procesa.** config; `<estado>/records/<código>.json`; documentos del proyecto

**Muestra.** entregado contra comprometido, números de cierre, RAID cerrado, lecciones

**Escribe.** nada: no escribe

**Skills.** **baseline-variance**, **governance-artifacts**

## Clara · el cierre

### `/criterio-finance:finance-setup`

**Qué hace.** La configuración, el inventario de la carpeta y la primera ficha del cierre

**Argumento.** `[ruta de la carpeta] o vacío`

**Procesa.** documentos de la entidad

**Muestra.** inventario, preguntas, estado del cierre

**Escribe.** `.criterio/finanzas/<entidad>/config.json`; `<estado>/ (init)`; `<estado>/cierre/<AAAA-MM>/ficha.json`; `.criterio/terminos/ (aceptar)`; `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`; `<raíz>/_CRITERIO_FINANZAS.txt (marcar-raiz, con permiso)`

**Skills.** **close-checklist**, **close-record**, **finance-intake**

### `/criterio-finance:close-scan`

**Qué hace.** La ficha del cierre al día, con lo que cambió y las señales nuevas

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<estado>/indice.json`; documentos del periodo

**Muestra.** qué cambió y las señales

**Escribe.** `<estado>/indice.json`; `<estado>/cache/`; `<estado>/cierre/<AAAA-MM>/ficha.json`; `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **close-record**, **finance-intake**

### `/criterio-finance:close-status`

**Qué hace.** El estado del cierre: declarado contra evidenciado, tarea por tarea

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `00-referencia/checklist-cierre`; `<AAAA-MM>/40-soportes/`; ficha

**Muestra.** tabla de tareas, avance, ruta crítica

**Escribe.** `<estado>/cierre/<AAAA-MM>/ficha.json (declared)`; `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **close-checklist**, **close-record**

### `/criterio-finance:bank-reconcile`

**Qué hace.** La conciliación de cada cuenta bancaria, con sus partidas abiertas por antigüedad

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<AAAA-MM>/20-bancos/`

**Muestra.** conciliación por cuenta y partidas abiertas

**Escribe.** `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **reconciliation**

### `/criterio-finance:account-reconcile`

**Qué hace.** La conciliación de cada cuenta contra su auxiliar

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<AAAA-MM>/10-contabilidad/auxiliares/`; balance

**Muestra.** conciliación por cuenta

**Escribe.** `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **reconciliation**

### `/criterio-finance:ledger-check`

**Qué hace.** El cuadre del balance y del mayor, cuenta por cuenta

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<AAAA-MM>/10-contabilidad/`; `00-referencia/plan-de-cuentas`

**Muestra.** cuadre y cuentas con diferencia

**Escribe.** `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **ledger-tieout**

### `/criterio-finance:einvoice-check`

**Qué hace.** Todas las facturas electrónicas del periodo contra la contabilidad, no una muestra

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<AAAA-MM>/30-facturacion/`; libro mayor

**Muestra.** cruce y señales

**Escribe.** `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **einvoice-matching**

### `/criterio-finance:audit-pack`

**Qué hace.** El índice del paquete del auditor, con el estado de cada requerimiento

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<AAAA-MM>/50-auditoria/`; ficha

**Muestra.** índice de requerimientos

**Escribe.** `<estado>/cierre/<AAAA-MM>/ficha.json (audit_requests)`; `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **audit-support**, **close-record**

### `/criterio-finance:finance-wake`

**Qué hace.** Lo que toca hoy en el cierre; si no toca nada, se calla

**Argumento.** `[AAAA-MM-DD]`

**Procesa.** `<estado>/corridas/registro.json`; `<estado>/peticiones/`; config

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/indice.json`; `<estado>/cierre/<AAAA-MM>/resultados.json`; `<estado>/cierre/<AAAA-MM>/reporte-<comando>.md`; `<estado>/peticiones/<id>.json (responder)`

**Skills.** **finance-intake**

## Tomás · el presupuesto

### `/criterio-budget:budget-setup`

**Qué hace.** La configuración, el inventario y la primera ficha del presupuesto de cada área

**Argumento.** `[ruta de la carpeta] o vacío`

**Procesa.** documentos de la entidad

**Muestra.** inventario, preguntas, primera ejecución contra lo aprobado

**Escribe.** `.criterio/presupuesto/<entidad>/config.json`; `<estado>/ (init)`; `<estado>/presupuesto/<AAAA>/ficha.json`; `.criterio/terminos/ (aceptar)`; `<estado>/presupuesto/<AAAA>/resultados.json`; `<estado>/presupuesto/<AAAA>/reporte-<comando>.md`; `<raíz>/_CRITERIO_FINANZAS.txt (marcar-raiz, con permiso)`

**Skills.** **budget-record**, **finance-intake**

### `/criterio-budget:budget-scan`

**Qué hace.** Las fichas del presupuesto al día, con lo que cambió y las señales nuevas

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<estado>/indice.json`; documentos

**Muestra.** qué cambió y las señales

**Escribe.** `<estado>/indice.json`; `<estado>/cache/`; `<estado>/presupuesto/<AAAA>/ficha.json`; `<estado>/presupuesto/<AAAA>/resultados.json`; `<estado>/presupuesto/<AAAA>/reporte-<comando>.md`

**Skills.** **budget-record**, **finance-intake**

### `/criterio-budget:variance-report`

**Qué hace.** Aprobado, ejecutado, comprometido, disponible y desviación por área y cuenta

**Argumento.** `[AAAA-MM]`

**Procesa.** config; presupuesto; contabilidad; compromisos; ficha

**Muestra.** tabla por área y línea

**Escribe.** `<estado>/presupuesto/<AAAA>/resultados.json`; `<estado>/presupuesto/<AAAA>/reporte-<comando>.md`

**Skills.** **variance-analysis**

### `/criterio-budget:forecast`

**Qué hace.** La proyección al cierre del año, con su supuesto declarado

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<AAAA>/30-proyecciones/`; ejecución; compromisos

**Muestra.** tres proyecciones por línea

**Escribe.** `<estado>/presupuesto/<AAAA>/resultados.json`; `<estado>/presupuesto/<AAAA>/reporte-<comando>.md`

**Skills.** **forecast-method**

### `/criterio-budget:transfer-log`

**Qué hace.** Cada traslado con su acta, y los que no la tienen

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<AAAA>/10-aprobado/`; ficha (minutes)

**Muestra.** registro de traslados

**Escribe.** `<estado>/presupuesto/<AAAA>/ficha.json (minutes)`; `<estado>/presupuesto/<AAAA>/resultados.json`; `<estado>/presupuesto/<AAAA>/reporte-<comando>.md`

**Skills.** **budget-record**, **transfer-control**

### `/criterio-budget:budget-committee-pack`

**Qué hace.** El material del comité de presupuesto como paquete de decisiones

**Argumento.** `[AAAA-MM]`

**Procesa.** config; resultados; ficha (committee_commitments)

**Muestra.** puntos de decisión y compromisos del comité anterior

**Escribe.** `<estado>/presupuesto/<AAAA>/ficha.json (committee_commitments)`; `<estado>/presupuesto/<AAAA>/resultados.json`; `<estado>/presupuesto/<AAAA>/reporte-<comando>.md`

**Skills.** **budget-record**, **committee-pack**

### `/criterio-budget:budget-wake`

**Qué hace.** Lo que toca hoy en el presupuesto; si no toca nada, se calla

**Argumento.** `[AAAA-MM-DD]`

**Procesa.** `<estado>/corridas/registro.json`; `<estado>/peticiones/`; config

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/indice.json`; `<estado>/presupuesto/<AAAA>/resultados.json`; `<estado>/presupuesto/<AAAA>/reporte-<comando>.md`; `<estado>/peticiones/<id>.json (responder)`

**Skills.** **finance-intake**

## Áurea · la tesorería

### `/criterio-treasury:treasury-setup`

**Qué hace.** La configuración, el inventario y la primera posición de caja

**Argumento.** `[ruta de la carpeta] o vacío`

**Procesa.** documentos de la entidad

**Muestra.** inventario, preguntas, primera posición de caja

**Escribe.** `.criterio/tesoreria/<entidad>/config.json`; `<estado>/ (init)`; `.criterio/terminos/ (aceptar)`; `<estado>/tesoreria/<AAAA-MM>/resultados.json`; `<estado>/tesoreria/<AAAA-MM>/reporte-<comando>.md`; `<raíz>/_CRITERIO_FINANZAS.txt (marcar-raiz, con permiso)`

**Skills.** **finance-intake**

### `/criterio-treasury:treasury-scan`

**Qué hace.** La tesorería al día, con lo que cambió y las señales nuevas

**Argumento.** `[AAAA-MM]`

**Procesa.** config; `<estado>/indice.json`; documentos

**Muestra.** qué cambió y las señales nuevas

**Escribe.** `<estado>/indice.json`; `<estado>/tesoreria/<AAAA-MM>/resultados.json`; `<estado>/tesoreria/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **finance-intake**

### `/criterio-treasury:cash-position`

**Qué hace.** La caja de cada cuenta contra su mínimo y su proyección, y la exposición cambiaria

**Argumento.** `[AAAA-MM]`

**Procesa.** config; extractos; flujo proyectado; política

**Muestra.** tabla por cuenta y por moneda

**Escribe.** `<estado>/tesoreria/<AAAA-MM>/resultados.json`; `<estado>/tesoreria/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **treasury-control**

### `/criterio-treasury:payment-check`

**Qué hace.** Cada pago programado contra quién puede aprobarlo

**Argumento.** `[AAAA-MM]`

**Procesa.** config; programa de pagos; política; matriz de firmas

**Muestra.** tabla por pago

**Escribe.** `<estado>/tesoreria/<AAAA-MM>/resultados.json`; `<estado>/tesoreria/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **treasury-control**

### `/criterio-treasury:debt-watch`

**Qué hace.** La deuda contra su vencimiento y lo que exige su contrato

**Argumento.** `[AAAA-MM]`

**Procesa.** config; registro de la deuda; covenants; balance de comprobación

**Muestra.** covenants y obligaciones por vencimiento

**Escribe.** `<estado>/tesoreria/<AAAA-MM>/resultados.json`; `<estado>/tesoreria/<AAAA-MM>/reporte-<comando>.md`

**Skills.** **treasury-control**

### `/criterio-treasury:treasury-wake`

**Qué hace.** Lo que toca hoy en la tesorería; si no toca nada, se calla

**Argumento.** `[AAAA-MM-DD]`

**Procesa.** `<estado>/corridas/registro.json`; `<estado>/peticiones/`; config

**Muestra.** qué tocaba y qué hizo, o nada

**Escribe.** `<estado>/indice.json`; `<estado>/tesoreria/<AAAA-MM>/resultados.json`; `<estado>/tesoreria/<AAAA-MM>/reporte-<comando>.md`; `<estado>/peticiones/<id>.json (responder)`

**Skills.** **finance-intake**

## Fidel · los contratos

### `/criterio-legal:legal-setup`

**Qué hace.** La configuración, el inventario y las primeras fichas de los contratos

**Argumento.** `[ruta de la carpeta de la entidad] o vacío`

**Procesa.** documentos de la entidad

**Muestra.** Configuración guardada; inventario por carpeta; los contratos de `contratos/` contra los del registro; las primeras fichas

**Escribe.** `.criterio/legal/<entidad>/config.json`; `<estado>/ (init)`; `<estado>/indice.json`; `<estado>/cache/`; `<estado>/contratos/<código>.json`; `.criterio/terminos/ (aceptar)`; `<estado>/contratos/resultados.json`; `<estado>/contratos/reporte-obligations-calendar.md`; `<estado>/corridas/salida-legal-setup.md`; `<raíz>/_CRITERIO_LEGAL.txt (marcar-raiz, con permiso)`

**Skills.** **contract-record**, **legal-intake**, **signing-authority**

### `/criterio-legal:contract-scan`

**Qué hace.** Las fichas de los contratos al día, con lo que cambió y las señales nuevas

**Argumento.** `[código del contrato] o vacío para todos`

**Procesa.** config; `<estado>/indice.json`; `contratos/`; `10-registro/`

**Muestra.** Qué cambió; qué contratos son nuevos; las señales nuevas; lo que no se pudo procesar y por qué

**Escribe.** `<estado>/indice.json`; `<estado>/cache/`; `<estado>/contratos/<código>.json`; `<estado>/contratos/resultados.json`; `<estado>/contratos/reporte-contract-scan.md`; `<estado>/corridas/salida-contract-scan.md`

**Skills.** **contract-record**, **legal-intake**

### `/criterio-legal:contract-register`

**Qué hace.** El registro de contratos contra lo que dicen los documentos

**Argumento.** `vacío`

**Procesa.** config; `10-registro/registro-contratos`; `<estado>/contratos/*.json`

**Muestra.** Por contrato: estado declarado y estado según sus fechas, y cada diferencia entre el registro y el documento

**Escribe.** `<estado>/contratos/<código>.json`; `<estado>/contratos/resultados.json`; `<estado>/contratos/reporte-contract-register.md`; `<estado>/corridas/salida-contract-register.md`

**Skills.** **contract-record**

### `/criterio-legal:obligations-calendar`

**Qué hace.** Vencimientos, preavisos y obligaciones, con lo que venció sin evidencia

**Argumento.** `vacío`

**Procesa.** config; `<estado>/contratos/*.json`; `contratos/*/40-ejecucion/`

**Muestra.** El calendario de los próximos días: vencimientos, preavisos y obligaciones; lo vencido sin evidencia y los preavisos que pasaron sin decisión

**Escribe.** `<estado>/contratos/resultados.json`; `<estado>/contratos/reporte-obligations-calendar.md`; `<estado>/corridas/salida-obligations-calendar.md`

**Skills.** **contract-calendar**

### `/criterio-legal:authority-check`

**Qué hace.** Quién firmó cada contrato y con qué facultad

**Argumento.** `vacío`

**Procesa.** config; `<estado>/contratos/*.json`; `00-referencia/matriz-atribuciones`

**Muestra.** Por contrato: quién firmó, su facultad y el monto; los que no tienen firma de las dos partes; los certificados vencidos; sin opinión sobre la validez del contrato

**Escribe.** `<estado>/contratos/resultados.json`; `<estado>/contratos/reporte-authority-check.md`; `<estado>/corridas/salida-authority-check.md`

**Skills.** **signing-authority**

### `/criterio-legal:contract-execution`

**Qué hace.** Lo pagado contra lo pactado, y las garantías contra lo exigido

**Argumento.** `vacío`

**Procesa.** config; `10-registro/pagos`; `<estado>/contratos/*.json`

**Muestra.** Por contrato: valor, pagado, saldo y último pago; cada garantía exigida con la aportada y su vigencia

**Escribe.** `<estado>/contratos/resultados.json`; `<estado>/contratos/reporte-contract-execution.md`; `<estado>/corridas/salida-contract-execution.md`

**Skills.** **payments-guarantees**

### `/criterio-legal:legal-wake`

**Qué hace.** Lo que toca hoy en los contratos; si no toca nada, se calla

**Argumento.** `[AAAA-MM-DD para simular otro día]`

**Procesa.** `<estado>/contratos/*.json`; `<estado>/corridas/`; `<estado>/peticiones/`; config

**Muestra.** Lo que corrió y lo que encontró; si no toca nada, se calla

**Escribe.** `<estado>/indice.json`; `<estado>/contratos/resultados.json`; `<estado>/contratos/reporte-obligations-calendar.md`; `<estado>/corridas/salida-legal-wake.md`; `<estado>/peticiones/<id>.json (responder)`

**Skills.** **legal-intake**

## Constanza · el cumplimiento

### `/criterio-compliance:compliance-setup`

**Qué hace.** La configuración, la matriz revisada y el primer estado del cumplimiento

**Argumento.** `[ruta de la carpeta de la entidad] o vacío`

**Procesa.** documentos de la entidad

**Muestra.** Configuración guardada; la matriz cargada y lo que le falta a cada obligación —responsable, fuente—; el primer estado del periodo

**Escribe.** `.criterio/cumplimiento/<entidad>/config.json`; `<estado>/ (init)`; `<estado>/indice.json`; `<estado>/cache/`; `<estado>/cumplimiento/<AAAA-MM>/ficha.json`; `.criterio/terminos/ (aceptar)`; `<estado>/cumplimiento/<AAAA-MM>/resultados.json`; `<estado>/cumplimiento/<AAAA-MM>/reporte-compliance-status.md`; `<estado>/corridas/salida-compliance-setup.md`; `<raíz>/_CRITERIO_LEGAL.txt (marcar-raiz, con permiso)`

**Skills.** **compliance-record**, **legal-intake**, **obligations-matrix**

### `/criterio-compliance:compliance-scan`

**Qué hace.** La ficha del cumplimiento al día, con lo que cambió y las señales nuevas

**Argumento.** `[AAAA-MM] o vacío`

**Procesa.** config; `<estado>/indice.json`; documentos del periodo

**Muestra.** Qué cambió; qué se agregó a la ficha; las señales nuevas; lo que no se pudo procesar

**Escribe.** `<estado>/indice.json`; `<estado>/cache/`; `<estado>/cumplimiento/<AAAA-MM>/ficha.json`; `<estado>/cumplimiento/<AAAA-MM>/resultados.json`; `<estado>/cumplimiento/<AAAA-MM>/reporte-compliance-scan.md`; `<estado>/corridas/salida-compliance-scan.md`

**Skills.** **compliance-record**, **legal-intake**

### `/criterio-compliance:compliance-status`

**Qué hace.** El estado del cumplimiento: declarado contra evidenciado, obligación por obligación

**Argumento.** `[AAAA-MM] o vacío`

**Procesa.** config; `00-referencia/matriz-obligaciones`; `cumplimiento-<AAAA-MM>/10-evidencias/`; `<estado>/cumplimiento/<AAAA-MM>/ficha.json`

**Muestra.** Estado declarado contra evidenciado; tabla de obligaciones ordenada por criticidad y vencimiento: cumplida con evidencia, cumplida sin evidencia, vencida, en plazo

**Escribe.** `<estado>/cumplimiento/<AAAA-MM>/ficha.json`; `<estado>/cumplimiento/<AAAA-MM>/resultados.json`; `<estado>/cumplimiento/<AAAA-MM>/reporte-compliance-status.md`; `<estado>/corridas/salida-compliance-status.md`

**Skills.** **compliance-record**, **obligations-matrix**

### `/criterio-compliance:policy-review`

**Qué hace.** Cada política con su próxima revisión, y las vencidas

**Argumento.** `vacío`

**Procesa.** config; `20-politicas/indice-politicas`

**Muestra.** Las políticas con la revisión vencida o sin responsable, y las próximas a revisar

**Escribe.** `<estado>/cumplimiento/<AAAA-MM>/resultados.json`; `<estado>/cumplimiento/<AAAA-MM>/reporte-policy-review.md`; `<estado>/corridas/salida-policy-review.md`

**Skills.** **policy-control**

### `/criterio-compliance:regulatory-watch`

**Qué hace.** Las normas nuevas con su evaluación, y las que aplican sin obligación

**Argumento.** `vacío`

**Procesa.** config; `30-normativa/`; `<estado>/cumplimiento/<AAAA-MM>/ficha.json`

**Muestra.** Las normas sin evaluar y las que aplican sin obligación en la matriz; sin opinión sobre el alcance de ninguna norma

**Escribe.** `<estado>/cache/`; `<estado>/cumplimiento/<AAAA-MM>/ficha.json`; `<estado>/cumplimiento/<AAAA-MM>/resultados.json`; `<estado>/cumplimiento/<AAAA-MM>/reporte-regulatory-watch.md`; `<estado>/corridas/salida-regulatory-watch.md`

**Skills.** **compliance-record**, **regulatory-change**

### `/criterio-compliance:reports-cases`

**Qué hace.** Los casos del canal de denuncias contra su plazo

**Argumento.** `vacío`

**Procesa.** config; `40-canal/casos`

**Muestra.** Los casos abiertos por antigüedad y los que pasaron su plazo; sin datos de quién denunció

**Escribe.** `<estado>/cumplimiento/<AAAA-MM>/resultados.json`; `<estado>/cumplimiento/<AAAA-MM>/reporte-reports-cases.md`; `<estado>/corridas/salida-reports-cases.md`

**Skills.** **whistleblowing-channel**

### `/criterio-compliance:compliance-wake`

**Qué hace.** Lo que toca hoy en el cumplimiento; si no toca nada, se calla

**Argumento.** `[AAAA-MM-DD para simular otro día]`

**Procesa.** `00-referencia/matriz-obligaciones`; `<estado>/corridas/`; `<estado>/peticiones/`; config

**Muestra.** Lo que corrió y lo que encontró; si no toca nada, se calla

**Escribe.** `<estado>/indice.json`; `<estado>/cumplimiento/<AAAA-MM>/resultados.json`; `<estado>/cumplimiento/<AAAA-MM>/reporte-compliance-status.md`; `<estado>/corridas/salida-compliance-wake.md`; `<estado>/peticiones/<id>.json (responder)`

**Skills.** **legal-intake**

## Ofelia · la oficina de dirección

### `/criterio-assistant:ea-setup`

**Qué hace.** La configuración, el inventario y los órganos con sus sesiones

**Argumento.** `[ruta de la carpeta de la oficina] o vacío`

**Procesa.** documentos de la oficina

**Muestra.** inventario, órganos y sesiones, preguntas, primer resultado

**Escribe.** `.criterio/direccion/<ejecutivo>/config.json`; `<estado>/ (init)`; `.criterio/terminos/ (aceptar)`; `<estado>/resultados.json`; `<estado>/reporte-ea-setup.md`; `<raíz>/_CRITERIO_DIRECCION.txt (marcar-raiz, con permiso)`

**Skills.** **ea-intake**

### `/criterio-assistant:ea-scan`

**Qué hace.** Las fichas de las reuniones, de la correspondencia, de los viajes y de la agenda

**Argumento.** `[órgano o fecha] o vacío`

**Procesa.** config; agenda .ics; `sesiones de organos/`; correos .eml y .msg; `itinerarios de 30-viajes/`

**Muestra.** las fichas nuevas y cambiadas, las señales

**Escribe.** `<estado>/reuniones/<órgano>-<AAAA-MM-DD>.json`; `<estado>/correspondencia/<correo>.json`; `<estado>/viajes/<itinerario>.json`; `<estado>/resultados.json`; `<estado>/reporte-ea-scan.md`

**Skills.** **commitment-tracking**, **correspondence-record**, **decision-brief**, **ea-intake**, **meeting-record**, **travel-record**

### `/criterio-assistant:ea-agenda`

**Qué hace.** La semana del ejecutivo: cruces, viajes contra la agenda, sesiones sin material y sesiones sin acta

**Argumento.** `[días] o vacío`

**Procesa.** config; agenda .ics; fichas de las reuniones; fichas de los viajes

**Muestra.** la semana: cruces, viajes contra la agenda, sesiones sin material y sin acta

**Escribe.** `<estado>/resultados.json`; `<estado>/reporte-ea-agenda.md`

### `/criterio-assistant:ea-prep`

**Qué hace.** El paquete de la sesión, con la ficha de cada decisión

**Argumento.** `<órgano> <AAAA-MM-DD>`

**Procesa.** config; fichas de las reuniones; material de la sesión

**Muestra.** el paquete de la sesión, sin ordenar las opciones

**Escribe.** `<estado>/reuniones/<órgano>-<AAAA-MM-DD>.json`; `<estado>/resultados.json`; `<estado>/reporte-ea-prep.md`

**Skills.** **decision-brief**

### `/criterio-assistant:ea-minutes`

**Qué hace.** El borrador del acta, con cada acuerdo y compromiso citado

**Argumento.** `<órgano> <AAAA-MM-DD>`

**Procesa.** config; notas de 30-notas

**Muestra.** lo que falta para cerrar el acta

**Escribe.** `90-borradores/BORRADOR-acta-<órgano>-<AAAA-MM-DD>.md`; `<estado>/resultados.json`; `<estado>/reporte-ea-minutes.md`

**Skills.** **minutes-draft**

### `/criterio-assistant:ea-commitments`

**Qué hace.** El estado de los compromisos de dirección, por órgano y por responsable

**Argumento.** `[órgano o responsable] o vacío`

**Procesa.** config; fichas de las reuniones; fichas de proyecto de Samuel, si están

**Muestra.** los compromisos por órgano y por responsable

**Escribe.** `<estado>/resultados.json`; `<estado>/reporte-ea-commitments.md`

**Skills.** **commitment-tracking**

### `/criterio-assistant:ea-mail`

**Qué hace.** La correspondencia que pide respuesta, con sus borradores

**Argumento.** `vacío`

**Procesa.** config; fichas de la correspondencia

**Muestra.** lo que pide respuesta y para cuándo

**Escribe.** `90-borradores/BORRADOR-respuesta-<correo>.md`; `<estado>/resultados.json`; `<estado>/reporte-ea-mail.md`

**Skills.** **correspondence-record**

### `/criterio-assistant:ea-weekly`

**Qué hace.** El resumen de la semana: lo que llegó, lo que vence y lo que falta preparar

**Argumento.** `vacío`

**Procesa.** config; fichas

**Muestra.** un resumen de la semana

**Escribe.** `<estado>/resultados.json`; `<estado>/reporte-ea-weekly.md`

### `/criterio-assistant:ea-wake`

**Qué hace.** Lo que toca hoy en la oficina; si no toca nada, se calla

**Argumento.** `vacío`

**Procesa.** config; fichas; preguntas de Rostrum

**Muestra.** lo que corrió y lo que encontró, o una línea si no toca nada

**Escribe.** `<estado>/corridas/`

## Rostrum · el portal de todas las familias

### `/criterio-server:server-setup`

**Qué hace.** El mapa: qué agentes de qué familias hay en la carpeta de trabajo y dónde está el estado de cada uno

**Argumento.** `[carpeta de trabajo] o vacío`

**Procesa.** `.criterio/<área>/[<instancia>/]config.json`

**Muestra.** el mapa encontrado, lo que falta y lo que se deja fuera

**Escribe.** `.criterio/rostrum/config.json`; `.criterio/terminos/ (aceptar)`

### `/criterio-server:server-start`

**Qué hace.** El portal levantado sobre el mapa, y qué pedirle a la organización para publicarlo

**Argumento.** `[rato|servicio] o vacío`

**Procesa.** `.criterio/rostrum/config.json`; el estado de cada entrada del mapa

**Muestra.** las direcciones del portal y qué se pide para publicarlo

**Escribe.** `<estado>/peticiones/<id>.json (el servidor, por cada petición)`
