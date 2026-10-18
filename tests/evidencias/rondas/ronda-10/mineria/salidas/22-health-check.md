# /criterio-portfolio:health-check PRY-202

# Diagnóstico · PRY-202 Planta de tratamiento de agua · 2026-10-18

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no hubo que registrarlos de nuevo.

**Leí:** 7 documentos, de 2025-12-09 a 2026-10-13. Son 5 en Markdown, 1 CSV y 1 XLSX. Pude leerlos todos. En las otras carpetas busqué el código PRY-202 solo en archivos de texto, no en .docx, .pdf ni .xlsx.

## Dictamen
De 13 afirmaciones evaluadas, 3 están sostenidas, 7 sin sustento y 3 contradichas.

- **Sostenido:**
  - El presupuesto aprobado es 2.400.000.000 COP.
  - Hay un acta de recibo de la ingeniería básica.
  - El cierre pasó del 2026-08-27 al 2026-11-30. CC-01 y el cronograma v2 coinciden en esos 95 días, el 37.8% contra la línea base original.
- **Contradicho:**
  - El estado «Verde». El mismo informe dice que el ensayo de disponibilidad no alcanzó lo pactado y se repite.
  - El avance de 84%. El cronograma v2 marca los 4 hitos como cerrados.
  - El hito «Montaje e instalación» como cerrado.
- **Sin sustento:**
  - Las cifras de comprometido, ejecutado y proyección.
  - Los hitos de detalle y de licencia como cerrados.
  - La autorización de CC-01 por el comité.
  - El plan de arranque acordado con operaciones.
  - La actualización del presupuesto con compras.
  - El ensayo fallido, que solo consta en el informe.

Desde esta carpeta no se puede afirmar el avance real, el gasto real ni que el comité aprobó el cambio. Cinco de los siete documentos son del 10 al 13 de octubre de 2026. No hay nada entre diciembre de 2025 y esa fecha.

## Gobierno
- Sandra Gil figura como patrocinadora y gerente a la vez.
- No hay autoridad declarada en ningún documento.
- La minuta del comité del 2026-10-12 lista como asistentes «Sandra Gil, Sandra Gil»: una sola persona.
- CC-01 dice «Autorizada por el comité» sin fecha, sin nombre y sin acta. Esa minuta no lo menciona.
- El alcance del acta son marcadores en blanco (Componente 1, 2, 3), así que no se puede saber qué amplió CC-01.

## Hitos vencidos sin evidencia
| Hito | Fecha | Días |
|---|---|---|
| Ingeniería de detalle aprobada | 2026-04-23 | 178 |
| Licencia y permisos obtenidos | 2026-06-25 | 115 |

«Montaje e instalación» figura cerrado con fecha vigente 2026-11-30 (futura) y sin acta. No escribo sus días porque el script no los da.

## Dinero (COP)
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 2.400.000.000 | 1.633.608.660 (68.1%) | 1.308.832.360 (54.5%) | 2.358.092.650 (−1.7%) | 766.391.340 |

Las cifras salen de `portafolio.py compute`. Su única fuente es el informe de avance, o sea una declaración. El costo adicional de 190.000.000 COP de CC-01 no aparece en ninguna línea base de presupuesto.

## Lo que se dijo y nadie registró
- Una incidencia: el ensayo de disponibilidad fallido, sin dueño ni fecha de repetición.
- Una dependencia de operaciones: la ventana de parada y el plan de arranque. El acta declara «Ninguna».
- Un compromiso: Carlos Peña debe entregar el «punto 40» el 2026-10-18. Ese punto no está definido en ningún documento y todavía no vence; la próxima corrida lo revisa.

## Lo que esta carpeta no permite saber
- Si el comité aprobó CC-01.
- Quién tiene autoridad sobre el proyecto.
- El avance real.
- El gasto real.
- Qué incluye el alcance.
- Qué pasó entre 2025-12-09 y 2026-10-10. Desde la carpeta no puedo decir de quién es ese silencio.

**Pie de rigor:** las cifras derivadas están copiadas del script. Separé lo declarado de lo probado. Son inferencias mías que «ventana de parada» es una dependencia, que el cronograma v1 no pudo estar cerrado en su fecha, y que el orden de los hitos cerrados no cuadra con la fecha del acta de ingeniería básica. No recomiendo detener, continuar ni reestructurar: eso lo decide quien tiene la facultad.

Puedo llevar las contradicciones y los puntos sin sustento a Sandra Gil como preguntas, una por una. También puedo preparar el punto de comité con la lista de lo que falta.

**Corrida registrada:** `2026-10-18-health-check-1`, 102 segundos, caso PRY-202, 5 señales abiertas. El conteo de documentos quedó sin medir porque el script no lo mide en esta corrida. La salida completa está en `estado/corridas/salida-health-check.md`.