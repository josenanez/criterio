---
description: Levanta Rostrum, el servidor que expone el informe del portafolio, y dice qué hay que pedirle a la organización para publicarlo
argument-hint: "[rato|servicio] o vacío para que se pregunte"
---

# /portfolio-server — Rostrum, el informe para quien no abre una carpeta

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla.

## Para qué existe

El informe ya existe como archivos. **Este comando es cómo llegan a alguien que no
va a abrir una carpeta de archivos**, que es exactamente el caso del patrocinador.

Un patrocinador no descarga un ZIP. Abre un enlace o no lo abre.

## Lo primero: hay dos formas, y no dan lo mismo

Pregúntalo antes de dar ninguna línea de comando, porque la respuesta cambia todo lo
demás:

**«Para mirarlo un rato»** — alguien lo levanta, mira, y lo apaga. Cero
infraestructura que pedirle a nadie, y ninguna conversación con seguridad. Lo que se
pierde: el patrocinador no tiene un enlace que funcione mañana.

**«Que quede corriendo»** — vive en una máquina de la PMO y el patrocinador tiene un
enlace estable. Es donde está el valor, y también donde está la conversación: alguien
tiene que aprobar un puerto, un host y quién puede llegar.

Si la persona no sabe cuál quiere, la respuesta es **empezar por la primera**. Se
levanta en diez segundos, se ve funcionando, y con eso en la mano la conversación con
seguridad es distinta: ya no se está pidiendo permiso para una idea.

## Para mirarlo un rato

Antes de levantar nada, confirma que hay informe. Si no lo hay, corre primero
`/portfolio-report html`: el servidor no genera el informe, lo sirve.

```
python3 scripts/servidor.py --informe <carpeta> --estado <estado> --config <archivo>
```

Escucha en `127.0.0.1:8787`, **solo en ese equipo**. Imprime las tres direcciones y se
para con Ctrl-C. Si el puerto está ocupado, `--puerto 8788`.

Di qué hay y a quién le sirve cada cosa. **El portal tiene tres secciones**, y esa
estructura es lo que hace que un equipo lo use en vez de pedirte el informe:

| Ruta | Qué es | Para quién |
|---|---|---|
| `/` | La portada, con las tres secciones y el formulario de peticiones | Todos |
| `/pmo` | **Cómo va el portafolio.** Lo que solo se ve mirando todo junto: los verdes que la evidencia no sostiene, lo que lleva semanas en silencio, quién patrocina más de una cosa | La PMO |
| `/decisiones` | **Lo que necesita una decisión**, como pregunta cerrada y con la consecuencia de no decidirla | El comité y el patrocinador |
| `/proyectos` | El listado, ordenado por lo que más pide atención | Todos |
| `/p/<código>` | El informe de un proyecto. **Enlaza al producto que le dio origen** | Quien gerencia, y quien pregunta |
| `/productos` | El listado de productos, y los proyectos que no dicen cuál construyen | Quien responde por un producto |
| `/producto/<nombre>` | El informe de un producto. **Enlaza a los proyectos que lo construyen** | Quien responde por un producto |
| `/estado.json` | De cuándo es el informe y cuántas peticiones hay abiertas | Un mecanismo, no una persona |

**El enlace entre proyecto y producto va en los dos sentidos, y ahí está el valor de
tener las tres secciones.** Quien entra por el proyecto quiere saber para qué es lo que
está haciendo. Quien entra por el producto quiere saber quién lo está haciendo, y
descubre —si es el caso— que lo construyen proyectos que reportan a comités distintos,
de modo que ningún comité lo está viendo completo. Ese hallazgo no existe en ninguna
otra página.

Si la configuración tiene `organization.name`, el portal lleva el nombre de la
organización en todas las páginas. Pásale `--config` para que lo lea.

## Que quede corriendo

Aquí no basta con dar la línea. **Di también qué hay que pedir**, porque si la persona
llega a seguridad sin eso, vuelve sin nada.

```
python3 scripts/servidor.py --informe <carpeta> --estado <estado> --config <archivo> --abierto
```

`--abierto` hace que escuche fuera del equipo. El programa lo advierte al arrancar, y
tú lo dices también:

> **No trae autenticación, y es a propósito.** Un servidor de cien líneas sobre la
> librería estándar no va a autenticar mejor que el proxy que el banco ya tiene, y
> prometer que sí sería exactamente lo que este plugin no hace. Se publica como se
> publica cualquier cosa adentro: detrás del control de acceso que ya existe.

Lo que hay que pedirle a la organización, en estos términos:

| Qué se pide | Por qué |
|---|---|
| Un host dentro de la red y un puerto | Es donde vive. No necesita salir a internet |
| Publicarlo detrás del control de acceso que ya usan | El servidor no autentica. Esa capa la pone la organización |
| Que el equipo siga encendido | Si se apaga, el enlace deja de funcionar. No hay alta disponibilidad y no hace falta: el informe se regenera |
| Nada más | No necesita base de datos, ni certificado propio, ni salida a internet, ni una cuenta de servicio con permisos |

Y lo que **no** hay que pedir, porque conviene decirlo: no toca ninguna carpeta de
documentación, no escribe ninguna ficha, y no manda correos.

Para que arranque solo, ofrece la forma que corresponda al sistema —`launchd` en
macOS, `systemd` en Linux, el Programador de tareas en Windows— con la ruta absoluta
del intérprete y de las carpetas. **No inventes rutas:** pregunta o léelas de la
configuración.

## La cola de peticiones

La portada tiene un formulario. No contesta a nadie en el momento: **escribe la
petición en `<estado>/peticiones/` y ahí se queda** hasta que el agente despierte.

Eso es deliberado y hay que decirlo cuando se explique la capacidad: **el servidor no
puede correr el agente.** Si pudiera, cualquiera que alcanzara el puerto podría hacer
que el agente leyera documentos, y el portafolio dejaría de ser el mismo para dos
personas que abren la misma página.

El agente las ve porque `due` las cuenta:

```
python3 scripts/portafolio.py due --state <estado> --config <archivo>
python3 scripts/portafolio.py requests --state <estado>
```

Una petición abierta **rompe el silencio de `/portfolio-wake`**: es la única cosa que no es
aritmética de fechas y aun así hace que el agente hable. Alguien preguntó.

Cuando se responda una, se marca, y solo entonces deja de aparecer:

```
python3 scripts/portafolio.py answered --state <estado> --id <identificador>
```

## Lo que Rostrum no hace

Dilo antes de que lo pregunten, no después:

- **No calcula.** Sirve lo que `informe.py` ya escribió. Abrir la página no dispara
  ninguna lectura de documentos. Por eso dos personas ven lo mismo.
- **No escribe ninguna ficha.** El único archivo que crea es la petición, en su propia
  carpeta. El camino de escritura hacia el portafolio no existe en ese programa.
- **No autentica.** Ver arriba.
- **No manda nada.** No hay correo, ni notificación, ni integración. Si el informe
  tiene que llegar a un buzón, hoy lo reenvía una persona.

## Cierre

Cierra diciendo **qué enlace le pasa a quién**, y cuándo va a estar desactualizado el
informe — la portada lo dice sola, pero conviene que la persona lo sepa antes de
mandarle el enlace a su patrocinador.
