# /criterio-product:product-wake 

## Microseguros (PRD-306) · 2026-10-17

Esta es la primera corrida y no había corte anterior. Por eso todo lo abierto cuenta como línea base. Desde hoy solo se reportará lo que cruce un umbral después de este corte. Los términos ya estaban vigentes (v0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo.

Tocaba `review`. No tocaba `report`, porque `committee_next` está vacío en la configuración.

**Lo que necesita decisión**
- **REQ-4606, 4608 y 4610** llevan 181, 169 y 103 días en «propuesto» sin que nadie los decida. Falta saber quién tiene la facultad de decidirlos. Propongo llevarlos al Comité de producto.
- **El supuesto «La demanda declarada se sostiene sin campaña»** lleva 166 días sin verificarse, con un umbral de 30. Para verificarlo hace falta medir la demanda en un periodo sin campaña. Ya pasó el punto en que conviene tratarlo como riesgo registrado.
- **El volumen mensual** está declarado en 140.572 en el caso de negocio y medido en 99.900 en el tablero del 2026-10-07. La diferencia es de 28,9 %, con un umbral de 20 %.

**Aceptado sin sustento**
- **Sin evidencia de demanda:** REQ-4605 y 4613.
- **Sin criterio de aceptación:** REQ-4602, 4609 y 4611.
- **Sin doliente:** REQ-4612.
- **Evidencia de 12 meses (entrevista del 2025-09-25):** 10 requerimientos, de REQ-4600 a REQ-4612 salvo 4605, 4606 y 4608. Esa entrevista habla de una «necesidad principal» y no nombra ninguno de ellos.

**Trazas**
Ninguno de los 11 requerimientos aceptados tiene proyecto. Leí las 13 fichas (PRY-199 a PRY-211) y ninguna nombra PRD-306 ni Microseguros. No hay traza que confirmar. Eso no prueba que nadie lo construya, solo que ninguna ficha lo declara.

**Lo que no sé**
No sé el criterio de éxito, porque no está dicho en ningún documento. Tampoco sé si se construye algo fuera de lo que declaran las fichas.

El corte quedó guardado en `snapshots/2026-10-17.json`. La salida está en `estado-producto/PRD-306/corridas/salida-product-wake.md` y la corrida quedó registrada como `2026-10-17-product-wake-1`. Tardó 25 segundos.

**Vuelvo el 2026-11-16.**