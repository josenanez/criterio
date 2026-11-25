# /criterio-claims:promo-check 

La corrida de `/promo-check` quedó registrada, pero el reporte salió vacío. Los términos (versión 1.6) ya estaban vigentes, así que no pedí aceptarlos de nuevo. La entidad es Consumo Maya Sintético (CMS210415XY3), periodo 2026-11, corte 2026-11-25.

# Cada promoción con sus condiciones · Consumo Maya Sintético · periodo 2026-11

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `promo-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Promoción | Inicio | Fin | Condiciones de modo y lugar | Bases |
|---|---|---|---|---|

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

**Qué significa:** la tabla de promociones está vacía, es decir, la ficha del periodo 2026-11 no trae ninguna promoción. Eso puede ser porque no hay bases en `30-promociones/` o porque falta correr `/criterio-claims:claims-scan` para llevarlas a la ficha. No revisé cuál de las dos es; este comando solo lee la ficha.

**Discrepancia:** el registro de la corrida (`2026-11-25-promo-check-1`) reporta `"hallazgos": 3`, pero el reporte muestra cero señales abiertas. No sé qué cuenta ese número. Conviene revisarlo antes de dar el resultado por limpio.

El reporte está en `estado-mercadeo/cms210415xy3-consumo-maya-sintetico/piezas/2026-11/reporte-promo-check.md`. Copié ese mismo texto a `corridas/salida-promo-check.md` y lo registré con `--caso 2026-11`.

Las preguntas de esta sesión no se hicieron, porque el comando no hizo ninguna.