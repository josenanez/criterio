# /criterio-resilience:resilience-scan 

Corrí el escaneo de resiliencia del periodo 2026-10 para Nube Austral Software Sintética y quedó con 8 señales por atender. La ficha del periodo ya tenía los 6 incidentes, las 3 revisiones y las 4 pruebas, y `record_issues` salió vacío. No la modifiqué.

No verifiqué la ficha contra los textos de los informes. Me apoyé en que el motor no reportó documentos faltantes.

Los términos (versión 1.3) ya estaban aceptados a nombre de José Francisco Ñáñez con fecha 2026-10-15. No hizo falta registrarlos de nuevo. Pasé `--today 2026-10-15` en cada llamada que lo acepta.

Estas son las 8 señales, con las cifras y fechas tal como las calculó el motor:
- **Notificaciones tarde o sin hacer (2):**
  - INC-NUB-103 a la Agencia de ciberseguridad: notificada el 2026-09-23T13:30, 6 horas después del plazo de 24 horas.
  - INC-NUB-104 a los clientes afectados: la matriz pide 72 horas y la ficha no registra la notificación.
- **Contención fuera de plazo (2):**
  - INC-NUB-102: se contuvo en 14 horas y la política da 8.
  - INC-NUB-106: no tiene contención registrada, pasado el plazo de 8 horas.
- **Prueba de continuidad vencida (1):** la recuperación del centro de datos alterno tocaba el 2026-08-19 y la última es del 2026-02-20.
- **Pruebas de restauración vencidas (2):**
  - Correo corporativo: tocaba el 2026-09-18 y la última es del 2026-06-20.
  - Base de clientes: no hay ninguna prueba registrada.
- **Revisión posterior faltante (1):** INC-NUB-105 se cerró el 2026-08-25 y no tiene revisión, con 37 días de atraso.

No abrí tres archivos que el motor excluye por ser credenciales, llaves o respaldos:
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

No notifiqué a nadie ni ejecuté ninguna prueba o restauración. Nadie respondió preguntas en esta sesión y no hice ninguna.

El reporte lo escribió el motor en `estado-seguridad/…/resiliencia/2026-10/reporte-resilience-scan.md`. Lo que te mostré, tal cual, está en `estado-seguridad/…/corridas/salida-resilience-scan.md`. La corrida quedó registrada como `2026-10-15-resilience-scan-1` con 8 hallazgos.