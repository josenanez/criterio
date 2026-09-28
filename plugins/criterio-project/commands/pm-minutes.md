---
description: El acta de tu reunión a partir de la transcripción o las notas — cada acuerdo, compromiso y decisión atribuido a una persona y con su cita
argument-hint: "<ruta de la transcripción o de las notas>"
---

# /pm-minutes — El acta de la reunión

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.


## Lo primero, antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

El acta la escribe alguien de memoria dos días después, y por eso el acta no sirve como
evidencia de nada. Lo que se dijo ya se perdió: quién se comprometió, para cuándo, y qué
se decidió de verdad frente a lo que quedó en *«lo vemos la otra semana»*.

Este comando redacta el acta **sobre lo que la reunión dejó escrito** —una transcripción,
las notas de alguien, el chat de la videollamada— y deja cada cosa atribuida a una
persona, con la línea de donde salió.

Y hace algo que un acta escrita a mano casi nunca hace: **separa las cuatro cosas que en
una reunión suenan igual.**

| Lo que se dijo | Qué es | Dónde queda |
|---|---|---|
| *«Rubén entrega el plan el 9»* | Compromiso | Con doliente y fecha, al seguimiento |
| *«se acordó usar el switch interoperable»* | Decisión | Con quién decidió y qué se descartó |
| *«tecnología lo revisa»* | Intención sin doliente | Se registra como tal, **y no se le inventa dueño** |
| *«si el proveedor no certifica, esto se corre»* | Riesgo dicho al pasar | Al RAID, marcado como no registrado antes |

**La cuarta es la que este comando existe para no perder.** Un riesgo dicho al pasar en
una reunión y nunca registrado es el hallazgo que aparece tres meses después convertido en
incidencia, con la frase *«eso ya lo habíamos dicho»*.

## Invocación

```
/pm-minutes 30-reuniones/2026-11-27-transcripcion.txt
/pm-minutes ~/notas-reunion.md
/pm-minutes                       pide la ruta; no redacta de memoria
```

**Sin insumo no hay acta.** Si no hay transcripción ni notas, este comando no redacta
nada: pide el archivo y explica que un acta escrita sin fuente es exactamente el problema
que viene a resolver.

## Flujo

**1. Lee el insumo tal como está.** Aplica **document-intake** para los formatos. Una
transcripción automática viene con nombres mal escritos y frases cortadas: **normaliza los
nombres contra los que ya conoces del proyecto, y no arregles el contenido.**

**2. Separa las cuatro clases**, con la tabla de arriba. Aplica **commitment-tracking**
para los compromisos y **raid-taxonomy** para los riesgos, supuestos, incidencias y
dependencias.

Reglas que no se negocian:

- **Quién es una persona, no un área.** *«Tecnología lo revisa»* se registra como
  intención sin doliente. No le pongas el nombre del jefe del área: nadie se comprometió.
- **Un compromiso sin fecha va con `due_date: no_declarada`.** No se descarta y no se le
  inventa una fecha. Se cuenta aparte, siempre.
- **No conviertas en decisión lo que fue una opinión.** Una decisión tiene quién la tomó y
  qué se descartó. Si nadie decidió, el acta dice *«quedó sin decidir»*, que es información.
- **Lo que no se entendió se marca.** *«No quedó claro si la fecha es el 9 o el 19»* es una
  línea legítima del acta, y vale más que elegir una.

**3. Cruza contra lo que ya existe.** El mismo doliente prometiendo lo mismo con fecha
nueva **es un compromiso reprogramado, no uno nuevo**: la fecha anterior entra en su
historial y el contador sube. Y si la reunión cerró algo, **ciérralo contra el documento**,
no contra la frase: *«Rubén dice que lo entregó»* no cierra nada.

**4. Recalcula. No cuentes tú.**

```
python3 scripts/portafolio.py compute --state <estado> --config <archivo>
```

**5. Marca lo que la reunión contradice.** Si en la reunión cambió el patrocinador, la
fecha de cierre o el comité, eso **no es solo un acuerdo: es un campo de la ficha que la
documentación oficial todavía dice distinto.** Nómbralo, con las dos fuentes y las dos
fechas. Es el caso donde el gerente tiene razón y el acta de constitución está vieja.

## Salida

```markdown
# Acta — [proyecto] · [fecha]
**Asistieron:** [nombres] · **Fuente:** [archivo] · **Ausentes con tema en agenda:** [nombres]

## Compromisos
| Quién | Qué | Para cuándo | |
[Marca los reprogramados con las veces. Los sin fecha van en su propia sección.]

### Sin fecha
| Quién | Qué |
[No pueden estar vencidos, y por eso mismo desaparecen de los informes. Aquí no.]

## Decisiones
| Qué se decidió | Quién | Qué se descartó |

## Quedó sin decidir
| Qué | Por qué | Quién tiene la facultad |

## Intenciones sin doliente
| Qué se dijo | Quién lo dijo |
[No son compromisos. Se registran para que alguien les ponga dueño, o no.]

## Dicho al pasar y no registrado
| Qué | Quién lo dijo | Categoría | Ya estaba en el RAID |
[El riesgo nombrado en una frase y nunca escrito en ninguna parte.]

## Cerrado en esta reunión
| Qué | Con qué documento |
[Sin documento no se cierra. Si no hay ninguno, se omite la sección.]

## Lo que esta reunión contradice
| Campo | Dijo la reunión | Dice el expediente | Fuente y fecha de cada uno |

## Sin resolver de la transcripción
[Lo que no se entendió. Una línea cada uno, con la cita.]
```

## Lo que este comando no hace

- **No asiste a la reunión.** Trabaja sobre lo que la reunión deja escrito.
- **No reparte tareas.** Registra lo que alguien se comprometió a hacer; asignarle algo a
  alguien es una conversación con esa persona.
- **No juzga lo que se decidió.** Deja la decisión con su dueño y con lo que se descartó,
  que es lo que sirve dentro de seis meses.
- **No le pone doliente a una intención.** Ver el paso 2.
- **No mejora la transcripción.** Un nombre mal escrito se normaliza; una frase confusa se
  cita confusa y se marca.

## Después

Ofrece `/pm-commitments` para ver el seguimiento completo con lo que acaba de entrar, y
`/pm-publish` si algún campo de la ficha cambió — sobre todo si el acta contradice al
expediente, porque ahí es donde la PMO tiene que enterarse.

**El acta sale en la conversación, y la guardas tú.** Samuel no la escribe en tu carpeta de
reuniones, y no es un descuido: el único archivo que este agente pone en la documentación
de un proyecto es `ficha-pm.json`, y solo cuando corres `/pm-publish`. Un acta con tu
nombre que apareció ahí sin que la hayas leído es precisamente lo que nadie quiere
encontrarse — **el acta es tuya antes de ser evidencia de nadie.**

## Deja la corrida registrada

Lo último, siempre:

```
python3 scripts/portafolio.py corrida --state <estado> --what sweep \
    --nota "qué compromisos salieron de la reunión"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` cuenta lo que hay que contar y deja `<estado>/corridas/<fecha>-sweep.md`: qué encontró por señal, cuánto tardó, y cuántos hallazgos más o menos que la vez anterior.
