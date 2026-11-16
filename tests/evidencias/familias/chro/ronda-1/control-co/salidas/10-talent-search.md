# /criterio-talent:talent-search 

El comando `/criterio-talent:talent-search` no está cargado en esta sesión, pero el plugin sí está instalado en el equipo (`criterio-talent` 0.1.0). Seguí sus instrucciones a mano, con el motor y la fecha `--today 2026-11-16`.

- **Términos:** están vigentes. Ya estaban aceptados por José Francisco Ñáñez el 2026-11-16 (versión 1.5), así que no hubo que registrar nada nuevo.
- **Vacante:** el comando no la traía, así que tomé la sugerida: **VAC-31**. Es la vacante abierta más cerca de su tope (2026-11-19), según el reporte de estado de las vacantes.

# La búsqueda de VAC-31 · Cooperativa Control Sintética
**Perfil:** PC-11 · **Ocupación según el estándar CUOC:** 24111

**Cadena para el buscador de quien recluta:**
```
("Contador" OR "Contadora" OR "Contador público" OR "Contadora pública") AND ("Contabilidad bajo NIIF" OR "Tarjeta profesional de contador vigente")
```
- **Nombres de la ocupación en el estándar:** Contador · Contadora · Contador público · Contadora pública
- **Requisitos esenciales del perfil:** Contabilidad bajo NIIF · Tarjeta profesional de contador vigente

**Base interna, en el orden de su identificador:**

| Persona | Ocupación | ¿Misma ocupación? | Cargo | Cita |
|---|---|---|---|---|
| P-01 | 24111 | Sí | Cargo interno sintético | `50-ats/base-interna.csv`, fila 2 |
| P-02 | 43111 | No | Cargo interno sintético | `50-ats/base-interna.csv`, fila 3 |

Las personas no van ordenadas por ningún puntaje, y quien recluta decide a quién contactar. Las cadenas las corre quien recluta en su propio buscador: no entré a ninguna red ni busqué a nadie fuera de lo que entregó la organización. Todo lo que llegó se procesó.

**Registro de la corrida:** dejé lo mostrado en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-talent-search.md`. La corrida quedó registrada como `2026-11-16-talent-search-1`.