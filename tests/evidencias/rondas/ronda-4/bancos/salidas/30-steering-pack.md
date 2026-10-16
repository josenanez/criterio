# /criterio-portfolio:steering-pack 

**Fichas cargadas:** las 13 de `estado/records` (PRY-199 a PRY-211), con cifras recalculadas por `compute` al 2026-10-15. También usé las salidas de hoy de change-control, raid-log y vendor-tracking, y el paquete de PRY-210. No reabrí ningún `.docx`, `.pdf` ni `.xlsx`. Los términos ya estaban vigentes (v1.1, aceptados el 2026-10-15 por José Francisco Ñáñez), así que no se registraron de nuevo. No se pasó fecha, así que tomé la del próximo comité de la configuración, 2026-10-22.

# Comité de proyectos — 2026-10-22
5 decisiones · 5 escalamientos · 10 de 13 proyectos con hallazgos (60 señales abiertas)

## Decisiones del comité anterior
No hay acta ni minuta de un comité de portafolio anterior en la carpeta, así que no puedo cerrar el ciclo. Cinco proyectos traen un CC-01 «autorizado por el comité» sin nombre del comité ni acta; es el punto 2.

## Decisiones de hoy

**1. ¿Se declara por escrito quién aprueba los cambios de alcance, fecha y presupuesto, y hasta qué monto y días decide cada gerente?**
- **Proyectos:** los 13 (la autoridad no aparece en ninguno).
- **Quién decide:** sin determinar. Cada ficha nombra un comité de proyecto distinto (Arquitectura, Transformación Digital, Medios de Pago y Riesgos).
- **Si no se decide hoy:** los puntos 2, 3 y 4 pueden devolverse con un «eso no lo decide este comité».
- **Opciones:** (A) una matriz única de autoridad del portafolio; (B) una adenda al acta de cada proyecto; (C) no declararla, y todo cambio sube a este comité. Ninguna cuesta COP.
- **Recomiendo A**, citada después en una adenda por proyecto (B). Con C este comité aprobaría hasta cambios de un día. No propongo umbrales: ningún documento da base para fijarlos.

**2. ¿Se ratifica con acta cada CC-01 que dice «autorizado por el comité», o se tratan como no autorizados hasta que la haya?**
- **Proyectos:** PRY-201, 202, 204, 205 y 207.
- **Si no se decide hoy:** cinco desviaciones de fecha y cinco aumentos de costo siguen sin documento que los respalde.

| Proyecto | Tiempo | Costo adicional | Desviación vs. línea base original | ¿Línea base nueva? |
|---|---|---|---|---|
| PRY-201 | +20 días | 40.000.000 COP | 20 días (5,7 %) | Cuadra |
| PRY-202 | +120 días | 240.000.000 COP | 120 días (52,6 %) | Cuadra |
| PRY-204 | +83 días | 166.000.000 COP | 83 días (21,0 %) | Falta |
| PRY-205 | +78 días | 156.000.000 COP | 78 días (37,3 %) | Falta |
| PRY-207 | +32 días | 64.000.000 COP | 32 días (8,8 %) | La ficha dice que no hay; `compute` no lo marca |

- **Opciones:** (A) ratificar en acta y registrar la línea base nueva donde falte; (B) no tratarlos como autorizados hasta que haya acta; (C) dejarlos como están.
- **Recomiendo A** para los que este comité pueda confirmar que sí autorizó, y B para los demás. Hoy la evidencia no distingue entre unos y otros. En ambos casos hay que pedir el alcance de cada CC-01: ninguno dice qué se agrega.

**3. PRY-210: ¿se aprueba CC-01 (+41 días, +82.000.000 COP) con salida a producción el 2027-04-11, o se rechaza y el cronograma vuelve al 2027-03-01?**
- **Quién decide:** sin determinar (punto 1).
- **Si no se decide hoy:** el cronograma v2 ya trae 2027-04-11 sin cambio aprobado, y la gerente reporta verde sobre ese plan. CC-01 está pendiente desde 2026-10-04.
- **Aprobar:** el alcance se amplía sin decir en qué, +41 días y +82.000.000 COP. Aprobado 2.400.000.000, proyección 2.406.453.124 (+0,3 %).
- **Rechazar:** hay que rehacer el cronograma, y nadie ha contrastado que 2027-03-01 sea alcanzable.
- **Recomiendo aprobar**, condicionado a que la gerente entregue el alcance antes de firmar. Es una recomendación con información incompleta.

**4. ¿Se retienen los pagos a Datacore Colombia hasta que haya acta de recibo de lo facturado, en CT-152 (PRY-204) y CT-932 (PRY-208)?**
- **Quién decide:** sin determinar (punto 1). Afecta a dos proyectos.
- **Si no se decide hoy:** FV-1152 puede pagarse sin acta de la parametrización. No sé si ya se pagó: el documento solo dice «Radicada en cuentas por pagar».
- **PRY-204:**
  - `compute` da 1.351.144.064 COP facturados.
  - El licenciamiento lleva 236 días tarde.
  - La parametrización figura como aceptada sin acta. Vale 675.572.032 COP y se facturó antes de su fecha comprometida (esta cifra sale del contrato, vía vendor-tracking de hoy, no de `compute`).
- **PRY-208:** 4 entregables, 0 aceptados, 3 tarde y 105.076.622 COP facturados.
- **Opciones:** (A) retener todo pago pendiente hasta tener acta y desglose; (B) pagar lo que tiene acta y retener lo demás; (C) no actuar.
- **Recomiendo B** si Datacore entrega el desglose de FV-1152 a tiempo, y A si no. No sé la vigencia del contrato, y eso cambia el apremio.

**5. ¿Se adopta como regla que un hito solo cuenta como cumplido con acta de recibo?**
- **Proyectos:** PRY-200, 202, 204, 205, 206, 207, 208, 209, 210 y 211.
- **Si no se decide hoy:** el avance y el estado de esos proyectos siguen apoyados en hitos sin evidencia. Cuatro reportan verde contra su evidencia (PRY-206, 209, 210, 211).
- PRY-211 (34 % declarado), PRY-207 (40 %) y PRY-206 (89 %) tienen el plan en 100 % de hitos y la fecha de cierre ya pasada, sin replanificar. O los hitos se marcaron cumplidos sin estarlo, o el avance está mal declarado; los documentos no dicen cuál.
- **Opciones:** (A) el hito sin acta pasa a «pendiente de evidencia»; (B) igual, con plazo hasta el siguiente comité para presentar las actas; (C) sin cambio.
- **Recomiendo B.** Lo que no recomiendo es C: quedaría un estado verde que ningún documento sostiene.

## Escalamientos sin decisión asociada
| Proyecto | Qué | Qué se necesita |
|---|---|---|
| PRY-200, 201, 202, 204, 205 | El proveedor no ha confirmado la fecha de la última entrega; no tiene nombre ni doliente. Informes del 2026-09-24 al 2026-10-13 | Qué proveedor es y quién lo confirma, con fecha |
| PRY-202, 208, 209 | Dependen de «el core», sin código de proyecto | Que cada gerente diga qué proyecto es |
| PRY-210 | Riesgo dicho en reunión el 2026-10-15 y no registrado: el proveedor podría no llegar con el equipo completo | Doliente y fecha |
| PRY-210 | Cuatro compromisos reprogramados entre 3 y 6 veces; el peor, «Enviar el documento 1», pasó de 2026-09-17 a 2026-12-08 | Nombrar qué bloquea cada entregable |
| PRY-203 | Rojo declarado (88 %, 2026-10-11) y sin línea base | Cronograma con línea base y la causa del rojo |

## Para conocimiento
Una línea por proyecto está en el archivo de salida. Ningún proyecto lleva más de 15 días en silencio; el máximo es PRY-200, con 10.

## Anexo
- **Contradicciones:**
  - PRY-210: fin del proyecto el 2027-04-11 en el cronograma v2 y el 2027-04-24 en el acta.
  - PRY-201: cierre el 2027-05-11 en el acta y el 2027-04-06 en el cronograma v1.
  - PRY-210 y PRY-211: ejecutado mayor que comprometido.
  - PRY-208: declara depender del core y su acta dice «Ninguna declarada».
- **Vacíos:**
  - Autoridad y fase faltan en los 13.
  - Los 35 ítems RAID no tienen doliente, fecha, probabilidad ni impacto, y las mismas frases se repiten en los 13 proyectos.
  - Hay campos de 12 a 17 meses en PRY-204, 206, 207, 210 y 211.
  - La corrida de change-control de hoy evaluó un cambio de +30 días en PRY-201 que no está en la ficha, y no lo traje como decisión.

## Después
Cuando el comité sesione, puedo registrar cada decisión con su fecha en la ficha del proyecto.

---
Criterio portfolio v0.3.10 · fichas PRY-199 a PRY-211 al 2026-10-15 · términos v1.1, aceptados el 2026-10-15 por José Francisco Ñáñez. Campos inciertos: quién decide en los 13 proyectos, el alcance de cada CC-01, el estado de pago de FV-1152, la vigencia de CT-152 y CT-932, y la identidad de «el core» y del proveedor sin nombre. Es un borrador de trabajo, no una decisión ni una asesoría; la verificación contra los documentos citados es de quien lo use. Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.10

La corrida quedó registrada como `2026-10-15-steering-pack-1`, con 128 segundos medidos. El material completo está en `estado/corridas/salida-steering-pack.md`.