# Criterio CFO · versión 0.10.0 · 26 de octubre de 2026

La función financiera de Criterio: tres agentes que procesan lo que el área financiera ya produce —la contabilidad, los extractos, la factura electrónica, el presupuesto, la política de tesorería y las actas— y lo contrastan contra la evidencia para decir qué está cumplido, qué no tiene soporte y qué se desvía. NIIF adoptadas en Colombia, Ecuador y Perú. Código abierto bajo Apache 2.0.

## Qué trae

| | Para quién | Comandos | Qué hace |
|---|---|---:|---|
| **Clara** · `criterio-finance` | La contraloría | 9 | El cierre mensual con su checklist y su evidencia, las conciliaciones bancarias y de cuentas, la factura electrónica de la DIAN, del SRI y de la SUNAT contra la contabilidad, y el paquete para el auditor |
| **Tomás** · `criterio-budget` | Planeación financiera (FP&A) | 7 | El presupuesto aprobado contra lo ejecutado y lo comprometido, la proyección al cierre del año, los traslados y el material del comité de presupuesto |
| **Áurea** · `criterio-treasury` | La tesorería | 6 | La caja contra su mínimo y su proyección, cada pago contra quién puede aprobarlo, la exposición cambiaria, y la deuda contra su vencimiento y sus covenants |

El modelo de lenguaje (LLM) extrae de los documentos escritos; el código calcula las 30 señales; la decisión la toma siempre una persona. Ninguno de los tres registra asientos, firma, aprueba traslados, mueve dinero ni declara el estado del cierre.

**Nuevo en la 0.10.0:** Áurea; Perú, con la factura electrónica de la SUNAT procesada desde su guía oficial; y el material en los formatos de un área financiera real —Excel, Word y PDF—, incluido el extracto bancario en PDF, que el motor procesa directamente.

## Lo que está medido

Datos de prueba de cuatro industrias en tres países —banca y retail en Colombia, cooperativas y minería en Ecuador, banca y minería en Perú— y una entidad de control por país, sin ningún defecto sembrado: cualquier señal en ella es una falla. Una clave que ningún agente ve.

**Ronda 3, con los tres agentes**, sobre banca de Colombia y banca, minería y el control de Perú. Cada agente corrió su instalación y su escaneo, que es donde levanta sus señales y extrae lo que traen los escritos:

| | Resultado | Margen del 95 % |
|---|---|---|
| Señales sembradas encontradas | 40 de 40 | 91,2–100 % |
| Señales de más | 0 | — |
| Datos extraídos correctos | 33 de 33 | 89,5–100 % |
| Entidad de control sin ninguna señal | 1 de 1 | — |

La primera pasada dio 38 de 40 y 32 de 33. Las dos fallas venían de la prueba y de las instrucciones, no del cálculo: la moneda de la cuenta en dólares solo estaba en la clave (CFO-5), y Tomás no llevó a la ficha un correo de un área (CFO-6). Al repetir apareció un tercer defecto: Tomás fijó por su cuenta la versión del presupuesto (CFO-7). Los tres están corregidos, y las corridas repetidas dieron lo esperado. La ronda usó 21,6 millones de tokens, con las repeticiones.

**Ronda 2, con Clara y Tomás**, completa sobre las seis entidades de Colombia y Ecuador: 45 de 45 señales (92,1–100 %), ninguna de más, 48 de 49 datos y los 2 controles sin ninguna señal.

Los siete defectos registrados tienen su origen, el commit que los corrige y la ronda que los verificó, en [`tests/evidencias/familias/cfo/`](../tests/evidencias/familias/cfo/RONDAS.md). El análisis estadístico completo está en [`families/criterio-cfo/analisis/`](../families/criterio-cfo/analisis/ANALISIS.es.md).

## Lo que cuesta hoy

Cifras de terceros, verificadas contra el texto de quien las publica, en [`FUENTES.es.md`](../families/criterio-cfo/FUENTES.es.md):

- **18 %** de las personas de la función de contraloría comete errores al menos a diario, y 59 % varios al mes, por restricciones de capacidad. Gartner, 2024; 497 personas.
- **45 %** de los controles SOX son manuales, y las horas del programa subieron 32 % en dos años. KPMG, SOX Survey 2025; cerca de 150 profesionales.
- **18 días** es la mediana del cierre anual; los más lentos tardan 35. APQC, 2026; 2.214 organizaciones.
- **79 %** de las organizaciones sufrió en 2024 un intento de fraude en pagos o un fraude consumado. Association for Financial Professionals, 2025; 521 profesionales de finanzas corporativas.

## Lo que sigue

- **La ronda de los tres agentes sobre el resto del material:** cooperativas y minería de Ecuador, retail de Colombia y los controles de Colombia y Ecuador, en los formatos nuevos.
- **Más países, por tamaño de mercado:** Chile, México y Brasil, cada uno con su lector de factura electrónica y sus fuentes verificadas. Un país se anuncia cuando pasa su ronda.
- **El primer uso sobre la documentación de una organización concreta**, que es el paso que lleva la familia a la versión 1.0. Antes del primero en Perú se contrasta el lector con las reglas de validación vigentes de la SUNAT.

## Antes de usarla

Cada versión se acepta de nuevo: el agente muestra los términos, pide un sí explícito y deja un comprobante con la huella SHA-256 de los términos. Produce borradores de trabajo, no decisiones.

Instalación: `/plugin marketplace add josenanez/criterio`, y después `criterio-finance` para Clara, `criterio-budget` para Tomás y `criterio-treasury` para Áurea. En Claude Cowork: Personalizar → Explorar plugins → Personal → + → `josenanez/criterio`.
