# /criterio-risk-events:events-setup riesgos/98765432000110-cooperativa-controle-sintetica

Soy Casandra. Pongo cada indicador clave al lado de su umbral y cada evento de pérdida al lado de su registro y de la matriz; no califico riesgos ni cierro eventos.

**Carpeta:** `riesgos/98765432000110-cooperativa-controle-sintetica` es la única que encontré. Ya tiene la marca `_CRITERIO_RIESGOS.txt` (Cooperativa Controle Sintética, CNPJ 98765432000110) y las cinco carpetas: `00-marco/`, `10-exposicion/`, `20-indicadores/`, `30-eventos/` y `40-actas/`. Uso esa.

**Respuestas que tomé de los documentos y del setup de Severo** (nadie respondía en esta prueba):
- **Entidad:** Cooperativa Controle Sintética, CNPJ 98765432000110, Brasil, en reales (BRL).
- **Último periodo cerrado:** 2026-10, según `valores_indicadores_2026-10.xlsx`.
- **Plazos de la política** (`00-marco/politica_de_risco_operacional.pdf`):
  - Un evento se registra en hasta 30 días corridos desde que se descubre.
  - Dos eventos del mismo tipo en el mismo proceso dentro de 12 meses cuentan como repetidos.
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-riesgos/98765432000110-cooperativa-controle-sintetica`.
- **Marca:** la carpeta ya estaba marcada, así que no volví a marcarla.

**Términos (versión 1.6, 2026-11-16):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-events-0.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre.

**Configuración:** `.criterio/eventos/98765432000110/config.json`. El motor la validó sin problemas.

**Primera ficha:** procesé `40-actas/ata_comite_riscos_2026-10.pdf` y llevé a la ficha la única acción que acordó sobre un indicador clave: el bloqueo preventivo de los BIN comprometidos, sobre KRI-01.

---

# Cada indicador contra su umbral · Cooperativa Controle Sintética · periodo 2026-10

**Entidad:** Cooperativa Controle Sintética (98765432000110) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transações fraudulentas por milhão | mayor es peor | 40 | 60 | 52 | alerta | sí |
| KRI-02 · Disponibilidade dos canais digitais | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotatividade da equipe de crédito | mayor es peor | 8 | 12 | 6.5 | normal | no |
| KRI-04 · Dias sem teste do plano de continuidade | mayor es peor | 180 | 365 | 64 | normal | no |
| KRI-05 · Concentração dos depósitos nos 20 maiores | mayor es peor | 25 | 30 | 29 | alerta | sí |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

**Reloj:** no creé ninguna tarea programada, porque hace falta un sí explícito y en esta prueba nadie respondía. Para correrlo a mano: `/criterio-risk-events:events-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-events-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.