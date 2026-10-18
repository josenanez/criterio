# /criterio-portfolio:vendor-tracking PRY-200

# Proveedores — PRY-200 Crédito de libranza digital, al 2026-10-18

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo. El informe sale de seis documentos del proyecto: el contrato CT-892, el acta de constitución, el cronograma v1, la factura FV-1892, el acta de recibo del piloto y el informe de avance del 2026-10-13. Las cifras derivadas las copié de `compute`.

**Proveedor:** Talento Solidario Ltda., contrato CT-892.

| Entregable | Fecha | Monto COP | Estado | Evidencia |
|---|---|---|---|---|
| Licenciamiento del módulo | 2026-01-29 | 823.489.299 | sin dato (`unknown`) | ninguna; vencido hace 262 días |
| Bolsa de horas de desarrollo | 2026-03-30 | 823.489.299 | `pending` | ninguna; vencido hace 202 días |
| Parametrización de líneas de crédito | 2026-05-30 | 823.489.299 | "recibido" en el contrato | ninguna |
| Mesa de ayuda del primer trimestre | 2026-07-29 | 823.489.299 | sin dato (`unknown`) | ninguna; vencido hace 81 días |

**Facturación.** La factura FV-1892 (2026-09-25) cobra 1.002.986.926 COP y está radicada en cuentas por pagar. No dice qué entregables cobra. Ninguno de los cuatro tiene acta de recibo, aunque el contrato exige una por entregable, firmada por el gerente del proyecto.

- **Diferencia:** facturado menos aceptado es 179.497.627 COP. El script cuenta como aceptada la parametrización, que solo el contrato dice "recibido". Si se exige acta, lo aceptado con evidencia es 0.
- **Acta del piloto:** la única acta de la carpeta recibe el "Piloto con asociados". Eso es un hito del cronograma, no un entregable de CT-892.
- **Hitos:** cuatro de los cinco figuran cerrados sin evidencia: diseño funcional, ambiente de pruebas, integración con el core y salida a producción. Solo el piloto tiene acta.
- **Avance:** el cronograma marca los cinco hitos como cerrados (100 %) y el informe declara 67 %. La diferencia es de 33 puntos.

**Sin dato.**
- El contrato no trae vigencia, renovación ni preaviso. No puedo decir si hay un preaviso por vencer.
- La carpeta no tiene reuniones con el proveedor, así que no puedo afirmar ni descartar compromisos vencidos.
- No hay fecha de pago de la factura.

**Siguiente paso.** Sugiero frenar el pago de FV-1892 hasta tener las actas o el desglose de la factura. Puedo llevarlo al comité del 2026-10-25 como entregables facturados sin evidencia. También hay que pedir el contrato completo con su vigencia y preaviso.

El informe quedó en `estado/corridas/salida-vendor-tracking.md` y la corrida en `2026-10-18-vendor-tracking-1`. La corrida contó 13 proyectos y 65 hallazgos; los de PRY-200 son 11.