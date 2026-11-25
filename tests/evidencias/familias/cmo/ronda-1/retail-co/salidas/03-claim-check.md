# /criterio-claims:claim-check 

Los términos están vigentes (versión 1.6, aceptados por José Francisco Ñáñez el 2026-11-25). Dos afirmaciones quedan por atender. La decisión sobre ellas es de legal y de mercadeo.

# Cada afirmación con su soporte · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | `10-piezas/pieza_P-03.pdf` |
| 2 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | `10-piezas/pieza_P-02.pdf` |

## El resultado

| Pieza | Afirmación | Soporte | En la carpeta | Comparativa | Fuente citada |
|---|---|---|---|---|---|
| P-01 | Entrega en 24 horas en las ciudades principales. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-02 | El precio más bajo del mercado en la canasta básica. | `20-soportes/comparativo_de_precios_2026-10.pdf` | sí | sí | — |
| P-03 | 9 de cada 10 clientes nos recomiendan. | — | no | no | — |
| P-04 | Mi pedido llegó al día siguiente. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-05 | Fabricado en el país. | `20-soportes/certificado_de_origen.pdf` | sí | no | — |
| P-06 | La colección llega en tres colores. | `20-soportes/catalogo_de_la_coleccion.pdf` | sí | no | — |

Si el soporte basta lo decide legal: aquí se dice qué afirmación no tiene ninguno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- Fuentes técnicas: F-01, F-10 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-claim-check-1`. La salida completa está en `corridas/salida-claim-check.md`.