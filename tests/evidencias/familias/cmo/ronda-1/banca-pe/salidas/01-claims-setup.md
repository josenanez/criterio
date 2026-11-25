# /criterio-claims:claims-setup mercadeo/20603335551-banco-altiplano-sintetico

Lucía quedó instalada sobre Banco Altiplano Sintético (RUC 20603335551, Perú) para el periodo 2026-10. Procesé las 6 piezas, los 4 soportes y las bases de las 2 promociones. Este reporte solo muestra lo de las afirmaciones. El cálculo también dio una promoción sin condiciones publicadas y una pieza pagada que no se identifica como publicidad. Esas dos las muestran `/criterio-claims:promo-check` y `/criterio-claims:approval-check`.

# Cada afirmación con su soporte · Banco Altiplano Sintético · periodo 2026-10

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |

## El resultado

| Pieza | Afirmación | Soporte | En la carpeta | Comparativa | Fuente citada |
|---|---|---|---|---|---|
| P-01 | Entrega en 24 horas en las ciudades principales. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-02 | El precio más bajo del mercado en la canasta básica. | `20-soportes/comparativo_de_precios_2026-10.pdf` | sí | sí | Comparativo de precios de un tercero independiente, octubre de 2026 |
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

- `10-piezas/pieza_P-03.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---

- **Configuración:** `.criterio/piezas/20603335551/config.json`
- **Aceptación de los términos 1.6:** por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-claims-0.1.0-2026-11-25.md` y en `.pdf`.
- **Marca:** `_CRITERIO_MERCADEO.txt` quedó en la carpeta de la entidad.
- **Corrida registrada:** `2026-11-25-claims-setup-1`, con 3 hallazgos.

**Cuándo vuelvo:** no quedó tarea programada, porque en esta sesión de prueba nadie podía dar el sí explícito que hace falta para crearla. Para correrlo a mano: `/criterio-claims:claims-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.