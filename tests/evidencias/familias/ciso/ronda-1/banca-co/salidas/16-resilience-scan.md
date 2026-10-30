# /criterio-resilience:resilience-scan 

No hay documentos nuevos desde la corrida anterior. La ficha ya traía los 6 incidentes, las 3 revisiones y las 4 pruebas, así que solo se recalcularon las señales: salieron 8. Las tres revisiones están en `80-revisiones/` y el inventario sugiere que irían en `70-incidentes/`.

Los términos (versión 1.3) ya estaban aceptados por José Francisco Ñáñez el 2026-10-15, así que no registré nada nuevo. El motor no pidió nada que no existiera. Los 3 archivos de credenciales, llaves y respaldos no se abrieron:
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

Las 8 señales, tal como las calculó el motor:

| # | Señal | Detalle |
|---|---|---|
| 1 | Notificación tarde | INC-BCO-103 a la Superintendencia Financiera: se notificó el 2026-09-23T13:30, 6 horas después del plazo de 24 horas. |
| 2 | Notificación sin hacer | INC-BCO-104 a clientes afectados: la matriz pide 72 horas y la ficha no registra la notificación. |
| 3 | Prueba vencida | Recuperación del centro de datos alterno: la última fue el 2026-02-20 y tocaba el 2026-08-19 (57 días de atraso). |
| 4 | Restauración vencida | Correo corporativo: la última fue el 2026-06-20 y tocaba el 2026-09-18 (27 días de atraso). |
| 5 | Contención tardía | INC-BCO-102 (alta): contenido en 30 horas y la política da 24. |
| 6 | Sin contención | INC-BCO-106 (alta): detectado el 2026-09-28T16:45 y sin contención registrada. |
| 7 | Restauración sin prueba | Base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días. |
| 8 | Sin revisión posterior | INC-BCO-105: cerrado el 2026-08-25 y sin revisión; la política da 10 días (41 días de atraso). |

Quién notifica y qué se hace con cada señal queda en manos de una persona.

La salida quedó en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-resilience-scan.md` y la corrida se registró como `2026-10-15-resilience-scan-1`. El reporte completo está en `resiliencia/2026-10/reporte-resilience-scan.md`, en esa misma carpeta de estado.