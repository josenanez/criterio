# /criterio-security:access-reviews 

Dos de los cuatro sistemas tienen la revisión de accesos vencida o sin ninguna. La corrida quedó registrada como `2026-10-15-access-reviews-1`. Los términos 1.6 estaban vigentes, así que no hizo falta aceptarlos de nuevo.

# Las revisiones de acceso · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Agente:** Alexis, versión 1.5.1 · **Comando:** `access-reviews`

## Lo que hay que atender

| # | Qué | Responsable | Días | Cita |
|---|---|---|---|---|
| 1 | **Directorio activo**: la última revisión de accesos es del 2026-06-30 y tocaba el 2026-09-28. | Jefe de seguridad de la información | 17 | `00-referencia/sistemas.csv` fila 4 · `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1` |
| 2 | **Portal de clientes**: no hay ninguna revisión de accesos registrada, y la tabla pide una cada 180 días. | Jefe de seguridad de la información | — | `00-referencia/sistemas.csv` fila 5 |

## El resultado

| Sistema | Cada | Última revisión | Tocaba | Responsable |
|---|---|---|---|---|
| Core bancario | 90 días | 2026-08-10 | 2026-11-08 | Jefe de seguridad de la información |
| Correo corporativo | 180 días | 2026-05-02 | 2026-10-29 | Jefe de seguridad de la información |
| Directorio activo | 90 días | 2026-06-30 | 2026-09-28 | Jefe de seguridad de la información |
| Portal de clientes | 180 días | — | — | Jefe de seguridad de la información |

## Lo que no se pudo procesar

Estos tres archivos se excluyeron y no se abrieron, porque son credenciales, llaves o respaldos:
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

## Las preguntas que hizo

Nadie respondió preguntas en esta sesión. Tomé las respuestas sugeridas a partir de los documentos:
- La carpeta de la entidad, la entidad (RUC 1790987654001, Ecuador, USD) y el periodo 2026-10 son los correctos.
- Las tablas de `00-referencia/` y `40-riesgos/` se toman sin mapeo de columnas.
- Los resultados se guardan en `estado-seguridad/1790987654001-banco-del-guayas-sintetico`.
- Se acepta la marca `_CRITERIO_SEGURIDAD.txt`.
- Se aceptan los términos 1.6 a nombre de José Francisco Ñáñez, 2026-10-15.
- No programé la tarea diaria de `security-wake`, porque nadie dio un sí explícito.

## Fuentes

- `00-referencia/sistemas.csv`
- `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1`

El registro de la corrida cuenta 8 hallazgos, aunque este reporte muestra 2 señales. No revisé a qué corresponden los otros.

El texto anterior quedó guardado tal cual en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-access-reviews.md`. El reporte del motor está en `<estado>/seguridad/2026-10/reporte-access-reviews.md`.