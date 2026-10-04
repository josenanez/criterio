# Acta — Originación digital (PRY-200) · 2026-09-30
**Asistieron:** Óscar Ramírez (gerente), Sandra Gil (patrocinadora), Andrés Cely (arquitectura), Paola Rueda (seguridad), Laura Pinzón (PMO) · **Fuente:** `30-reuniones/2026-09-30-notas-reunion-seguimiento.md` · **Ausentes con tema en agenda:** ninguno

## Compromisos

| Quién | Qué | Para cuándo | Nota |
|---|---|---|---|
| Óscar Ramírez | Presentar solicitud de cambio CC-01 al comité | 2026-10-12 | El comité es ese día. CC-01 lleva desde el 2026-09-11 sin presentarse. |
| Paola Rueda | Revisión final de seguridad | 2026-10-15 | **Reprogramado 2 veces** (era 2026-09-25, luego 2026-10-03). Motivo: sin disponibilidad del equipo de seguridad. |
| Óscar Ramírez | Conseguir acta de recibo del ambiente de pruebas firmada por el proveedor | ~2026-10-04 | Dijo *«esta semana»*. Sin fecha exacta. |

### Sin fecha

| Quién | Qué | Nota |
|---|---|---|
| Andrés Cely | Repetir la prueba de carga con la conexión al core corregida | Dijo *«la semana que viene»* (línea 35–36) — no es una fecha. |

## Decisiones

Ninguna. No se tomó ninguna decisión formal en esta reunión.

## Quedó sin decidir

| Qué | Por qué | Quién tiene la facultad |
|---|---|---|
| Qué pasa si la prueba de carga no pasa antes de la revisión de seguridad | Andrés lo planteó (línea 24–25): la salida a producción se corre a noviembre. Nadie respondió. Sandra dijo *«lo ve en el comité»* (línea 26). | Comité de Banca Empresas / Sandra Gil |
| Si el proyecto sigue en verde | Sandra dijo *«si el 12 no tenemos el acta y la carga, el proyecto no está en verde»* (línea 39). Óscar no contestó. No hubo cambio de estado. | Óscar Ramírez (declara) / Sandra Gil (puede exigirlo) |

## Intenciones sin doliente

Ninguna en esta reunión — cada compromiso tiene nombre.

## Dicho al pasar y no registrado

| Qué | Quién lo dijo | Categoría | Ya estaba en el RAID |
|---|---|---|---|
| Si la prueba de carga no pasa antes de la revisión de seguridad, la salida a producción se corre a noviembre | Andrés Cely (línea 24–25) | Dependencia / riesgo de calendario | No. El informe del 2026-09-22 registra *«disponibilidad del equipo de seguridad»* como riesgo abierto, pero no la dependencia secuencial carga → seguridad → producción. |
| *«El piloto no necesita esa carga»* — el umbral pactado (2.000 TPS) no aplica según Óscar para el piloto | Óscar Ramírez (línea 13–14) | Supuesto no declarado | No. Si el criterio de aceptación del piloto es distinto al del go-live, no hay documento que lo establezca. |

## Cerrado en esta reunión

Nada. El ambiente de pruebas se declaró certificado verbalmente (línea 16–17) pero Sandra pidió el acta de recibo y no existe todavía (línea 18). Sin documento no se cierra.

## Lo que esta reunión contradice

| Campo | Dijo la reunión | Dice el expediente | Fuente de cada uno |
|---|---|---|---|
| Estado del proyecto | Sandra: *«si el 12 no tenemos el acta y la carga, el proyecto no está en verde»* (línea 39). Óscar mantiene verde. | Verde, informe del 2026-09-22 | Notas línea 39 vs. `20-seguimiento/2026-09-22-informe-avance.md` línea 9 |
| Certificación del ambiente de pruebas | Óscar: *«está certificado desde la semana pasada»* (línea 16–17) | El informe del 2026-09-22 dice *«se cerró la certificación del ambiente de pruebas»* (línea 16), pero no hay acta de recibo | Notas línea 17–18 vs. informe línea 16 |
| Resultado de la prueba de carga | Falló dos veces (1.400 vs 2.000 TPS). Óscar dice que no afecta el semáforo. | El informe dice *«no alcanzó el umbral pactado y se repite»* sin indicar que falló de nuevo | Notas línea 11–14 vs. informe línea 17 |

## Sin resolver de la transcripción

- **¿El umbral del piloto es distinto al del go-live?** Óscar dijo que el piloto no necesita 2.000 TPS (línea 13–14), pero no hay documento que defina un umbral distinto para el piloto. Si existe, falta en la carpeta.

---

**4 compromisos extraídos** (3 con fecha, 1 sin fecha) · **1 reprogramado 2 veces** (Paola, revisión de seguridad) · **0 decisiones** · **2 temas sin decidir que van al comité del 12 de octubre** · **2 riesgos dichos al pasar y no registrados**

Cuando quieras ver el seguimiento completo: `/pm-commitments`. Si algún campo de la ficha cambió — y esta reunión sugiere que el estado podría cambiar —: `/pm-publish`.
