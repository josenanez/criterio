# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio retail

**Miré:** 72 documentos en 13 proyectos. Los formatos son .md (33), .docx (12), .pdf (11), .csv (7), .xlsx (7), .json (1) y .txt (1). El más reciente es del 2026-10-16.
**Eres:** PMO del portafolio. Lo tomé por defecto porque hay 13 proyectos.
**Te aviso:** dos días antes del comité semanal. Tomé el 2026-10-23 como próximo comité, así que el informe llegaría el 2026-10-21. Es un valor por defecto: los documentos son actas de comité semanal.
**En:** presentación, por defecto.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.11 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.11-2026-10-16.md` y `.pdf`. Su SHA-256 empieza por 41a739aec7049af3…
**Dónde queda todo:** la configuración está en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`.

Nadie respondió preguntas en esta prueba: tomé la respuesta sugerida en cada una. Del primer resultado no tengo un tiempo exacto. El registro de la corrida mide 92 segundos de cálculo, y estimé unos 15 minutos de punta a punta.

### Probé con tres proyectos
Son los de documentación más reciente.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-208 Domicilios en dos horas | 4 | Gerente Ricardo Salas, patrocinador Liliana Torres. Declara verde y 59 %. Aprobado 6.800 M COP, ejecutado 3.915 M, proyección 8.460 M. | Facultad del gerente, fase |
| PRY-209 Migración del ERP | 16 | Gerente Liliana Torres, patrocinador Gustavo Neira. Declara verde y 71 %. Aprobado 2.400 M COP, ejecutado 1.178 M. Seguí 26 compromisos en seis comités y unas notas del 2026-10-16. Trae `ficha-pm.json` del gerente, que dejé aparte. | Facultad del gerente, fase, producto |
| PRY-203 Reposición automática | 4 | Gerente Mauricio Pérez, patrocinador Óscar Ramírez. Declara amarillo y 38 %. Aprobado 18.000 M COP, ejecutado 10.027 M. | Facultad del gerente, fase, producto («No aplica») |

### Lo que levantó el cálculo
`compute` levantó 21 señales. En dos de los tres proyectos el verde declarado queda contradicho.

**PRY-208**
- `declared_vs_evidence`: declara verde, pero la proyección supera lo aprobado en 24,4 % (`variance_cost`) y falta un acta de recibo.
- `milestone_met_without_evidence`: «Diseño de la experiencia aprobado» figura cerrado (2026-08-17) sin acta de recibo.
- `commitment_undated`: Javier Hoyos, «Entregar el punto 13», sin fecha.

**PRY-209**
- `declared_vs_evidence`: declara verde con 71 %, pero tiene compromisos vencidos y reprogramados.
- `progress_vs_plan`: el plan respalda 25–50 % (1 de 4 hitos cumplidos), así que el avance declarado va 21 puntos por delante.
- `commitment_overdue` (6):
  - Felipe Arango, «documento 9»: 9 días.
  - Natalia Ospina, «prueba 10»: 7 días.
  - Beatriz Cuéllar, «anexo 11»: 22 días.
  - Javier Hoyos, «matriz 14»: 16 días.
  - Carlos Peña, «matriz 22»: 1 día.
  - Elena Duarte, «fecha 23»: 1 día.
- Los compromisos «anexo 11» y «prueba 10» se dieron por entregados en comité sin presentar acta. Lo mismo pasó con «fecha 7» de Óscar Ramírez, que ya no figura abierto.
- `commitment_rescheduled` (2): Natalia Ospina, «documento 1», seis veces (del 2026-09-20 al 2026-11-25). Mauricio Pérez, «prueba 2», cinco veces (del 2026-09-30 al 2026-11-28).
- `commitment_undated` (3): Carlos Peña «ambiente 12», Javier Hoyos «ambiente 20» y Laura Vélez «ajuste del presupuesto».
- `pm_vs_pmo`: la ficha del gerente da cierre el 2027-12-02, según el acta, mientras que el cronograma v1 termina el 2027-09-28.
- Los dos casos siguientes están en la ficha, pero el cálculo no los levantó:
  - Un riesgo dicho en reunión que nadie anotó: el proveedor podría no llegar con el equipo completo.
  - Un hallazgo de seguridad en medios de pago, anotado como incidencia sin responsable.

**PRY-203**
- `milestone_overdue`: «Integración con el ERP» lleva 10 días vencido (2026-10-06).
- `milestone_met_without_evidence`: «Ambiente de pruebas certificado» figura cerrado (2026-08-06) sin acta. «Diseño de la experiencia aprobado» sí tiene acta, del 2026-10-15.
- `progress_vs_plan`: declara 38 % y el plan respalda 50–75 %, 12 puntos por detrás. El amarillo está declarado, no oculto.

Ninguno de los tres tiene la facultad del gerente en el acta. Por eso el control de cambios no podría saber si un cambio la excede.

### El portafolio completo
Faltan 10 proyectos y 48 documentos: PRY-199 a PRY-202, PRY-204 a PRY-207, PRY-210 y PRY-211. Se leen en un lote de 10 y otro de 1, uno tras otro. Estimo unos 25–30 minutos.

### Lo que le falta a tu carpeta
Ninguno de estos puntos bloquea el análisis.
- Las actas no traen la facultad del gerente ni la fase.
- El alcance de las actas leídas es genérico («Componente 1, 2, 3»), así que no se puede contrastar con el avance.
- Hay hitos cerrados sin acta de recibo en 208 y 203. Cada acta de recibo debería nombrar el hito que cierra.
- Hay compromisos sin fecha o con «por definir».
- En `estado/` ya existía una carpeta `PRY-209-migración-del-erp`, de otra herramienta (criterio-project). No la toqué: las fichas del portafolio viven en `estado/records/`.

La corrida quedó registrada como `2026-10-16-portfolio-setup-2`. La primera versión de la salida decía que «fecha 7» estaba vencido y no lo está, así que corregí la frase y registré la corrida otra vez. Puedo correr el portafolio completo cuando quieras.