# /criterio-audit-work:work-setup auditoria/20602888432-cooperativa-control-sintetica

Justo quedó configurado para la Cooperativa Control Sintética (RUC 20602888432, Perú). La primera revisión de hallazgos no encontró nada que atender.

**Lo que se configuró**, con las respuestas que sugerían los documentos:
- **Periodo:** 2026-11.
- **Escala de prioridad**, de la metodología: impacto por probabilidad, alta desde 15, media desde 8, baja desde 1.
- **Quién aprueba:** el estatuto dice que el comité de auditoría aprueba el plan y sus cambios. La configuración no tiene un campo para quién aprueba el programa y los papeles, así que para eso valen los documentos de aprobación de cada trabajo.
- **Rostrum:** no se publica nada.
- **Dónde quedan los resultados:** `estado-auditoria/20602888432-cooperativa-control-sintetica`.
- **Configuración:** `.criterio/trabajos/20602888432/config.json`.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-work-0.1.0-2026-11-24.md` y en `.pdf`.
- **Marca:** la carpeta tiene su `_CRITERIO_AUDITORIA.txt`.

**Lo que se procesó:** convertí los 15 documentos de `20-trabajos/` y llevé a la ficha 2 trabajos con 3 hallazgos. También encontré dos archivos que no están donde van: `informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/` y `riesgos_aceptados.xlsx` en `10-plan/`. Siguen en `30-seguimiento/`; no los moví.

# Cada hallazgo y sus elementos · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (20602888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `finding-check`

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

**Revisión diaria automática:** no la programé, porque necesita un sí explícito y en esta sesión no había nadie para darlo. Para correrla a mano: `/criterio-audit-work:work-wake`.

**Cuándo vuelvo:** no hay revisión programada.

La corrida quedó registrada como `2026-11-24-work-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.