# /criterio-talent:talent-setup talento/900777888-cooperativa-control-sintetica

Cándido quedó configurado para la Cooperativa Control Sintética (NIT 900777888), los términos quedaron aceptados y la primera ficha y el reporte de vacantes ya están hechos.

- **Configuración:** `.criterio/seleccion/900777888/config.json`. Las respuestas salen del setup de Norma y de la política de selección:
  - 45 días para cubrir una vacante y 180 días para conservar los datos de un candidato, tomados de `00-referencia/politica-de-seleccion.pdf`.
  - Usa el estándar CUOC y el periodo 2026-11.
  - Los reportes de candidatos no se publican en Rostrum.
- **Términos:** aceptados por José Francisco Ñáñez el 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-talent-0.1.0-2026-11-16.md` y `.pdf`.
- **Marca de la carpeta:** ya tenía `_CRITERIO_TALENTO.txt`, así que no la marqué otra vez.
- **Ficha del periodo:** procesé las hojas de vida y sus soportes de `30-candidatos/`.
  - El diploma escaneado de CAN-406 (`diploma.jpg`) lo abrí solo para confirmar que es el diploma, y quedó como soporte.
  - En una hoja de vida llegó un dato que no se trata. La ficha registra solo su tipo y dónde está, y el motor lo deja fuera del análisis; el detalle sale con `/criterio-talent:privacy-check`.

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

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

---

**Reloj:** no creé la tarea programada porque nadie dio un sí. Para revisar a mano lo que toca cada día: `/criterio-talent:talent-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-16-talent-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.