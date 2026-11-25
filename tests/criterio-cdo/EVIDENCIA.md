# criterio-cdo · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada vez,
byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el generador al
sembrar cada defecto; el motor no la ve. Los nombres, las empresas y los documentos son inventados, y
ninguna entidad trae un dato personal: el catálogo dice qué conjunto los tiene, y nada más.

## Las entidades

| Carpeta del material | País | Industria | Señales esperadas |
|---|---|---|---:|
| `banca-co` | Colombia | banca | 14 |
| `seguros-pe` | Perú | seguros | 6 |
| `retail-mx` | México | retail | 8 |
| `control-co` | Colombia | banca | 0 |
| `control-mx` | México | retail | 0 |

Cada una trae su carpeta de datos al 25 de noviembre de 2026, con el periodo de noviembre: la política de
datos y la de conservación en PDF y el glosario de negocio en Excel; la exportación del catálogo y el
registro de bases de datos personales en Excel; el informe de junta de octubre en PDF, con sus cifras y su
corte; y el linaje, las cifras de la fuente por corte, las reglas de calidad, sus resultados de noviembre y
los datos críticos en Excel.

## Lo que se siembra, y la señal que tiene que levantar

La lista exacta está en la clave de cada entidad, en `esperado`. Las trece señales se siembran al menos una
vez.

| Agente | Lo que se siembra | Señal |
|---|---|---|
| Custodia | Un conjunto del catálogo sin dueño de negocio | `dataset_without_owner` |
| Custodia | Un conjunto sin clasificación de confidencialidad | `dataset_without_classification` |
| Custodia | La política de datos con su revisión del 30 de junio de 2025 | `policy_review_overdue` |
| Custodia | Datos de candidatos desde junio de 2023, con un plazo de 24 meses | `retention_exceeded` |
| Custodia | Un indicador del informe que el glosario no define | `term_not_in_glossary` |
| Custodia | Un conjunto con datos personales que no está en el registro de bases | `personal_data_unregistered` |
| Ariadna | Un indicador del informe sin linaje ni cifra en la fuente | `figure_without_source` |
| Ariadna | Ventas netas 1,3 % por encima de su fuente, con una tolerancia del 0,5 % | `figure_differs_from_source` |
| Ariadna | La cartera vencida de septiembre presentada con el corte de octubre | `cutoff_mismatch` |
| Ariadna | Un paso del linaje sin su sistema de origen | `lineage_broken` |
| Ariadna | Una regla de calidad con 96,1 cuando su umbral es 98 | `quality_rule_below_threshold` |
| Ariadna | Una regla sobre un dato crítico sin resultado en noviembre | `quality_rule_not_run` |
| Ariadna | Un dato crítico que ninguna regla mide | `critical_data_without_rule` |

## Lo que se parece a un defecto y no lo es

En las entidades de control: una política que se revisa el mes que viene, datos de candidatos justo dentro
de su plazo, un término del informe escrito con otras mayúsculas que el del glosario, ventas netas 0,21 %
por encima de su fuente —dentro de la tolerancia—, una regla que da exactamente su umbral y una regla sin
corrida sobre un dato que no es crítico. Ninguno puede levantar una señal.

## Lo que el material no prueba

- **La extracción.** El evaluador escribe la ficha con la extracción correcta, de la clave. Que la agente
  procese las políticas, los plazos, los términos y las cifras de los informes y los registre bien lo
  prueba la ronda con las agentes, en la 0.2.0.
- **Las exportaciones reales** de Collibra, Alation, Microsoft Purview o Informatica: el material usa tablas
  con columnas en español; el setup mapea las de cualquier exportación.
- **La ley de cada país** sobre el registro de bases de datos personales: está por verificar, país por país;
  el material compara el catálogo con el registro de la organización.
- **El juicio del área de datos**: quién debe ser el dueño de un conjunto, qué clasificación le corresponde y
  cuál de dos cifras es la correcta.
