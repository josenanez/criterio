# 0027 · A cada agente se le pide en palabras, por su nombre

**Fecha:** 2026-11-06 · **Estado:** propuesta · **Modifica:** la forma de entrar a cada agente; no cambia ningún comando existente

## Contexto

Los catorce agentes tienen entre seis y diecisiete comandos cada uno, con nombres en inglés que
se escriben con el prefijo del plugin: `/criterio-finance:bank-reconcile`. Quien dirige una
función no sabe cuál de ellos resuelve lo que necesita, y no tiene por qué saberlo. Lo que sabe
decir es lo que necesita: «concilia las cuentas de octubre», «qué contratos vencen este mes».

José Francisco Ñáñez pidió el 6 de noviembre de 2026 un comando de entrada por agente que
reciba el pedido en palabras y lleve al comando que corresponde.

## Propuesta

1. **Cada agente tiene un comando con su nombre:** `/criterio-portfolio:vera`,
   `/criterio-finance:clara`, `/criterio-legal:fidel`… Sin argumento, muestra lo que el agente
   sabe hacer, por grupos y sin nombres de comando; con argumento, elige el comando que lo
   resuelve, dice en una línea cuál y por qué, y lo corre.
2. **No hace el trabajo ni escribe nada.** Lo hace el comando elegido, con su motor, sus reglas
   y su corrida. Si dos comandos encajan, pregunta; si el pedido es de otro agente de la
   familia, da su entrada; si no es de nadie, lo dice. No improvisa con lo que hay en la
   conversación.
3. **No tiene texto propio.** `scripts/familias.py` lo escribe desde los grupos del agente —los
   mismos que publica Rostrum— y la descripción de cada comando, y `--check` rompe la
   verificación si alguien lo edita a mano o si un comando cambia de descripción sin
   regenerarlo. Entra al grupo «Arranque y ritmo» de cada agente, después de la instalación.
4. **Se cuenta como un comando más** en cada página y en el manual, y tiene su contrato en el
   `contratos.json` de su plugin: no lee, no escribe y no llama al motor.

## Consecuencias

- Quien instala un agente aprende un solo nombre, el del agente, y lo demás se lo dice el agente.
- Los nombres de los comandos existentes no cambian: quien ya los usa los sigue usando.
- La elección del comando la hace el modelo de lenguaje (LLM) sobre la tabla generada; la tabla
  es verificable, la elección todavía no. **Por probar:** una ronda con pedidos en palabras por
  cada grupo, uno ambiguo y uno de otro agente de la familia, contra la elección esperada.
