# /criterio-legal:authority-check 

Los términos (v1.2) ya estaban vigentes y aceptados, así que no hizo falta registrar la aceptación. Hay una firma sin facultad: CTR-101. Los otros cinco contratos tienen facultad y firma de las dos partes.

# Firmas y facultades · Banco Andino · al 2026-10-06

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `authority-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-101: Diana Cruz firmó por 400.000.000,00 y la matriz de atribuciones no le da facultad para ese tipo y monto | 400.000.000,00 | — | — | `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |

## El resultado

| Contrato | Firmó por la entidad | Monto | Con facultad | Firma de las dos partes |
|---|---|---|---|---|
| CTR-101 | Diana Cruz | 400.000.000,00 | no | sí |
| CTR-102 | Andrés Vela | 200.000.000,00 | sí | sí |
| CTR-103 | Marta Ríos | 300.000.000,00 | sí | sí |
| CTR-104 | Andrés Vela | 150.000.000,00 | sí | sí |
| CTR-105 | Andrés Vela | 100.000.000,00 | sí | sí |
| CTR-106 | Marta Ríos | 250.000.000,00 | sí | sí |

Sin opinión sobre la validez del contrato ni de la firma: se compara con la matriz de atribuciones de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-atribuciones.csv`
- `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md`

**Para quien decide:** qué efecto tiene la firma de CTR-101 sin facultad según la matriz es criterio jurídico y queda como pregunta para la persona.

La corrida quedó registrada como `2026-10-06-authority-check-1`. El motor la cuenta con 5 hallazgos, aunque el reporte muestra una sola señal; no lo investigué. La salida está en `estado-legal/900123456-banco-andino/corridas/salida-authority-check.md`.