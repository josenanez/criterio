# /criterio-roles:profile-build 

Armé un borrador de perfil para el cargo de Almacenista con el código **43-5081.00 Stockers and Order Fillers (synthetic)**. Una persona tiene que confirmar ese código y aprobar el perfil.

**Términos:** están vigentes (versión 1.6, aceptados por José Francisco Ñáñez el 2026-11-16), así que no hubo que registrarlos otra vez.

**Por qué esta ocupación.** El argumento no traía un código ni un cargo. Tomé el que señalan los documentos: según el último reporte de revisión de perfiles, PT-04 Almacenista es el único perfil sin ocupación. La descarga de O*NET no trae un índice de nombres de cargo, así que no pude buscar «Almacenista» por nombre. Entre las 3 ocupaciones de la descarga, la que corresponde es la de «Receive and store items».

**Lo que devuelve el motor** para 43-5081.00:
- Una función: «Receive and store items».
- Zona de preparación: 2.
- Nivel de competencia: ninguno.
- Destrezas y conocimientos con importancia de 3.5 o más (el umbral de la organización): ninguno.

**El borrador:**

| Id | Contenido | Tarea | ¿Viene del estándar? | Fuente |
|---|---|---|---|---|
| T1 | Tarea: recibir y almacenar la mercancía | — | sí, tarea 1000 | O*NET 43-5081.00 |
| R1 | Manejo de inventario (conocimiento) | T1 | no, es de la organización | PT-04, R1 |
| R2 | Estudios: Secundaria (CINE 3 según la configuración) | T1 | no, es de la organización | PT-04 |

El requisito R2 de PT-04, «Mujer entre 20 y 30 años», no pasó al borrador: pide edad y sexo, y la política de selección prohíbe pedirlos. Con O*NET el motor no compara los estudios con la ocupación.

**Lo que decide la persona** (entre paréntesis, la respuesta que tomé de los documentos):
1. **Nivel de estudios:** Secundaria, CINE 3, como en PT-04.
2. **Experiencia en lugar del título:** PT-04 no lo dice; lo decide quien aprueba.
3. **Si R1 es indispensable:** sí, como en PT-04.
4. **Qué se excluye del estándar:** nada, porque no trae destrezas ni conocimientos sobre el umbral.
5. **El código 43-5081.00:** hasta que alguien lo confirme, PT-04 sigue sin ocupación.

El borrador quedó en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/perfiles/borradores/43-5081.00-2026-11-16.md`, con «BORRADOR» en la primera línea; no escribí nada en `10-perfiles/`. La corrida quedó registrada como `2026-11-16-profile-build-1`, y el mensaje que mostré quedó en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/corridas/salida-profile-build.md`.

Fuente: O*NET 31.0 Database, USDOL/ETA (CC BY 4.0), procesada.