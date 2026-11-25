# /criterio-data-quality:lineage-setup datos/901555777-banco-cordillera-sintetico

Ariadna está configurada para Banco Cordillera Sintético (NIT 901555777). En el informe de junta de octubre, tres de las cinco cifras no cuadran con su fuente. Cuál cifra es la correcta lo decide quien firma el informe; Ariadna no las corrige.

**Lo que quedó configurado** (sin preguntas abiertas: tomé las respuestas de los documentos y de la configuración que ya había dejado Custodia):
- **Carpeta:** `datos/901555777-banco-cordillera-sintetico`, la única candidata. Ya estaba marcada, así que no la marqué de nuevo.
- **Periodo:** 2026-11, el mismo de Custodia.
- **Tolerancia:** 0,5 %, tomada de la política de datos.
- **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
- **Términos v1.6:** José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-quality-0.1.0-2026-11-25.md` y `.pdf`.
- **Configuración:** `.criterio/calidad/901555777/config.json`.

**El primer resultado.** Crucé las cinco cifras del informe con `30-calidad/cifras_fuente.xlsx`, al corte 2026-10-31 que declara el informe:

| Indicador | En el informe | En la fuente | Estado |
|---|---|---|---|
| Ventas netas | 9.520.000.000 | 9.400.000,000 | No coincide: 120.000.000 de diferencia, más que el 0,5 % |
| Índice de rotación | 4,2 | — | Sin fuente en el linaje ni en las cifras exportadas |
| Cartera vencida | 1.180.000.000 | 1.250.000.000 | Es la cifra de la fuente al 2026-09-30, un mes antes del corte declarado |
| Clientes activos | 84.200 | 84.200 | Coincide |
| Margen operacional | 3.400.000.000 | 3.400.000.000 | Coincide |

El reporte completo está en `estado-datos/901555777-banco-cordillera-sintetico/calidad/2026-11/reporte-figure-check.md`.

El cálculo del periodo dio 7 señales en total. Además de estas tres, hay un dato crítico sin regla que lo mida, un linaje que se corta, una regla por debajo de su umbral y otra que no corrió. Esas cuatro salen en `/criterio-data-quality:lineage-check` y `/criterio-data-quality:rule-check`.

**Un fallo del motor:** el reporte muestra el Índice de rotación como «4» en dos columnas, aunque el informe dice 4,2 y así quedó en la ficha. La cifra no cambia, pero el reporte la redondea.

**Cuándo vuelvo:** sin reloj. Nadie aprobó la tarea programada en esta prueba, así que no la creé. Para correrlo a mano: `/criterio-data-quality:lineage-wake`.

La corrida quedó registrada como `2026-11-25-lineage-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.