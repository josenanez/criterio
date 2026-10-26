<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-cfo-oscuro.svg"><img src="../../docs/img/marca/es/criterio-cfo-claro.svg" alt="Criterio CFO · La función financiera" height="48"></picture>

# Áurea · Tesorería

<img src="../../docs/img/es/robot-aurea.gif" alt="Áurea" width="220" align="right">

**Áurea pone la caja, los pagos y la deuda al lado de su política.** Tú respondes por la caja de
la entidad. Ella llega con cada cuenta contra su mínimo y su proyección, cada pago programado
contra quién puede aprobarlo, la exposición cambiaria contra su límite y cada covenant calculado
desde el balance que cierra Clara.

[English](README.md) · `criterio-treasury` · Apache 2.0 · Una instancia por entidad

**Estado: los seis comandos construidos**, su skill y el motor de cálculo, probado con su
autoprueba. Su ronda con el agente sobre el material de prueba es el siguiente paso; nada se ha
corrido aún sobre los documentos de una organización. Nada se anuncia como terminado hasta que
pasen los [criterios de aceptación](ACCEPTANCE.md).

**Es el tercer agente de la oficina del CFO** ([ADR 0016](../../docs/decisions/0016-tesoreria-tercer-agente-cfo.md)):
comparte con Clara el motor, la carpeta y el periodo. La familia está en
[criterio-cfo](../../families/criterio-cfo/README.es.md).

---

## Qué es

La tercera capacidad de la oficina del CFO: la tesorería. O*NET reúne a tesoreros y contralores en
una misma ocupación (11-3031.01), y por eso Áurea vive en la familia CFO y no aparte.

## Qué hace

<!-- cfo:comandos · generado por scripts/familias.py; no se edita a mano -->
### Los seis comandos

> Se escriben con el prefijo del plugin: `/criterio-treasury:` y autocompletar hace el resto. Es la única forma que resuelve en una sesión de Claude Code.

| Comando | Qué hace |
|---|---|
| `/criterio-treasury:treasury-setup` | La configuración, el inventario y la primera posición de caja |
| `/criterio-treasury:treasury-scan` | La tesorería al día, con lo que cambió y las señales nuevas |
| `/criterio-treasury:cash-position` | La caja de cada cuenta contra su mínimo y su proyección, y la exposición cambiaria |
| `/criterio-treasury:payment-check` | Cada pago programado contra quién puede aprobarlo |
| `/criterio-treasury:debt-watch` | La deuda contra su vencimiento y lo que exige su contrato |
| `/criterio-treasury:treasury-wake` | Lo que toca hoy en la tesorería; si no toca nada, se calla |
<!-- /cfo:comandos -->

<!-- cfo:skills · generado por scripts/familias.py; no se edita a mano -->
### Los dos skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se consultan como un manual.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `finance-intake` | Qué documentos procesa la familia, dónde va cada uno, qué procesa el motor directamente y qué extrae el agente a la ficha | Copia de Clara · también en Tomás |
| `treasury-control` | La tesorería contra su política: la caja contra su mínimo y su proyección, los pagos contra sus aprobadores y la matriz de firmas, la exposición cambiaria y los covenants calculados desde el balance | Propio |
<!-- /cfo:skills -->

## Para qué sirve

Para que la tesorería llegue al comité y al banco con la caja, los pagos y la deuda contrastados
contra su política, sin armarlo a mano. Lo que procesa:

| Documento | Dónde |
|---|---|
| El extracto de cada cuenta, el mismo que concilia Clara | `<AAAA-MM>/20-bancos/<cuenta>/` |
| El programa de pagos, con quién aprobó cada uno, y el flujo de caja proyectado | `<AAAA-MM>/60-tesoreria/` |
| La política de tesorería, la matriz de firmas, el registro de la deuda y los covenants | `00-referencia/` |
| El balance de comprobación del periodo, para los covenants | `<AAAA-MM>/10-contabilidad/` |

**La política es de la organización.** Áurea no la propone como norma: sin política no hay
mínimo de caja ni aprobadores por monto, y el reporte lo dice.

### Lo que nunca hace

Áurea **nunca** mueve dinero, hace un pago, entra a un portal bancario, negocia con un banco ni
recomienda una inversión, un financiamiento o una cobertura. Procesa las exportaciones que la
tesorería ya tiene, y la decisión la toma siempre una persona.

## Instalación y configuración

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-treasury@criterio
```

Después, `/criterio-treasury:treasury-setup`. **El primer resultado, en los primeros quince minutos:** la posición de caja de cada cuenta contra su mínimo y su proyección, sacada de sus propios extractos. Su reporte no se publica en Rostrum por omisión: trae
saldos y cuentas.

## Trabajo en equipo

Áurea no le habla a Clara ni a Tomás: toma los extractos que Clara concilia y el balance que ella
cierra, de la misma carpeta, y escribe su propia ficha en `tesoreria/` del estado compartido.
Rostrum muestra lo que vence de su registro de la deuda; su reporte con saldos se publica solo si la
configuración lo dice.

## Pruebas

El motor de Áurea pasa su autoprueba sobre una entidad mínima con todo mal: caja bajo el mínimo,
desviación contra la proyección, exposición cambiaria, pagos sin aprobación, firmantes sin facultad,
vencimientos y covenants. Los resultados, en [`tests/criterio-treasury/RESULTADOS.md`](../../tests/criterio-treasury/RESULTADOS.md),
y lo que falta para darla por probada, en los [criterios de aceptación](ACCEPTANCE.md).

