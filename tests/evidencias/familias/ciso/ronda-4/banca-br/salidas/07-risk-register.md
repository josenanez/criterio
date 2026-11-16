# /criterio-security:risk-register 

Hay una aceptación de riesgo vencida (R-03); las demás están dentro de su fecha de revisión según el registro.

# El registro de riesgos · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.4.0 · **Comando:** `risk-register`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una aceptación de riesgo pasó su fecha de revisión (`risk_acceptance_expired`) | R-03 · Respaldo fuera de sitio a más de 24 horas: aceptado por Comité de riesgos hasta el 2026-09-30, y no se volvió a revisar | — | Comité de riesgos | 15 | `40-riesgos/registro-riesgos.xlsx` fila 4 |

## El resultado

| Riesgo | Decisión | Aceptado por | Revisión |
|---|---|---|---|
| R-01 · Sistema heredado sin soporte del fabricante | Aceptar | Gerente general | 2026-12-31 |
| R-02 · Correo sin doble factor para proveedores | Mitigar | — | 2026-12-31 |
| R-03 · Respaldo fuera de sitio a más de 24 horas | Aceptar | Comité de riesgos | 2026-09-30 |
| R-04 · Equipos personales en la red de invitados | Aceptar | Gerente de tecnología | 2026-10-15 |

Ningún riesgo lo acepta el agente: aquí se dice qué aceptación pasó su fecha de revisión.

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

- `40-riesgos/registro-riesgos.xlsx`

La corrida quedó registrada como `2026-10-15-risk-register-1`.