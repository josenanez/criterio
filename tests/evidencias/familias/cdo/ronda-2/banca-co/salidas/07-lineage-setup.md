# /criterio-data-quality:lineage-setup datos/901555777-banco-cordillera-sintetico

Ariadna quedó instalada para Banco Cordillera Sintético (NIT 901555777), y la primera revisión del informe a la junta de octubre encontró 9 cifras que hay que atender.

- **Configuración:** quedó en `.criterio/calidad/901555777/config.json`. Usé las mismas respuestas que ya había dado Custodia y las confirmé: periodo 2026-11, tolerancia de 0.5 % según `politica_de_datos.pdf`, se publica en Rostrum y el estado se guarda en `estado-datos/901555777-banco-cordillera-sintetico`. La carpeta ya tenía su marca, así que no la volví a pedir.
- **Términos:** los acepta José Francisco Ñáñez, 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-quality-0.2.0-2026-11-25.md` y `.pdf`.
- **Ficha:** procesé el informe y llevé sus 13 cifras a `estado-datos/901555777-banco-cordillera-sintetico/calidad/2026-11/ficha.json`, todas con el corte que declara el informe, 2026-10-31.

En la tabla de abajo, la columna «Qué» y la tabla del resultado muestran los porcentajes e índices redondeados a entero; la columna «Monto» los trae completos.

# Cada cifra contra su fuente · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `figure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Ventas netas» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 9,520,000,000 y la fuente 9,400,000,000 al mismo corte, 2026-10-31: una diferencia de 120,000,000, más allá de la tolerancia del 0.5 % | 120.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 6 |
| 2 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Depósitos» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 5,100,000,000 y la fuente 5,000,000,000 al mismo corte, 2026-10-31: una diferencia de 100,000,000, más allá de la tolerancia del 0.5 % | 100.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 10 |
| 3 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Gastos operacionales» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 2,060,000,000 y la fuente 2,000,000,000 al mismo corte, 2026-10-31: una diferencia de 60,000,000, más allá de la tolerancia del 0.5 % | 60.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 12 |
| 4 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Participación de mercado» del informe 20-informes/informe_junta_2026-10.pdf: 12 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 12,50 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de satisfacción» del informe 20-informes/informe_junta_2026-10.pdf: 8 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 8,10 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 6 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de rotación» del informe 20-informes/informe_junta_2026-10.pdf: 4 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 4,20 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 7 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Colocaciones» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 7,600,000,000, es la de la fuente al 2026-09-30 | 7.600.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 15 |
| 8 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Cartera vencida» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 1,180,000,000, es la de la fuente al 2026-09-30 | 1.180.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 3 |
| 9 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Provisiones» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 610,000,000, es la de la fuente al 2026-09-30 | 610.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 17 |

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Informe | Indicador | Corte | En el informe | En la fuente | Estado |
|---|---|---|---|---|---|
| `20-informes/informe_junta_2026-10.pdf` | Cartera vencida | 2026-10-31 | 1,180,000,000 | 1,250,000,000 | otro corte |
| `20-informes/informe_junta_2026-10.pdf` | Clientes activos | 2026-10-31 | 84,200 | 84,200 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Ventas netas | 2026-10-31 | 9,520,000,000 | 9,400,000,000 | distinta |
| `20-informes/informe_junta_2026-10.pdf` | Margen operacional | 2026-10-31 | 3,400,000,000 | 3,400,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Depósitos | 2026-10-31 | 5,100,000,000 | 5,000,000,000 | distinta |
| `20-informes/informe_junta_2026-10.pdf` | Gastos operacionales | 2026-10-31 | 2,060,000,000 | 2,000,000,000 | distinta |
| `20-informes/informe_junta_2026-10.pdf` | Colocaciones | 2026-10-31 | 7,600,000,000 | 7,800,000,000 | otro corte |
| `20-informes/informe_junta_2026-10.pdf` | Provisiones | 2026-10-31 | 610,000,000 | 640,000,000 | otro corte |
| `20-informes/informe_junta_2026-10.pdf` | Costo de adquisición | 2026-10-31 | 185,000 | 185,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Tasa de retención | 2026-10-31 | 88 | 88 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Índice de satisfacción | 2026-10-31 | 8 | — | sin fuente |
| `20-informes/informe_junta_2026-10.pdf` | Participación de mercado | 2026-10-31 | 12 | — | sin fuente |
| `20-informes/informe_junta_2026-10.pdf` | Índice de rotación | 2026-10-31 | 4 | — | sin fuente |

Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con su fuente.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-informes/informe_junta_2026-10.pdf`
- `30-calidad/cifras_fuente.xlsx`
- Fuentes técnicas: F-01, F-02 (families/criterio-cdo/FUENTES.es.md)

---

En esta misma corrida aparecieron más señales que este reporte no muestra: linajes cortados, datos críticos sin regla y reglas bajo su umbral o que no corrieron. Se ven con `/criterio-data-quality:lineage-check` y `/criterio-data-quality:rule-check`.

No creé la tarea diaria porque esta sesión de prueba no tiene un sí explícito. A mano se corre con `/criterio-data-quality:lineage-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-lineage-setup-1`, y lo que mostré está en `estado-datos/901555777-banco-cordillera-sintetico/corridas/salida-lineage-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.