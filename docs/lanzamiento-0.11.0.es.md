# Criterio · versión 0.11.0 · 27 de octubre de 2026

Chile entra a la función financiera, y Perú y Chile, a la de contratos y cumplimiento. Cada país entra con su ronda con los agentes, sobre material sintético que ningún agente vio calificado: lo que encontraron se mide contra una clave escrita antes de correr. Código abierto bajo Apache 2.0.

## Qué trae

| Familia | Nuevo en la 0.11.0 |
|---|---|
| **Criterio CFO** · Clara, Tomás y Áurea | **Chile.** La factura electrónica del SII (el DTE) procesada desde su formato oficial, con el RUT y su dígito verificador; el IVA del 19 % y las NIIF que adoptó el Colegio de Contadores, cada uno con su fuente verificada |
| **Criterio CLO** · Fidel y Constanza | **Perú y Chile.** Contratos y cumplimiento de banca, minería y retail con la identificación fiscal de cada país. Una obligación atada a la terminación —el informe final, el acta de liquidación— vence ahora en la terminación vigente, la del último otrosí |

El modelo de lenguaje (LLM) extrae de los documentos escritos; el código calcula las señales; la decisión la toma siempre una persona.

## Lo que está medido

Cada país nuevo tiene dos entidades de industria con defectos sembrados a propósito y una de control, sin ninguno: cualquier señal en ella es una falla.

| | CFO · ronda 5, Chile | CLO · ronda 4, Perú y Chile |
|---|---|---|
| Entidades | 3 | 6 |
| Señales sembradas encontradas | 26 de 26 (margen del 95 %: 87,1–100 %) | 37 de 37 (90,5–100 %) |
| Señales de más | 0 | 0 |
| Datos extraídos correctos | 24 de 24 | 812 de 813 |
| Entidades de control sin ninguna señal | 1 de 1 | 2 de 2 |
| Tokens | 12,7 millones | 21,6 millones, con la repetición |

En la CLO, el único dato que faltó fue la fecha del informe final de un contrato cuyo otrosí movió la terminación (CLO-10). Se corrigió la instrucción de Fidel, se repitió su corrida sobre esa entidad —128 de 128 datos— y las entidades de Chile, corridas ya con la corrección, dieron 132 de 132.

## Dónde está probada cada familia

| Familia | Países | Entidades del material |
|---|---|---|
| CFO | Colombia, Ecuador, Perú y Chile | 12 |
| CLO | Colombia, Ecuador, Perú y Chile | 12 |
| PMO | Seis industrias | — |

**Lo que sigue:** México y Brasil en las dos familias, uno a la vez, por tamaño de mercado; en la PMO, telecomunicaciones y logística (0.12.0). Nada de esto se ha probado todavía sobre la documentación de una organización concreta: ese es el paso que decide la versión 1.0.

## Para quien ya la tiene instalada

Activa una vez la actualización automática: en /plugin, Marketplaces → criterio → Enable auto-update. Cada versión pide aceptar de nuevo los términos, y deja su comprobante.

Las rondas, cada salida y cada defecto con su origen, en [las rondas de la CFO](../tests/evidencias/familias/cfo/RONDAS.md) y [las de la CLO](../tests/evidencias/familias/clo/RONDAS.md).
