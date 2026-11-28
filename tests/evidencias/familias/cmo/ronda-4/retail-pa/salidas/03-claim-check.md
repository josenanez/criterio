# /criterio-claims:claim-check 

Corrí primero el periodo 2026-11 por error y salió vacío. El periodo de la configuración es 2026-10, y este es su reporte. Dejé en `piezas/2026-11/` un reporte vacío por ese error, y no lo borré.

# Cada afirmación con su soporte · Almacenes del Canal Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Canal Sintéticos (155634567-2-2020) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 1.1.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Afirmación de una pieza aprobada sin soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» | `10-piezas/pieza_P-03.pdf` |
| 2 | Afirmación de una pieza aprobada sin soporte en la carpeta de soportes (`claim_without_substantiation`) | P-12: «Atención en menos de 5 minutos en todas las sucursales.» | `10-piezas/pieza_P-12.pdf` |
| 3 | Comparativa sin fuente ni fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» La pieza no dice su fuente ni su fecha. | `10-piezas/pieza_P-02.pdf` |
| 4 | Comparativa sin fuente ni fecha (`comparative_claim_without_source`) | P-22: «Más barato que cualquier otra cadena en útiles escolares.» La pieza no dice su fuente ni su fecha. | `10-piezas/pieza_P-22.pdf` |

## El resultado

| Pieza | Afirmación | Soporte | En la carpeta | Comparativa | Fuente citada |
|---|---|---|---|---|---|
| P-01 | Entrega en 24 horas en las ciudades principales. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-02 | El precio más bajo del mercado en la canasta básica. | `20-soportes/comparativo_de_precios_2026-10.pdf` | sí | sí | — |
| P-03 | 9 de cada 10 clientes nos recomiendan. | — | no | no | — |
| P-04 | Mi pedido llegó al día siguiente. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-05 | Fabricado en el país. | `20-soportes/certificado_de_origen.pdf` | sí | no | — |
| P-06 | La colección llega en tres colores. | `20-soportes/catalogo_de_la_coleccion.pdf` | sí | no | — |
| P-12 | Atención en menos de 5 minutos en todas las sucursales. | — | no | no | — |
| P-22 | Más barato que cualquier otra cadena en útiles escolares. | `20-soportes/comparativo_de_utiles_2026-10.pdf` | sí | sí | — |
| P-32 | La tienda abre hasta las 10 de la noche. | `20-soportes/horarios_de_atencion.pdf` | sí | no | — |
| P-42 | Devoluciones en 30 días. | `20-soportes/politica_de_devoluciones.pdf` | sí | no | — |

Si el soporte basta lo decide legal: aquí se dice qué afirmación no tiene ninguno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Carpeta de la entidad? → mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos (única candidata)
- ¿Entidad, identificación fiscal y país? → Almacenes del Canal Sintéticos, 155634567-2-2020, PA, USD
- ¿Periodo? → 2026-10
- ¿Publicar en Rostrum? → Sí; la política no dice otra cosa
- ¿Dónde guardar el estado? → estado-mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos
- ¿Términos 1.6? → Aceptados por José Francisco Ñáñez, 2026-11-25
- ¿Marcar la carpeta? → Sí

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/pieza_P-12.pdf`
- `10-piezas/pieza_P-22.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-claim-check-1`, con la salida en `corridas/salida-claim-check.md`.