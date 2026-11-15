# /criterio-security:soa-status 

Un control aplicable, el A.8.24 (Uso de la criptografía), figura sin responsable en la declaración. Los términos ya estaban vigentes, así que no hizo falta registrar la aceptación.

# La declaración de aplicabilidad · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.2.3 · **Comando:** `soa-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un control aplicable no tiene responsable (`soa_control_unassigned`) | A.8.24 · Uso de la criptografía: aplicable y sin responsable en la declaración | — | — | — | `00-referencia/declaracion-aplicabilidad.xlsx` fila 14 |

## El resultado

| Control | Nombre | Aplicable | Estado | Responsable | Periodicidad |
|---|---|---|---|---|---|
| 5.1 | Políticas de seguridad de la información | sí | Implementado | Jefe de seguridad de la información | 366 días |
| 5.9 | Inventario de información y otros activos | sí | Implementado | Gerente de tecnología | 183 días |
| 5.15 | Control de acceso | sí | Implementado | Oficial de cumplimiento | 92 días |
| 5.18 | Derechos de acceso | sí | Implementado | Jefe de infraestructura | 92 días |
| 5.19 | Seguridad en las relaciones con proveedores | sí | Implementado | Jefe de seguridad de la información | 366 días |
| 5.24 | Preparación para la gestión de incidentes | sí | Implementado | Gerente de tecnología | 366 días |
| 5.30 | Preparación de las TIC para la continuidad | sí | Implementado | Oficial de cumplimiento | 366 días |
| 8.7 | Protección contra el malware | sí | Implementado | Jefe de infraestructura | 31 días |
| 8.8 | Gestión de las vulnerabilidades técnicas | sí | Implementado | Jefe de seguridad de la información | 31 días |
| 8.13 | Copias de seguridad de la información | sí | Implementado | Gerente de tecnología | 31 días |
| 8.15 | Registro de eventos | sí | Implementado | Oficial de cumplimiento | 31 días |
| 8.16 | Actividades de seguimiento | sí | Implementado | Jefe de infraestructura | 31 días |
| 8.24 | Uso de la criptografía | sí | Implementado | — | 366 días |
| 7.4 | Seguimiento de la seguridad física | no | — | — | — |
| 8.28 | Codificación segura | sí | En implementación | Gerente de tecnología | 366 días |

La declaración la aprueba una persona: aquí se dice qué control aplicable no tiene responsable.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

- ¿Cuál es la entidad, su identificación fiscal y su país? → Banco Cordillera Sintético, NIT 901555123, Colombia (sugerida por el nombre de la carpeta; sesión de prueba sin interfaz)
- ¿Qué periodo se revisa? → 2026-10 (sugerida por la fecha de la prueba)
- ¿Las columnas reconocidas de la declaración de aplicabilidad, la tabla de sistemas, el registro de terceros y el de riesgos son las correctas? → Sí (sugerida: todas se llaman como el motor las espera; no hace falta mapear columns)
- ¿Dónde se guarda lo que se encuentra? → estado-seguridad/901555123-banco-cordillera-sintetico (sugerida)
- ¿Se acepta la versión vigente de los términos? → Sí, José Francisco Ñáñez
- ¿Se deja la marca _CRITERIO_SEGURIDAD.txt en la carpeta raíz? → Sí (sugerida); el motor falló al escribirla y no quedó
- ¿Se crea una tarea programada para que Alexis revise lo que toca cada día? → Sin respuesta explícita en la sesión de prueba: no se crea, sin reloj

## Fuentes

- `00-referencia/declaracion-aplicabilidad.xlsx`

La corrida quedó registrada como `2026-10-15-soa-status-1`. Lo mostrado está en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-soa-status.md`.