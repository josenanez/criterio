# Evidencia · criterio-pmo

Corrida del **25 de septiembre de 2026** sobre material sintético. Fecha de corte de
todas las comprobaciones: **2026-09-30**, fija a propósito.

**Esto no es una corrida real.** Es material construido para contener las fallas que
contiene una carpeta real, con las respuestas escritas a mano. Las cifras de corridas
sobre documentación real no existen todavía, y hasta que existan no se inventan.

## Lo que se corrió

```
python3 plugins/criterio-pmo/scripts/pmo.py selftest    24 resultados conocidos · sin errores
python3 tests/criterio-pmo/generar.py                   26 documentos en 6 proyectos
python3 tests/criterio-pmo/grade.py                     49 comprobaciones · sin errores
python3 tests/coherencia.py                             coherente
python3 scripts/validate_plugins.py                     clean
```

## El portafolio sintético

Seis proyectos de un banco, con la estructura de carpetas de una PMO real —
`00-gobierno`, `10-plan`, `20-seguimiento`, `30-reuniones` — y nombres de archivo con
fecha, que es la convención que el plugin espera.

| Proyecto | Qué planta |
|---|---|
| **PRY-001** Originación digital | El caso central: declara verde en agosto y la evidencia no lo sostiene. Hito vencido sin evidencia, 19 días de silencio, 95,2% comprometido, patrocinador contradicho entre el acta y la minuta de septiembre, compromiso reprogramado tres veces, y una replanificación de 61 días contra 60 autorizados |
| **PRY-002** Core de depósitos | Declara amarillo. Dos controles: el amarillo **no** dispara la alerta de brecha, y un hito cuya fecha de línea base ya pasó pero cuya fecha vigente es de diciembre **no** es un hito vencido |
| **PRY-003** Migración a nube | Proveedores: un entregable vencido sin evidencia, dos dados por entregados sin acta de recibo, y facturación por 620 millones |
| **PRY-004** Open Banking | El caso más común en una PMO real: sin plan aprobado, sin presupuesto, cinco meses en silencio, y aun así reportado en verde |
| **PRY-005** Débito contactless | **Control negativo.** Todo en orden. Cero alertas |
| **PRY-006** SARLAFT | Un cambio aprobado con impacto escrito en «tres meses», y un presupuesto aprobado que nunca incorporó los 180 millones que el comité autorizó |

## Lo que la corrida prueba

**Las 14 señales se disparan cuando deben.** Cada una tiene al menos un caso plantado, y
el grader compara el conjunto exacto: falla igual si falta una señal o si aparece una que
no está declarada.

**El control negativo pasa.** PRY-005 produce cero alertas. Es la comprobación más
importante del conjunto: un agente que alerta sobre un proyecto sano es un generador de
ruido, y en un mes se silencia.

**El amarillo no se trata como el verde.** PRY-002 tiene señales y no dispara
`declared_vs_evidence`. Quien ya reportó problema no está escondiendo nada.

**No se inventan números donde no se pueden leer.** «Tres meses» de PRY-006 queda en
`time_impact_unreadable` en vez de convertirse en 90 días.

**El umbral es un umbral.** La proyección de PRY-001 se pasa del aprobado un 3,2% y no
dispara `variance_cost`; la de PRY-006 se pasa 17,3% y sí.

**La documentación y el código dicen lo mismo.** Los 14 nombres técnicos citados en la
documentación existen en `pmo.py`, todo umbral nombrado existe, los 11 comandos están
documentados, y el número de resultados del selftest declarado en la documentación
coincide con el real.

## Lo que la corrida NO prueba

**La extracción.** Todo lo anterior corre sobre las fichas de referencia de
`expected/fichas/`, que están escritas a mano. Que un modelo leyendo `input/` produzca
esas mismas fichas es la otra mitad, y necesita correr el plugin en una sesión:

```
python3 tests/criterio-pmo/grade.py --fichas <las que produjo la corrida>
```

**Documentación real.** Seis proyectos sintéticos no son cuarenta carpetas de un banco
con quince años de historia, formatos mezclados y convenciones inconsistentes.

**Los comandos.** Los once son instrucciones para un modelo. Lo verificado aquí es la
aritmética que los alimenta y la coherencia de lo que prometen, no su salida.

## Límites conocidos que esta corrida destapó

**1 · Factura contra un entregable que no existe.** En PRY-003 Finanzas pregunta en la
minuta por qué hay facturación de una migración que no ha empezado. El cálculo **no lo
detecta**: `vendor_invoiced_without_delivery` solo se dispara cuando no hay ni un
entregable aceptado, y aquí hay tres. Para detectarlo haría falta **monto por
entregable**, que el esquema no tiene. Es una decisión de esquema, y es la primera que
sale de una prueba y no de una conversación.

**2 · Un compromiso sin fecha es invisible.** El skill de compromisos dice que uno sin
fecha se registra con `due_date: no_declarada`. El cálculo lo ignora —correctamente, no
puede estar vencido— pero tampoco lo cuenta, así que desaparece del informe. Un
compromiso que nadie fechó es un hallazgo, no un vacío.

**3 · `stated_on` está en el esquema y el cálculo no lo lee.** Es exactamente lo que
falta para detectar el compromiso reprogramado tres veces. PRY-001 lo tiene plantado con
su historial, y el cálculo solo ve que está vencido.

**4 · Un cambio aprobado con impacto ilegible desaparece del control de replanificación.**
En PRY-006 el impacto en «tres meses» no se puede leer, así que el cambio no suma a
`approved_time_days` **ni** entra en `approved_without_new_baseline`. Solo aparece en la
lista de ilegibles. El encadenamiento es correcto en cada paso y el resultado es que un
cambio real queda fuera del control.

**5 · Siete claves de configuración que nadie lee.** `paths.standard`,
`cycle.committee_next`, `cycle.report_lead_days`, `cycle.daily_sweep`, `report.language`,
`report.recipients` y `confirmation.fields_per_run`. Son el zócalo de la cadencia, las
notificaciones y el presupuesto de preguntas: está puesto y vacío.

**6 · El hash solo existe en markdown.** Es la regla que controla el costo de todo el
sistema, y hoy se le pide al modelo que la ejecute por su cuenta.

## Reproducirlo

```
git clone https://github.com/josenanez-company/criterio.git
cd criterio
python3 plugins/criterio-pmo/scripts/pmo.py selftest
python3 tests/criterio-pmo/generar.py
python3 tests/criterio-pmo/grade.py
python3 tests/coherencia.py
```

Sin dependencias. Los cuatro corren con la librería estándar de Python 3.10 o superior.
