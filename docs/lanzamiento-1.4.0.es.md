# Criterio · catálogo 1.4.0 · 30 de octubre de 2026

La familia comercial cambia de nombre: es la **CCO · La función comercial**, por Chief Commercial Officer (decisión 0022). Abre su 0.3.0 en Ecuador, Perú y Chile, con las exportaciones de Microsoft Dynamics 365 y de Zoho CRM, y pasa a estable. Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** La versión de cada familia es la suya.

## Qué trae

| | |
|---|---|
| **CCO, el nombre de la familia** | Antes era CSO, una sigla que también se lee como Chief Security Officer, la familia de seguridad que viene después. Las entradas 1.0.0 a 1.3.0 del registro siguen selladas como se escribieron; el registro lee su CSO 0.1.0 y 0.2.0 como la CCO |
| **Dynamics 365 Sales y Zoho CRM** | El motor procesa la exportación a Excel de Dynamics por la etiqueta o el nombre lógico de cada columna, y con el estado —abierta, ganada o perdida— por encima de la etapa (F-06, F-07). Procesa también la exportación de negocios de Zoho por la etiqueta de cada campo estándar (F-08, F-09). Cada campo, verificado en su fuente |
| **Ecuador, Perú y Chile** | Material de dos industrias y un control por país, con el RUC de Ecuador y el de Perú, y el RUT de Chile con su dígito: 117 señales sembradas |
| **CCO 0.3.0 · Augusto y Valeria** | La ronda 2, sobre las nueve entidades: 117 de 117 señales y 45 de 45 datos en la primera corrida, con una señal de más en el control de Perú. Era la última actividad de Zoho, que no está entre sus campos estándar: ahora el motor la pregunta y el setup la registra (CCO-4), y la verificación salió sin ninguna. Con las dos rondas, el piso del margen del 95 % es 98,0 % en señales y 95,1 % en datos: estable |

## Las versiones en la 1.4.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | 1.0.0 | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | 1.0.0 | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | 1.0.0 | Estable | Sin lanzar |
| EA · Ofelia | 1.0.0 | Estable | Semana del 26 de octubre |
| CCO · Augusto y Valeria | **0.3.0** | Estable | Sin lanzar |
| Rostrum | 1.0.0 | — | — |

En esta entrada se libera la CCO.

## Si ya la tienes instalada

Actualiza `criterio-sales` y `criterio-revenue`. Cada agente te pide aceptar los términos de su versión nueva y deja su comprobante en `.criterio/terminos/`. Tu configuración sigue en `.criterio/comercial` y `.criterio/ingresos`: el cambio de nombre no la toca.
