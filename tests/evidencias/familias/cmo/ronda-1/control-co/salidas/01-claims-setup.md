# /criterio-claims:claims-setup mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos

Soy Lucía. Pongo cada afirmación al lado de su soporte y cada pieza al lado de su aprobación; no apruebo piezas ni juzgo la creatividad.

**Carpeta:** encontré una sola carpeta posible, `mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos`. Tiene las seis subcarpetas, de `00-politica/` a `50-campanas/`, y la tomo. Hay 20 documentos; ninguno está fuera de lugar y todos se pudieron procesar.

**Respuestas, sacadas de los documentos:**
- **Entidad:** Almacenes Control de Mercadeo Sintéticos, NIT 901444666. El nombre sale de la política de publicidad y el NIT del nombre de la carpeta. El país, Colombia (COP), no lo dice ningún documento: lo supuse por el formato del NIT.
- **Periodo:** 2026-10. En ese mes se publicaron las piezas y ese es el mes del comparativo de precios y del informe de resultados.
- **Publicar en Rostrum:** sí, porque la política no dice lo contrario.
- **Dónde guardo lo que encuentro:** `estado-mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos`.
- **Tolerancias:** según `00-politica/politica_de_publicidad.pdf`, la pauta puede pasar el presupuesto hasta en un 5 %, y un resultado puede diferir de la plataforma hasta en un 2 %.
- **Archivo `_CRITERIO_MERCADEO.txt` en la carpeta:** sí, para que se reconozca a primera vista.

**Términos (versión 1.6):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-claims-0.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre.

**Configuración:** quedó en `.criterio/piezas/901444666/config.json` y pasó la validación sin problemas. La carpeta quedó marcada.

**Primera ficha:** procesé las 6 piezas de `10-piezas/` y las bases de las 2 promociones de `30-promociones/`, y crucé cada afirmación contra los documentos de `20-soportes/`. Cada afirmación tiene un soporte que trata de lo mismo. La de P-04 es el testimonio de una creadora de contenido; la crucé contra los tiempos de entrega, pero puedo sacarla de la ficha.

# Cada afirmación con su soporte · Almacenes Control de Mercadeo Sintéticos · periodo 2026-10

**Entidad:** Almacenes Control de Mercadeo Sintéticos (901444666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claim-check`

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

**Cuándo vuelvo:** sin reloj. En esta sesión nadie dio un sí explícito a una tarea programada, así que se corre a mano con `/criterio-claims:claims-wake`.

**Falta revisar las aprobaciones:** este reporte no revisa si cada pieza tiene su aprobación y se identifica como publicidad, ni si cada base de contactos tiene su autorización. Eso lo revisa `/criterio-claims:approval-check`. En el registro de piezas, P-06 tiene un influenciador (`@creador_sintetico`) pero está marcada como no pagada y como no identificada como publicidad. Esa pieza es la primera que hay que revisar ahí.

La corrida quedó registrada como `2026-11-25-claims-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.