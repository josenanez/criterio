# La forma de lo que Criterio entrega

Dos cosas gobiernan cada pieza que sale de aquí: **para quién está escrita** y **cómo se ve**.
La primera decide si alguien la lee. La segunda, si la reconoce.

---

## Para quién está escrita

Todo lo que construimos se diseña para **nivel C y sus escalas**. No es una preferencia de
tono: si no está diseñado así, no lo ven, y lo que no ven no les genera valor.

Y «sus escalas» importa tanto como el nivel: la misma pieza tiene que responder a tres
personas distintas. Si no podemos decir qué gana una de ellas, esa no lo adopta.

| Quién | Qué gana, dicho en su lenguaje |
|---|---|
| **Nivel C** | La decisión que hoy no puede tomar, y qué le cuesta no tomarla |
| **Dirección o VP** | Cuáles de sus proyectos no se sostienen, y qué necesita de él esta semana |
| **Gerente o analista** | La semana preparada: la lectura hecha, el informe armado, el compromiso vencido con nombre y fecha |

### Cómo se escribe una pieza, en orden

1. **El problema en su lenguaje**, no la descripción de la solución. *«Nadie ha leído junta la
   documentación que ya existe»* se entiende; *«consolidación de fichas con trazabilidad»* no.
2. **Lo que cuesta hoy**, con cifra citada y fuente. Nunca una cifra nuestra inventada.
3. **Cómo se instala**, en la primera pantalla. Una pieza que no dice cómo empezar no se
   empieza.
4. **El tiempo hasta el primer resultado**, sobre sus propios datos. Quince minutos con algo
   real vale más que una lista de funciones.
5. **Lo que nunca hace.** A este nivel la pregunta no es qué puede: es qué no va a pasar. La
   confianza es la puerta, no la capacidad.
6. **Y después, y separado por una línea visible, la mitad técnica.** El que decide tiene que
   saber dónde dejar de leer; el que audita tiene que encontrarlo todo.

### Lo que no se hace

- **Nada de jerga interna en la primera mitad.** «Ficha», «skill», «aguas arriba», «esquema»
  no significan nada fuera de este repositorio.
- **No se abre comparando con otra herramienta.** A quien decide no le interesa qué plugin
  existe o no existe: le interesa qué decisión gana.
- **No se abre con una tabla de comandos.** Una tabla de comandos es el índice de un manual,
  y un manual no vende una capacidad.
- **No se promete lo que el insumo no permite.** Prometer capacidad o beneficios cuando los
  datos no están en la carpeta quema la credibilidad de todo lo demás.

Lo verifica `tests/coherencia.py`: el README de cada plugin tiene que traer su instalación,
su tiempo hasta el primer resultado y su sección de lo que nunca hace. **Si falta una, falla.**

---

## Cómo se ve

Toda pieza que se vea —el informe que produce un agente, la proyección en el servidor, un
diagrama, una tarjeta social, una lámina— **usa el diseño de [josenanez.com](https://www.josenanez.com)**.
No es decoración: es la misma marca, y cada pieza que sale de aquí la sostiene o la diluye.

**Fuente única de verdad: `lib/palette.ts` del portal.** Este archivo es una copia de trabajo
para que el repositorio sea autocontenido; cuando el portal cambie un token, manda el portal.

---

## Dos modos, no dos paletas

El mismo rol tiene un valor sobre crema y otro sobre negro. **Usar el del modo equivocado es el
error que más ha costado en el portal**, y es lo que hay que revisar primero en cualquier pieza
nueva.

Los contrastes están medidos contra el fondo de su propio modo. El mínimo es 4,5:1 para texto
normal y 3:1 para texto grande —24 px, o 18,66 px en negrita—, según WCAG AA.

## Superficies

| Token | Valor | Rol | Modo |
|---|---|---|---|
| `negro` | `#050505` | Fondo de sección oscura | ambos |
| `panelOscuro` | `#0c0c0b` | Tarjeta sobre fondo oscuro | oscuro |
| `tinta` | `#111111` | Fondo de elemento activo, y título sobre crema | ambos |
| `crema` | `#f5f4ef` | Fondo de sección clara, y texto sobre oscuro | ambos |
| `panelCrema` | `#efeee8` | Tarjeta sobre fondo claro | claro |
| `panelElevado` | `#f8f7f3` | Tarjeta que debe leerse por encima de la crema | claro |
| `lavadoOro` | `#fffaf0` | Fondo cálido para destacar una fila o una nota | claro |

## Filetes

| Token | Valor | Rol | Modo |
|---|---|---|---|
| `fileteClaro` | `#c9c6bd` | Línea divisoria sobre crema | claro |
| `fileteClaroSuave` | `#d8d5cd` | Línea divisoria tenue sobre crema | claro |
| `fileteOscuro` | `#2b2b28` | Línea divisoria sobre negro | oscuro |
| `fileteOscuroSuave` | `#4a4740` | Línea divisoria marcada sobre negro | oscuro |
| `fileteOro` | `#d7c7a4` | Línea que enmarca un bloque destacado en modo claro | claro |

## Texto

| Token | Valor | Rol | Modo | Contraste |
|---|---|---|---|---|
| `cuerpo` | `#3f4450` | Párrafo sobre crema | claro | 8,9:1 |
| `apagadoFrio` | `#616a7e` | Etiqueta y nota sobre crema | claro | 4,9:1 |
| `apagadoClaro` | `#6b675f` | Texto secundario sobre crema | claro | 5,5:1 |
| `apagadoOscuro` | `#8a867e` | Texto secundario sobre negro | oscuro | 5,6:1 |
| `blanco` | `#ffffff` | Texto sobre negro. Se atenúa con opacidad | oscuro | |

## Oro — el acento

| Token | Valor | Rol | Modo | Contraste |
|---|---|---|---|---|
| `oroOscuro` | `#d5a84b` | Acento sobre negro | oscuro | 9,3:1 |
| `oroClaro` | `#8a6327` | Acento sobre crema | claro | 4,9:1 |

## Semánticos

| Token | Valor | Rol | Modo | Contraste |
|---|---|---|---|---|
| `okClaro` | `#3f6b4a` | Indicador positivo sobre crema | claro | 5,6:1 |
| `okOscuro` | `#7fae89` | Indicador positivo sobre negro | oscuro | 8,1:1 |
| `okFondo` | `#e7eee7` | Fondo de bloque positivo | claro | |
| `errorClaro` | `#8f3a2c` | Indicador negativo sobre crema | claro | 6,9:1 |
| `errorOscuro` | `#c97b6b` | Indicador negativo sobre negro | oscuro | 6,3:1 |
| `errorFondo` | `#f3e7e3` | Fondo de bloque negativo | claro | |
| `errorFilete` | `#ddc2ba` | Línea de bloque negativo | claro | |
| `alertaClaro` | `#8a4412` | Advertencia sobre crema | claro | 7,4:1 |
| `alertaFondo` | `#f4ead9` | Fondo de bloque de advertencia | claro | |
| `infoClaro` | `#3d5d75` | Nota informativa sobre crema | claro | 6,3:1 |
| `infoOscuro` | `#7f9db5` | Nota informativa sobre negro | oscuro | 7,2:1 |
| `infoFondo` | `#e6edf3` | Fondo de bloque informativo | claro | |
| `infoFilete` | `#cfdae3` | Línea de bloque informativo | claro | |

---

## Tipografía

**Inter Tight.** Variable, eje de peso 100–900, cobertura completa del español. En el portal se
sirve desde el propio build; una pieza generada fuera del portal usa las instancias estáticas en
400, 500 y 600.

Nada de segunda familia. La jerarquía sale del peso y del tamaño, no de mezclar tipografías.

## Lo que no se hace

- **No entra un hex que no esté en esta tabla.** En el portal eso lo verifica
  `scripts/check-palette.mjs` contra `prebuild`. Una pieza de Criterio se revisa contra este
  documento.
- **No se usa un color en el modo que no le corresponde.** La columna *Modo* no es informativa.
- **No se traduce el semáforo del proyecto a los semánticos sin pensarlo.** Verde, amarillo y
  rojo son la declaración del gerente; `okClaro` y `errorClaro` son indicadores de la pieza. Que
  un proyecto declarado verde salga pintado de verde cuando el agente encontró evidencia que ese
  verde no explica es exactamente el error que este proyecto existe para evitar.
- **Los datos no se ilustran con imágenes.** Un número va como número o como gráfico sobre los
  datos, nunca como una captura.

## Dónde aplica

| Pieza | Aplica |
|---|---|
| Informe que produce un agente (`report.format: html`) | Sí, completo |
| Proyección y aplicación del servidor | Sí, completo |
| Diagramas y láminas de documentación publicada | Sí |
| Tarjetas sociales y piezas de difusión | Sí |
| Diagramas dentro de documentos de trabajo de este repositorio | No. Van en texto: se leen en cualquier editor y se comparan en un diff |
