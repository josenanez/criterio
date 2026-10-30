# Criterio · catálogo 1.7.0 · 30 de octubre de 2026

La CFO y la CLO suman **Argentina, Panamá, Guatemala y Costa Rica**: la CFO pasa a la 1.1.0 y la CLO a la 1.2.0, las dos estables. Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** La versión de cada familia es la suya.

## Qué trae

| País | CFO · la factura electrónica | CLO · la contratación pública |
|---|---|---|
| **Argentina** | El comprobante de ARCA con su CAE (F-24) | La garantía de cumplimiento del 10 %, integrada dentro de los cinco días hábiles (Decreto 1030/2016, arts. 77 y 78) |
| **Panamá** | La factura electrónica de la DGI con su CUFE (F-27) | La fianza de cumplimiento, exigida en los actos de más de B/.50 000 (Ley 22, art. 123) |
| **Guatemala** | La FEL de la SAT con su número de autorización (F-30) | La identificación de cada contraparte. **Sin entidad pública**: la Ley 57-92 deja el porcentaje de la garantía a su reglamento, que no está entre las fuentes verificadas |
| **Costa Rica** | El comprobante 4.4 de Hacienda con su clave de cincuenta posiciones (F-34), el IVA del 13 % (F-35) y el perfil NIIF (F-36) | La garantía de cumplimiento entre el 5 % y el 10 % del monto adjudicado (Ley 9986, art. 44) |

Cada país trae tres entidades de prueba, una de ellas de control, sin defectos sembrados. Argentina, Panamá y Costa Rica traen además una entidad pública en la CLO.

## Cómo se probó

Una ronda por país con los agentes, sobre todas las entidades del material:

| Ronda | País | CFO · señales | CFO · datos | CLO · señales | CLO · datos |
|---|---|---|---|---|---|
| 8 | Argentina | 24 de 24 | 25 de 25 | 25 de 25 | 548 de 548 |
| 9 | Panamá | 27 de 27 | 24 de 24 | 24 de 24 | 569 de 569 |
| 10 | Guatemala | 24 de 24 | 25 de 25 | 20 de 20 | 396 de 396 |
| 11 | Costa Rica | 25 de 25 | 25 de 25 | 23 de 23 | 569 de 569 |

Ninguna señal de más y ningún defecto en las cuatro. El material es sintético y lo escribe el repositorio. Las cuatro rondas no reemplazan el primer uso sobre los documentos de una organización real.

## Las versiones en la 1.7.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | 1.0.0 | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | **1.1.0** | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | **1.2.0** | Estable | Sin lanzar |
| EA · Ofelia | 1.0.0 | Estable | Semana del 26 de octubre |
| CCO · Augusto y Valeria | 0.3.0 | Estable | Sin lanzar |
| CISO · Alexis, Guillermo y Amparo | 0.1.0 | De laboratorio | Sin lanzar |
| Rostrum | 1.0.0 | — | — |

En esta entrada se liberan la CFO y la CLO.

## Lo que sigue

Honduras, en la CFO 1.2.0 y la CLO 1.3.0. Honduras no publica un esquema de factura electrónica, así que la factura entra como documento: el agente extrae su CAI, su rango autorizado y su fecha límite de emisión, y el motor los valida (decisión 0024).

## Para actualizar

```
/plugin marketplace update criterio
```

Cada agente pide aceptar los términos de su versión y deja su comprobante en `.criterio/terminos/`.
