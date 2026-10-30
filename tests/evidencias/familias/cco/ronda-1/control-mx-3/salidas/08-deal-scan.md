# /criterio-revenue:deal-scan 

Tres cotizaciones nuevas (COT-1601, COT-1602 y COT-1603) quedaron en la ficha del periodo, y el motor no levantó ninguna señal sobre ellas.

# Qué cambió en lo vendido · Comercial Control de México · periodo 2026-10

**Entidad:** Comercial Control de México (CCM101010AB3) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.1.0 · **Comando:** `deal-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Cotizaciones en la ficha:** 3 · **Exportación:** `10-crm/oportunidades-2026-11-03.xlsx`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Quién aprobó el descuento de COT-1601? → Nadie por escrito: la cotización dice «Descuento dentro del nivel sin aprobación», así que la aprobación queda vacía

## Fuentes

- Sin documentos citados.

---

- **Términos:** ya estaban vigentes y registrados a nombre de José Francisco Ñáñez, con fecha 2026-11-05.
- **Configuración:** había dos, `ingresos` y `comercial`. Usé la de `ingresos`, que es la de este comando.
- **Ficha:** `ingresos/2026-10/ficha.json` no existía. La creé con las tres cotizaciones.
- **Aprobaciones:** COT-1602 la aprobó Marta Gil, gerente comercial, el 2026-10-05. COT-1603 la aprobó Ricardo Paz, gerente general, el 2026-10-20. COT-1601 queda sin aprobación porque nadie la dio por escrito.
- **Pendiente:** este comando no revisa los descuentos contra la matriz. Eso lo hace `/criterio-revenue:discount-check`.
- **Corrida:** la salida quedó en `corridas/salida-deal-scan.md` y la corrida se registró como `2026-11-05-deal-scan-1`, con 0 hallazgos.