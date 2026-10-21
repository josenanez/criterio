# 0010 · Rostrum es uno para todas las familias, y es un plugin propio

**Fecha:** 2026-10-21 · **Estado:** aceptada

## Contexto

Rostrum nació dentro de `criterio-portfolio` para publicar el informe de la PMO a quien no abre
una carpeta. Con la familia PMO completa ya era uno para tres agentes —Vera, Samuel y Alba—,
porque «un portal por agente obligaría a un patrocinador a saber a cuál entrar». Las familias
CFO y CLO llegaron después, y Rostrum no las ve:

- **Los agentes estaban escritos en el servidor**: tres nombres, tres plugins y sus comandos.
  Clara, Tomás, Fidel y Constanza no existían para él.
- **Los estados se adivinaban**: el de la PMO como raíz, sus hermanos `-proyectos` y `-productos`,
  y una búsqueda por contenido porque la primera corrida real los dejó en otro sitio.
- **Dos formatos de corrida**: la PMO escribe `<estado>/corridas.json`; los motores de CFO y CLO,
  `<estado>/corridas/registro.json`.
- **El rastro del arnés solo estaba en los tres plugins PMO.** En CFO y CLO la corrida dependía de
  que el agente obedeciera el último paso del comando, que es el defecto que `rastro.py` vino a
  quitar.
- **Solo Vera procesaba peticiones.** Un patrocinador no podía preguntarle a Clara.
- **Viajaba dentro de `criterio-portfolio`**: quien instala solo la CFO o la CLO no tenía servidor.

Se evaluó un servidor por familia. Se descarta: duplica el servidor, separa el portal y hace
imposible lo que solo un portal único puede mostrar —las caras del mismo caso en varias
familias: el proyecto, su línea de presupuesto, el contrato de su proveedor—.

## Decisión

**Rostrum es un plugin propio, `criterio-server`, uno para todas las familias.**

1. **El mapa se arma por selección de carpeta.** `server-setup` recibe la carpeta de trabajo, encuentra
   la configuración de cada agente bajo `.criterio/<área>/[<instancia>/]config.json` —la ubicación
   que ya fija cada setup— y cada una dice dónde está su estado. Muestra lo encontrado, la persona
   lo confirma o lo corrige y queda escrito en `.criterio/rostrum/config.json`. **Lo que no está en
   el mapa no se sirve**, y una familia nueva entra al mapa volviendo a escanear, sin tocar el
   servidor.
2. **Los agentes salen de su familia.** Cada familia declara sus agentes en `families/<familia>/familia.json`;
   `scripts/familias.py` escribe `agentes.json` junto al servidor. El servidor no lleva ningún nombre
   de agente escrito a mano.
3. **Un contrato de estado común**, que cumple todo agente:
   - `<estado>/corridas.json` y `<estado>/corridas/<id>.md`, con el mismo esquema en todas las familias;
   - `reporte-<comando>.md` y `resultados.json` donde el motor los escribe;
   - `resultados.json` trae `vence`: lo que tiene fecha y está pendiente, calculado por el motor;
   - `<estado>/peticiones/<id>.json`, con un solo esquema, y cada `*-wake` responde las suyas.
4. **El rastro del arnés va en todos los plugins**, copiado con `scripts/sincronizar.py`.

## Lo que no cambia

Rostrum **no calcula nada y no escribe ninguna ficha**: sirve lo que los agentes ya escribieron.
Lo único que escribe son las peticiones, en la carpeta `peticiones/` del estado del agente al que
van dirigidas. **No autentica**: escucha en `127.0.0.1` salvo que se le pida otra cosa, y publicarlo
se hace detrás del control de acceso de la organización.

## Consecuencias

- `/criterio-portfolio:portfolio-server` pasa a `/criterio-server:server-start`. Las evidencias de
  las rondas anteriores conservan el nombre con que corrieron.
- `robots.py` pasa a `criterio-server`: el servidor es quien dibuja a todos.
- El servidor conserva `--informe` y `--estado` para quien lo levante solo con la PMO; con `--mapa`
  sirve todas las familias.
- La hoja de ruta tenía a Rostrum como plugin propio en la 0.10.0; entra antes, sin el Gantt ni la
  revisión visual, que siguen en esa versión.
