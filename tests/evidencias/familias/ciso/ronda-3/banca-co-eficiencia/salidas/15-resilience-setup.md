# /criterio-resilience:resilience-setup seguridad/901555123-banco-cordillera-sintetico

Amparo quedó instalada sobre Banco Cordillera Sintético (NIT 901555123), periodo 2026-10, fecha de prueba 2026-10-15. El motor encontró 8 señales; el reporte de abajo muestra las 3 de la línea de tiempo de los incidentes.

**Carpeta:** `seguridad/901555123-banco-cordillera-sintetico`, la que venía en el argumento. Procesé 60 archivos.

**Lo que no abro**, porque el motor lo excluye:
- `00-referencia/credenciales-vpn.txt`: por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: un archivo .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: un archivo .zip es una llave, una credencial o un respaldo.

**Una sugerencia de orden:** el motor propone pasar las tres revisiones de `80-revisiones/` a `70-incidentes/`. No moví nada.

**Respuestas que tomé.** Nadie respondía en esta sesión, así que usé las que sugerían los documentos y lo que ya habían fijado Alexis y Guillermo:
1. **Entidad:** Banco Cordillera Sintético, NIT 901555123, Colombia.
2. **Periodo:** 2026-10.
3. **Plazos de contención** (política de respuesta a incidentes, sección 5): crítica 4 h, alta 24 h, media 72 h, baja 168 h.
4. **Revisión posterior** (sección 7): dentro de los 10 días calendario siguientes al cierre.
5. **Matriz de notificaciones:** Superintendencia Financiera, si es crítica, en 24 h; Autoridad de protección de datos, si hay datos personales, en 72 h; Clientes afectados en 72 h; Comité de riesgos, siempre, en 48 h. El motor reconoce sus columnas, así que no hizo falta mapearlas.
6. **Calendario de continuidad:** cinco pruebas, con frecuencias de 365, 180, 90, 90 y 180 días. El motor reconoce sus columnas.
7. **Dónde guardo lo que encuentro:** `estado-seguridad/901555123-banco-cordillera-sintetico`.
8. **Términos:** los mostré tal cual y quedaron aceptados por José Francisco Ñáñez el 2026-10-15. El comprobante está en `.criterio/terminos/`.
9. **Marca `_CRITERIO_SEGURIDAD.txt`:** la respuesta fue sí, pero **no quedó**. `marcar-raiz` falla dentro del motor (`KeyError: 'ciso'` en `raiz.py:230`), el mismo fallo que tuvo Alexis. No la creé a mano.
10. **Reloj:** no lo creé, porque pide un sí explícito y esta sesión no lo tiene.

**Configuración:** `.criterio/resiliencia/901555123/config.json`. El motor la validó sin problemas.

**La ficha:** lleva 6 incidentes con 9 constancias de notificación, 3 revisiones y 4 pruebas de continuidad. De las 8 señales, las 5 que no salen en este reporte son 2 notificaciones tardías, 1 prueba de continuidad vencida y 2 restauraciones vencidas. Esas las detallan `/criterio-resilience:notifications` y `/criterio-resilience:continuity-tests`.

# La línea de tiempo de cada incidente · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.2.3 · **Comando:** `incident-timeline`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BCO-102 · Acceso indebido a una cuenta privilegiada: alta, contenido en 30 horas y la política da 24 | — | — | — | `70-incidentes/INC-BCO-102_informe.docx, línea de tiempo` |
| 2 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BCO-106 · Malware en una estación de trabajo de finanzas: alta, detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — | — | `70-incidentes/INC-BCO-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)` |
| 3 | Un incidente cerrado no tiene su revisión posterior dentro del plazo (`incident_without_review`) | INC-BCO-105: cerrado el 2026-08-25 y sin revisión posterior; la política da 10 días | — | — | 41 | `70-incidentes/INC-BCO-105_informe.docx, línea de tiempo` |

## El resultado

**Plazos de contención de la política:** critica 4 h · alta 24 h · media 72 h · baja 168 h · **Revisión posterior:** 10 días

| Incidente | Severidad | Detectado | Contenido | Horas | Plazo | Cerrado | Revisión |
|---|---|---|---|---|---|---|---|
| INC-BCO-105 · Correo de suplantación con un enlace malicioso | baja | 2026-08-18T10:00 | 2026-08-19T16:00 | 30,00 | 168,00 | 2026-08-25 | — |
| INC-BCO-101 · Ransomware contenido en un servidor de archivos | critica | 2026-09-03T09:10 | 2026-09-03T12:40 | 3,50 | 4,00 | 2026-09-08 | 2026-09-12 |
| INC-BCO-102 · Acceso indebido a una cuenta privilegiada | alta | 2026-09-10T14:00 | 2026-09-11T20:00 | 30,00 | 24,00 | 2026-09-15 | 2026-09-20 |
| INC-BCO-103 · Exfiltración de una base de datos de clientes | critica | 2026-09-22T07:30 | 2026-09-22T11:00 | 3,50 | 4,00 | 2026-09-26 | 2026-09-30 |
| INC-BCO-106 · Malware en una estación de trabajo de finanzas | alta | 2026-09-28T16:45 | — | — | 24,00 | — | — |
| INC-BCO-104 · Indisponibilidad del portal por denegación de servicio | media | 2026-10-01T11:00 | 2026-10-02T07:00 | 20,00 | 72,00 | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `70-incidentes/INC-BCO-102_informe.docx, línea de tiempo`
- `70-incidentes/INC-BCO-105_informe.docx, línea de tiempo`
- `70-incidentes/INC-BCO-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)`
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. Para correrlo a mano: `/criterio-resilience:resilience-wake`.

La corrida quedó registrada como `2026-10-15-resilience-setup-1`, con 8 hallazgos.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.