# /criterio-risk-appetite:framework-check 

El reporte de `framework-check` de 2026-11 salió sin hallazgos, pero la declaración de apetito aparece vacía y ningún área reportó exposición.

- **Términos:** vigentes (versión 1.6), así que el comando siguió. No tuve que registrar ninguna aceptación en esta corrida.
- **Declaración de apetito:** la ficha no trae ninguna. El reporte muestra "—" en la declaración, en la fecha de revisión de la junta y en la próxima revisión, así que el motor no pudo comparar la declaración con el plazo del marco.
- **Límites:** los cinco (L-01 a L-05) tienen dueño y fecha de próxima revisión. El de más cerca es L-02, de Tesorería, que se revisa el 2026-12-15. Ninguno aparece sin dueño ni vencido.
- **Exposición sin reportar:** el motor lista como "no se pudo procesar" los cinco límites. Ningún área reportó su exposición de 2026-11, y el único archivo en `10-exposicion/` es `exposicion_2026-10.xlsx`.
- **Preguntas:** no hice ninguna en esta corrida.

---

# El marco y la declaración · Banco Control de Riesgos Sintético · periodo 2026-11

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `framework-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —.

| Límite | Métrica | Dueño | Próxima revisión |
|---|---|---|---|
| L-01 | Cartera vencida de consumo | Vicepresidencia de crédito | 2027-03-31 |
| L-02 | Indicador de cobertura de liquidez | Tesorería | 2026-12-15 |
| L-03 | Concentración en el mayor deudor | Vicepresidencia de crédito | 2027-03-31 |
| L-04 | Pérdidas por fraude externo sobre ingresos | Operaciones | 2027-06-30 |
| L-05 | Exposición a contrapartes sin calificación | Tesorería | 2027-06-30 |

Quién es el dueño de un límite y cuándo se revisa lo fija el marco: aquí se dice cuál falta o se venció.

## Lo que no se pudo procesar

- `10-exposicion/exposicion_2026-10.xlsx`: L-01 · Cartera vencida de consumo: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-02 · Indicador de cobertura de liquidez: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-03 · Concentración en el mayor deudor: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-04 · Pérdidas por fraude externo sobre ingresos: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-05 · Exposición a contrapartes sin calificación: ningún área reportó su exposición de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-10 (families/criterio-cro/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-framework-check-1` y lo mostrado está en `estado-riesgos/901888444-banco-control-de-riesgos-sintetico/corridas/salida-framework-check.md`.