# Evidencia · criterio-pm

Lo que Samuel puede demostrar hoy, y lo que todavía no.

Nada aquí es real. El corpus se construyó desde cero, como exige
[CONTRIBUTING.md](../../CONTRIBUTING.md).

## Lo que se corre

```
python3 tests/criterio-pm/generar.py    16 documentos en 2 proyectos, 7 minutas
python3 tests/criterio-pm/grade.py      19 comprobaciones
python3 plugins/criterio-pm/scripts/pmo.py selftest       la aritmética
python3 plugins/criterio-pm/scripts/texto.py --selftest   la conversión
python3 scripts/sincronizar.py --check  que las copias no se hayan separado
```

Con la librería estándar y sin instalar nada. La fecha de referencia es fija en
**2026-11-20**: una prueba que use la fecha de hoy cambia de respuesta cada semana.

## Por qué un corpus propio

El de `tests/criterio-pmo/` mira cuarenta proyectos desde arriba. Este mira **uno
desde adentro**, que es lo que Samuel ve, y no son intercambiables: un barrido de
portafolio no lee minutas semana a semana, y **la función central de Samuel vive
exactamente ahí**.

| Proyecto | Qué planta |
|---|---|
| **PRY-101** Pasarela de pagos QR | Ocho semanas de comité. Un compromiso **reprogramado tres veces** por la misma persona sobre lo mismo; uno **sin fecha** —«lo vemos la otra semana»—; dos **cumplidos con evidencia**, para que no todo sea hallazgo; un **hito vencido sin evidencia**; y un **riesgo dicho al pasar** que nunca entró al registro formal |
| **PRY-102** Portal de proveedores | **Control negativo.** Tiene reuniones, tiene compromisos, y no produce ni un hallazgo: todo lo prometido se cumplió con evidencia, nada venció, nada se reprogramó |

## Lo que la corrida prueba

| Qué se comprobó | Resultado |
|---|---|
| El compromiso reprogramado es **uno con historial**, no tres vencidos | 1 compromiso, 3 reprogramaciones, con sus tres fechas. Ninguno de los tres cuenta como vencido por separado |
| El reprogramado **no está vencido hoy** y aun así se reporta | Vence el 27 de noviembre, después del corte. La señal no es que se pase de fecha: es que nadie nombró el bloqueo |
| El compromiso **sin fecha** no desaparece | Se cuenta aparte. No puede estar vencido, y por eso mismo se perdía del informe |
| Lo cumplido con evidencia **no genera ruido** | Dos compromisos cerrados con su acta de recibo: cero señales |
| El hito vencido se detecta por **ausencia de evidencia**, no por la fecha | La certificación del 6 de noviembre, sin nada en el expediente |
| La declaración del gerente **no se contradice porque sí** | PRY-101 declara amarillo y la evidencia lo sostiene: `declared_vs_evidence` en falso. Un agente que contradice siempre es tan inútil como uno que nunca contradice |
| El riesgo **dicho y no registrado** queda marcado | `formally_registered: false`, con la cita de la minuta donde se dijo |
| El **conjunto exacto** de señales, no «al menos estas» | Una señal de más es un falso positivo, y el grader lo trata como falla |
| **El control negativo** | PRY-102: cero señales. Y probado ensuciándolo — se le metió un compromiso vencido y el grader lo detectó |

**Las respuestas se escribieron leyendo las minutas, no calculándolas.** Si salieran
de las mismas fórmulas que el código, esto no probaría nada.

## Lo que esta corrida NO cubre

Conviene decirlo antes de que alguien lo suponga.

- **La extracción nunca se ha corrido.** El estado se siembra copiando
  `expected/fichas/`, así que la cadena documento → modelo → ficha no se ha
  ejercitado. `grade.py --fichas` existe para eso y todavía no se ha ejecutado.
- **No hay comandos.** Samuel trae los ocho skills del método y la aritmética, y
  ninguna puerta propia. Lo que se prueba aquí es el cálculo, no el agente.
- **La ficha publicada y el contraste `pm_vs_pmo` están construidos pero no corridos
  de punta a punta.** `/pm-publish` escribe la ficha y `contrastar()` emite la señal con
  sus dos citas — verificado con siete comprobaciones en `pmo.py selftest` y con una
  corrida a mano sobre PRY-101. Lo que falta es que un agente de verdad publique y otro
  de verdad lea.
- **Ni agenda, ni acta, ni informe semanal.** Son las tres funciones que cierran el
  ciclo de la reunión y todavía no se han construido.

## Reproducirlo

```
python3 tests/criterio-pm/generar.py
mkdir -p /tmp/estado-pm/records
cp tests/criterio-pm/expected/fichas/*.json /tmp/estado-pm/records/
python3 plugins/criterio-pm/scripts/pmo.py compute --state /tmp/estado-pm --today 2026-11-20
python3 tests/criterio-pm/grade.py
```
