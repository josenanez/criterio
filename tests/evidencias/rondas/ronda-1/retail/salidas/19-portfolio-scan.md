# /criterio-portfolio:portfolio-scan 

Terminé el barrido. Leí 38 de los 55 documentos y dejé 10 fichas actualizadas y selladas.

**Qué hice:** los términos ya estaban aceptados (v1.0, igual que `TERMS.md`). Seguí el plan de lectura tal cual: un lote de 10 proyectos, `workers: 1`, nada diferido. Ningún documento fue ilegible.

**Qué cambió:**
- **Fichas:** PRY-199, 200, 201, 202, 204, 205, 206, 207, 209 y 210.
- **Sin cambio:** PRY-203, 208 y 211 no se tocaron; sus 17 documentos no cambiaron y no se releyeron.
- **`entrada/`:** no existe, así que no se movió nada.

**Qué dejó el cálculo del script:** 37 hallazgos sobre los 13 proyectos, y 11 de ellos caen en PRY-203, 208 y 211, que no toqué. Los principales:
- **Hitos cerrados sin acta de recibo:** 17, en 201, 203, 205, 206, 208, 209 y 210.
- **Avance contra plan:** 6 hallazgos, en 201, 203, 205, 206, 209 y 211.
- **Declarado contra evidencia:** 5 hallazgos, en 203, 206, 208, 210 y 211.
- **Compromisos vencidos:** 2, en PRY-203 y PRY-208.
- **Otros:** hitos vencidos en 205 y 210; entregable de proveedor tarde en 206; sobrecosto y silencio en 210; compromiso sin fecha y contraste con la ficha del gerente en 211.

**Campos sin dato:**
- `authority` y `phase` en los 10 proyectos.
- `product` en PRY-202, 206, 209 y 210.
- Hitos en PRY-202, 204 y 207, porque no hay cronograma en la carpeta.
- Lo facturado en PRY-199.

**Para mirar:**
- **PRY-211:** el plan marcó 10 citas de `pm_record` que no resuelven desde la raíz de documentos. La ficha del gerente cita la ruta relativa al proyecto. No la toqué: es su ficha, no la mía.
- **Cierres comprometidos pasados:** PRY-201 (2026-08-19), PRY-202 (2026-09-14) y PRY-209 (2026-06-26) siguen reportando avance del 77 %, 58 % y 78 %.
- **PRY-207:** tiene una solicitud de cambio pendiente (CC-01: +90 días, +180 M COP) y ejecutado mayor que comprometido.
- **PRY-206:** la factura FV-1140 por 252.927.117 COP no nombra a qué entregable corresponde.

**Corrección a la salida guardada:** `estado-portafolio/corridas/salida-portfolio-scan.md` no incluye los 37 hallazgos, porque los calculó el script después de escribirla. Tampoco incluye el dato de 17 hitos sin acta en todo el portafolio. Dice que se leyeron 38 y quedaron 17 sin cambio; esas cifras son del plan, y el registro final ya cuenta los 55 como vistos. Si quieres que la salida quede completa, la actualizo y registro la corrida otra vez.

Los registros de la corrida están en `estado-portafolio/corridas/` (id `2026-10-14-portfolio-scan-1`). Siguiente paso, si lo quieres: `/criterio-portfolio:portfolio-report` para el informe consolidado.