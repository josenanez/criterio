# /criterio-vulnerability:scan-coverage 

Dos activos del inventario no tienen escaneo dentro de la ventana de 30 días, y dos cierres no tienen un escaneo posterior que los pruebe. Los términos (versión 1.5) estaban vigentes, así que no hizo falta registrar una aceptación. Ninguna pregunta quedó pendiente.

# La cobertura de los escaneos · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 1.4.0 · **Comando:** `scan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Cerrada sin escaneo posterior que la dé por corregida (`vuln_closed_without_rescan`) | TK-203 · bps-correo-01 · CVE-2099-12005: figura cerrada el 2026-09-25 y el escaneo del 2026-10-10 la sigue encontrando | — | 20 | `60-remediacion/seguimiento.csv` fila 4 · `50-escaneos/escaneo-2026-10-10.csv` |
| 2 | Cerrada sin escaneo posterior (`vuln_closed_without_rescan`) | TK-202 · bps-backup-01 · CVE-2099-12004: figura cerrada el 2026-10-12 y ningún escaneo posterior incluye el activo | — | 3 | `60-remediacion/seguimiento.csv` fila 3 |
| 3 | Activo sin escaneo en la ventana (`asset_not_scanned`) | bps-vpn-01: el último escaneo que lo incluye es del 2026-08-20; la ventana es de 30 días | Jefe de infraestructura | 56 | `00-referencia/inventario-activos.csv` fila 6 |
| 4 | Activo sin escaneo en la ventana (`asset_not_scanned`) | bps-ws-finanzas-01: ningún escaneo lo incluye; la ventana es de 30 días | Jefe de infraestructura | — | `00-referencia/inventario-activos.csv` fila 10 |

## El resultado

**Ventana:** 30 días.

| Activo | Criticidad | Último escaneo | En la ventana |
|---|---|---|---|
| bps-web-01 | alta | 2026-10-10 | sí |
| bps-app-01 | media | 2026-10-10 | sí |
| bps-db-01 | alta | 2026-10-10 | sí |
| bps-fw-borde-01 | alta | 2026-10-10 | sí |
| bps-vpn-01 | media | 2026-08-20 | no |
| bps-ad-01 | alta | 2026-10-10 | sí |
| bps-correo-01 | media | 2026-10-10 | sí |
| bps-backup-01 | media | 2026-10-10 | sí |
| bps-ws-finanzas-01 | media | — | no |

**Escaneados y fuera del inventario:** bps-prueba-07.

| Ticket | Activo | Vulnerabilidad | Cerrada | Escaneo posterior | La sigue encontrando |
|---|---|---|---|---|---|
| TK-201 | bps-app-01 | CVE-2099-11002 | 2026-09-01 | 2026-09-20 | no |
| TK-202 | bps-backup-01 | CVE-2099-12004 | 2026-10-12 | — | no |
| TK-203 | bps-correo-01 | CVE-2099-12005 | 2026-09-25 | 2026-10-10 | 2026-10-10 |

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión, por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión, .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión, .zip es una llave, una credencial o un respaldo.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/inventario-activos.csv`
- `50-escaneos/escaneo-2026-10-10.csv`
- `60-remediacion/seguimiento.csv`

La salida quedó en `estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-scan-coverage.md`. La corrida quedó registrada como `2026-10-15-scan-coverage-1`, con 9 hallazgos.

Dos cosas no son como el pedido las daba por hechas:
- **Aceptación de términos:** la configuración tiene aceptada la versión 1.4.0, pero el motor la da por vigente, así que no hubo nada que registrar a nombre de José Francisco Ñáñez.
- **Fecha del sistema:** la del sistema es 2026-11-16. Usé 2026-10-15 en las llamadas al motor que aceptan `--today`, como se pidió.