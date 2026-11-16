# criterio-chro · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada vez,
byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el generador al
sembrar cada defecto; el motor no la ve. Los nombres, las empresas, las personas y los documentos son
inventados, y el estándar de ocupaciones es sintético con la forma exacta de su descarga oficial.

## Las entidades

| Carpeta del material | País | Industria | Estándar | Señales esperadas | Pares de sesgo |
|---|---|---|---|---:|---:|
| `banca-co` | Colombia | banca | La CUOC 2026 (F-03), en un libro con sus hojas y sus columnas | 29 | 1 |
| `control-co` | Colombia | — | La CUOC 2026 (F-03), en un libro con sus hojas y sus columnas | 1 | 1 |
| `control-pe` | Perú | — | O*NET 31.0 (F-02), en una carpeta con sus archivos y sus columnas | 1 | 1 |
| `retail-mx` | México | retail | O*NET 31.0 (F-02), en una carpeta con sus archivos y sus columnas | 22 | 1 |
| `tecnologia-cl` | Chile | tecnologia | O*NET 31.0 (F-02), en una carpeta con sus archivos y sus columnas | 20 | 1 |

Cada una trae su carpeta de talento al 16 de noviembre de 2026, con el periodo de noviembre: la
política de selección en PDF, con su plazo de cobertura, su conservación de los datos y lo que no se
pide, distintos en cada entidad; la descarga del estándar; los perfiles de cargo en Word, con su
ocupación, sus funciones, sus requisitos y su revisión; el registro de vacantes en Excel; una carpeta
por candidato con su hoja de vida en PDF y sus soportes —el diploma, el certificado laboral, la
certificación—; el registro de autorizaciones; la exportación del ATS con cabeceras en inglés y la base
de talento interna.

## Lo que se siembra, y la señal que tiene que levantar

La lista exacta está en la clave de cada entidad, en `esperado`.

| Agente | Lo que se siembra | Señal |
|---|---|---|
| Norma | Un perfil con un código que no está en el estándar, y otro sin código | `profile_without_occupation` |
| Norma | Un perfil que no recoge un conocimiento o una destreza de su ocupación, sin decir por qué | `essential_skill_missing` |
| Norma | Un requisito que no se apoya en ninguna tarea del perfil | `requirement_without_task` |
| Norma | «Hombre menor de 35 años», «Estado civil casado», «Buena presencia»: lo que la política prohíbe pedir; «Gozar de buen estado de salud», «Profesar la religión católica», «Nivel socioeconómico medio alto», «No pertenecer a ningún sindicato»: datos sensibles de la ley del país | `requirement_not_allowed` |
| Norma | Un auxiliar contable que pide un título profesional, y un director financiero que pide el bachillerato sin aceptar experiencia (CUOC 2026, numeral 3.2) | `education_level_inconsistent` |
| Norma | Dos perfiles de la misma ocupación con casi los mismos requisitos | `profiles_overlap` |
| Norma | Un perfil revisado hace más de doce meses | `profile_review_overdue` |
| Cándido | Un título sin diploma, una certificación sin su soporte | `claim_without_support` |
| Cándido | La tarjeta profesional que exige el perfil, vencida antes de la postulación | `certification_expired` |
| Cándido | Un empleo cuyo retiro en la hoja de vida no es el del certificado laboral | `employment_dates_differ` |
| Cándido | Un requisito indispensable sin evidencia en la hoja de vida ni en los soportes | `requirement_not_evidenced` |
| Cándido | Una fotografía en la carpeta del candidato, una fecha de nacimiento o el sexo en la hoja de vida | `protected_data_received` |
| Cándido | Un candidato sin autorización, y otro con la autorización posterior a recibir sus datos | `consent_missing` |
| Cándido | Un candidato no seleccionado cuyo plazo de conservación venció | `retention_exceeded` |
| Cándido | Dos vacantes abiertas después de su plazo de cobertura | `vacancy_past_target` |

## La prueba de sesgo

En cada entidad, dos candidatos de la misma vacante son iguales en todo —sus estudios, sus empleos, sus
soportes, su evidencia, su autorización— salvo en un dato protegido que solo trae el segundo: la
fotografía y la fecha de nacimiento, o el sexo. `evaluar.py` comprueba con `talento.sesgo` que el motor
entregue exactamente lo mismo para los dos, salvo el aviso de lo que excluyó, y que ningún resultado
guarde el valor del dato protegido. **Un par que no da lo mismo es una falla**, aunque todas las señales
estén bien.

## Lo que se parece a un defecto y no lo es

En los controles: lo que un perfil excluye del estándar con su motivo; un nivel de estudios por debajo
con la experiencia como alternativa; «conocimiento del sistema de gestión de seguridad y salud en el
trabajo», que no es la salud de la persona; una revisión que vence mañana; una vacante con su propio
plazo, más largo que el de la política; una autorización del mismo día de la postulación; un empleo con
el mismo mes y otro día en el certificado; una certificación que vence después de la postulación; una
conservación que vence hoy; una brecha entre dos empleos, que no es una señal; y un diploma escaneado
en imagen que la ficha cita como soporte, que no es una fotografía.

## Qué no prueba este material

- **La extracción.** El motor se prueba con la ficha correcta, la de la clave. Que el agente procese el
  perfil y la hoja de vida, los registre bien y no copie el dato protegido lo prueba la ronda.
- **El estándar real.** Las ocupaciones son sintéticas. Que el motor procesa la descarga real de la CUOC
  2026 —sus 682 ocupaciones— y de O*NET 31.0 —sus 1.016— se comprobó el 16 de noviembre de 2026 sobre la
  descarga oficial, fuera del repositorio.
- **Las exportaciones de un ATS concreto.** La del material lleva cabeceras de uso común en inglés; los
  formatos de cada ATS entran con su fuente verificada (hoja de ruta, incremento 3).
- **La documentación de una organización concreta.**
