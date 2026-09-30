---
description: El informe de avance de la semana, completo salvo una línea — el estado lo declaras tú, y Samuel te muestra contra qué
argument-hint: "[fecha de corte] o vacío para hoy"
---

# /pm-report — El informe semanal

> **Dónde está la configuración:** `.criterio/proyecto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo proyecto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-project:pm-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.


## Lo primero, antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

El informe de avance se escribe el jueves en la noche, se arma copiando el de la semana
pasada, y cambia tres cifras. Cuesta dos horas y lo lee gente que no puede distinguir qué
cambió.

Samuel lo arma completo **salvo una línea: el estado.** Esa la escribes tú, y el sistema
está construido para que no pueda escribirla él.

**Y es un informe de proyecto, no de comité.** La diferencia no es de longitud: un comité
decide lo que excede la autoridad del gerente, así que su material es un paquete de
decisiones. Un informe semanal de proyecto le habla a quien sigue el proyecto, y su unidad
es **qué cambió desde la semana pasada**. Un informe que vuelve a contar lo mismo con una
fecha nueva no se lee dos veces.

## Invocación

```
/pm-report                    corte a hoy
/pm-report 2026-11-27         corte a una fecha
```

## Flujo

**1. Compara contra la corrida anterior. Es el eje del informe.**

```
python3 scripts/portafolio.py snapshot --state <estado>
python3 scripts/portafolio.py diff     --state <estado>
python3 scripts/portafolio.py compute  --state <estado> --config <archivo>
```

Lo que cambió va arriba, con qué era y qué es. Lo que no cambió y está bien va al final en
una línea. **Lo que no cambió y está mal va arriba también**, con los días que lleva así:
una desviación que sigue igual cuatro semanas no es estabilidad.

**2. Pide la declaración. Una pregunta, con lo que ya tienes a la vista.**

Muéstrale las señales abiertas y **después** pregunta qué estado declara y con qué avance.
Nunca al revés, y nunca con una propuesta: **si Samuel sugiere el estado, la declaración
deja de ser información independiente y el hallazgo de más valor del sistema desaparece.**

Si el gerente no declara, el informe sale con esa línea en blanco y lo dice. Un informe sin
declaración es incómodo a propósito.

**3. Contrasta la declaración contra la evidencia, y no la maquilles.**

El cálculo ya lo hizo: `declared.unaccounted_signals` trae las señales que el semáforo
declarado no explica, y `declared_vs_evidence` aparece cuando se declara verde y hay
evidencia que ese verde no cubre. **Cítala, no la vuelvas a juzgar a ojo.** Si la
declaración tiene más de un mes, `declaration_stale` lo dice: un verde de hace seis semanas
no es un verde.

**4. Mide contra el plan.** Aplica **baseline-variance**: desviación contra la línea base
original y contra la vigente, con el número de replanificaciones. Las dos, siempre. Solo
contra la vigente cualquier atraso se ve pequeño, porque la vigente se movió con él.

**5. Las cuatro cifras y el disponible real.** Aprobado, comprometido, ejecutado y
proyectado. **El disponible real no es aprobado menos ejecutado:** es aprobado menos
comprometido, y esa diferencia es la que sorprende en el comité.

**6. Lo abierto, ordenado por lo que necesita a alguien.** Compromisos reprogramados
primero, después vencidos sin evidencia, después el RAID sin movimiento, después los
entregables de proveedor vencidos o aceptados sin documento.

**7. Cierra con lo que no se sabe.** Los campos en `not_found` que importan para juzgar
este proyecto, y **los días de silencio**: desde el último documento y desde la última
reunión. Un proyecto que reporta verde y lleva cinco semanas sin un documento es el caso
que este informe existe para mostrar.

## Salida

```markdown
# [Proyecto] — semana del [fecha] al [fecha]

**Declara el gerente:** [estado] · [avance]% · al [fecha]
**Sustento documental:** [sustentado | sin sustento | contradicho]
**Lo que el semáforo no explica:** [señales, o «nada»]

## Qué cambió esta semana
| Qué | Estaba | Está | |
[Lo nuevo, lo cerrado y lo que se movió. Si no cambió nada, se dice en una línea.]

## Lo que sigue igual y sigue mal
| Qué | Desde | Días así |

## Contra el plan
| | Línea base original | Vigente | Desviación |
| Fecha de cierre | | | |
| Presupuesto | | | |

Replanificaciones: [N] — [fechas y motivos declarados]

### Hitos de las próximas cuatro semanas
| Hito | Base | Vigente | Evidencia |

## Las cifras
| Aprobado | Comprometido | Ejecutado | Proyectado | Disponible real |

## Abierto
**Reprogramados:** [quién, qué, cuántas veces]
**Vencidos sin evidencia:** [quién, qué, desde cuándo]
**RAID sin movimiento:** [qué, días]
**Proveedor:** [vencidos, aceptados sin documento, facturado sin entrega]

## Lo que necesito de alguien
[Una línea por cosa, con nombre. Lo que excede la autoridad del gerente va marcado, y es
material de comité, no de este informe.]

## Lo que no se sabe
**Sin dato:** [campos que importan para juzgar este proyecto]
**Silencio:** último documento hace [N] días · última reunión hace [N] días
```

**Pie obligatorio:** de qué ficha sale, de cuándo es, cuántos campos van sin dato, y el
enlace a los términos. Un informe sin eso es una afirmación sin origen.

## Lo que este comando no hace

- **No declara el estado.** Es la sexta invariante del diseño, no una recomendación: si el
  agente declara, la comparación compara al sistema consigo mismo.
- **No sugiere qué declarar.** Ver el paso 2. Es la restricción incómoda del comando, y es
  la que lo hace valer algo.
- **No suaviza.** Un rojo que la evidencia sostiene sale rojo, y una declaración que la
  evidencia contradice sale con las dos cosas al lado.
- **No se lo manda a nadie.** Produce el informe; a quién se le envía y cuándo es del
  gerente.
- **No reemplaza el material de comité.** Eso es un paquete de decisiones y tiene otra
  forma y otra cadencia.

## Después

Si hay algo reprogramado tres veces o una desviación por encima del umbral, ofrece armar el
punto de comité con la decisión formulada. Si la declaración quedó contradicha por la
evidencia, ofrece `/pm-publish`: **eso es exactamente lo que la PMO tiene que poder leer**,
y es mejor que lo lea de tu ficha que se lo encuentre por su cuenta.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/portafolio.py corrida --state <estado> --what report \
    --salida <estado>/corridas/salida-report.md \
    --nota "qué cambió, qué hay que mirar"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` cuenta lo que hay que contar y deja `<estado>/corridas/<fecha>-report.md`: qué encontró por señal, cuánto tardó, y cuántos hallazgos más o menos que la vez anterior.
