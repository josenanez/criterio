# /criterio-risk-appetite:appetite-setup riesgos/1790123456001-banco-del-pichincha-sur-sintetico

Soy Severo. Pongo cada exposición al lado de su límite y cada límite al lado de su dueño y su revisión. No apruebo excesos ni cambio límites.

**Carpeta:** encontré una sola carpeta posible, `riesgos/1790123456001-banco-del-pichincha-sur-sintetico`, que tiene 00-marco/, 10-exposicion/, 20-indicadores/, 30-eventos/ y 40-actas/. La tomé como la carpeta de la entidad. Tiene 11 documentos, todos en su lugar.

**Respuestas tomadas de los documentos:**
- **Entidad:** Banco del Pichincha Sur Sintético, identificación fiscal 1790123456001, país EC, moneda USD.
- **Último periodo cerrado:** 2026-10, según `10-exposicion/exposicion_2026-10.xlsx`.
- **Plazo para reportar la exposición:** 10 días después del cierre, según `00-marco/declaracion_de_apetito.pdf`.
- **Revisión de la declaración por la junta:** cada 12 meses, según `00-marco/declaracion_de_apetito.pdf`.
- **Plazos de Casandra,** según `00-marco/politica_de_riesgo_operacional.pdf`: 30 días para registrar un evento y 12 meses para tratar dos eventos como repetidos.
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-riesgos/1790123456001-banco-del-pichincha-sur-sintetico`.
- **Marca `_CRITERIO_RIESGOS.txt` en la carpeta:** sí.

**Términos (versión 1.6, del 2026-11-16):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-appetite-1.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre.

**Quedó listo:** la configuración está en `.criterio/apetito/1790123456001/config.json` y pasó la validación sin problemas. La marca quedó en la carpeta de la entidad.

**Primera ficha (2026-10):** registré la declaración de apetito con su última revisión por la junta, según `00-marco/declaracion_de_apetito.pdf`. También registré tres excesos que aprobó el comité en `40-actas/acta_comite_riesgos_2026-10.pdf`: L-04, L-06 y L-07. Sobre el L-03, el acta solo dice que el comité «toma nota del plan de acción», así que no lo registré como exceso aprobado.

El cálculo encontró además señales que este reporte no muestra: límites sin dueño, límites con la revisión vencida, riesgos sin límite y la declaración de apetito vencida. Las muestran `/criterio-risk-appetite:framework-check` y `/criterio-risk-appetite:coverage-check`.

# Cada exposición contra su límite · Banco del Pichincha Sur Sintético · periodo 2026-10

**Entidad:** Banco del Pichincha Sur Sintético (1790123456001) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 1.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-12 · Cartera vencida de vivienda: la exposición de 2026-10 es 4.6 % y el límite máximo es 4; no hay plan de acción ni aprobación del exceso | 0.60 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicion_2026-10.xlsx` fila 9 |
| 2 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0.40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 3 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 4 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-42 · Cupos de contraparte utilizados: Tesorería reportó su exposición de 2026-10 el 2026-11-16, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 6 | `10-exposicion/exposicion_2026-10.xlsx` fila 12 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-18 |
| L-03 | Concentración en el mayor deudor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo sobre ingresos | máximo 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Exposición a contrapartes sin calificación | máximo 15 % | 12 | no | — | Tesorería | 2026-11-09 |
| L-06 | Pérdidas operacionales sobre el patrimonio | máximo 1 % | 1.1 | sí | aprobado | Operaciones | 2026-11-08 |
| L-07 | Exposición al mayor banco corresponsal | máximo 20 % | 23 | sí | aprobado | Tesorería | 2026-11-09 |
| L-12 | Cartera vencida de vivienda | máximo 4 % | 4.6 | sí | — | Vicepresidencia de crédito | 2026-11-06 |
| L-22 | Concentración sectorial de la cartera | máximo 25 % | 21 | no | — | Vicepresidencia de crédito | 2026-11-05 |
| L-32 | Exposición en moneda extranjera | máximo 20 % | 14 | no | — | Tesorería | 2026-11-04 |
| L-42 | Cupos de contraparte utilizados | máximo 80 % | 62 | no | — | Tesorería | 2026-11-16 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

**Reloj:** no creé la tarea programada diaria porque necesita un sí explícito y en esta sesión nadie puede darlo. Para correrlo a mano: `/criterio-risk-appetite:appetite-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.