# /criterio-revenue:deal-scan 

Las tres cotizaciones de `40-cotizaciones/` están en la ficha del periodo, y el motor marcó 2 señales, las dos de comisión. No había documentos nuevos desde la corrida anterior. Los términos (v1.3) ya estaban vigentes con la aceptación de José Francisco Ñáñez del 2026-11-05, así que no registré nada nuevo.

**Cotizaciones en la ficha** (`ingresos/2026-10/ficha.json`):
- **COT-1601:** el documento dice que el descuento está dentro del nivel sin aprobación, así que la aprobación quedó vacía.
- **COT-1602:** con la aprobación escrita de Marta Gil.
- **COT-1603:** con la aprobación escrita de Ricardo Paz.

**Señales** (las calcula el motor):
- **Óscar Delgado:** se liquidaron 37,800.00 y el plan da 0.00 sobre lo ganado y facturado (`50-comisiones/liquidacion-2026-10.csv`, fila 3).
- **Isabel Méndez:** se liquidaron 25,200.00 y el plan da 0.00 sobre lo ganado y facturado (fila 2).

**Sin procesar:** una oportunidad ganada trae la cuenta «(sin cuenta)», que no está en la tabla de cuentas, y sin su identificación no se cruza.

**Archivos:**
- El reporte, tal cual, está en `ingresos/2026-10/reporte-deal-scan.md`.
- Lo mostrado quedó en `corridas/salida-deal-scan.md`.
- La corrida quedó registrada como `2026-11-05-deal-scan-1`.

La única pregunta del flujo fue el periodo: tomé 2026-10, el de la configuración.