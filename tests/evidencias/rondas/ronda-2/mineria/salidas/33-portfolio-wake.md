# /criterio-portfolio:portfolio-wake 

## 2026-10-15

**Revisé:** 74 documentos. Ninguno cambió, así que no recalculé ningún proyecto. No había peticiones en el servidor.

### Lo que cruzó un umbral
Nada. El barrido corrió y no había noticia nueva.

### Preguntas (confirmación mensual, 5 de 13 proyectos)
Es la primera confirmación, porque no hay una corrida anterior. En los cinco proyectos, ningún documento nombra a la autoridad de aprobación, el campo `authority` de la ficha. Elegí los tres en rojo y los dos con el dato más viejo:

1. **PRY-200** (rojo, informe del 11-oct): ¿quién es la autoridad de aprobación?
2. **PRY-202** (rojo, informe del 13-oct): ¿quién es la autoridad de aprobación?
3. **PRY-209** (rojo, informe del 8-oct): ¿quién es la autoridad de aprobación?
4. **PRY-206** (amarillo, informe del 25-sep, el más viejo): ¿quién es la autoridad de aprobación?
5. **PRY-207** (verde, informe del 6-oct): ¿quién es la autoridad de aprobación?

Nadie respondió, porque la sesión era sin interfaz. Las preguntas quedan abiertas y no escribí nada en las fichas.

**Cómo corrió:**
- **Términos:** ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15 (versión 0.3.8). No hizo falta registrarlos de nuevo.
- **Comando en un solo paso:** hice un `cd` en un comando para listar las fichas, aunque las instrucciones lo desaconsejan.
- **Registro de la corrida:** registré el barrido y la confirmación como hechos, y dejé la corrida guardada. Tardó 29 segundos y quedó con 44 hallazgos abiertos de corridas anteriores en las 13 fichas.
- **Documentos no medidos:** el registro no pudo medir el número de documentos leídos, y quedó como `null`.
- **Salida guardada:** `estado/corridas/salida-portfolio-wake.md`.

**Vuelvo el 2026-10-16.**

Para que esto corra solo, hace falta un programador (Cowork, o cron en Claude Code en modo no interactivo) con la sesión autorizada a no pedir aprobación en cada paso. También hace falta que `documentos/proyectos` esté montada cuando dispare. Si la organización no quiere corridas desatendidas, el comando también sirve a mano.