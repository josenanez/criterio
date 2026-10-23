# 0012 · El alcance se amplía a la asistente ejecutiva: Ofelia

**Fecha:** 2026-10-23 · **Estado:** aceptada · **Modifica:** 0009

## Contexto

El mapa de capacidades de la página de Agentes, acordado el 23 de octubre de 2026, deja cuatro
capacidades como «Siguiente»: la asistente ejecutiva, seguridad (CISO), auditoría (CAE) y datos
(CDO). El orden lo pone cuánto reutiliza cada una de lo ya construido, y la asistente va primero.

**El CEO no tiene tarjeta propia en el mapa.** No procesa documentos: decide sobre lo que le
prepara su equipo, y eso ya lo cubren las demás familias. Lo que sí le llega directo es el trabajo
de su oficina, que hoy vive en la memoria de una persona y en su correo.

**El rol se define desde una fuente externa, no desde lo que se nos ocurra.** O*NET, la
clasificación de ocupaciones del Departamento de Trabajo de los Estados Unidos (43-6011.00,
*Executive Secretaries and Executive Administrative Assistants*), pone en el centro del rol:

- llevar la agenda del ejecutivo;
- preparar el orden del día y la logística de juntas y comités;
- levantar y distribuir las actas;
- abrir, clasificar y distribuir la correspondencia, y responder la rutinaria;
- archivar y recuperar documentos;
- reunir información y preparar material para el ejecutivo.

La frontera con el jefe de gabinete o con un VP es la que marca la práctica. La asistente es dueña
del día a día del ejecutivo: su agenda, su correo y la preparación y el seguimiento de sus
reuniones. Las iniciativas, la coordinación del equipo directivo y las decisiones sobre procesos y
recursos son del otro rol.

Cumple las cuatro condiciones de las 0006 y 0009:

- trabajo recurrente sobre documentos;
- una brecha entre lo declarado y lo escrito, como el compromiso que se da por hecho y no tiene
  evidencia o la reunión que no tiene acta;
- fechas y conteos que calcula el código;
- una persona que decide.

## Decisión

**El alcance se amplía a una familia de dirección con un agente: Ofelia, la asistente
ejecutiva.** Su nombre viene del griego *ōphéleia*, «ayuda»: es la que prepara. Trabaja en
Colombia y Ecuador, como las demás. La sigla de la familia es **EA** (*executive assistant*), por
confirmar.

**Ofelia prepara; no recomienda ni decide.** Para cada punto que pide una decisión, arma la ficha
de la decisión:

- la decisión, como la escribe el material;
- las opciones que traen los documentos;
- la evidencia de cada opción, con su cita;
- lo que falta saber;
- las fechas que fijan el plazo, calculadas por el código.

No las ordena ni dice cuál conviene. Hay cuatro razones:

1. Solo sabe lo que está escrito, y una decisión de dirección pesa sobre todo lo que no lo está.
2. Que una opción sea la mejor no se puede calificar contra una clave.
3. Si propusiera qué acordar, después mediría su propia propuesta en el seguimiento.
4. En una entidad vigilada, una recomendación necesita un dueño que responda por ella.

Recomendar es otra capacidad, más cerca de Estrategia y transformación, con su propio ADR y un
responsable humano que la firme.

**Reutiliza lo que ya está probado.**

- El motor de compromisos de Samuel: el compromiso vencido sin evidencia, el que nadie fechó y el
  prometido una y otra vez.
- El skill `commitment-tracking`.
- El núcleo común de las familias CFO y CLO.
- Rostrum como portal.

Las reglas de compromiso salen de `portafolio.py` y pasan al núcleo común (`nucleo.py`), para que
Samuel y Ofelia usen el mismo código. Las pruebas de Samuel tienen que dar exactamente lo mismo
antes y después del cambio.

**La secretaría de junta es un modo de Ofelia, no un agente aparte.** Es el mismo trabajo cuando
el órgano es la junta. Se separa solo si una ronda muestra que necesita reglas propias.

## Las reglas de Ofelia

Las reglas de la 0009 siguen. Estas son las propias, y responden a lo que podría salir mal en la
operación real de una oficina de dirección:

| Lo que podría salir mal | La regla |
|---|---|
| Que actúe en nombre del ejecutivo | No envía, no acepta y no mueve nada. Escribe borradores solo en `borradores/`; quien los envía es una persona |
| Que toque documentos oficiales | No edita actas, agendas ni correos originales. Escribe solo en `.criterio/` y en `borradores/`, más el archivo que marca su carpeta raíz (ADR 0011) |
| Que el borrador del acta se tome como el acta | Cada borrador lleva «BORRADOR» en el nombre y en el texto; el acta es la que se firma, y Ofelia nunca la archiva como tal |
| Que la información de la presidencia quede a la vista del equipo | Su informe **no se publica en Rostrum por omisión**; publicarlo es una decisión explícita de la configuración |
| Que procese lo que no debe | Procesa solo las carpetas que se le indican y respeta una lista de carpetas excluidas, que dice en el setup y en cada informe |
| Que dos agentes lleven el mismo compromiso con datos distintos | Cada compromiso es del acta donde nació. Los de proyecto son de Samuel: Ofelia los cita de su ficha y no los recalcula |
| Una agenda vieja que da cruces falsos | Cada informe dice la fecha de la exportación; si tiene más de N días, avisa y no calcula cruces |
| Eventos recurrentes o zonas horarias mal leídos | Las repeticiones y las zonas horarias del .ics las calcula el código, con su autoprueba; un evento ambiguo se declara, no se adivina |
| Saturar de avisos | Se calla cuando nada cruza un umbral; un solo resumen a la semana |
| Conectarse al buzón o al calendario | En esta versión procesa exportaciones —la agenda en .ics y los correos guardados como archivo—, no cuentas; una conexión directa es otra decisión, con su revisión de privacidad |
| Que reemplace a la persona | Es para quien asiste al ejecutivo; la persona sigue siendo dueña de la agenda y de lo que se envía |

## El diseño

**Para quién.** Para la oficina del presidente o del gerente general, y para quien asiste a un
ejecutivo de la alta dirección.

**Lo que calcula el código.** Todos los umbrales son configuración.

| Señal | Cuándo se levanta |
|---|---|
| `meeting_conflict` | Dos reuniones del ejecutivo se cruzan en la agenda exportada |
| `meeting_without_material` | A N días de una reunión de un órgano, su material no está en la carpeta |
| `meeting_without_minutes` | Pasados N días de una reunión, su acta no está |
| `agreement_without_owner` | Un acuerdo del acta no tiene responsable |
| `agreement_without_date` | Un acuerdo del acta no tiene fecha |
| `commitment_overdue` | Un compromiso venció y ningún documento lo sostiene como cumplido |
| `commitment_rescheduled` | Un compromiso se movió más de N veces |
| `correspondence_unanswered` | Un correo guardado pide respuesta y su plazo venció sin respuesta guardada |
| `decision_deadline` | Una decisión pendiente tiene una fecha que la fija dentro de N días |

**Las fichas.** Cada dato lleva su cita.

| Ficha | Una por | Qué lleva |
|---|---|---|
| Ficha de la reunión | Reunión de un órgano | Órgano, fecha, orden del día, material, acta, acuerdos, compromisos y las decisiones con su ficha |
| Ficha de la correspondencia | Hilo guardado | De quién, qué pide, para cuándo y si hay respuesta guardada |
| Ficha de la agenda | Exportación | Los eventos normalizados, con la fecha de la exportación |

**Los comandos, en borrador.**

| Comando | Lo que entrega |
|---|---|
| `ea-setup` | Pide la carpeta raíz, los órganos, el ejecutivo, quién lo asiste, las carpetas excluidas, los umbrales, si publica en Rostrum y los términos |
| `ea-scan` | Procesa la agenda, los órganos y la correspondencia, y escribe las fichas |
| `ea-agenda` | La semana del ejecutivo contra sus compromisos: cruces, reuniones sin material y reuniones sin acta |
| `ea-prep` | El paquete de la próxima reunión de un órgano: orden del día con lo abierto de la anterior, lista del material que falta y la ficha de cada decisión |
| `ea-minutes` | El borrador del acta desde las notas o la transcripción, con cada acuerdo y compromiso citado |
| `ea-commitments` | El estado de los compromisos de dirección, por órgano y por responsable |
| `ea-mail` | La correspondencia guardada: qué pide respuesta y para cuándo, y el borrador de las respuestas rutinarias |
| `ea-weekly` | El resumen de la semana: lo que llegó, lo que vence y lo que falta preparar |
| `ea-wake` | La cadencia; se calla si nada cruza un umbral |

**Nunca:** envía, agenda, acepta, mueve, declara cumplido un compromiso sin evidencia, recomienda
una opción, prioriza por el ejecutivo ni evalúa a una persona o a un área.

**Las carpetas.** Es la estructura recomendada, no obligatoria:

```
direccion/
  agenda/                     las exportaciones .ics
  organos/<órgano>/<fecha>/   orden del día, material, notas y acta
  correspondencia/            los correos guardados
  borradores/                 lo único que escribe Ofelia entre los documentos
```

**La prueba.** Material sintético por industria y una entidad de control por país, con su clave.
Va con el mismo arnés, `tests/ronda_familia.py`: primero el motor contra la clave y después la
ronda con el agente.

## Lo que queda para un segundo incremento

- Viajes: los itinerarios contra la agenda.
- La conexión directa al calendario o al correo.

## Alternativas descartadas

**Un agente del CEO.** Duplica lo que preparan las demás familias, y su entregable sería una opinión
sobre el negocio.

**Una asistente que recomienda.** Es el jefe de gabinete con otro nombre. Las cuatro razones están
en la decisión.

**Extender a Samuel.** Samuel responde por un proyecto y su cadencia es la reunión de seguimiento.
La oficina del ejecutivo cruza órganos y proyectos, y tiene otros dueños.

## Consecuencias

- El diseño se escribe en `families/criterio-ea/DISENO.es.md` desde las mismas tres fuentes que las
  familias CFO y CLO (`familia.json`, `carpetas.json` y `fuentes.json`), con `scripts/familias.py`,
  que hoy conoce tres familias y tiene que conocer una cuarta.
- Las reglas de compromiso pasan al núcleo común, y las pruebas de Samuel siguen dando lo mismo.
- El mapa de la página de Agentes la muestra como «Siguiente», sin fecha, hasta que la familia esté
  construida y probada.
