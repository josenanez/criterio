# Plan de pruebas · cinco días sobre una organización que cambia

Este plan se ejecuta **en Claude Code, con los tres plugins instalados**, y no desde los
scripts. Es deliberado: los scripts prueban la aritmética, y eso ya está cubierto por las
veintiún puertas de `scripts/verificar.py`. Lo que no está probado —y es la deuda que este
repositorio declara desde el principio— es la cadena completa: **el comando que el modelo
ejecuta, los skills que carga, y la ficha que produce leyendo documentos de verdad.**

Cinco días. **Cada día equivale a una semana de trabajo** de una organización de cincuenta
proyectos y sesenta y cinco productos. El día 1 la organización nace; del 2 al 5 le pasan
semanas encima: minutas nuevas, actas de recibo, replanificaciones, presupuesto que se
mueve, y proyectos que simplemente se callan.

---

## Qué se prueba, y qué no

| Se prueba | No se prueba |
|---|---|
| Los 37 comandos ejecutados por el modelo | Documentación de una organización real |
| Los 18 skills, cargándose cuando el tema aparece | Formatos que no sean markdown y CSV |
| La extracción documento → ficha | Que el resultado le sirva a alguien para decidir |
| El seguimiento entre días: qué cambió, qué se cerró, qué se calló | Rendimiento bajo concurrencia |
| El servidor: que publique y reciba preguntas | Seguridad del servidor expuesto |

**La organización es sintética y la escribió este repositorio.** Eso acota lo que estas
cinco corridas pueden concluir, y el informe de cada día lo repite.

---

## La línea base, ya medida

Antes de poner al modelo a ejecutar comandos había que saber si la cadena determinista
—extraer documentos, calcular señales, calificar contra una clave— es confiable. Se corrió
la simulación completa de cinco semanas y **encontró seis defectos**, todos reales, ninguno
un desacuerdo de contabilidad:

| Dónde estaba | Qué pasaba |
|---|---|
| `extractor.py` · `filas()` | Una fila de datos que repetía la palabra de la columna se descartaba por parecer encabezado. **Ningún requerimiento se extrajo nunca**, y no falló nada |
| `extractor.py` · estado | La extracción no borraba lo anterior: un requerimiento que ya no estaba en ningún documento seguía produciendo hallazgos |
| `extractor.py` · traza | La traza al proyecto se heredaba del producto, así que `requirement_untraced` no podía sonar en un producto que declarara algún proyecto |
| `portafolio.py` · `EVIDENCE_SIGNALS` | Al partir `milestone_overdue` en dos señales, la nueva no entró a la lista que el verde tiene que explicar: partir una señal debilitó en silencio el contraste contra la declaración |
| material · supuestos | El documento no decía si el supuesto se había verificado, así que el lector no tenía más opción que asumir que no: la señal sonaba en los 65 productos y no distinguía nada |
| material · cronograma | Todas las versiones del cronograma llevaban las mismas fechas, así que una replanificación de noventa días no dejaba rastro documental |

Y dos correcciones en la clave de respuestas, que también eran defectos: tres fechas en un
compromiso son **dos** reprogramaciones, no tres; y los meses se cuentan por calendario, no
dividiendo días por treinta.

Corregidos, la cadena califica **100% de precisión y 100% de cobertura los cinco días**,
con el material escrito en las cuatro disposiciones. Está en
[`tests/informes/RESUMEN.md`](informes/RESUMEN.md).

Lo que esa línea base **no** dice: nada sobre los comandos. Mide extracción y aritmética.
Los cinco días de abajo son para lo otro.

---

## Antes de empezar · hoy

### Paso 0.1 · Comprobar que la línea base sigue verde

```
python3 scripts/verificar.py
```

Veintiuna puertas. Si alguna está en rojo se arregla antes de seguir: los cinco días miden
contra ella.

### Paso 0.2 · Instalar los tres agentes

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-portfolio@criterio
/plugin install criterio-project@criterio
/plugin install criterio-product@criterio
```

**Evidencia:** `tests/evidencias/dia-0/instalacion.md` — qué versión quedó instalada y si
algún comando no apareció. Un comando declarado que no aparece en la sesión es un defecto
del manifiesto, y es el primero que hay que ver.

### Paso 0.3 · Levantar la organización

```
python3 tests/sintetico/simulador.py .pruebas/corp-demo --dia 1
```

Deja `.pruebas/corp-demo/` con `documentos/`, `organizacion.json`, la bitácora del día y
`esperado.json`. **Este último es la clave de respuestas** y se deriva de los hechos que el
simulador plantó, con los umbrales copiados de los skills — no importados del código que se
está midiendo. Si las dos reglas se separan, la calificación lo dice, y eso es precisamente
lo que se quiere saber.

La organización vive **dentro del repositorio y fuera de git** — `.pruebas/` está en el
`.gitignore`. No es capricho: una corrida programada arranca en una sesión nueva que solo
alcanza la carpeta del repositorio, y con el material en un temporal el día 2 no
encontraría el estado del día 1 — que es lo único que cinco días pueden medir y una
corrida suelta no.

### Paso 0.4 · Configurar los tres agentes

```
/criterio-portfolio:portfolio-setup      → apuntar a .pruebas/corp-demo/documentos/proyectos
                        y el estado a .pruebas/corp-demo/estado
/criterio-project:pm-setup             → un proyecto: .pruebas/corp-demo/documentos/proyectos/PRY-200-...
/criterio-product:product-setup        → un producto: .pruebas/corp-demo/documentos/productos/PRD-300
```

**Evidencia:** `tests/evidencias/dia-0/setup-<agente>.md` con **cuántas preguntas hizo,
cuáles, cuánto tardó hasta el primer resultado, y qué encontró en ese primer barrido.**
La promesa publicada es *quince minutos*; aquí se mide.

---

## Qué tiene que hacer cada funcionalidad, escrito antes

«Este comando se corrió» no valida nada: un comando puede correr, imprimir algo razonable
y no hacer lo que promete. Así que para cada uno de los 37 está escrito de antemano —en
`tests/sintetico/funcionalidades.py`, y la puerta 23 falla si falta alguno— qué tiene que
producir, **qué deja escrito que lo pruebe**, y dónde lo lee alguien que no estuvo:

```
python3 tests/sintetico/funcionalidades.py             # la matriz completa
python3 tests/sintetico/funcionalidades.py --verificar # la puerta
```

La columna que separa este diseño del anterior es **qué deja**. Un comando que produce algo
y no deja registro no se puede auditar: su resultado vive en una conversación que se cierra.
Hoy la cuenta es **18 de 37 dejan rastro en disco** y **20 de 37 se pueden leer sin
preguntarle a nadie**. Los otros son deuda declarada, no un descuido — y aparecen en la
matriz con ese nombre.

Eso es lo que hace la diferencia entre confiable y creíble. Un director de PMO, un gerente
o un patrocinador entra al portal, abre el histórico de corridas y lee qué se encontró y
desde cuándo, sin pedirle permiso a quien corrió el comando. Si para verificar una
funcionalidad hay que preguntarle al que la ejecutó, no es transparente.

## Cada día, en este orden

### Paso 1 · Pasar una semana

```
python3 tests/sintetico/simulador.py .pruebas/corp-demo --dia <N>
```

Escribe la semana nueva y regenera `esperado.json`. La bitácora del día dice qué le pasó a
cada caso, en una línea: quién se calló, quién reprogramó, quién cerró un hito.

**La organización vive en su propio calendario y avanza una semana por día.** El día 5 cae
en la fecha real y cada anterior está una semana atrás, así que el silencio y la antigüedad
se acumulan de verdad. **Quince de las veinte señales solo aparecen con el tiempo
corriendo** —compromisos vencidos, desviaciones, replanificaciones, evidencia envejecida—,
y con el reloj congelado no podían sonar nunca. Todo lo que lee el material tiene que decir
contra qué fecha mira: `--today <corte>`, que el simulador imprime al generar el día.

Y hay una tensión entre `--todos` y el silencio: si cada caso se mueve cada semana, nadie
se queda callado. La semana probabilística deja proyectos en silencio, que es lo realista;
`--todos` estresa el índice de documentos. Las dos cosas se prueban, pero no en la misma
corrida.

**La disposición de las carpetas rota con el día** —ordenada, plana, revuelta, sin
carpetas— y lo esperado no cambia. Una caída de fiabilidad entre días no es variación: es
una dependencia del layout, y es un defecto.

### Paso 2 · Los diecisiete comandos de Vera

En este orden, que es el de uso real y no el alfabético:

| # | Comando | Qué se verifica | Evidencia |
|---|---|---|---|
| 1 | `/criterio-portfolio:portfolio-wake` | Que diga qué toca hoy — y que **se calle** si no toca nada | `wake.md` |
| 2 | `/criterio-portfolio:document-index` | Cuántos documentos cambiaron de verdad desde ayer, y cuántos no hubo que releer | `index.md` |
| 3 | `/criterio-portfolio:portfolio-scan` | Las cincuenta fichas, con cita en cada dato | `scan.md` |
| 4 | `/criterio-portfolio:portfolio-report` | Qué cambió, qué se contradice, qué está en silencio | `report.md` |
| 5 | `/criterio-portfolio:status-report` | Sobre tres proyectos: el semáforo declarado y lo que no explica | `status.md` |
| 6 | `/criterio-portfolio:health-check` | Un proyecto desde cero, sin mirar su informe | `health.md` |
| 7 | `/criterio-portfolio:project-history` | Desde cuándo lo declarado dejó de sostenerse | `history.md` |
| 8 | `/criterio-portfolio:raid-log` | Riesgos y dependencias, incluidos los dichos y no registrados | `raid.md` |
| 9 | `/criterio-portfolio:change-control` | Mover un proyecto 60 días: **a quién alcanza** | `change.md` |
| 10 | `/criterio-portfolio:budget-tracking` | Las cuatro cifras, y la desviación contra las dos líneas base | `budget.md` |
| 11 | `/criterio-portfolio:vendor-tracking` | Contrato contra recibo contra factura | `vendor.md` |
| 12 | `/criterio-portfolio:product-view` | Un producto a través de los proyectos que lo construyen | `product-view.md` |
| 13 | `/criterio-portfolio:project-charter` | Revisar un acta: qué le falta y qué consecuencia tiene | `charter.md` |
| 14 | `/criterio-portfolio:project-closure` | Cerrar contra el criterio pactado | `closure.md` |
| 15 | `/criterio-portfolio:steering-pack` | El material del comité, como paquete de decisiones | `steering.md` |
| 16 | `/criterio-portfolio:portfolio-server` | Levantar Rostrum | `server.md` |
| 17 | `/criterio-portfolio:portfolio-setup` | **Solo el día 1.** Del 2 al 5 no debe hacer falta | — |

**Y se contrasta contra la clave, no a ojo:**

```
python3 tests/sintetico/contrastar.py .pruebas/corp-demo \
  --alertas <lo que dijo> --aprobado <lo que dijo> --verde <lo que dijo>
```

Imprime las cifras que el informe tiene que acertar y dice en qué se separó — incluido *por
cuánto*, que es lo que distingue un criterio distinto de un cero de más. La primera corrida
acertó las 158 alertas, los 128 hitos sin evidencia y los 30 verdes contradichos, y escribió
el presupuesto aprobado mil veces mayor. La aritmética estaba bien; el agente la transcribió
mal, y ninguna puerta podía verlo porque el script tenía razón.

**Las estadísticas las mide la corrida, no las teclea nadie.** Es la diferencia entre medir
y creer: una cifra que escribe quien conduce la prueba mide su transcripción, y eso vicia el
resultado — es el mismo defecto que este repositorio le encontró a un informe que reescribió
una cifra ya calculada.

Los comandos de los agentes llaman `portafolio.py corrida-inicio` al arrancar y
`portafolio.py corrida` al terminar. Eso deja en `<estado>/corridas.json` los proyectos, los
hallazgos por señal, los documentos releídos y el tiempo, medidos por la propia corrida. Al
cerrar el día se cosechan:

```
python3 tests/sintetico/evidencia.py cosechar \
  --agente portfolio --estado .pruebas/corp-demo/estado --dia <N>
```

Lo único que no puede salir de un script es lo cualitativo —**qué dijo el agente que no
sabía**— y eso se anota aparte, marcado como anotación:

```
python3 tests/sintetico/evidencia.py registrar --agente portfolio \
  --comando portfolio-scan --dia <N> \
  --no-supo "qué dijo que no estaba dicho en ninguna parte" \
  --salida <archivo con lo que imprimió>
```

La página de cada agente distingue las dos cosas, porque no valen igual. **Un comando sin
entrada no se probó**: no se cuenta como aprobado, la página lo dice con ese nombre, y
`evidencia.py cobertura` dice cuántos van de los 37.

Un comando que nunca dice *«no está dicho en ninguna parte»* sobre cincuenta proyectos está
rellenando huecos, y el registro lo marca solo.

### Paso 3 · Los nueve comandos de Samuel

Sobre **tres proyectos distintos cada día**, rotando, para que al quinto día haya quince
proyectos vistos desde adentro.

`/criterio-project:pm-wake` · `/criterio-project:pm-agenda` · `/criterio-project:pm-minutes` · `/criterio-project:pm-commitments` · `/criterio-project:pm-report` ·
`/criterio-project:pm-plan` · `/criterio-project:pm-escalate` · `/criterio-project:pm-publish` · (`/criterio-project:pm-setup` solo el día 1)

**Lo que hay que ver en particular:** que `/criterio-project:pm-commitments` reconozca el compromiso que el
simulador reprogramó —el mismo doliente, lo mismo, fecha nueva— como **uno reprogramado y
no como tres**. Y que `/criterio-project:pm-publish` deje la ficha donde Vera la lea: el día siguiente,
`/criterio-portfolio:portfolio-scan` tiene que encontrar la diferencia entre las dos fichas.

### Paso 4 · Los once comandos de Alba

Sobre **cuatro productos distintos cada día**, rotando.

`/criterio-product:product-wake` · `/criterio-product:product-discovery` · `/criterio-product:product-requirements` · `/criterio-product:product-definition` ·
`/criterio-product:product-trace` · `/criterio-product:product-spec` · `/criterio-product:product-business-case` · `/criterio-product:product-charter` ·
`/criterio-product:product-overlap` · `/criterio-product:product-publish` · (`/criterio-product:product-setup` solo el día 1)

**Lo que hay que ver:** que `/criterio-product:product-overlap` encuentre los productos que comparten
métrica, proyecto o segmento — con sesenta y cinco productos, tiene que haber varios.

### Paso 5 · El servidor

Con Rostrum levantado:

1. Abrir las tres secciones del portal y **ver que los números coincidan con el informe**.
2. Entrar a un proyecto y a un producto, y comprobar que el enlace entre los dos va en los
   dos sentidos.
3. **Dejar una pregunta escrita** desde el portal.
4. Al día siguiente, comprobar que `/criterio-portfolio:portfolio-wake` la recogió.

**Evidencia:** `tests/evidencias/dia-N/servidor.md`, con capturas de las tres secciones.

### Paso 6 · Calificar y cerrar el día

```
python3 tests/sintetico/fiabilidad.py .pruebas/corp-demo
python3 tests/sintetico/resumen.py
python3 scripts/verificar.py
git add -A && git commit
```

El informe del día queda en `tests/informes/dia-N-<fecha>.md`: aciertos, falsos positivos,
falsos negativos, precisión y cobertura **por señal**, tiempo total y por documento.

**El commit del día dice tres cosas**: precisión y cobertura, qué falló, y **en qué capa
estaba el defecto** — código, material o clave de respuestas. Sin esa última, cinco días
de informes no permiten decidir nada.

---

## Cómo se lee el resultado, el día cinco

Tres preguntas, y ninguna se contesta con un promedio:

**¿Se sostuvo la fiabilidad entre disposiciones?** Si no, hay una dependencia del layout, y
eso contradice lo que las páginas prometen.

**¿Qué señal es la menos fiable?** Y de sus fallos, ¿cuántos eran falsos positivos? Esa es
la que se arregla primero: un hallazgo falso hace que la siguiente lista no se lea.

**¿Siguió el rastro entre días?** Es lo que ninguna corrida suelta puede contestar. Un hito
que se cerró el martes no puede seguir reportándose el miércoles; un proyecto que se calló
tiene que aparecer al día siguiente; una promesa movida por tercera vez tiene que
reconocerse como una, no como tres.

---

## Dónde queda cada cosa

```
.pruebas/corp-demo/               la organización: fuera de git, dentro del repositorio
tests/evidencias/dia-N/           lo que produjo cada comando, un archivo por comando
tests/informes/dia-N-<fecha>.md   la calificación del día
tests/informes/RESUMEN.md         los cinco días juntos
```

La organización **no entra a git**: es material de una corrida, pesa, y se reconstruye con
un comando. Lo que entra son las evidencias y los informes.
