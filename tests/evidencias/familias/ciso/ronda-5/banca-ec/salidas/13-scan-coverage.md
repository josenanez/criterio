# /criterio-vulnerability:scan-coverage 

Corrí la cobertura de los escaneos de Banco del Guayas Sintético para 2026-10. Los términos ya estaban vigentes (versión 1.6), así que no hubo que registrar ninguna aceptación. No hice ninguna pregunta.

# La cobertura de los escaneos · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-10 · **Procesado:** 2026-10-15 · **Agente:** Guillermo, versión 1.5.1 · **Comando:** `scan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Una vulnerabilidad figura cerrada y ningún escaneo posterior la da por corregida (`vuln_closed_without_rescan`) | TK-203 · bgs-correo-01 · CVE-2099-12005: figura cerrada el 2026-09-25 y el escaneo del 2026-10-10 la sigue encontrando | — | 20 | `60-remediacion/seguimiento.xlsx` fila 4 · `50-escaneos/escaneo-2026-10-10.csv` |
| 2 | Una vulnerabilidad figura cerrada y ningún escaneo posterior la da por corregida (`vuln_closed_without_rescan`) | TK-202 · bgs-backup-01 · CVE-2099-12004: figura cerrada el 2026-10-12 y ningún escaneo posterior incluye el activo | — | 3 | `60-remediacion/seguimiento.xlsx` fila 3 |
| 3 | Un activo del inventario no aparece en ningún escaneo de la ventana configurada (`asset_not_scanned`) | bgs-vpn-01: el último escaneo que lo incluye es del 2026-08-20; la ventana es de 30 días | Jefe de infraestructura | 56 | `00-referencia/inventario-activos.xlsx` fila 6 |
| 4 | Un activo del inventario no aparece en ningún escaneo de la ventana configurada (`asset_not_scanned`) | bgs-ws-finanzas-01: ningún escaneo lo incluye; la ventana es de 30 días | Jefe de infraestructura | — | `00-referencia/inventario-activos.xlsx` fila 10 |

## El resultado

**Ventana:** 30 días.

| Activo | Criticidad | Último escaneo | En la ventana |
|---|---|---|---|
| bgs-web-01 | alta | 2026-10-10 | sí |
| bgs-app-01 | media | 2026-10-10 | sí |
| bgs-db-01 | alta | 2026-10-10 | sí |
| bgs-fw-borde-01 | alta | 2026-10-10 | sí |
| bgs-vpn-01 | media | 2026-08-20 | no |
| bgs-ad-01 | alta | 2026-10-10 | sí |
| bgs-correo-01 | media | 2026-10-10 | sí |
| bgs-backup-01 | media | 2026-10-10 | sí |
| bgs-ws-finanzas-01 | media | — | no |

**Escaneados y fuera del inventario:** bgs-prueba-07.

| Ticket | Activo | Vulnerabilidad | Cerrada | Escaneo posterior | La sigue encontrando |
|---|---|---|---|---|---|
| TK-201 | bgs-app-01 | CVE-2099-11002 | 2026-09-01 | 2026-09-20 | no |
| TK-202 | bgs-backup-01 | CVE-2099-12004 | 2026-10-12 | — | no |
| TK-203 | bgs-correo-01 | CVE-2099-12005 | 2026-09-25 | 2026-10-10 | 2026-10-10 |

No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023).

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/inventario-activos.xlsx`
- `50-escaneos/escaneo-2026-10-10.csv`
- `60-remediacion/seguimiento.xlsx`

La salida quedó guardada en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-scan-coverage.md`. La corrida quedó registrada como `2026-10-15-scan-coverage-1`, con 9 hallazgos.

Omití la columna "Monto" de la tabla "Lo que hay que atender" al copiar, porque venía vacía en las cuatro filas. El archivo guardado sí la conserva.