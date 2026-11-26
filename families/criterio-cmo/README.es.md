<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-cmo-oscuro.svg"><img src="../../docs/img/marca/es/criterio-cmo-claro.svg" alt="Criterio CMO · El mercadeo" height="48"></picture>

# criterio-cmo · la familia del mercadeo

**Dos agentes y un portal, alrededor de sus fichas.** Cada uno extiende a una persona distinta del área de
mercadeo —quien responde por lo que la marca anuncia y quien responde por lo que se invierte en las campañas— y
comparten la carpeta y la política de publicidad de la entidad: cada uno escribe solo su ficha.

[English](README.md) · [← Criterio](../../README.es.md) · Apache 2.0

![Criterio CMO](../../docs/img/es/cmo.png)

---

## Qué hace la familia

Una pieza llega a la calle después de pasar por la agencia, el área de mercadeo y legal. Lo que dice obliga
a quien la anuncia, y lo que se paga por ponerla en un medio se factura aparte, contra una campaña. Cuando
una afirmación no tiene con qué sostenerse o una campaña se pasa de su presupuesto, casi nunca es por mala fe:
es un soporte que nadie archivó, una aprobación que llegó tarde o una factura que nadie cruzó con su orden.
Ese cruce hoy se hace a mano, pieza por pieza y factura por factura. La familia lo calcula, sobre el Código de
Publicidad y Comunicaciones de Mercadeo de la ICC (F-01) y los estándares de resultados del MRC (F-02)
([decisión 0036](../../docs/decisions/0036-la-familia-cmo.md)).

- **Lucía** pone cada afirmación de una pieza al lado de su soporte y cada promoción al lado de sus
  condiciones, y dice qué pieza salió sin aprobación o sin identificarse como publicidad y qué base de
  contactos se usó sin autorización.
- **Próspero** pone cada campaña al lado de su presupuesto, su meta, su fecha de fin y sus facturas de
  pauta, y cada resultado del informe al lado de la plataforma.

## Lo que sigue siendo de las personas

Aprobar una pieza, juzgar la creatividad, decir si una afirmación es verdadera, aprobar o ampliar un
presupuesto y decidir cuál de dos cifras es la correcta. Los agentes dicen qué falta y dónde; la decisión es
siempre de legal, del área de mercadeo y de quien firma el informe.

## La estructura de carpetas recomendada

<!-- cmo:carpetas · generado por scripts/familias.py; no se edita a mano -->
Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, la política de publicidad; las piezas aprobadas con su registro; los soportes de las afirmaciones; las bases de cada promoción; el registro de bases de contactos, y el plan de mercadeo con las facturas de pauta, la exportación de la plataforma y el informe de resultados.

```
mercadeo/
└── <entidad>/
    ├── 00-politica/
    ├── 10-piezas/
    ├── 20-soportes/
    ├── 30-promociones/
    ├── 40-bases/
    └── 50-campanas/
estado-mercadeo/
```

**`<entidad>/`** · Lo que el área de mercadeo lleva de la entidad

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-politica/` | La política de publicidad y de aprobación de piezas, con sus tolerancias | Lucía, Próspero |
| `10-piezas/` | Cada pieza aprobada con su texto y el registro de piezas: su canal, su fecha de publicación, su aprobación y si es pagada a un influenciador | Lucía |
| `20-soportes/` | Los soportes de cada afirmación: estudios, mediciones, certificados y comparativos | Lucía |
| `30-promociones/` | Las bases de cada promoción, con su vigencia y sus condiciones de modo y lugar | Lucía |
| `40-bases/` | El registro de bases de contactos: cada base con sus registros, su autorización para mercadeo y su fecha. Nunca los datos de una persona | Lucía |
| `50-campanas/` | El plan de mercadeo con el presupuesto, la meta y la base de cada campaña; las facturas de pauta; la exportación de la plataforma y el informe de resultados | Próspero, Lucía |

**`estado-mercadeo/`** · Lo que escriben Lucía y Próspero: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cmo:carpetas -->

Un archivo sin el formato esperado no se adivina: se reporta con lo que le falta.

## Instalación de la familia

Necesita Claude Code 2.1.110 o posterior; si algo falla, [la instalación paso a paso](../../docs/instalacion.es.md).

**La familia se instala de una vez.** El plugin `criterio-cmo` trae a sus agentes y a Rostrum, y
`/criterio-cmo:cmo-setup` los configura en orden, en una sola conversación: lo que ya se respondió
no se vuelve a preguntar.

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-cmo@criterio
/criterio-cmo:cmo-setup
```

Después, a cada agente se le pide en tus palabras, sin saber cómo se llama cada comando:
`/criterio-claims:lucia` y `/criterio-campaigns:prospero`
([decisión 0027](../../docs/decisions/0027-cada-agente-se-pide-en-palabras.md)).

## De qué responde cada agente, y dónde está su detalle

<!-- cmo:familia-agentes · generado por scripts/familias.py; no se edita a mano -->
| | De qué responde | Lo que nunca hace | Su página | Sus pruebas |
|---|---|---|---|---|
| **Lucía** · lo que se anuncia | Cada pieza aprobada contra su soporte, cada promoción contra sus condiciones publicadas y cada base de contactos contra su autorización: la afirmación sin soporte, la comparativa sin fuente, la promoción sin vigencia o sin condiciones, la pieza pagada a un influenciador sin identificarse como publicidad, la pieza publicada sin la aprobación de legal y la base usada sin autorización para mercadeo | No aprueba una pieza, no juzga la creatividad, no dice si una afirmación es verdadera, no procesa los datos de una persona y no se conecta a una plataforma | [criterio-claims](../../plugins/criterio-claims/README.es.md) · 8 comandos, 3 skills | [resultados](../../tests/criterio-claims/RESULTADOS.md) |
| **Próspero** · lo que se invierte | El presupuesto de cada campaña contra la pauta facturada y contra su resultado medido: la campaña que pasó su presupuesto, la factura de pauta sin campaña ni orden, la campaña sin meta ni indicador, el resultado reportado que no coincide con la plataforma y la pauta facturada después de la fecha de fin | No aprueba un presupuesto, no juzga una campaña, no decide cuál cifra es la correcta y no se conecta a una plataforma de pauta ni de analítica | [criterio-campaigns](../../plugins/criterio-campaigns/README.es.md) · 8 comandos, 3 skills | [resultados](../../tests/criterio-campaigns/RESULTADOS.md) |
| **Rostrum** · el portal | Publicar lo que escriben los agentes donde el equipo lo vea, y recibir la pregunta de quien no abre una carpeta | **No escribe en el estado ni recalcula nada**, y no decide nada | [criterio-server](../../plugins/criterio-server/README.es.md) · 3 comandos, uno para todas las familias | [resultados](../../tests/criterio-server/RESULTADOS.md) |
<!-- /cmo:familia-agentes -->

## Cómo se configura y cada cuánto corre cada uno

<!-- cmo:configuracion · generado por scripts/familias.py; no se edita a mano -->
| | Lucía | Próspero |
|---|---|---|
| **Se instala** | `criterio-claims` | `criterio-campaigns` |
| **Instancias** | Una por entidad | Una por entidad |
| **Se configura con** | `/criterio-claims:claims-setup` | `/criterio-campaigns:campaigns-setup` |
| **Cuánto tarda eso** | Quince minutos | Quince minutos |
| **Qué le tienes que decir** | Entidad y su identificación fiscal, país y el periodo | Entidad y su identificación fiscal, país, el periodo y las dos tolerancias de la política: sobre el presupuesto y entre un resultado y la plataforma |
| **Dónde queda** | `.criterio/piezas/<entidad>/config.json`, escrito por el comando | `.criterio/campanas/<entidad>/config.json`, escrito por el comando |
| **El que se le pone a un reloj** | `/criterio-claims:claims-wake` | `/criterio-campaigns:campaigns-wake` |
| **Qué toca cada día** | Decide si toca procesar las piezas —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Decide si toca procesar las campañas —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla |
| **Qué lo despierta además del reloj** | Una pregunta que alguien dejó en Rostrum | Una pregunta que alguien dejó en Rostrum |
<!-- /cmo:configuracion -->

**Nadie edita un archivo de configuración a mano.** Se dice en la conversación y el comando lo reescribe.
Las tolerancias, las metas y quién aprueba cada pieza salen de la política de publicidad de la organización.

## Las pruebas de la familia

**Una sola puerta corre todo lo que este repositorio comprueba**, de todas las familias a la vez:

```
python3 scripts/verificar.py
```

Lo propio de la CMO está en [`tests/criterio-cmo/`](../../tests/criterio-cmo/): material sintético con
una clave que el motor no ve y dos entidades de control, donde cualquier señal es una falla. **Una señal
de más cuenta igual que una de menos.** Qué se siembra y qué no prueba el material, en
[`EVIDENCIA.md`](../../tests/criterio-cmo/EVIDENCIA.md).

## Hoja de ruta

<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->
<!-- /hoja de ruta -->

## Los skills de la familia

<!-- cmo:skills-familia · generado por scripts/familias.py; no se edita a mano -->
Cuatro skills distintos entre los dos agentes. **Los que comparten son copias literales, no un módulo importado**: un plugin instalado tiene que correr solo. `scripts/sincronizar.py` las copia y `scripts/sincronizar.py --check` falla si se separan.

| Skill | Lucía | Próspero |
|---|:--:|:--:|
| `claim-record` | ● | · |
| `marketing-intake` | ● | ● |
| `marketing-policy` | ● | ● |
| `result-record` | · | ● |
<!-- /cmo:skills-familia -->

## Estado

<!-- cmo:estado · generado por scripts/familias.py; no se edita a mano -->
| Agente | Se instala | Su prueba |
|---|---|---|
| **Lucía** · Lo que se anuncia | `criterio-claims` · 8 comandos, 3 skills | El motor, probado; con el agente, todas las entidades del material, hasta la ronda 1 · [resultados](../../tests/criterio-claims/RESULTADOS.md) |
| **Próspero** · Lo que se invierte | `criterio-campaigns` · 8 comandos, 3 skills | El motor, probado; con el agente, todas las entidades del material, hasta la ronda 1 · [resultados](../../tests/criterio-campaigns/RESULTADOS.md) |
| **Rostrum** · el portal | `criterio-server` · 3 comandos, para todas las familias | — |

Las pruebas usan material sintético construido sobre información real de empresas, anonimizada antes de procesarse: ningún nombre, identificación, cifra ni dato personal que permita reconocer a una empresa o a una persona se conserva ni se publica. Lo que se publica de cada prueba son sus resultados, sin datos.
<!-- /cmo:estado -->
