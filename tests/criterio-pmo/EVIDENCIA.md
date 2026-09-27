# Evidencia · criterio-pmo

Última corrida: **25 de septiembre de 2026**, sobre material sintético. Fecha de corte de
todas las comprobaciones: **2026-09-30**, fija a propósito.

**Esto no es una corrida real.** Es material construido para contener las fallas que contiene
una carpeta real, con las respuestas escritas a mano. Las cifras de corridas sobre
documentación real no existen todavía, y hasta que existan no se inventan.

## Lo que se corre, y qué verifica cada cosa

**El resultado de la última corrida, generado**, en [`RESULTADOS.md`](RESULTADOS.md).
Esta página dice qué prueba cada pieza del material; esa dice cómo salió la última vez.

**Una sola puerta:** `python3 scripts/verificar.py` corre todo lo de abajo y lo de
`criterio-pm`, y dice qué prueba cada cosa. Lo que sigue es el detalle.

```
python3 plugins/criterio-pmo/scripts/pmo.py selftest       42 resultados · la aritmética
python3 plugins/criterio-pmo/scripts/texto.py --selftest   12 resultados · la conversión
python3 plugins/criterio-pmo/scripts/informe.py --selftest 15 resultados · el informe
python3 plugins/criterio-pmo/scripts/servidor.py --selftest 30 resultados · Rostrum
python3 tests/criterio-pmo/generar.py                      28 documentos en 6 proyectos
python3 tests/criterio-pmo/grade.py                        69 comprobaciones
python3 tests/coherencia.py                                documentación contra código
python3 scripts/validate_plugins.py                        estructura del market
```

Los ocho en verde. Sin dependencias: librería estándar de Python 3.10 o superior.

## El portafolio sintético

Seis proyectos de un banco, con la estructura de carpetas de una PMO real —
`00-gobierno`, `10-plan`, `20-seguimiento`, `30-reuniones` — y nombres de archivo con fecha.

| Proyecto | Qué planta |
|---|---|
| **PRY-001** Originación digital | El caso central: declara verde en agosto y la evidencia no lo sostiene. Hito vencido sin evidencia, 19 días de silencio, 95,2% comprometido, patrocinador contradicho entre el acta y la minuta, un compromiso prometido tres veces, y una replanificación de 61 días contra 60 autorizados |
| **PRY-002** Core de depósitos | Declara amarillo. Tres controles: el amarillo **no** dispara la alerta de brecha; un hito cuya fecha de línea base pasó pero cuya fecha vigente es de diciembre **no** es un hito vencido; y un compromiso sin fecha que hasta hace poco desaparecía del informe |
| **PRY-003** Migración a nube | Proveedores: un entregable vencido sin evidencia, dos dados por entregados sin acta de recibo, y 620 millones facturados contra 580 de entregables aceptados |
| **PRY-004** Open Banking | El caso más común en una PMO real: sin plan aprobado, sin presupuesto, cinco meses en silencio, y aun así reportado en verde |
| **PRY-005** Débito contactless | **Control negativo.** Todo en orden. Cero alertas. Declara el mismo producto que PRY-002, para que el portafolio tenga un producto construido por dos proyectos que reportan a comités distintos |
| **PRY-006** SARLAFT | Un cambio aprobado con impacto escrito en «tres meses», y un presupuesto aprobado que nunca incorporó los 180 millones que el comité autorizó |

## Lo que la corrida prueba

**Las 17 señales se disparan cuando deben.** Cada una tiene al menos un caso plantado, y el
grader compara el conjunto exacto: falla igual si falta una señal o si aparece una que no
está declarada. Eso ya pasó — al agregar `commitment_rescheduled`, el grader falló porque la
señal apareció sin estar declarada en las respuestas conocidas.

**El control negativo pasa.** PRY-005 produce cero alertas. Es la comprobación más
importante del conjunto: un agente que alerta sobre un proyecto sano es un generador de
ruido, y en un mes se silencia.

**El amarillo no se trata como el verde.** PRY-002 tiene señales y no dispara
`declared_vs_evidence`. Quien ya reportó problema no está escondiendo nada.

**No se inventan números donde no se pueden leer.** «Tres meses» de PRY-006 queda en
`time_impact_unreadable` en vez de convertirse en 90 días.

**El umbral es un umbral.** La proyección de PRY-001 se pasa del aprobado un 3,2% y no
dispara `variance_cost`; la de PRY-006 se pasa 17,3% y sí.

**El índice de documentos distingue los cuatro casos.** Una prueba de mutación sobre una copia
del corpus: un cambio real, un guardado que solo movió espacios, un renombrado y un borrado.
El reguardado **no** entra en lo que hay que releer, el renombrado se detecta por contenido con
su ruta vieja y su nueva, y las citas que dejaron de resolver salen con su proyecto y su campo.
Es el caso que paga el diseño.

**Los formatos de Office se leen sin instalar nada.** El selftest de `texto.py` construye un
`.docx`, un `.xlsx` con cadenas compartidas y un `.pptx` mínimos y los vuelve a leer, y
verifica que un `.msg` se declare ilegible **con la razón y con cómo arreglarlo**.

**La documentación y el código dicen lo mismo.** Los nombres técnicos citados en la
documentación existen en el código, todo umbral nombrado existe, los 15 comandos están
listados en el README del plugin, y el número de resultados del selftest declarado en la
documentación coincide con el real — eso último lo atrapó el verificador antes que yo.

## Lo que esta corrida no cubre, y cómo se cubre

**La extracción de campos.** Todo lo anterior corre sobre las fichas de referencia de
`expected/fichas/`, escritas a mano. Que un modelo leyendo `input/` produzca esas mismas
fichas se califica con el segundo modo del grader:

```
python3 tests/criterio-pmo/grade.py --fichas <las que produjo la corrida>
```

Compara campo por campo y reporta tres cosas distintas: un valor equivocado, un campo
inventado que la referencia no tiene, y un valor sin cita.

**Cómo se cubre: con pruebas progresivas.** No es un pendiente de construcción — es un
programa. Corpus cada vez más parecidos a una carpeta real —más proyectos, más formatos,
convenciones peores— y el plugin corriendo como lo correría alguien de afuera, instalándolo
desde cero. Cada escalón deja su resultado aquí, y el escalón que falla dice qué hay que
arreglar antes de subir el siguiente.

Este documento registra **el escalón donde vamos**, no una aspiración. Hoy es el primero:
seis proyectos, formatos de texto, convención de nombres respetada.

## El informe, sobre el mismo portafolio

`informe.py` corrido sobre las fichas de referencia al 2026-09-30 produce **8 páginas**:
las dos vistas y una por proyecto. Los números que imprime no son suyos —los toma de
`pmo.py compute`—, así que lo que esta corrida prueba es otra cosa: **que lo que sale se
pueda leer sin conocer el esquema.**

| Qué se comprobó | Resultado |
|---|---|
| Ninguna ruta de la ficha impresa en crudo | 14 campos vacíos en 5 proyectos, los 14 en castellano: *«la evidencia del hito Motor de decisión certificado»*, *«hasta dónde decide el gerente sin subir al comité»* |
| Concordancia de número | `1 día`, no `1 días`. El selftest lo fija en singular, plural y negativo |
| Cifras con la coma del lector y sin cola | `95,2%`, no `95.20%`. `78%`, no `78.0%` |
| Ningún color del modo oscuro | Cero coincidencias de los siete tokens oscuros de la paleta en las 8 páginas |
| La vista de decisiones no es la interna recortada | 6 puntos en 4 de 6 proyectos, contra 26 alertas de 16 señales distintas en 5 proyectos de la interna. Lo que no excede la facultad del gerente no sube |
| El control negativo también en el informe | PRY-005: *«ninguna»* en las señales, y ningún punto de decisión |

**Cómo se encontraron los errores que tenía.** Se renderizaron las páginas en un navegador
y se miraron. Cuatro de los seis defectos —`1 días`, `6 punto(s)`, `78.0%`, y las rutas
`plan.milestones[1].evidence` impresas tal cual— pasan todos los tests de aritmética sin
problema, porque no son errores de cálculo. **Un informe correcto que se lee como un
volcado de datos es un informe que el nivel C no va a abrir dos veces.**

Los dos primeros ya no pueden volver: `informe.py --selftest` los fija. El tercero también.
La cuarta clase —una señal nueva que salga con su nombre en inglés— la fija
`tests/coherencia.py`, que importa la tabla de nombres y la compara con las señales que
`pmo.py` calcula.

## El portal: proyectos, productos y la ida y vuelta

El corpus tenía un defecto que solo se vio al construir la vista de producto: **las
fichas de referencia declaraban `identity.product` con una cita a un acta que no lo
decía en ninguna parte.** Es exactamente el error que todo este diseño existe para
impedir —«no adivina»— sentado dentro del material de prueba. Una extracción correcta
habría devuelto `not_found` y el grader la habría marcado mal.

Corregido: el producto entra en las actas, que es donde una PMO lo declara, y la ficha
lo cita de ahí.

Con eso el portafolio sintético queda con el caso que la vista de producto existe para
atrapar:

| Qué se plantó | Qué prueba |
|---|---|
| **Cuenta transaccional**, construida por PRY-002 y PRY-005 | Un producto con dos proyectos. PRY-002 reporta al Comité de Tecnología y PRY-005 al de Medios de Pago: **ningún comité lo ve completo** |
| Patrocinadores distintos en esos dos | No hay una sola respuesta a quién se le escala el producto |
| PRY-005 limpio y PRY-002 con desviación | **El proyecto sano no salva al producto.** Su estado es el del peor, no el promedio |
| **Crédito de consumo**, un solo proyecto | El caso simple: un comité, un patrocinador, y el informe de producto dice que no hay hallazgo propio. Que no haya hallazgo es un resultado |
| PRY-003, PRY-004 y PRY-006 sin producto | Tres proyectos que no declaran producto. No es un error de ellos, y el portal lo reporta sin tratarlo como falta |

**Un error que la aritmética no habría detectado.** El listado de productos mostraba
«Crédito de consumo · verde» junto a «10 señales», porque tomaba el semáforo declarado
del peor de sus proyectos. Correcto como cálculo, y exactamente la mentira que este
portal existe para destapar. Ahora el semáforo va con la marca de que la evidencia no
lo sostiene, y en qué proyecto.

**Y otro que solo se ve mirando.** La portada del servidor ponía un enlace dentro de
otro enlace. No es HTML válido: el navegador cierra la tarjeta donde empieza el de
adentro, y la primera sección salía partida en dos cajas con media frase suelta
debajo. Pasa cualquier prueba que mire el texto y ninguna que mire la página.

Las doce páginas de una corrida sobre el corpus: las cuatro del portal —informe PMO,
decisiones, listado de proyectos, listado de productos—, seis de proyecto y dos de
producto.

## Rostrum, y la frontera que no cruza

Un servidor que expone un portafolio de proyectos tiene dos formas de fallar que no se
ven mirando la pantalla: **servir un archivo que no es del informe**, y **tener un
camino de escritura hacia la ficha**. Las dos se comprueban.

| Qué se comprobó | Resultado |
|---|---|
| Las seis rutas declaradas responden | `RUTAS` es un dato del programa, no un `if` implícito. El selftest recorre la tabla y exige 200 en cada una: una ruta declarada y no servida sale en el README como una promesa que devuelve 404 |
| No se sale de la carpeta del informe | `/p/../../secreto`, `/p//etc/hostname` y un archivo vecino que no es del informe: 404 los tres. Los nombres se filtran por forma **y** la ruta resuelta se comprueba contra la raíz |
| No hay camino de escritura hacia la ficha | Se manda una petición y se compara la ficha byte a byte antes y después. Idéntica. Lo único que el programa escribe es el archivo de la petición, en `<estado>/peticiones/` |
| Una petición enorme se rechaza y no entra | 413, y la cola sigue con las mismas que tenía |
| Lo que escribe alguien se escapa | `<script>` en el campo del nombre no sale como etiqueta en la confirmación |
| El POST solo existe en su ruta | `POST /interna` es 404 |
| La corrida completa, de punta a punta | Informe sobre las fichas de referencia → servidor → petición de un patrocinador sobre PRY-003 → `pmo.py due` responde `["requests"]`, sin cadencia configurada. La ficha, intacta |

**La cola es la única cosa que rompe el silencio sin ser aritmética de fechas.** Eso es
deliberado y se comprueba en `pmo.py selftest`: una petición abierta hace que `due` deje
de estar callado, una respondida lo devuelve al silencio, y la ya respondida nunca
cuenta.

## Límites conocidos

**Cerrados desde la corrida anterior**

| Límite | Cómo se cerró |
|---|---|
| Una factura contra un entregable que no empezó pasaba desapercibida | `amount` por entregable, y la señal `vendor_invoiced_over_accepted`. Es la pregunta que Finanzas hace en la minuta de PRY-003 |
| Un compromiso sin fecha desaparecía del informe | `commitment_undated`. No puede estar vencido, y por eso mismo se cuenta aparte |
| El compromiso reprogramado tres veces no se detectaba | `reschedules` en el esquema y `commitment_rescheduled` en el cálculo |
| El hash de documentos solo existía en markdown | `pmo.py index`, con dos etapas y verificación de citas |
| No se podía leer un `.docx`, un `.xlsx` ni un `.pptx` | `texto.py`, sin dependencias: son ZIP con XML adentro |

**Abiertos**

**1 · Un cambio aprobado con impacto ilegible queda fuera del control de replanificación.**
Si el impacto está escrito en meses, no suma a `approved_time_days` ni entra en
`approved_without_new_baseline`. Solo aparece en la lista de ilegibles. Cada paso es correcto
y el resultado es que un cambio real se pierde del control. **La mitigación es preguntar, no
convertir**: un mes no tiene un número fijo de días.

**2 · Siete claves de configuración que nadie lee.** `paths.standard`,
`cycle.committee_next`, `cycle.report_lead_days`, `cycle.daily_sweep`, `report.language`,
`report.recipients` y `confirmation.fields_per_run`. Son el zócalo de la cadencia, las
notificaciones y el presupuesto de preguntas: está puesto y vacío. El disparador ya existe
—el índice de documentos— y falta quién lo invoca sin que alguien abra una sesión.

**3 · Un PDF escaneado sin capa de texto no se lee.** `pdftotext` devuelve vacío y el
documento se declara ilegible, que es la conducta correcta y no la útil. Con OCR se vuelve
legible y deja de ser determinístico: el texto pasa a ser una lectura probable, no el
contenido. Si entra, entra marcado como tal.

**4 · `.msg`, `.doc`, `.xls` y `.mpp` no se leen.** Cada uno se declara con la razón y con
cómo guardarlo para que sí. En una PMO real hay carpetas enteras de `.msg`.

**5 · `stated_on` sigue sin leerse.** El compromiso reprogramado ya se detecta por
`reschedules`; el campo queda para cuando haga falta la fecha en que se dijo cada cosa y no
solo la que se prometió.

**6 · El informe no existe en la forma configurada.** `report.format: html` está declarado y
nada produce HTML. Es la capacidad siguiente: informe estructurado con el diseño base del
producto, servido por el servidor, y en PDF para quien lo quiera adjunto.

## Reproducirlo

```
git clone https://github.com/josenanez-company/criterio.git
cd criterio
python3 plugins/criterio-pmo/scripts/pmo.py selftest
python3 plugins/criterio-pmo/scripts/texto.py --selftest
python3 tests/criterio-pmo/generar.py
python3 tests/criterio-pmo/grade.py
python3 tests/coherencia.py
```
