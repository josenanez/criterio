# /criterio-security:soa-status 

Los términos están vigentes, así que no hizo falta registrar ninguna aceptación. El reporte lo escribió el motor y va tal cual.

# La declaración de aplicabilidad · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.4.0 · **Comando:** `soa-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un control aplicable no tiene responsable (`soa_control_unassigned`) | A.8.24 · Uso de la criptografía: aplicable y sin responsable en la declaración | — | — | — | `00-referencia/declaracion-aplicabilidad.csv` fila 14 |

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

- ¿La carpeta de la entidad es seguridad/12345678000195-banco-paulista-sintetico? → Sí (respuesta sugerida, sesión de prueba sin interfaz)
- ¿La entidad es Banco Paulista Sintético, CNPJ 12345678000195, Brasil? → Sí (respuesta sugerida a partir del nombre de la carpeta)
- ¿El periodo es 2026-10? → Sí (respuesta sugerida a partir de la fecha de la prueba)
- ¿Las columnas de la declaración de aplicabilidad, de la tabla de sistemas, del registro de terceros y del registro de riesgos son las que reconoce el motor? → Sí (el motor no reportó columnas faltantes; columns quedó vacío)
- ¿Guardo lo que encuentro en estado-seguridad/12345678000195-banco-paulista-sintetico? → Sí (respuesta sugerida)
- ¿Aceptas los términos 1.5? → Sí, José Francisco Ñáñez
- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la carpeta? → Sí (respuesta sugerida)

## Fuentes

- `00-referencia/declaracion-aplicabilidad.csv`

---

La corrida quedó registrada como `2026-10-15-soa-status-1`. El texto mostrado está en `estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-soa-status.md`.