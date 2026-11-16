# /criterio-legal:legal-setup legal/39910202-instituto-publico-del-altiplano-sintetic

Soy Fidel. Proceso lo que tu empresa firmó y te digo qué vence, quién firmó con qué facultad y qué se pagó por fuera de lo pactado.

**Carpeta:** 1. `legal/39910202-instituto-publico-del-altiplano-sintetic`. Tiene `00-referencia/`, `10-registro/`, `20-politicas/`, `30-normativa/` y `40-canal/`, además de 6 contratos y 3 periodos. Era la única candidata, así que la tomé.

**Inventario:**
- Hay 6 contratos en `contratos/`, del CTR-4801 al CTR-4806.
- Están el registro de contratos (`10-registro/registro-contratos.csv`), los pagos (`pagos-2026-09-30.csv`) y la matriz de atribuciones (`00-referencia/matriz-atribuciones.csv`).
- Fuera de la estructura recomendada: `00-referencia/politica-contratacion.md` iría en `20-politicas/`. Es solo una sugerencia; no moví nada.

**Respuestas tomadas de los documentos:**
1. **Entidad:** Instituto Público del Altiplano Sintético, NIT 39910202, Guatemala, en quetzales (GTQ).
2. **Matriz de atribuciones:** `00-referencia/matriz-atribuciones.csv`.
3. **Avisos:** 60 días antes de un vencimiento y 30 antes de un preaviso, los valores por omisión de la configuración de ejemplo.
4. **Certificado de la contraparte:** como máximo 30 días de antigüedad al firmar.
5. **Entidad pública:** sí, porque `politica-contratacion.md` dice que publica en GUATECOMPRAS. En Guatemala no hay umbral de garantía que preguntar.
6. **Dónde guardo lo que encuentro:** `estado-legal/39910202-instituto-publico-del-altiplano-sintetic`.
7. **Términos, versión 1.5:**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Quedaron aceptados a nombre de José Francisco Ñáñez. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-1.8.0-2026-10-06.md`, con su versión `.pdf`. También dejé la marca `_CRITERIO_LEGAL.txt` en la carpeta de documentos.

**Configuración:** quedó en `.criterio/legal/39910202/config.json` y pasó la revisión sin problemas.

**Fichas:** procesé los 6 contratos con sus pólizas, certificados y constancias de publicación, más el otrosí OT-1 de CTR-4802 y el acta del comité de CTR-4805. Las 6 fichas quedaron sin datos faltantes.

**Garantías por debajo del mínimo:** fuera del calendario, el motor encontró 2 garantías de cumplimiento por debajo del mínimo de la ley de contratación pública, en CTR-4801 y CTR-4803. Las detalla `/criterio-legal:contract-execution`. Qué implica eso es una pregunta para ti, no una conclusión mía.

---

# Vencimientos, preavisos y obligaciones · Instituto Público del Altiplano Sintético · al 2026-10-06

**Entidad:** Instituto Público del Altiplano Sintético (39910202) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.8.0 · **Comando:** `obligations-calendar`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Fecha | Contrato | Qué | Días | Evidencia |
|---|---|---|---|---|
| 2026-09-30 | CTR-4801 | obligación OBL-3 · Reporte de operaciones del periodo al oficial de cumplimiento | -6 | `contratos/CTR-4801-tecnologia-gubernamental-sintetica-s-a/40-ejecucion/OBL-3_reporte-de-operaciones-al-oficial-de-cum.md` |
| 2026-11-20 | CTR-4805 | terminación | 45 | — |
| 2026-11-20 | CTR-4805 | obligación OBL-2 · Informe final y acta de liquidación | 45 | — |
| 2026-12-31 | CTR-4803 | terminación | 86 | — |
| 2026-12-31 | CTR-4803 | obligación OBL-2 · Informe final y acta de liquidación | 86 | — |

Entre 30 días atrás y 90 adelante. La decisión de renovar o terminar es de una persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

---

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque esta sesión no tenía a nadie que la autorizara con un sí. Para correrlo a mano: `/criterio-legal:legal-wake`.

La lista de días festivos de la configuración quedó vacía, porque ningún documento trae los de Guatemala.

La salida quedó en `estado-legal/39910202-instituto-publico-del-altiplano-sintetic/corridas/salida-legal-setup.md` y la corrida quedó registrada como `2026-10-06-legal-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.