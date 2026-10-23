# /criterio-portfolio:portfolio-scan 

Terminé el barrido. Leí 69 de los 93 documentos y escribí y sellé 10 fichas nuevas: PRY-199, 200, 201, 203, 204, 205, 206, 207, 208 y 210. PRY-202, 209 y 211 no tuvieron cambios y no se releyeron.

- **Términos:** vigentes en la versión 0.8.0, a nombre de José Francisco Ñáñez, 2026-10-23.
- **No se pudo leer:** nada. El inventario marcó 9 cronogramas `.xml` como no legibles, pero el conversor los leyó todos. Leí 6 de ellos.
- **`entrada/`:** no existe, así que no moví ni dejé pendiente ningún archivo.
- **Campos sin dato:** 24 en `not_found`. La autoridad y la fase no aparecen en ningún documento de los 10 proyectos. El producto falta en PRY-201, 205, 206 y 210, porque el acta dice «No aplica».
- **Tiempo:** la corrida midió 418 segundos. El script cuenta 80 hallazgos en los 13 proyectos, incluidos PRY-202, 209 y 211.

Lo principal que dejó el barrido:
- **Hitos cerrados sin acta:** PRY-206 (los 3 hitos), PRY-210 (los 4) y PRY-200 (3 de 5).
- **Cierre comprometido ya pasado:** PRY-200, 203, 205 y 210. Los tres primeros declaran verde y PRY-210 amarillo.
- **Cronograma v2 con la solicitud de cambio sin decisión:** PRY-204 y PRY-208. PRY-205 tiene dos solicitudes pendientes y ningún cronograma.
- **Facturas sin respaldo de acta:**
  - PRY-208 radicó una factura con los tres entregables aún pendientes.
  - PRY-204 radicó dos facturas antes de la fecha del entregable, y una supera su valor.
  - PRY-200 radicó una factura que no nombra los entregables, y solo uno tiene acta.
- **Compromisos de PRY-204:** son 26: 3 cumplidos con acta, 8 vencidos y 15 abiertos. «Cerrar la prueba 2» se reprogramó 6 veces. La última fecha sale de las notas como «02/01/2027»: la leí día/mes (2027-01-02) y falta confirmarla con el gerente.
- **`ficha-pm.json` de PRY-204:** la guardé entera en `pm_record`, sin fusionarla con mi lectura.

Dejé la salida completa y el rastro de la corrida en `estado/corridas/`, y la instantánea en `estado/snapshots/2026-10-23.json`. Con más de un proyecto con ficha, puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`.

Archivos en `estado/corridas/`:
- `salida-portfolio-scan.md`
- `2026-10-23-portfolio-scan-1.md`