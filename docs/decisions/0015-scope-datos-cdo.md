# 0015 · Propuesta: el alcance se amplía a datos (CDO)

**Fecha:** 2026-10-23 · **Estado:** propuesta · **Modifica:** 0012

## Contexto

Datos es la cuarta capacidad «Siguiente» del mapa, y va al final del orden porque es terreno
nuevo: casi nada de lo construido se reutiliza tal cual.

El rol se define desde **DAMA-DMBOK2**, el cuerpo de conocimiento de gestión de datos. Tiene once
áreas, con el gobierno de datos al centro. Para un agente que contrasta documentos, tres de ellas
cumplen las condiciones de las 0006 y 0009:

- **El gobierno de datos:** quién decide sobre cada dato y si las políticas se cumplen.
- **La calidad de datos:** si un dato sirve para el uso que se le da.
- **Los metadatos y el linaje:** de dónde sale cada cifra.

Las demás áreas —arquitectura, modelado, almacenamiento, integración— son trabajo sobre sistemas,
no sobre documentos, y quedan fuera.

## Decisión propuesta

**Una familia con un agente que contrasta la cifra publicada contra su fuente y su linaje, y la
política de datos contra su cumplimiento.**

| Lo que calcula el código | Cuándo se levanta |
|---|---|
| Cifra sin fuente | Una cifra de un informe de dirección no tiene fuente en el catálogo o el linaje exportado |
| Cifra distinta de su fuente | La cifra del informe no coincide con la de su fuente, para el mismo corte |
| Dato sin dueño | Un conjunto de datos del catálogo no tiene responsable |
| Regla de calidad incumplida | El resultado exportado de una regla de calidad está bajo su umbral |
| Revisión de política vencida | Una política de datos o de retención pasó su revisión |
| Base de datos personales sin registro | Un conjunto con datos personales no aparece en el registro que exige la ley del país (por verificar en cada país) |

**Nunca:**

- se conecta a una base de datos;
- modifica un dato;
- asigna dueños;
- decide la clasificación de un dato.

## Reglas para la operación real

- **Procesa exportaciones**: del catálogo, del linaje, de los resultados de calidad y de los
  informes. Nunca se conecta a las bases.
- **No procesa los datos personales en sí, solo sus metadatos.** La configuración excluye por
  omisión las extracciones con registros de personas.
- **La ley de datos personales de cada país se verifica antes de citarse**: en Colombia, la Ley
  1581 de 2012; en Ecuador, la ley orgánica de 2021. Las dos están por verificar.

## Lo que falta decidir

1. El nombre del agente.
2. Qué formatos de exportación del catálogo y del linaje soporta primero.
3. Si la familia CFO entra como primera fuente de cifras a trazar: el informe al supervisor contra
   su contabilidad.
