# Criterio · catálogo 2.0.0 · 5 de noviembre de 2026

Las seis familias quedan lanzadas: la CLO, la CCO y la CISO se suman a la PMO, la CFO y la EA. La CCO y
la CISO se lanzan estables, así que abren su 1.0.0 (decisión 0021). Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** La versión de cada familia es la suya.

## Qué trae

| | |
|---|---|
| **Criterio CLO (1.4.0), lanzada** | Fidel, los contratos, y Constanza, el cumplimiento, probados en 12 países, con la contratación pública donde su regla tiene fuente |
| **Criterio CCO (1.0.0), lanzada** | Augusto, el pronóstico, y Valeria, de la venta a la factura, con las exportaciones de Salesforce, HubSpot, Microsoft Dynamics y Zoho |
| **Criterio CISO (1.0.0), lanzada** | Alexis, el gobierno y los controles; Guillermo, las vulnerabilidades, con Tenable y Microsoft Defender; y Amparo, la respuesta y la recuperación |

## Cómo se probó

| Familia | Rondas | Señales | Datos extraídos |
|---|---|---|---|
| CLO | 2 a 13 | 262, con un piso del 98,5 % | 6 367, con un piso del 99,8 % |
| CCO | 1 y 2 | 197, con un piso del 98,0 % | 75, con un piso del 95,1 % |
| CISO | 1 y 2 | 148, con un piso del 97,4 % | 80, con un piso del 95,4 % |

El piso es el límite inferior del intervalo con 95 % de confianza. El material es sintético y lo
escribe el repositorio; las rondas no reemplazan el primer uso sobre los documentos de una
organización real.

## Las versiones en la 2.0.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | **1.0.2** | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | **1.3.0** | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | **1.4.0** | Estable | Semana del 5 de noviembre |
| EA · Ofelia | **1.0.2** | Estable | Semana del 26 de octubre |
| CCO · Augusto y Valeria | **1.0.0** | Estable | Semana del 5 de noviembre |
| CISO · Alexis, Guillermo y Amparo | **1.0.0** | Estable | Semana del 5 de noviembre |
| Rostrum | **1.0.2** | — | — |

## Para actualizar

```
/plugin marketplace update criterio
```

Cada agente pide aceptar los términos de su versión y deja su comprobante en `.criterio/terminos/`.
