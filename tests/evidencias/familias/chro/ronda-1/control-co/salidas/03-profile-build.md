# /criterio-roles:profile-build 

No armé ningún borrador de perfil, porque el argumento no indica qué ocupación usar: no trae un código de la CUOC ni el nombre de un cargo. Los documentos tampoco sugieren una:

- **Estándar:** la hoja Ocupación de `PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx` tiene tres ocupaciones, y las tres ya tienen perfil en `10-perfiles/`:
  - 24111 Contadores sintéticos → PC-11
  - 43111 Auxiliares contables sintéticos → PC-12
  - 25120 Desarrolladores de software sintéticos → PC-13
- **Vacantes:** `registro-vacantes.xlsx` solo menciona esos tres perfiles (VAC-31 → PC-11, VAC-32 → PC-13, VAC-33 → PC-12).

Si yo eligiera una ocupación, la estaría inventando, así que paré ahí. Los términos están vigentes, aceptados por José Francisco Ñáñez el 2026-11-16, y no hubo que registrarlos de nuevo.

Dejé registrado lo que se mostró en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-profile-build.md`. La corrida quedó como `2026-11-16-profile-build-1`.

Para tener el borrador, vuelve a correr `/criterio-roles:profile-build` con el código de una ocupación (por ejemplo, `24111`) o con el nombre del cargo.