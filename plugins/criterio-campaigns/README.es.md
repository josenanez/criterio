<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-cmo-oscuro.svg"><img src="../../docs/img/marca/es/criterio-cmo-claro.svg" alt="Criterio CMO · El mercadeo" height="48"></picture>

# Próspero · lo que se invierte

<img src="../../docs/img/es/robot-prospero.gif" alt="Próspero" width="220" align="right">

**Próspero pone cada peso de la pauta al lado de lo que produjo.**
Tú respondes por la inversión en las campañas. Él llega con cada campaña al lado de su presupuesto, su factura y su resultado: la campaña que pasó su presupuesto, la factura de pauta sin campaña ni orden, la campaña sin meta ni indicador, la que siguió después de su fecha de fin y el resultado del informe que no coincide con la plataforma.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**El nombre.** Próspero, del latín *prosperus*, el que hace que algo rinda: cada peso de la pauta contra lo que produjo.
<!-- /agente:nombre -->

[English](README.md) · `criterio-campaigns` · Apache 2.0 · Una instancia por entidad

**Estado: construido y probado, en laboratorio, con la familia CMO.** El motor de cálculo, probado contra todo el material sintético de la familia con una clave que el agente no ve y entidades de control. En la 0.2.0, el agente corrió sobre todas las entidades del material, con una clave que no ve; no se ha probado sobre la documentación de una organización concreta.

**Esta página se lee sola.** Próspero funciona sin la otra agente de la familia. La familia —cómo se encuentran entre sí y con Rostrum— está en la [familia criterio-cmo](../../families/criterio-cmo/README.es.md).

---

## Qué es

| | |
|---|---|
| **A quién extiende** | A quien responde por la inversión de mercadeo —el CMO o el gerente de medios— y a quien arma el informe de resultados |
| **Sobre qué trabaja** | **El plan de mercadeo, la pauta y los resultados de una entidad, periodo a periodo** |
| **Qué mira** | El plan de mercadeo con el presupuesto y la meta de cada campaña, las facturas de pauta, la exportación de la plataforma y el informe de resultados |
| **Cadencia** | Cuando llega una factura, una exportación o un informe, y una vez por semana |
| **Instancias** | Una por entidad |

## Qué hace

**Lo que hace y hoy no se hace a mano: poner todo, no una muestra, al lado de su fuente.**

**Lo que puede responder:** qué campaña pasó su presupuesto, qué factura de pauta no tiene campaña ni orden, qué campaña no tiene meta ni indicador, cuál siguió después de su fin y qué resultado del informe no coincide con la plataforma.

<!-- cmo:comandos · generado por scripts/familias.py; no se edita a mano -->
### Los ocho comandos

> Se escriben con el prefijo del plugin: `/criterio-campaigns:` y autocompletar hace el resto. Es la única forma que resuelve en una sesión de Claude Code.

| Comando | Qué hace |
|---|---|
| `/criterio-campaigns:campaigns-setup` | La configuración, el inventario y las tablas reconocidas |
| `/criterio-campaigns:prospero` | Lo que necesites, en tus palabras: Próspero elige el comando que lo resuelve y lo corre |
| `/criterio-campaigns:campaigns-scan` | La ficha del periodo al día |
| `/criterio-campaigns:budget-check` | Qué campaña se pasó, siguió o no mide nada |
| `/criterio-campaigns:invoice-check` | Qué pauta se facturó sin campaña ni orden |
| `/criterio-campaigns:result-check` | Qué resultado del informe no se sostiene en la plataforma |
| `/criterio-campaigns:campaigns-wake` | Las campañas al día sin que nadie se acuerde |
| `/criterio-campaigns:share-findings` | Un resumen sin datos, solo si se dice que sí |
<!-- /cmo:comandos -->

`campaigns-setup` va primero porque los demás lo necesitan, y `campaigns-wake` es el que se le pone a un reloj.

<!-- cmo:skills · generado por scripts/familias.py; no se edita a mano -->
### Los tres skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se consultan como un manual.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `marketing-intake` | La estructura recomendada de la carpeta de mercadeo, qué va en cada carpeta y qué agente la usa | Copia de Lucía |
| `marketing-policy` | La política de publicidad en la configuración: las tolerancias, quién aprueba y lo que nunca se decide | Copia de Lucía |
| `result-record` | Cómo se lleva a la ficha cada resultado del informe de mercadeo: su campaña, su indicador, su valor y su corte, con la cita | Propio |
<!-- /cmo:skills -->

## Lo que cuesta hoy

<!-- cmo:cifras · generado por scripts/familias.py; no se edita a mano -->
<!-- /cmo:cifras -->

## Para qué sirve

`/criterio-campaigns:budget-check` pone cada caso al lado de su fuente. **Lo que falta se dice con su cita.**

### Y para qué no sirve

- **No aprueba un presupuesto ni juzga una campaña.** Dice qué se pasó y qué no se sostiene; la decisión es del área de mercadeo.
- **No decide cuál cifra es la correcta.** Dice cuál no coincide con la plataforma; lo decide quien firma el informe.
- **No se conecta a una plataforma de pauta ni de analítica.** Procesa sus exportaciones.

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura de la plataforma de IA**, no solo en tu equipo. Un plan de mercadeo o unas facturas de pauta pueden traer información confidencial: confirma que sea admisible bajo tu política antes de apuntarla a esa carpeta. Descargo completo en [DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

## Instalación y configuración

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-campaigns@criterio
/criterio-campaigns:campaigns-setup
```

### El primer resultado

`/criterio-campaigns:campaigns-setup` no te pide que ordenes nada antes de empezar. Mira la carpeta de mercadeo de la entidad, la compara con la [estructura recomendada](../../families/criterio-cmo/README.es.md#la-estructura-de-carpetas-recomendada), procesa la política de publicidad y hace las preguntas que ningún documento responde. En los primeros quince minutos deja ver el primer resultado.

### Cada cuánto corre

`/criterio-campaigns:campaigns-wake` es el comando que el reloj invoca: hace lo que toca, responde primero las preguntas que alguien dejó en Rostrum, y **si no toca nada no produce nada.** La decisión de qué toca es aritmética de fechas, y la toma el código:

```
python3 scripts/mercadeo.py despertar --config <archivo>
```

## Trabajo en equipo

| Con quién | Qué pasa |
|---|---|
| **Lucía** | Comparten la carpeta y la política de publicidad; cada uno escribe solo su ficha |
| **Rostrum** | Solo si la configuración lo dice (`publish_rostrum`): publica sus reportes, lo que vence y sus señales para quien no abre una carpeta, y le devuelve las preguntas que deja quien lo mira. **No escribe en el estado** |

## Pruebas

[`scripts/mercadeo.py`](scripts/mercadeo.py), con la librería estándar, hace todo lo que es cálculo: procesa cada tabla con su fila de origen, suma la pauta facturada de cada campaña contra su presupuesto y su tolerancia, compara cada factura con la fecha de fin y cada resultado con la plataforma al mismo corte, el mismo resultado cada vez. Vive en `criterio-claims` y se copia a Próspero; `scripts/sincronizar.py --check` falla si la copia se separa.

```
python3 scripts/mercadeo.py selftest
python3 tests/criterio-cmo/generar.py
python3 tests/criterio-cmo/evaluar.py
```

Qué se siembra en cada entidad y **qué no prueba el material**, en [`EVIDENCIA.md`](../../tests/criterio-cmo/EVIDENCIA.md). El diseño, con la entrada, el proceso y el reporte de cada comando, en el [diseño de la familia](../../families/criterio-cmo/DISENO.es.md).
