# Criterio

**Un market de agentes que aceleran capacidades organizacionales.**

[English](README.md) · [Términos](TERMS.es.md) · [Descargo](DISCLAIMER.es.md) · [Cómo aportar](CONTRIBUTING.es.md)

Apache 2.0 · Se instala en cuatro clics · Cada agente produce su primer resultado en quince minutos

---

## Qué es

Una organización no se mueve por departamentos: se mueve por **capacidades**. La capacidad de gobernar un portafolio de proyectos. La de cerrar un mes y saber qué dicen los números. La de revisar un contrato antes de firmarlo.

Cada una de esas capacidades tiene su método, su lenguaje y sus formas propias de fallar. Un asistente genérico no sabe qué es una línea base, ni por qué replanificar esconde el atraso, ni por qué una exclusión de responsabilidad redactada en absoluto no vale.

**Criterio es un market de agentes, uno por capacidad.** Se instalan, se configuran hablando, y se bajan al equipo que hace ese trabajo.

---

## Las capacidades

| Capacidad | Agentes | Estado |
|---|---|---|
| **[PMO](capabilities/pmo.es.md)** — gobierno de portafolio y de proyectos | Agente PMO · Agente PM | **Agente PMO disponible**, Agente PM en construcción |
| **CFO** — cierre, control y reporte financiero | — | Declarada |
| **CLO** — contratos, cumplimiento y riesgo legal | — | Declarada |

La lista no está cerrada. Una capacidad entra cuando hay alguien que la ejerce y quiere construir su agente.

---

## Instalación

**Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar marketplace desde GitHub → `josenanez-company/criterio`

**Claude Code**

```
/plugin marketplace add josenanez-company/criterio
```

Después de instalar, cada agente tiene un comando de instalación que mira tus carpetas, hace cinco preguntas y produce un primer resultado sobre tus propios documentos. **Nadie edita un archivo de configuración a mano.**

---

## Lo que comparten todos los agentes

No es una colección de asistentes sueltos. Todos se construyen sobre las mismas cuatro reglas, y de ahí sale que se puedan poner frente a un comité.

**Separan lo declarado de lo evidenciado.** Lo que alguien afirma va en una columna; lo que sustentan los documentos, en otra. Nunca se fusionan, y la diferencia entre las dos suele ser el hallazgo de más valor.

**Nada se sobrescribe.** Un registro guarda su historia. Cuando la versión nueva reemplaza a la anterior en silencio, desaparece justo lo que había que ver.

**El modelo extrae, el código calcula.** Leer una fecha es lectura. Restar, proyectar y sumar es aritmética, y la aritmética vive en código, donde es determinística y se puede probar. Ningún número de un informe sale de una estimación del modelo.

**Todo dato lleva su cita, o declara que no está.** *"No está dicho en ninguna parte"* es un hallazgo válido y esperado.

**Y saben callarse.** Corren solos y solo hablan cuando algo cruza un umbral. Un agente que reporta todas las semanas haya o no noticia se ignora en un mes.

---

## Evidencia

Cada capacidad publica las cifras de sus corridas reales: cuántos documentos, cuánto tomó, cuántos hallazgos, y cuáles nadie había visto. Junto con el procedimiento para que cualquiera las reproduzca.

**Las que todavía no se han medido no se inventan.** Todo el proyecto descansa en que una afirmación lleve su fuente; una cifra de marketing sin respaldo contradiría lo único que lo hace confiable. Mientras una capacidad no tenga corridas, su página lo dice.

Lo que se puede verificar hoy, clonando el repositorio:

```
python3 plugins/criterio-pmo/scripts/pmo.py selftest    la aritmética contra 12 resultados conocidos
python3 scripts/validate_plugins.py                     estructura y consistencia del market
```

---

## Apache 2.0 — qué entregamos y a qué invitamos

**Entregamos completo y sin condiciones** el método de cada agente, el esquema de sus registros, el código que calcula, sus criterios de aceptación y la forma de medirlos.

**A qué invitamos**

- Úsalo dentro de tu organización sin pedir permiso, y adáptalo a cómo trabajas.
- Cambia los criterios: los umbrales son configuración, no código.
- **Construye la capacidad que te falta.** Si ejerces una función que no está en la lista, su agente lo escribe quien la conoce, no quien sabe programar. El formato está en [CONTRIBUTING.es.md](CONTRIBUTING.es.md).
- Si encuentras que se equivoca, ábrelo como issue con el documento que lo demuestra. Vale más que una estrella.

**Lo que no afirmamos**

Esto produce borradores de trabajo, no decisiones. Nadie ha certificado nada aquí. Los agentes saben lo que se escribió, no lo que se habló fuera de los documentos. Lee el [descargo](DISCLAIMER.es.md) antes de instalar: usarlo implica aceptar los [términos](TERMS.es.md).

---

Mantenido por [José Francisco Ñáñez](https://josenanez.com).
