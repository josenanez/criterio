# /criterio-claims:claims-setup mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico

Lucía quedó instalada sobre la entidad y la primera revisión de afirmaciones no encontró nada pendiente. Como nadie respondía en esta sesión, tomé las respuestas que sugerían los documentos. Lo que conviene confirmar está en las notas del final.

**Comprobante de aceptación de los términos (versión 1.6)** a nombre de José Francisco Ñáñez, con fecha 2026-11-25: `.criterio/terminos/aceptacion-criterio-claims-0.1.0-2026-11-25.md`, con su `.pdf` en la misma carpeta.

**Lo que quedó fijado:**
- **Entidad:** Consumo Control de Mercadeo Sintético, RFC CCM220101ZZ9.
- **País y moneda:** México y MXN. Lo deduje del formato del RFC; ningún documento lo dice.
- **Periodo:** 2026-10.
- **Tolerancias:** 5 % sobre el presupuesto y 2 % entre el resultado y la plataforma, tomadas de la política.
- **Rostrum:** sí.
- **Configuración:** `.criterio/piezas/CCM220101ZZ9/config.json`.
- **Estado:** `estado-mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico`.
- **Marca:** dejé `_CRITERIO_MERCADEO.txt` en la carpeta de la entidad.

Encontré cinco afirmaciones objetivas en las piezas y cada una tiene un soporte en `20-soportes/` que trata de lo mismo. Las dos promociones publican su vigencia y sus condiciones. P-04 es el testimonio de una creadora sobre su propio pedido, así que no la llevé a la ficha como afirmación de la marca.

# Cada afirmación con su soporte · Consumo Control de Mercadeo Sintético · periodo 2026-10

**Entidad:** Consumo Control de Mercadeo Sintético (CCM220101ZZ9) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claim-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Pieza | Afirmación | Soporte | En la carpeta | Comparativa | Fuente citada |
|---|---|---|---|---|---|
| P-01 | Entrega en 24 horas en las ciudades principales. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-02 | El precio más bajo del mercado en la canasta básica. | `20-soportes/comparativo_de_precios_2026-10.pdf` | sí | sí | Comparativo de precios de un tercero independiente, octubre de 2026 |
| P-03 | 9 de cada 10 clientes nos recomiendan. | `20-soportes/encuesta_de_satisfaccion_2026.pdf` | sí | no | — |
| P-05 | Fabricado en el país. | `20-soportes/certificado_de_origen.pdf` | sí | no | — |
| P-06 | La colección llega en tres colores. | `20-soportes/catalogo_de_la_coleccion.pdf` | sí | no | — |

Si el soporte basta lo decide legal: aquí se dice qué afirmación no tiene ninguno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---

**Notas:**
- **P-06:** el registro de piezas no la marca como pagada ni como identificada como publicidad, pero nombra a un influenciador. Este reporte no revisa eso: lo cubre `/criterio-claims:approval-check`.
- **Fuentes:** el pie del reporte dice «Sin documentos citados», aunque la tabla sí cita las piezas y los soportes. Parece un problema de cómo el motor arma ese pie.

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie podía darlo, así que no la creé. A mano se corre con `/criterio-claims:claims-wake`.

Corrida registrada como `2026-11-25-claims-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.