# criterio-finance

Cierre mensual, facturación electrónica y reportes al supervisor, por país.

[English](README.md) · Apache 2.0

**Estado: capacidad declarada, sin construir.** No hay contenido, y en este repositorio no
existe ningún paquete por jurisdicción. Aquí no se construye nada hasta que el alcance se
amplíe deliberadamente — ver [ADR 0005](../../docs/decisions/0005-scope-pmo-only.md).

Lo que está construido hoy es la familia PMO: **Vera** para la oficina de proyectos,
**Samuel** para un proyecto y **Alba** para un producto. La familia entera, con sus comandos
y su estado, en el [README del marketplace](../../README.es.md).

## El problema que va a atacar

**Qué es.** La función que cierra los libros y responde por lo que dicen. Sus componentes son el cierre y la consolidación, las conciliaciones, la contabilidad frente a la base fiscal, el reporte a supervisores y la preparación de auditoría.

**Lo que cuesta hoy**

| Cifra | Fuente |
|---|---|
| **18%** de los contadores comete errores a diario y **59%** varios al mes, por restricciones de capacidad | [Gartner, feb. 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) — 497 contadores, encuesta jul. 2023 |
| Cierre anual: **10 días** los mejores, **18** la mediana, **35** los rezagados | [APQC, abr. 2026](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-up-year-end-close) |
| El cierre trimestral **empeoró**: 49% cerraba en seis días hábiles en 2019, 44% en 2023 | [Ventana Research / ISG, dic. 2023](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) |
| Las horas de programa SOX subieron **32% en dos años**, a 15.580. El **45% de los controles sigue siendo totalmente manual** | [KPMG, *SOX Survey* 2025](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) — ~150 profesionales |

El dato que debería incomodar es el segundo: **el cierre no mejoró en cuatro años**, a pesar de todo lo que se gastó en tecnología.

→ Agente CFO: capacidad declarada, sin construir

---

Cuando esta capacidad se construya, seguirá las mismas reglas que las otras tres: cada dato
con la cita del documento del que salió, declarado y evidenciado sin fusionar, y el agente
callado mientras no haya novedad.
