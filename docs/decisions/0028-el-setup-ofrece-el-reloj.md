# 0028 · El setup ofrece el reloj, y lo crea solo con un sí

**Fecha:** 2026-11-06 · **Estado:** aceptada el 2026-11-06 · **Modifica:** el final del setup de cada agente y de cada familia

## Contexto

Cada agente trae el comando que un reloj invoca —`finance-wake`, `legal-wake`…—: mira qué toca hoy
según su frecuencia, lo hace, y si no toca nada se calla. Hasta ahora ponerlo en un reloj era del
lado de la organización, y casi nadie lo hace: sin reloj, el agente trabaja solo cuando alguien se
acuerda de llamarlo, que es justo lo que un agente viene a evitar.

José Francisco Ñáñez decidió el 6 de noviembre de 2026 que el setup ofrezca crear esa tarea.

## Decisión

1. **El setup de la familia ofrece una sola tarea** que corre, en orden, el reloj de cada agente que
   quedó configurado. Un agente que se configura solo, fuera de su familia, ofrece la suya. Samuel
   y Alba, que son una instancia por proyecto y por producto, corren una vez por cada uno.
2. **Los días hábiles a las 7:00**, como propuesta; la persona confirma o cambia la hora.
3. **Según dónde corre el setup.** Con una herramienta para crear tareas programadas —en Cowork, las
   de la app—, la crea ahí. En Claude Code en una terminal, arma la línea del programador del equipo
   (`crontab`) con `claude -p`, la muestra completa y la agrega solo con un sí.
4. **La tarea solo procesa y escribe en el estado de Criterio.** No envía nada. Sus permisos son los
   que declaran los comandos de reloj de sus agentes, y nada más; si un paso necesita otro, se
   detiene y lo deja dicho. En Claude Code, su salida queda en `.criterio/reloj/<familia o agente>.log`.
5. **Nunca sin un sí explícito.** Si la persona dice que no, el setup le dice cómo se corre a mano.
6. **No tiene texto propio.** El paso lo escribe `scripts/familias.py` en cada setup, desde los
   comandos de reloj de cada agente y sus permisos, y `--check` rompe si alguien lo edita a mano.

## Consecuencias

- **Después de cada versión nueva, la tarea se detiene** hasta que alguien acepte los términos de esa
  versión con la persona presente: la aceptación por versión no se da desatendida. Con una versión
  cada viernes, la primera corrida de la semana siguiente espera esa aceptación.
- En Claude Code, el equipo tiene que estar encendido a la hora de la tarea; si no, ese día no corre.
- La tarea es de quien la creó, en su equipo o en su cuenta: Criterio no la ve ni la administra.
