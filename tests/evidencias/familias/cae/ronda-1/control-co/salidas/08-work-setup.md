# /criterio-audit-work:work-setup auditoria/901888432-banco-control-sintetico

Justo quedó instalado para Banco Control Sintético. La configuración está en `.criterio/trabajos/901888432/config.json`, y el comprobante de los términos en `.criterio/terminos/aceptacion-criterio-audit-work-0.1.0-2026-11-24.md` y `.pdf`.

Los tres hallazgos de TR-01 y TR-02 tienen la prioridad que da la metodología. H-02 no tiene causa, pero el papel dice por qué no se identificó. Hay dos archivos fuera de lugar que no moví: `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/`, y `30-seguimiento/riesgos_aceptados.xlsx` iría en `10-plan/`.

# Cada hallazgo y sus elementos · Banco Control Sintético · periodo 2026-11

**Entidad:** Banco Control Sintético (901888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `finding-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Escala de la metodología:** alta desde 15, media desde 8, baja desde 1 (impacto por probabilidad).

| Trabajo | Hallazgo | Prioridad | La de la metodología | Le falta | Papeles |
|---|---|---|---|---|---|
| TR-01 | H-01 | Alta | alta | — | PT-03 |
| TR-01 | H-02 | Media | media | — | PT-02 |
| TR-02 | H-03 | Media | media | — | PT-02 |

La prioridad la pone el auditor: aquí se dice cuándo no es la que da la metodología.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

**El reloj:** propuse una tarea programada para los días hábiles a las 7:00. En esta sesión de prueba nadie dio un sí explícito, así que no la creé. Para correrlo a mano: `/criterio-audit-work:work-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-24-work-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.