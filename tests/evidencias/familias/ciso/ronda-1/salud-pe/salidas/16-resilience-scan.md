# /criterio-resilience:resilience-scan 

Corrí `resilience-scan` para Clínica del Pacífico (sintética), periodo 2026-10, con fecha 2026-10-15. Salieron 8 señales y la corrida quedó registrada como `2026-10-15-resilience-scan-1`.

Los términos de esta versión ya estaban aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-15, así que no registré nada. La ficha del periodo ya tenía los 6 incidentes, las 3 revisiones y las 4 pruebas, y coincide con los documentos. Tras leerlos, el motor no pidió llevar nada más.

**Lo que hay que atender (las cifras y fechas las dio el motor):**
1. **INC-CLI-103:** se notificó a la Superintendencia de salud 6 horas después del plazo de 24.
2. **INC-CLI-104:** la matriz pide notificar a los clientes afectados y la ficha no registra esa notificación.
3. **Recuperación del centro de datos alterno:** la última prueba es del 2026-02-20 y tocaba el 2026-08-19, con 57 días de atraso.
4. **Restauración del correo corporativo:** la última prueba es del 2026-06-20 y tocaba el 2026-09-18, con 27 días de atraso.
5. **INC-CLI-102:** de severidad alta, se contuvo en 18 horas y la política da 12.
6. **INC-CLI-106:** de severidad alta, está sin contención registrada y la política da 12 horas.
7. **Restauración de la base de clientes:** está en el calendario y no hay ninguna prueba registrada.
8. **INC-CLI-105:** cerrado el 2026-08-25 sin revisión posterior, con 31 días y un plazo de 20.

No se abrieron tres archivos que el motor excluye por ser credenciales, llaves o respaldos:
- `credenciales-vpn.txt`
- `servidor-web.pem`
- `respaldo-correo-2026-06-20.zip`

Conviene sacarlos de la carpeta.

El inventario también marcó las tres revisiones de `80-revisiones/` como fuera de lugar, porque irían en `70-incidentes/`. Ya están en la ficha.

No notifiqué a nadie ni ejecuté ninguna prueba; quién actúa sobre cada señal es de una persona. Las respuestas a las preguntas sin interfaz son las sugeridas desde los documentos y están en el reporte.

El reporte está en `estado-seguridad/…/resiliencia/2026-10/reporte-resilience-scan.md`. Lo que te mostré está guardado en `estado-seguridad/…/corridas/salida-resilience-scan.md`.