# /criterio-claims:claims-setup mercadeo/96789012-3-seguros-cordillera-sinteticos

Soy Lucía. Pongo cada afirmación al lado de su soporte y cada pieza al lado de su aprobación; no apruebo piezas ni juzgo la creatividad.

**Lo que se respondió** (sesión de prueba: tomé la respuesta sugerida por los documentos en cada caso):
- **Carpeta:** `mercadeo/96789012-3-seguros-cordillera-sinteticos`. Era la única que el motor encontró: tiene 00-politica/, 10-piezas/, 20-soportes/, 30-promociones/, 40-bases/ y 50-campanas/.
- **Entidad:** Seguros Cordillera Sintéticos, RUT 96789012-3, Chile, en pesos chilenos.
- **Periodo:** 2026-10.
- **Publicar en Rostrum:** sí, la opción por omisión, porque la política no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-mercadeo/96789012-3-seguros-cordillera-sinteticos`.
- **Términos 1.6:** los mostré tal cual y los aceptó José Francisco Ñáñez el 2026-11-25.
- **Marca de la carpeta:** sí, dejé `_CRITERIO_MERCADEO.txt` en ella.

**Dónde quedó:**
- **Configuración:** `.criterio/piezas/96789012-3/config.json`.
- **Comprobante de los términos:** `.criterio/terminos/aceptacion-criterio-claims-1.0.0-2026-11-25.md` y su `.pdf`.

Procesé las piezas, los soportes y las bases de las promociones. Dos afirmaciones no tienen soporte en la carpeta y dos comparativas no citan su fuente ni su fecha en la pieza. Si el soporte basta, lo decide legal.

# Cada afirmación con su soporte · Seguros Cordillera Sintéticos · periodo 2026-10

**Entidad:** Seguros Cordillera Sintéticos (96789012-3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 1.0.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |
| 2 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-12: «Atención en menos de 5 minutos en todas las sucursales.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-12.pdf` |
| 3 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |
| 4 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-22: «Más barato que cualquier otra cadena en útiles escolares.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-22.pdf` |

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

- ¿Cuál es la carpeta de la entidad? → mercadeo/96789012-3-seguros-cordillera-sinteticos, la única candidata
- ¿Entidad, identificación fiscal y país? → Seguros Cordillera Sintéticos, RUT 96789012-3, Chile (CLP)
- ¿Periodo? → 2026-10
- ¿Se publica en Rostrum? → Sí, por omisión; la política no dice otra cosa
- ¿Dónde se guarda el estado? → estado-mercadeo/96789012-3-seguros-cordillera-sinteticos
- ¿Acepta los términos 1.6? → Sí, José Francisco Ñáñez, 2026-11-25
- ¿Se marca la carpeta con _CRITERIO_MERCADEO.txt? → Sí

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/pieza_P-12.pdf`
- `10-piezas/pieza_P-22.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. La tarea programada solo se crea con un sí explícito, y en esta prueba nadie lo da. Para correrla a mano: `/criterio-claims:claims-wake`.

La corrida quedó registrada como `2026-11-25-claims-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.