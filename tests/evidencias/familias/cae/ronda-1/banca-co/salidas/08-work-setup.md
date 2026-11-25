# /criterio-audit-work:work-setup auditoria/901777321-banco-andino-sintetico

Justo quedó instalado sobre el Banco Andino Sintético y aceptó los términos. La primera ficha sale vacía porque los papeles de trabajo no traen ningún hallazgo.

- **Carpeta:** `auditoria/901777321-banco-andino-sintetico`. Era la única candidata y ya tenía la marca `_CRITERIO_AUDITORIA.txt`, así que no la volví a marcar.
- **Respuestas que tomé de los documentos:**
  - **Entidad:** NIT 901777321, Colombia (COP).
  - **Periodo:** 2026-11.
  - **Escala de prioridad:** Alta desde 15, Media desde 8, Baja desde 1, según la metodología.
  - **Aprobaciones:** el programa y los papeles los aprueba la jefa de auditoría; el plan y sus cambios, el comité de auditoría.
  - **Rostrum:** no se publica.
  - **Estado:** `estado-auditoria/901777321-banco-andino-sintetico`.
- **Términos v1.6:** aceptados por José Francisco Ñáñez. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-work-0.1.0-2026-11-24.md` y `.pdf`.
- **Configuración:** `.criterio/trabajos/901777321/config.json`.
- **Fuera de lugar:** la carpeta tiene dos archivos en otra subcarpeta. `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/` y `30-seguimiento/riesgos_aceptados.xlsx` iría en `10-plan/`. No moví nada.

Procesé los documentos de `20-trabajos/`. Los papeles PT-01 a PT-03 de TR-01 y TR-02 solo traen su encabezado, así que ningún hallazgo aparece con su criterio, su condición, su causa o su efecto. Los informes nombran H-01 y H-02 (TR-01) y H-03 (TR-02), todos con prioridad Media, sin un papel que los sostenga. El motor encontró otras señales que este reporte no muestra: las del informe salen con `/criterio-audit-work:report-check`, las de los pasos y las revisiones con `/criterio-audit-work:workpaper-check`, y la del auditor que revisa su propio trabajo con `/criterio-audit-work:objectivity-check`.

# Cada hallazgo y sus elementos · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `finding-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Escala de la metodología:** alta desde 15, media desde 8, baja desde 1 (impacto por probabilidad).

| Trabajo | Hallazgo | Prioridad | La de la metodología | Le falta | Papeles |
|---|---|---|---|---|---|

La prioridad la pone el auditor: aquí se dice cuándo no es la que da la metodología.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

**Reloj:** no creé la tarea programada porque en esta prueba nadie dio un sí explícito. Para correrlo a mano: `/criterio-audit-work:work-wake`.
**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-24-work-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.