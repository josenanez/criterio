# /criterio-claims:claims-setup mercadeo/cms210415xy3-consumo-maya-sintetico

Soy Lucía. Pongo cada afirmación al lado de su soporte y cada pieza al lado de su aprobación; no apruebo piezas ni juzgo la creatividad.

**Carpeta:** 1. `mercadeo/cms210415xy3-consumo-maya-sintetico`. Tiene 00-politica/, 10-piezas/, 20-soportes/, 30-promociones/, 40-bases/ y 50-campanas/. Era la única candidata, así que la tomé.

- **Entidad:** Consumo Maya Sintético, RFC CMS210415XY3, México (MXN). Lo tomé de la carpeta y de la política.
- **Periodo:** 2026-10, porque los soportes y el informe son de octubre.
- **Rostrum:** sí, porque la política no dice otra cosa.
- **Estado:** `estado-mercadeo/cms210415xy3-consumo-maya-sintetico`.
- **Términos 1.6:** los mostré tal cual. José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-claims-0.2.0-2026-11-25.md` y en el `.pdf` del mismo nombre.
- **Marca `_CRITERIO_MERCADEO.txt`:** sí, quedó en la carpeta.

**Configuración:** `.criterio/piezas/CMS210415XY3/config.json`.

Crucé las 10 piezas contra los 7 soportes. Dos afirmaciones no tienen soporte en la carpeta y dos comparativas no dicen en la pieza su fuente ni su fecha. El cálculo encontró además señales de aprobación, de identificación como publicidad, de bases de contactos y de promociones; esas aparecen en approval-check y promo-check.

---

# Cada afirmación con su soporte · Consumo Maya Sintético · periodo 2026-10

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.2.0 · **Comando:** `claim-check`

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

- ¿Entidad, identificación fiscal y país? → Consumo Maya Sintético, RFC CMS210415XY3, México (MXN), por la carpeta y la política
- ¿Periodo? → 2026-10, por los soportes y el informe de octubre
- ¿Se publica en Rostrum? → Sí; la política no dice otra cosa
- ¿Dónde se guarda el estado? → estado-mercadeo/cms210415xy3-consumo-maya-sintetico
- ¿Acepta los términos 1.6? → Sí, José Francisco Ñáñez, 2026-11-25
- ¿Se marca la carpeta con _CRITERIO_MERCADEO.txt? → Sí

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/pieza_P-12.pdf`
- `10-piezas/pieza_P-22.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---

## Cuándo vuelvo

Sin reloj: nadie dio un sí explícito a la tarea programada, y crearla lo requiere. Para correrlo a mano: `/criterio-claims:claims-wake`.

La corrida quedó registrada como `2026-11-25-claims-setup-1`.

Una nota de esta prueba: la primera llamada a `reporte` se cayó porque escribí las preguntas de la ficha como texto, y el motor las espera como `{question, answer}`. Las corregí, volví a calcular y el reporte salió.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.