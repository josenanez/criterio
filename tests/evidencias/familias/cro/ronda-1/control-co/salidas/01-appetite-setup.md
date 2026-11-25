# /criterio-risk-appetite:appetite-setup riesgos/901888444-banco-control-de-riesgos-sintetico

Severo quedó configurado para el Banco Control de Riesgos Sintético (901888444), y la primera revisión de octubre de 2026 no encontró nada abierto. Los dos límites excedidos (L-03 y L-04) tienen respaldo: L-03 un plan de acción y L-04 la aprobación del comité. Las cinco áreas reportaron dentro del plazo.

- **Configuración:** quedó en `.criterio/apetito/901888444/config.json`.
- **Términos:** quedó registrada la aceptación de José Francisco Ñáñez. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.1.0-2026-11-25.md` y en `.pdf`.
- **Marca:** dejé `_CRITERIO_RIESGOS.txt` en la carpeta de la entidad.
- **Ficha de octubre:** lleva la revisión de la declaración por la junta del 2026-02-26 y la aprobación del exceso de L-04 hasta el 2027-01-31. Sobre L-03 el acta solo «toma nota del plan», así que no la registré como aprobación.

Nadie podía responder, así que tomé todas las respuestas de los documentos. El periodo es 2026-10, el último con exposición reportada. Los plazos de 10 días para reportar y 12 meses para revisar salen de la declaración de apetito. Los 30 días para registrar un evento y los 12 meses para los eventos repetidos salen de la política de riesgo operacional. Lo que encuentro se publica en Rostrum, porque los documentos no dicen lo contrario.

# Cada exposición contra su límite · Banco Control de Riesgos Sintético · periodo 2026-10

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 5.8 | no | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-10 |
| L-03 | Concentración en el mayor deudor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo sobre ingresos | máximo 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Exposición a contrapartes sin calificación | máximo 15 % | 12 | no | — | Tesorería | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-10 (families/criterio-cro/FUENTES.es.md)

---

El reporte dice «Sin documentos citados» en las fuentes, aunque la ficha sí cita la declaración y el acta. Así lo escribió el motor y no lo cambié.

**Cuándo vuelvo:** sin reloj, porque en una sesión sin interfaz nadie puede aceptar la tarea programada. Para correrlo a mano: `/criterio-risk-appetite:appetite-wake`.

La corrida quedó registrada como `2026-11-25-appetite-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.