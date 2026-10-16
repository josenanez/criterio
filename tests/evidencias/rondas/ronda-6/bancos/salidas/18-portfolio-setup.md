# /criterio-portfolio:portfolio-setup documentos/proyectos

Terminé: la instalación quedó lista y la corrida registrada. Cierro con el resultado.

## Listo — Portafolio de proyectos

**Miré:** 95 documentos en 13 proyectos · formatos: .md (37), .pdf (20), .docx (19), .xlsx (10), .csv (7), .json (1), .txt (1) · más reciente: 2026-10-16
**Eres:** PMO del portafolio (propuesto: hay 13 proyectos)
**Te aviso:** dos días antes del comité del 2026-10-23 (comité semanal, propuesto a partir de las minutas)
**En:** presentación (propuesto)
**Términos:** aceptados por José Francisco Ñáñez para la versión 0.3.12 (términos 1.1) · comprobante en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.12-2026-10-16.md` y `.pdf` · SHA-256 08da686bb7c9acf4…

Dónde guardo lo que voy encontrando: `estado/` · informes en `reportes/` (junto a `documentos/`, nunca dentro de `.criterio/`).

### Probé con tres proyectos

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-207 Onboarding PyME (gerente Beatriz Cuéllar, patrocinador Sandra Gil) | 15 | Declara verde y 30 %. Presupuesto 2.400 M COP, ejecutado 922 M. Cierre movido del 2027-03-22 al 2027-06-07 por CC-01 (acta de cambio de 2026-10-06). 26 compromisos tomados de 6 minutas y de las notas del 2026-10-16. | Facultad del gerente, fase, proveedores y contratos. El acta de cambio dice «autorizada por el comité» sin nombrar cuál. |
| PRY-200 Originación digital (gerente Ricardo Salas, patrocinador Felipe Arango) | 10 | Declara rojo y 49 %. Presupuesto 6.800 M COP, comprometido 5.617 M. Dos proveedores: Datacore (CT-936) y Núcleo Financiero (CT-107). | Facultad del gerente, fase. Ningún entregable de proveedor con acta de recibo. |
| PRY-202 Migración a la nube (gerente Rubén Cárdenas, patrocinador Mauricio Pérez) | 8 | Declara amarillo y 80 % (corte 2026-09-27). Presupuesto 9.500 M COP. Datacore tiene dos contratos (CT-726, CT-894). Un entregable recibido con acta (licenciamiento, CT-726). | Facultad del gerente, fase; el acta dice «No aplica» como producto. Sin factura de CT-894. |

### Lo que levantó el cálculo (36 señales en los tres)

**PRY-207** (21 señales):
- **Verde contradicho** (`declared_vs_evidence`): el gerente declara verde el 2026-10-13, pero el cálculo levanta sobre el mismo proyecto compromisos vencidos, reprogramados e hitos sin prueba.
- **Avance por detrás del plan** (`progress_vs_plan`): declara 30 %; el cronograma sostiene entre 50 % y 75 % (2 de 4 hitos cerrados). Brecha de 20 puntos.
- **Desviación de tiempo contra la línea base original** (`variance_time`): 77 días, 18,5 %. Es CC-01.
- **Hitos declarados cerrados sin acta que lo pruebe** (`milestone_met_without_evidence`): Diseño funcional aprobado (2026-05-14) y Ambiente de pruebas certificado (2026-08-26).
- **Compromisos vencidos** (`commitment_overdue`), 8: Revisar el anexo 3 (Sandra Gil, 7 días), Validar el ambiente 4 (Jorge Medina, 2), Aprobar el diseño 5 (Liliana Torres, 3), Actualizar la matriz 6 (Sandra Gil, 13), Revisar el anexo 11 (Javier Hoyos, 25), Entregar el punto 16 (Rubén Cárdenas, 5), Revisar el anexo 19 (Óscar Ramírez, 6), Entregar el punto 24 (Paula Céspedes, 1). En tres de ellos (anexo 3, ambiente 4, matriz 6) alguien dijo en la reunión que ya entregó, y no se presentó acta.
- **Compromisos reprogramados** (`commitment_rescheduled`): «Enviar el documento 1» (Rubén Cárdenas) 6 veces, del 2026-09-25 al 2026-12-12; «Cerrar la prueba 2» (Elena Duarte) 5 veces, del 2026-09-19 al 2026-11-17.
- **Compromisos sin fecha** (`commitment_undated`), 6: documento 9, prueba 10, matriz 14, diseño 21, fecha 23 y el ajuste del presupuesto de Laura Vélez («la otra semana»).
- **Riesgo dicho en reunión y no registrado:** el 2026-10-16 se comentó que el proveedor podría no llegar con el equipo completo; nadie lo anotó como riesgo. Está en la ficha como riesgo sin responsable.

**PRY-200** (8 señales):
- **Avance por detrás del plan:** declara 49 %; el cronograma sostiene entre 60 % y 80 %. Brecha de 11 puntos.
- **Hito declarado cerrado sin acta:** Integración con el core (2026-09-08), 38 días.
- **Facturado sin entrega** (`vendor_invoiced_without_delivery`): Datacore, 489.791.403 COP facturados (FV-1936, 2026-09-27) sin ningún entregable entregado ni aceptado; Núcleo Financiero, 707.420.229 COP (FV-2107, 2026-09-10), ídem. El contrato dice que cada entregable se factura contra acta de recibo del gerente.
- **Entregables de proveedor atrasados** (`vendor_deliverable_late`), 4: Licenciamiento del motor de Datacore (139 días) y de Núcleo (202 días), Bolsa de horas de Núcleo (107 días), Parametrización del tarifario de Núcleo (12 días).

**PRY-202** (7 señales):
- **Hito vencido** (`milestone_overdue`): Integración con el core, venció el 2026-10-12 (4 días).
- **Hitos declarados cerrados sin acta:** Diseño funcional aprobado (195 días) y Ambiente de pruebas certificado (99 días).
- **Avance:** declara 80 %; el cronograma sostiene entre 40 % y 60 % (2 de 5 hitos). Es el único caso donde el gerente declara por delante del plan.
- **Compromiso vencido:** «Entregar el punto 21» (Jorge Medina), con fecha 2026-10-05, registrado en el comité del 2026-10-16, donde Jorge Medina no figura entre los asistentes.
- **Entregables de proveedor atrasados:** Bolsa de horas de CT-726 (27 días) y Licenciamiento de CT-894 (115 días), ambos de Datacore.

**En los tres:** ninguno tiene definida la facultad del gerente (`no_authority`). El script no levantó contradicciones entre la ficha publicada por el gerente de PRY-207 (`ficha-pm.json`) y mi lectura de los documentos; las dos conviven.

### El portafolio completo
10 proyectos más (PRY-199, 201, 203 a 206, 208 a 211), 62 documentos. Lo estimo en unos 30 a 40 minutos, en dos lotes, uno tras otro en esta conversación. Es una estimación a partir de lo que costaron estos tres, no una medida.

### Lo que le falta a tu carpeta
Ninguno bloquea nada:
- **Actas de recibo de los hitos.** Los tres proyectos declaran hitos cerrados y en ninguno hay acta que pruebe uno solo, salvo dos en PRY-200.
- **Actas de recibo de entregables de proveedor.** Hay facturas radicadas en PRY-200 sin acta de recibo de ningún entregable contra el cual facturar.
- **Facultad del gerente.** Ninguna de las tres actas la dice.
- **Dependencias, alcance y fase.** Las actas dicen «Ninguna declarada» y «Componente 1, 2, 3» sin detalle; la fase no está en ningún documento.
- **Notas fuera de lugar.** En PRY-207, `2026-10-16-notas-reunion.txt` está en la raíz del proyecto y no en `30-reuniones/`, y es el único documento donde aparece el riesgo del proveedor.
- **Contratos de PRY-207.** Es el único de los tres con proveedor mencionado en una reunión y sin ningún contrato en la carpeta.

Una cosa más: había una carpeta `estado/PRY-207-onboarding-pyme/` que no creé; no la toqué.

**Preguntas que hice:** 0 (sesión sin interfaz; tomé las respuestas sugeridas: PMO, comité semanal, presentación, estado junto a los documentos).

**Ofrezco:** correr el portafolio completo. Como eres PMO y tienes gerentes de proyecto con su propia ficha (PRY-207 ya publica `ficha-pm.json`), también puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios.

Corrida registrada en `estado/corridas/2026-10-16-portfolio-setup-2.md`. La salida completa está en `estado/corridas/salida-portfolio-setup.md`.