# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos mineros

La instalación está lista y probé el agente con tres de los 13 proyectos. Nadie respondió preguntas, así que tomé los valores sugeridos.

**Miré:** 69 documentos en 13 proyectos. Formatos: .md (28), .docx (14), .pdf (13), .xlsx (8), .csv (4), .json (1), .txt (1). El más reciente es del 2026-10-14.

**Eres:** PMO del portafolio, porque hay 13 proyectos.

**Te aviso:** dos días antes del comité del 2026-10-28 y cada dos semanas desde ahí. Es un valor sugerido porque no había a quién preguntarle la fecha real.

**En:** presentación, también sugerido.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-14 para esta prueba.

**Dónde quedó:**
- La configuración está en `.criterio/portafolio/config.json`.
- Lo que voy encontrando está en `estado/portafolio`. `estado/` ya tenía datos de producto y de PRY-208, y no los mezclé.
- Los informes irán a `reportes`.

### Probé con tres proyectos

Elegí los de documentación más reciente: PRY-203, PRY-208 y PRY-207. Son 24 documentos.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-203 Despacho automático de flota | 7 | Declara amarillo y 40 %. Presupuesto 2.400 M COP, con proyección +0,8 %. El cambio CC-01 suma 32 días y 64 M COP. | Facultad del gerente, fase, proveedor del contrato, acta del comité que autorizó CC-01. |
| PRY-208 Trazabilidad del mineral | 11 | Declara verde y 75 %, con corte al 2026-09-26. Presupuesto 3.300 M COP, con proyección −0,3 %. Contrato CT-462 con Equipos Pesados Andinos, 289,3 M facturados. Gustavo Neira es patrocinador y gerente a la vez. | Facultad del gerente, fase, estado declarado en las notas del 2026-10-14. |
| PRY-207 Gemelo digital de la planta | 6 | Declara rojo y 65 %. Presupuesto 9.500 M COP, con proyección +24,1 %. | Facultad del gerente, fase, nombre del proveedor que no confirmó la entrega. |

### Lo que levantó el cálculo

`compute` levantó 18 señales en los tres proyectos. No agrego ninguna por lectura propia.

**PRY-208 (9 señales)**
- **Declara verde y los documentos lo contradicen** (`declared_vs_evidence`). Tiene tres hitos sin acta, avance por debajo de lo que sostiene el plan y un entregable del proveedor atrasado.
- **Hitos cerrados sin acta de recibo** (`milestone_met_without_evidence`). Son Ingeniería básica, Montaje e instalación y Pruebas en operación.
- **Avance bajo el plan** (`progress_vs_plan`). Declara 75 % con 5 de 5 hitos cerrados.
- **Entregable atrasado** (`vendor_deliverable_late`). La bolsa de horas de ingeniería venció el 2026-03-26 y sigue pendiente.
- **Compromiso sin fecha** (`commitment_undated`). Laura Vélez, ajuste del presupuesto, «la otra semana».
- **Dos diferencias entre la ficha del gerente y la mía** (`pm_vs_pmo`). La fecha de cierre es 2026-07-21 en el acta y 2026-06-19 en el cronograma. El estado declarado es `not_found` en la ficha del gerente.

**PRY-207 (5 señales)**
- **Sobrecosto proyectado de 24,1 %** (`variance_cost`).
- **Compromiso vencido** (`commitment_overdue`). Laura Vélez, punto 36, venció el 2026-09-17, hace 27 días.
- **Dos hitos cerrados sin acta** (`milestone_met_without_evidence`). Ingeniería de detalle y Montaje e instalación.
- **Avance bajo el plan** (`progress_vs_plan`). Declara 65 % con 4 de 4 hitos cerrados.

**PRY-203 (4 señales)**
- **Tres hitos cerrados sin acta** (`milestone_met_without_evidence`). Ingeniería básica, Ingeniería de detalle y Montaje e instalación.
- **Avance bajo el plan** (`progress_vs_plan`). Declara 40 % con 4 de 4 hitos cerrados.
- **El cambio CC-01 no levantó señal.** Sus 32 días ya están en el cronograma v2.

### El portafolio completo

Faltan 10 proyectos y 45 documentos, en un lote. Calculo entre 20 y 30 minutos, en una sola conversación y uno tras otro. Es una estimación mía, no una medida.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea el análisis.
- Casi todos los hitos se declaran cerrados sin acta de recibo.
- Ningún proyecto declara la facultad del gerente para decidir sin subir a comité.
- Las actas de constitución no dicen la fase.
- Hay compromisos de comité con responsables que no asistieron (PRY-203 y PRY-207) y uno sin fecha (PRY-208).
- PRY-208 tiene a la misma persona como patrocinador y gerente.
- La autorización de CC-01 dice «Autorizada por el comité», pero ningún acta de comité la respalda.
- Los nombres de archivo ya traen fecha (AAAA-MM-DD), y eso ayudó.
- PRY-208 tiene una ficha del gerente (`ficha-pm.json`). La guardé aparte, sin mezclarla con mi lectura.

La salida quedó en `estado/portafolio/corridas/salida-portfolio-setup.md` y la corrida quedó registrada como `2026-10-14-portfolio-setup-1`.

**Siguiente paso:** ¿corro el portafolio completo? También puedo publicar el estándar en una carpeta compartida para que tus gerentes de proyecto usen los mismos criterios.