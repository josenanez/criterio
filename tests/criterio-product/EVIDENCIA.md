# Evidencia · criterio-product

Lo que Alba puede demostrar hoy, y lo que todavía no.

Nada aquí es real. El corpus se construyó desde cero, como exige
[CONTRIBUTING.md](../../CONTRIBUTING.md).

## Lo que se corre

**El resultado de la última corrida, generado**, en [`RESULTADOS.md`](RESULTADOS.md).
Esta página dice qué prueba cada pieza del material; esa dice cómo salió la última vez.

**Una sola puerta:** `python3 scripts/verificar.py` corre todo lo de abajo y lo de los otros
dos plugins. Lo que sigue es el detalle.

```
python3 tests/criterio-product/generar.py   10 documentos en 2 productos, 8 registros
python3 tests/criterio-product/grade.py     28 comprobaciones
python3 plugins/criterio-product/scripts/producto.py selftest   44 comprobaciones
python3 scripts/sincronizar.py --check      que las copias no se hayan separado
```

Con la librería estándar y sin instalar nada. La fecha de referencia es fija en
**2026-11-20** —la misma del corpus de `criterio-project`, para que los dos se puedan leer
juntos—: una prueba que use la fecha de hoy cambia de respuesta cada semana.

## Por qué un corpus propio

Los otros dos corpus miran proyectos: uno desde arriba, cuarenta a la vez; el otro desde
adentro, uno solo. **Este mira lo que hay antes de que exista el proyecto**, y ahí no hay
plan, ni línea base, ni presupuesto contra los que medir. Lo que hay es una definición, unas
entrevistas y un registro, y la comparación es otra: **la definición contra la evidencia de
demanda.**

| Producto | Qué planta |
|---|---|
| **PRD-QR** Pagos QR | Los diez hallazgos, cada uno con su documento: la cifra del caso de negocio que la métrica contradice (250.000 declaradas contra 180.000 medidas), un requerimiento **aceptado que nadie pidió**, uno **decidido y sin proyecto**, uno cuya traza apunta a un proyecto **cuya ficha dice otro producto**, un **área en vez de una persona**, un **supuesto de marzo sin verificar**, uno **propuesto en mayo que nadie decide**, evidencia de **hace diecisiete meses**, y un **descarte que no quedó en ningún acta** |
| **PRD-NOMINA** Dispersión de nómina | **Control negativo.** Tiene definición, entrevistas, métricas, cuatro documentos y tres requerimientos —uno de ellos propuesto—, y **no produce ni un hallazgo** |

## Lo que la corrida prueba

| Qué se comprobó | Resultado |
|---|---|
| Lo declarado contra lo medido, **con las dos fuentes y las dos fechas** | 28% de diferencia, el caso de negocio del 4 de marzo contra el tablero del 1 de septiembre. Sin las dos citas el hallazgo no sirve |
| Una diferencia pequeña **no se reporta** | Comercios activos: 1.200 declarados contra 1.150 medidos, 4,2%. Por debajo del umbral es imprecisión, y reportarla mata el informe |
| Un requerimiento **propuesto** no se le exige evidencia ni criterio | Nadie dijo todavía que se hace. Exigírselo convertiría el registro en un trámite, y el grader verifica que la señal **no** aparezca |
| Un **entregado sin traza** no es hallazgo | Es historia. Verificado en el selftest |
| La traza se confirma **contra la ficha del proyecto**, no contra el registro | PRY-101 dice `PRD-QR` y confirma; PRY-105 dice `PRD-ORIGINACION` y la señal nombra qué dice el otro lado |
| Sin la carpeta de fichas, **ninguna traza se da por confirmada** | Se declara así en la salida en vez de dar por bueno lo que no se verificó |
| Un **área no es un doliente** | `kind: area` produce la misma señal que no tener doliente. Son dos formas distintas de que nadie responda |
| Dos formas de no tener doliente en el mismo producto | REQ-003 tiene un área; el doliente de REQ-005 no sale de ningún documento. Dos hallazgos, no uno |
| La evidencia **más nueva** es la que decide si el conjunto envejeció | Diecisiete meses, contando desde el ticket de junio de 2025 y no desde el más viejo |
| **Meses de calendario**, no días divididos por 30 | Once meses no son doce, y el día exacto sí cumple. Tres comprobaciones en el selftest |
| Un **supuesto verificado** deja de contarse | Ya hizo su trabajo. El de marzo sin verificar sí cuenta, y el del switch no |
| El **conjunto exacto** de señales y **el conteo de cada una** | Una señal de más es un falso positivo, y el grader lo trata como falla |
| **El control negativo** | PRD-NOMINA: cero señales, con un propuesto de hace quince días y una diferencia declarado-medido del 4% que un agente ruidoso reportaría |
| Las **10 señales declaradas son las que se emiten** | El selftest lee su propio archivo: una señal nueva sin declarar rompe, y una declarada que nadie emite también |

**Las respuestas se escribieron leyendo los documentos, no calculándolas.** Si salieran de
las mismas fórmulas que el código, esto no probaría nada.

Y una regla que este corpus respeta, y que el de `criterio-portfolio` rompió una vez: **todo campo
de un registro de referencia cita un documento que de verdad lo dice.** Un registro que cita
un acta que nunca dijo eso es el error que este diseño existe para evitar, sentado dentro del
material de prueba.

## Lo que esta corrida NO cubre

Conviene decirlo antes de que alguien lo suponga.

- **La extracción nunca se ha corrido.** El corpus siembra los registros desde
  `expected/registros/`, así que la cadena documento → modelo → registro no se ha
  ejercitado. `grade.py --registros` existe para eso y todavía no se ha ejecutado. **Es la
  misma deuda que tienen los otros dos plugins**, y es la más importante de las tres.
- **Ningún comando se ha corrido con un agente de verdad.** Lo que se prueba aquí es la
  aritmética del registro y su contraste contra las fichas. Los siete comandos están
  escritos y verificados como estructura —existen, declaran, y no inventan skills— y eso no
  es lo mismo que haberlos ejercitado.
- **La síntesis de descubrimiento no se puede calificar con esto.** Convertir ocho
  entrevistas en temas con sus citas es trabajo del modelo, no del código, y un grader
  determinista no lo mide. Las entrevistas del corpus están escritas con el conteo explícito
  —«6 de 8»— precisamente para que el día que se califique, haya contra qué.
- **El barrido normativo no se prueba en ninguna parte.** Es el único skill de Alba cuya
  salida depende de conocimiento externo al repositorio, y su regla dura —*no dice si
  cumple*— no se puede verificar con una aserción. Lo que sí está escrito es el estado **«no
  tengo la norma a la vista»**, para que un vacío del agente no se lea como un cumplimiento.
- **La costura con el proyecto está construida y no corrida de punta a punta.**
  `/product-charter` crea la ficha y `/product-trace` la lee; el contraste está verificado
  con cuatro comprobaciones sobre fichas sintéticas. Lo que falta es que un agente de verdad
  cree la ficha y otro de verdad la escriba después.

## Reproducirlo

```
python3 tests/criterio-product/generar.py
python3 plugins/criterio-product/scripts/producto.py compute \
    --state tests/criterio-product/expected/registros/PRD-QR \
    --fichas tests/criterio-product/expected/fichas \
    --today 2026-11-20
python3 tests/criterio-product/grade.py
```
