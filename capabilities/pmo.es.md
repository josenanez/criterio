# Capacidad PMO

**Gobierno de portafolio y de proyectos.**

[English](pmo.md) · [Volver al market](../README.es.md)

Estado: **Agente PMO disponible** · Agente PM en construcción

---

## Dónde se rompe una PMO

No es que le falten plantillas. Tiene de sobra.

Lo que le falta es que alguien lea junta la documentación que ya existe. Cuarenta proyectos, cada uno con su acta, su cronograma, sus minutas, sus correos y sus hojas de cálculo. Cada documento lo leyó alguien, una vez. Nadie los ha cruzado.

Y en el cruce está lo que decide:

- El hito cuya fecha pasó y no hay un solo documento que pruebe que se cumplió.
- El proyecto que reporta verde y lleva cinco semanas sin producir un documento.
- La minuta de la semana pasada que nombra a un patrocinador distinto del que dice el acta.
- La dependencia que un plan declara y el plan del otro proyecto ignora.
- El compromiso que alguien asumió en tres reuniones seguidas, con fecha nueva cada vez.

Ninguna de esas cosas aparece en un informe de avance, porque el informe de avance lo escribe quien está siendo evaluado.

---

## Los dos agentes

La capacidad tiene dos agentes porque la organización tiene dos roles, y necesitan cosas distintas.

### Agente PMO

Para el gerente de la PMO y sus analistas. **Cuarenta proyectos, barrido amplio, cadencia semanal o de comité.**

Lee toda la documentación del portafolio, mantiene un registro por proyecto, y en cada corrida dice qué cambió. Consolida, cruza dependencias entre proyectos, prepara el comité.

### Agente PM

Para cada gerente de proyecto, junior o senior. **Un proyecto, profundidad, cadencia diaria o por reunión.**

Convierte transcripciones y minutas en decisiones y compromisos con doliente y fecha. Su función central no la hace ninguna herramienta que un gerente de proyecto use hoy: **el compromiso dicho y no cumplido.** Las reuniones están llenas de *"yo lo tengo para el viernes"* y nadie los registra. El agente los extrae y en cada corrida revisa cuáles vencieron sin evidencia.

### Cómo se relacionan

El registro de proyecto es la interfaz entre los dos: el agente PM lo llena como subproducto de su trabajo diario, y el agente PMO deja de hacer ingeniería inversa sobre carpetas desordenadas.

Con una regla que no se negocia: **el registro del PM es una declaración; el hallazgo del PMO es evidencia.** Se mantienen como dos fuentes distintas, y la diferencia entre ellas es la señal más valiosa del sistema. *"El gerente reporta el hito en verde; la última minuta dice que el proveedor no entregó"* es la conversación que hoy no se puede tener.

Los estándares bajan de la PMO: umbrales, convenciones y esquema se publican en una carpeta compartida, y cada agente PM los lee y se verifica contra ellos antes de que la PMO mire nada. Funciona sobre un servidor de archivos corporativo, sin proyecto de integración.

---

## Qué hace hoy el Agente PMO

Se instala, se le indica dónde viven los documentos, y trabaja con lo que haya. No exige que la carpeta esté ordenada.

| Quiero… | Comando |
|---|---|
| Dejarlo listo y ver un primer resultado | `/pmo-setup` |
| Que lea todo y arme el registro | `/portfolio-scan` |
| El estado del portafolio | `/portfolio-report` |
| El estado de un proyecto | `/status-report` |
| Material para el comité | `/steering-pack` |
| Riesgos, supuestos, incidencias y dependencias | `/raid-log` |
| Evaluar un cambio de alcance, tiempo o costo | `/change-control` |
| Proveedores: entregado contra facturado | `/vendor-tracking` |
| Presupuesto | `/budget-tracking` |
| Revisar o redactar el acta | `/project-charter` |
| Cerrar un proyecto | `/project-closure` |

### Lo que lo hace distinto de un generador de informes

**La línea base es de solo agregar.** Cuando se replanifica, la anterior no se borra. Así es exactamente como se esconde el atraso: se replanifica, el semáforo vuelve a verde y nadie ve que el proyecto lleva un año corrido. Aquí toda desviación se reporta contra dos referencias —la original y la vigente— con el número de replanificaciones al lado.

**Las cuatro cifras del presupuesto, no dos.** Aprobado, comprometido, ejecutado y proyección. Un proyecto con 40% ejecutado y 95% comprometido no tiene holgura: tiene el presupuesto agotado y todavía no se ha causado. Eso no se ve mirando ejecutado contra aprobado, que es como se mira casi siempre.

**El silencio se mide.** Días desde el último documento y desde la última reunión. Un proyecto sin documentación no está mal gestionado: está sin documentar, y eso es un hallazgo distinto que también hay que decir.

**No hay privilegio para el que reporta.** El estado que produce es una comparación entre lo declarado y lo evidenciado. Cuando ningún documento respalda lo declarado, el estado es *sin sustento* — que no es lo mismo que estar mal, y es el estado más común en una PMO real.

### Cuándo habla

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

Todos son configurables, y se cambian hablando, no editando archivos.

---

## Evidencia

**Todavía no hay corridas reales.** Cuando las haya, aquí van: cuántos documentos, cuántos proyectos, cuánto tomó, cuántos hallazgos y cuáles nadie había visto — con el procedimiento para reproducirlas.

Lo verificado hoy es la máquina, no el valor:

```
python3 ../plugins/criterio-pmo/scripts/pmo.py selftest
```

Doce resultados conocidos, incluidos los casos que se equivocan solos: el atraso contra la línea base original frente a la vigente con una replanificación de por medio, y el presupuesto comprometido que se ve sano y no lo está.

---

## Empezar

```
/plugin marketplace add josenanez-company/criterio
/pmo-setup
```

El comando de instalación mira tus carpetas, hace cinco preguntas y corre un primer barrido sobre **tres proyectos**, no sobre el portafolio completo, para que veas un resultado en minutos y no un mensaje de "listo, ya puedes empezar".

Antes de instalar, lee el [descargo](../DISCLAIMER.es.md). Esto produce borradores de trabajo, no decisiones.
