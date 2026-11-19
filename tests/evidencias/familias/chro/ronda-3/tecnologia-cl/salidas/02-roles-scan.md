# /criterio-roles:roles-scan 

La ficha de este periodo ya tenía todos los perfiles de `10-perfiles/`. Los revisé contra el texto de cada perfil y contra la descarga de O*NET, y no hubo que cambiar nada. Las señales son las mismas que dejó el setup; esta corrida no encontró ninguna nueva. El inventario no pudo leer las fotos de candidatos, pero son de la selección (Cándido), no de los perfiles.

# Qué cambió en los perfiles · Nube Austral Software Sintética · periodo 2026-11

**Entidad:** Nube Austral Software Sintética (76543210k) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `roles-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | TI-02 · Analista de soporte: el requisito R4 «Nivel socioeconómico medio alto» pide la situación socioeconómica, que no se puede pedir según Ley 19.628, modificada por la Ley 21.719, art. 2, letra g) (F-13) | — | — | — | `10-perfiles/TI-02_analista-de-soporte.docx` |
| 2 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | TI-03 · Analista de seguridad: el requisito R3 «No pertenecer a ningún sindicato» pide la afiliación sindical, que no se puede pedir según Ley 19.628, modificada por la Ley 21.719, art. 2, letra g) (F-13) | — | — | — | `10-perfiles/TI-03_analista-de-seguridad.docx` |
| 3 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | TI-05 · Líder técnico: el código 15-9999.00 no está en ONET | — | — | — | `10-perfiles/TI-05_lider-tecnico.docx` |
| 4 | Un perfil pasó su fecha de revisión (`profile_review_overdue`) | TI-01 · Desarrollador de software: tocaba revisarlo el 2026-10-01 | — | — | 46 | `10-perfiles/TI-01_desarrollador-de-software.docx` |
| 5 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | TI-01 · Desarrollador de software: «Computers and Electronics» (conocimiento de la ocupación 15-1252.00 en ONET) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/TI-01_desarrollador-de-software.docx` |
| 6 | Dos perfiles comparten la ocupación y la mayor parte de sus requisitos (`profiles_overlap`) | TI-01 · Desarrollador de software y TI-04 · Desarrollador backend: la misma ocupación 15-1252.00 y 100 % de los requisitos en común | — | — | — | `10-perfiles/TI-01_desarrollador-de-software.docx` · `10-perfiles/TI-04_desarrollador-backend.docx` |
| 7 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | TI-02 · Analista de soporte: el requisito R4 «Nivel socioeconómico medio alto» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/TI-02_analista-de-soporte.docx` |

## El resultado

**Perfiles en la ficha:** 5 · **Estándar:** ONET, 3 ocupaciones.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Desde qué importancia de O*NET una destreza es exigible? → 3, propuesta de Norma; la política de selección no lo fija
- ¿Qué nivel de la CINE corresponde a cada forma de nombrar los estudios? → Técnico = 5, Ingeniería = 6, propuesta desde los perfiles

## Fuentes

- `10-perfiles/TI-01_desarrollador-de-software.docx`
- `10-perfiles/TI-02_analista-de-soporte.docx`
- `10-perfiles/TI-03_analista-de-seguridad.docx`
- `10-perfiles/TI-04_desarrollador-backend.docx`
- `10-perfiles/TI-05_lider-tecnico.docx`
- Fuentes técnicas: F-02, F-13 (families/criterio-chro/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-16-roles-scan-1`. Lo que se mostró aquí está guardado en `estado-talento/76543210k-nube-austral-software-sintetica/corridas/salida-roles-scan.md`.