# /criterio-security:risk-register 

Los términos 1.6 figuran como aceptados por José Francisco Ñáñez el 2026-10-15. El reporte salió con corte 2026-10-15, y la corrida quedó registrada como `2026-10-15-risk-register-1`.

# El registro de riesgos · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Agente:** Alexis, versión 1.5.1 · **Comando:** `risk-register`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Una aceptación de riesgo pasó su fecha de revisión (`risk_acceptance_expired`) | R-03 · Respaldo fuera de sitio a más de 24 horas: aceptado por Comité de riesgos hasta el 2026-09-30, y no se volvió a revisar | Comité de riesgos | 15 | `40-riesgos/registro-riesgos.csv` fila 4 |

## El resultado

| Riesgo | Decisión | Aceptado por | Revisión |
|---|---|---|---|
| R-01 · Sistema heredado sin soporte del fabricante | Aceptar | Gerente general | 2026-12-31 |
| R-02 · Correo sin doble factor para proveedores | Mitigar | — | 2026-12-31 |
| R-03 · Respaldo fuera de sitio a más de 24 horas | Aceptar | Comité de riesgos | 2026-09-30 |
| R-04 · Equipos personales en la red de invitados | Aceptar | Gerente de tecnología | 2026-10-15 |

Ningún riesgo lo acepta el agente: aquí se dice qué aceptación pasó su fecha de revisión.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión (por su nombre es una credencial o una llave).
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión (.pem es una llave, una credencial o un respaldo).
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión (.zip es una llave, una credencial o un respaldo).

## Las preguntas que hizo

Se tomó la respuesta sugerida en todas, porque la sesión no tenía interfaz:

- ¿Es esta la carpeta de la entidad? → Sí.
- ¿La entidad es Banco del Guayas Sintético, RUC 1790987654001, Ecuador, en USD? → Sí.
- ¿El periodo es 2026-10? → Sí.
- ¿Las tablas de `00-referencia/` y `40-riesgos/` se toman sin mapeo? → Sí.
- ¿Guardo lo que encuentro en `estado-seguridad/1790987654001-banco-del-guayas-sintetico`? → Sí.
- ¿Aceptas los términos 1.6? → Sí, José Francisco Ñáñez, 2026-10-15.
- ¿Dejo la marca `_CRITERIO_SEGURIDAD.txt` en la carpeta? → Sí.
- ¿Programo la tarea diaria de security-wake? → No, porque nadie dio un sí explícito.

## Fuentes

- `40-riesgos/registro-riesgos.csv`

El reporte completo está en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/seguridad/2026-10/reporte-risk-register.md`. Esta salida está guardada en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-risk-register.md`.