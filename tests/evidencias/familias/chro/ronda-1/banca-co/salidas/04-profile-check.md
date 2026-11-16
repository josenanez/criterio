# /criterio-roles:profile-check 

Términos vigentes (versión 1.5, aceptados por José Francisco Ñáñez el 2026-11-16). Revisé los siete perfiles contra su ocupación. Este es el reporte que escribió el motor, tal cual:

# Los perfiles contra su ocupación · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación (`education_level_inconsistent`) | PC-03 · Auxiliar contable: pide «Profesional» (CINE 6); la ocupación 43111 es de nivel de competencia 2, que suele exigir CINE 2 a 4 (CUOC 2026, numeral 3.2): pide más de lo que la ocupación exige | — | — | — | `10-perfiles/PC-03_auxiliar-contable.docx` |
| 2 | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación (`education_level_inconsistent`) | PC-07 · Director financiero: pide «Bachiller» (CINE 3); la ocupación 12110 es de nivel de competencia 4, que suele exigir CINE 6 a 8 (CUOC 2026, numeral 3.2): pide menos de lo que la ocupación exige | — | — | — | `10-perfiles/PC-07_director-financiero.docx` |
| 3 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PC-05 · Cajero: el código 42999 no está en CUOC | — | — | — | `10-perfiles/PC-05_cajero.docx` |
| 4 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PC-06 · Coordinador de cobranzas: el perfil no tiene un código de ocupación que lo ate a un estándar | — | — | — | `10-perfiles/PC-06_coordinador-de-cobranzas.docx` |
| 5 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PC-01 · Contador: «Legislación tributaria» (conocimiento de la ocupación 24111 en CUOC) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PC-01_contador.docx` |
| 6 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PC-04 · Analista de crédito: «Análisis de necesidades» (destreza de la ocupación 33121 en CUOC) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PC-04_analista-de-credito.docx` |
| 7 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PC-02 · Contador de impuestos: el requisito R5 «Hombre menor de 35 años» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 8 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PC-07 · Director financiero: el requisito R4 «Dominio del inglés de negocios» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PC-07_director-financiero.docx` |

## El resultado

| Perfil | Ocupación | Nivel | Estudios | Requisitos | Tareas | Del estándar sin recoger | Revisión |
|---|---|---|---|---|---|---|---|
| PC-01 · Contador | 24111 · Contadores sintéticos | 4 | Profesional | 4 | 2 | 1 | — |
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

- Entidad, identificación fiscal y país → Banco Cordillera Sintético, NIT 901555123, CO (tomado de la carpeta y la política; prueba sin interfaz)
- Periodo → 2026-11
- Estándar de ocupaciones y su descarga → CUOC, 00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx
- Equivalencia de estudios con la CINE → Bachiller 3, Tecnólogo 5, Profesional 6
- Cada cuántos meses se revisa un perfil → La política no lo dice; sin fijar
- Lo que la política prohíbe pedir → edad, sexo, estado civil, fotografía (politica-de-seleccion.pdf, «Lo que no se pide»)
- Marcar la carpeta raíz → sí
- Términos → aceptados por José Francisco Ñáñez, 2026-11-16

## Fuentes

- `10-perfiles/PC-01_contador.docx`
- `10-perfiles/PC-02_contador-de-impuestos.docx`
- `10-perfiles/PC-03_auxiliar-contable.docx`
- `10-perfiles/PC-04_analista-de-credito.docx`
- `10-perfiles/PC-05_cajero.docx`
- `10-perfiles/PC-06_coordinador-de-cobranzas.docx`
- `10-perfiles/PC-07_director-financiero.docx`
- Fuentes técnicas: F-03, F-10 (families/criterio-chro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-16-profile-check-1`, con 13 hallazgos. La salida está en `corridas/salida-profile-check.md`, dentro de la carpeta de estado.