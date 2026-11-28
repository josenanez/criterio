# /criterio-changes:service-check 

Corrí `service-check` para el periodo 2026-10 y dos servicios quedaron por debajo del nivel acordado en el catálogo. Decidirlo y calificarlo es del comité de cambios y del área de tecnología. El periodo lo elegí yo, porque el comando no traía ninguno. Los términos (versión 1.6) ya estaban vigentes, así que no registré ninguna aceptación nueva.

# Cada servicio contra su nivel · Banco del Istmo Sintético · periodo 2026-10

**Entidad:** Banco del Istmo Sintético (155612345-2-2019) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.2.0 · **Comando:** `service-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Disponibilidad por debajo del nivel acordado (`service_below_level`) | S-11 · Pagos en línea: dio 99.4 % en 2026-10 y el catálogo acuerda 99.9 % | `20-servicio/disponibilidad_2026-10.xlsx` fila 5 · `00-politica/catalogo_de_servicios.xlsx` fila 5 |
| 2 | Disponibilidad por debajo del nivel acordado (`service_below_level`) | S-12 · Aplicación móvil: dio 98.7 % en 2026-10 y el catálogo acuerda 99.5 % | `20-servicio/disponibilidad_2026-10.xlsx` fila 6 · `00-politica/catalogo_de_servicios.xlsx` fila 6 |

## El resultado

| Servicio | Nivel acordado | Disponibilidad del periodo |
|---|---|---|
| S-01 · Banca en línea | 99.9 % | 99.95 % |
| S-02 · Pagos | 99.5 % | 99.5 % |
| S-03 · Correo | 99 % | 99.2 % |
| S-11 · Pagos en línea | 99.9 % | 99.4 % |
| S-12 · Aplicación móvil | 99.5 % | 98.7 % |

El nivel lo acuerda el área con el negocio, en el catálogo: aquí se dice qué servicio no lo cumplió.

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `00-politica/catalogo_de_servicios.xlsx`
- `20-servicio/disponibilidad_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-service-check-1`, con la salida en `estado-tecnologia/155612345-2-2019-banco-del-istmo-sintetico/corridas/salida-service-check.md`.

El reporte lo dejó el motor en `cambios/2026-10/reporte-service-check.md`. Copié ese archivo como la salida de la corrida en vez de reescribirlo.

La tabla de arriba es el reporte del motor sin las columnas Monto, Responsable y Días, que venían vacías (—) en ambas filas.