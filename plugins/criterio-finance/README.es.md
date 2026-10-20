# criterio-finance

Cierre mensual, facturación electrónica y reportes al supervisor, por país.

[English](README.md) · Apache 2.0

**Estado: en diseño.** Es el plugin de **Clara**, la contralora de la familia CFO, que se diseña
para NIIF adoptadas localmente en Colombia y Ecuador, con la factura electrónica de la DIAN y del
SRI ([ADR 0006](../../docs/decisions/0006-scope-cfo.md)). El diseño completo, con sus comandos, sus
señales y su estructura de carpetas, está en
[`families/criterio-cfo/DISENO.es.md`](../../families/criterio-cfo/DISENO.es.md).

Lo que está construido hoy es la familia PMO: **Vera** para la oficina de proyectos,
**Samuel** para un proyecto y **Alba** para un producto. La familia entera, con sus comandos
y su estado, en el [README del marketplace](../../README.es.md).

## El problema que va a atacar

**Qué es.** La función que cierra los libros y responde por lo que dicen. Sus componentes son el cierre y la consolidación, las conciliaciones, la contabilidad frente a la base fiscal, el reporte a supervisores y la preparación de auditoría.

**Lo que cuesta hoy**

<!-- cfo:cifras · generado por scripts/cfo.py; no se edita a mano -->
| Cifra | Fuente |
|---|---|
| **44 %** cerraba el trimestre en seis días hábiles en 2023, contra 49 % en 2019 | [Ventana Research / ISG, investigación Smart Financial Close, 2023](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) — No indicada en la nota |
| **45 %** de los controles SOX son manuales en las organizaciones encuestadas; las horas del programa subieron 32 % en dos años, de 11.800 a 15.580 | [KPMG, SOX Survey, 2025](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) — Cerca de 150 profesionales SOX |
| **18 días** es la mediana del cierre anual; los mejores lo hacen en 10 días o menos y los más lentos en 35 | [APQC, blog del 8 de abril de 2026, y su medida de Open Standards Benchmarking del cierre anual a nivel de sitio, 2026](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-year-end-close) — La nota no la indica; la medida de benchmarking reporta la mediana de 18,0 días con 2.214 organizaciones |
| **18 %** de las personas de la función de contraloría comete errores al menos a diario, y 59 % varios al mes, por restricciones de capacidad | [Gartner, comunicado del 21 de febrero de 2024, 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) — 497 personas de la función de contraloría, encuesta de julio de 2023 |
<!-- /cfo:cifras -->

El dato que debería incomodar es el primero: **el cierre no mejoró en cuatro años**, a pesar de todo lo que se gastó en tecnología.

→ [El diseño de Clara y Tomás](../../families/criterio-cfo/DISENO.es.md)

---

Cuando esta capacidad se construya, seguirá las mismas reglas que la familia PMO: cada dato
con la cita del documento del que salió, declarado y evidenciado sin fusionar, y el agente
callado mientras no haya novedad.
