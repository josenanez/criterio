# /criterio-roles:profile-build 

No armé ningún borrador porque no hay ocupación para armarlo.

- **El argumento no trae una ocupación.** Solo trae las instrucciones de la prueba: ni un código ni el nombre de un cargo.
- **Los documentos no sugieren ninguna nueva.**
  - La descarga del estándar (`00-referencia/onet-31-0-sintetico/Occupation Data.xlsx`) trae dos ocupaciones, y las dos ya tienen perfil:
    - 15-1232.00 · Computer User Support Specialists (synthetic) tiene el perfil SA-01 · Analista de soporte.
    - 41-2011.00 · Cashiers (synthetic) tiene el perfil SA-02 · Cajero.
  - Las tres vacantes del registro también tienen perfil: VAC-41 tiene SA-01, y VAC-42 y VAC-43 tienen SA-02.
- **Tampoco se puede buscar un cargo por su nombre.** Esa descarga de O*NET no trae el índice de nombres de cargo (el archivo Alternate Titles).

Como la prueba pide no inventar lo que no existe, terminé ahí. No escribí nada en `perfiles/borradores/` ni en `10-perfiles/`. Los términos estaban vigentes (los aceptó José Francisco Ñáñez el 2026-11-16), así que no hubo que registrar una aceptación nueva.

Lo que le mostré a la persona quedó en `estado-talento/20601234567-servicios-andinos-control-sinteticos/corridas/salida-profile-build.md`. La corrida quedó registrada como `2026-11-16-profile-build-1`, sin hallazgos y sin `--caso`, porque no había un código de ocupación que poner.

Para armar un perfil, hay que correr otra vez `/criterio-roles:profile-build <código>` con el código de una ocupación que esté en la descarga. Si no está, primero hay que poner en `00-referencia/` la descarga oficial de O*NET 31.0 que la incluya.