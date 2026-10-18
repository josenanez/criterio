# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Retail

**Miré:** 91 documentos en 13 proyectos. Los formatos son md (45), docx (13), pdf (13), xlsx (13), csv (5), json (1) y txt (1). El más reciente es del 2026-10-17.

**Eres:** PMO del portafolio, porque hay 13 proyectos.

**Te aviso:** dos días antes del comité semanal. Supuse que el próximo es el 2026-10-23, porque tus comités caen en jueves o viernes; si no es así, dímelo y lo cambio.

**En:** la configuración queda con formato `html`, que es el que usa el ejemplo de configuración. No verifiqué que sea la «presentación» que sugería el flujo; dime si quieres otra forma y lo cambio.

**Términos:** aceptados por José Francisco Ñáñez para la versión 0.4.0 (términos 1.1), fecha 2026-10-17. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.4.0-2026-10-17.md` y `.pdf`. Los primeros 16 caracteres del SHA-256 del `.md` son 96015115a67f6c94.

No hice ninguna pregunta; tomé los valores sugeridos. La configuración está en `.criterio/portafolio/config.json`. Lo que voy encontrando va en `estado/` y los informes irán en `reportes/`. Leo un proyecto a la vez, en lotes de diez, hasta 400 documentos por corrida. La verificación de la configuración pasó sin problemas.

### Probé con tres proyectos

Elegí los de documentación más reciente. PRY-203 también tiene un documento del 2026-10-17, pero lo dejé para el barrido completo.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-201 Programa de fidelización | 7 | Patrocinador Jorge Medina y gerente Andrés Lozano. Declara **verde** y 34 % de avance. Presupuesto aprobado 9.500 M COP, ejecutado 5.399,9 M. Cierre original 2026-08-24, vigente 2026-09-17. CC-01 está pendiente de comité. | Facultad del gerente, fase, acta de recibo de 4 de los 5 hitos, y quién decidirá CC-01. |
| PRY-208 Domicilios en dos horas | 7 | Patrocinador Camilo Beltrán y gerente Beatriz Cuéllar. Declara **rojo** y 54 %. Cierre original 2027-01-23, vigente 2027-04-11 por CC-01, autorizada por el comité el 2026-10-11. Contrato CT-741 con Datos y Demanda, con 3 entregables de 859,5 M COP cada uno. | Facultad del gerente, fase, actas de 2 de los 3 hitos cerrados, recibo de cualquier entregable del proveedor, y facturación. |
| PRY-209 Migración del ERP | 6 | Patrocinadora Natalia Ospina y gerente Javier Hoyos. Declara **amarillo** y 41 %. Presupuesto aprobado 1.200 M COP. Cierre original 2027-07-28, vigente 2027-10-16. El hito de diseño tiene acta de recibo. CC-01 está pendiente de comité. | Producto asociado (el acta dice «No aplica»), facultad del gerente y fase. |

### Lo que levantó el cálculo (15 señales)

**PRY-201 (8 señales): declara verde y los documentos no lo sostienen.**
- `declared_vs_evidence`: el verde del 2026-10-09 convive con cuatro señales sin explicar.
- `progress_vs_plan`: declara 34 %, pero el cronograma marca los cinco hitos como cerrados, lo que sostiene 100 %. Los dos documentos se desmienten.
- `milestone_met_without_evidence` ×4: cuatro hitos cerrados no tienen acta de recibo. Diseño de la experiencia venció hace 420 días, Ambiente de pruebas hace 329, Integración con el ERP hace 237 y Despliegue en la cadena hace 30. Solo Piloto en tiendas tiene acta.
- `rebaseline_unauthorized`: el cronograma v2 ya corrió el cierre 24 días. CC-01 pide esos mismos 24 días y sigue pendiente de comité.
- `commitment_overdue`: Natalia Ospina debía «Entregar el punto 16» el 2026-10-01, hace 16 días.

**PRY-208 (5 señales).**
- `variance_time`: 78 días (23,2 %) contra el cierre original. Está autorizada por CC-01, que quedó como línea base v2.
- `milestone_met_without_evidence` ×2: Diseño de la experiencia (hace 171 días) y Ambiente de pruebas (hace 104) están cerrados sin acta.
- `vendor_deliverable_late` ×2: Licenciamiento de la plataforma (hace 146 días) y Bolsa de horas (hace 53) siguen sin recibo. El contrato los marcaba «en curso» y «pendiente», y los leí como pendientes.

**PRY-209 (2 señales).**
- `variance_time`: 80 días (17,4 %) contra el original.
- `rebaseline_unauthorized`: el cronograma v2 ya mueve el cierre 80 días y CC-01 sigue pendiente.

Ninguna de las tres fichas tiene la facultad del gerente. En PRY-201 hay además 12 campos tomados de un acta de hace 17 meses, sin confirmación posterior.

### El portafolio completo
Faltan 10 proyectos y 71 documentos, en un solo lote y de uno en uno. La prueba tomó 103 segundos, y calculo unas 3 a 4 veces eso para el resto. La mayor parte de lo que tardó fue leer los archivos.

### Lo que le falta a tu carpeta
- De los 9 hitos cerrados que vi en estos tres proyectos, solo 3 tienen acta de recibo. Eso explica la mayoría de las señales.
- Las solicitudes de cambio no dicen quién las decidió ni cuándo.
- Ninguna acta de constitución fija qué puede decidir el gerente sin subir a comité.
- En `PRY-203-reposición-automática` hay un `ficha-pm.json` y unas notas de reunión del 2026-10-17 sueltas fuera de `30-reuniones`. Las leeré en el barrido.
- Dentro de `estado/` ya existía una carpeta `PRY-203-reposición-automática/` con su propio estado (`records/`, `corridas/`, `snapshots/`). No es mía y no la toqué. Conviene moverla o borrarla si es un resto de otra prueba.

La salida quedó en `estado/corridas/salida-portfolio-setup.md` y la corrida en el registro de corridas (`2026-10-17-portfolio-setup-1`).

¿Corro ahora el portafolio completo? Si quieres que tus gerentes de proyecto usen los mismos criterios, también puedo publicar el estándar en una carpeta compartida.