# /criterio-roles:roles-setup talento/76543210k-nube-austral-software-sintetica

Norma quedó instalada sobre Nube Austral Software Sintética. El primer reporte encontró cuatro puntos para atender en los perfiles; nada de esto aprueba un perfil, eso lo decide una persona.

**Respuestas tomadas de los documentos, una por pregunta:**
1. **Carpeta:** solo había una, `talento/76543210k-nube-austral-software-sintetica`, con las seis subcarpetas de la estructura. Tomé esa.
2. **Entidad:** Nube Austral Software Sintética, RUT 76543210-K, Chile.
3. **Periodo:** 2026-11.
4. **Estándar:** O*NET 31.0 (versión sintética), en `00-referencia/onet-31-0-sintetico`. Lo comprobé con la ocupación 15-1252.00, que trae «Software Developers (synthetic)» con sus destrezas, su conocimiento y su zona.
5. **Desde qué importancia una destreza es exigible:** 3. **Lo propuse yo, porque la política no lo fija;** tiene que confirmarlo una persona.
6. **Niveles de estudio frente a la CINE:** Técnico = 5 e Ingeniería = 6, propuestos a partir de los perfiles. Con O*NET esta comparación no se calcula.
7. **Revisión de cada perfil:** cada 12 meses, según la política de selección.
8. **Lo que no se pide:** edad, sexo, estado civil y fotografía, según la política.
9. **Dónde guardo lo que encuentro:** `estado-talento/76543210k-nube-austral-software-sintetica`.
10. **Marca de la carpeta:** sí. Dejé `_CRITERIO_TALENTO.txt` en la carpeta de la entidad.

**Términos (versión 1.6):** los mostré tal cual y quedaron aceptados a nombre de José Francisco Ñáñez con fecha 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-roles-0.1.0-2026-11-16.md` y en `.pdf`. La configuración quedó en `.criterio/perfiles/76543210k/config.json`.

Procesé los cinco perfiles de `10-perfiles/` contra O*NET. En el cálculo salieron 7 señales; este reporte trae las 4 que le tocan. Las otras 3 se ven con dos comandos más:
- `/criterio-roles:profile-language` muestra los requisitos que la ley o la política no permiten pedir.
- `/criterio-roles:profile-map` muestra los perfiles que se solapan.

---

# Los perfiles contra su ocupación · Nube Austral Software Sintética · periodo 2026-11

**Entidad:** Nube Austral Software Sintética (76543210k) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar (`profile_without_occupation`) | TI-05 · Líder técnico: el código 15-9999.00 no está en ONET | — | — | — | `10-perfiles/TI-05_lider-tecnico.docx` |
| 2 | Un perfil pasó su fecha de revisión (`profile_review_overdue`) | TI-01 · Desarrollador de software: tocaba revisarlo el 2026-10-01 | — | — | 46 | `10-perfiles/TI-01_desarrollador-de-software.docx` |
| 3 | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica (`essential_skill_missing`) | TI-01 · Desarrollador de software: «Computers and Electronics» (conocimiento de la ocupación 15-1252.00 en ONET) no está en el perfil, ni el perfil dice por qué no aplica | — | — | — | `10-perfiles/TI-01_desarrollador-de-software.docx` |
| 4 | Un requisito del perfil no se apoya en ninguna de sus tareas (`requirement_without_task`) | TI-02 · Analista de soporte: el requisito R4 «Nivel socioeconómico medio alto» no se apoya en ninguna tarea del perfil | — | — | — | `10-perfiles/TI-02_analista-de-soporte.docx` |

## El resultado

| Perfil | Ocupación | Nivel | Estudios | Requisitos | Tareas | Del estándar sin recoger | Revisión |
|---|---|---|---|---|---|---|---|
| TI-01 · Desarrollador de software | 15-1252.00 · Software Developers (synthetic) | — | Ingeniería | 2 | 1 | 1 | 2026-10-01 |
| TI-02 · Analista de soporte | 15-1232.00 · Computer User Support Specialists (synthetic) | — | Técnico | 4 | 1 | 0 | 2027-03-01 |
| TI-03 · Analista de seguridad | 15-1212.00 · Information Security Analysts (synthetic) | — | Ingeniería | 3 | 1 | 0 | 2027-03-01 |
| TI-04 · Desarrollador backend | 15-1252.00 · Software Developers (synthetic) | — | Ingeniería | 3 | 1 | 0 | 2027-03-01 |
| TI-05 · Líder técnico | 15-9999.00 | — | Ingeniería | 1 | 1 | 0 | 2027-03-01 |

El perfil lo aprueba una persona: aquí se dice qué le falta frente a su ocupación y qué requisito no se apoya en una tarea.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Desde qué importancia de O*NET una destreza es exigible? → 3, propuesta de Norma; la política de selección no lo fija
- ¿Qué nivel de la CINE corresponde a cada forma de nombrar los estudios? → Técnico = 5, Ingeniería = 6, propuesta desde los perfiles

## Fuentes

- `10-perfiles/TI-01_desarrollador-de-software.docx`
- `10-perfiles/TI-02_analista-de-soporte.docx`
- `10-perfiles/TI-05_lider-tecnico.docx`
- Fuentes técnicas: F-02, F-13 (families/criterio-chro/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque nadie dio un sí explícito. Para revisar lo que toca, se corre a mano con `/criterio-roles:roles-wake`.

La corrida quedó registrada como `2026-11-16-roles-setup-1`, y lo que se muestra aquí quedó en `estado-talento/76543210k-nube-austral-software-sintetica/corridas/salida-roles-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.