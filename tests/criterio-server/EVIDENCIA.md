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

## Lo que no prueba

Las rondas de la familia PMO levantan Rostrum de punta a punta sobre lo que los agentes de verdad
escribieron. Con las familias CFO y CLO eso todavía no se ha hecho: es el paso siguiente, en la
primera ronda con sus agentes.
