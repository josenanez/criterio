# /criterio-product:product-publish 

**No publiqué la ficha de PRD-309 (Microseguros).** La configuración (`.criterio/producto/PRD-309/config.json`) no define una carpeta de productos publicados, así que el comando no tiene dónde escribir `PRD-309.json`. No inventé la carpeta. Definirla es una decisión de la organización, no de este comando.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no registré una aceptación nueva.

Esto es lo que habría llevado la ficha, con corte al 2026-10-16:
- **Requerimientos:** 16, de los cuales 12 están aceptados y 4 propuestos.
- **Proyectos:** 0. Ningún requerimiento tiene proyecto asociado, así que hoy no habría nada que cruzar por proyecto.
- **Métricas afirmadas:** 1. `volumen_mensual` = 276481, tomada de `documentos/productos/PRD-309/00-definicion/2026-01-25-caso-de-negocio.md`. El tablero del 2026-10-14 mide 194582, un 29.6 % por debajo. La ficha llevaría solo la cifra afirmada, no la medida.
- **Segmento declarado:** Pensionados.
- **Gerente:** Beatriz Cuéllar.

Dejé la corrida registrada como `2026-10-16-product-publish-1`, con la salida guardada en `estado-producto/PRD-309/corridas/salida-product-publish.md`.

Para publicar, hay que definir la carpeta común de fichas publicadas en la configuración y volver a correr `/product-publish`.