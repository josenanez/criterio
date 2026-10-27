---
name: minutes-draft
description: "Cómo se escribe el borrador del acta de una sesión desde las notas o la transcripción: cada acuerdo y compromiso citado, lo que no tiene responsable o fecha marcado, «BORRADOR» en el nombre y en el texto, y nunca en 40-acta. Úsalo cuando una sesión tiene notas y no tiene acta. Draft minutes from notes or transcripts."
---

# El borrador del acta

**Es un borrador, y se ve.** Va en `90-borradores/BORRADOR-acta-<órgano>-<AAAA-MM-DD>.md`, y su primera línea es `BORRADOR — no es el acta`. El acta es la que redacta y firma quien corresponde; el borrador es su material. **Nunca va a `40-acta/`.**

## La forma

```
BORRADOR — no es el acta

# <Órgano> · sesión del <AAAA-MM-DD>

Asistentes, según las notas: …
Orden del día, según la convocatoria: …

## Acuerdos
- A-1 · <lo que se resolvió> — responsable: <quien> · fecha: <AAAA-MM-DD> · (notas, línea 34)
- A-2 · <lo que se resolvió> — **sin responsable en las notas** · fecha: … · (notas, línea 51)

## Compromisos
- C-1 · <quien> se compromete a <qué> para el <fecha> · (transcripción, 00:42:10)

## Lo que falta para cerrarlo
- A-2 no tiene responsable.
```

## Las reglas

1. **Cada acuerdo y cada compromiso, con su cita** a la línea de las notas o al minuto de la transcripción.
2. **Lo que las notas no dicen queda marcado**, no completado: un acuerdo sin responsable o sin fecha se escribe así, y va a «Lo que falta para cerrarlo».
3. **No resumas el debate ni atribuyas opiniones.** El borrador recoge lo que se resolvió y lo que se prometió.
4. **Un compromiso que ya existía** se nombra con su id de la sesión donde nació; no se crea otro.
