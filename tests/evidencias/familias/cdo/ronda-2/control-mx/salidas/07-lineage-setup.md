# /criterio-data-quality:lineage-setup datos/rcc200101cd2-retail-control-de-datos-sintetico

Soy Ariadna. Sigo cada cifra de los informes hasta su fuente, su corte y su linaje; no corrijo cifras.

**Carpeta:** solo había una candidata y la tomé: `datos/rcc200101cd2-retail-control-de-datos-sintetico`. Ya tenía la marca `_CRITERIO_DATOS.txt` (Retail Control de Datos Sintético · RFC RCC200101CD2) y sigue la estructura de carpetas. Tiene 11 documentos; ninguno está fuera de lugar ni es ilegible.

**Respuestas que tomé de los documentos y del setup que ya hizo Custodia:**
- **Entidad:** Retail Control de Datos Sintético, RFC RCC200101CD2, México (MXN).
- **Periodo:** 2026-11.
- **Tolerancia:** 0.5 %. Sale de `00-referencia/politica_de_datos.pdf`: «Una cifra de un informe de dirección no puede diferir de su fuente en más del 0.5 % al mismo corte».
- **Publicar en Rostrum:** sí, porque la política de datos no dice lo contrario.
- **Dónde guardo lo que encuentro:** `estado-datos/rcc200101cd2-retail-control-de-datos-sintetico`.
- **Marca:** la carpeta ya estaba marcada, así que no volví a marcarla.

**Términos (versión 1.6, 2026-11-16):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-data-quality-0.2.0-2026-11-25.md` y en su `.pdf`. La configuración está en `.criterio/calidad/RCC200101CD2/config.json` y el motor la validó sin problemas.

**Primera ficha:** procesé `20-informes/informe_junta_2026-10.pdf`, pasé sus 4 cifras a la ficha y las crucé contra `30-calidad/cifras_fuente.xlsx`. Todas quedan dentro de la tolerancia. Ventas netas no es idéntica a su fuente, pero también cabe.

# Cada cifra contra su fuente · Retail Control de Datos Sintético · periodo 2026-11

**Entidad:** Retail Control de Datos Sintético (RCC200101CD2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `figure-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Informe | Indicador | Corte | En el informe | En la fuente | Estado |
|---|---|---|---|---|---|
| `20-informes/informe_junta_2026-10.pdf` | Cartera vencida | 2026-10-31 | 1,250,000,000 | 1,250,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Clientes activos | 2026-10-31 | 84,200 | 84,200 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Ventas netas | 2026-10-31 | 9,420,000,000 | 9,400,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Margen operacional | 2026-10-31 | 3,400,000,000 | 3,400,000,000 | coincide |

Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con su fuente.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-02 (families/criterio-cdo/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. Crear la tarea programada pide un sí explícito, y en esta sesión de prueba nadie podía darlo. A mano se corre con `/criterio-data-quality:lineage-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---

**Para la prueba:**
- **Corrida registrada:** `2026-11-25-lineage-setup-1`, y la salida está en `estado-datos/rcc200101cd2-retail-control-de-datos-sintetico/corridas/salida-lineage-setup.md`.
- **Posible fallo del motor en el reporte:** en «Fuentes» dice «Sin documentos citados», aunque la tabla cita `20-informes/informe_junta_2026-10.pdf`. No lo cambié porque el reporte se muestra tal cual.
- **Citas sin página:** las cifras de la ficha citan el PDF sin número de página, porque la conversión del PDF no la trae.