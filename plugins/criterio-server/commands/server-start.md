---
description: Levanta Rostrum, el portal de todas las familias, sobre el mapa que dejó server-setup, y dice qué hay que pedirle a la organización para publicarlo
argument-hint: "[rato|servicio] o vacío para que se pregunte"
allowed-tools: Read, Glob, Grep, Bash(python3:*), Bash(ls:*)
---

# /server-start — Rostrum, lo escrito para quien no abre una carpeta

> **Dónde está el mapa:** `.criterio/rostrum/config.json`, en la carpeta de trabajo. Lo escribe `/criterio-server:server-setup`. Si no existe, dilo en una línea y para: no lo armes aquí ni lo inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías. **Y sin subagentes en paralelo:** todo se hace en esta misma conversación.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" terminos --config <mapa>`. Si no están vigentes, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-server:server-setup`, que registra la aceptación.

## Para qué existe

Lo que los agentes escriben ya existe como archivos. **Este comando es cómo llega a alguien que no va a abrir una carpeta**, que es exactamente el caso del patrocinador, del comité o del gerente que quiere saber qué vence. Un patrocinador no descarga un ZIP. Abre un enlace o no lo abre.

**Es un portal para todas las familias**, no uno por agente: un patrocinador no tiene que saber a cuál entrar, y solo en un portal único se ve el mismo caso desde varias familias.

## Lo primero: hay dos formas, y no dan lo mismo

Pregúntalo antes de dar ninguna línea de comando, porque la respuesta cambia todo lo demás:

**«Para mirarlo un rato»**: alguien lo levanta, lo mira y lo apaga. No hay que pedirle infraestructura a nadie ni hablar con seguridad. Lo que se pierde: el patrocinador no tiene un enlace que funcione mañana.

**«Que quede corriendo»**: vive en una máquina de la organización y el patrocinador tiene un enlace estable. Es donde está el valor, y también donde está la conversación: alguien tiene que aprobar un puerto, un host y quién puede llegar.

Si la persona no sabe cuál quiere, la respuesta es **empezar por la primera**. Se levanta en diez segundos y se ve funcionando. Con eso en la mano, la conversación con seguridad cambia: ya no se pide permiso para una idea.

## Para mirarlo un rato

Antes de levantarlo, revisa el mapa contra el disco:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" revisar --mapa <mapa>
```

Si hay entradas `nuevas`, dilo y propón volver a `server-setup`. Si hay entradas `sin_estado`, di qué agente todavía no ha corrido. El portal las muestra como pendientes, sin inventarles nada. Si la PMO está en el mapa y no hay informe, corre primero `/criterio-portfolio:portfolio-report html`: el servidor no genera el informe, lo sirve.

Después lo levantas, con el mapa:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/servidor.py" --mapa <mapa>
```

Escucha en `127.0.0.1:8787`, **solo en ese equipo**. Imprime las direcciones de lo que hay en el mapa y se para con Ctrl-C. Si el puerto está ocupado, `--puerto 8788`.

Di qué hay y a quién le sirve cada cosa. Lo que aparece depende del mapa:

| Ruta | Qué es | Para quién |
|---|---|---|
| `/` | La portada: los agentes del mapa, una puerta por familia y el formulario de peticiones | Todos |
| `/pmo`, `/decisiones`, `/proyectos`, `/productos` | El informe de la PMO, si la familia PMO está en el mapa | La PMO, el comité y el patrocinador |
| `/familia/cfo`, `/familia/clo` | Cada familia: lo último que escribió el motor de cada agente, sus señales abiertas y sus reportes | El contralor, el área de FP&A, el área legal, el oficial de cumplimiento |
| `/reporte/…` | Un reporte tal como lo escribió el motor | Quien responde por él |
| `/vence` | Lo pendiente con fecha, de todas las familias: contratos, obligaciones, tareas del cierre, el comité | La gerencia |
| `/caso/<código>` | Todo lo que los agentes han hecho sobre un proyecto, un producto o un contrato | Quien pregunta por ese caso |
| `/corridas` | La historia de todas las corridas, de todos los agentes | Quien audita |
| `/estado.json` | De cuándo es lo de cada agente y cuántas peticiones tiene abiertas | Un mecanismo, no una persona |

**El caso cruza familias, y ahí está el valor de un solo portal.** Un proyecto de la PMO puede tener su línea en el presupuesto de Tomás y una señal de Clara, y la página del caso las junta. Esa vista no existe en ninguna otra parte.

Si la persona solo tiene la familia PMO y no ha corrido `server-setup`, el servidor también levanta como antes:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/servidor.py" --informe <carpeta del informe> --estado <estado de la PMO> --config <configuración de la PMO>
```

## Que quede corriendo

Aquí no basta con dar la línea. **Di también qué hay que pedir**, porque si la persona llega a seguridad sin eso, vuelve sin nada.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/servidor.py" --mapa <mapa> --abierto
```

`--abierto` hace que escuche fuera del equipo. El programa lo advierte al arrancar, y tú lo dices también:

> **No trae autenticación, y es a propósito.** Un servidor sobre la librería estándar no va a autenticar mejor que el proxy que la organización ya tiene, y prometer que sí sería exactamente lo que este plugin no hace. Se publica como se publica cualquier cosa adentro: detrás del control de acceso que ya existe.

Lo que hay que pedirle a la organización, en estos términos:

| Qué se pide | Por qué |
|---|---|
| Un host dentro de la red y un puerto | Es donde vive. No necesita salir a internet |
| Publicarlo detrás del control de acceso que ya usan | El servidor no autentica. Esa capa la pone la organización |
| Que el equipo siga encendido | Si se apaga, el enlace deja de funcionar. No hay alta disponibilidad y no hace falta: lo que sirve se vuelve a producir |
| Nada más | No necesita base de datos, ni certificado propio, ni salida a internet, ni una cuenta de servicio con permisos |

Y lo que **no** hay que pedir, porque conviene decirlo: no toca ninguna carpeta de documentos, no escribe ninguna ficha y no manda correos.

Para que arranque solo, ofrece la forma que corresponda al sistema —`launchd` en macOS, `systemd` en Linux, el Programador de tareas en Windows— con la ruta absoluta del intérprete y del mapa. **No inventes rutas:** pregunta o tómalas del mapa.

## La cola de peticiones

La portada tiene un formulario con un **«Para quién»**: cada agente e instancia del mapa. No contesta a nadie en el momento: **escribe la petición en `<estado>/peticiones/` del agente elegido**, y ahí se queda hasta que ese agente despierte.

Eso es deliberado y hay que decirlo cuando se explique la capacidad: **el servidor no puede correr el agente.** Si pudiera, cualquiera que alcanzara el puerto podría hacer que el agente procesara documentos, y dos personas que abren la misma página verían cosas distintas.

Cada agente las toma en su `*-wake`: una petición abierta **rompe su silencio**, y cuando la responde la marca.

## Lo que Rostrum no hace

Dilo antes de que lo pregunten, no después:

- **No calcula.** Sirve lo que los agentes ya escribieron. Abrir la página no dispara ningún procesamiento de documentos. Por eso dos personas ven lo mismo, y cada página dice de cuándo es.
- **No escribe ninguna ficha.** El único archivo que crea es la petición, en la carpeta `peticiones/` del agente al que va.
- **No autentica.** Ver arriba.
- **No manda nada.** No hay correo, ni notificación, ni integración. Si algo tiene que llegar a un buzón, hoy lo reenvía una persona.

## Cierre

Cierra diciendo **qué enlace le pasa a quién**: `/` al patrocinador, `/familia/clo` al área legal, `/vence` a la gerencia. Di también de cuándo es lo que cada uno va a ver. La portada lo dice sola, pero conviene que la persona lo sepa antes de mandar el enlace.
