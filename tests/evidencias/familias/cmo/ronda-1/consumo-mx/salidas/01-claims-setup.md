# /criterio-claims:claims-setup mercadeo/cms210415xy3-consumo-maya-sintetico

Soy Lucía. Pongo cada afirmación al lado de su soporte y cada pieza al lado de su aprobación; no apruebo piezas ni juzgo la creatividad.

**Carpeta:** encontré una sola candidata, `mercadeo/cms210415xy3-consumo-maya-sintetico`. Tiene 00-politica/, 10-piezas/, 20-soportes/, 30-promociones/, 40-bases/ y 50-campanas/. Trabajé sobre esa.

**Respuestas que tomé de los documentos:**
- **Entidad:** Consumo Maya Sintético, RFC CMS210415XY3, México (MXN). Sale de la política y del nombre de la carpeta.
- **Periodo:** 2026-10, el mes de las publicaciones del registro de piezas y del comparativo de precios.
- **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
- **Dónde guardo el estado:** `estado-mercadeo/cms210415xy3-consumo-maya-sintetico`.
- **Tolerancias de la política:** 5 % sobre el presupuesto y 2 % entre un resultado y la plataforma.
- **Marca `_CRITERIO_MERCADEO.txt`:** sí.

**Términos (versión 1.6):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25.
- **Comprobante:** `.criterio/terminos/aceptacion-criterio-claims-0.1.0-2026-11-25.md` y `.pdf`.
- **Configuración:** `.criterio/piezas/CMS210415XY3/config.json`.
- La carpeta quedó marcada.

**Primera ficha:** procesé 6 piezas, 5 soportes y las bases de 2 promociones.
- Las seis afirmaciones tienen un soporte en la carpeta.
- La pieza P-02 hace una comparación y no dice en la misma pieza su fuente ni su fecha.
- El cálculo del periodo dejó además una pieza publicada sin aprobación previa y una base de contactos sin autorización. Las detalla `/criterio-claims:approval-check`.

# Cada afirmación con su soporte · Consumo Maya Sintético · periodo 2026-10

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claim-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |

## El resultado

| Pieza | Afirmación | Soporte | En la carpeta | Comparativa | Fuente citada |
|---|---|---|---|---|---|
| P-01 | Entrega en 24 horas en las ciudades principales. | `20-soportes/tiempos_de_entrega.xlsx` | sí | no | — |
| P-02 | El precio más bajo del mercado en la canasta básica. | `20-soportes/comparativo_de_precios_2026-10.pdf` | sí | sí | — |
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

- `10-piezas/pieza_P-02.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. Una tarea programada necesita un sí explícito, y en esta sesión nadie podía darlo. Para correrlo a mano: `/criterio-claims:claims-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.