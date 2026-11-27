# /criterio-claims:claims-setup mercadeo/901333555-almacenes-del-valle-sinteticos

Lucía quedó instalada para Almacenes del Valle Sintéticos (NIT 901333555) y la primera revisión del periodo 2026-10 está hecha. En las piezas hay **3 afirmaciones sin soporte** (P-03, P-12, P-13) y **3 comparaciones con la competencia que no dicen en la pieza su fuente ni su fecha** (P-02, P-22, P-23). Si el soporte basta lo decide legal.

El cálculo del periodo dio 18 señales en total. Las otras 12 son piezas publicadas sin aprobación, piezas pagadas a creadores sin identificarse como publicidad, bases de contactos sin autorización y promociones sin condiciones. No salen en el reporte de abajo: las muestran `/criterio-claims:approval-check` y `/criterio-claims:promo-check`.

- **Configuración:** `.criterio/piezas/901333555/config.json`, con el periodo 2026-10, publicación en Rostrum y las tolerancias de 5 % y 2 % de la política.
- **Términos:** los acepta José Francisco Ñáñez con fecha 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-claims-0.2.0-2026-11-25.md` y en `.pdf`.
- **Marca:** dejé `_CRITERIO_MERCADEO.txt` en la carpeta de la entidad.
- **Lo que encuentro se guarda en:** `estado-mercadeo/901333555-almacenes-del-valle-sinteticos`. La corrida quedó registrada como `2026-11-25-claims-setup-1`.

# Cada afirmación con su soporte · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.2.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |
| 2 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-12: «Atención en menos de 5 minutos en todas las sucursales.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-12.pdf` |
| 3 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-13: «Más de 500 puntos de atención en el país.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-13.pdf` |
| 4 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |
| 5 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-22: «Más barato que cualquier otra cadena en útiles escolares.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-22.pdf` |
| 6 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-23: «El envío más rápido del mercado.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-23.pdf` |

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
| P-13 | Más de 500 puntos de atención en el país. | — | no | no | — |
| P-22 | Más barato que cualquier otra cadena en útiles escolares. | `20-soportes/comparativo_de_utiles_2026-10.pdf` | sí | sí | — |
| P-23 | El envío más rápido del mercado. | `20-soportes/comparativo_de_envios_2026-10.pdf` | sí | sí | — |
| P-32 | La tienda abre hasta las 10 de la noche. | `20-soportes/horarios_de_atencion.pdf` | sí | no | — |
| P-33 | Tienen más de 200 referencias de café. | `20-soportes/catalogo_de_cafes.pdf` | sí | no | — |
| P-42 | Devoluciones en 30 días. | `20-soportes/politica_de_devoluciones.pdf` | sí | no | — |
| P-43 | Garantía de dos años en electrodomésticos. | `20-soportes/terminos_de_garantia.pdf` | sí | no | — |

Si el soporte basta lo decide legal: aquí se dice qué afirmación no tiene ninguno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/pieza_P-12.pdf`
- `10-piezas/pieza_P-13.pdf`
- `10-piezas/pieza_P-22.pdf`
- `10-piezas/pieza_P-23.pdf`
- Fuentes técnicas: F-01, F-10 (families/criterio-cmo/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión de prueba nadie lo dio, así que no la creé. Mientras tanto se corre a mano con `/criterio-claims:claims-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.