# /criterio-security:security-setup seguridad/12345678000195-banco-paulista-sintetico

Soy Alexis. Pongo cada control de la declaración de aplicabilidad al lado de la evidencia de que operó; no acepto riesgos ni declaro cumplido un control.

Alexis quedó configurado sobre Banco Paulista Sintético (CNPJ 12345678000195, Brasil) para el periodo 2026-10. El motor validó la configuración sin problemas y la primera ficha marca 2 asuntos de evidencia: el control A.8.15 no tiene ninguna y la del A.5.18 está vencida.

- **Carpeta:** había una sola candidata, `seguridad/12345678000195-banco-paulista-sintetico`, con la estructura completa (de `00-referencia/` a `90-continuidad/`). La tomé.
- **Lo que no abrí:** `00-referencia/credenciales-vpn.txt` (por su nombre es una credencial), `10-controles/A.8.24_certificados/servidor-web.pem` (es una llave o un certificado) y `90-continuidad/respaldo-correo-2026-06-20.zip` (es un respaldo). Conviene sacarlos de la carpeta de evidencia.
- **Archivos fuera de lugar:** según el inventario, `INC-BPS-101`, `102` y `103_revision.md` de `80-revisiones/` irían en `70-incidentes/`. No moví nada.
- **Preguntas, todas con la respuesta sugerida por los documentos:**
  - **Entidad:** Banco Paulista Sintético, CNPJ 12345678000195, Brasil (BRL). Periodo: 2026-10.
  - **Declaración de aplicabilidad:** reconocí las columnas `Control`, `Nombre`, `Aplicable`, `Estado`, `Responsable` y `Periodicidad`. La de `Justificación` el motor no la usa.
  - **Otras tablas:** el motor no reportó columnas faltantes en la de sistemas, la de terceros ni el registro de riesgos, así que no hubo que registrar nada en `columns`.
  - **Estado:** lo que encuentro se guarda en `estado-seguridad/12345678000195-banco-paulista-sintetico`.
  - **Marca:** sí; `_CRITERIO_SEGURIDAD.txt` quedó en la carpeta de la entidad.
- **Términos:** mostré tal cual el texto corto de la versión 1.5, que vino de `arranque`. José Francisco Ñáñez los aceptó el 2026-10-15. Los términos 1.5 tienen fecha 2026-11-09, posterior a la fecha de la prueba; los registré igual porque son los vigentes de esta versión, como pidió la prueba. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-security-1.4.0-2026-10-15.md` y `.pdf`.
- **Configuración:** está en `.criterio/seguridad/12345678000195/config.json`.
- **Primera ficha:** procesé 12 evidencias, 3 revisiones de accesos y 3 evaluaciones de terceros. `A.8.28_borrador-guia-codificacion.docx` quedó como revisado: es un borrador sin aprobar, así que no cuenta como evidencia.
- **Otras señales:** el cálculo del periodo da 8 en total. Las de accesos, terceros, riesgos y responsables se ven con `/criterio-security:access-reviews`, `third-parties`, `risk-register` y `soa-status`.

# Los controles contra su evidencia · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.4.0 · **Comando:** `control-evidence`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un control aplicable de la declaración figura implementado y no tiene ninguna evidencia de que operó (`control_without_evidence`) | A.8.15 · Registro de eventos: figura «Implementado» y la ficha no tiene ninguna evidencia de que operó | — | Oficial de cumplimiento | — | `00-referencia/declaracion-aplicabilidad.csv` fila 12 |
| 2 | La evidencia más reciente de un control periódico es anterior a su periodicidad (`control_evidence_stale`) | A.5.18 · Derechos de acceso: la evidencia más reciente es del 2026-06-30 y su periodicidad es de 92 días; venció el 2026-09-30 | — | Jefe de infraestructura | 15 | `00-referencia/declaracion-aplicabilidad.csv` fila 5 · `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1` |

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

(Las 7 preguntas de la lista de arriba, con su respuesta sugerida y la aceptación de los términos por José Francisco Ñáñez.)

## Fuentes

- `00-referencia/declaracion-aplicabilidad.csv`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión no hay nadie presente para darlo. Se corre a mano con `/criterio-security:security-wake`.

La corrida quedó registrada como `2026-10-15-security-setup-1`, con 8 hallazgos. Lo que mostré está completo en `estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-security-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.