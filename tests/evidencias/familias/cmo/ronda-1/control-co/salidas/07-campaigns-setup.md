# /criterio-campaigns:campaigns-setup mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos

Próspero quedó listo para Almacenes Control de Mercadeo Sintéticos (NIT 901444666), y el primer cruce de octubre no muestra nada que atender.

Todas las respuestas salieron de los documentos o de la instrucción de la prueba:
- **Carpeta:** `mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos`. Era la única candidata y ya tenía la marca `_CRITERIO_MERCADEO.txt`, así que no la volví a dejar.
- **Periodo:** 2026-10, el del informe de resultados en `50-campanas/`.
- **Tolerancias:** 5 % sobre el presupuesto y 2 % entre el resultado y la plataforma. Las dos salen de la política de publicidad.
- **Rostrum:** sí; es el valor por omisión y la política no dice otra cosa.
- **Estado:** `estado-mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos`, fuera de los documentos.
- **Términos v1.6:** los acepta José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-campaigns-0.1.0-2026-11-25.md`, con su `.pdf`.

La configuración quedó en `.criterio/campanas/901444666/config.json`. Llevé a la ficha los tres resultados del informe de octubre, con el corte que declara. Este es el reporte del motor:

---

# Cada campaña contra su presupuesto · Almacenes Control de Mercadeo Sintéticos · periodo 2026-10

**Entidad:** Almacenes Control de Mercadeo Sintéticos (901444666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 104,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | 1200 recompras | Recompras |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 7,000,000 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea diaria necesita un sí explícito y en esta prueba nadie podía darlo. Para correrlo a mano: `/criterio-campaigns:campaigns-wake`.

La corrida quedó registrada como `2026-11-25-campaigns-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.