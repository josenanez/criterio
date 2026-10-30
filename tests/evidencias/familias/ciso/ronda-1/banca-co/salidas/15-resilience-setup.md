# /criterio-resilience:resilience-setup seguridad/901555123-banco-cordillera-sintetico

Amparo quedó instalada sobre Banco Cordillera Sintético (901555123), periodo 2026-10, con corte 2026-10-15. La primera ficha tiene 8 señales. Este es el reporte de `incident-timeline`; las otras señales salen con `notifications` y `continuity-tests`.

**Lo que hay que atender (`incident-timeline`)**

| # | Qué | Cita |
|---|---|---|
| 1 | INC-BCO-102 (acceso indebido a una cuenta privilegiada, alta) se contuvo en 30 horas y la política da 24. | `70-incidentes/INC-BCO-102_informe.docx` |
| 2 | INC-BCO-106 (malware en una estación de finanzas, alta) se detectó el 2026-09-28 16:45 y no tiene contención registrada, pasado el plazo de 24 horas. | `70-incidentes/INC-BCO-106_informe.docx` |
| 3 | INC-BCO-105 (correo de suplantación, baja) se cerró el 2026-08-25 y no tiene revisión posterior. La política da 10 días y van 41 de retraso. | `70-incidentes/INC-BCO-105_informe.docx` |

**Línea de tiempo**

| Incidente | Severidad | Horas hasta contener | Plazo (h) | Cierre | Revisión |
|---|---|---|---|---|---|
| INC-BCO-105 | baja | 30 | 168 | 2026-08-25 | — |
| INC-BCO-101 | crítica | 3,5 | 4 | 2026-09-08 | 2026-09-12 |
| INC-BCO-102 | alta | 30 | 24 | 2026-09-15 | 2026-09-20 |
| INC-BCO-103 | crítica | 3,5 | 4 | 2026-09-26 | 2026-09-30 |
| INC-BCO-106 | alta | sin contención | 24 | abierto | — |
| INC-BCO-104 | media | 20 | 72 | abierto | — |

**Qué quedó registrado**
- **Plazos de la política** (versión 2): contención de 4, 24, 72 y 168 horas según la severidad, en la sección 5. La revisión posterior es a los 10 días calendario del cierre, en la sección 7. Los acepté como propuesta porque nadie respondió.
- **Fichas:** 6 incidentes, 3 revisiones y 4 pruebas de continuidad.
- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez, con fecha 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-resilience-0.1.0-2026-10-15.md` y `.pdf`.
- **Matriz de notificaciones y calendario de continuidad:** los usé tal cual vienen en `00-referencia/`.
- **Corrida:** registrada como `2026-10-15-resilience-setup-1`.

**Lo que no abrí**
- `00-referencia/credenciales-vpn.txt`: por su nombre es una credencial.
- `10-controles/A.8.24_certificados/servidor-web.pem`: es una llave.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: es un respaldo.

**Pendientes**
- No marqué la carpeta con `_CRITERIO_SEGURIDAD.txt`, porque nadie lo autorizó en esta sesión.
- Las 3 revisiones de `80-revisiones/` salen como fuera de lugar en el inventario, que las ubica en `70-incidentes/`. No moví nada.
- Las demás señales (sin comandos de reporte ejecutados aún) son 2 notificaciones tarde o sin hacer, 3 pruebas vencidas o sin hacer, y las 3 de arriba.

Archivos en `estado-seguridad/901555123-banco-cordillera-sintetico/`:
- `resiliencia/2026-10/reporte-incident-timeline.md`
- `resiliencia/2026-10/resultados.json`
- `corridas/salida-resilience-setup.md`

La configuración está en `.criterio/resiliencia/901555123/config.json`.