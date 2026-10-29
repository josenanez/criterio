# /criterio-portfolio:portfolio-setup documentos/proyectos

Quedó instalado, y el primer resultado sobre tus documentos son las fichas de tres proyectos, calculadas sin errores de ficha. Esta sesión no tenía a quién preguntar. Por eso tomé las respuestas sugeridas y las digo en la salida.

Soy Vera, el agente PMO de Criterio. Proceso la documentación que ya tienes y digo qué no se sostiene.

## Listo — Telecomunicaciones

**Miré:** 92 documentos en 13 proyectos (PRY-199 a PRY-211) · formatos: .md 39, .docx 19, .pdf 16, .xlsx 9, .xml 4, .csv 3, .json 1, .txt 1 · más reciente: 2026-10-28
**Eres:** PMO del portafolio (propuesto: hay varios proyectos). Carpeta: `documentos/proyectos`, la que trajo el comando. La dejé marcada con `_CRITERIO_PORTAFOLIO.txt`.
**Te aviso:** dos días antes del comité semanal, el próximo el 2026-11-04 (propuesto)
**En:** presentación (propuesto)
**Términos:** aceptados por José Francisco Ñáñez, versión 0.12.1 (términos 1.3), 2026-10-28
- Comprobante en `.criterio/terminos/aceptacion-criterio-portfolio-0.12.1-2026-10-28.md` y `.pdf`.
- SHA-256 8ab8d7533e9518b6…
**Dónde queda:** la configuración está en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`.

Términos, en corto:
- Criterio produce borradores de trabajo, no decisiones ni asesoría.
- Puede equivocarse. Por eso cada dato lleva la cita del documento y la verificación es tuya.
- Tus documentos se procesan en la infraestructura de la plataforma de IA.
- Garantía y responsabilidad: licencia Apache 2.0.
- Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

### Probé con tres proyectos

Tomé PRY-208, PRY-210 y PRY-211. Cuatro proyectos empatan en documentación más reciente (2026-10-28), y PRY-204 quedó fuera por orden.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-208 Red privada para empresas | 3 | Gerente Felipe Arango, patrocinadora María Restrepo. Declara amarillo, 79 % (informe 2026-10-21). Aprobado 3.300.000.000 COP; proyección 3.320.169.600 (+0,6 %). Cierre comprometido 2026-04-14 (acta). CC-01 pendiente: +76 días y 152.000.000 COP. | Cronograma, minutas y contratos. Sin hitos no puedo contrastar la fecha de cierre del acta, que ya pasó. Autoridad del gerente y fase. |
| PRY-210 Conectividad para colegios públicos | 6 | Declara rojo, 50 %. Cierre original 2027-07-28; el cronograma v2 (2026-10-28) lo mueve a 2027-11-15. Proyección 3.951.444.314 COP contra 3.300.000.000 aprobados (+19,7 %). | Acta de recibo del hito «Diseño de red aprobado». Producto (el acta dice «No aplica»), autoridad y fase. Fecha del compromiso de Natalia Ospina. |
| PRY-211 Plataforma de internet de las cosas | 17 + la ficha del gerente | Declara amarillo, 49 %. Cierre original 2026-07-26; cronograma v2 (2026-10-28) lo mueve a 2026-11-05. Contrato CT-707 con dos entregables de 371.745.399 COP cada uno. 24 compromisos extraídos de seis minutas y de las notas del 28 de octubre. | Actas de recibo de «Diseño de red aprobado», «Integración con la red» y «Lanzamiento comercial». Acta de recibo de los dos entregables del proveedor. Facturas. Autoridad y fase. |

**Lo que levantó el cálculo** (con el nombre que le da portfolio-health):

- **PRY-210:**
  - `rebaseline_unauthorized`: la línea base se movió 110 días y ningún documento autoriza ninguno. CC-01 está «pendiente de presentación al comité».
  - `variance_time`: 110 días, 25,6 % contra la original.
  - `variance_cost`: la proyección está 19,7 % sobre lo aprobado.
  - `milestone_met_without_evidence`: «Diseño de red aprobado», vencido hace 71 días.
  - `progress_vs_plan`: declara 50 % y el plan sostiene entre 20 % y 40 %.
  - `commitment_undated`.
- **PRY-211:**
  - `rebaseline_unauthorized`: 102 días movidos, 0 autorizados. CC-01 también está pendiente.
  - `variance_time`: 102 días, 53,1 %.
  - `progress_vs_plan`: el cronograma declara los cinco hitos cerrados y el informe dice 49 %.
  - `milestone_met_without_evidence`: dos, «Diseño de red aprobado» (248 días) e «Integración con la red» (132).
  - `vendor_deliverable_late`: suministro de antenas y radios (216 días) y bolsa de horas de ingeniería (145).
  - `commitment_overdue`: seis, de 4 a 9 días.
  - `commitment_rescheduled`: siete. El de «Enviar el documento 1» lleva seis reprogramaciones, de 2026-09-20 a 2026-12-26.
  - `commitment_undated`: el ajuste del presupuesto, «la otra semana».
- **PRY-210 y PRY-211:** en ambos el informe declara un estado y el cálculo levanta señales que ese informe no explica (cinco en PRY-210, siete en PRY-211).
- **PRY-208:** el cálculo no levantó ninguna señal.

Otras cosas que dicen los documentos, sin que el cálculo las convierta en señal:
- En PRY-211 el hito «Lanzamiento comercial» figura cerrado con fecha 2026-11-05, posterior a hoy.
- El riesgo de que el proveedor no llegue con el equipo completo se dijo en la reunión del 28 de octubre y nadie lo anotó.
- Carlos Peña dijo el 21 de octubre que ya entregó «Aprobar el diseño 13». No hay acta y el compromiso sigue abierto.

La ficha que publicó el gerente de PRY-211 (`ficha-pm.json`) quedó guardada aparte, sin mezclarla con mi lectura. El contraste entre las dos no levantó diferencias.

### El portafolio completo

Faltan 10 proyectos y 66 documentos, en dos lotes uno tras otro en esta conversación. Mi estimación es de unos 20 a 30 minutos, pero no la medí.

### Lo que le falta a tu carpeta

- No puedo leer cuatro cronogramas en `.xml` (PRY-200, 201, 204 y 206) sin instalar algo. Sin ellos esos proyectos quedan sin hitos.
- PRY-203 tiene solo acta e informe: sin cronograma, minutas ni contrato.
- PRY-208 no tiene cronograma ni minutas, y PRY-210 no tiene actas de recibo.
- Ninguna de las tres actas que leí declara la autoridad del gerente, y la fase no aparece en ninguna parte.
- La carpeta ya tiene la estructura por proyecto (gobierno, plan, seguimiento, reuniones). No moví ni creé nada dentro de los documentos, salvo la marca de la carpeta raíz.
- `estado/` ya tenía la carpeta de PRY-211 de Samuel (la familia de proyecto). La mía convive en `estado/records`, `estado/snapshots` y `estado/reports`.

Siguiente paso: correr el portafolio completo con `/criterio-portfolio:portfolio-scan`. Como PMO con equipo, también puedo publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios.

**Preguntas hechas:** 0.

La corrida quedó registrada como `2026-10-28-portfolio-setup-1`, con el texto completo en `estado/corridas/salida-portfolio-setup.md`.