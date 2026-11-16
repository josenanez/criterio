# /criterio-roles:profile-map 

Los términos vigentes quedaron registrados a nombre de José Francisco Ñáñez (2026-11-16). El reporte agrupa los siete perfiles de la ficha del periodo por su ocupación en el estándar.

# El mapa de los perfiles · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-map`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Dos perfiles comparten la ocupación y la mayor parte de sus requisitos (`profiles_overlap`) | PC-01 · Contador y PC-02 · Contador de impuestos: la misma ocupación 24111 y 75 % de los requisitos en común | — | — | — | `10-perfiles/PC-01_contador.docx` · `10-perfiles/PC-02_contador-de-impuestos.docx` |

## El resultado

| Perfil | Ocupación |
|---|---|
| PC-01 · Contador | 24111 · Contadores sintéticos |
| PC-02 · Contador de impuestos | 24111 · Contadores sintéticos |
| PC-03 · Auxiliar contable | 43111 · Auxiliares contables sintéticos |
| PC-04 · Analista de crédito | 33121 · Analistas de crédito sintéticos |
| PC-05 · Cajero | 42999 |
| PC-06 · Coordinador de cobranzas | — |
| PC-07 · Director financiero | 12110 · Directores financieros sintéticos |

| Se solapan | Ocupación | En común |
|---|---|---|
| PC-01 y PC-02 | 24111 | 75 % |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Entidad, identificación fiscal y país → Banco Cordillera Sintético · 901555123 · CO (tomada de la carpeta y de la política)
- Periodo → 2026-11
- Estándar de ocupaciones y su descarga → CUOC · 00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx
- Equivalencia de los niveles de estudio con la CINE → Bachiller 3 · Tecnólogo 5 · Profesional 6 (propuesta desde los perfiles)
- Cada cuántos meses se revisa un perfil → 12 (00-referencia/politica-de-seleccion.pdf, Plazos)
- Lo que la política prohíbe pedir → edad, sexo, estado civil, fotografía (00-referencia/politica-de-seleccion.pdf, Lo que no se pide)
- Dónde se guarda el estado → estado-talento/901555123-banco-cordillera-sintetico
- Términos → Aceptados por José Francisco Ñáñez, 2026-11-16
- Marca _CRITERIO_TALENTO.txt → Sin marca: no hubo un sí explícito

## Fuentes

- `10-perfiles/PC-01_contador.docx`
- `10-perfiles/PC-02_contador-de-impuestos.docx`
- Fuentes técnicas: F-03, F-10 (families/criterio-chro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-16-profile-map-1`, con la salida en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-profile-map.md`.