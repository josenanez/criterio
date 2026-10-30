# /criterio-compliance:compliance-scan 

Términos vigentes; el inventario no trae archivos nuevos, cambiados ni borrados. El registro normativo es una tabla y la procesó el motor. El reporte trae cinco señales abiertas.

(Los términos ya figuraban como aceptados en la versión 0.12.1. No registré una aceptación nueva.)

# Qué cambió en el cumplimiento · Banco Serra Verde · periodo 2026-09

**Entidad:** Banco Serra Verde (52817460000100) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.12.1 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Relatório mensal de reclamações: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Paulo Nogueira | 1 | `00-referencia/matriz-obrigacoes.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/relatorio-compliance-2026-09.md) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/relatorio-compliance-2026-09.md` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Fernanda Costa | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-1601 · OBL-3 · Relatório de operações do período ao responsável de compliance: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `legal/52817460000100-banco-serra-verde/contratos/CTR-1601-sistemas-bancarios-ltda/10-contrato/contrato.md, cláusula 7` |
| 5 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflitos de interesses: no tiene responsable | — | — | — | `00-referencia/matriz-obrigacoes.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el más reciente con carpeta y con informe de compliance
- ¿Plazo de respuesta del canal de denuncias? → 15 días (valor por defecto; ningún documento fija otro)
- ¿Días para evaluar una norma nueva? → 30 días (valor por defecto; ningún documento fija otro)

## Fuentes

- `00-referencia/matriz-obrigacoes.csv`
- `30-normativa/registro-normativo.csv`
- `cumplimiento-2026-09/20-reportes/relatorio-compliance-2026-09.md`
- `legal/52817460000100-banco-serra-verde/contratos/CTR-1601-sistemas-bancarios-ltda/10-contrato/contrato.md, cláusula 7`

La corrida quedó registrada como `2026-10-06-compliance-scan-1`, con 5 hallazgos. La salida está en `estado-legal/52817460000100-banco-serra-verde/corridas/salida-compliance-scan.md`.

Dos notas sobre el reporte:
- La sección "El resultado" salió vacía en la salida del motor. La dejo tal cual, sin rellenarla.
- Escribí a mano una línea antes del encabezado sobre los términos. No puse ninguna cifra ni fecha que el reporte no traiga, aparte del conteo de cinco señales, que sale de `compute`.