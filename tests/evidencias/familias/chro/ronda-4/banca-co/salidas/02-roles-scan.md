# /criterio-roles:roles-scan 

Los perfiles de `10-perfiles/` ya estaban en la ficha del periodo desde el setup y coinciden con el texto de cada documento, así que no hubo que agregar ninguno ni anotar nada en `reviewed`.
Las fotos de los candidatos no se procesan: el motor no lee ese formato, y además la política no permite pedir fotografías. Son parte de la selección, no de los perfiles.
Qué hacer con cada señal lo decide una persona.

# Qué cambió en los perfiles · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.2.0 · **Comando:** `roles-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PC-02 · Contador de impuestos: el requisito R5 «Hombre menor de 35 años» pide edad, que no se puede pedir según la política de selección de la organización | — | — | — | `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 2 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PC-02 · Contador de impuestos: el requisito R5 «Hombre menor de 35 años» pide sexo, que no se puede pedir según la política de selección de la organización | — | — | — | `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 3 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PC-04 · Analista de crédito: el requisito R4 «Gozar de buen estado de salud» pide la salud, que no se puede pedir según Ley 1581 de 2012, art. 5 (F-10) | — | — | — | `10-perfiles/PC-04_analista-de-credito.docx` |
| 4 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PC-06 · Coordinador de cobranzas: el requisito R2 «Estado civil casado» pide estado civil, que no se puede pedir según la política de selección de la organización | — | — | — | `10-perfiles/PC-06_coordinador-de-cobranzas.docx` |
| 5 | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación (`education_level_inconsistent`) | PC-03 · Auxiliar contable: pide «Profesional» (CINE 6); la ocupación 43111 es de nivel de competencia 2, que suele exigir CINE 2 a 4 (CUOC 2026, numeral 3.2): pide más de lo que la ocupación exige | — | — | — | `10-perfiles/PC-03_auxiliar-contable.docx` |
| 6 | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación (`education_level_inconsistent`) | PC-07 · Director financiero: pide «Bachiller» (CINE 3); la ocupación 12110 es de nivel de competencia 4, que suele exigir CINE 6 a 8 (CUOC 2026, numeral 3.2): pide menos de lo que la ocupación exige | — | — | — | `10-perfiles/PC-07_director-financiero.docx` |
| 7 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PC-05 · Cajero: el código 42999 no está en CUOC | — | — | — | `10-perfiles/PC-05_cajero.docx` |
| 8 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PC-06 · Coordinador de cobranzas: el perfil no tiene un código de ocupación que lo ate a un estándar | — | — | — | `10-perfiles/PC-06_coordinador-de-cobranzas.docx` |
| 9 | Un perfil pasó su fecha de revisión (`profile_review_overdue`) | PC-01 · Contador: tocaba revisarlo el 2026-03-01 | — | — | 260 | `10-perfiles/PC-01_contador.docx` |
| 10 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PC-01 · Contador: «Legislación tributaria» (conocimiento de la ocupación 24111 en CUOC) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PC-01_contador.docx` |
| 11 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PC-04 · Analista de crédito: «Análisis de necesidades» (destreza de la ocupación 33121 en CUOC) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PC-04_analista-de-credito.docx` |
| 12 | Dos perfiles comparten la ocupación y la mayor parte de sus requisitos (`profiles_overlap`) | PC-01 · Contador y PC-02 · Contador de impuestos: la misma ocupación 24111 y 75 % de los requisitos en común | — | — | — | `10-perfiles/PC-01_contador.docx` · `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 13 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PC-02 · Contador de impuestos: el requisito R5 «Hombre menor de 35 años» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 14 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PC-07 · Director financiero: el requisito R4 «Dominio del inglés de negocios» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PC-07_director-financiero.docx` |

## El resultado

**Perfiles en la ficha:** 7 · **Estándar:** CUOC, 5 ocupaciones.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Carpeta raíz de la entidad → talento/901555123-banco-cordillera-sintetico (única candidata)
- Entidad, identificación fiscal y país → Banco Cordillera Sintético, 901555123, CO
- Periodo → 2026-11
- Estándar de ocupaciones y su descarga → CUOC, 00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx
- Equivalencia de estudios con la CINE → Bachiller 3, Tecnólogo 5, Profesional 6
- Cada cuántos meses se revisa un perfil → 12, según la política de selección
- Lo que la política prohíbe pedir → edad, sexo, estado civil, fotografía, según la política de selección
- Dónde se guarda el estado → estado-talento/901555123-banco-cordillera-sintetico
- Términos 1.6 → aceptados por José Francisco Ñáñez el 2026-11-16
- Marcar la carpeta con _CRITERIO_TALENTO.txt → sí

## Fuentes

- `10-perfiles/PC-01_contador.docx`
- `10-perfiles/PC-02_contador-de-impuestos.docx`
- `10-perfiles/PC-03_auxiliar-contable.docx`
- `10-perfiles/PC-04_analista-de-credito.docx`
- `10-perfiles/PC-05_cajero.docx`
- `10-perfiles/PC-06_coordinador-de-cobranzas.docx`
- `10-perfiles/PC-07_director-financiero.docx`
- Fuentes técnicas: F-03, F-10 (families/criterio-chro/FUENTES.es.md)

---
Corrida registrada como `2026-11-16-roles-scan-1`. La salida mostrada quedó en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-roles-scan.md`.