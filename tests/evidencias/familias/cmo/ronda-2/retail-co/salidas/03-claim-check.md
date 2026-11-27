# /criterio-claims:claim-check 

Corrí el reporte de 2026-11 y salió vacío, porque ese periodo no tiene ficha. Los datos están en 2026-10, así que te muestro ese. La decisión sobre cada punto es de legal y del área de mercadeo.

# Cada afirmación con su soporte · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Agente:** Lucía, versión 0.2.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Afirmación sin soporte en la carpeta (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» | `10-piezas/pieza_P-03.pdf` |
| 2 | Afirmación sin soporte en la carpeta (`claim_without_substantiation`) | P-12: «Atención en menos de 5 minutos en todas las sucursales.» | `10-piezas/pieza_P-12.pdf` |
| 3 | Afirmación sin soporte en la carpeta (`claim_without_substantiation`) | P-13: «Más de 500 puntos de atención en el país.» | `10-piezas/pieza_P-13.pdf` |
| 4 | Comparativa sin fuente ni fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» | `10-piezas/pieza_P-02.pdf` |
| 5 | Comparativa sin fuente ni fecha (`comparative_claim_without_source`) | P-22: «Más barato que cualquier otra cadena en útiles escolares.» | `10-piezas/pieza_P-22.pdf` |
| 6 | Comparativa sin fuente ni fecha (`comparative_claim_without_source`) | P-23: «El envío más rápido del mercado.» | `10-piezas/pieza_P-23.pdf` |

## El resultado

Hay 14 afirmaciones revisadas. Las tres sin soporte son P-03, P-12 y P-13. Las tres comparativas (P-02, P-22 y P-23) tienen un soporte en la carpeta, pero la pieza no cita su fuente ni su fecha. Las otras ocho tienen soporte en la carpeta y no son comparativas: P-01, P-04, P-05, P-06, P-32, P-33, P-42 y P-43.

Todo lo que llegó se procesó. El comando no hizo preguntas.

**Fuentes:** las seis piezas señaladas en `10-piezas/` y las fuentes técnicas F-01 y F-10.

La corrida quedó registrada como `2026-11-25-claim-check-1`. La salida completa está en `corridas/salida-claim-check.md`, dentro de la carpeta de estado. No tuve que aceptar términos porque ya estaban vigentes (versión 1.6).

Al mostrarte el reporte resumí la tabla de resultados: quité las columnas de soporte, carpeta, comparativa y fuente, y dejé solo las pruebas con señal. El archivo guardado trae el reporte completo del motor.