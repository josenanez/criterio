# /criterio-claims:claims-setup mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos

Lucía quedó configurada para Almacenes Control de Mercadeo Sintéticos (NIT 901444666) y la primera revisión, la del periodo 2026-10, no dejó nada abierto. Procesé las 6 piezas y las 2 promociones. Cada afirmación tiene en la carpeta un soporte sobre lo mismo, la pieza comparativa cita su fuente y las dos promociones publican su vigencia y sus condiciones. Si cada soporte basta lo decide legal.

- **Configuración:** quedó en `.criterio/piezas/901444666/config.json`. Tomé las respuestas sugeridas de los documentos: Colombia (COP), periodo 2026-10, las tolerancias de la política (5 % sobre el presupuesto y 2 % contra la plataforma), publicación en Rostrum y el estado en `estado-mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos`.
- **Términos:** quedan aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-claims-0.2.0-2026-11-25.md` y `.pdf`.
- **Marca:** dejé `_CRITERIO_MERCADEO.txt` en la carpeta de la entidad.

# Cada afirmación con su soporte · Almacenes Control de Mercadeo Sintéticos · periodo 2026-10

**Entidad:** Almacenes Control de Mercadeo Sintéticos (901444666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.2.0 · **Comando:** `claim-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Pieza | Afirmación | Soporte | En la carpeta | Comparativa | Fuente citada |
|---|---|---|---|---|---|
| P-01 | Entrega en 24 horas en las ciudades principales. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-02 | El precio más bajo del mercado en la canasta básica. | `20-soportes/comparativo_de_precios_2026-10.pdf` | sí | sí | Comparativo de precios de un tercero independiente, octubre de 2026 |
| P-03 | 9 de cada 10 clientes nos recomiendan. | `20-soportes/encuesta_de_satisfaccion_2026.pdf` | sí | no | — |
| P-04 | Mi pedido llegó al día siguiente. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-05 | Fabricado en el país. | `20-soportes/certificado_de_origen.pdf` | sí | no | — |
| P-06 | La colección llega en tres colores. | `20-soportes/catalogo_de_la_coleccion.pdf` | sí | no | — |

Si el soporte basta lo decide legal: aquí se dice qué afirmación no tiene ninguno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-10 (families/criterio-cmo/FUENTES.es.md)

---

**Reloj:** la tarea programada pide un sí explícito y en esta sesión de prueba nadie lo dio, así que no la creé. Para correrla a mano: `/criterio-claims:claims-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-claims-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.