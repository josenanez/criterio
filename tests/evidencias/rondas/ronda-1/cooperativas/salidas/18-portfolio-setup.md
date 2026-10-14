# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativas (prueba)

**Miré:** 72 documentos en 13 proyectos. Los formatos son .md (27), .docx (14), .pdf (11), .xlsx (10), .csv (8), .json (1) y .txt (1). El más reciente es del 2026-10-14.
**Eres:** PMO del portafolio, porque hay varios proyectos (respuesta sugerida).
**Te aviso:** dos días antes del comité del 2026-10-21. Los archivos se llaman «comité semanal», así que asumí comité semanal. La fecha del próximo comité es una suposición mía; dime la real y la cambio.
**En:** página. Es el formato de la plantilla de configuración; la respuesta sugerida era presentación, y se cambia si lo pides.
**Términos:** José Francisco Ñáñez los aceptó para esta prueba el 2026-10-14.
**Dónde queda:** la configuración está en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`. La verificación pasó sin problemas.

### Probé con tres proyectos

Tomé los tres con la documentación más reciente: PRY-208, PRY-205 y PRY-209. Las fichas están en `estado/records/` y quedaron selladas.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-208 Motor de crédito | 8 | Presupuesto de 2.400 M COP, cierre el 2026-11-29, declara Verde con 81% | Autoridad del gerente, fase, actas de recibo de sus dos hitos cerrados, dueño del riesgo del proveedor |
| PRY-205 Prevención de lavado de activos | 7 | Presupuesto de 2.400 M COP, declara Amarillo con 67%, dos solicitudes de cambio (CC-01 autorizada, CC-02 pendiente) | Autoridad, fase, actas de recibo de tres de sus cuatro hitos, acta del comité que autorizó CC-01 |
| PRY-209 Convenios de libranza | 8 | Presupuesto de 6.800 M COP, declara Verde con 40%, CC-01 autorizada | Autoridad, fase, actas de recibo del diseño funcional y de la integración con el core |

### Hallazgos

Todo esto sale del cálculo (`compute`): 23 señales en total, y dos proyectos que declaran Verde contradichos por la evidencia (PRY-208 y PRY-209).

- **PRY-208:**
  - Lleva 100 días de atraso contra la línea base original, y ningún cambio aprobado los respalda: CC-01 sigue pendiente del comité.
  - La proyección al cierre es 16,1% sobre lo aprobado.
  - Dos hitos cerrados no tienen acta que lo pruebe.
  - Un compromiso quedó sin fecha («la otra semana»).
- **PRY-205:**
  - Lleva 112 días de atraso; solo 41 están autorizados, así que 71 quedan sin autorizar.
  - CC-01 está autorizada, pero no hay línea base nueva que la recoja.
  - Declara 67% con los cuatro hitos cerrados.
  - Tres hitos cerrados no tienen acta.
  - Tiene 91,1% del presupuesto comprometido.
  - Un compromiso lleva 15 días vencido (Óscar Ramírez, «punto 15») y otro no tiene fecha.
- **PRY-209:**
  - Lleva 114 días de atraso, autorizados por CC-01, pero la línea base tampoco se actualizó.
  - Declara 40% con los cuatro hitos cerrados.
  - Dos hitos cerrados no tienen acta.

No hay contradicciones entre documentos ni cambios de gobierno. La ficha que publicó el gerente de PRY-208 (`ficha-pm.json`) no discrepa de mi lectura.

### El portafolio completo

Faltan 10 proyectos (unos 57 documentos), en dos lotes uno tras otro en esta conversación. No medí el tiempo; a ojo es unas tres veces y media lo que acabo de hacer.

### Lo que le falta a tu carpeta

- **Actas de recibo:** casi ningún hito cerrado tiene la suya, y es lo que más señales produce.
- **Actas de las autorizaciones:** las solicitudes dicen «autorizada por el comité» sin decir cuál ni dejar el acta.
- **Autoridad del gerente y fase:** ninguna acta los declara.
- **Línea base:** los cambios aprobados no dejan una línea base nueva firmada.
- **Compromisos y riesgos:** hay compromisos con fecha relativa («la otra semana», «por definir») y un riesgo dicho en reunión que nadie registró (el equipo incompleto del proveedor en PRY-208).

Ninguno es bloqueante.

**Cómo corrió:** hice 0 preguntas, porque era una sesión de prueba sin interfaz. Los minutos hasta el primer resultado no los medí. La corrida quedó registrada como `2026-10-14-portfolio-setup-1` y la salida está en `estado/corridas/salida-portfolio-setup.md`.

¿Corro el portafolio completo? También puedo publicar el estándar en una carpeta compartida para tus gerentes. No hay ninguna configurada y no la inventé.