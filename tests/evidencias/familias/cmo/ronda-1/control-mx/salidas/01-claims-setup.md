# /criterio-claims:claims-setup mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico

Lucía quedó instalada sobre Consumo Control de Mercadeo Sintético (RFC CCM220101ZZ9). La primera revisión de octubre de 2026 no encontró nada que atender: cada afirmación de las seis piezas tiene un soporte que trata de lo mismo, y la única comparativa cita su fuente.

- **Configuración:** quedó en `.criterio/piezas/CCM220101ZZ9/config.json`. La entidad, el país (México) y las tolerancias (5 % sobre el presupuesto y 2 % entre el resultado y la plataforma) salen de la política de publicidad y del nombre de la carpeta.
- **Respuestas sugeridas que tomé:** la carpeta era la única candidata. El periodo es 2026-10, el del informe de resultados y del comparativo. Se publica en Rostrum porque la política no dice otra cosa. El estado se guarda en `estado-mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico`.
- **Términos:** registré la aceptación de la versión 1.6 a nombre de José Francisco Ñáñez. El comprobante está en `.criterio/terminos/aceptacion-criterio-claims-0.1.0-2026-11-25.md`, con su versión en `.pdf`.
- **Marca:** dejé `_CRITERIO_MERCADEO.txt` en la carpeta de la entidad.

Este reporte no cruza el registro de piezas ni el de bases de contactos; eso lo hace `/criterio-claims:approval-check`. El reporte del motor, tal cual:

---

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
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---

**Cuándo vuelvo:** no configuré la revisión diaria. Esta tarea pide un sí explícito, y en esta prueba nadie lo dio. Para revisar a mano, corre `/criterio-claims:claims-wake`.

Dejé la salida en `estado-mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico/corridas/salida-claims-setup.md` y la corrida quedó registrada como `2026-11-25-claims-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.