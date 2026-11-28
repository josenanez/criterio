# /criterio-revenue:discount-check 

Tres de las cinco cotizaciones del periodo 2026-10 tienen un descuento sin la aprobación que pide la matriz. Los términos estaban vigentes (versión 1.6), así que no hizo falta registrar la aceptación.

La primera llamada la hice con el periodo 2026-11 por suposición y salió vacía. La configuración y la ficha con las cotizaciones son de 2026-10, así que repetí el reporte con ese periodo. Eso dejó un `reporte-discount-check.md` vacío en `ingresos/2026-11/`, que queda como sobrante.

Resultado de `discount-check` (el reporte del motor, copiado sin cambios):

# Los descuentos contra su política · Almacenes del Istmo · periodo 2026-10

**Entidad:** Almacenes del Istmo (155622222-2-2017) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 1.4.2 · **Comando:** `discount-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-2603 · OPP-2603: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 95,700.00 | — | — | `40-cotizaciones/COT-2603_cotizacion.pdf, p. 1` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 2 | (igual) | COT-2604 · OPP-2627: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 42,900.00 | — | — | `40-cotizaciones/COT-2604_cotizacion.pdf, p. 1` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 3 | (igual) | COT-2605 · OPP-2628: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 33,000.00 | — | — | `40-cotizaciones/COT-2605_cotizacion.pdf, p. 1` · `00-referencia/matriz-descuentos.csv` fila 4 |

## El resultado

| Cotización | Oportunidad | Descuento | Nivel | Pide | Aprobó | Cargo | Dentro de la política |
|---|---|---|---|---|---|---|---|
| COT-2601 | OPP-2601 | 10.00 % | 1 | ninguno | — | — | sí |
| COT-2602 | OPP-2602 | 18.00 % | 2 | gerente_comercial | Marta Gil | gerente comercial | sí |
| COT-2603 | OPP-2603 | 22.00 % | 3 | gerente_general | Marta Gil | gerente comercial | no |
| COT-2604 | OPP-2627 | 22.00 % | 3 | gerente_general | Marta Gil | gerente comercial | no |
| COT-2605 | OPP-2628 | 22.00 % | 3 | gerente_general | Marta Gil | gerente comercial | no |

Ningún descuento lo aprueba el agente: aquí se dice cuál no tiene la aprobación que pide la matriz.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-descuentos.csv`
- `40-cotizaciones/COT-2603_cotizacion.pdf, p. 1`
- `40-cotizaciones/COT-2604_cotizacion.pdf, p. 1`
- `40-cotizaciones/COT-2605_cotizacion.pdf, p. 1`

La salida quedó en `corridas/salida-discount-check.md` y la corrida se registró como `2026-11-05-discount-check-1`.