# /criterio-security:control-evidence 

Dos controles piden atención: A.8.15 no tiene evidencia y A.5.18 la tiene vencida. Los términos ya estaban vigentes, así que no registré una aceptación nueva.

# Los controles contra su evidencia · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Agente:** Alexis, versión 1.4.0

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Control implementado sin ninguna evidencia (`control_without_evidence`) | A.8.15 · Registro de eventos | Oficial de cumplimiento | — | `00-referencia/declaracion-aplicabilidad.csv` fila 12 |
| 2 | Evidencia anterior a su periodicidad (`control_evidence_stale`) | A.5.18 · Derechos de acceso: la evidencia más reciente es del 2026-06-30, la periodicidad es de 92 días y venció el 2026-09-30 | Jefe de infraestructura | 15 | `00-referencia/declaracion-aplicabilidad.csv` fila 5 · `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1` |

## El resultado

| Control | Estado | Evidencias | La más reciente | Vence |
|---|---|---|---|---|
| 5.1 · Políticas de seguridad de la información | Implementado | 1 | 2026-02-20 | 2027-02-21 |
| 5.9 · Inventario de información y otros activos | Implementado | 1 | 2026-07-31 | 2027-01-30 |
| 5.15 · Control de acceso | Implementado | 1 | 2026-09-30 | 2026-12-31 |
| 5.18 · Derechos de acceso | Implementado | 1 | 2026-06-30 | 2026-09-30 |
| 5.19 · Seguridad en las relaciones con proveedores | Implementado | 1 | 2026-03-15 | 2027-03-16 |
| 5.24 · Preparación para la gestión de incidentes | Implementado | 1 | 2026-01-30 | 2027-01-31 |
| 5.30 · Preparación de las TIC para la continuidad | Implementado | 1 | 2026-04-10 | 2027-04-11 |
| 8.7 · Protección contra el malware | Implementado | 1 | 2026-09-30 | 2026-10-31 |
| 8.8 · Gestión de las vulnerabilidades técnicas | Implementado | 1 | 2026-09-30 | 2026-10-31 |
| 8.13 · Copias de seguridad de la información | Implementado | 1 | 2026-09-30 | 2026-10-31 |
| 8.15 · Registro de eventos | Implementado | 0 | — | — |
| 8.16 · Actividades de seguimiento | Implementado | 1 | 2026-09-15 | 2026-10-16 |
| 8.24 · Uso de la criptografía | Implementado | 1 | 2026-05-20 | 2027-05-21 |
| 8.28 · Codificación segura | En implementación | 0 | — | — |

Ningún control se declara cumplido aquí: se dice cuál no tiene evidencia de que operó.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión, por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión, .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión, .zip es una llave, una credencial o un respaldo.

## Las preguntas que hizo

- ¿La carpeta de la entidad es seguridad/12345678000195-banco-paulista-sintetico? → Sí (respuesta sugerida, sesión de prueba sin interfaz).
- ¿La entidad es Banco Paulista Sintético, CNPJ 12345678000195, Brasil? → Sí (respuesta sugerida a partir del nombre de la carpeta).
- ¿El periodo es 2026-10? → Sí (respuesta sugerida a partir de la fecha de la prueba).
- ¿Las columnas de las tablas son las que reconoce el motor? → Sí (el motor no reportó columnas faltantes).
- ¿Guardo lo que encuentro en estado-seguridad/12345678000195-banco-paulista-sintetico? → Sí (respuesta sugerida).
- ¿Aceptas los términos 1.5? → Sí, José Francisco Ñáñez.
- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la carpeta? → Sí (respuesta sugerida).

## Fuentes

- `00-referencia/declaracion-aplicabilidad.csv`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`

---
La salida quedó en `corridas/salida-control-evidence.md` y la corrida quedó registrada como `2026-10-15-control-evidence-1`. El reporte completo está en `seguridad/2026-10/reporte-control-evidence.md`.