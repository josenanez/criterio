# /criterio-data-quality:lineage-setup datos/901666888-banco-control-de-datos-sintetico

Soy Ariadna. Sigo cada cifra de los informes hasta su fuente, su corte y su linaje; no corrijo cifras.

**Carpeta:** solo había una candidata, `datos/901666888-banco-control-de-datos-sintetico` (tiene 00-referencia/, 10-catalogo/, 20-informes/, 30-calidad/). Tomé el sí.

**Respuestas que tomé** de lo que Custodia ya había fijado y de la política de datos:
- **Entidad:** Banco Control de Datos Sintético, NIT 901666888, Colombia, en COP.
- **Periodo:** 2026-11.
- **Tolerancia:** 0.5 % de diferencia entre una cifra y su fuente, según `00-referencia/politica_de_datos.pdf`.
- **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
- **Estado:** `estado-datos/901666888-banco-control-de-datos-sintetico`.
- **Marca:** sí a dejar `_CRITERIO_DATOS.txt` en la carpeta.

**Términos (versión 1.6):** se mostraron tal cual. José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-data-quality-0.1.0-2026-11-25.md` y en `.pdf`. La configuración está en `.criterio/calidad/901666888/config.json` y la carpeta ya tiene la marca.

Procesé el informe de junta de octubre de 2026 y pasé sus cuatro cifras a la ficha de 2026-11. Las crucé contra `30-calidad/cifras_fuente.xlsx` al mismo corte. En «Ventas netas» el informe y la fuente traen cifras distintas, pero el motor la marca como «coincide»: la diferencia queda dentro de la tolerancia del 0.5 %.

---

# Cada cifra contra su fuente · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.1.0 · **Comando:** `figure-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Informe | Indicador | Corte | En el informe | En la fuente | Estado |
|---|---|---|---|---|---|
| `20-informes/informe_junta_2026-10.pdf` | Cartera vencida | 2026-10-31 | 1,250,000,000 | 1,250,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Clientes activos | 2026-10-31 | 84,200 | 84,200 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Ventas netas | 2026-10-31 | 9,420,000,000 | 9,400,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Margen operacional | 2026-10-31 | 3,400,000,000 | 3,400,000,000 | coincide |

Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con su fuente.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-02 (families/criterio-cdo/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta prueba nadie lo dio. Para correrlo a mano: `/criterio-data-quality:lineage-wake`.

La corrida quedó registrada como `2026-11-25-lineage-setup-1`, y lo que se mostró está en `estado-datos/901666888-banco-control-de-datos-sintetico/corridas/salida-lineage-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.