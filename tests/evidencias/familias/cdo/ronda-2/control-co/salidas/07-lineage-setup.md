# /criterio-data-quality:lineage-setup datos/901666888-banco-control-de-datos-sintetico

Ariadna quedó instalada sobre el Banco Control de Datos Sintético (NIT 901666888). Ninguna de las cuatro cifras del informe a la junta deja algo abierto.

- **Configuración:** `.criterio/calidad/901666888/config.json`, con periodo 2026-11 y tolerancia del 0.5 %. Esa tolerancia sale de la política de datos. Las respuestas sobre la entidad, el periodo y dónde guardar el estado son las que ya había fijado Custodia.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-quality-0.2.0-2026-11-25.md` y en `.pdf`.
- **Marca de la carpeta:** ya estaba puesta, así que no hizo falta otra.

Procesé el informe a la junta y crucé sus cuatro cifras contra las de la fuente. En «Ventas netas» el valor del informe y el de la fuente no son iguales, pero el motor dice que la diferencia está dentro de la tolerancia. Por eso no queda ninguna señal abierta.

# Cada cifra contra su fuente · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `figure-check`

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

**El reloj:** no creé la tarea programada, porque esta sesión no tenía a nadie que diera un sí explícito. Se corre a mano con `/criterio-data-quality:lineage-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-lineage-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.