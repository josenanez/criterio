# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo: Portafolio Oil & Gas (prueba)

**Miré:** 66 documentos en 13 proyectos (PRY-199 a PRY-211). Los más usados son .md (28), .docx (15) y .pdf (11). El más reciente es del 2026-10-22.
**Eres:** PMO del portafolio. Lo propuse porque hay varios proyectos.
**Te aviso:** dos días antes del comité semanal. La fecha del próximo (2026-10-29) la propuse yo, porque ninguna acta de comité dice cuándo es.
**En:** presentación, que es el valor por defecto.
**Términos:** quedaron aceptados para la versión 0.8.0 (términos 1.2) a nombre de José Francisco Ñáñez, con fecha 2026-10-23. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.8.0-2026-10-23.md` y `.pdf`. Su SHA-256 empieza por fe830b9a4eee0bc9.

Dejé el archivo `_CRITERIO_PORTAFOLIO.txt` en la carpeta de documentos. No hice ninguna pregunta: en todo tomé el valor sugerido.

### Probé con tres proyectos
Fueron PRY-200, PRY-204 y PRY-202, los de documentación más reciente. El tercer puesto lo empataban otros dos y elegí PRY-202. Las fichas sellaron sin `record_issues`.

| Proyecto | Qué supe | Qué no está |
|---|---|---|
| PRY-200, campaña de perforación del bloque sur | Gerente Carlos Peña, 3.300 M COP aprobados. Declara verde y 84 %. Cierre vigente 2026-10-06, ya pasado. Saqué 26 compromisos de las minutas. | Producto («No aplica»), facultad del gerente y etapa. Falta acta de recibo en 2 de los 4 hitos. |
| PRY-204, integridad de ductos | Gerente Javier Hoyos, 2.400 M COP. Declara verde y 35 %. Cierre 2027-01-13. | Producto, facultad y etapa. Falta acta en los 2 hitos cerrados. |
| PRY-202, gasoducto de interconexión | Gerente Natalia Ospina, 4.200 M COP, producto «transporte de gas». Declara amarillo y 75 %. Cierre 2026-06-05, ya pasado. | Facultad y etapa. Falta acta en 3 de los 4 hitos. |

### Hallazgos
El cálculo levantó 28 señales.

- **PRY-200 declara verde y no se sostiene.**
  - Declara 84 % con los cuatro hitos cerrados en el cronograma, que respaldarían 100 %.
  - Dos hitos cerrados no tienen acta: licencia ambiental y montaje de facilidades.
  - Hay 8 compromisos vencidos sin evidencia. En cinco, la persona dijo en el comité que ya entregó y nadie presentó acta.
  - Ricardo Salas reprogramó «Enviar el documento 1» 6 veces, de 2026-09-30 a 2027-01-15. «Cerrar la prueba 2» lleva 5 reprogramaciones.
  - Tres compromisos no tienen fecha.
  - En las notas del 2026-10-22 se comentó que el proveedor podría no llegar con el equipo completo, y nadie lo anotó como riesgo.
- **PRY-204 declara verde y no se sostiene.**
  - La proyección al cierre supera lo aprobado en 20,5 %.
  - Declara 35 % y el cronograma respalda entre 50 % y 75 %.
  - Dos hitos cerrados no tienen acta.
- **PRY-202, en amarillo.**
  - La proyección supera lo aprobado en 14,4 %.
  - El cierre pasó hace 140 días y declara 75 %.
  - Tres hitos cerrados no tienen acta.
  - Un compromiso de Rubén Cárdenas lleva 18 días vencido. La minuta del 2026-10-21 lo lista con fecha 2026-10-05, anterior a la propia reunión.

El `ficha-pm.json` de PRY-200 quedó guardado aparte, sin mezclar con mi lectura. Los compromisos los saqué yo de las minutas.

### El portafolio completo
Faltan 10 proyectos (55 documentos), en dos lotes, uno tras otro. Calculo unos 15 minutos.

### Lo que le falta a tu carpeta
Ninguno de estos puntos bloquea el análisis.
- Cuatro cronogramas .xml (PRY-204, 206, 209 y 210) no se leen sin instalar algo. El de PRY-204 lo leí como texto. Ese archivo no queda en el sello de lo leído, así que si cambia no lo detectaré solo.
- PRY-201, 203 y 207 solo tienen acta e informe. Sin cronograma ni reuniones no hay contra qué contrastar su avance.
- Siete hitos cerrados en estos tres proyectos no tienen acta de recibo.
- Ningún acta dice hasta dónde decide el gerente sin subir a comité.
- `2026-10-22-notas-reunion.txt` está en la raíz de PRY-200 y no en `30-reuniones/`. Lo leí igual.
- Todos los proyectos tienen una sola versión de cronograma (v1). Si hubo replanificaciones, no están en la carpeta.

La carpeta ya sigue la estructura recomendada de `document-intake`. No moví, renombré ni creé nada dentro de los documentos.

La configuración quedó en `.criterio/portafolio/config.json`. Las fichas están en `estado/records/`. Dejé la salida de esta corrida en `estado/corridas/salida-portfolio-setup.md`, y la corrida quedó registrada como `2026-10-23-portfolio-setup-1`.

Te ofrezco correr el portafolio completo con `/portfolio-scan`. Si tienes gerentes de proyecto con equipo, también puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios.