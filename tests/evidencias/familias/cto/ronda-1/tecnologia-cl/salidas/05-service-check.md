# /criterio-changes:service-check 

Los términos están vigentes (versión 1.6, aceptada el 2026-11-25 por José Francisco Ñáñez). No hubo que registrar nada nuevo.

Usé el periodo de la configuración, 2026-10. Una primera corrida sobre 2026-11 salió con la tabla vacía, porque no hay disponibilidad de ese mes.

# Cada servicio contra su nivel · Software Austral Sintético · periodo 2026-10

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `service-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo (`service_below_level`) | S-11 · Pagos en línea: dio 99.4 % de disponibilidad en 2026-10 y el catálogo acuerda 99.9 % | — | — | — | `20-servicio/disponibilidad_2026-10.xlsx` fila 5 · `00-politica/catalogo_de_servicios.xlsx` fila 5 |
| 2 | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo (`service_below_level`) | S-12 · Aplicación móvil: dio 98.7 % de disponibilidad en 2026-10 y el catálogo acuerda 99.5 % | — | — | — | `20-servicio/disponibilidad_2026-10.xlsx` fila 6 · `00-politica/catalogo_de_servicios.xlsx` fila 6 |

## El resultado

| Servicio | Nivel acordado | Disponibilidad del periodo |
|---|---|---|
| S-01 · Tienda en línea | 99.9 % | 99.95 % |
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

---
La corrida quedó registrada como `2026-11-25-service-check-1`. La salida completa está en `estado-tecnologia/76543210-k-software-austral-sintetico/corridas/salida-service-check.md`. Quedó también el reporte vacío de 2026-11 en la carpeta de cambios de ese mes.