# /criterio-product:product-wake 

## Crédito de libre inversión (PRD-309) · 2026-10-15

Los términos ya estaban vigentes (José Francisco Ñáñez, 2026-10-15, versión 0.3.10).

**Es la primera revisión y no había corte anterior.** Por eso no puedo decir qué cruzó un umbral desde un corte. Lo que sigue es la línea de base, y desde la próxima corrida solo se reportará lo nuevo.

**Necesita decisión (umbral de 60 días):**
- Cuatro requerimientos propuestos llevan entre 137 y 168 días sin decidirse: REQ-4903 (168), REQ-4913 (155), REQ-4908 (143) y REQ-4901 (137).
- REQ-4913 además no tiene doliente.
- Ningún documento dice quién tiene la facultad de decidirlos. La configuración propone el Comité de producto, y eso queda por confirmar.

**Aceptado y nadie lo construye:**
- Los 11 requerimientos aceptados no tienen proyecto asignado. El más viejo, REQ-4911, lleva 212 días.
- Cuatro están aceptados sin evidencia de quién los pidió: REQ-4900, REQ-4902, REQ-4905 y REQ-4907.
- REQ-4900 y REQ-4905 tampoco tienen doliente.
- Ocho carecen de criterio de aceptación.

**Lo declarado frente a lo medido:**
- El caso de negocio declara un volumen mensual de 117.145. El tablero del 2026-10-11 mide 85.140, un 27,3 % menos, por encima del umbral de 20 %.
- El supuesto «el canal actual soporta el volumen» figura como verificado, pero no hay documento de verificación.

**Trazas:**
- Ninguna se confirma. Solo hay una ficha de proyecto a la vista (PRY-210) y no dice ejecutar PRD-309. Sobre los otros 12 proyectos no sé nada.

**Nota técnica:** `plan-lectura` marca como no encontradas las fuentes de 7 campos de `producto.json`, aunque los archivos existen. Parece un problema de rutas relativas.

La revisión, el corte (`snapshots/2026-10-15.json`) y la corrida quedaron registrados.

**Vuelvo el 2026-11-14.**