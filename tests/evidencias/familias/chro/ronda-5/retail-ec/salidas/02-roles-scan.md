# /criterio-roles:roles-scan 

El inventario marca los 43 archivos como nuevos porque es el primero que se guarda. Los cuatro perfiles de `10-perfiles/` ya estaban en la ficha del periodo desde el setup y su texto no cambió, así que no agregué nada. Las señales son las mismas que encontró el setup; no aparece ninguna nueva.

# Qué cambió en los perfiles · Almacenes del Pacífico Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Pacífico Sintéticos (1792345678001) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 1.0.0 · **Comando:** `roles-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PT-01 · Cajero de tienda: el requisito R3 «Buena presencia» pide apariencia, que no se puede pedir según la política de selección de la organización | — | — | — | `10-perfiles/PT-01_cajero-de-tienda.docx` |
| 2 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PT-03 · Supervisor de tienda: el requisito R4 «Profesar la religión católica» pide la religión o las convicciones, que no se puede pedir según Ley Orgánica de Protección de Datos Personales, art. 4 (F-14) | — | — | — | `10-perfiles/PT-03_supervisor-de-tienda.docx` |
| 3 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PT-04 · Almacenista: el requisito R2 «Mujer entre 20 y 30 años» pide edad, que no se puede pedir según la política de selección de la organización | — | — | — | `10-perfiles/PT-04_almacenista.docx` |
| 4 | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir (`requirement_not_allowed`) | PT-04 · Almacenista: el requisito R2 «Mujer entre 20 y 30 años» pide sexo, que no se puede pedir según la política de selección de la organización | — | — | — | `10-perfiles/PT-04_almacenista.docx` |
| 5 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PT-04 · Almacenista: el perfil no tiene un código de ocupación que lo ate a un estándar | — | — | — | `10-perfiles/PT-04_almacenista.docx` |
| 6 | Un perfil pasó su fecha de revisión (`profile_review_overdue`) | PT-01 · Cajero de tienda: tocaba revisarlo el 2026-01-10 | — | — | 310 | `10-perfiles/PT-01_cajero-de-tienda.docx` |
| 7 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PT-01 · Cajero de tienda: «Customer and Personal Service» (conocimiento de la ocupación 41-2011.00 en ONET) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PT-01_cajero-de-tienda.docx` |
| 8 | Dos perfiles comparten la ocupación y la mayor parte de sus requisitos (`profiles_overlap`) | PT-01 · Cajero de tienda y PT-02 · Cajero de autoservicio: la misma ocupación 41-2011.00 y 67 % de los requisitos en común | — | — | — | `10-perfiles/PT-01_cajero-de-tienda.docx` · `10-perfiles/PT-02_cajero-de-autoservicio.docx` |
| 9 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PT-01 · Cajero de tienda: el requisito R3 «Buena presencia» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PT-01_cajero-de-tienda.docx` |

## El resultado

**Perfiles en la ficha:** 4 · **Estándar:** ONET, 3 ocupaciones.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué código O*NET tiene PT-04 Almacenista? → El perfil dice «sin código»; queda vacío hasta que una persona lo confirme.
- ¿Qué fecha de próxima revisión tiene PT-01? → El perfil dice «cada 12 meses», sin fecha; se registra sin fecha y rige la política.

## Fuentes

- `10-perfiles/PT-01_cajero-de-tienda.docx`
- `10-perfiles/PT-02_cajero-de-autoservicio.docx`
- `10-perfiles/PT-03_supervisor-de-tienda.docx`
- `10-perfiles/PT-04_almacenista.docx`
- Fuentes técnicas: F-02, F-14 (families/criterio-chro/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-16-roles-scan-1`, y lo que se mostró quedó guardado en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/corridas/salida-roles-scan.md`.