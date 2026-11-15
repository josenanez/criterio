# /criterio-security:security-setup seguridad/901555123-banco-cordillera-sintetico

Soy Alexis. Pongo cada control de la declaración de aplicabilidad al lado de la evidencia de que operó; no acepto riesgos ni declaro cumplido un control.

Procesé 60 archivos en `seguridad/901555123-banco-cordillera-sintetico`.

- **Lo que no abrí:** tres archivos. `00-referencia/credenciales-vpn.txt` es una credencial, `10-controles/A.8.24_certificados/servidor-web.pem` es una llave y `90-continuidad/respaldo-correo-2026-06-20.zip` es un respaldo. Te sugiero sacarlos de la carpeta de evidencia.
- **Las respuestas que tomé** (todas las sugeridas, porque es una prueba sin interfaz):
  - **La entidad:** Banco Cordillera Sintético, NIT 901555123, Colombia.
  - **El periodo:** 2026-10.
  - **Las columnas:** las de la declaración de aplicabilidad, la tabla de sistemas, el registro de terceros y el de riesgos se reconocen por su nombre, así que no hubo que agregar nada en `columns`.
  - **El estado:** queda en `estado-seguridad/901555123-banco-cordillera-sintetico`.
- **Los términos 1.5:** quedaron aceptados a nombre de José Francisco Ñáñez el 2026-10-15. El comprobante está en `.criterio/terminos/`.
- **La marca de la carpeta:** `_CRITERIO_SEGURIDAD.txt` no quedó porque `marcar-raiz` falló dentro del motor (`KeyError: 'ciso'` en `raiz.py:230`). No la creé a mano.
- **El borrador:** `A.8.28_borrador-guia-codificacion.docx` está sin aprobar y no cuenta como evidencia.
- **Las señales:** el motor encontró 8. Abajo van las 2 de los controles. Las demás (accesos, terceros, riesgos y el control sin responsable) las muestran `/criterio-security:access-reviews`, `/criterio-security:third-parties`, `/criterio-security:risk-register` y `/criterio-security:soa-status`.

---

# Los controles contra su evidencia · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.2.3 · **Comando:** `control-evidence`

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

- ¿Cuál es la entidad, su identificación fiscal y su país? → Banco Cordillera Sintético, NIT 901555123, Colombia (sugerida por el nombre de la carpeta; sesión de prueba sin interfaz)
- ¿Qué periodo se revisa? → 2026-10 (sugerida por la fecha de la prueba)
- ¿Las columnas reconocidas de la declaración de aplicabilidad, la tabla de sistemas, el registro de terceros y el de riesgos son las correctas? → Sí (sugerida: todas se llaman como el motor las espera; no hace falta mapear columns)
- ¿Dónde se guarda lo que se encuentra? → estado-seguridad/901555123-banco-cordillera-sintetico (sugerida)
- ¿Se acepta la versión vigente de los términos? → Sí, José Francisco Ñáñez
- ¿Se deja la marca _CRITERIO_SEGURIDAD.txt en la carpeta raíz? → Sí (sugerida); el motor falló al escribirla y no quedó
- ¿Se crea una tarea programada para que Alexis revise lo que toca cada día? → Sin respuesta explícita en la sesión de prueba: no se crea, sin reloj

## Fuentes

- `00-referencia/declaracion-aplicabilidad.xlsx`
- `10-controles/A.5.18_derechos-de-acceso_2026-06.pdf, p. 1`

---

**Cuándo vuelvo:** sin reloj. Una tarea programada necesita un sí explícito, y en esta prueba no hubo quien lo diera. Para correrlo a mano: `/criterio-security:security-wake`.

La configuración quedó en `.criterio/seguridad/901555123/config.json`. La corrida quedó registrada como `2026-10-15-security-setup-1`, y lo que se mostró arriba está en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-security-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.