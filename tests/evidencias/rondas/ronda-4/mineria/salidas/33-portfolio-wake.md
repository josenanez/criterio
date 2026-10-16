# /criterio-portfolio:portfolio-wake 

Hoy tocaban el barrido y la confirmación mensual. Vuelvo el 2026-10-16.

- **Términos:** ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15, así que no registré nada nuevo.
- **Barrido:** el índice marcó 23 documentos de PRY-200 como nuevos y 250 de sus citas como rotas. No es así. La ficha de PRY-200 se escribió hoy a las 20:58 con esos documentos, y ninguno es posterior. Quedó sin sellar, y por eso el índice la trata como no leída.
- **Sellado:** corrí `/portfolio-scan` sobre PRY-200. El script rechazó el sello porque la ficha no se reescribió en esta corrida. No releí los 23 documentos ni forcé el sello, y el aviso se repetirá en cada barrido hasta que la ficha se reescriba y se selle.
- **Umbrales:** no recalculé nada y ninguno cruzó.
- **Confirmación:** dejé cinco preguntas sin respuesta, porque no había a quién preguntar. Son los patrocinadores con más de 12 meses de antigüedad en PRY-204, PRY-209, PRY-205, PRY-210 y PRY-200. No revisé presupuesto aprobado ni fecha de cierre.
- **Peticiones:** no corrí `requests`, porque `due` no devolvió esa tarea.

Dejé registradas las dos tareas hechas y la corrida. La salida está en `/home/claude/banco/ronda-4/mineria/espacio/estado/corridas/salida-portfolio-wake.md`.