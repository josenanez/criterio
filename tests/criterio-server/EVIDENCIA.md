# criterio-server · qué prueba cada corrida

Escrito a mano. Rostrum no tiene material propio: sirve lo que escriben los agentes. Sus dos
selftests arman, en una carpeta temporal, lo que un agente habría dejado, y lo piden como lo pediría
un navegador.

## `servidor.py --selftest`

**La familia PMO sola, sin mapa**, como se levantaba antes: un estado con dos cortes y dos corridas,
el informe de un proyecto y de un producto, y un archivo vecino que no debe salir. Comprueba que
cada ruta declarada responda, que ninguna se salga de la carpeta —`..`, rutas absolutas, un vecino
en disco—, que una petición quede en la cola sin cambiar la ficha byte a byte, y que la historia,
lo que se arrastra, el corte y la página de cada corrida digan lo que el estado dice.

**Las tres familias en un mapa**: la PMO con su informe, Clara con un `resultados.json` que trae una
señal sobre un proyecto de la PMO y lo que vence, un reporte y una corrida en el formato común, y
Fidel con su calendario y un archivo en su estado que no es un reporte. Comprueba que:

- la portada lleve a los siete agentes y a Rostrum;
- cada familia tenga su puerta;
- el reporte se sirva tal cual, y nada del estado que no sea un reporte;
- lo que vence salga ordenado por fecha con el próximo comité;
- la señal de Clara aparezca en el caso del proyecto de la PMO;
- la petición llegue solo al estado del agente elegido;
- a un agente fuera del mapa no se le escriba.

## `mapa.py --selftest`

Una carpeta de trabajo con la configuración de la PMO, de Clara, de Fidel y de Tomás —esta sin
estado—, y una carpeta en `.criterio/` que no es de ningún agente. Comprueba que:

- cada agente se encuentre por la carpeta de su configuración;
- lo que falta se diga;
- el mapa guarde lo confirmado con rutas relativas;
- lo dejado fuera no vuelva solo;
- una familia instalada después aparezca como nueva.

## La auditoría de accesibilidad y uso, 2026-10-21

Se hizo con Chromium y axe-core sobre un espacio de trabajo de demostración con salidas reales de
los motores de las tres familias (la misma entidad de prueba para Vera, Clara, Tomás, Fidel y Constanza). Se corrió
[`accesibilidad/auditar.mjs`](accesibilidad/auditar.mjs) en cuatro configuraciones: el mapa con
las tres familias, el modo heredado solo con la PMO, un mapa solo con la CFO y un mapa con un
agente que todavía no ha corrido.

**Antes:** 131 páginas con el mapa completo.

- axe encontró seis reglas incumplidas:
  - sin `main`, y contenido fuera de toda región;
  - 109 páginas sin `h1`;
  - encabezados que saltan de nivel en 11 páginas;
  - en 8 páginas, migas cuyos enlaces solo se distinguían por el color, con 1,04:1 contra el
    texto de al lado;
  - en 32 páginas, cajas que se deslizan sin poderse alcanzar con el teclado.
- 10 enlaces llevaban a un 404.
- El menú del teléfono no se abría con el teclado.
- Los robots se movían sin parar (WCAG 2.2.2).
- El borde de los campos del formulario tenía 1,7:1 contra el fondo (WCAG 1.4.11 pide 3:1).

En la lectura:

- las señales salían como código (`trial_balance_unbalanced`), cortado a mitad de palabra en las
  tablas de los reportes;
- en un teléfono, las tablas anchas quedaban cortadas;
- en un portal sin la PMO, el formulario decía «proyecto»;
- dos textos describían a los agentes con «leyó».

**Después:** 138 páginas con el mapa completo, 78 con el modo heredado, 34 con solo la CFO y 21
con un agente sin corridas.

- En las cuatro configuraciones axe no encuentra ninguna incumplida.
- No hay enlaces rotos ni errores de consola.
- Ninguna página se sale del ancho a 1280, 768, 390 ni 320 px, y ninguna letra baja de 12 px.
- El primer Tab salta al contenido y el foco se ve.
- El menú del teléfono se abre con el teclado.
- El formulario no se envía sin texto.
- Los robots se paran solos antes de cinco segundos.

**Con la marca y «Dónde trabaja»**, la misma auditoría se volvió a correr con el mapa de las tres
familias: 139 páginas, ninguna regla incumplida.

Desde ahora, el `--selftest` de `informe.py` y el de `servidor.py` comprueban sin navegador:

- el contraste de la paleta;
- el tamaño mínimo de letra;
- la estructura de cada página enlazada;
- que los robots se paren.

## Lo que no prueba

Las rondas de la familia PMO levantan Rostrum de punta a punta sobre lo que los agentes de verdad
escribieron. Con las familias CFO y CLO eso todavía no se ha hecho: es el paso siguiente, en la
primera ronda con sus agentes.
