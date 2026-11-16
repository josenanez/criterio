# /criterio-talent:vacancy-status 

El comando `/criterio-talent:vacancy-status` no está cargado en esta sesión, pero el plugin está instalado en disco. Seguí su definición y usé su motor `talento.py` con `--today 2026-11-16`. Los términos ya estaban aceptados, así que no hubo que registrarlos de nuevo. Este es el reporte del motor, tal como lo generó:

---

# Las vacantes contra su plazo · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (900777888) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-31 | PC-11 | 2026-10-05 | 45 días | 2026-11-19 | — | 42 | Rosa Díaz |
| VAC-32 | PC-13 | 2026-08-01 | 120 días | 2026-11-29 | — | 107 | Rosa Díaz |
| VAC-33 | PC-12 | 2026-04-01 | 45 días | 2026-05-16 | 2026-05-20 | 49 | Rosa Díaz |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Plazo de cobertura de una vacante? → 45 días calendario desde la apertura, salvo plazo propio en el registro · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Días de conservación de los datos de un candidato no seleccionado? → 180 días desde que termina su proceso · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se publican los reportes de candidatos en Rostrum? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se marca la carpeta con _CRITERIO_TALENTO.txt? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)

## Fuentes

- Sin documentos citados.

---

- **Registro de la corrida:** lo que se mostró quedó guardado en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-vacancy-status.md` y la corrida está registrada como `2026-11-16-vacancy-status-1`.
- **Posible fallo del motor:** la sección "Fuentes" dice "Sin documentos citados", pero las preguntas sí citan `politica-de-seleccion.pdf`. Parece que el motor no está pasando esa cita a la lista de fuentes.