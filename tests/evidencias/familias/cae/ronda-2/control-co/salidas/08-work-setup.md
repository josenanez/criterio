# /criterio-audit-work:work-setup auditoria/901888432-banco-control-sintetico

Soy Justo. Pongo cada hallazgo al lado de su criterio y de su papel, y cada informe al lado de sus papeles; no cambio prioridades ni firmo informes.

**Carpeta:** solo encontré una, `auditoria/901888432-banco-control-sintetico` (tiene 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/). La tomé como respuesta sugerida.

**Respuestas:** las tomé de la configuración que Prudencia ya dejó y de la metodología. No hice ninguna pregunta nueva.
- **Entidad:** Banco Control Sintético, NIT 901888432, Colombia (COP). **Periodo:** 2026-11.
- **Escala de prioridad:** alta desde 15, media desde 8 y baja desde 1, por impacto × probabilidad, cada uno de 1 a 5. Sale de `00-referencia/metodologia-de-auditoria.pdf`, «Escala de prioridad de los hallazgos».
- **Quién aprueba el programa:** los dos documentos de aprobación dicen «la jefa de auditoría». La configuración no tiene un campo para este dato, así que no quedó en ella.
- **Rostrum:** no. **Estado:** `estado-auditoria/901888432-banco-control-sintetico`.
- **Marca `_CRITERIO_AUDITORIA.txt`:** no la dejé, porque el setup de Prudencia tampoco la dejó.
- **Términos (versión 1.6):** mostré el texto en corto tal cual y quedaron aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-audit-work-0.2.2-2026-11-24.md` y `.pdf`.

**Configuración:** `.criterio/trabajos/901888432/config.json`. Es la ruta de la entidad, pero la carpeta lleva solo el NIT, sin el nombre.

Procesé los 15 documentos de `20-trabajos/`: son dos trabajos (TR-01 y TR-02) con tres hallazgos (H-01, H-02 y H-03), y los llevé a la ficha de 2026-11. A H-02 no se le identificó la causa; el papel da la razón (la gerencia no entregó el registro de avalúos a tiempo). H-03 no trae cifras ni en el papel ni en el informe.

# Cada hallazgo y sus elementos · Banco Control Sintético · periodo 2026-11

**Entidad:** Banco Control Sintético (901888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.2.2 · **Comando:** `finding-check`

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

**Reloj:** no creé la tarea programada, porque en esta sesión sin interfaz nadie pudo dar el sí explícito. Para correrlo a mano: `/criterio-audit-work:work-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-24-work-setup-1`, y lo que se mostró está en `estado-auditoria/901888432-banco-control-sintetico/corridas/salida-work-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.