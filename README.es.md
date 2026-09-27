# Criterio

**Un market de agentes que aceleran capacidades organizacionales.**

[English](README.md) · [Términos](TERMS.es.md) · [Descargo](DISCLAIMER.es.md) · [Cómo aportar](CONTRIBUTING.es.md)

Apache 2.0 · Se instala en cuatro clics · Cada agente produce su primer resultado en quince minutos

---

| | | |
|:--:|:--:|:--:|
| [![PMO](docs/img/es/pmo.png)](plugins/criterio-pmo/README.es.md) | ![CFO](docs/img/es/cfo.png) | ![CLO](docs/img/es/clo.png) |
| **[Ver la familia PMO →](plugins/criterio-pmo/README.es.md)** | Sin construir | Sin construir |

---

## El problema no es que falten herramientas

Una organización no se mueve por departamentos: se mueve por **capacidades**. La capacidad de gobernar un portafolio de proyectos. La de cerrar un mes y responder por los números. La de revisar un contrato antes de firmarlo.

Cada una tiene su método, su lenguaje y sus formas propias de fallar. Y todas comparten el mismo cuello de botella: **cientos de documentos que nadie ha leído juntos.** Actas, cronogramas, minutas, conciliaciones, contratos. Cada uno lo leyó alguien, una vez. Nadie los ha cruzado.

Las herramientas de trabajo ayudan a producir un documento más. El problema nunca fue que faltara una plantilla.

**Criterio es un market de agentes, uno por capacidad.** Leen lo que ya existe, guardan lo que encontraron con una cita por cada dato, y en la corrida siguiente dicen qué cambió.

---

## Las capacidades

### PMO — gobierno de portafolio y de proyectos

**Qué es.** La función que responde por el conjunto de los proyectos: qué hay en curso, contra qué plan, con qué presupuesto y con qué riesgos. Sus componentes son la priorización de la demanda, la planeación y la línea base, el seguimiento contra plan, el registro de riesgos y dependencias, el control de cambios, el presupuesto, los proveedores, el comité y el cierre.

**Lo que cuesta hoy**

| Cifra | Fuente |
|---|---|
| Los proyectos de TI tienen un sobrecosto medio de **73%**, y el 18% se pasa por más del 50% | [Flyvbjerg et al., *Project Management Journal*, 2026](https://journals.sagepub.com/doi/10.1177/87569728251340590) — 11.011 proyectos, 126 países |
| **31%** de los proyectos complejos no alcanzan los beneficios que se propusieron | [PMI, *Pulse of the Profession* 2026](https://www.pmi.org/learning/thought-leadership/driving-success-in-complex-projects) — 2.534 encuestados, 35 países |
| **72%** dedica medio día o más cada mes solo a consolidar informes a mano, y la mitad no tiene indicadores en tiempo real | [Wellingtone, *State of Project Management* 2026](https://wellingtone.co.uk/publications/state-of-project-management-research/) |
| **Un tercio de los proyectos no tiene línea base**, y el 22% se sigue planificando en Excel | Wellingtone 2026 |
| **93%** de las organizaciones de más de mil millones de dólares tienen una PMO | [PM Solutions, *State of the PMO* 2025](https://www.pmsolutions.com/uploads/files/uploads/files/State_of_the_PMO_2025_Research_Report.pdf) — 134 organizaciones |

Un tercio sin línea base significa que un tercio de los proyectos **no tiene contra qué medirse**. No es un problema de herramienta: es que nadie volvió a mirar.

**Qué atacamos.** No la falta de plantillas: de eso hay de sobra. Atacamos que **nadie ha leído junta la documentación que ya existe.** Cada documento lo leyó alguien, una vez. Nadie los ha cruzado, y en el cruce está lo que decide:

- El hito cuya fecha pasó y **no hay un solo documento que pruebe que se cumplió**.
- El proyecto que reporta verde y **lleva cinco semanas sin producir un documento**.
- La minuta de la semana pasada que **nombra a un patrocinador distinto** del que dice el acta.
- La dependencia que un plan declara y **el plan del otro proyecto ignora**.
- El compromiso que alguien asumió en **tres reuniones seguidas, con fecha nueva cada vez**.
- La replanificación que devolvió el semáforo a verde y **borró un año de atraso acumulado**.

Nada de eso aparece en un informe de avance. **El informe de avance lo escribe quien está siendo evaluado.**

Dos decisiones que se notan el primer día. **Las cuatro cifras del presupuesto, no dos:** un proyecto con 40% ejecutado y 95% comprometido no tiene holgura, tiene el presupuesto agotado y todavía sin causar, y eso es invisible si se mira ejecutado contra aprobado. **El silencio se mide:** un proyecto sin documentación no está mal gestionado, está sin documentar, y ese es un hallazgo distinto que también hay que decir.

**La familia PMO tiene más de un agente porque la organización tiene más de un rol.** Llevan nombre de persona porque son capacidades extendidas de personas, y el significado de cada nombre apunta a lo que hace.

| | | |
|---|---|---|
| **[Vera](plugins/criterio-pmo/README.es.md)** | Agente PMO · **disponible** | *Verus*, lo verdadero. Dice lo que los documentos dicen, no lo que se reporta. 17 comandos, 10 skills |
| **[Samuel](plugins/criterio-pm/README.es.md)** | Agente de proyecto · **disponible** | «El que escuchó». Su función central es el compromiso dicho y no cumplido. 9 comandos, 8 skills |
| **[Alba](plugins/criterio-product/README.es.md)** | Agente de producto · **disponible** | El amanecer: la luz que hay antes de que se vea nada. Trabaja antes de que el proyecto exista. 11 comandos, 12 skills |
| **[Rostrum](plugins/criterio-pmo/SERVER.es.md)** | El servidor · **disponible** | Una tribuna. Sostiene lo que ya está escrito, donde el equipo puede leerlo |

Rostrum es el único sin nombre de persona, y es a propósito: los agentes deciden sobre lo que leen, y el servidor no decide nada.

---

### CFO — cierre, control y reporte financiero

**Qué es.** La función que cierra los libros y responde por lo que dicen. Sus componentes son el cierre y la consolidación, las conciliaciones, la contabilidad frente a la base fiscal, el reporte a supervisores y la preparación de auditoría.

**Lo que cuesta hoy**

| Cifra | Fuente |
|---|---|
| **18%** de los contadores comete errores a diario y **59%** varios al mes, por restricciones de capacidad | [Gartner, feb. 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) — 497 contadores, encuesta jul. 2023 |
| Cierre anual: **10 días** los mejores, **18** la mediana, **35** los rezagados | [APQC, abr. 2026](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-up-year-end-close) |
| El cierre trimestral **empeoró**: 49% cerraba en seis días hábiles en 2019, 44% en 2023 | [Ventana Research / ISG, dic. 2023](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) |
| Las horas de programa SOX subieron **32% en dos años**, a 15.580. El **45% de los controles sigue siendo totalmente manual** | [KPMG, *SOX Survey* 2025](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) — ~150 profesionales |

El dato que debería incomodar es el segundo: **el cierre no mejoró en cuatro años**, a pesar de todo lo que se gastó en tecnología.

→ Agente CFO: capacidad declarada, sin construir

---

### CLO — contratos, cumplimiento y riesgo legal

**Qué es.** La función que responde por lo que la empresa firmó. Sus componentes son la revisión de contratos, el repositorio de lo firmado, el seguimiento de obligaciones y vencimientos, el cumplimiento normativo y las disputas.

**Lo que cuesta hoy**

| Cifra | Fuente |
|---|---|
| La mala gestión contractual erosiona en promedio **8,6% del valor del contrato** — los mejores 3%, los peores más de 20% | [World Commerce & Contracting con Deloitte, 2023](https://info.worldcc.com/roi) — 1.236 organizaciones |
| Los equipos de contratación gastan **más del 40% de su tiempo y su presupuesto** en contratos de baja complejidad | [EY con Harvard Law School, 2021](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) — 1.000 profesionales, 22 países |
| Una organización grande maneja **19.000 contratos al año**, y **90% tiene dificultad para encontrar los suyos** | EY / Harvard Law School, 2021 |
| Solo el **27%** guarda todos sus contratos firmados en un único repositorio | [Sirion y World Commerce & Contracting, 2026](https://www.sirion.ai/press/trusted-contract-data-world-cc-research-report/) — 170 empresas |

Una empresa que no encuentra sus propios contratos no puede saber qué firmó, ni qué vence, ni a qué se obligó.

→ Agente CLO: capacidad declarada, sin construir

---

La lista no está cerrada. **Una capacidad entra cuando alguien que la ejerce quiere construir su agente.**

---

## Instalación

**Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar marketplace desde GitHub → `josenanez-company/criterio`

**Claude Code**

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-pmo@criterio     si gestionas el portafolio
/plugin install criterio-pm@criterio      si gestionas un proyecto
/plugin install criterio-product@criterio si defines un producto
```

Después de instalar, cada agente tiene un comando de instalación que mira tus carpetas, hace cinco preguntas y produce un primer resultado sobre tus propios documentos. **Nadie edita un archivo de configuración a mano.**

**Cada cuánto corre cada uno, qué le tienes que decir y qué comando se le pone a un reloj:** [`plugins/criterio-pmo/README.es.md`](plugins/criterio-pmo/README.es.md) — **la página de la familia**: cómo operan los tres juntos, cómo se trabaja con cada uno, y cada cuánto corre. Ninguno se programa solo — los tres traen el comando que un reloj invoca, y el reloj vive fuera del plugin.

---

## Lo que comparten todos los agentes

No es una colección de asistentes sueltos. Todos se construyen sobre las mismas reglas, y de ahí sale que su salida se pueda poner frente a un comité.

**Separan lo declarado de lo evidenciado.** Lo que alguien afirma va en una columna; lo que sustentan los documentos, en otra. Nunca se fusionan, y la diferencia entre las dos suele ser el hallazgo de más valor.

**Nada se sobrescribe.** Un registro guarda su historia. Cuando la versión nueva reemplaza a la anterior en silencio, desaparece justo lo que había que ver.

**El modelo extrae, el código calcula.** Leer una fecha es lectura. Restar, proyectar y sumar es aritmética, y la aritmética vive en código, donde es determinística y se puede probar. Ningún número de un informe sale de una estimación del modelo.

Esto no es un detalle técnico. La investigación disponible sobre hojas de cálculo operativas —[Powell, Baker y Lawson, 2009](http://mba.tuck.dartmouth.edu/spreadsheet/product_pubs_files/errors.pdf), 50 hojas auditadas, 270.722 fórmulas— encontró errores en el 94%. Conviene decir que es el estudio de campo más reciente de su tipo y ya tiene años: nadie ha publicado una réplica comparable. Un agente que estima números en vez de calcularlos agrega una capa más de ese mismo problema.

**Todo dato lleva su cita, o declara que no está.** *"No está dicho en ninguna parte"* es un hallazgo válido y esperado.

**Y saben callarse.** Corren solos y solo hablan cuando algo cruza un umbral. Un agente que reporta todas las semanas haya o no noticia se ignora en un mes.

---

## Evidencia

Cada capacidad publica las cifras de sus corridas reales: cuántos documentos, cuánto tomó, cuántos hallazgos, y cuáles nadie había visto. Junto con el procedimiento para que cualquiera las reproduzca.

**Las que todavía no se han medido no se inventan.** Las cifras de esta página son de terceros y llevan su fuente, su año y su muestra. Las nuestras van cuando existan. Mientras una capacidad no tenga corridas reales, su página lo dice.

Lo que se puede verificar hoy, clonando el repositorio:

```
python3 scripts/verificar.py
```

Una sola puerta, trece comprobaciones: el material sintético, la aritmética de los dos plugins, las respuestas escritas a mano, y que la documentación diga lo que el código hace. **Con la librería estándar y sin instalar nada** — si algo de esto necesitara una dependencia, la propiedad que hace auditable a este repositorio se habría roto.

El detalle de qué prueba cada corrida y, con la misma franqueza, **qué no**, en [`tests/criterio-pmo/EVIDENCIA.md`](tests/criterio-pmo/EVIDENCIA.md) y [`tests/criterio-pm/EVIDENCIA.md`](tests/criterio-pm/EVIDENCIA.md).

**Los resultados de la última corrida, por agente y en conjunto, con gráficas y con lo que todavía no se ha probado:** [`docs/pruebas.html`](docs/pruebas.html) — la genera `python3 scripts/resultados.py`, y sale de correr las puertas, no de escribirlas.

---

## Apache 2.0 — qué entregamos y a qué invitamos

**Entregamos completo y sin condiciones** el método de cada agente, el esquema de sus registros, el código que calcula, sus criterios de aceptación y la forma de medirlos.

**A qué invitamos**

- Úsalo dentro de tu organización sin pedir permiso, y adáptalo a cómo trabajas.
- Cambia los criterios: los umbrales son configuración, no código.
- **Construye la capacidad que te falta.** Si ejerces una función que no está en la lista, su agente lo escribe quien conoce el trabajo, no quien sabe programar. El formato está en [CONTRIBUTING.es.md](CONTRIBUTING.es.md).
- Si encuentras que se equivoca, ábrelo como issue con el documento que lo demuestra. Vale más que una estrella.

**Lo que no afirmamos**

Esto produce borradores de trabajo, no decisiones. Nadie ha certificado nada aquí. Los agentes saben lo que se escribió, no lo que se habló fuera de los documentos. Lee el [descargo](DISCLAIMER.es.md) antes de instalar: usarlo implica aceptar los [términos](TERMS.es.md).

---

Mantenido por [José Francisco Ñáñez](https://josenanez.com).
