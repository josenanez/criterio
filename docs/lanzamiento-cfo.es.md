# Criterio CFO · versión 0.9.0 · 27 de octubre de 2026

La familia de cierre, control y reporte de Criterio: dos agentes que procesan lo que el área financiera ya produce —la contabilidad, los extractos, la factura electrónica, el presupuesto y las actas— y lo contrastan contra la evidencia para decir qué está cumplido, qué no tiene soporte y qué se desvía. Primera versión para las NIIF adoptadas en Colombia y Ecuador. Código abierto bajo Apache 2.0.

## Qué trae

| | Para quién | Comandos | Qué hace |
|---|---|---:|---|
| **Clara** · `criterio-finance` | La contraloría | 9 | El cierre mensual con su checklist y su evidencia, las conciliaciones bancarias y de cuentas, la factura electrónica de la DIAN y del SRI contra la contabilidad, y el paquete para el auditor |
| **Tomás** · `criterio-budget` | Planeación financiera (FP&A) | 7 | El presupuesto aprobado contra lo ejecutado y lo comprometido, la proyección al cierre del año, los traslados y el material del comité de presupuesto |

El modelo de lenguaje (LLM) extrae de los documentos escritos; el código calcula las 23 señales; la decisión la toma siempre una persona. Ninguno de los dos registra asientos, firma, aprueba traslados ni declara el estado del cierre.

## Lo que está medido

Dos rondas, sobre datos de prueba de cuatro industrias —banca y retail en Colombia, cooperativas y minería en Ecuador— y una entidad de control por país, sin ningún defecto sembrado: cualquier señal en ella es una falla. 340 documentos en CSV, XML de factura electrónica y Markdown, más las fichas de proyectos de la PMO, con una clave que ningún agente ve.

Ronda 2, completa, sobre las seis entidades:

| | Resultado | Margen del 95 % |
|---|---|---|
| Señales sembradas encontradas | 45 de 45 | 92,1–100 % |
| Señales de más | 0 | — |
| Datos extraídos correctos | 48 de 49 (98 %) | 89,3–99,7 % |
| Entidades de control sin ninguna señal | 2 de 2 | — |

El dato que faltó fue de la calificación, no del agente: en minería, Tomás escribió el compromiso del comité con más palabras que la clave. Está corregido y verificado (CFO-4). Los cuatro defectos registrados tienen su origen, el commit que los corrige y la ronda que los verificó, en [`tests/evidencias/familias/cfo/`](../tests/evidencias/familias/cfo/RONDAS.md). El análisis estadístico completo está en [`families/criterio-cfo/analisis/`](../families/criterio-cfo/analisis/ANALISIS.es.md).

## Lo que cuesta hoy

Cifras de terceros, verificadas contra el texto de quien las publica, en [`FUENTES.es.md`](../families/criterio-cfo/FUENTES.es.md):

- **18 %** de las personas de la función de contraloría comete errores al menos a diario, y 59 % varios al mes, por restricciones de capacidad. Gartner, 2024; 497 personas.
- **45 %** de los controles SOX son manuales, y las horas del programa subieron 32 % en dos años. KPMG, SOX Survey 2025; cerca de 150 profesionales.
- **18 días** es la mediana del cierre anual; los más lentos tardan 35. APQC, 2026; 2.214 organizaciones.

## Lo que sigue

- **Más países, por tamaño de mercado:** Perú, Chile, México y Brasil, cada uno con su lector de factura electrónica y sus fuentes verificadas. Un país se anuncia cuando pasa su ronda.
- **Áurea, la tesorería**, el tercer agente de la familia: la caja, los pagos y la deuda contra su política. Está construida y su motor da exactamente la clave del material; su ronda con el agente es el siguiente paso, y entra en una versión cuando la pase.
- **El primer uso sobre la documentación de una organización concreta**, que es el paso que lleva la familia a la versión 1.0.

## Antes de usarla

Cada versión se acepta de nuevo: el agente muestra los términos, pide un sí explícito y deja un comprobante con la huella SHA-256 de los términos. Produce borradores de trabajo, no decisiones.

Instalación: `/plugin marketplace add josenanez/criterio`, y después `criterio-finance` para Clara y `criterio-budget` para Tomás. En Claude Cowork: Personalizar → Explorar plugins → Personal → + → `josenanez/criterio`.
