# /criterio-claims:claims-setup mercadeo/901333555-almacenes-del-valle-sinteticos

Lucía quedó configurada sobre Almacenes del Valle Sintéticos (NIT 901333555, Colombia, periodo 2026-10). La primera revisión encontró 2 afirmaciones que hay que atender: P-03 no tiene soporte y P-02 compara con la competencia sin citar su fuente.

- **Configuración:** `.criterio/piezas/901333555/config.json`.
- **Términos:** quedó registrada la aceptación de José Francisco Ñáñez (versión 1.6, 2026-11-25). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-claims-0.1.0-2026-11-25.md` y en `.pdf`.
- **Marca:** dejé `_CRITERIO_MERCADEO.txt` en la carpeta de la entidad.

Crucé las 6 piezas contra los 4 soportes y procesé las bases de las 2 promociones. El cálculo del periodo encontró en total 6 señales. Las otras 4 no salen en este reporte de afirmaciones: una pieza publicada sin aprobación previa, una base de contactos sin autorización, una promoción sin todas sus condiciones y una pieza pagada que no se identifica como publicidad. Las detallan `/criterio-claims:approval-check` y `/criterio-claims:promo-check`.

Una decisión que legal puede querer revisar: la frase de la creadora en P-04 («Mi pedido llegó al día siguiente.») la registré como una afirmación sobre el plazo y la crucé contra los tiempos de entrega.

# Cada afirmación con su soporte · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |
| 2 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |

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

---

**Reloj:** no creé la tarea diaria porque en esta prueba nadie dio un sí explícito. A mano se corre con `/criterio-claims:claims-wake`.
**Cuándo vuelvo:** sin reloj.

Registré la corrida como `2026-11-25-claims-setup-1`. Lo que mostré quedó en `estado-mercadeo/901333555-almacenes-del-valle-sinteticos/corridas/salida-claims-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.