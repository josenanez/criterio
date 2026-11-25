# /criterio-remediation:remediation-setup auditoria/20602888432-cooperativa-control-sintetica

Soy Remedios. Llevo cada hallazgo hasta su cierre, con su evidencia; no cierro nada ni acepto riesgos.

Remedios ya está lista para esta entidad. El reporte no trae ninguna señal abierta.

**Carpeta:** 1. `auditoria/20602888432-cooperativa-control-sintetica`. Ya tiene la marca `_CRITERIO_AUDITORIA.txt` (Cooperativa Control Sintética, RUC 20602888432) y las cuatro subcarpetas: 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/. Es la única candidata, así que la tomo.

**Respuestas que tomé de los documentos y de lo que ya fijaron Prudencia y Justo:**
- **Entidad:** Cooperativa Control Sintética, RUC 20602888432, Perú (PEN).
- **Periodo:** 2026-11.
- **Reprogramaciones permitidas:** 2. La metodología dice: «La fecha de un plan de acción se puede correr hasta dos veces» (metodologia-de-auditoria.pdf, sección «Seguimiento»).
- **Quién valida un cierre:** auditoría, con la evidencia de su implementación (misma sección).
- **Alta dirección y consejo para escalar un riesgo aceptado:** ni el estatuto ni la metodología los nombran. El motor toma ese dato de las columnas «Discutido alta dirección» y «Escalado consejo» del registro de riesgos aceptados.
- **Publicar en Rostrum:** no (decisión 0014).
- **Dónde guardo lo que encuentro:** `estado-auditoria/20602888432-cooperativa-control-sintetica`.
- **Marca de la carpeta:** ya estaba, no la vuelvo a dejar.

**Términos (versión 1.6, del 2026-11-16):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-remediation-0.1.0-2026-11-24.md` y en `.pdf`.

**Configuración:** quedó en `.criterio/seguimiento/20602888432/config.json` y el motor la validó sin problemas.

**Una contradicción para revisar (no moví nada):** el inventario sugiere llevar `30-seguimiento/informe_revisor_fiscal_2026.pdf` a `20-trabajos/` y `30-seguimiento/riesgos_aceptados.xlsx` a `10-plan/`. Pero la estructura recomendada de la familia pone esos dos archivos justo en `30-seguimiento/`, así que los dejé donde están.

**Primera ficha (2026-11):** procesé los 6 documentos de `30-seguimiento/`. Llevé a la ficha:
- 2 evidencias, de H-20 y H-21;
- 1 explicación de atraso, de H-03;
- 1 hallazgo externo, RF-01, del revisor fiscal.

El motor no encontró señales abiertas. Este es el reporte, tal como lo escribió:

---

# Los planes contra su fecha · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (20602888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `action-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Reprogramaciones que permite la metodología:** 2.

| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |
|---|---|---|---|---|---|---|
| H-01 | TR-01 | Alta | Gerencia de crédito | 2026-12-31 | 0 | 0 |
| H-02 | TR-01 | Media | Gerencia de garantías | 2026-12-15 | 0 | 0 |
| H-03 | TR-02 | Media | Gerencia de tecnología | 2026-09-30 | 2 | 0 |
| RF-01 | — | Media | Gestión humana | 2026-12-31 | 0 | 0 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión no hay nadie que lo dé. Para correrlo a mano: `/criterio-remediation:remediation-wake`.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.