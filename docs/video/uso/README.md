# El video de uso de cada familia

Cada familia tiene dos videos en YouTube: el de **presentación** (qué hace, animado desde el portal:
`grabar.mjs`) y el de **uso**, este: una sesión real de Claude Code que instala la familia, la configura
sobre material sintético, muestra el primer resultado y le pide algo a cada agente en lenguaje natural.
Sin voz, con textos. Lo que se ve en la terminal es lo que pasó: el montaje acelera, sostiene y corta,
pero no cambia lo que Claude Code escribió.

## Los pasos

1. **La carpeta de trabajo**: la entidad de prueba de la familia, sacada de la demostración
   (`plugins/criterio-server/demo/criterio-demo.zip`), sin su estado. Por ejemplo, para la CFO,
   `finanzas/900123456-banco-andino` dentro de una carpeta `banco-andino/`.
2. **La toma.** Claude Code arranca en una terminal virtual de 120 × 36, con su propia configuración y un
   entorno limpio, y queda grabando:

   ```
   python3 uso/sesion.py uso/tomas/cfo-es arrancar ~/banco-andino
   python3 uso/sesion.py uso/tomas/cfo-es texto "/plugin marketplace add josenanez/criterio"
   python3 uso/sesion.py uso/tomas/cfo-es tecla enter
   uso/espera.sh uso/tomas/cfo-es           # hasta que la terminal quede quieta o pida una decisión
   ```

   Se instala la familia, se corre su setup, se contesta cada pregunta como lo haría la persona, los
   términos se aceptan como «Usuario de demostración» y, al final, una pregunta en lenguaje natural a dos
   agentes. Lo que se escribió va, en orden, en el `escrito` del guion.
3. **La línea de tiempo y el montaje**, desde el guion (`uso/guiones/<familia>.<idioma>.json`):

   ```
   python3 uso/linea.py uso/tomas/cfo-es uso/guiones/cfo.es.json
   python3 uso/montaje.py uso/tomas/cfo-es uso/guiones/cfo.es.json
   ```

   Las reglas del montaje son las mismas en cada video: lo que escribe la persona va a 1,4×; lo que hace el
   agente se comprime a una quinta parte, entre 1 y 5 segundos; lo que deja en pantalla se sostiene para
   leerlo; la espera se corta. El guion ajusta lo que hace falta por entrada (`entradas`) y dice qué capítulo
   va a la izquierda desde qué segundo de la toma (`capitulos`).
4. **El video**, cuadro por cuadro, con la terminal en xterm.js y los robots de las figuras del portal:

   ```
   PORTAL=../jf-amplify-portal node uso/render.mjs uso/tomas/cfo-es uso/guiones/cfo.es.json uso/tomas/cfo-es/criterio-cfo-uso-es.mp4
   PORTAL=… node uso/render.mjs uso/tomas/cfo-es uso/guiones/cfo.es.json cuadro.png --cuadro 1350   # un cuadro, para revisar
   ```

Lo único que se quita de la toma son los avisos del entorno donde se grabó, no de Criterio ni de Claude Code
al usarlo (`ocultar` en el guion). La toma, la configuración de esa sesión y el video quedan en
`uso/tomas/`, fuera del repositorio: el video se sube a YouTube y la fuente es el guion.

## Lo que el guion no puede decir

Los textos de los capítulos describen lo que se ve: cada cifra que citan está en la pantalla en ese
momento. Si una toma nueva cambia una cifra, el capítulo cambia con ella.
