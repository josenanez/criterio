# Criterio · catálogo 1.0.0 · 28 de octubre de 2026

La familia CSO, la función comercial, entra al marketplace en su versión 0.1.0, como versión de laboratorio y sin lanzar. Y desde esta entrada, tres cosas de cada familia se dicen por separado: su etapa, la dice el código; su calidad, laboratorio o estable, la dice la evidencia; y su lanzamiento, una fecha (decisiones 0020 y 0021). Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** Pasa a la 1.0.0 porque, después de la 0.12, viene el entero siguiente (decisión 0020). No dice nada de ninguna familia: cada una lleva su propia versión.

## Qué trae

| | |
|---|---|
| **CSO 0.1.0** | Augusto, el pronóstico, y Valeria, de la venta a la factura: doce comandos, sus skills y el motor, con las nueve señales. Las exportaciones de Salesforce y de HubSpot, y cualquier CSV o Excel con su mapeo de columnas. El motor pasa su prueba determinista contra la clave de todo su material, seis entidades de Colombia y México con sus controles. La ronda con los agentes llega en la 0.2.0 |
| **Laboratorio o estable** | Lo dice la evidencia, no el número: el piso del margen del 95 % en 95 % o más, en señales y en datos, sobre la corrida más reciente de cada entidad del material, y ningún control con una señal. Lo calcula `scripts/calidad.py` y el registro lo anota en esta entrada |
| **Diez versiones por entero** | De x.0 a x.9, y después la x+1.0. Las correcciones no cuentan entre las diez. La 0.10, la 0.11 y la 0.12 son las únicas excepciones |
| **Se publica desde la primera versión y se lanza en una fecha** | Una familia entra al marketplace y al portal con su primera liberación; se marca «Corre hoy» la semana de su lanzamiento. Una familia lanzada sube a la 1.0.0 en su primera versión estable |

## Las versiones en la 1.0.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | 0.12.1 | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | 0.12.1 | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | 0.12.1 | Estable | Sin lanzar |
| EA · Ofelia | 0.12.1 | Laboratorio | Sin lanzar |
| CSO · Augusto y Valeria | 0.1.0 | Laboratorio | Sin lanzar |
| Rostrum | 0.12.1 | — | — |

En esta entrada solo se libera la CSO. La siguiente versión de la PMO, la CFO, la CLO, la EA y Rostrum es su 1.0.0.

## Si ya la tienes instalada

Nada cambia en las familias que ya usas: su versión y sus términos son los mismos. Para probar la CSO, instala `criterio-sales` o `criterio-revenue`; cada agente te pide aceptar los términos y deja su comprobante en `.criterio/terminos/`.
