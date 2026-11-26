# /criterio-risk-appetite:limit-check 

Hay cuatro señales en el periodo 2026-10. Dos exposiciones superan su límite sin plan de acción ni aprobación, y dos reportes de Tesorería llegaron fuera de plazo. El comité y la junta deciden qué se hace con cada exceso.

Los términos (versión 1.6) ya estaban vigentes, así que no registré ninguna aceptación nueva.

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Exceso sin plan ni aprobación | L-12 · Carteira vencida imobiliária: exposición 4.6 %, límite máximo 4 % | Diretoria de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicao_2026-10.xlsx` fila 9 |
| 2 | Exceso sin plan ni aprobación | L-01 · Carteira vencida de crédito pessoal: exposición 6.4 %, límite máximo 6 % | Diretoria de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicao_2026-10.xlsx` fila 2 |
| 3 | Reporte fuera de plazo | L-02 · Índice de liquidez de curto prazo: reportado el 2026-11-18, plazo hasta el 2026-11-10 | Tesouraria | 8 | `10-exposicion/exposicao_2026-10.xlsx` fila 3 |
| 4 | Reporte fuera de plazo | L-42 · Limites de contraparte utilizados: reportado el 2026-11-16, plazo hasta el 2026-11-10 | Tesouraria | 6 | `10-exposicion/exposicao_2026-10.xlsx` fila 12 |

## El resultado

El marco da 10 días después del cierre para reportar, hasta el 2026-11-10. De los 11 límites del periodo, 6 están excedidos. Otros tres de esos excesos sí tienen respaldo: L-03 tiene plan, y L-04, L-06 y L-07 tienen la aprobación registrada. Eso suma siete excedidos con L-01 y L-12, por lo que debes revisar el conteo en la tabla del reporte antes de citarlo.

| Límite | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|
| L-01 | máx. 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | mín. 120 % | 131 | no | — | Tesouraria | 2026-11-18 |
| L-03 | máx. 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | máx. 0.5 % | 0.62 | sí | aprobado | Operações | 2026-11-07 |
| L-05 | máx. 15 % | 12 | no | — | Tesouraria | 2026-11-09 |
| L-06 | máx. 1 % | 1.1 | sí | aprobado | Operações | 2026-11-08 |
| L-07 | máx. 20 % | 23 | sí | aprobado | Tesouraria | 2026-11-09 |
| L-12 | máx. 4 % | 4.6 | sí | — | Diretoria de crédito | 2026-11-06 |
| L-22 | máx. 25 % | 21 | no | — | Diretoria de crédito | 2026-11-05 |
| L-32 | máx. 20 % | 14 | no | — | Tesouraria | 2026-11-04 |
| L-42 | máx. 80 % | 62 | no | — | Tesouraria | 2026-11-16 |

Todo lo que llegó se procesó y el motor no hizo preguntas en esta corrida.

## Corrida registrada

El reporte del motor está en `estado-riesgos/12345678000190-cooperativa-vale-sintetica/apetito/2026-10/reporte-limit-check.md`. Lo mostrado quedó en `corridas/salida-limit-check.md` y la corrida se registró como `2026-11-25-limit-check-1`.

Corrección: en el apartado «El resultado» conté mal los límites excedidos. La tabla muestra siete (L-01, L-03, L-04, L-06, L-07, L-12, no seis; contando bien son seis: L-01, L-03, L-04, L-06, L-07 y L-12). El número correcto es **6 excedidos**: 2 sin plan ni aprobación, 1 con plan y 3 con aprobación. Mi frase sobre «siete» era un error. El archivo `salida-limit-check.md` contiene el reporte completo del motor, que es la fuente de las cifras.