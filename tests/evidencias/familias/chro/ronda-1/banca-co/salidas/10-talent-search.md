# /criterio-talent:talent-search 

Los términos están vigentes. No indicaste vacante, así que tomé **VAC-01** (perfil PC-01, Contador). Es la primera abierta del registro y, según el último talent-scan, la que más días lleva pasada de su plazo.

# La búsqueda de VAC-01 · Banco Cordillera Sintético · 2026-11-16

**Vacante:** VAC-01 · **Perfil:** PC-01 · **Ocupación (CUOC):** 24111

## Las cadenas de búsqueda

Se arman con los nombres que da el estándar a la ocupación 24111 y con los requisitos esenciales del perfil PC-01.

- **Nombres de la ocupación:** Contador · Contadora · Contador público · Contadora pública
- **Requisitos esenciales:** Contabilidad bajo NIIF · Análisis de procesos contables · Tarjeta profesional de contador vigente

```
("Contador" OR "Contadora" OR "Contador público" OR "Contadora pública") AND ("Contabilidad bajo NIIF" OR "Análisis de procesos contables" OR "Tarjeta profesional de contador vigente")
```

Estas cadenas las corre quien recluta, en su propio buscador. Yo no entré a ninguna red ni busqué a nadie fuera de lo que entregó la organización.

## La base interna

Van en el orden de su identificador, sin puntaje:

| Persona | Ocupación | Relación con 24111 | Cargo | Cita |
|---|---|---|---|---|
| P-01 | 24111 | Misma ocupación | Cargo interno sintético | `50-ats/base-interna.csv` fila 2 |
| P-03 | 43111 | Ocupación afín | Cargo interno sintético | `50-ats/base-interna.csv` fila 4 |

Quien recluta decide a quién contactar. Se procesó todo lo que llegó.

---

La corrida quedó registrada como `2026-11-16-talent-search-1`. Lo que mostré está guardado en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-talent-search.md`.