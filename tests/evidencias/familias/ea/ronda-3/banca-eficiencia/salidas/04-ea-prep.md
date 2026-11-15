# /criterio-assistant:ea-prep 

La próxima sesión es la de la Junta Directiva del 2026-10-29. Las fichas de la sesión anterior (2026-09-24) y de esta ya existían, así que no hizo falta `ea-scan`. Comparé la ficha de la decisión D-1 con `propuesta-centro-de-datos.md` y con el acta, y coinciden línea por línea. La carpeta `20-material/` de esta sesión está vacía. Las opciones aparecen en el mismo orden que en los documentos, sin ordenarlas.

# Preparar una sesión · Banco Andino · al 2026-10-26 · oficina de Presidencia

**Entidad:** Banco Andino · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.2.3 · **Comando:** `ea-prep`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una decisión pendiente tiene una fecha que la fija dentro de los días configurados (`decision_deadline`) | comite-de-presidencia, D-2: «Sede de la oficina regional» tiene plazo el 2026-11-04, en 9 días, y sigue pendiente | — | — | 9 | `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-2.md, línea 3: «La decisión vence el 2026-11-04»` |
| 2 | Una decisión pendiente tiene una fecha que la fija dentro de los días configurados (`decision_deadline`) | comite-de-presidencia, D-1: «Proveedor de la mesa de ayuda» tiene plazo el 2026-11-03, en 8 días, y sigue pendiente | — | — | 8 | `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-1.md, línea 3: «La decisión vence el 2026-11-03»` |
| 3 | Una decisión pendiente tiene una fecha que la fija dentro de los días configurados (`decision_deadline`) | junta-directiva, D-1: «Proveedor del centro de datos alterno» tiene plazo el 2026-11-02, en 7 días, y sigue pendiente | — | — | 7 | `organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md, línea 3: «La oferta del proveedor actual vence el 2026-11-02»` |
| 4 | A los días configurados de una sesión de un órgano, su material no está en la carpeta (`meeting_without_material`) | junta-directiva del 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | — | 3 | `organos/junta-directiva/2026-10-29/20-material/` |

## El resultado

### junta-directiva · 2026-10-29

**Material en la carpeta:** 0 archivo(s) — falta
**Lo que quedó abierto de la sesión del 2026-09-24:**

- C-1 · Presentar el informe de cartera vencida — Felipe Duarte, 2026-10-15 (vencido)
- C-2 · Entregar el plan de continuidad del negocio — Andrés Vela, 2026-11-20 (abierto)

**Decisión D-1: Proveedor del centro de datos alterno** — plazo 2026-11-02 (`organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md, línea 3: «La oferta del proveedor actual vence el 2026-11-02»`)

- Renovar con el proveedor actual, por tres años — evidencia: `organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md`
- Abrir una licitación con al menos tres oferentes — evidencia: `organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md`
- Lo que falta saber: La oferta económica de la licitación no está disponible todavía (propuesta-centro-de-datos.md, línea 8)

### Decisiones pendientes de un órgano sin sesión convocada

*comite-de-presidencia, de la sesión del 2026-10-05*

**Decisión D-1: Proveedor de la mesa de ayuda** — plazo 2026-11-03 (`organos/comite-de-presidencia/2026-10-05/20-material/propuesta-1.md, línea 3: «La decisión vence el 2026-11-03»`)

- Renovar con el proveedor actual por tres años, a 18.000 al mes — evidencia: `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-1.md`
- Contratar al proveedor que ganó la cotización, a 15.500 al mes — evidencia: `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-1.md`

*comite-de-presidencia, de la sesión del 2026-10-05*

**Decisión D-2: Sede de la oficina regional** — plazo 2026-11-04 (`organos/comite-de-presidencia/2026-10-05/20-material/propuesta-2.md, línea 3: «La decisión vence el 2026-11-04»`)

- Mantener la sede actual, con un canon de 42.000 al mes — evidencia: `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-2.md`
- Trasladarse a la sede nueva del centro, con un canon de 47.500 al mes — evidencia: `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-2.md`

Las opciones van en el orden en que las traen los documentos. Ofelia no las ordena ni dice cuál conviene: la decisión es del órgano.

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-1.md, línea 3: «La decisión vence el 2026-11-03»`
- `organos/comite-de-presidencia/2026-10-05/20-material/propuesta-2.md, línea 3: «La decisión vence el 2026-11-04»`
- `organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md, línea 3: «La oferta del proveedor actual vence el 2026-11-02»`
- `organos/junta-directiva/2026-10-29/20-material/`

---

La corrida quedó registrada como `2026-10-26-ea-prep-1`. Lo que se muestra arriba está guardado tal cual en `<espacio>/estado-direccion/presidencia/corridas/salida-ea-prep.md`.