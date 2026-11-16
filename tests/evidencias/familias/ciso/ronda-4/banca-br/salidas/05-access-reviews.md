# /criterio-security:access-reviews 

Los términos 1.5 estaban vigentes, así que no hizo falta registrar la aceptación otra vez. El motor ya dejó constancia de la de José Francisco Ñáñez. Dos de los cuatro sistemas de Banco Paulista Sintético (CNPJ 12345678000195) tienen la revisión de accesos vencida o sin hacer, con corte al 2026-10-15.

# Las revisiones de acceso · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 1.4.0 · **Comando:** `access-reviews`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La revisión de accesos de un sistema pasó su fecha, o no hay ninguna (`access_review_overdue`) | Directorio activo: la última revisión de accesos es del 2026-06-30; tocaba el 2026-09-28 | — | Jefe de seguridad de la información | 17 | `00-referencia/sistemas.csv` fila 4 · `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1` |
| 2 | La revisión de accesos de un sistema pasó su fecha, o no hay ninguna (`access_review_overdue`) | Portal de clientes: ninguna revisión de accesos registrada; la tabla pide una cada 180 días | — | Jefe de seguridad de la información | — | `00-referencia/sistemas.csv` fila 5 |

## El resultado

| Sistema | Cada | Última revisión | Tocaba | Responsable |
|---|---|---|---|---|
| Core bancário | 90 días | 2026-08-10 | 2026-11-08 | Jefe de seguridad de la información |
| Correo corporativo | 180 días | 2026-05-02 | 2026-10-29 | Jefe de seguridad de la información |
| Directorio activo | 90 días | 2026-06-30 | 2026-09-28 | Jefe de seguridad de la información |
| Portal de clientes | 180 días | — | — | Jefe de seguridad de la información |

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

- `00-referencia/sistemas.csv`
- `20-accesos/revision-accesos_directorio-activo_2026-06-30.pdf, p. 1`

La corrida quedó registrada como `2026-10-15-access-reviews-1`. El reporte está en `seguridad/2026-10/reporte-access-reviews.md`, y copié lo que te mostré en `corridas/salida-access-reviews.md`, dentro de la carpeta de estado de la entidad.