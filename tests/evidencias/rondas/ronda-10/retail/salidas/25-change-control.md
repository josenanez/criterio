# /criterio-portfolio:change-control PRY-200 mover la salida a producción 30 días

## Solicitud de cambio PRY-200 (Tienda en línea): pasar la salida a producción 30 días, de 2027-01-02 a 2027-02-01

El cambio no tiene a nadie con autoridad declarada para aprobarlo, así que lo mando a comité y no creo línea base nueva.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-18). No hizo falta registrarlos otra vez.

- **Alcance:** no declara cambio. Si el alcance sigue igual y el tiempo sube 30 días, alguien absorbe la diferencia en horas o en calidad, y nadie lo dice.
- **Tiempo:** el cierre sube 30 días contra la línea base 1, que es la única.
- **Costo:** la solicitud no declara nada. La proyección actual (18.137.414.819 COP) ya supera lo aprobado (18.000.000.000) en 137.414.819 COP, y los 30 días extra no están costeados en ningún documento.
- **Piloto en tiendas:** sigue pendiente para el 2026-10-24, a 6 días. La solicitud no dice si se mueve.
- **Portafolio:** el cálculo no alcanza a ningún otro proyecto, porque el acta dice «Ninguna declarada» y ninguna otra ficha cita PRY-200. Eso no prueba que nadie dependa de él. Tampoco puedo decir cuántos días se mueve cada actividad, porque la ficha no tiene holgura por actividad.
- **Quién decide:** el acta no declara autoridad para cambios de fecha, y ese es el hallazgo de fondo. Recomiendo llevarlo al Comité de Arquitectura. Es mi recomendación, no una cláusula del acta.
- **Si se aprueba:** sería la línea base 2, con cierre 2027-02-01 y desviación de +30 días contra la original. La línea base 1 no se toca.

Tomé la respuesta por defecto en lo que faltaba: no consta quién pide el cambio, el motivo, el costo ni qué pasa con el piloto, y lo dejé escrito así en vez de inventarlo. El informe del 2026-10-07 lista tres incidencias abiertas sin dueño (prueba de carga, hallazgo de seguridad en pagos y rotación de un desarrollador). Podrían explicar el cambio, pero ningún documento las vincula con él.

La corrida quedó registrada como `2026-10-18-change-control-1`. El texto completo está en `/home/claude/banco/ronda-10/retail/espacio/estado/corridas/salida-change-control.md`.