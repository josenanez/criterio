---
description: Pídeselo a Clara (Contralor) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cfo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /clara — Pídeselo a Clara

Quien trabaja con Clara no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Clara sabe hacer —los grupos de la tabla de abajo,
con sus etiquetas y sin nombres de comando— y pregunta qué necesita la persona.

**2. Con argumento, elige de la tabla el comando que lo resuelve:**

- **Uno claro:** di en una línea cuál vas a correr y por qué —«Esto es *<etiqueta>*: corro
  `/<comando>`»— y córrelo con la herramienta que corre los comandos, pasándole como argumento lo que
  del pedido le sirva. Si no puedes invocarlo, dile a la persona exactamente qué escribir.
- **Dos posibles:** pregunta cuál, con las dos etiquetas. No adivines.
- **Es de otro agente de la familia:** dilo en una línea y da su entrada, de la segunda tabla.
- **Ninguno:** dilo en una línea. No improvises el trabajo con lo que hay en la conversación.

**Un comando a la vez, sin subagentes en paralelo.**

**3. Lo que el pedido no dice no se inventa.** Si el comando necesita un dato que el pedido no trae —un
periodo, un proyecto, una ruta—, lo pide el propio comando.

**4. Si el comando elegido responde que falta la configuración**, ofrece
`/criterio-finance:finance-setup` y no corras nada más.

## Lo que Clara sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-finance:finance-setup` | Deja a Clara lista sobre una entidad — mira la carpeta, hace las preguntas que ningún documento responde y muestra el primer estado del cierre |
| Arranque y ritmo · Compartir hallazgos | `/criterio-finance:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |
| Contralor · Qué cambió en el cierre | `/criterio-finance:close-scan` | Procesa lo que cambió en el periodo, actualiza la ficha del cierre y dice qué señales nuevas aparecieron |
| Contralor · Estado del cierre | `/criterio-finance:close-status` | El estado del cierre: lo declarado contra lo evidenciado, tarea por tarea del checklist, con la ruta crítica |
| Contralor · Conciliación bancaria | `/criterio-finance:bank-reconcile` | La conciliación de cada cuenta bancaria del periodo, con sus partidas abiertas por antigüedad y la diferencia sin explicar |
| Contralor · Conciliación de cuentas | `/criterio-finance:account-reconcile` | Cada cuenta contra su auxiliar —cartera, proveedores, inventarios, activos fijos, intercompañías— con la diferencia y la antigüedad de sus partidas |
| Contralor · Cuadre del balance y el mayor | `/criterio-finance:ledger-check` | El cuadre del balance de comprobación y del libro mayor, cuenta por cuenta, y los saldos contrarios a su naturaleza |
| Contralor · Facturas electrónicas | `/criterio-finance:einvoice-check` | Todas las facturas electrónicas del periodo contra la contabilidad —no una muestra—: sin registro, registros sin factura, diferencias y duplicados |
| Contralor · Paquete del auditor | `/criterio-finance:audit-pack` | El índice del paquete del auditor: cada requerimiento con su respuesta, su soporte y su estado; no mueve ni copia archivos |
| Contralor · Qué toca hoy | `/criterio-finance:finance-wake` | Lo que toca hoy en el cierre según su ventana — a diario mientras dura, semanal fuera de ella — y si no toca nada, se calla |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Tomás · el presupuesto | `/criterio-budget:tomas` |
| Áurea · la tesorería | `/criterio-treasury:aurea` |
