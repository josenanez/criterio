# /criterio-assistant:ea-setup direccion/direccion-general

Ofelia quedó configurada para la oficina de la Dirección general de Plásticos Control. La aceptación de los términos (versión 1.6) quedó registrada a nombre de José Francisco Ñáñez, con fecha 2026-10-26. La validación no encontró problemas.

- **Configuración:** está en `.criterio/direccion/direccion-general/config.json`. Las respuestas salen de `00-referencia/oficina.md` y `00-referencia/organos.csv`; los umbrales son los de `config.example.json`, Rostrum está apagado y el estado se guarda en `estado-direccion/direccion-general`.
- **Comprobante:** en `.criterio/terminos/`, como `aceptacion-criterio-assistant-1.4.2-2026-10-26.md` y su `.pdf`.
- **Lo que procesé:** 4 sesiones, de las cuales solo 2 tienen acta firmada, más 3 correos recibidos y 1 itinerario. Las 2 respuestas de la oficina las cruzó el motor. Ninguna ficha trajo `record_issues`.
- **Lo que no hice:**
  - No dejé la marca `_CRITERIO_DIRECCION.txt`, para no escribir dentro de los documentos.
  - No creé la tarea programada diaria, porque necesita un sí explícito que en esta prueba nadie podía dar. A mano se corre con `/criterio-assistant:ea-wake`.
- **Un desvío de las reglas:** una vez usé `cd` y `cat` para listar los documentos, cuando el comando pide no hacerlo. No cambió nada. El resto de las llamadas fueron por ruta absoluta.

# La semana · Plásticos Control · al 2026-10-26 · oficina de Dirección general

**Entidad:** Plásticos Control · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.4.2 · **Comando:** `ea-agenda`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

Agenda exportada el 2026-10-25 (`10-agenda/agenda-2026-10-25.ics`), del 2026-10-26 al 2026-11-09.

| Inicio | Fin | Reunión |
|---|---|---|
| 2026-10-26 08:30 | 09:30 | Desayuno con la calificadora |
| 2026-10-27 08:00 | 12:00 | Bloque de concentración (libre) |
| 2026-10-27 09:00 | 10:00 | Reunión de seguimiento |
| 2026-10-29 14:00 | 17:00 | Sesión de la junta |
| 2026-10-30 12:30 | 14:00 | Almuerzo con el comité de auditoría |
| 2026-11-02 | todo el día | Día sin reuniones |
| 2026-11-02 08:00 | 09:30 | Comité de presidencia |
| 2026-11-05 07:00 | 08:20 | Vuelo Y4 3010 Ciudad de México–Guadalajara |
| 2026-11-05 10:00 | 12:00 | Visita a la planta |
| 2026-11-05 15:00 | 16:00 | Comité de compras |
| 2026-11-05 19:00 | 20:20 | Vuelo Y4 3017 Guadalajara–Ciudad de México |

| Órgano | Sesión | Días | Material | Acta |
|---|---|---|---|---|
| comite-de-direccion | 2026-09-21 | -35 | 1 | sí |
| comite-de-direccion | 2026-10-19 | -7 | 1 | no |
| consejo-de-administracion | 2026-09-24 | -32 | 2 | sí |
| consejo-de-administracion | 2026-10-29 | 3 | 1 | no |

| Viaje | Vuelo | Ruta | Sale | Llega | En la agenda |
|---|---|---|---|---|---|
| Guadalajara | Y4 3010 | Ciudad de México → Guadalajara | 2026-11-05 07:00 | 08:20 | sí |
| Guadalajara | Y4 3017 | Guadalajara → Ciudad de México | 2026-11-05 19:00 | 20:20 | sí |

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

---

**Cuándo vuelvo:** sin reloj. La corrida quedó registrada como `2026-10-26-ea-setup-1`, y su salida está en `estado-direccion/direccion-general/corridas/salida-ea-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.