# /criterio-talent:talent-search 

Corrí la búsqueda para **VAC-51** (perfil PT-01, cajero de tienda, O\*NET 41-2011.00) de Almacenes del Pacífico Sintéticos. El argumento no traía vacante. Tomé VAC-51 porque, de las abiertas, es la que más tiempo lleva pasada del plazo según el reporte de estado de vacantes. Los términos ya estaban aceptados para esta versión, así que no hubo que registrarlos.

**Cadena de búsqueda.** Sale de las denominaciones de la ocupación en el estándar y de los dos requisitos esenciales del perfil:

```
("Cajero de tienda" OR "Cashiers (synthetic)") AND ("Escucha activa con el cliente" OR "Matemáticas para el arqueo de caja")
```

La corre quien recluta, en su propio buscador. Yo no entré a ninguna red ni busqué a nadie fuera de lo que entregó la organización.

**Base interna.** Una sola persona tiene la misma ocupación:

| Persona | Ocupación | Misma ocupación | Cargo | Cita |
|---|---|---|---|---|
| P-01 | 41-2011.00 | Sí | Cargo interno sintético | `50-ats/base-interna.csv` fila 2 |

Ninguna persona está ordenada por puntaje; quien recluta decide a quién contactar. No quedó ningún archivo sin procesar.

**Registro.** La salida completa quedó en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/corridas/salida-talent-search.md` y la corrida se registró como `2026-11-16-talent-search-1`.