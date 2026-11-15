# /criterio-security:third-parties 

Dos terceros críticos tienen la evaluación de seguridad vencida o sin ninguna. El reporte completo está abajo.

# Los terceros críticos · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.2.3 · **Comando:** `third-parties`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Evaluación vencida (`third_party_assessment_overdue`) | Mesa de Ayuda Externa: la última evaluación es del 2025-09-30; tocaba el 2026-09-30 | 15 | `00-referencia/terceros.csv` fila 4 · `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1` |
| 2 | Sin evaluación (`third_party_assessment_overdue`) | Centro de Datos Alterno: tercero crítico sin ninguna evaluación registrada; el registro pide una cada 365 días | — | `00-referencia/terceros.csv` fila 6 |

## El resultado

| Tercero | Servicio | Crítico | Cada | Última evaluación | Resultado | Tocaba |
|---|---|---|---|---|---|---|
| Nube Andina Servicios | infraestructura en la nube | sí | 365 días | 2026-02-10 | sin hallazgos | 2027-02-10 |
| Pasarela de Pagos Sintética | procesamiento de pagos | sí | 365 días | 2025-11-20 | con observaciones | 2026-11-20 |
| Mesa de Ayuda Externa | soporte a usuarios | sí | 365 días | 2025-09-30 | sin hallazgos | 2026-09-30 |
| Papelería del Centro | insumos de oficina | no | 365 días | — | — | — |
| Centro de Datos Alterno | sitio de recuperación | sí | 365 días | — | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`: excluidos por ser credenciales, llaves o respaldos. No se abrieron.

## Las preguntas que hizo

- Entidad, identificación fiscal y país: Banco Cordillera Sintético, NIT 901555123, Colombia (sugerida por el nombre de la carpeta).
- Periodo: 2026-10 (sugerida por la fecha de la prueba).
- Columnas reconocidas: sí, todas se llaman como el motor las espera.
- Dónde se guarda lo que se encuentra: `estado-seguridad/901555123-banco-cordillera-sintetico`.
- Aceptación de los términos vigentes: sí, José Francisco Ñáñez.
- Marca `_CRITERIO_SEGURIDAD.txt` en la carpeta raíz: el motor falló al escribirla y no quedó.
- Tarea programada diaria: no se crea, porque la sesión de prueba no dio respuesta.

## Fuentes

- `00-referencia/terceros.csv`
- `30-terceros/evaluacion_mesa-de-ayuda-externa_2025-09-30.pdf, p. 1`

Los términos (versión 1.5) ya estaban vigentes, así que este comando no registró ninguna aceptación. La corrida quedó registrada como `2026-10-15-third-parties-1`, con la salida en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-third-parties.md`.