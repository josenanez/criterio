# criterio-cmo · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada vez,
byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el generador al
sembrar cada defecto; el motor no la ve. Los nombres, las empresas y los documentos son inventados, y
ninguna entidad trae los datos de una persona: el registro de bases dice cuántos registros tiene cada una
y con qué autorización, y nada más.

## Las entidades

| Carpeta del material | País | Industria | Señales esperadas |
|---|---|---|---:|
| `retail-co` | Colombia | retail | 33 |
| `banca-pe` | Perú | banca | 33 |
| `consumo-mx` | México | manufactura de consumo masivo | 22 |
| `control-co` | Colombia | retail | 0 |
| `control-mx` | México | manufactura de consumo masivo | 0 |

Cada una trae su carpeta de mercadeo al 25 de noviembre de 2026, con octubre como el periodo que se evalúa:
la política de publicidad en PDF; el registro de piezas en Excel y seis piezas aprobadas con su texto en PDF;
los soportes de las afirmaciones en PDF y en Excel; las bases de dos promociones en PDF; el registro de bases
de contactos en Excel; y el plan de mercadeo, las facturas de pauta y la exportación de la plataforma en
Excel, con el informe de resultados de octubre en PDF.

## Lo que se siembra, y la señal que tiene que levantar

La lista exacta está en la clave de cada entidad, en `esperado`. Las tres entidades sembradas traen las once
señales: el retail y el banco, cada una tres veces, y la de consumo masivo, dos. Cada repetición va en su
propia pieza, promoción, base, campaña o factura, y la tabla dice la primera.

| Agente | Lo que se siembra | Señal |
|---|---|---|
| Lucía | «9 de cada 10 clientes nos recomiendan», sin la encuesta en la carpeta de soportes | `claim_without_substantiation` |
| Lucía | «El precio más bajo del mercado», sin la fuente ni la fecha en la pieza | `comparative_claim_without_source` |
| Lucía | La promoción de puntos dobles, con su inicio y sin su fin | `promotion_terms_missing` |
| Lucía | La reseña pagada a una creadora, sin identificarse como publicidad | `sponsored_content_unidentified` |
| Lucía | Una pieza publicada el 12 de octubre y aprobada el 15 | `piece_published_unapproved` |
| Lucía | Una campaña que usa una base sin autorización para mercadeo | `contact_base_without_consent` |
| Próspero | La campaña de fin de año con 108 millones facturados sobre 100 de presupuesto, con una tolerancia del 5 % | `campaign_over_budget` |
| Próspero | Una factura de radio sin campaña ni orden de compra | `media_invoice_unmatched` |
| Próspero | Una campaña sin meta ni indicador | `campaign_without_goal` |
| Próspero | 4.600 ventas en el informe y 4.100 en la plataforma al mismo corte, con una tolerancia del 2 % | `result_differs_from_platform` |
| Próspero | Pauta de exteriores facturada hasta el 31 de octubre en una campaña que terminaba el 15 | `campaign_ran_past_end` |

Las repeticiones: «atención en menos de 5 minutos» y «más de 500 puntos de atención» sin soporte; «más barato
que cualquier otra cadena» y «el envío más rápido del mercado» sin fuente; las promociones de cumpleaños, sin
su fin, y de regreso a clases, sin el modo ni el lugar; dos piezas pagadas a un creador invitado sin
identificarse; dos piezas publicadas antes de aprobarse; dos bases sin autorización que usa una campaña; dos
campañas sin meta; dos que pasan su presupuesto; dos facturas sin campaña; las visitas y las impresiones del
informe por encima de la plataforma; y dos campañas con pauta facturada después de su fin.

## Lo que se parece a un defecto y no lo es

En las entidades de control: una pieza aprobada el mismo día en que se publicó, una pieza de un influenciador
que no se le pagó y no se identifica como publicidad, una base sin autorización que ninguna campaña usa, una
campaña que pasa su presupuesto dentro de la tolerancia, una factura con servicio el último día de su
campaña, un resultado que difiere de la plataforma dentro de la tolerancia y una comparativa que cita su
fuente y su fecha. Ninguno puede levantar una señal.

## Lo que el material no prueba

- **La extracción.** El evaluador escribe la ficha con la extracción correcta, de la clave. Que el agente
  procese las piezas, asocie cada afirmación con el soporte que trata de lo mismo, lea las bases de cada
  promoción y el informe de resultados, y los registre bien, lo prueba la ronda con los agentes, desde la 0.2.0: [las rondas](../evidencias/familias/cmo/RONDAS.md).
  Desde la ronda 2, cada afirmación, cada promoción y cada resultado se califican por separado, campo por campo.
- **Las exportaciones reales** de Google Ads, Meta o LinkedIn: el material usa tablas con columnas en
  español; el setup mapea las de cualquier exportación.
- **La ley de publicidad de cada país** fuera de Colombia: está por verificar, y no sostiene ninguna señal.
- **El juicio de legal y del área**: si un soporte basta, si una afirmación es verdadera y cuál de dos cifras
  es la correcta.
