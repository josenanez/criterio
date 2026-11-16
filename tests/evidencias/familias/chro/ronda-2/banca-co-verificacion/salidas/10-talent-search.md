# /criterio-talent:talent-search 

Como no indicaste la vacante, tomé **VAC-01** (perfil PC-01). Es la que el registro de vacantes muestra abierta y fuera del plazo de cobertura. Los términos ya estaban aceptados.

# La búsqueda de VAC-01 · Banco Cordillera Sintético

**Vacante:** VAC-01 · **Perfil:** PC-01 · **Ocupación en la CUOC:** 24111 · **Fecha de corte:** 2026-11-16

## La cadena de búsqueda

La cadena usa los nombres que la CUOC da a la ocupación y los requisitos esenciales del perfil:

```
("Contador" OR "Contadora" OR "Contador público" OR "Contadora pública") AND ("Contabilidad bajo NIIF" OR "Análisis de procesos contables" OR "Tarjeta profesional de contador vigente")
```

- **Nombres de la ocupación (CUOC 24111):** Contador · Contadora · Contador público · Contadora pública
- **Requisitos esenciales de PC-01:** Contabilidad bajo NIIF · Análisis de procesos contables · Tarjeta profesional de contador vigente

Quien recluta corre esta cadena en su propio buscador. No entré a LinkedIn ni a ninguna otra red, no compré bases y no busqué a nadie fuera de lo que entregó la organización.

## La base interna

Las personas van ordenadas por su identificador, sin puntaje:

| Persona | Ocupación | Relación con 24111 | Cargo | Cita |
|---|---|---|---|---|
| P-01 | 24111 | Misma ocupación | Cargo interno sintético | `50-ats/base-interna.csv` fila 2 |
| P-03 | 43111 | Ocupación afín | Cargo interno sintético | `50-ats/base-interna.csv` fila 4 |

Quien recluta decide a quién contactar.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

---

La corrida quedó registrada como `2026-11-16-talent-search-1`. Lo que se mostró está en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-talent-search.md`.