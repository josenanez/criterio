# /criterio-legal:contract-register 

Los términos (versión 1.2) ya estaban vigentes y aceptados, así que no hizo falta registrar la aceptación de nuevo. Corrí el cruce con fecha de corte 2026-10-06.

# Registro de contratos · Banco Andino · al 2026-10-06

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `contract-register`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El valor o las fechas del registro no son los del documento (`register_differs_from_contract`) | CTR-102: valor 300.000.000,00 en el registro y 250.000.000,00 en el documento | — | — | — | `10-registro/registro-contratos.csv` fila 3 · `contratos/CTR-102-papeleria-nacional-s-a-s/10-contrato/contrato.md` |

## El resultado

| Contrato | Contraparte | Estado en el registro | Estado según sus fechas | Diferencias |
|---|---|---|---|---|
| CTR-101 | Soluciones Andinas S.A.S. | vigente | vigente | — |
| CTR-102 | Papelería Nacional S.A.S. | vigente | vigente | valor 300.000.000,00 en el registro y 250.000.000,00 en el documento |
| CTR-103 | Inmobiliaria Centro S.A. | vigente | vigente | — |
| CTR-104 | Licencias del Norte S.A.S. | vigente | vigente | — |
| CTR-105 | Consultores Asociados S.A.S. | vigente | vigente | — |
| CTR-106 | Mantenimientos Unidos S.A.S. | terminado | terminado | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-registro/registro-contratos.csv`
- `contratos/CTR-102-papeleria-nacional-s-a-s/10-contrato/contrato.md`

La corrida quedó registrada como `2026-10-06-contract-register-1`. Lo que mostré está guardado en `estado-legal/900123456-banco-andino/corridas/salida-contract-register.md`.

El motor reporta 5 hallazgos en la corrida registrada y el reporte lista uno. No averigüé de dónde sale esa diferencia.

En la nota de la corrida puse 0 contratos sin registro y 0 registros sin documento. Eso lo deduje de que el reporte no marca ninguno; el motor no me dio esas cifras.

La diferencia de valor en CTR-102 queda para que la revise una persona. No opino sobre cuál de los dos valores es el correcto.