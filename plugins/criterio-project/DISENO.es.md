# Samuel · el agente Project Manager

**Samuel**, «el que escuchó». Su función central es el compromiso dicho y no cumplido, así
que el nombre es literalmente la función: oyó lo que se dijo en la reunión, y lo recuerda el
viernes.

Extiende al **gerente de proyecto**: la persona que responde por un proyecto.

Marco general, definición de las clases y de las columnas:
[la hoja de Vera](../criterio-portfolio/DISENO.es.md#el-marco-de-la-familia).

| | |
|---|---|
| **Instancia** | Una por proyecto |
| **Alcance** | Un proyecto. Profundidad, cadencia diaria o por reunión |
| **Cadencia** | Gira alrededor de la reunión: la agenda antes, el acta después. `/criterio-project:pm-wake` mira de qué lado estás |
| **Se distribuye** | Como `criterio-project`, plugin aparte, con los scripts copiados de `criterio-portfolio` |
| **Escribe** | La ficha del proyecto — **excepto el estado declarado** |
| **Publica** | `ficha-pm.json` en la carpeta de gobierno del proyecto, y nada más |
| **Lee** | Su propia ficha y el estándar que publica la PMO |
| **Estado** | Los nueve comandos construidos, ocho skills, corpus propio y 19 comprobaciones. **La extracción sobre documentación real no se ha corrido** |
| **Evidencia** | [`tests/criterio-portfolio/EVIDENCIA.md`](../../tests/criterio-portfolio/EVIDENCIA.md) |

---

## El flujo

El agente no asiste a la reunión. Trabaja sobre el rastro que la reunión deja, **y produce el
rastro que necesita**: el que arma la agenda antes recibe la minuta después.

```
GERENTE DE PROYECTO  (clase C)                 AGENTE PM  (clases A y B)
──────────────────────────────────────────────────────────────────────────────────
                                          ┌──  lee lo que cambió en la carpeta
                                          │    mantiene el plan contra la evidencia
                                          │    calcula desviación y alertas
   ◄──── agenda de la reunión ◄───────────┘     ordena por lo que necesita a alguien

dirige la reunión
negocia, desbloquea, decide
   └─► transcripción o notas ────────────────►  redacta el acta
                                               extrae compromisos: quién, qué, cuándo
                                               marca los vencidos sin evidencia
                                               levanta los riesgos dichos al pasar

   ◄──── informe semanal ◄────────────────────  todo salvo una línea
declara el estado del proyecto
   └─► `declared` ───────────────────────────►  la mitad de la comparación

acepta o rechaza lo entregado
   └─► evidencia de aceptación ──────────────►  se cruza contra la facturación

compromete una fecha
   └─► línea base o compromiso ──────────────►  referencia del cálculo siguiente
```

---

## La restricción que define este agente

**El agente PM no escribe `declared`.** Es la sexta invariante del diseño, no una
recomendación: la persona declara, el agente le muestra contra qué. Si el agente declara, la
comparación compara al sistema consigo mismo.

---

## Las dos fichas

Samuel y Vera leen **los mismos documentos** y escriben **dos fichas distintas que
nunca se fusionan.** Es la misma regla que ya gobierna declarado contra evidenciado,
aplicada un nivel más arriba.

| | Ficha del proyecto | Lectura de portafolio |
|---|---|---|
| **La escribe** | Samuel, salvo `declared` | Vera |
| **Vive en** | El estado de Samuel, en el equipo del gerente | El estado de Vera |
| **Profundidad** | Todo: compromisos de cada reunión, RAID, entregables por proveedor | Lo que un barrido de portafolio alcanza a leer |
| **Cadencia** | Diaria o por reunión | Semanal o de comité |
| **Para qué** | Que el gerente llegue con la semana preparada | Que la PMO vea el conjunto |

### Por qué dos y no una

Una sola ficha con dos escritores es una carrera: el barrido de Vera pasa el martes
y sobreescribe lo que Samuel puso el lunes, o al revés. La forma habitual de
resolverlo —un dueño, y el otro solo lee— obliga a elegir mal en las dos direcciones:
si manda Samuel, la PMO pierde la capacidad de leer un proyecto por su cuenta cuando
duda del gerente; si manda Vera, la PMO entra en el camino crítico de cada proyecto,
y con setenta proyectos eso es un cuello de botella.

Dos fichas quitan el problema en vez de arbitrarlo. **Y lo que era un conflicto de
escritura se vuelve la señal.**

### Lo que la diferencia significa

Dos lectores, los mismos documentos, y distinto resultado. Eso no es un error del
sistema: es información sobre la carpeta.

| Lo que se observa | Qué significa |
|---|---|
| **Los dos citan, y no coinciden** | Leyeron documentos distintos. El que cita el más reciente vio algo que el otro no. Es el hallazgo de más valor, y apunta a un documento concreto |
| **Samuel lo tiene, Vera no** | Diferencia de profundidad, no contradicción. Un compromiso dicho en una reunión no está al alcance de un barrido de portafolio. **No es hallazgo** |
| **Vera lo tiene, Samuel no** | Sí es hallazgo: la PMO leyó un documento del proyecto que el gerente no está viendo |
| **Coinciden** | El caso normal, y no se reporta. Un agente que celebra las coincidencias es ruido |

La distinción de la segunda fila es la que hace que esto sirva. Sin ella, cada corrida
reportaría cien diferencias de alcance y nadie volvería a abrir el informe.

### Cómo se encuentran las dos fichas

**Samuel publica; Vera lee.** Ninguno de los dos alcanza el estado del otro, y no
hace falta: la ficha del proyecto se publica **como un documento más del proyecto**, en
la carpeta de gobierno, y Vera la lee como lee todo lo demás.

```
PRY-001-originacion-digital/
  00-gobierno/
    2026-01-12-acta-constitucion.md
    ficha-pm.json          ← lo que Samuel publica
  10-plan/
  20-seguimiento/
  30-reuniones/
```

Eso resuelve de un golpe tres cosas que de otro modo habría que construir: no hay
almacenamiento compartido, no hay consistencia distribuida entre N instancias, y la
cita de cualquier campo de esa ficha ya es una ruta válida como la de cualquier otro
documento.

**Publicar es un acto explícito, no un efecto.** Vera promete no escribir en las
carpetas de documentación, y Samuel hereda esa promesa: escribe en su propio estado y
solo pone `ficha-pm.json` en la carpeta del proyecto cuando alguien corre el comando que
lo publica, o cuando la cadencia configurada lo hace. Es el único archivo que Samuel
escribe fuera de su estado, y esa lista no crece sin decirlo aquí.

### Qué campos se contrastan

**Solo los que los dos tienen por qué leer.** Contrastar todo produciría la avalancha de
diferencias de alcance que acabaría con el informe:

```
identity.sponsor      identity.manager      identity.committee
identity.product      plan.end_date         money.approved
declared.status       declared.as_of
```

Ocho campos, los que envejecen peor y los que una PMO usa para decidir. El contraste es
aritmética sobre dos registros que Vera ya tiene, así que **lo hace el código**, y
produce una señal nueva: `pm_vs_pmo`.

La señal dice qué campo, qué dijo cada uno, y **de qué documento y de qué fecha lo sacó
cada uno**. Sin esas dos citas el hallazgo no sirve: *«el gerente y la PMO no coinciden
en el patrocinador»* no le permite a nadie hacer nada, y *«el gerente cita la minuta del
11 de septiembre y la PMO el acta de enero»* sí.

---

## Cómo se distribuye

**Dos plugins.** `criterio-portfolio` para la oficina de proyectos, `criterio-project` para el
gerente de un proyecto. Cada uno con su README hablándole a su audiencia, porque la
política de valor no permite otra cosa: un gerente de proyecto que abre un README que
empieza hablándole de portafolio no se reconoce, y no instala.

Un solo plugin con `role: pmo | pm` era la alternativa barata, y se descartó por eso
mismo. La configuración conserva el campo —sigue diciendo qué es esta instalación— pero
ya no es lo que decide qué comandos existen.

### Y los scripts, en un solo sitio

La aritmética es la misma. Dos copias de `portafolio.py` que se separan es exactamente la deuda
que este proyecto no acepta, así que:

- **La fuente vive en `plugins/criterio-portfolio/scripts/`.** Ahí se edita, y en ningún otro
  sitio.
- **`criterio-project/scripts/` recibe copias literales** de las que comparte, con una
  cabecera que dice de dónde salieron y que no se editan ahí.
- **`scripts/sincronizar.py` las copia**, y **`tests/coherencia.py` falla si difieren.**
  Una copia que se separó en silencio es peor que no tenerla.

| Script | `criterio-portfolio` | `criterio-project` | Por qué |
|---|---|---|---|
| `portafolio.py` | fuente | copia | La aritmética es la misma; `compute` ya trabaja proyecto a proyecto y después agrega |
| `texto.py` | fuente | copia | Leer un `.docx` es leer un `.docx` |
| `informe.py` | fuente | **no** | El informe de un proyecto no es el del portafolio recortado |
| `servidor.py` | fuente | **no** | Rostrum es de la PMO |

Que la copia sea literal y no un módulo compartido es a propósito: **un plugin instalado
tiene que correr solo.** Un `import` a una ruta del otro plugin funciona en este
repositorio y falla en el equipo de quien lo instaló, que es el peor sitio para
enterarse.

---

## A · Lo que hace, y hoy consume tiempo de alguien

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Mantener el plan actualizado contra la evidencia | Documentos del proyecto y el plan vigente | La ficha al día; desviación contra la línea base original y la vigente | Construido |
| Llevar el RAID al día | Registro existente y las minutas | Riesgos, supuestos, incidencias y dependencias con doliente y fecha; los dichos y no registrados, marcados | Construido |
| Consolidar las cifras del proyecto | Aprobado, contratos y órdenes, ejecución, proyección | Las cuatro cifras y el disponible real | Construido |
| Preparar la solicitud de cambio | Lo que se quiere cambiar, la línea base vigente, la autoridad declarada | Borrador con impacto en alcance, tiempo y costo, y quién debe decidir | Construido |
| Mantener el expediente ordenado y trazable | La carpeta como esté | Cada dato con su ruta y su fecha; lo que no está, declarado | Construido |
| Seguir los entregables del proveedor | Contrato, actas de recibo, facturación declarada | Vencidos sin evidencia, aceptados sin documento, factura sin entrega | Construido |
| Ver si la replanificación se pasó de lo autorizado | Línea base de solo agregar y cambios aprobados | Días que se movió, días autorizados, días que nadie autorizó | Construido |
| **Extraer y seguir los compromisos de cada reunión** | Minuta o transcripción | Compromisos con doliente, fecha y fuente; vencidos sin evidencia; sus reprogramaciones | **Construido**: `/criterio-project:pm-commitments`. Y un límite que conviene tener escrito: un compromiso sin fecha (`due_date: no_declarada`) el cálculo lo ignora y tampoco lo cuenta, así que el comando lo cuenta aparte a mano — es la razón por la que la sección «sin fecha» es obligatoria en la salida |
| **Armar el informe de avance semanal** | Ficha, alertas y lo que cambió desde la corrida anterior | El informe completo salvo el estado declarado | **Construido**: `/criterio-project:pm-report`, con cadencia de proyecto y con la declaración pedida después de mostrar la evidencia, nunca antes |
| **Armar la estructura de la reunión** | Alertas abiertas, compromisos vencidos, decisiones pendientes | Agenda con los puntos que necesitan a alguien, en orden | **Construido**: `/criterio-project:pm-agenda`, con lo que esta reunión no puede mover declarado aparte |
| **Redactar el acta de la reunión** | Transcripción o notas | Acta con acuerdos, compromisos y decisiones, cada uno atribuido | **Construido**: `/criterio-project:pm-minutes`, que separa compromiso, decisión, intención sin doliente y riesgo dicho al pasar |

## B · Lo que hace, y hoy no se hace

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Revisar el acta de constitución y decir qué falta | El acta | Los campos ausentes con su consecuencia; sobre todo la autoridad del gerente | Construido |
| Borrador del cierre y de las lecciones | Criterio de éxito pactado y la historia documental | Entregado contra comprometido, desviación final, lecciones con hecho y fecha | Construido |
| Evaluar el efecto real de un cambio en el cronograma y en otros proyectos | El cambio y las dependencias declaradas | Los hitos propios por los que pasa el cambio, los proyectos alcanzados —directos e indirectos—, sus gerentes, y cuáles no pueden sostener su fecha | **Construido** · `portafolio.py impact`, dentro de `/criterio-project:pm-escalate`. Lo que no dice, y no se inventa: cuántos días se mueve cada uno |
| Preparar el escalamiento con la decisión formulada | El ítem que excede su autoridad | La decisión como pregunta cerrada, con opciones, recomendación, y la consecuencia de no decidir con fecha | **Construido** · `/criterio-project:pm-escalate`. Y si lo que traías no escala, lo dice en vez de armar el paquete |
| **Detectar el compromiso reprogramado tres veces** | Historial de compromisos del mismo doliente sobre lo mismo | Un compromiso con su historial de reprogramaciones, señalado como bloqueo | **Construido.** `reschedules` en el esquema, `commitment_rescheduled` en el cálculo con su umbral, y la corrida lo verifica sobre PRY-001 |
| **Primer borrador del plan y de la WBS** | El acta y proyectos análogos del portafolio | WBS por entregable, el orden por dependencia, los supuestos declarados como tales y los nodos sin definir **sin rellenar**. Las fechas van en blanco | **Construido** · `/criterio-project:pm-plan`. No compromete ninguna fecha: eso es autoridad |

Tres veces reprogramado **no es un problema de seguimiento: es un bloqueo que nadie ha
nombrado.** Es información distinta de tres compromisos vencidos, y es la que le sirve al
gerente.

## C · Lo que el agente no hace

Lista de acciones que el agente no ejecuta. No es una evaluación de riesgo ni pretende ser
exhaustiva: **la responsabilidad de uso y ejecución es de la organización que lo despliega.**
Ver [la hoja de Vera](../criterio-portfolio/DISENO.es.md#el-marco-de-la-familia).

| Función | Requiere | Qué le entrega al agente |
|---|---|---|
| Declarar el estado del proyecto | Que sea de una persona, por diseño — sexta invariante | La declaración: la mitad de la comparación. Sin ella el sistema no tiene señal |
| Dirigir la reunión | Información fuera de los documentos · autoridad | La minuta, que es el insumo principal de este agente |
| Negociar con proveedores y con otras áreas | Autoridad | El acuerdo, cuando queda escrito |
| Aceptar o rechazar un entregable | Autoridad | La evidencia de aceptación, que el agente cruza contra la facturación |
| Gestionar a las personas del equipo | Juicio sobre personas | El desbloqueo, que es lo que cierra un compromiso vencido |
| Leer la política del patrocinador y decidir qué se pelea | Información fuera de los documentos | La prioridad real, que decide qué se escala |
| Comprometer al proyecto en una fecha | Autoridad | La fecha, que se vuelve línea base o compromiso |
| Decidir la prioridad cuando dos cosas chocan | Autoridad · información fuera de los documentos | La decisión fechada |

---

## Lo que sigue siendo del gerente persona

Todas las semanas el gerente va a la reunión, la dirige, hace y recibe seguimiento, negocia,
acepta o rechaza lo entregado, sostiene a su equipo, lee la política de su patrocinador y
**declara el estado de su proyecto.**

Lo que cambia es que llega con la semana preparada: la agenda armada, los compromisos vencidos
con nombre y fecha, el plan al día contra la evidencia, el informe listo salvo el estado, y la
lista de lo que la evidencia no sostiene.

Si una organización quitara al gerente y dejara solo al agente, lo que se rompe primero:

1. **Nadie dirige la reunión**, y la reunión es donde se desbloquea lo que está trabado.
2. **Nadie declara**, y sin declaración no hay contra qué contrastar la evidencia: el hallazgo
   de más valor desaparece.
3. **La ficha se seca.** Su fuente principal es lo que la reunión produce, así que el agente se
   queda ciego exactamente en la función que lo justifica.

El tercero conviene tenerlo claro al hablar con un director: **este agente no es viable sin su
persona.** No por prudencia — por arquitectura.

---

## Lo que falta por construir, en orden

1. ~~El plugin `criterio-project`~~ — **construido**, con la regla que mantiene iguales las copias.
2. ~~El comando de compromisos~~ — **construido**: `/criterio-project:pm-commitments`, con `/criterio-project:pm-setup` delante.
3. ~~Publicar la ficha~~ — **construido**: `/criterio-project:pm-publish`.
4. ~~El contraste `pm_vs_pmo` en código~~ — **construido**, del lado de Vera, con sus dos
   citas y con las cuatro formas de diferir distinguidas. Siete comprobaciones.
5. ~~La estructura de la reunión~~ — **construido**: `/criterio-project:pm-agenda`. Cierra el ciclo, y es la
   de más apalancamiento: el que arma la agenda antes recibe la minuta después.
6. ~~El informe semanal~~ — **construido**: `/criterio-project:pm-report`, con cadencia de proyecto.
7. ~~El acta de la reunión~~ — **construido**: `/criterio-project:pm-minutes`.
8. ~~El primer borrador del plan y de la WBS~~ — **construido**: `/criterio-project:pm-plan`, con los
   proyectos análogos entrando como referencia citada y nunca como estimación.
9. ~~El escalamiento con la decisión formulada~~ — **construido**: `/criterio-project:pm-escalate`, con el
   efecto del cambio calculado en vez de descrito.

**Las tablas A y B quedan sin filas abiertas.** Lo que sigue pendiente no es construcción:
es que esto corra sobre la documentación real de una organización.

Y una deuda de verificación que conviene tener a la vista: **la extracción nunca se ha
corrido.** El corpus siembra el estado desde `expected/fichas/`, así que la cadena
documento → modelo → ficha no se ha ejercitado. `grade.py --fichas` existe para eso.

## Decisiones cerradas

- **Dos fichas que nunca se fusionan**, y la diferencia entre ellas es la señal. Ver arriba.
- **Dos plugins con los scripts en un solo sitio**, copiados por una regla que falla si se
  separan. Ver arriba.
- **El registro de preguntas vive en el estado de Samuel**, con la forma de un compromiso
  —quién, qué, cuándo— porque es el mismo objeto. La regla que decide si esto sobrevive a
  setenta proyectos: **la misma pregunta no se hace dos veces.** Si nadie contestó, la corrida
  siguiente reporta *«preguntada el 12, sin respuesta»*, que es un hallazgo, en vez de volver
  a preguntar. Es la misma mecánica que la cola de Rostrum, y se implementa con ella.

## Decisiones abiertas propias de esta hoja

- **Cómo bajan los estándares de la PMO.** `paths.standard` está declarado en la configuración y
  no lo lee ninguna línea de código. Con N instancias de agente PM, la versión del esquema y los
  umbrales se vuelven un problema de consistencia distribuida: barato si la carpeta del estándar
  es de solo lectura y versionada, caro si cada PM puede cambiar sus umbrales. **Con dos plugins
  la pregunta se vuelve más aguda**, porque ahora los umbrales pueden diferir por instalación y
  no solo por configuración.
- **Qué pasa cuando Samuel publica y el gerente no quiere.** Publicar la ficha expone al
  proyecto a la lectura de la PMO con una profundidad que antes no tenía. Es deseable y también
  es político, y este diseño no decide por la organización: publicar es explícito, y quien lo
  corre sabe lo que hace.

---

# Criterios de aceptación

Nada se anuncia como terminado hasta que todos pasen. Están escritos antes que el código a
propósito: un criterio escrito después describe lo que se construyó, no lo que hacía falta.

La corrida que los sostiene, con lo que **no** cubre, está en
[`EVIDENCIA.md`](../../tests/criterio-project/EVIDENCIA.md) y, generada desde la corrida misma, en
[`RESULTADOS.md`](../../tests/criterio-project/RESULTADOS.md).

## La ficha

1. **El agente nunca escribe `declared`.** No es una regla de documentación: es una restricción
   del camino de escritura, y el selftest lo intenta y comprueba que falle.
2. **Todo campo lleva su cita** —documento fuente y fecha— o el estado `not_found`. Un campo con
   valor y sin fuente es un defecto, no un caso degradado.
3. **Dos fichas no se fusionan nunca.** La ficha de Samuel y la lectura que Vera hace del mismo
   proyecto siguen siendo dos archivos con dos dueños, y ningún comando escribe las dos.

## Publicar

4. **Publicar es explícito.** `ficha-pm.json` llega a la carpeta de gobierno del proyecto solo
   cuando un comando la pone ahí. Ningún comando escribe nada más fuera del estado del agente, y
   la prueba enumera lo que se escribió.
5. **Una ficha publicada es un documento válido**: Vera la lee con su lectura de documentos
   normal, y cada cita que lleva resuelve.

## Los compromisos

6. **Un compromiso extraído de una minuta lleva quién, qué, para cuándo y la fuente.** Uno sin
   fecha se cuenta aparte — no puede estar vencido, y no puede desaparecer del informe, que es
   justamente la falla que esto existe para terminar.
7. **El mismo compromiso reprogramado es uno con historial**, no tres. La tercera
   reprogramación se reporta como bloqueo, no como tres vencidos.
8. **La misma pregunta no se hace dos veces.** Si nadie contestó, la corrida siguiente reporta
   *«preguntada el 12, sin respuesta»* —que es un hallazgo por sí solo— en vez de volver a
   preguntar.

## El cambio y el escalamiento

9. **El efecto de un cambio se calcula, no se describe.** A quién alcanza, por qué camino,
   quién no puede sostener su fecha y por cuántos días. **Y no se estima cuántos días se mueve
   cada alcanzado**: eso necesita holgura por actividad y la ficha no la tiene.
10. **El plan no compromete ninguna fecha.** El borrador propone estructura y orden; la fecha
    la compromete el gerente, porque es un acto de autoridad.

## La aritmética compartida

11. **Los scripts copiados son idénticos byte a byte a su fuente**, y la comprobación que lo
    demuestra corre en la misma puerta que todo lo demás.
12. **Cada copia corre sola.** El plugin instalado no importa nada de la ruta del otro plugin.

## La evidencia

13. **Un corpus sintético con respuestas conocidas**, incluido un control negativo: un proyecto
    cuyas reuniones no producen ni un hallazgo. Un agente que reporta sobre un proyecto sano es
    un generador de ruido.
14. **Toda cifra de la documentación sale de una corrida**, y la corrida se reproduce desde el
    repositorio con la librería estándar y sin instalar nada.
