# /criterio-talent:talent-search 

Los términos están vigentes: ya figuraban aceptados por José Francisco Ñáñez con fecha 2026-11-16, así que no hubo que registrarlos de nuevo. El argumento no traía la vacante y elegí **VAC-31** porque está abierta y es la que vence más pronto en el registro (2026-11-19).

## Búsqueda para VAC-31 (perfil PC-11, ocupación 24111 en la CUOC)

**Nombres de la ocupación en el estándar:** Contador, Contadora, Contador público, Contadora pública

**Requisitos esenciales del perfil:** Contabilidad bajo NIIF y tarjeta profesional de contador vigente

**Cadena de búsqueda, para que quien recluta la use en su buscador:**

```
("Contador" OR "Contadora" OR "Contador público" OR "Contadora pública") AND ("Contabilidad bajo NIIF" OR "Tarjeta profesional de contador vigente")
```

### Personas de la base interna, por identificador

| Persona | Ocupación | Relación con la vacante | Cargo | Fuente |
|---|---|---|---|---|
| P-01 | 24111 | Misma ocupación | Cargo interno sintético | `50-ats/base-interna.csv`, fila 2 |
| P-02 | 43111 | Ocupación afín | Cargo interno sintético | `50-ats/base-interna.csv`, fila 3 |

Todo se procesó; no quedó nada pendiente.

No entré a ninguna red ni busqué a nadie fuera de lo que entrega la organización. Las personas de la base interna no están ordenadas por ningún puntaje: quien recluta decide a quién contactar.

La salida quedó escrita en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-talent-search.md` y la corrida quedó registrada como `2026-11-16-talent-search-1`.