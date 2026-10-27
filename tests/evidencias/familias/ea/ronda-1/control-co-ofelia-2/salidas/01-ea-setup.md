# /criterio-assistant:ea-setup direccion/gerencia-general

La instalación quedó hecha para Gerencia general (Distribuidora Control, CO). El motor no encontró cruces de agenda, sesiones sin material ni compromisos vencidos. Nadie respondió preguntas: tomé las 9 respuestas de `00-referencia/oficina.md`, `organos.csv` y `config.example.json`.

**Lo que hice**
- **Carpeta raíz:** la única candidata era `direccion/gerencia-general`, así que la tomé.
- **Marca de la raíz:** no dejé `_CRITERIO_DIRECCION.txt`. Nadie la autorizó y no escribí nada dentro de los documentos.
- **Configuración:** la escribí en `.criterio/direccion/gerencia-general/config.json` y el motor la validó sin problemas. El estado va en `estado-direccion/gerencia-general`, fuera de los documentos.
- **Términos:** mostré los de la versión 1.2 (texto literal arriba) y registré la aceptación a nombre de José Francisco Ñáñez, con fecha 2026-10-26. El comprobante, en Markdown y PDF, está en `.criterio/terminos/`.
- **Fichas:** escribí las de las 4 sesiones y de los 3 correos que lo pedían. Las dos respuestas de la oficina no llevan ficha; el motor las empareja por `In-Reply-To`.

**Lo que encontré**
- **Agenda:** hay una exportación del 2026-10-25, con 6 eventos entre el 2026-10-26 y el 2026-11-09. El motor no marca cruces.
- **Sesiones:** la junta del 2026-10-29 está a 3 días y tiene 1 material, pero aún no tiene acta. El comité del 2026-10-19 tiene 1 material y no tiene acta.
- **Compromisos:** ninguno vencido, y el informe de cartera vencida de Camilo Prieto quedó cumplido con evidencia. Esa evidencia es una línea del `informe-de-gestion.md` de la sesión del 2026-09-24 que dice que el informe se presentó el 2026-10-14. Es extraño que material de una sesión de septiembre mencione una fecha posterior, así que conviene verificarlo. El plan de continuidad del negocio de Jorge Silva sigue abierto y pasó del 2026-09-30 al 2026-11-20.
- **Decisión pendiente:** la ficha D-1 es el proveedor del centro de datos alterno. Tiene dos opciones, plazo 2026-12-18 y la oferta de la licitación sin disponible.
- **Correspondencia:** los dos correos que pedían respuesta ya tienen su respuesta guardada. El boletín del gremio no pide nada.
- **Notas del comité:** Natalia Rincón figura revisando los indicadores de servicio para el 2026-11-06, pero solo en las notas, no en un acta firmada. Por eso no entró a la ficha; saldrá cuando exista el acta.

**No se pudo procesar:** `90-borradores/LEEME.txt` no lleva «BORRADOR» en el nombre. No lo toqué.

La corrida quedó registrada como `2026-10-26-ea-setup-1`, con la salida completa en `estado-direccion/gerencia-general/corridas/salida-ea-setup.md`.

Esto es lo que mostró el reporte de agenda, tal cual:

# La semana · Distribuidora Control · al 2026-10-26 · oficina de Gerencia general

**Entidad:** Distribuidora Control · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 0.12.0 · **Comando:** `ea-agenda`

## Lo que hay que atender
Nada abierto en lo que procesa este comando.

## El resultado
Agenda exportada el 2026-10-25 (`10-agenda/agenda-2026-10-25.ics`), del 2026-10-26 al 2026-11-09.

| Inicio | Fin | Reunión |
|---|---|---|
| 2026-10-26 08:00 | 09:30 | Comité de presidencia |
| 2026-10-27 08:00 | 12:00 | Bloque de concentración (libre) |
| 2026-10-29 14:00 | 17:00 | Sesión de la junta |
| 2026-10-30 12:30 | 14:00 | Almuerzo con el comité de auditoría |
| 2026-11-02 | todo el día | Día sin reuniones |
| 2026-11-02 08:00 | 09:30 | Comité de presidencia |

| Órgano | Sesión | Días | Material | Acta |
|---|---|---|---|---|
| comite-de-gerencia | 2026-09-21 | -35 | 1 | sí |
| comite-de-gerencia | 2026-10-19 | -7 | 1 | no |
| junta-directiva | 2026-09-24 | -32 | 2 | sí |
| junta-directiva | 2026-10-29 | 3 | 1 | no |

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar
- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- Sin documentos citados.