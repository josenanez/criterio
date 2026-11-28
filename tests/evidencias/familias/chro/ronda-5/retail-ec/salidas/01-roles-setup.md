# /criterio-roles:roles-setup talento/1792345678001-almacenes-del-pacifico-sinteticos

Norma quedó instalada para Almacenes del Pacífico Sintéticos, con el periodo 2026-11 y el estándar O*NET. Procesé los cuatro perfiles de `10-perfiles/`.

- **Configuración:** quedó en `.criterio/perfiles/1792345678001/config.json`. Los datos de umbral (3,5), revisión (12 meses) y lo que no se puede pedir salen de la política de selección.
- **Términos:** aceptados por José Francisco Ñáñez el 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-roles-1.0.0-2026-11-16.md` y en su `.pdf`.
- **Marca:** el archivo `_CRITERIO_TALENTO.txt` quedó en la carpeta de la entidad.

El cálculo encontró también requisitos que la ley o la política no permiten pedir, y perfiles que se solapan. Este reporte no los muestra: los muestran `/criterio-roles:profile-language` y `/criterio-roles:profile-map`.

# Los perfiles contra su ocupación · Almacenes del Pacífico Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Pacífico Sintéticos (1792345678001) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 1.0.0 · **Comando:** `profile-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | PT-04 · Almacenista: el perfil no tiene un código de ocupación que lo ate a un estándar | — | — | — | `10-perfiles/PT-04_almacenista.docx` |
| 2 | Un perfil pasó su fecha de revisión (`profile_review_overdue`) | PT-01 · Cajero de tienda: tocaba revisarlo el 2026-01-10 | — | — | 310 | `10-perfiles/PT-01_cajero-de-tienda.docx` |
| 3 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | PT-01 · Cajero de tienda: «Customer and Personal Service» (conocimiento de la ocupación 41-2011.00 en ONET) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/PT-01_cajero-de-tienda.docx` |
| 4 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | PT-01 · Cajero de tienda: el requisito R3 «Buena presencia» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/PT-01_cajero-de-tienda.docx` |

## El resultado

| Perfil | Ocupación | Nivel | Estudios | Requisitos | Tareas | Del estándar sin recoger | Revisión |
|---|---|---|---|---|---|---|---|
| PT-01 · Cajero de tienda | 41-2011.00 · Cashiers (synthetic) | — | Secundaria | 3 | 1 | 1 | 2026-01-10 |
| PT-02 · Cajero de autoservicio | 41-2011.00 · Cashiers (synthetic) | — | Secundaria | 3 | 1 | 0 | 2027-02-01 |
| PT-03 · Supervisor de tienda | 41-1011.00 · First-Line Supervisors of Retail Sales Workers (synthetic) | — | Licenciatura | 4 | 1 | 0 | 2027-02-01 |
| PT-04 · Almacenista | — | — | Secundaria | 2 | 1 | 0 | 2027-02-01 |

El perfil lo aprueba una persona: aquí se dice qué le falta frente a su ocupación y qué requisito no se apoya en una tarea.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué código O*NET tiene PT-04 Almacenista? → El perfil dice «sin código»; queda vacío hasta que una persona lo confirme.
- ¿Qué fecha de próxima revisión tiene PT-01? → El perfil dice «cada 12 meses», sin fecha; se registra sin fecha y rige la política.

## Fuentes

- `10-perfiles/PT-01_cajero-de-tienda.docx`
- `10-perfiles/PT-04_almacenista.docx`
- Fuentes técnicas: F-02, F-14 (families/criterio-chro/FUENTES.es.md)

---

**Reloj:** no creé la tarea programada porque en esta sesión nadie respondió que sí. Para correrlo a mano: `/criterio-roles:roles-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-16-roles-setup-1`, con la salida en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/corridas/salida-roles-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.