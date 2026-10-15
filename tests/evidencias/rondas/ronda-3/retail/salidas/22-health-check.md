# /criterio-portfolio:health-check PRY-205

# Diagnóstico · PRY-205 Pago con QR en caja · 2026-10-15

Los términos ya estaban vigentes (v1.1), aceptados por José Francisco Ñáñez el 2026-10-15, así que no tuve que registrarlos de nuevo.

**Leí:** 7 documentos, del 2025-09-07 al 2026-10-14: 3 docx, 3 md y 1 csv. No hubo ninguno ilegible. Ninguna minuta de otro proyecto menciona PRY-205 ni "QR".

**Dictamen:** de 14 afirmaciones, 3 están sostenidas, 7 sin sustento y 4 contradichas.

Desde esta carpeta se puede afirmar el gobierno nominal, el presupuesto aprobado y un único recibo. El recibo es el del hito "Ambiente de pruebas certificado". No se puede afirmar que el proyecto esté en verde. El informe del 2026-10-14 lo declara verde con 37% de avance, y `compute` encuentra 5 señales abiertas que el informe no explica.

**Contradicciones**
- **Estado verde:** las 5 señales son un compromiso vencido, hitos cerrados sin evidencia, avance contra plan, entregables del proveedor vencidos y una factura sin entrega.
- **Avance de 37%:** el cronograma marca 4 de 5 hitos cerrados, lo que sostiene entre 80% y 100%. La brecha es de 43,0 puntos.
- **Fecha de cierre:** el acta dice 2027-01-16 y el cronograma dice 2026-12-03. Ningún documento aclara cuál rige, y la desviación de 0 días solo vale si rige el 2026-12-03.
- **Factura FV-1377:** vale 247.703.694 COP y está radicada en cuentas por pagar. El contrato CT-377 exige un acta de recibo firmada por entregable. No hay ninguna acta de recibo de entregables del contrato, y 0 entregables están aceptados.

**Hitos y proveedor**
- **Hitos sin evidencia:** tres hitos aparecen cerrados sin documento que lo pruebe: Diseño (299 días desde su fecha), Integración con el ERP (125) y Piloto en tiendas (38).
- **Entregables vencidos:** los 4 entregables de CT-377 siguen pendientes, con atrasos de 290, 194, 99 y 3 días.

**Dinero (COP)**

| | |
|---|---|
| Aprobado | 4.200.000.000 |
| Comprometido | 3.065.681.148 (73,0%) |
| Ejecutado | 2.002.590.000 (47,7%) |
| Proyección | 3.958.059.174 (−5,8% frente a lo aprobado) |
| Disponible real | 1.134.318.852 |

Solo el aprobado tiene respaldo en el acta. Las otras tres cifras vienen únicamente del informe de avance.

**Gobierno y compromisos**
- **Autoridad del gerente:** el acta no la declara. Sin ella, ninguna fecha vigente cuenta como desviación aprobada.
- **Compromiso de Sandra Gil:** debía entregar "el punto 37" el 2026-10-01 y lleva 14 días vencido. Ningún documento define qué es ese punto, y ella no aparece entre los asistentes de la minuta.
- **Riesgos y dependencias sin registro:** los dos riesgos del informe no están en ningún registro RAID. El acta dice "ninguna dependencia" aunque el proyecto depende de un proveedor con cuatro entregables.

**No recomiendo detener, continuar ni reestructurar.** Eso lo decide quien tiene la facultad. Puedo llevar las 4 contradicciones al gerente como preguntas, una por una, o preparar el punto de comité con la lista de lo que falta.

**Corrida registrada:** 2026-10-15-health-check-1, con la salida completa en `estado/corridas/salida-health-check.md`. `compute` y la corrida cubren los 13 proyectos del portafolio. El diagnóstico solo cubre PRY-205.