# /criterio-assets:license-check 

Términos vigentes (versión 1.6). Corrí el cruce de licencias de Software Austral Sintético para 2026-11, con corte 2026-11-25. Abajo está el reporte tal cual lo escribió el motor.

# Cada licencia contra su uso · Software Austral Sintético · periodo 2026-11

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `license-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Las licencias en uso de un software superan las compradas (`license_shortfall`) | Herramienta de analítica: 131 en uso y 120 compradas | 11,00 | — | — | `30-activos/licencias.xlsx` fila 6 |
| 2 | Las licencias en uso de un software superan las compradas (`license_shortfall`) | Diseño gráfico: 46 en uso y 40 compradas | 6,00 | — | — | `30-activos/licencias.xlsx` fila 5 |
| 3 | Las licencias pagadas sin uso de un software superan el umbral de la política (`license_unused`) | Videoconferencia: 190 de 600 licencias pagadas sin uso, el 31.7 %; la política tolera un 15 % | 190,00 | — | — | `30-activos/licencias.xlsx` fila 7 |
| 4 | Las licencias pagadas sin uso de un software superan el umbral de la política (`license_unused`) | Firma electrónica: 80 de 200 licencias pagadas sin uso, el 40 %; la política tolera un 15 % | 80,00 | — | — | `30-activos/licencias.xlsx` fila 8 |

## El resultado

**Licencias sin uso que tolera la política:** 15 %.

| Software | Compradas | En uso | Sin uso |
|---|---|---|---|
| Correo | 500 | 480 | 4 % |
| Ofimática | 300 | 300 | 0 % |
| Base de datos | 20 | 18 | 10 % |
| Diseño gráfico | 40 | 46 | -15 % |
| Herramienta de analítica | 120 | 131 | -9.2 % |
| Videoconferencia | 600 | 410 | 31.7 % |
| Firma electrónica | 200 | 120 | 40 % |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/licencias.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-license-check-1`. El reporte está en `activos/2026-11/reporte-license-check.md` y la salida mostrada en `corridas/salida-license-check.md`, ambos dentro de la carpeta de estado de la entidad.