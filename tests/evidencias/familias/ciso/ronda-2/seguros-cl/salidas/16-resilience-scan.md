# /criterio-resilience:resilience-scan 

La ficha del periodo ya traía los incidentes, las revisiones y las pruebas, y el motor no encontró documentos sin registrar. Calculó ocho señales. Los términos estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.

# Qué cambió en la respuesta · Seguros del Sur (sintéticos) · periodo 2026-10

Corte 2026-10-15. En la ficha hay 6 incidentes, 3 revisiones posteriores y 4 pruebas.

**Lo que hay que atender**

| # | Señal | Qué | Responsable | Días |
|---|---|---|---|---|
| 1 | Notificación tarde | INC-SEG-103 → Comisión para el mercado financiero: notificada el 2026-09-23T13:30, 6 horas después del plazo de 24 horas | — | — |
| 2 | Notificación sin hacer | INC-SEG-104 → Clientes afectados: la matriz pide 72 horas y la ficha no registra la notificación | — | — |
| 3 | Prueba de recuperación vencida | Recuperación del centro de datos alterno: última prueba 2026-02-20, tocaba el 2026-08-19 | Jefe de infraestructura | 57 |
| 4 | Restauración vencida | Correo corporativo: última prueba 2026-06-20, tocaba el 2026-09-18 | Jefe de infraestructura | 27 |
| 5 | Contención tardía | INC-SEG-102, alta: contenido en 18 horas y la política da 12 | — | — |
| 6 | Sin contención | INC-SEG-106, alta: detectado el 2026-09-28T16:45 y sin contención registrada; la política da 12 horas | — | — |
| 7 | Restauración sin prueba | Base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | Jefe de infraestructura | — |
| 8 | Sin revisión posterior | INC-SEG-105: cerrado el 2025-08-25… *(en el reporte: 2026-08-25)* y sin revisión; la política da 14 días | — | 37 |

Citas: `00-referencia/matriz-notificaciones.xlsx`, `00-referencia/calendario-continuidad.csv` y los informes y constancias de `70-incidentes/` y `90-continuidad/`. El reporte completo está en `resiliencia/2026-10/reporte-resilience-scan.md`.

**Excluidos sin abrir:** `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`.

**Preguntas con respuesta sugerida (sin interfaz):**
- Las tres revisiones de `80-revisiones/` quedan donde están, sin mover nada.
- Los tres `.gz` de `50-escaneos/` se dejan fuera, porque son del escáner de vulnerabilidades.

Dos correcciones a lo que acabo de mostrar:
- En la fila 8 escribí mal la fecha de cierre. La correcta es 2026-08-25, como dice el reporte del motor.
- En el archivo de la corrida el reporte se guardó tal cual, así que ahí no está el error.

La corrida quedó registrada como `2026-10-15-resilience-scan-1`, con 8 hallazgos. La salida está en `corridas/salida-resilience-scan.md`.

No notifiqué a nadie ni cerré ningún incidente. Quién notifica y qué se hace con cada señal lo decide una persona.