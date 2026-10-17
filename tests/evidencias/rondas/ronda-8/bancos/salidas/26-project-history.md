# /criterio-portfolio:project-history PRY-202

## Historia · PRY-202 Migración a la nube · 2025-10-27 a 2026-10-17

**Leí:** 20 archivos entre 2025-10-27 y 2026-10-17: 19 documentos fuente y la `ficha-pm.json`, que es un registro derivado y no cuenta como evidencia.
**Trimestres sin un solo documento:** 2026-T1 (ene–mar) y 2026-T2 (abr–jun). Entre el contrato CT-243 (2025-11-08) y la factura FV-1267 (2026-08-30) la carpeta no tiene nada.

**Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo.

### En una línea
El proyecto arrancó con acta, contratos y cronograma entre el 2025-10-27 y el 2025-11-08, y de ahí no hay nada hasta el 2026-08-30. Los dos primeros hitos vencieron en ese vacío (2026-02-24 y 2026-06-07). Desde septiembre de 2026 la carpeta se llena de comités semanales. En tres semanas aparecen la solicitud de cambio CC-01 (2026-10-08, sin decidir), la línea base v2 que mueve el cierre de 2027-04-14 a 2027-06-29 (2026-10-17) y un informe que declara Rojo con 77 % (2026-10-17). La línea base se movió 76 días sin aprobación documentada, y dos de los tres hitos que se dan por cerrados no tienen acta.

### Las cuatro cifras
| Replanificaciones | Atraso acumulado vs. original | Meses declarando sin sustento | Cambios de gobierno |
|---|---|---|---|
| 1 (v2, 2026-10-17) | 76 días (14,7 %) | No calculable: hay una sola declaración (2026-10-17) y ninguna serie | 0 en los documentos |

Las cifras vienen de `portafolio.py compute`.

### Línea de tiempo
| Fecha | Documento | Qué cambió |
|---|---|---|
| 2025-10-27 | contrato CT-267 (Datacore Colombia) | Tres entregables. La columna de estado ya marca «recibido» para «Bolsa de horas de desarrollo», que vence 2026-08-24. El documento se editó después de la firma. |
| 2025-11-03 | acta de constitución | Patrocinadora María Restrepo, gerente Camilo Beltrán, Comité de Banca Empresas. Presupuesto 6.800.000.000 COP, inicio 2025-11-13, cierre 2027-04-14. Dependencias: «Ninguna declarada». |
| 2025-11-03 | cronograma-v1.xlsx | Línea base original. Cinco hitos, con «Salida a producción» el 2027-04-14. Tres hitos figuran «cerrado», uno con fecha 2026-09-19. El archivo se editó después de la fecha de su nombre. |
| 2025-11-08 | contrato CT-243 (Datacore Colombia) | Dos entregables más. «Licenciamiento del motor» vuelve a aparecer, ahora con vencimiento 2026-05-21. |
| — | *(sin documentos de 2026-01 a 2026-08-29)* | Vencen «Diseño funcional aprobado» (2026-02-24), «Ambiente de pruebas certificado» (2026-06-07), «Licenciamiento del motor» CT-267 (2026-04-04) y CT-243 (2026-05-21). |
| 2026-08-30 | factura FV-1267 | Datacore cobra 428.583.833 COP por «Entregables del contrato CT-267». Radicada en cuentas por pagar. No hay acta de recibo en la carpeta. |
| 2026-09-05 | comité semanal | Primer comité en la carpeta. Asisten 4 personas. Cuatro compromisos abiertos. |
| 2026-09-12 | comité semanal | Primeras fechas nuevas para «documento 1», «prueba 2» y «ambiente 4». |
| 2026-09-19 | comité semanal + actas de recibo 3 y 7 | Dos compromisos cerrados con acta. Ricardo Salas dice que ya entregó el «punto 8»; no se presentó acta. |
| 2026-09-26 | comité semanal | «Aprobar el diseño 13» queda «por definir». |
| 2026-10-03 | comité semanal | Ricardo Salas dice que ya entregó el «diseño 13»; no se presentó acta. Sale de la lista. |
| 2026-10-04 | acta de recibo «Ambiente de pruebas certificado» | Único respaldo documental de un hito. Fecha de la línea base del hito: 2026-06-07. |
| 2026-10-08 | solicitud de cambio CC-01 | Ampliación de alcance: +76 días sobre la línea base vigente y 152.000.000 COP. «Pendiente de presentación al comité». |
| 2026-10-10 | comité semanal + acta de recibo 11 | Mauricio Pérez dice que ya entregó el «anexo 19»; no se presentó acta. No se menciona CC-01. |
| 2026-10-17 | cronograma-v2.csv | «Salida a producción» pasa de 2027-04-14 a 2027-06-29. No hay motivo ni aprobación. |
| 2026-10-17 | informe de avance | Rojo, 77 %. Dos semanas perdidas por rotación de un desarrollador. La prueba de carga no alcanzó el umbral y se repite. |
| 2026-10-17 | notas de reunión (.txt, no es acta de comité) | La fecha de «documento 1» pasa por sexta vez, al 2026-12-28. Se comentó un riesgo del proveedor y nadie lo registró. |

### Replanificaciones
| Nº | Fecha | Fecha de cierre nueva | Motivo declarado | Documento que la aprobó |
|---|---|---|---|---|
| 1 | 2026-10-17 | 2027-06-29 (original 2027-04-14) | **No documentado** | **Ninguno.** CC-01 (2026-10-08) sigue «pendiente de presentación al comité». El script cuenta 76 días movidos y 0 autorizados. |

La v2 conserva la fecha original en su columna `fecha_linea_base`, así que el atraso de 76 días se puede medir. El cierre de 2027-04-14 también está en el acta de constitución, que respalda esa fecha como original.

### Gobierno
| Fecha | Qué cambió | Documento |
|---|---|---|
| — | Nada. Patrocinadora, gerente y comité son los mismos en el acta (2025-11-03) y en el informe (2026-10-17). | acta de constitución; informe de avance |

La autoridad y la fase no aparecen en ningún documento. El comité sesionó semanalmente del 2026-09-05 al 2026-10-10, pero CC-01 no figura en ninguna de esas minutas.

### Compromisos que se repitieron
| Doliente | Qué | Veces | Fechas prometidas |
|---|---|---|---|
| Laura Vélez | Enviar el documento 1 | 6 | 09-24 → 10-03 → 10-15 → 11-04 → 11-24 → 12-14 → 12-28 |
| María Restrepo (patrocinadora) | Cerrar la prueba 2 | 5 | 09-13 → 10-02 → 10-23 → 11-05 → 11-24 → 12-15 |
| Paula Céspedes | Validar el ambiente 4 | 2 (bajo el umbral de 3) | 09-24 → 10-14 → 11-03 |

Hay además cuatro compromisos vencidos que siguen en la lista sin fecha nueva: Sandra Gil «ambiente 12» (2026-09-24), Natalia Ospina «matriz 6» (2026-10-04) y «ambiente 20» (2026-10-07), y Ricardo Salas «punto 16» (2026-10-13). Tres más salieron de la lista porque su responsable dijo «ya lo entregué», sin acta: «punto 8», «diseño 13» y «anexo 19». Los tres compromisos sin fecha son «diseño 13», «matriz 22» y «ajuste del presupuesto» («la otra semana»).

### Desde cuándo lo declarado no se sostiene
No se puede fechar con una serie, porque en la carpeta hay un único informe de estado (2026-10-17). Lo que sí se puede decir:

- **El primer hito sin evidencia** es «Diseño funcional aprobado», con fecha 2026-02-24. Figura «cerrado» y no hay ningún documento suyo. El otro cierre sin acta es «Integración con el core» (2026-09-19). El 77 % se apoya en tres de cinco hitos cerrados, y solo uno tiene acta (el ambiente de pruebas, fechada 2026-10-04).
- **Lo anterior a 2026-08-30 no se puede verificar**, porque la carpeta no tiene ningún documento de ese tramo. No sé si faltan documentos o si no se produjeron.
- **Después de esa fecha se siguió reportando** el 77 %, el cierre de la integración con el core y la línea base v2. El informe declara Rojo y no menciona seis señales que sí están en los documentos: atraso de 76 días, línea base movida sin autorización, hitos cerrados sin evidencia, entregables del proveedor vencidos, compromisos vencidos y compromisos reprogramados.

El color declarado (Rojo) no es optimista. Lo que no tiene sustento son los cierres de hitos y la línea base v2.

### Lecciones ancladas a un hecho
1. **Pago sin acta localizable.** El 2026-08-30 se radicó la factura FV-1267 por 428.583.833 COP contra CT-267, cuya condición de pago exige acta de recibo firmada por el gerente. No hay acta de «Bolsa de horas de desarrollo» (vencía 2026-08-24). Efecto: no se puede sustentar que lo facturado se entregó. Lección: el acta se archiva antes de radicar la factura.
2. **Hito con acta tardía.** El acta de «Ambiente de pruebas certificado» lleva fecha 2026-10-04 y el hito estaba planeado para 2026-06-07. Efecto: entre una y otra fecha el cierre se sostuvo sin documento. Lección: un hito se cierra el día del acta, no el de la fecha planeada.
3. **Línea base movida antes de la decisión.** El 2026-10-17 la v2 corrió el cierre 76 días mientras CC-01 (2026-10-08) seguía pendiente. Efecto: el atraso de 14,7 % existe en el plan vigente sin aprobación. Lección: la v2 se emite cuando el comité decide, no antes.
4. **Fecha nueva sin causa registrada.** «Enviar el documento 1» cambió de fecha en seis comités consecutivos (2026-09-12 a 2026-10-17), sin motivo en ninguna minuta. Efecto: la última fecha (2026-12-28) cae después del piloto planeado (2026-12-31) casi sin margen. Lección: cada reprogramación se registra con su causa.
5. **Archivos con fecha vieja y contenido nuevo.** El cronograma v1 (nombrado 2025-11-03) y el contrato CT-267 (2025-10-27) traen estados posteriores a su fecha. Efecto: no puedo confirmar que la línea base «original» esté intacta; solo el cierre de 2027-04-14 está respaldado por el acta de constitución. Lección: la línea base se congela y los estados se llevan en un documento aparte.

### Lo que no sé
- Por qué no hay documentos de enero a agosto de 2026.
- Quién emitió la v2 y con qué motivo.
- Si CC-01 llegó al comité fuera de las minutas que tengo.
- Si la factura FV-1267 se pagó.
- Si «Licenciamiento del motor» de CT-267 y de CT-243 son el mismo entregable cobrado en dos contratos o dos entregables distintos. Los documentos no lo aclaran.

Nada de esto dice que alguien ocultara algo: lo que hay es una carpeta que quedó callada durante ocho meses y que se llenó de golpe. Quién tiene esa conversación es una persona; esta historia es el insumo.

### Siguiente paso
Puedo llevar esta historia al comité (para la decisión de CC-01 y la línea base v2) o al cierre del proyecto. Sugiero llevarla al comité del 2026-10-20.

---
*Pie de rigor: borrador de trabajo, no decisión ni asesoría. Cada dato sale del documento citado en la línea de tiempo y la verificación es suya. Las cifras derivadas vienen de `portafolio.py compute`; las que el script no entrega no se escribieron.*

La corrida quedó registrada como `2026-10-17-project-history-1`, con la salida guardada en `estado/corridas/salida-project-history.md`.