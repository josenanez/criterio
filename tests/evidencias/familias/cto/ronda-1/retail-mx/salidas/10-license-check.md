# /criterio-assets:license-check 

Los términos ya estaban vigentes, así que no registré ninguna aceptación. Después corrí el reporte de `license-check` de 2026-11.

Los términos (versión 1.6) ya estaban aceptados. Este es el cruce de las licencias compradas contra las que están en uso. Si se compran o se devuelven licencias lo decide el área de tecnología.

# Cada licencia contra su uso · Retail del Golfo Sintético · periodo 2026-11

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Las licencias en uso superan las compradas (`license_shortfall`) | Herramienta de analítica: 131 en uso y 120 compradas (11 de diferencia) | `30-activos/licencias.xlsx` fila 6 |
| 2 | Las licencias en uso superan las compradas (`license_shortfall`) | Diseño gráfico: 46 en uso y 40 compradas (6 de diferencia) | fila 5 |
| 3 | Las licencias en uso superan las compradas (`license_shortfall`) | Gestor de proyectos: 80 en uso y 75 compradas (5 de diferencia) | fila 7 |
| 4 | Las licencias pagadas sin uso superan el umbral (`license_unused`) | Antivirus de escritorio: 200 de 900 sin uso, el 22.2 %; la política tolera un 15 % | fila 10 |
| 5 | Las licencias pagadas sin uso superan el umbral (`license_unused`) | Videoconferencia: 190 de 600 sin uso, el 31.7 % | fila 8 |
| 6 | Las licencias pagadas sin uso superan el umbral (`license_unused`) | Firma electrónica: 80 de 200 sin uso, el 40 % | fila 9 |

El reporte no trae responsable ni días para ninguna señal.

## El resultado

Licencias sin uso que tolera la política: 15 %.

| Software | Compradas | En uso | Sin uso |
|---|---|---|---|
| Correo | 500 | 480 | 4 % |
| Ofimática | 300 | 300 | 0 % |
| Base de datos | 20 | 18 | 10 % |
| Diseño gráfico | 40 | 46 | -15 % |
| Herramienta de analítica | 120 | 131 | -9.2 % |
| Gestor de proyectos | 75 | 80 | -6.7 % |
| Videoconferencia | 600 | 410 | 31.7 % |
| Firma electrónica | 200 | 120 | 40 % |
| Antivirus de escritorio | 900 | 700 | 22.2 % |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/licencias.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-license-check-1` con 18 hallazgos. La salida completa está en `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/corridas/salida-license-check.md`. El reporte del motor está en `activos/2026-11/reporte-license-check.md` de la misma carpeta. Lo que aparece arriba es una copia abreviada, sin la columna de monto ni la de días.