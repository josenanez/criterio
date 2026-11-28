# /criterio-security:security-setup seguridad/1790987654001-banco-del-guayas-sintetico

Alexis queda configurado para Banco del Guayas Sintético (RUC 1790987654001). La primera ficha procesó la evidencia de 12 controles y el reporte de evidencia de controles trae 2 señales.

- **Configuración:** está en `.criterio/seguridad/1790987654001/config.json`, para Ecuador, en USD y con el periodo 2026-10. El motor la validó sin problemas.
- **Términos 1.6:** quedan aceptados a nombre de José Francisco Ñáñez con fecha 2026-10-15. Los comprobantes son `.criterio/terminos/aceptacion-criterio-security-1.5.1-2026-10-15.md` y `.pdf`.
- **Marca:** dejé `_CRITERIO_SEGURIDAD.txt` en la carpeta de la entidad.
- **Archivos que no abrí:** `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`. Son credenciales, llaves o respaldos, y conviene sacarlos de la carpeta de evidencia.
- **Archivos fuera de lugar:** las tres revisiones `INC-BGS-10x_revision.md` de `80-revisiones/` irían en `70-incidentes/`. No moví nada.
- **Lo que no cuenta como evidencia:** `A.8.28_borrador-guia-codificacion.docx` dice «sin aprobar».
- **Tablas:** la declaración de aplicabilidad, `sistemas.csv`, `terceros.csv` y `registro-riesgos.csv` traen las columnas que el motor reconoce, así que no hizo falta mapear nada.

`compute` encontró 8 señales en total. Solo 2 son de evidencia de controles y salen en este reporte. Las otras 6 aparecen en otros comandos:
- 2 revisiones de accesos vencidas (`access-reviews`)
- 2 evaluaciones de terceros vencidas (`third-parties`)
- 1 aceptación de riesgo vencida (`risk-register`)
- 1 control sin responsable (`soa-status`)

Los términos 1.6 tienen fecha 2026-11-16, que es posterior a la fecha de la prueba (2026-10-15). El motor registró la aceptación de todos modos. Conviene revisarlo si la prueba busca verificar esa coherencia.

# Los controles contra su evidencia · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.5.1 · **Comando:** `control-evidence`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un control aplicable de la declaración figura implementado y no tiene ninguna evidencia de que operó (`control_without_evidence`) | A.8.15 · Registro de eventos: figura «Implementado» y la ficha no tiene ninguna evidencia de que operó | — | Oficial de cumplimiento | — | `00-referencia/declaracion-aplicabilidad.xlsx` fila 12 |
| 2 | La evidencia más reciente de un control periódico es anterior a su periodicidad (`control_evidence_stale`) | A.5.18 · Derechos de acceso: la evidencia más reciente es del 2026-06-30 y su periodicidad es de 92 días; venció el 2026-09-30 | — | Jefe de infraestructura | 15 | `00-referencia/declaracion-aplicabilidad.xlsx` fila 5 · `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1` |

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

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

- ¿Es esta la carpeta de la entidad: seguridad/1790987654001-banco-del-guayas-sintetico? → Sí (respuesta sugerida; prueba sin interfaz)
- ¿La entidad es Banco del Guayas Sintético, RUC 1790987654001, Ecuador, en USD? → Sí (respuesta sugerida a partir del nombre de la carpeta; prueba sin interfaz)
- ¿El periodo es 2026-10? → Sí (respuesta sugerida a partir de la fecha de la prueba)
- ¿Las tablas de 00-referencia/ y 40-riesgos/ se toman con las columnas que el motor reconoce, sin mapeo? → Sí (respuesta sugerida: sistemas.csv, terceros.csv y registro-riesgos.csv traen los nombres esperados)
- ¿Guardo lo que encuentro en estado-seguridad/1790987654001-banco-del-guayas-sintetico? → Sí (respuesta sugerida)
- ¿Aceptas los términos 1.6? → Sí, José Francisco Ñáñez, 2026-10-15
- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la carpeta? → Sí (respuesta sugerida)
- ¿Programo la tarea diaria de security-wake? → No (sin interfaz, nadie dio un sí explícito)

## Fuentes

- `00-referencia/declaracion-aplicabilidad.xlsx`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`

**Cuándo vuelvo:** sin reloj, porque nadie dio un sí explícito a la tarea programada. Se corre a mano con `/criterio-security:security-wake`.

La corrida quedó registrada como `2026-10-15-security-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.