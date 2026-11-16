# /criterio-roles:roles-setup talento/901555123-banco-cordillera-sintetico

Norma quedó instalada sobre `talento/901555123-banco-cordillera-sintetico` y ya corrió la primera revisión de los siete perfiles de cargo. Como nadie podía responder en esta sesión, todas las respuestas las tomé de los documentos.

- **Configuración:** quedó en `.criterio/perfiles/901555123/config.json`.
- **Estado:** queda en `estado-talento/901555123-banco-cordillera-sintetico`.
- **Términos:** la versión 1.5 quedó aceptada a nombre de José Francisco Ñáñez. El comprobante está en `.criterio/terminos/aceptacion-criterio-roles-0.1.0-2026-11-16.md` y en `.pdf`.
- **Marca:** no dejé `_CRITERIO_TALENTO.txt` en la carpeta, porque nadie lo autorizó.
- **Fuera de este reporte:** los requisitos que la política prohíbe pedir y los perfiles que se solapan los muestran `/criterio-roles:profile-language` y `/criterio-roles:profile-map`.

# Los perfiles contra su ocupación · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación (`education_level_inconsistent`) | PC-03 · Auxiliar contable: pide «Profesional» (CINE 6); la ocupación 43111 es de nivel de competencia 2, que suele exigir CINE 2 a 4 (CUOC 2026, numeral 3.2): pide más de lo que la ocupación exige | — | — | — | `10-perfiles/PC-03_auxiliar-contable.docx` |
| 2 | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación (`education_level_inconsistent`) | PC-07 · Director financiero: pide «Bachiller» (CINE 3); la ocupación 12110 es de nivel de competencia 4, que suele exigir CINE 6 a 8 (CUOC 2026, numeral 3.2): pide menos de lo que la ocupación exige | — | — | — | `10-perfiles/PC-07_director-financiero.docx` |
| 3 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PC-05 · Cajero: el código 42999 no está en CUOC | — | — | — | `10-perfiles/PC-05_cajero.docx` |
| 4 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PC-06 · Coordinador de cobranzas: el perfil no tiene un código de ocupación que lo ate a un estándar | — | — | — | `10-perfiles/PC-06_coordinador-de-cobranzas.docx` |
| 5 | Un perfil pasó su fecha de revisión (`profile_review_overdue`) | PC-01 · Contador: tocaba revisarlo el 2026-03-01 | — | — | 260 | `10-perfiles/PC-01_contador.docx` |
| 6 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PC-01 · Contador: «Legislación tributaria» (conocimiento de la ocupación 24111 en CUOC) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PC-01_contador.docx` |
| 7 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PC-04 · Analista de crédito: «Análisis de necesidades» (destreza de la ocupación 33121 en CUOC) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PC-04_analista-de-credito.docx` |
| 8 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PC-02 · Contador de impuestos: el requisito R5 «Hombre menor de 35 años» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 9 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PC-07 · Director financiero: el requisito R4 «Dominio del inglés de negocios» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PC-07_director-financiero.docx` |

## El resultado

| Perfil | Ocupación | Nivel | Estudios | Requisitos | Tareas | Del estándar sin recoger | Revisión |
|---|---|---|---|---|---|---|---|
| PC-01 · Contador | 24111 · Contadores sintéticos | 4 | Profesional | 4 | 2 | 1 | 2026-03-01 |
| PC-02 · Contador de impuestos | 24111 · Contadores sintéticos | 4 | Profesional | 5 | 2 | 0 | 2027-03-01 |
| PC-03 · Auxiliar contable | 43111 · Auxiliares contables sintéticos | 2 | Profesional | 2 | 1 | 0 | 2027-02-01 |
| PC-04 · Analista de crédito | 33121 · Analistas de crédito sintéticos | 3 | Tecnólogo | 4 | 2 | 1 | 2027-04-01 |
| PC-05 · Cajero | 42999 | — | Bachiller | 1 | 1 | 0 | 2027-05-01 |
| PC-06 · Coordinador de cobranzas | — | — | Profesional | 2 | 1 | 0 | 2027-05-01 |
| PC-07 · Director financiero | 12110 · Directores financieros sintéticos | 4 | Bachiller | 4 | 1 | 0 | 2027-01-15 |

El perfil lo aprueba una persona: aquí se dice qué le falta frente a su ocupación y qué requisito no se apoya en una tarea.

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
- `10-perfiles/PC-03_auxiliar-contable.docx`
- `10-perfiles/PC-04_analista-de-credito.docx`
- `10-perfiles/PC-05_cajero.docx`
- `10-perfiles/PC-06_coordinador-de-cobranzas.docx`
- `10-perfiles/PC-07_director-financiero.docx`
- Fuentes técnicas: F-03, F-10 (families/criterio-chro/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. Una tarea programada necesita un sí explícito y en esta sesión nadie lo dio. Para correrlo a mano: `/criterio-roles:roles-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

La corrida quedó registrada como `2026-11-16-roles-setup-1`, con la salida en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-roles-setup.md`.