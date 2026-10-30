# Criterio · catálogo 1.8.0 · 30 de octubre de 2026

Honduras entra a la CFO y a la CLO; la CISO tiene su primera ronda con los agentes; y cada agente
puede compartir sus hallazgos, siempre preguntando. Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** La versión de cada familia es la suya.

## Qué trae

| | |
|---|---|
| **Honduras en la CFO (1.2.0)** | Honduras no publica un esquema de factura electrónica, así que la factura entra como documento (decisión 0024): el agente extrae de cada PDF la CAI, el rango autorizado, la fecha límite de emisión y el número correlativo, y el motor los valida contra el Acuerdo 481-2017 (F-37) y el ISV del 15 % (F-38). Una señal nueva, `invoice_outside_authorization`: la factura recibida fuera de su rango autorizado o emitida después de su fecha límite no sustenta el crédito fiscal del ISV |
| **Honduras en la CLO (1.3.0)** | La garantía de cumplimiento del 15 % de la Ley de Contratación del Estado (Decreto 74-2001, art. 100), con los contratos que se publican en HonduCompras (F-14) |
| **La CISO, con su ronda (0.2.0)** | Alexis, Guillermo y Amparo sobre las seis entidades del material: 100 de 100 señales y ninguna de más. Sigue de laboratorio: los 48 datos extraídos dan un piso del 92,5 %, por debajo del 95 % |
| **Compartir hallazgos (decisión 0025)** | `/criterio-<plugin>:share-findings` en cada agente —`/criterio-finance:share-findings` para Clara—: un resumen sin datos de lo que corrió, armado por el código desde el rastro local; la pregunta siempre, y con un sí, el enlace a la plantilla de hallazgo, que abre la persona. Nada se envía |
| **Lo que corrigieron las rondas** | La conversión de documentos ya no copia una credencial que el motor excluye (CISO-4); las corridas de la CCO y de la CISO dejan su rastro para Rostrum (CISO-2); `cuentas` propone las cuentas de Honduras desde la ficha (CFO-12) |

## Cómo se probó

| Ronda | | Señales | Datos |
|---|---|---|---|
| CFO · 12 | Honduras: banca, retail y control | 27 de 27 | 625 de 625 |
| CLO · 12 | Honduras: banca, retail, control y una entidad pública | 22 de 22 | 569 de 569 |
| CISO · 1 | Banca, retail, salud, tecnología y dos controles | 100 de 100 | 48 de 48, con CISO-1 (el arnés) y CISO-3 (las instrucciones) corregidos y verificados |

Ninguna señal de más. El material es sintético y lo escribe el repositorio; las rondas no reemplazan el
primer uso sobre los documentos de una organización real.

## Las versiones en la 1.8.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | **1.0.1** | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | **1.2.0** | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | **1.3.0** | Estable | Sin lanzar |
| EA · Ofelia | **1.0.1** | Estable | Semana del 26 de octubre |
| CCO · Augusto y Valeria | **0.3.1** | Estable | Sin lanzar |
| CISO · Alexis, Guillermo y Amparo | **0.2.0** | De laboratorio | Sin lanzar |
| Rostrum | **1.0.1** | — | — |

Todas suben: `share-findings` llega a cada agente. La CFO y la CLO suman Honduras, y la CISO su ronda.

## Para actualizar

```
/plugin marketplace update criterio
```

Cada agente pide aceptar los términos de su versión y deja su comprobante en `.criterio/terminos/`.
