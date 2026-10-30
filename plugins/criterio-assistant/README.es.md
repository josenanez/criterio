<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-ea-oscuro.svg"><img src="../../docs/img/marca/es/criterio-ea-claro.svg" alt="Criterio EA · Dirección" height="48"></picture>

# Ofelia · la asistente ejecutiva

**Ofelia prepara el trabajo de la oficina del ejecutivo.** Tú asistes al presidente o al gerente
general. Ella llega con la agenda de la semana contra sus sesiones y sus compromisos, el paquete de
la próxima sesión de cada órgano con la ficha de cada decisión, el borrador del acta desde las notas,
el estado de los compromisos de dirección y la correspondencia que pide respuesta. **Prepara; no
recomienda ni decide, y nunca envía nada.**

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**El nombre.** Ofelia, del griego *ōphéleia*, «ayuda»: es la que prepara.
<!-- /agente:nombre -->

[English](README.md) · `criterio-assistant` · Apache 2.0 · Una instancia por ejecutivo

**Estado:** construida, con el motor probado contra el material de prueba de cuatro oficinas —una
presidencia y una gerencia general con defectos sembrados, y dos de control— y con la ronda completa
con la agente sobre las cuatro, en [las rondas de la familia](../../tests/evidencias/familias/ea/RONDAS.md).
Nada se ha corrido aún sobre la oficina de un ejecutivo concreto. Lo que falta para darla por
terminada, en los [criterios de aceptación](ACCEPTANCE.md).

---

## Qué es

La asistente ejecutiva, como la define O*NET (43-6011): la agenda del ejecutivo, el orden del día y
la logística de juntas y comités, las actas, la correspondencia y la información que el ejecutivo
necesita. La frontera con el jefe de gabinete es la que marca la práctica: las iniciativas, la
coordinación del equipo directivo y las decisiones sobre procesos y recursos son del otro rol
([ADR 0012](../../docs/decisions/0012-scope-asistente-ejecutivo.md)). La secretaría de junta es un
modo de Ofelia, no un agente aparte.

## Qué hace

<!-- ea:comandos · generado por scripts/familias.py; no se edita a mano -->
### Los diez comandos

> Se escriben con el prefijo del plugin: `/criterio-assistant:` y autocompletar hace el resto. Es la única forma que resuelve en una sesión de Claude Code.

| Comando | Qué hace |
|---|---|
| `/criterio-assistant:ea-setup` | La configuración, el inventario y los órganos con sus sesiones |
| `/criterio-assistant:ea-scan` | Las fichas de las reuniones, de la correspondencia, de los viajes y de la agenda |
| `/criterio-assistant:ea-agenda` | La semana del ejecutivo: cruces, viajes contra la agenda, sesiones sin material y sesiones sin acta |
| `/criterio-assistant:ea-prep` | El paquete de la sesión, con la ficha de cada decisión |
| `/criterio-assistant:ea-minutes` | El borrador del acta, con cada acuerdo y compromiso citado |
| `/criterio-assistant:ea-commitments` | El estado de los compromisos de dirección, por órgano y por responsable |
| `/criterio-assistant:ea-mail` | La correspondencia que pide respuesta, con sus borradores |
| `/criterio-assistant:ea-weekly` | El resumen de la semana: lo que llegó, lo que vence y lo que falta preparar |
| `/criterio-assistant:ea-wake` | Lo que toca hoy en la oficina; si no toca nada, se calla |
| `/criterio-assistant:share-findings` | Un resumen sin datos para compartir, solo si dices que sí |
<!-- /ea:comandos -->

<!-- ea:skills · generado por scripts/familias.py; no se edita a mano -->
### Los siete skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se consultan como un manual.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `commitment-tracking` | El compromiso vencido sin evidencia, el que nadie fechó y el que se movió una y otra vez: las reglas de Samuel | Propio |
| `correspondence-record` | La ficha de un correo: si pide respuesta, qué pide y para cuándo; y el borrador de las respuestas rutinarias, que nunca se envía | Propio |
| `decision-brief` | La ficha de una decisión: las opciones que traen los documentos con su evidencia, lo que falta saber y el plazo, sin ordenarlas ni recomendar | Propio |
| `ea-intake` | Qué documentos procesa Ofelia, dónde va cada uno, qué procesa el código directamente —la agenda .ics y los encabezados del correo— y qué extrae la agente a la ficha | Propio |
| `meeting-record` | La ficha de una sesión: orden del día, acuerdos con su responsable y su fecha, compromisos con su historia y decisiones pendientes, cada dato con su cita | Propio |
| `minutes-draft` | El borrador del acta desde las notas o la transcripción, con cada acuerdo citado y «BORRADOR» en el nombre y en el texto | Propio |
| `travel-record` | La ficha de un viaje: cada vuelo del itinerario con su número, su ruta, y su salida y su llegada con fecha, hora y zona, cada uno con su cita | Propio |
<!-- /ea:skills -->

## Para qué sirve

Para que el ejecutivo llegue a cada sesión con lo abierto, el material y las decisiones preparadas, y
para que ningún acuerdo quede sin dueño ni fecha y ningún compromiso venza sin que alguien lo vea. Lo
que procesa:

| Documento | Dónde |
|---|---|
| La agenda exportada en .ics, con la fecha de la exportación en el nombre | `10-agenda/` |
| Los correos guardados como archivo, uno por mensaje | `20-correspondencia/` |
| La convocatoria, el material, las notas y el acta firmada de cada sesión | `organos/<órgano>/<AAAA-MM-DD>/` |
| Los órganos que se siguen y la ficha de la oficina | `00-referencia/` |

**Exportaciones, no cuentas.** Ofelia no se conecta al buzón ni al calendario: procesa lo que la
oficina exporta. Una conexión directa es otra decisión, con su revisión de privacidad.

### Lo que cuesta hoy

<!-- ea:cifras · generado por scripts/familias.py; no se edita a mano -->
| Cifra | Fuente |
|---|---|
| **57 %** del tiempo de trabajo se va en comunicar —reuniones, correo y chat— y el 43 % en crear | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?», 2023](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) — Datos agregados de uso de Microsoft 365, no la encuesta; el informe no da el tamaño de esa muestra |
| **55 %** dice que los próximos pasos al final de una reunión no quedan claros | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?», 2023](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) — 31.000 trabajadores de tiempo completo o independientes en 31 mercados |
| **68 %** no tiene suficiente tiempo de concentración sin interrupciones en su jornada | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?», 2023](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) — 31.000 trabajadores de tiempo completo o independientes en 31 mercados |
<!-- /ea:cifras -->

### Y para qué no sirve

- **No envía, no agenda, no acepta y no mueve nada.** Escribe borradores solo en `90-borradores/`, con
  «BORRADOR» en el nombre y en el texto; quien envía es una persona.
- **No recomienda una opción ni prioriza por el ejecutivo.** Cada decisión llega con sus opciones en el
  orden en que las traen los documentos, con su evidencia y lo que falta saber.
- **No edita actas, agendas ni correos originales**, y nunca archiva un borrador como acta.
- **No declara cumplido un compromiso sin un documento que lo sostenga**, y no evalúa a una persona ni a
  un área.
- **No procesa lo que se excluye.** Las carpetas excluidas se dicen en cada informe.

Y una que hay que decir en voz alta: **los documentos se procesan en la infraestructura de la
plataforma de IA**, no solo en tu equipo, y la oficina del ejecutivo es de lo más sensible que tiene
una organización. Su informe **no se publica en Rostrum por omisión**. Descargo completo en
[DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

## Instalación y configuración

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-assistant@criterio
/criterio-assistant:ea-setup
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar
marketplace desde GitHub → `josenanez/criterio`.

### El primer resultado

`/criterio-assistant:ea-setup` no te pide que ordenes nada. Busca la carpeta de la oficina, dice qué
exportación de la agenda hay y de qué fecha, qué órganos tienen sesiones y cuántos correos hay
guardados, y pregunta lo que ningún documento responde: el ejecutivo, los órganos, las carpetas
excluidas, el correo de la oficina, la zona horaria y los umbrales. En los primeros quince minutos
deja ver la agenda de las próximas dos semanas con sus cruces, las sesiones sin material y las que
siguen sin acta.

**Lo que queda configurado** lo escribe el setup en `.criterio/direccion/<ejecutivo>/config.json`.
Todo eso se cambia **hablando**.

### Cada cuánto corre

Cada día que corre, con un solo resumen a la semana. La decisión es aritmética de fechas:

```
python3 scripts/asistente.py despertar --config <archivo>
```

Y `/criterio-assistant:ea-wake` es el comando que el reloj invoca: hace lo que toca —procesar lo
nuevo, preparar una sesión que entra en su ventana, las actas pendientes, la correspondencia vencida—
y, **si no toca nada, se calla.**

## Trabajo en equipo

Ofelia funciona sola. Si están los otros, **no hay nada que conectar**.

| Con quién | Qué pasa |
|---|---|
| **Samuel** | Los compromisos de proyecto son suyos: Ofelia los cita de su ficha y no los recalcula. Comparten las reglas de compromiso del núcleo común |
| **Rostrum** | Publica su informe solo si la configuración lo dice; por omisión, no |

## Pruebas

### Cómo está construido

[`scripts/asistente.py`](scripts/asistente.py), con la librería estándar, hace todo lo que es cálculo:
lee la agenda .ics —repeticiones, excepciones, ocurrencias movidas y zonas horarias, con su
autoprueba—, lee los encabezados de cada correo, recorre las sesiones de cada órgano y calcula cada
señal con las reglas de compromiso que comparte con Samuel (`nucleo.py`). La agente lleva a cada ficha
solo lo que trae un documento escrito: los acuerdos y los compromisos del acta, las decisiones con sus
opciones y lo que pide cada correo.

### Cómo se verifica

```
python3 scripts/asistente.py selftest        el motor
python3 tests/criterio-ea/generar.py          el material de las cuatro oficinas
python3 tests/criterio-ea/evaluar.py          cada señal contra la clave, y las reglas
```

Sobre material sintético con una clave que el motor no ve, incluidas las oficinas de control, donde
cualquier señal es una falla. El material prueba además las reglas de la operación real: una reunión
en otra zona horaria que solo se cruza después del cambio de hora, un evento libre y uno cancelado que
no cruzan, una agenda vieja que no da cruces, un borrador puesto en `40-acta/` y una carpeta excluida.
La última corrida, en [`tests/criterio-assistant/RESULTADOS.md`](../../tests/criterio-assistant/RESULTADOS.md);
qué prueba el material y qué no, en [`EVIDENCIA.md`](../../tests/criterio-ea/EVIDENCIA.md).
