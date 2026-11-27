# /criterio-remediation:remediation-setup auditoria/901888432-banco-control-sintetico

Soy Remedios. Sigo cada hallazgo hasta su cierre, con su evidencia, pero no cierro nada ni acepto riesgos.

**Carpeta:** solo encontré una candidata, `auditoria/901888432-banco-control-sintetico`, que tiene 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/. Uso esa.

**Respuestas que ya estaban dadas.** Las tomé de los setups de Prudencia y Justo y las comprobé contra la metodología:
- **Entidad:** Banco Control Sintético, identificación fiscal 901888432, país CO, moneda COP.
- **Periodo:** 2026-11.
- **Reprogramaciones permitidas:** 2. La metodología, en «Seguimiento», dice que la fecha de un plan se puede correr hasta dos veces.
- **Publicar en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-auditoria/901888432-banco-control-sintetico`.
- **Marca `_CRITERIO_AUDITORIA.txt`:** no. Los setups anteriores tampoco la dejaron.

**Términos (versión 1.6):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Los aceptó José Francisco Ñáñez el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-remediation-0.2.2-2026-11-24.md` y en su versión `.pdf`.

**Configuración:** `.criterio/seguimiento/901888432/config.json`. La validación salió sin problemas.

**Ficha de 2026-11:** en `30-seguimiento/` encontré las evidencias de H-20 y H-21, la explicación del atraso de H-03 y el hallazgo RF-01 del informe del revisor fiscal.

El motor no encontró nada que atender en este comando. H-03 tiene en la ficha una explicación documentada de su atraso. Aceptarla o no le toca al responsable de auditoría.

# Los planes contra su fecha · Banco Control Sintético · periodo 2026-11

**Entidad:** Banco Control Sintético (901888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `action-status`

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

**Cuándo vuelvo:** sin reloj, porque en esta sesión de prueba nadie dio el sí a la tarea programada. Para correrlo a mano: `/criterio-remediation:remediation-wake`.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.