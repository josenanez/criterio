# 0030 · Una aceptación mientras los términos no cambien

**Fecha:** 2026-11-09 · **Estado:** aceptada el 2026-11-09 · **Modifica:** la puerta de los términos de todos los agentes (`terminos.py`), los términos (versión 1.5) y el setup de cada agente

## Contexto

Desde los términos 1.1, cada versión de una familia pedía aceptar los términos de nuevo, aunque su
texto no hubiera cambiado. Con una familia que libera cada pocos días, eso obliga a quien la usa a
aceptar lo mismo una y otra vez, y lo empuja a quedarse en una versión vieja para no repetirlo. Lo
que importa es que las personas usen la última versión estable.

José Francisco Ñáñez decidió el 9 de noviembre de 2026 que actualizar no pida aceptar de nuevo, y
que eso quede explícito en los términos desde el inicio, contra la jurisdicción más exigente de los
países de Criterio.

## Lo que exigen los países de Criterio

Las leyes de consumo de varios de los doce países tienen por no escrita, o sin efecto, la cláusula
que deja al proveedor modificar el contrato por su cuenta después de celebrado:

- **Argentina:** el Código Civil y Comercial, art. 988, para todo contrato por adhesión, también
  entre empresas; y la Disposición 377/2026 (que reemplaza el anexo de la Resolución 53/2003),
  letra b), en los contratos de consumo.
- **Brasil:** el Código de Defesa do Consumidor, art. 51, XIII.
- **Chile:** la Ley 19.496, art. 16, letra a).
- **México:** la Ley Federal de Protección al Consumidor, art. 90, fracción I.
- **Colombia y Perú:** sus estatutos de consumo (Ley 1480, arts. 42 y 43, y el Código de Protección
  y Defensa del Consumidor, art. 50) castigan las cláusulas abusivas con ineficacia, y la autoridad
  peruana ha sancionado términos y condiciones en línea por esa vía.

La regla más exigente, entonces: **ningún cambio a los términos rige sin una aceptación expresa**.
Una actualización del software que no cambia los términos no modifica el contrato y no la necesita.
No es una opinión legal: conviene que la revise un abogado de cada país antes de lanzar en él.

## Decisión

1. **La aceptación rige mientras el texto de los términos sea el mismo.** La puerta compara la huella
   SHA-256 del texto aceptado con la del instalado; ya no compara la versión de la familia.
   Actualizar a una versión con los mismos términos no pide nada.
2. **Un cambio a los términos se acepta de nuevo, siempre.** Cambia la huella, la puerta se cierra y
   el agente muestra el texto nuevo y pide un sí expreso antes de producir análisis o informes. Si
   la persona no lo acepta, puede seguir con la versión que ya aceptó.
3. **Los términos lo dicen desde el inicio** (versión 1.5, secciones 8 y 9 y «En corto»), y
   recomiendan usar siempre la última versión estable.
4. **Los comprobantes, la bitácora encadenada y el registro de versiones no cambian.**

## Consecuencias

- La tarea programada de cada agente (decisión 0028) solo se detiene cuando cambian los términos.
- Una liberación que cambia los términos sigue subiendo todas las familias; las demás ya no le piden
  nada a quien actualiza.
