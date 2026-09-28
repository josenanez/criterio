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

## Antes de empezar · hoy

### Paso 0.1 · Instalar los tres agentes

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-portfolio@criterio
/plugin install criterio-project@criterio
/plugin install criterio-product@criterio
```

**Evidencia:** `tests/evidencias/dia-0/instalacion.md` — qué versión quedó instalada y si
algún comando no apareció. Un comando declarado que no aparece en la sesión es un defecto
del manifiesto, y es el primero que hay que ver.

### Paso 0.2 · Levantar la organización

```
python3 tests/sintetico/simulador.py ~/Projects/corp-demo --dia 1
```

Deja `~/Projects/corp-demo/` con `documentos/`, la bitácora del día y `esperado.json`.
**Este archivo es la clave de respuestas** y se deriva de los hechos que el simulador
plantó, con las reglas escritas en los skills — no con el código que se está midiendo.

### Paso 0.3 · Resolver las tres divergencias abiertas

La primera corrida del calificador encontró tres señales donde **la regla escrita y el
código no coinciden**: `requirement_untraced`, `declared_vs_evidence` y `evidence_stale`.
Están en la derivación del simulador y en el extractor de referencia, no en los agentes.

Antes de empezar los cinco días hay que decidir, para cada una, **cuál de las dos tiene
razón**, corregir la que no, y dejar escrito por qué. Si se arranca con la clave mal, los
cinco días miden contra una vara torcida.

### Paso 0.4 · Configurar los tres agentes

```
/portfolio-setup      → apuntar a ~/Projects/corp-demo/documentos/proyectos
                        y el estado a ~/Projects/corp-demo/estado
/pm-setup             → un proyecto: ~/Projects/corp-demo/documentos/proyectos/PRY-200-...
/product-setup        → un producto: ~/Projects/corp-demo/documentos/productos/PRD-300
```

**Evidencia:** `tests/evidencias/dia-0/setup-<agente>.md` con **cuántas preguntas hizo,
cuáles, cuánto tardó hasta el primer resultado, y qué encontró en ese primer barrido.**
La promesa publicada es *quince minutos*; aquí se mide.

---

## Cada día, en este orden

### Paso 1 · Pasar una semana

```
python3 tests/sintetico/simulador.py ~/Projects/corp-demo --dia <N>
```

Escribe la semana nueva y regenera `esperado.json`. La bitácora del día dice qué le pasó a
cada caso, en una línea: quién se calló, quién reprogramó, quién cerró un hito.

**La disposición de las carpetas rota con el día** —ordenada, plana, revuelta, sin
carpetas— y lo esperado no cambia. Una caída de fiabilidad entre días no es variación: es
una dependencia del layout, y es un defecto.

### Paso 2 · Los diecisiete comandos de Vera

En este orden, que es el de uso real y no el alfabético:

| # | Comando | Qué se verifica | Evidencia |
|---|---|---|---|
| 1 | `/portfolio-wake` | Que diga qué toca hoy — y que **se calle** si no toca nada | `wake.md` |
| 2 | `/document-index` | Cuántos documentos cambiaron de verdad desde ayer, y cuántos no hubo que releer | `index.md` |
| 3 | `/portfolio-scan` | Las cincuenta fichas, con cita en cada dato | `scan.md` |
| 4 | `/portfolio-report` | Qué cambió, qué se contradice, qué está en silencio | `report.md` |
| 5 | `/status-report` | Sobre tres proyectos: el semáforo declarado y lo que no explica | `status.md` |
| 6 | `/health-check` | Un proyecto desde cero, sin mirar su informe | `health.md` |
| 7 | `/project-history` | Desde cuándo lo declarado dejó de sostenerse | `history.md` |
| 8 | `/raid-log` | Riesgos y dependencias, incluidos los dichos y no registrados | `raid.md` |
| 9 | `/change-control` | Mover un proyecto 60 días: **a quién alcanza** | `change.md` |
| 10 | `/budget-tracking` | Las cuatro cifras, y la desviación contra las dos líneas base | `budget.md` |
| 11 | `/vendor-tracking` | Contrato contra recibo contra factura | `vendor.md` |
| 12 | `/product-view` | Un producto a través de los proyectos que lo construyen | `product-view.md` |
| 13 | `/project-charter` | Revisar un acta: qué le falta y qué consecuencia tiene | `charter.md` |
| 14 | `/project-closure` | Cerrar contra el criterio pactado | `closure.md` |
| 15 | `/steering-pack` | El material del comité, como paquete de decisiones | `steering.md` |
| 16 | `/portfolio-server` | Levantar Rostrum | `server.md` |
| 17 | `/portfolio-setup` | **Solo el día 1.** Del 2 al 5 no debe hacer falta | — |

**Qué anotar en cada evidencia**, y es lo mismo para los tres agentes: el comando, cuánto
tardó, cuántos documentos leyó, qué produjo, **cuántos hallazgos y de qué señal**, y —lo
más importante— **qué dijo que no sabía**. Un comando que nunca dice *«no está dicho en
ninguna parte»* sobre cincuenta proyectos está rellenando huecos.

### Paso 3 · Los nueve comandos de Samuel

Sobre **tres proyectos distintos cada día**, rotando, para que al quinto día haya quince
proyectos vistos desde adentro.

`/pm-wake` · `/pm-agenda` · `/pm-minutes` · `/pm-commitments` · `/pm-report` ·
`/pm-plan` · `/pm-escalate` · `/pm-publish` · (`/pm-setup` solo el día 1)

**Lo que hay que ver en particular:** que `/pm-commitments` reconozca el compromiso que el
simulador reprogramó —el mismo doliente, lo mismo, fecha nueva— como **uno reprogramado y
no como tres**. Y que `/pm-publish` deje la ficha donde Vera la lea: el día siguiente,
`/portfolio-scan` tiene que encontrar la diferencia entre las dos fichas.

### Paso 4 · Los once comandos de Alba

Sobre **cuatro productos distintos cada día**, rotando.

`/product-wake` · `/product-discovery` · `/product-requirements` · `/product-definition` ·
`/product-trace` · `/product-spec` · `/product-business-case` · `/product-charter` ·
`/product-overlap` · `/product-publish` · (`/product-setup` solo el día 1)

**Lo que hay que ver:** que `/product-overlap` encuentre los productos que comparten
métrica, proyecto o segmento — con sesenta y cinco productos, tiene que haber varios.

### Paso 5 · El servidor

Con Rostrum levantado:

1. Abrir las tres secciones del portal y **ver que los números coincidan con el informe**.
2. Entrar a un proyecto y a un producto, y comprobar que el enlace entre los dos va en los
   dos sentidos.
3. **Dejar una pregunta escrita** desde el portal.
4. Al día siguiente, comprobar que `/portfolio-wake` la recogió.

**Evidencia:** `tests/evidencias/dia-N/servidor.md`, con capturas de las tres secciones.

### Paso 6 · Calificar y cerrar el día

```
python3 tests/sintetico/fiabilidad.py ~/Projects/corp-demo
python3 tests/sintetico/resumen.py
python3 scripts/verificar.py
git add -A && git commit
```

El informe del día queda en `tests/informes/<fecha>.md`: aciertos, falsos positivos,
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
~/Projects/corp-demo/          la organización: documentos, estado, bitácora, esperado.json
tests/evidencias/dia-N/        lo que produjo cada comando, un archivo por comando
tests/informes/<fecha>.md      la calificación del día
tests/informes/RESUMEN.md      los cinco días juntos
```

La organización **no entra al repositorio**: es material de una corrida, pesa, y se
reconstruye con un comando. Lo que entra son las evidencias y los informes.
