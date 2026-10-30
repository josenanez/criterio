# /criterio-budget:budget-scan 

Inventario sin archivos nuevos, cambiados ni borrados (65 documentos); las tres actas ya estaban en la ficha. Se calcularon 3 señales para el corte 2026-09.

# Qué cambió en el presupuesto · Lojas Paulistas · presupuesto 2026, corte 2026-09

**Entidad:** Lojas Paulistas (31452078000170) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.12.1 · **Aprueba:** Sofia Leão · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administração se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/email-administracao.md) y 1 línea(s) no lo sostienen: Serviços públicos | 20.250,00 | — | — | `presupuesto-2026/30-proyecciones/email-administracao.md` |
| 2 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administração · Serviços públicos: ejecutado 155.250,00 contra 135.000,00 aprobado al corte (+15,0 %) | 20.250,00 | — | — | `presupuesto-2026/10-aprobado/orcamento-2026-v2-2026-06-30.xlsx` fila 2 · `2026-01/10-contabilidad/livro-razao.xlsx` fila 2 · `2026-02/10-contabilidad/livro-razao.xlsx` fila 2 |
| 3 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administração · Manutenção: ejecutado más comprometido es 96,0 % de lo aprobado en el año | -4.750,00 | — | — | `presupuesto-2026/10-aprobado/orcamento-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/livro-razao.xlsx` fila 4 · `2026-02/10-contabilidad/livro-razao.xlsx` fila 4 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Sin pregunta a la persona: rige la más reciente de 10-aprobado/ (v2, 2026-06-30); el acta 01 aprueba la v1 y el acta 05 respalda el traslado Publicidade → Eventos
- ¿Fechas del comité de presupuesto? → No encontradas en los documentos; committee_dates queda vacío
- ¿Dejo la marca _CRITERIO_FINANZAS.txt en la carpeta? → Sesión sin interfaz: no se escribió nada en la carpeta de documentos

## Fuentes

- `2026-01/10-contabilidad/livro-razao.xlsx`
- `2026-02/10-contabilidad/livro-razao.xlsx`
- `presupuesto-2026/10-aprobado/orcamento-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/email-administracao.md`

Corrida registrada como `2026-10-06-budget-scan-1` con 3 hallazgos.

Una aclaración sobre los términos: el motor los dio por vigentes (versión 1.3, aceptada en 0.12.1), así que no se mostraron ni se registró una aceptación nueva a nombre de José Francisco Ñáñez.