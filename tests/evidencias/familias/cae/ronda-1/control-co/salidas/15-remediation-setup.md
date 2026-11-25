# /criterio-remediation:remediation-setup auditoria/901888432-banco-control-sintetico

Soy Remedios. Llevo cada hallazgo hasta su cierre, con su evidencia; no cierro nada ni acepto riesgos.

**Carpeta:** 1. `auditoria/901888432-banco-control-sintetico`: marcada con _CRITERIO_AUDITORIA.txt (Banco Control Sintético, NIT 901888432); tiene 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/. Es la única candidata, así que la tomo.

**Respuestas, tomadas de los documentos y del setup de Prudencia y Justo:**
- Entidad: Banco Control Sintético, NIT 901888432, Colombia (COP). Periodo: 2026-11.
- Reprogramaciones permitidas: 2. Fuente: metodología, «Seguimiento»: «La fecha de un plan de acción se puede correr hasta dos veces».
- Quién valida un cierre: auditoría, con la evidencia de su implementación (metodología, «Seguimiento»).
- Alta dirección y consejo para escalar un riesgo aceptado: no aparecen en el estatuto ni en la metodología, y la configuración no tiene un campo para ellos. Quedan sin registrar.
- Publicar en Rostrum: no (decisión 0014).
- Estado: `estado-auditoria/901888432-banco-control-sintetico`.
- Marca: la carpeta ya estaba marcada, así que no la marqué de nuevo.
- Fuera de lugar, como sugerencia (no moví nada): `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/` y `30-seguimiento/riesgos_aceptados.xlsx` en `10-plan/`.

**Términos 1.6:** Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-remediation-0.1.0-2026-11-24.md` y `.pdf`.

**La ficha de 2026-11:** procesé los 6 documentos de `30-seguimiento/`. Encontré la evidencia de H-20 y de H-21, la explicación del atraso de H-03 y el hallazgo RF-01 del revisor fiscal.

**Revisar en el motor:** H-03 tiene fecha 2026-09-30, anterior al corte del 2026-11-24, y no tiene evidencias. Aun así, el motor no levantó ninguna señal. Esa conclusión le toca al responsable de auditoría.

# Los planes contra su fecha · Banco Control Sintético · periodo 2026-11

**Entidad:** Banco Control Sintético (901888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `action-status`

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

**Cuándo vuelvo:** sin reloj. La sesión no tiene interfaz y nadie dio un sí explícito. Se corre a mano con `/criterio-remediation:remediation-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.