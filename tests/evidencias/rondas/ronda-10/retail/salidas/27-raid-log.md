# /criterio-portfolio:raid-log portafolio

Armé el RAID del portafolio y la corrida quedó registrada como `2026-10-18-raid-log-1`. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-18), así que no los volví a registrar. El texto completo está en `estado/corridas/salida-raid-log.md`.

**De dónde sale:** las 13 fichas (PRY-199 a PRY-211), con los informes de avance, las actas de constitución y las minutas de reunión que citan. No había un RAID previo con historial de movimiento.

## RAID: portafolio al 2026-10-18
13 riesgos, 0 supuestos, 21 incidencias y 6 dependencias, 40 ítems en total. Los 40 están sin doliente, sin fecha, sin probabilidad y sin impacto. Solo uno es un riesgo dicho en reunión y no registrado formalmente.

No puedo medir "sin movimiento". Cada proyecto tiene un solo informe y ningún ítem trae fecha de último movimiento, así que no hay dos períodos que comparar.

**Reclasificado:** los 6 ítems "el proveedor no ha confirmado la fecha de la última entrega" (PRY-200, 202, 207, 208, 209 y 210) venían como riesgo. Pasan a dependencia declarada, no acordada. Dependen de un tercero y ya es un hecho que no confirmó.

**Dependencias entre proyectos:** las 13 actas dicen "Ninguna declarada". Por eso no hay nada que cruzar. Eso no prueba que no existan, solo que nadie las declaró.

### Necesitan decisión ahora
| Id | Qué | Por qué sube |
|---|---|---|
| PRY-200-3, PRY-201-2 | Hallazgo de seguridad en los medios de pago | No tiene doliente ni fecha de resolución, y ambos proyectos declaran verde. |
| PRY-200-2, 201-3, 203-3, 204-2, 210-2 | La prueba de carga de temporada no alcanzó el umbral y se repite | Es el mismo problema en cinco proyectos, con la temporada cerca. |
| PRY-199-4, 201-4, 203-4, 204-3, 207-3, 208-3 | Despliegue reprogramado por el congelamiento de fin de año, sin cronograma posterior a v1 que lo recoja | Afecta a seis proyectos. En PRY-208 la fecha fin de la ficha (2026-02-13) ya pasó. |
| PRY-206-3 | El proveedor podría no llegar con el equipo completo para la siguiente fase | Hay una revisión con el proveedor comprometida para 2026-10-28 (Óscar Ramírez). |

### Detectados en reuniones, no registrados
Solo uno: PRY-206-3, dicho en las notas de reunión del 2026-10-18 ("nadie lo anotó como riesgo"). Las demás minutas solo traen tablas de compromisos, y no agregué riesgos que nadie dijo.

### Dependencias en riesgo
Las seis dependencias de proveedor están sin confirmar. En PRY-200, 202, 207 y 208 tampoco hay contrato de proveedor en la carpeta.

### Registro completo
Los 40 ítems con tipo, descripción y último movimiento están en el archivo. Probabilidad, impacto, doliente y fecha figuran "no dicho" en todos.

## Lo que no sé
- Si los textos repetidos entre proyectos son el mismo hecho o texto de plantilla de los informes. La rotación del desarrollador aparece en 6 proyectos y el cambio de regulación de datos personales en 7. No lo contrasté con otra fuente.
- La fecha "desde" de una incidencia es la del informe que la reporta, no la de cuando ocurrió.
- Si algún ítem tiene doliente fuera de los documentos.

## Después
Puedo subir a comité los cuatro grupos de arriba con la decisión formulada. También puedo proponer dolientes para los 40 ítems; propondría, no asignaría. Como esta sesión es de prueba sin interfaz, no hice ninguna de las dos.

*Pie de rigor: borrador de trabajo hecho solo con los documentos citados, sin asesoría. La verificación es tuya.*