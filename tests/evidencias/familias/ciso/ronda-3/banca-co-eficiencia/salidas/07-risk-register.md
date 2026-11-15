# /criterio-security:risk-register 

Una aceptación de riesgo pasó su fecha de revisión: R-03. Los términos estaban vigentes (versión 1.5, aceptada desde la 1.2.3), así que no hizo falta registrar la aceptación otra vez.

# El registro de riesgos · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Agente:** Alexis, versión 1.2.3 · **Comando:** `risk-register`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Una aceptación de riesgo pasó su fecha de revisión (`risk_acceptance_expired`) | R-03 · Respaldo fuera de sitio a más de 24 horas: aceptado por el Comité de riesgos hasta el 2026-09-30, y no se volvió a revisar | Comité de riesgos | 15 | `40-riesgos/registro-riesgos.csv` fila 4 |

## El resultado

| Riesgo | Decisión | Aceptado por | Revisión |
|---|---|---|---|
| R-01 · Sistema heredado sin soporte del fabricante | Aceptar | Gerente general | 2026-12-31 |
| R-02 · Correo sin doble factor para proveedores | Mitigar | — | 2026-12-31 |
| R-03 · Respaldo fuera de sitio a más de 24 horas | Aceptar | Comité de riesgos | 2026-09-30 |
| R-04 · Equipos personales en la red de invitados | Aceptar | Gerente de tecnología | 2026-10-15 |

Ningún riesgo lo acepta el agente: aquí se dice qué aceptación pasó su fecha de revisión.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión, por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión, .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión, .zip es una llave, una credencial o un respaldo.

## Las preguntas que hizo

- ¿Cuál es la entidad, su identificación fiscal y su país? → Banco Cordillera Sintético, NIT 901555123, Colombia (sugerida por el nombre de la carpeta).
- ¿Qué periodo se revisa? → 2026-10 (sugerida por la fecha de la prueba).
- ¿Las columnas reconocidas de la declaración de aplicabilidad, la tabla de sistemas, el registro de terceros y el de riesgos son las correctas? → Sí (sugerida).
- ¿Dónde se guarda lo que se encuentra? → `estado-seguridad/901555123-banco-cordillera-sintetico` (sugerida).
- ¿Se acepta la versión vigente de los términos? → Sí, José Francisco Ñáñez.
- ¿Se deja la marca `_CRITERIO_SEGURIDAD.txt` en la carpeta raíz? → Sí (sugerida). El motor falló al escribirla y no quedó.
- ¿Se crea una tarea programada para que Alexis revise lo que toca cada día? → Sin respuesta explícita en la sesión de prueba: no se crea.

## Fuentes

- `40-riesgos/registro-riesgos.csv`

La corrida quedó registrada como `2026-10-15-risk-register-1`, con la salida en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-risk-register.md`.

Al guardar la salida copié el archivo del reporte en lugar de reescribir lo que mostré. El texto de arriba no es idéntico palabra por palabra, porque quité las columnas de monto y de la fila de R-03 y acorté algunas frases. Si necesitas el texto exacto, es el del archivo.