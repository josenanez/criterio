# 0026 · Una familia se instala de una vez y se configura en una sola conversación

**Fecha:** 2026-11-06 · **Estado:** aceptada el 2026-11-06 · **Modifica:** la instalación de cada familia y la regla de las referencias entre plugins

## Contexto

Cada agente es un plugin y se instala solo ([ADR 0004](0004-plugin-naming.md)). Es lo correcto
para quien responde por un rol: el contralor instala a Clara y nada más. Pero quien quiere la
familia completa hace hoy una instalación y un setup por agente: la CFO son tres instalaciones y
tres setups de unos quince minutos, y la entidad, la carpeta y dónde guardar el estado se
responden tres veces.

Claude Code permite que un plugin declare `dependencies` en su `plugin.json`: instalarlo instala
cada dependencia del mismo marketplace, y un manifiesto con solo su nombre y sus dependencias es
un plugin válido. Eso no existía cuando se fijó la regla de que los plugins se instalan por
separado.

José Francisco Ñáñez pidió el 6 de noviembre de 2026 que una familia se instale de una vez y se
configure con un solo setup.

## Decisión

1. **Un plugin por familia, `criterio-<sigla>`**, sin skills ni motor. Declara como dependencias
   los plugins de los agentes de su `familia.json` y Rostrum (`criterio-server`). Instalar
   `criterio-cfo@criterio` instala a Clara, a Tomás, a Áurea y a Rostrum.
2. **Un setup de la familia, `/criterio-<sigla>:<sigla>-setup`**, en las familias de más de un
   agente. No escribe ninguna configuración: corre el setup de cada agente, en el orden de su
   `familia.json`, en la misma conversación, y al final resume la familia. La configuración la sigue
   escribiendo el setup de cada agente, con su motor y sus validaciones. La EA, de un solo agente,
   no lo necesita.
3. **Lo que ya se respondió no se vuelve a preguntar.** Cada setup de agente agrega esa regla: si
   en la conversación ya quedaron fijados la carpeta, la entidad o dónde guardar el estado, los
   propone y pide solo que se confirmen.
4. **Los términos siguen siendo de cada agente.** Cada setup muestra los suyos y pide su sí; el
   setup de la familia no los resume ni los acepta por la persona.
5. **La versión del plugin de la familia es la de su familia** ([ADR 0017](0017-una-version-por-familia.md)),
   y sube con ella. `scripts/registro.py` lo cuenta entre los plugins de la familia.
6. **La regla de las referencias se mantiene para los agentes** —un comando solo referencia skills
   de su propio plugin— y se abre solo para el plugin de la familia, que nombra los comandos de sus
   dependencias declaradas. `scripts/validate_plugins.py` comprueba que sus dependencias sean
   exactamente los agentes de su `familia.json` más Rostrum, y que cada una esté en el marketplace.
7. **Instalar un agente suelto sigue igual.** Nadie que solo quiera a Clara instala la familia.

## Consecuencias

- Los nombres quedaron como se propusieron: `criterio-<sigla>` para el plugin y `<sigla>-setup` para
  su comando.
- **Necesita Claude Code 2.1.110 o posterior.** Probado el 6 de noviembre de 2026: la 2.1.109 y las
  anteriores instalan solo el plugin de la familia, sin sus agentes, y no avisan. La versión mínima vive
  en `scripts/familias.py` (`MIN_CLAUDE`) y su `--check` rompe si una página dice otra.
