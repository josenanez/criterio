# 0012 · El alcance se amplía al asistente ejecutivo

**Fecha:** 2026-10-23 · **Estado:** propuesta · **Modifica:** 0009

## Contexto

El mapa de capacidades de la página de Agentes, acordado el 23 de octubre de 2026, deja cuatro
capacidades como «Siguiente»: el asistente ejecutivo, seguridad (CISO), auditoría (CAE) y datos
(CDO). El orden lo pone cuánto reutiliza cada una de lo ya construido, y el asistente va primero.

**El CEO no tiene tarjeta propia en el mapa.** No procesa documentos: decide sobre lo que le
prepara su equipo, y eso ya lo cubren las demás familias. Lo que sí le llega directo es el trabajo
de su oficina: qué se comprometió en cada reunión, qué se cumplió, qué viene en la próxima y qué
material falta. Hoy ese trabajo vive en la memoria de una persona y en su correo.

Cumple las cuatro condiciones de las 0006 y 0009:

- **Trabajo recurrente sobre documentos:** agendas, actas, minutas, material de comités y
  correos de seguimiento.
- **Una brecha entre lo declarado y lo escrito:** el compromiso que se da por hecho y no tiene
  evidencia, o la reunión que no tiene acta.
- **Cifras y fechas que calcula el código:** vencimientos, días sin acta y veces que se movió un
  compromiso.
- **Una persona que decide:** el ejecutivo y su asistente.

## Decisión

**El alcance se amplía a una familia de dirección con un agente: el asistente ejecutivo.** Corre
en Colombia y Ecuador, como las demás. Contrasta los compromisos de cada reunión de dirección
contra su seguimiento y prepara la próxima reunión de cada órgano.

**Reutiliza lo que ya está probado.**

- El motor de compromisos de Samuel: un compromiso vencido sin evidencia, uno que nadie fechó y
  uno prometido una y otra vez.
- El skill `commitment-tracking`.
- Rostrum como portal.

Las reglas del compromiso salen de `portafolio.py` y pasan al núcleo común (`nucleo.py`), para
que Samuel y el asistente usen el mismo código y no dos copias que se separan. Es el mismo
camino que tomó la familia CFO con su núcleo.

**Las reglas de la 0009 siguen, más tres propias:**

1. **No actúa en nombre del ejecutivo.** No envía correos, no acepta ni mueve reuniones y no
   responde por nadie. Prepara el borrador; quien lo envía es una persona.
2. **Procesa exportaciones, no buzones.** En la primera versión, la agenda llega como archivo
   (`.ics`) y los correos como archivos guardados en la carpeta. Una conexión directa al correo
   o al calendario es otra decisión, por la sensibilidad de lo que trae.
3. **Un compromiso se da por cumplido solo con su evidencia.** Que alguien diga «ya está» queda
   como declarado, en un campo separado de lo evidenciado, como en las demás familias.

## Diseño propuesto

| Qué | Propuesta |
|---|---|
| Para quién | La oficina del presidente o del gerente general, y quien asiste a un ejecutivo de la alta dirección |
| Qué procesa | La agenda exportada; por cada órgano (junta, comité directivo, comités), su agenda, su material y su acta; los correos de seguimiento guardados; y los informes que ya publican las demás familias en sus carpetas, como cualquier otro documento |
| Lo que calcula el código | Compromisos vencidos sin evidencia; compromisos sin fecha o sin responsable; compromisos movidos más de N veces; reuniones sin acta pasados N días; reuniones cuyo material no está N días antes; decisiones del acta sin compromiso que las ejecute. Los umbrales son configuración |
| Entregables | El estado de los compromisos de dirección, por órgano y por responsable; el paquete de la próxima reunión de cada órgano, con lo abierto de la anterior y lo que reportan las familias; y el resumen semanal para el ejecutivo |
| Comandos, en borrador | `ea-setup`, `ea-scan`, `ea-commitments`, `ea-prep`, `ea-weekly`, `ea-wake` |
| Nunca | Envía, agenda, acepta, declara cumplido un compromiso sin evidencia, prioriza por el ejecutivo |
| Carpetas | `direccion/` con `agenda/`, `organos/<órgano>/<fecha>/` (agenda, material, acta) y `seguimiento/` |
| Prueba | Material sintético por industria y una entidad de control por país, con su clave, con el mismo arnés `tests/ronda_familia.py`; primero el motor contra la clave y después la ronda con el agente |

**La secretaría de junta** (los acuerdos del acta contra su cumplimiento) reutiliza este mismo
agente cuando el órgano es la junta. Queda como un modo del asistente, no como un agente aparte,
hasta que una ronda muestre que necesita reglas propias.

## Lo que falta decidir

1. **El nombre del agente.** Cada nombre de Criterio dice lo que hace la capacidad. Candidatos:
   - **Ofelia**, del griego *ōphéleia*, «ayuda»: es la que prepara.
   - **Mónica**, que la tradición asocia con el latín *monere*, «advertir, recordar». La
     etimología no es segura.
2. **La sigla y el nombre de la familia** en el mapa y en el repositorio. El grupo del mapa es
   «Transversales».
3. **Si la primera versión incluye la exportación del calendario** o empieza solo con las actas
   y el material de cada órgano.

## Alternativas descartadas

**Un agente del CEO.** Duplica lo que preparan las demás familias y su entregable sería una
opinión sobre el negocio, no un contraste contra documentos.

**Conectar el correo y el calendario desde la primera versión.** Es la entrada más útil y la más
sensible: el buzón de un ejecutivo trae información de toda la organización. Se decide aparte,
con su propia revisión de privacidad.

**Extender a Samuel.** Samuel responde por un proyecto y su cadencia es la reunión de
seguimiento. La oficina del ejecutivo cruza órganos y proyectos, y tiene otros dueños.

## Consecuencias

- El diseño se escribe en `families/criterio-<sigla>/DISENO.es.md` desde las mismas tres fuentes
  que las familias CFO y CLO (`familia.json`, `carpetas.json`, `fuentes.json`), con
  `scripts/familias.py`.
- Las reglas de compromiso pasan al núcleo común, y las pruebas de Samuel tienen que seguir
  dando lo mismo antes y después del cambio.
- El mapa de la página de Agentes lo muestra como «Siguiente», sin fecha, hasta que la familia
  esté construida y probada.
