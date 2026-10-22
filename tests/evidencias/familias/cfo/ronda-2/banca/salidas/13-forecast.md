# /criterio-budget:forecast 

Términos vigentes (versión 1.2), aceptados por José Francisco Ñáñez el 2026-10-06. Ninguna de las proyecciones es la correcta por definición: la decisión de cuál usar es de una persona, y los supuestos van escritos debajo de la tabla.

# Proyección al cierre del año · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `forecast`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |
|---|---|---|---|---|---|
| Administración | Mantenimiento | 24.000.000,00 | 23.520.000,00 (2026-09-30) | 23.280.000,00 | 23.460.000,00 |
| Administración | Servicios públicos | 36.000.000,00 | 35.280.000,00 (2026-09-30) | 41.400.000,00 | 40.050.000,00 |
| Comercial | Eventos | 21.000.000,00 | 20.580.000,00 (2026-09-30) | 19.400.000,00 | 20.550.000,00 |
| Comercial | Publicidad | 45.000.000,00 | 44.100.000,00 (2026-09-30) | 44.620.000,00 | 43.965.000,00 |
| Operaciones | Transporte | 46.800.000,00 | 45.864.000,00 (2026-09-30) | 43.844.000,00 | 45.783.000,00 |
| Personal | Nómina | 240.000.000,00 | 240.000.000,00 (2026-09-30) | 240.000.000,00 | 240.000.000,00 |
| Tecnología | Licencias | 55.200.000,00 | 54.096.000,00 (2026-09-30) | 55.096.000,00 | 53.922.000,00 |
| Tecnología | PRY-310 | 72.000.000,00 | 70.560.000,00 (2026-09-30) | 69.840.000,00 | 70.380.000,00 |

**Al ritmo:** el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido. **Al plan:** el ejecutado más lo que falta del aprobado según su distribución mensual.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La 1: el acta 01 del 2026-01-20 es la única que aprueba una versión. La v2 (2026-06-30) no tiene acta de aprobación; el acta 05 solo aprueba un traslado de 3,000,000.00.
- ¿Quién es el responsable de cada área? → No encontrado en los documentos; sin responsable asignado.
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- ¿Fechas del comité de presupuesto? → No encontradas; el acta 06 habla de «el próximo comité» sin fecha.
- ¿Fichas PMO? → estado-pmo/records, con PRY-310.json.
- ¿Marcar la carpeta con _CRITERIO_FINANZAS.txt? → No: nadie lo autorizó; no se escribió nada en los documentos.

## Fuentes

- Sin documentos citados.

---
La corrida quedó registrada como `2026-10-06-forecast-1`. El motor reportó 5 hallazgos, cifra que no desglosó en esa salida.