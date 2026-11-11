# /criterio-legal:legal-setup legal/88399201-9-instituto-publico-del-guaira-sintetico

Soy Fidel. Proceso lo que tu empresa firmó y te digo qué vence, quién firmó con qué facultad y qué se pagó por fuera de lo pactado.

**Carpeta:** `legal/88399201-9-instituto-publico-del-guaira-sintetico`, la que venía en el argumento.

**Inventario**
- Hay 6 contratos en `contratos/`, del CTR-4701 al CTR-4706.
- Están el registro de contratos (`10-registro/registro-contratos.csv`) y la matriz de atribuciones (`00-referencia/matriz-atribuciones.csv`).
- Un archivo está fuera de la estructura recomendada: `00-referencia/politica-contratacion.md` iría en `20-politicas/`. Es solo una sugerencia; no moví nada.

**Respuestas tomadas de los documentos**
1. **Entidad:** Instituto Público del Guairá Sintético, RUC 88399201-9, Paraguay, en guaraníes (PYG).
2. **Matriz de atribuciones:** la de `00-referencia/matriz-atribuciones.csv`.
3. **Avisos:** 60 días antes de un vencimiento y 30 días antes de un preaviso, que son los de `config.example.json`.
4. **Certificado de la contraparte:** puede tener hasta 30 días de antigüedad al firmar.
5. **Entidad pública:** sí. Según su política de contratación, publica sus contratos en SICP. En Paraguay no hace falta registrar un umbral de garantía.
6. **Dónde guardo lo que encuentro:** `estado-legal/88399201-9-instituto-publico-del-guaira-sintetico`.
7. **Términos (versión 1.5):** «Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal»
   - Los aceptó José Francisco Ñáñez el 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-1.6.3-2026-10-06.md` y en su `.pdf`.

**Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie lo autorizó en esta sesión.

**Configuración:** quedó en `.criterio/legal/88399201-9/config.json` y la validación no encontró problemas.

Procesé los 6 contratos y armé la ficha de cada uno; el cálculo no encontró nada que corregir en ellas. También encontró problemas con las garantías que pide la ley de contratación pública, que no entran en el calendario; los muestra `/criterio-legal:contract-execution`.

# Vencimientos, preavisos y obligaciones · Instituto Público del Guairá Sintético · al 2026-10-06

**Entidad:** Instituto Público del Guairá Sintético (88399201-9) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.6.3 · **Comando:** `obligations-calendar`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Fecha | Contrato | Qué | Días | Evidencia |
|---|---|---|---|---|
| 2026-09-30 | CTR-4701 | obligación OBL-3 · Reporte de operaciones al oficial de cumplimiento | -6 | `contratos/CTR-4701-tecnologia-gubernamental-sintetica-s-a/40-ejecucion/OBL-3_reporte-de-operaciones-al-oficial-de-cum.md` |
| 2026-11-20 | CTR-4705 | terminación | 45 | — |
| 2026-11-20 | CTR-4705 | obligación OBL-2 · Informe final y acta de liquidación | 45 | — |
| 2026-12-31 | CTR-4703 | terminación | 86 | — |
| 2026-12-31 | CTR-4703 | obligación OBL-2 · Informe final y acta de liquidación | 86 | — |

Entre 30 días atrás y 90 adelante. La decisión de renovar o terminar es de una persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

---

**Cuándo vuelvo:** sin reloj, porque nadie confirmó la tarea programada en esta sesión. Para correrlo a mano: `/criterio-legal:legal-wake`.

Guardé esta salida en `estado-legal/88399201-9-instituto-publico-del-guaira-sintetico/corridas/salida-legal-setup.md` y la corrida quedó registrada como `2026-10-06-legal-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.