# /criterio-roles:profile-build 

No dejé ningún borrador: el cargo que tocaba armar no tiene una ocupación en el estándar.

**Términos:** están vigentes (versión 1.6, aceptados por José Francisco Ñáñez el 2026-11-16).

**La ocupación:** la instrucción no traía un código ni el nombre de un cargo. Según los documentos, el cargo que toca es **TI-05 · Líder técnico** (`10-perfiles/TI-05_lider-tecnico.docx`). Es el único perfil que no está atado a una ocupación del estándar; los otros cuatro ya tienen la suya.

**Por qué paré:**
- El código que trae el perfil, 15-9999.00, no existe. El motor responde: «el código 15-9999.00 no está en ONET».
- La descarga de O*NET en `00-referencia/onet-31-0-sintetico` no trae el índice de denominaciones, así que no hay dónde buscar «Líder técnico» por su nombre. Ninguna de sus tres ocupaciones (15-1252.00, 15-1232.00 y 15-1212.00) nombra ese cargo.

No escribo una ocupación de memoria. Para seguir, una persona tiene que dar el código O*NET del cargo, o hay que añadir a `00-referencia/` la descarga oficial completa de O*NET con su índice de denominaciones. Después se vuelve a correr `/criterio-roles:profile-build` con el código o el nombre del cargo.

**Registro:** lo que se mostró quedó en `estado-talento/76543210k-nube-austral-software-sintetica/corridas/salida-profile-build.md`, y la corrida quedó registrada como `2026-11-16-profile-build-1`, con el caso 15-9999.00.