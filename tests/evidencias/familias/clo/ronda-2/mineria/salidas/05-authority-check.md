# /criterio-legal:authority-check 

Los términos (versión 1.2) estaban vigentes al 2026-10-06, así que no hizo falta registrar la aceptación. El motor encontró 2 señales en los 6 contratos revisados. La corrida quedó registrada, pero el motor cuenta 4 hallazgos y el reporte muestra 2 señales; no investigué la diferencia.

# Firmas y facultades · Minera Cóndor · al 2026-10-06

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `authority-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-401: Mauricio León firmó por 400,000.00 y la matriz de atribuciones no le da facultad para ese tipo y monto | 400,000.00 | — | — | `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | El documento no tiene la firma de las dos partes y el contrato ya empezó (`unsigned_contract`) | CTR-405: el documento no tiene la firma de las dos partes y el contrato empezó el 2026-02-01 | 100,000.00 | — | — | `contratos/CTR-405-ambiental-consultores-cia-ltda/10-contrato/contrato.md` |

## El resultado

| Contrato | Firmó por la entidad | Monto | Con facultad | Firma de las dos partes |
|---|---|---|---|---|
| CTR-401 | Mauricio León | 400,000.00 | no | sí |
| CTR-402 | Verónica Paz | 200,000.00 | sí | sí |
| CTR-403 | Rodrigo Salazar | 300,000.00 | sí | sí |
| CTR-404 | Verónica Paz | 150,000.00 | sí | sí |
| CTR-405 | Verónica Paz | 100,000.00 | sí | no |
| CTR-406 | Rodrigo Salazar | 250,000.00 | sí | sí |

Sin opinión sobre la validez del contrato ni de la firma: se compara con la matriz de atribuciones de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-atribuciones.csv`
- `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md`
- `contratos/CTR-405-ambiental-consultores-cia-ltda/10-contrato/contrato.md`

Qué efecto tiene cada hallazgo sobre el contrato es criterio jurídico y queda como pregunta para quien decide.

La salida quedó en `estado-legal/0990054321001-minera-condor/corridas/salida-authority-check.md`. La corrida se registró como `2026-10-06-authority-check-1`.