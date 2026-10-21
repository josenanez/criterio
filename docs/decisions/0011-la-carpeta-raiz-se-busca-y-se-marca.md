# 0011 · La carpeta raíz se busca, y con permiso se marca

**Fecha:** 2026-10-21 · **Estado:** aceptada · **Modifica:** 0007

## Contexto

Cada agente necesita saber dónde están los documentos que procesa: la carpeta del portafolio, la
de un proyecto, la de finanzas o la legal de una entidad. Hasta ahora el setup lo preguntaba, y
quien instala un agente casi nunca sabe cuál de sus carpetas es «la carpeta de documentos».
Escribir una ruta a mano es donde más se equivoca la gente, y una carpeta equivocada no falla
ruidosamente: el agente procesa otra cosa.

Y una vez elegida, la carpeta no se distingue de las demás. Una copia de respaldo con la misma
estructura, una carpeta del año anterior o una de otra entidad se ven iguales en el explorador.

## Decisión

1. **El setup busca la raíz; no la pide.** `buscar-raiz`, en el motor de cada agente, recorre la
   carpeta de trabajo hacia abajo y propone las candidatas numeradas. Cada una lleva la evidencia
   de por qué parece serlo, sacada de la estructura recomendada de su familia: «tiene
   `00-referencia/` y nueve periodos», «se llama como un proyecto y tiene `00-gobierno/`». La
   persona contesta con un número. Lo hace `raiz.py`, uno para todos los agentes.
2. **Con el sí explícito de la persona, la raíz se marca** con un archivo de texto visible,
   `_CRITERIO_<QUÉ>.txt`: `_CRITERIO_PORTAFOLIO.txt`, `_CRITERIO_PROYECTO.txt`,
   `_CRITERIO_PRODUCTO.txt`, `_CRITERIO_FINANZAS.txt` y `_CRITERIO_LEGAL.txt`.
   - **Su nombre la hace visible:** empieza por guion bajo para salir primero en la carpeta y
     dice de qué es.
   - **Su texto no pide conocimientos:** dice qué agentes la procesan, de qué entidad o caso es y
     que no se mueva.
   - **La próxima búsqueda la pone primero,** con certeza, aunque al lado haya una copia idéntica.
3. **Es la única excepción a la 0007:** el único archivo que un agente escribe dentro de los
   documentos de la organización. Ningún inventario lo cuenta como documento, ningún agente lo
   procesa y borrarlo no pierde nada más que la marca.

## Alternativas descartadas

- **Solo el nombre de la carpeta.** Pedir que la carpeta se llame de cierta forma es pedir que
  la persona la renombre, y una carpeta compartida no siempre se puede renombrar.
- **La marca solo en la configuración del agente.** El agente sabría dónde está, pero la persona,
  en su explorador, seguiría sin distinguirla.
- **Una marca oculta, `.criterio`.** Es invisible justo para quien la necesita.

## Consecuencias

- Los siete setups buscan antes de preguntar y ofrecen la marca después de elegir.
- Los inventarios de los dos motores y el recorrido de la PMO saltan el marcador.
- El mapa de Rostrum dice de cada agente si su raíz está marcada.
- Los README, los skills de documentos y los criterios de aceptación dicen la excepción con las
  mismas palabras.
