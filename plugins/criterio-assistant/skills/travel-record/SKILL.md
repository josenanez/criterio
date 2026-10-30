---
name: travel-record
description: "Cómo se lleva a la ficha un viaje del ejecutivo: cada vuelo del itinerario con su número, su ruta y su salida y su llegada con fecha, hora y zona horaria, cada uno con su cita. Úsalo al procesar los itinerarios de 30-viajes/. Travel itinerary, flight record, trip against the calendar."
---

# La ficha de un viaje

Una por itinerario de `30-viajes/`, en `<estado>/viajes/<nombre del archivo sin extensión>.json`:

```json
{
  "file": "30-viajes/2026-11-03-itinerario-quito.md",
  "trip": "Quito",
  "flights": [
    {"flight": "AV 9341", "from": "Bogotá", "to": "Quito",
     "depart": "2026-11-03T06:00-05:00", "arrive": "2026-11-03T07:35-05:00",
     "source": "30-viajes/2026-11-03-itinerario-quito.md, línea 7"},
    {"flight": "AV 9342", "from": "Quito", "to": "Bogotá",
     "depart": "2026-11-05T18:00-05:00", "arrive": "2026-11-05T19:35-05:00",
     "source": "30-viajes/2026-11-03-itinerario-quito.md, línea 8"}
  ]
}
```

## Las reglas

1. **Un vuelo por tramo**, en el orden del itinerario, con el número tal como lo trae el documento. Un hotel o un traslado no es un vuelo: no va.
2. **`depart` y `arrive` llevan fecha, hora y zona horaria**, `AAAA-MM-DDTHH:MM±HH:MM`: la hora local de la ciudad de salida y la de llegada, con el desfase que dice el itinerario. Si el itinerario no dice la zona de una hora, el vuelo queda sin esa hora y se dice en la corrida: el motor no cruza un vuelo con la hora a medias.
3. **`from` y `to` son las ciudades** como las nombra el itinerario, no los códigos de aeropuerto si trae el nombre. El motor toma la ciudad de salida del primer vuelo como la ciudad del ejecutivo, y si el último vuelo vuelve a ella, el tiempo entre los dos es el viaje.
4. **Cada vuelo con su cita**, `<archivo>, línea N`, a la línea del itinerario que lo trae.
5. **El cruce lo hace el motor**: qué reunión cae durante un vuelo, qué reunión presencial en la ciudad del ejecutivo cae mientras está de viaje y qué vuelo no está en la agenda. Un vuelo está en la agenda cuando un evento lleva su número en el título. Tú no marcas cruces ni mueves reuniones.
