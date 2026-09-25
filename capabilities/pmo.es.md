# Capacidad PMO

**Gobierno de portafolio y de proyectos.**

[English](pmo.md) · [Volver al market](../README.es.md)

Estado: **Agente PMO disponible** · Agente PM en construcción

---

## Qué atacamos

No la falta de plantillas. De eso hay de sobra.

Atacamos el hecho de que **nadie ha leído junta la documentación que ya existe**. Cuarenta proyectos, cada uno con su acta, su cronograma, sus minutas, sus correos y sus hojas de cálculo. Cada documento lo leyó alguien, una vez. Nadie los ha cruzado.

Y en el cruce está lo que decide:

- El hito cuya fecha pasó y **no hay un solo documento que pruebe que se cumplió**.
- El proyecto que reporta verde y **lleva cinco semanas sin producir un documento**.
- La minuta de la semana pasada que **nombra a un patrocinador distinto** del que dice el acta.
- La dependencia que un plan declara y **el plan del otro proyecto ignora**.
- El compromiso que alguien asumió en **tres reuniones seguidas, con fecha nueva cada vez**.
- La replanificación que devolvió el semáforo a verde y **borró un año de atraso acumulado**.

Nada de eso aparece en un informe de avance. El informe de avance lo escribe quien está siendo evaluado.

Eso no es una sospecha: [Wellingtone](https://wellingtone.co.uk/publications/state-of-project-management-research/) encontró en 2026 que **un tercio de los proyectos no tiene línea base** y que la mitad de las organizaciones no tiene indicadores en tiempo real. Un tercio de los proyectos no tiene contra qué medirse.

---

## Qué vamos a mejorar

Tres cosas concretas, y ninguna es "visibilidad".

**Que la evidencia pese más que la declaración.** Hoy el estado de un proyecto es lo que dice quien lo gerencia. Aquí es una comparación entre lo declarado y lo que sustentan los documentos, con las dos columnas a la vista y la diferencia señalada — y la comparación la hace el código, no el criterio del momento.

**Que el atraso no se pueda borrar.** Hoy una replanificación reemplaza la línea base anterior y el historial desaparece. Lo vamos a volver acumulativo: toda desviación se reporta contra la línea base original **y** contra la vigente, con el número de replanificaciones al lado.

**Que la aritmética deje de ser una opinión.** Días de silencio, desviación, disponible real, proyección: todo eso se calcula en código, no se estima. Ningún número de un informe sale de una estimación.

---

## Esto es lo que hacemos

Cada línea de esta tabla es **algo que el agente hace**, no algo que promete. Están escritas, se pueden leer en este repositorio, y se pueden correr hoy.

| Lo que hace | Comando |
|---|---|
| Mira tus carpetas, hace cinco preguntas y produce un primer resultado sobre tus documentos | `/pmo-setup` |
| Lee toda la documentación del portafolio y arma una ficha por proyecto, con cita y fecha en cada dato | `/portfolio-scan` |
| Dice qué cambió desde la corrida anterior, qué se contradice, qué está en silencio y qué no tiene sustento | `/portfolio-report` |
| Compara un proyecto contra su plan y nombra las señales que el semáforo declarado no explica | `/status-report` |
| Arma el comité como un paquete de decisiones, no como un informe de avance | `/steering-pack` |
| Levanta riesgos, supuestos, incidencias y dependencias — **incluidos los que se dijeron en una reunión y nadie registró** | `/raid-log` |
| Evalúa un cambio en alcance, tiempo y costo, y crea línea base nueva sin borrar la anterior | `/change-control` |
| Cruza entregables contractuales contra evidencia de recibo y contra lo facturado | `/vendor-tracking` |
| Muestra aprobado, comprometido, ejecutado y proyección — las cuatro, no dos | `/budget-tracking` |
| Revisa el acta y dice qué falta y qué consecuencia tiene que falte | `/project-charter` |
| Cierra contra el criterio de éxito que se pactó al inicio, con lecciones ancladas a hechos documentados | `/project-closure` |

**Por qué esto es un compromiso y no una promesa:** cada comando está escrito como instrucciones legibles en [`plugins/criterio-pmo/`](../plugins/criterio-pmo/), bajo Apache 2.0. Se puede auditar antes de instalarlo, cambiar si no corresponde a cómo trabajas, y medir contra los criterios de aceptación que vienen con él.

### Cinco decisiones de diseño que se notan el primer día

**El semáforo se contrasta, no se repite.** El estado declarado se compara contra las señales calculadas, y las que ese estado no explica se listan. Cuando un proyecto reporta verde y hay evidencia que ese verde no cubre, el informe lo dice, y el portafolio trae la cifra: cuántos verdes no se sostienen. Un semáforo que repite lo que declaró el gerente ya existe y se llama el reporte semanal.

**La línea base es de solo agregar.** Cuando se replanifica, la anterior no se borra. Así es exactamente como se esconde el atraso: se replanifica, el semáforo vuelve a verde y nadie ve que el proyecto lleva un año corrido.

**Las cuatro cifras del presupuesto, no dos.** Un proyecto con 40% ejecutado y 95% comprometido no tiene holgura: tiene el presupuesto agotado y todavía no se ha causado. Eso es invisible si se mira ejecutado contra aprobado, que es como se mira casi siempre.

**El silencio se mide.** Días desde el último documento y desde la última reunión. Un proyecto sin documentación no está mal gestionado: está sin documentar, y ese es un hallazgo distinto que también hay que decir.

**"No está dicho en ninguna parte" es una respuesta.** El agente no rellena vacíos con lo razonable. Los declara.

---

## Los dos agentes

La capacidad tiene dos porque la organización tiene dos roles, y necesitan cosas distintas.

### Agente PMO — disponible

Para el gerente de la PMO y sus analistas. **Cuarenta proyectos, barrido amplio, cadencia de comité.** Consolida, cruza dependencias entre proyectos, prepara el comité.

### Agente PM — en construcción

Para cada gerente de proyecto, junior o senior. **Un proyecto, profundidad, cadencia diaria o por reunión.**

Su función central no la hace ninguna herramienta que un gerente de proyecto use hoy: **el compromiso dicho y no cumplido.** Las reuniones están llenas de *"yo lo tengo para el viernes"* y nadie los registra. El agente los extrae con doliente y fecha, y en cada corrida revisa cuáles vencieron sin evidencia.

### Cómo se relacionan

La ficha de proyecto es la interfaz: el agente PM la llena como subproducto de su trabajo diario, y el agente PMO deja de hacer ingeniería inversa sobre carpetas desordenadas.

Con una regla que no se negocia: **la ficha del PM es una declaración; el hallazgo del PMO es evidencia.** Se mantienen como dos fuentes distintas, y la diferencia entre ellas es la señal más valiosa del sistema. *"El gerente reporta el hito en verde; la última minuta dice que el proveedor no entregó"* es la conversación que hoy no se puede tener.

Los estándares bajan de la PMO: umbrales, convenciones y esquema se publican en una carpeta compartida, y cada agente PM se verifica contra ellos antes de que la PMO mire nada. Funciona sobre un servidor de archivos corporativo, sin proyecto de integración.

---

## Cuándo habla

Corre solo y solo levanta la voz cuando algo cruza un umbral:

| Señal | Habla cuando |
|---|---|
| Hito vencido | La fecha pasó y no hay evidencia de cumplimiento |
| Proyecto en silencio | 15 días sin documento nuevo |
| Desviación contra línea base | Supera 10% en tiempo o en costo |
| Compromiso vencido | Pasó la fecha y no hay evidencia |
| Contradicción entre documentos | Siempre — no lleva número |
| Presupuesto | Ejecutado supera 90% de lo comprometido |
| Cambio de gobierno | Siempre |
| Declaración que la evidencia no explica | Declara verde y hay al menos una señal que ese verde no cubre |
| Declaración vieja | La declaración tiene 30 días o más |
| Entregable de proveedor vencido | Pasó la fecha y no hay evidencia de entrega |
| Facturado sin entrega | Hay factura declarada y ni un entregable aceptado |
| Replanificación sin autorizar | La línea base se movió más días de los que autorizaron los cambios aprobados |

Todos son configurables, y se cambian hablando, no editando archivos. **El silencio cuando no pasó nada es la característica, no la falla.**

---

## Evidencia

**Todavía no hay corridas reales.** Cuando las haya, aquí van: cuántos documentos, cuántos proyectos, cuánto tomó, cuántos hallazgos y cuáles nadie había visto — con el procedimiento para reproducirlas.

Lo que sí hay es una corrida sobre **material sintético con respuestas conocidas**: seis proyectos, veintiséis documentos, construidos para contener las fallas que contiene una carpeta real. Las catorce señales se disparan cuando deben, el proyecto sano no produce ni una alerta, y el conjunto se califica con 49 comprobaciones. Lo que esa corrida prueba, lo que no prueba, y los seis límites que destapó están en [`tests/criterio-pmo/EVIDENCIA.md`](../tests/criterio-pmo/EVIDENCIA.md).

Lo verificado hoy es la máquina, no el valor:

```
python3 plugins/criterio-pmo/scripts/pmo.py selftest    la aritmética
python3 tests/criterio-pmo/generar.py                   el portafolio sintético
python3 tests/criterio-pmo/grade.py                     49 comprobaciones contra las respuestas conocidas
python3 tests/coherencia.py                             que la documentación y el código digan lo mismo
```

Veinticuatro resultados conocidos, incluidos los casos que se equivocan solos: el atraso contra la línea base original frente a la vigente con una replanificación de por medio, el presupuesto comprometido que se ve sano y no lo está, la replanificación que movió sesenta y un días cuando el comité autorizó treinta, y el verde que no explica nueve señales.

---

## Empezar

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-pmo@criterio
/pmo-setup
```

El comando de instalación corre un primer barrido sobre **tres proyectos**, no sobre el portafolio completo, para que veas un resultado en minutos y no un mensaje de "listo, ya puedes empezar".

Antes de instalar, lee el [descargo](../DISCLAIMER.es.md). Esto produce borradores de trabajo, no decisiones.
