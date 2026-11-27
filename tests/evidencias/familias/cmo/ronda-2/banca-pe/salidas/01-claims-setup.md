# /criterio-claims:claims-setup mercadeo/20603335551-banco-altiplano-sintetico

Lucía quedó configurada para el Banco Altiplano Sintético (RUC 20603335551, Perú), periodo 2026-10. El reporte de soportes trae 6 señales: 3 afirmaciones sin soporte y 3 comparativas cuya pieza no dice su fuente ni su fecha.

- **Configuración:** quedó en `.criterio/piezas/20603335551/config.json`, con tolerancias de 5 % sobre el presupuesto y 2 % frente a la plataforma, tomadas de la política. Se publica en Rostrum.
- **Términos 1.6:** registré la aceptación de José Francisco Ñáñez con fecha 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-claims-0.2.0-2026-11-25.md` y `.pdf`.
- **Marca:** dejé `_CRITERIO_MERCADEO.txt` en la carpeta de mercadeo.
- **Las demás señales:** el motor encontró 18 en total. Las otras 12 son de aprobación, de identificación como publicidad, de bases de contactos y de condiciones de las promociones. Las muestran `/criterio-claims:approval-check` y `/criterio-claims:promo-check`.
- **Cuándo vuelvo:** sin reloj. En esta sesión de prueba nadie dio un sí explícito a la tarea programada. A mano se corre con `/criterio-claims:claims-wake`.

---

# Cada afirmación con su soporte · Banco Altiplano Sintético · periodo 2026-10

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.2.0 · **Comando:** `claim-check`

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

- Entidad, identificación fiscal y país → Banco Altiplano Sintético, RUC 20603335551, PE (de la política de publicidad y la carpeta)
- Periodo → 2026-10 (de los comparativos y el informe de resultados)
- ¿Se publica en Rostrum? → Sí (por omisión; la política no dice otra cosa)
- Dónde se guarda el estado → estado-mercadeo/20603335551-banco-altiplano-sintetico
- Términos 1.6 → Aceptados por José Francisco Ñáñez el 2026-11-25
- ¿Se marca la carpeta con _CRITERIO_MERCADEO.txt? → Sí

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/pieza_P-12.pdf`
- `10-piezas/pieza_P-13.pdf`
- `10-piezas/pieza_P-22.pdf`
- `10-piezas/pieza_P-23.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---

Corrida registrada como `2026-11-25-claims-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.