# /criterio-portfolio:vendor-tracking PRY-203

Corrida terminada y registrada. Este es el resultado para PRY-203 Open Banking, proveedor Datacore Colombia, contrato CT-948.

**Hallazgo principal:** hay una factura de 631.036.273 COP (FV-1948, del 2026-09-15) radicada en cuentas por pagar y no hay ningún entregable aceptado. El contrato dice que cada entregable se factura contra un acta de recibo firmada por la gerente del proyecto, y esa acta no está en la carpeta.

| Entregable | Fecha comprometida | Atraso | Estado | Evidencia |
|---|---|---|---|---|
| Licenciamiento del motor | 2026-05-17 | 150 días | `pending` | ninguna |
| Bolsa de horas de desarrollo | 2026-07-26 | 80 días | `pending` | ninguna |
| Parametrización del tarifario | 2026-10-03 | 11 días | `pending` | ninguna |

- **Cifras del script:** 3 entregables, 0 aceptados, 3 vencidos sin evidencia y 0 declarados entregados sin documento.
- **Informe de avance:** el del 2026-10-12 no menciona ni al proveedor, ni la factura, ni los atrasos.
- **Compromisos del proveedor:** no hay ninguno vencido. El único compromiso registrado es de Laura Vélez, "Entregar el punto 30", para el 2026-10-28. No consta que sea del proveedor.
- **Sin dato:**
  - La vigencia y el preaviso de CT-948: el contrato no los trae. Con CC-01 el cierre del proyecto se movió de 2026-11-16 a 2027-03-08, así que conviene revisarlos.
  - A cuál entregable corresponde la factura: dice solo "Entregables del contrato CT-948" y el valor es igual al de cada uno.
  - Si la factura ya se pagó.
  - Si CC-01 toca el contrato con Datacore: no lo verifiqué.
- **Recomendación:** llevarlo al comité del 2026-10-20, antes de que se pague. Pedir el acta de recibo a María Restrepo, o que confirme que no existe, y pedir el contrato completo.

No abrí el acta de constitución (.docx). Los dos PDF los leí con `pdftotext`.

Los términos están aceptados desde 2026-10-14 (v1.0, a nombre de José Francisco Ñáñez).

El informe completo está en `/home/claude/banco/ronda-1/bancos/espacio/estado/corridas/salida-vendor-tracking.md`. La corrida quedó registrada como `2026-10-14-vendor-tracking-1`.